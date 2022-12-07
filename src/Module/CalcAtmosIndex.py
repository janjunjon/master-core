import math
import metpy.calc as calc
import numpy as np

class Calculation:
    # !! Unit of temperature is K !!
    # P0: sea level pressure, Rd: const of dry air, Cp: specific heat at constant pressure
    # DALR: dry adiabatic lapse rate (K/m), L: condensation latent heat
    P0 = 1013.25
    Rd = 287
    Cp = 1004
    DALR = 0.976
    L = 2.5 * (10**6)

    @classmethod
    def getSaturatedWaterVaporPressure(cls, temp):
        ESAT = 6.1078 * pow(10, 7.5 * (temp - 273.15)/(237.3 + (temp - 273.15)))
        return ESAT

    @classmethod
    def getWaterVaporPressure(cls, temp, rh):
        ESAT = cls.getSaturatedWaterVaporPressure(temp)
        E = ESAT * rh / 100
        return E

    @classmethod
    def getMixingRatio(cls, temp, P, rh):
        E = cls.getWaterVaporPressure(temp, rh)
        MR = 0.622 * (E / P)
        return MR

    @classmethod
    def getSaturatedMixingRatio(cls, temp, P):
        ESAT = cls.getSaturatedWaterVaporPressure(temp)
        MR = 0.622 * (ESAT / P)
        return MR

    @classmethod
    def getHeight(cls, temp, P):
        P0 = cls.P0
        height = ((((P0 / P) ** (1 / 5.257)) - 1) * temp) / 0.0065
        return height

    @classmethod
    def getMoistAdiabaticLapseRate(cls, temp, P, rh):
        MR = cls.getMixingRatio(temp, P, rh)
        MALR = cls.DALR / (1 + 0.846 * MR)
        return MALR

    @classmethod
    def getSaturatedAdiabaticLapseRate(cls, temp, P):
        DALR = cls.DALR
        L = cls.L
        ratio = 0.622
        MR = cls.getSaturatedMixingRatio(temp, P)
        Rd = cls.Rd
        Cp = cls.Cp
        SALR = DALR * ((1 + ((L*MR)/(Rd*temp))) / (1 + ((ratio*(L**2)*MR) / (Cp*Rd*(temp**2)))))
        return SALR

    @classmethod
    def getPotentialTemperature(cls, temp, P):
        # temp: K
        P0 = cls.P0
        Rd = cls.Rd
        Cp = cls.Cp
        PT = temp * ((P0 / P) ** (Rd /Cp))
        return PT

    @classmethod
    def getEquivalentPotentialTemperature(cls, temp, rh, P):
        # temp: K
        P0 = cls.P0
        MR = cls.getMixingRatio(temp, P, rh)
        L = cls.L
        Rd = cls.Rd
        Cp = cls.Cp
        EPT = temp * (math.e ** ((L * MR) / (Cp * temp)) * ((P0 / P) ** (Rd /Cp)))
        # EPT = (temp + (temp * L * l) / (Cp * temp)) * ((P0 / P) ** (Rd /Cp))
        return EPT

    @classmethod
    def getDewPointTemperature(cls, temp, rh):
        # Td: dew point temperature
        e = cls.getWaterVaporPressure(temp, rh)
        Td = (237.3 * math.log10(6.1078/e)) / (math.log10(e/6.1078) - 7.5)
        return Td

    @classmethod
    def getCondensationTemperature(cls, temp, rh):
        # Tl: condensation temperature
        Tl = 1 / (1 / (temp - 55) - math.log(rh/100) / 2840) + 55
        return Tl

    @classmethod
    def getLCL(cls, temp, rh):
        # lifted condensation level
        Tl = cls.getCondensationTemperature(temp, rh)
        LCL = (temp - Tl) / 9.81 * 1000
        return LCL

    @classmethod
    def getSSI(cls, temp500hPa, temp850hPa, rh850hPa):
        # SSI: Showalter Stability Index
        DALR = cls.DALR/100
        SALR = cls.getSaturatedAdiabaticLapseRate(temp850hPa, 850)/100
        height850hPa = cls.getHeight(temp850hPa, 850)
        height500hPa = cls.getHeight(temp500hPa, 500)
        LCL = cls.getLCL(temp850hPa, rh850hPa)
        heightUntilLCL = LCL - height850hPa if height850hPa < LCL else 0
        heightFromLCL = height500hPa - LCL if height850hPa < LCL else height500hPa - height850hPa
        temp850hPa -= DALR*heightUntilLCL
        temp850hPa -= SALR*heightFromLCL
        SSI = temp500hPa - temp850hPa
        return SSI

    @classmethod
    def getKI(cls, temp850hPa, temp700hPa, temp500hPa, rh850hPa, rh700hPa):
        # KI: K Index
        Td850hPa = cls.getDewPointTemperature(temp850hPa, rh850hPa)
        Td700hPa = cls.getDewPointTemperature(temp700hPa, rh700hPa)
        temp850hPa -= 273.15
        temp700hPa -= 273.15
        temp500hPa -= 273.15
        KI = (temp850hPa - temp500hPa) + Td850hPa - (temp700hPa - Td700hPa)
        return KI

    @classmethod
    def getParcelProfile(cls, temp, P, rh):
        Td = cls.getDewPointTemperature(temp=temp, rh=rh)
        parcel_profile = calc.parcel_profile(
            pressure=P,
            temperature=temp,
            dewpoint=Td
        )
        return parcel_profile

    @classmethod
    def getEL(cls, temp, P, rh):
        Td = cls.getDewPointTemperature(temp=temp, rh=rh)
        EL = calc.el(
            pressure=P,
            temperature=temp,
            dewpoint=Td,
        )
        return EL

    @classmethod
    def getLFC(cls, temp, P, rh):
        Td = cls.getDewPointTemperature(temp=temp, rh=rh)
        LFC = calc.lfc(
            pressure=P,
            temperature=temp,
            dewpoint=Td,
        )
        return LFC

    @classmethod
    def getCAPE(cls, temp, P, rh):
        Td = cls.getDewPointTemperature(temp=temp, rh=rh)
        parcel_profile = cls.getParcelProfile(temp, P, rh)
        CAPE, CIN = calc.cape_cin(
            pressure=P,
            temperature=temp,
            dewpoint=Td,
            parcel_profile=parcel_profile
        )
        return CAPE, CIN

    @classmethod
    def getVerticalSheer(cls, upperU, upperV, lowerU, lowerV):
        diffU = upperU - lowerU
        diffV = upperV - lowerV
        return diffU, diffV
        