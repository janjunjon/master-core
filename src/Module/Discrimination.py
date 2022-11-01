from Module.CalcAtmosIndex import Calculation as AtmosCalculation

class Discrimination:
    @classmethod
    def getAdiabaticLapseRateStabilityScore(cls, upperTemp, lowerTemp, upperPres, lowerPres):
        DALR = AtmosCalculation.DALR
        SALR = AtmosCalculation.getSaturatedAdiabaticLapseRate(lowerTemp, lowerPres)
        upperHeight = AtmosCalculation.getHeight(upperTemp, upperPres)
        lowerHeight = AtmosCalculation.getHeight(lowerTemp, lowerPres)
        height = upperHeight - lowerHeight
        tempDiff = upperTemp - lowerTemp
        ALR = abs(tempDiff / height * 100)
        if ALR <= SALR:
            SCORE = 0
        elif ALR > SALR and ALR < DALR:
            SCORE = 1
        elif ALR > DALR:
            SCORE = 2
        return SCORE

    @classmethod
    def getSSIScore(cls, SSI):
        # 0: stability, 1: weak unstability, 2: middle unstability, 3: strong unstability, 4: too strong unstability
        if SSI > 0:
            SCORE = 0
        elif SSI > -3:
            SCORE = 1
        elif SSI > -6:
            SCORE = 2
        elif SSI > -9:
            SCORE = 3
        else:
            SCORE = 4
        return SCORE

    @classmethod
    def getKIScore(cls, KI):
        # possibility of thunder
        # 0: 0%, 1: 20%, 2: 20~40%, 3: 40~60%, 4: 60~80%, 5: 80~90%, 6: almost 100%
        if KI <= 15:
            SCORE = 0
        elif KI > 15 and KI <= 20:
            SCORE = 1
        elif KI > 20 and KI <= 25:
            SCORE = 2
        elif KI > 25 and KI <= 30:
            SCORE = 3
        elif KI > 30 and KI <= 35:
            SCORE = 4
        elif KI > 35 and KI <= 40:
            SCORE = 5
        elif KI > 40:
            SCORE = 6
        return SCORE