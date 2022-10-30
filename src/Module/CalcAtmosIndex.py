import numpy as np
import math

class Calculation:
    @classmethod
    def getPotentialTemperature(cls, temp, P0, P):
        # temp: K
        # P0: base pressure, P: pressure, Cp: specific heat at constant pressure
        Rd = 287
        Cp = 1004
        PT = temp * ((P0 / P) ** (Rd /Cp))
        return PT

    @classmethod
    def getEquivalentPotentialTemperature(cls, temp, rh, P0, P):
        # temp: K
        # l: mixing ratio, Cp: specific heat at constant pressure, L: condensation latent heat
        esat =  6.1078 * pow(10, 7.5 * (temp - 273.15)/(237.3 + (temp - 273.15)))
        e = esat * rh / 100
        l = 0.622 * (e / P)
        L = 2.5 * (10**6)
        Rd = 287
        Cp = 1004
        EPT = temp * (math.e ** ((L * l) / (Cp * temp)) * ((P0 / P) ** (Rd /Cp)))
        # EPT = (temp + (temp * L * l) / (Cp * temp)) * ((P0 / P) ** (Rd /Cp))
        return EPT

    @classmethod
    def getDewPointReductionRate(cls, temp, rh):
        # Td: dew point temperature
        esat =  6.1078 * pow(10, 7.5 * (temp - 273.15)/(237.3 + (temp - 273.15)))
        e = esat * rh / 100
        Td = (237.3 * math.log10(6.1078/e)) / (math.log10(e/6.1078) - 7.5)
        return Td

    @classmethod
    def getLCL(cls, temp, rh):
        # Tl: condensation temperature
        Tl = 1 / (1 / (temp - 55) - math.log(rh/100) / 2840) + 55
        LCL = (temp - Tl) / 9.81 * 1000
        return LCL

    @classmethod
    def getSSI(cls, temp500hPa, temp, rh, P0, P):
        # EPT = cls.getEquivalentPotentialTemperature(temp, rh, P0, P)
        PT = cls.getPotentialTemperature(temp, P0, P)
        SSI = temp500hPa - PT
        return SSI