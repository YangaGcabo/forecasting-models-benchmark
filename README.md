# forecasting-models-benchmark
Benchmark and comparison of statistical, machine learning, and deep learning forecasting models using proper time-series cross-validation and engineering-style error analysis.
# Forecasting Models Benchmark

## Purpose
This repository compares different forecasting models under the same data and validation framework.

Instead of chasing accuracy only, the focus is on stability, error behaviour, and interpretability.

## Models Compared
- ARIMA / SARIMAX
- Prophet
- LightGBM with engineered features
- N-BEATS
- Temporal Fusion Transformer (TFT)

## Validation Strategy
- Rolling-origin time-series cross-validation
- No future data leakage
- Residual diagnostics

## Evaluation Metrics
- MAE
- RMSE
- MAPE / SMAPE
- Residual autocorrelation

## Engineering Motivation
In real systems, models must be reliable, not just accurate on one split.

## Tools
Python, Statsmodels, Prophet, LightGBM, PyTorch.

## Author
Yanga Gcabo
