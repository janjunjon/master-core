from External.Slack import Slack

# from netCDF.v3.HeavyRainCases.LinearRegression import Model5 as HeavyLinearModel5
# instance = HeavyLinearModel5()
# instance.create()
# instance.correct()

# from netCDF.v3.HeavyRainCases.SDGRegressor import Model5 as HeavySDGModel5
# instance = HeavySDGModel5()
# instance.create()
# instance.correct()

# from netCDF.v3.HeavyRainCases.NonLinearSDGRegressor import Model5 as HeavyNonLinearModel5
# instance = HeavyNonLinearModel5()
# instance.create()
# instance.correct()

from netCDF.v3.Rain.LinearRegression import Model5 as RainLinearModel5
instance = RainLinearModel5()
instance.create()
instance.correct()

Slack.notification(f'correct finished.: {type(instance)}')

from netCDF.v3.Rain.SDGRegressor import Model5 as RainSDGModel5
instance = RainSDGModel5()
instance.create()
instance.correct()

Slack.notification(f'correct finished.: {type(instance)}')

from netCDF.v3.Rain.NonLinearSDGRegressor import Model5 as RainNonLinearModel5
instance = RainNonLinearModel5()
instance.create()
instance.correct()

Slack.notification(f'correct finished.: {type(instance)}')

# SVR

from netCDF.v3.HeavyRainCases.SVR import Model5 as HeavySVRModel5
instance = HeavySVRModel5()
instance.create()
instance.correct()

Slack.notification(f'correct finished.: {type(instance)}')

from netCDF.v3.Rain.SVR import Model5 as RainSVRModel5
instance = RainSVRModel5()
instance.create()
instance.correct()

Slack.notification(f'correct finished.: {type(instance)}')