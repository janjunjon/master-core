class Discrimination:
    @classmethod
    def getSSIStabilityScore(cls, SSI):
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