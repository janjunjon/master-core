from netCDF.CalcEvaluationIndex import *
from External.Slack import *
from Exception.Exception import *

class Execution:
    def main(self):
        try:
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='Rain/SDGRegressor',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'Rain/SDGRegressor'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='HeavyRainCases/SDGRegressor',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'HeavyRainCases/SDGRegressor'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='Rain/LinearRegression',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'Rain/LinearRegression'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='HeavyRainCases/LinearRegression',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'HeavyRainCases/LinearRegression'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='Rain/NonLinearSDGRegressor',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'Rain/NonLinearSDGRegressor'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='HeavyRainCases/NonlinearSDGRegressor',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'HeavyRainCases/NonLinearSDGRegressor'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='Rain/SVR',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'Rain/SVR'))
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = Eval(
                    dirPath='HeavyRainCases/SVR',
                    pattern=pattern
                )
                instance.main()
            Slack.notification('file: {}, finished: {}'.format(__file__, 'HeavyRainCases/SVR'))
        except ExecutionError as e:
            Slack.notification('ERROR. file: {}, error: {}'.format(__file__, e))

class Execution2:
    def main(self):
        try:
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='Rain/SDGRegressor',
                    pattern=pattern
                )
                instance.main()
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='HeavyRainCases/SDGRegressor',
                    pattern=pattern
                )
                instance.main()
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='Rain/LinearRegression',
                    pattern=pattern
                )
                instance.main()
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='HeavyRainCases/LinearRegression',
                    pattern=pattern
                )
                instance.main()
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='Rain/NonLinearSDGRegressor',
                    pattern=pattern
                )
                instance.main()
            for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
                instance = EvalSpecificRegions(
                    dirPath='HeavyRainCases/NonlinearSDGRegressor',
                    pattern=pattern
                )
                instance.main()
            # for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
            #     instance = EvalSpecificRegions(
            #         dirPath='Rain/SVR',
            #         pattern=pattern
            #     )
            #     instance.main()
            # for pattern in ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6']:
            #     instance = EvalSpecificRegions(
            #         dirPath='HeavyRainCases/SVR',
            #         pattern=pattern
            #     )
            #     instance.main()
        except ExecutionError as e:
            Slack.notification('file: {}, error: {}'.format(__file__, e))