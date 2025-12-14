"""
LightGBM regression model for forecasting tasks.
"""

from lightgbm import LGBMRegressor

def train_lgbm(X, y):
    model = LGBMRegressor(n_estimators=200)
    model.fit(X, y)
    return model
