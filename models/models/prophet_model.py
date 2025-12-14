"""
Prophet forecasting model for trend and seasonality.
"""

from prophet import Prophet

def train_prophet(df):
    model = Prophet()
    model.fit(df)
    return model
