from netCDF.v3.HeavyRainCases.NonLinearSDGRegressor import *
from External.Slack import *
from Exception.Exception import *

class Execution:
    def exec(self):
        try:
            instance = Model1()
            instance.create()
            instance.correct()
            instance = Model2()
            instance.create()
            instance.correct()
            instance = Model3()
            instance.create()
            instance.correct()
            instance = Model4()
            instance.create()
            instance.correct()
            instance = Model5()
            instance.create()
            instance.correct()
            instance = Model6()
            instance.create()
            instance.correct()
        except ExecutionError as e:
            Slack.notification('file: {}, error: {}'.format(__file__, e))

# if __name__ == '__main__':
#     instance = Execution()
#     instance.exec()
#     Slack.notification('file: {}, finished'.format(__file__))