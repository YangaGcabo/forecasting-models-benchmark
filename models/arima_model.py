"""
ARIMA baseline forecasting model.
"""

from statsmodels.tsa.arima.model import ARIMA

def train_arima(series, order=(1, 1, 1)):
    model = ARIMA(series, order=order)
    return model.fit()
