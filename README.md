# Predicting-stock-market-index-using-fusion-of-machine-learning-techniques
This project is to determine the future value of the company stock by doing stock market prediction.In this approach we are doing technical analysis using technical indicators with the help of machine learning. Ten technical indicators are selected as the inputs to each of the prediction models. The predictions are made for 1–10, 15 and 30 days in advance. The prediction performance of these hybrid models is compared with the single stage scenarios.
## Technologies Used
- Python
- Machine Learning(Regression Model)
- Deep Learning
## About Dataset
In this 10 years of stock data has been used. Two indices namely CNX Nifty and S&P Bombay Stock Exchange (BSE) Sensex from Indian stock markets are selected for experimental evaluation.nifty.csv and sensex.csv are the raw data downloaded and dataset having 10 technical indicators by using dataset_creation.py and output is paramdataset.csv. techincal indicator used are Simple 10-day moving average, Weighted 10-day moving average, Momentum, Stochastic K%, Stochastic D%, Relative strength index (RSI), Moving average convergence divergence (MACD), Larry William’s R%, A/D (Accumulation/Distribution) oscillator, CCI (Commodity channel index). 
## Description
In this Single stage Approach, Two stage fusion Approach and a Deep learning (lstm) approach has been implemented.
- Single stage Approach-In this approach ten technical indicators which describe t day is the input for models(SVR, ANN and Random Forest) and the output is t+n day closing price.
- Two stage fusion Approach-In first stage SVR is used and its output works as an test input for second stage. In this input is t day data to the SVR and output is t+n day in terms of technical indicator. In second stage train data is same like first stage and test data is the output of stage 1. In second stage SVR, ANN and Random Forest models has been used for prediction.
## Installation
- stock.ipynb is having all the models for prediction for single stage and two stage fusion approches. Single stage approach take input dataset paramdataset.csv.
- Approach2datacreation.ipynb is used for two stage fusion approach, takes input sensexdata.csv and paramdataset.csv. In which for each technical indicator SVR has been applied, which will predict techincal indicator values, gives output in testdata.csv and will become test data for 2nd stage in fusion approach. This testdata.csv become test input for stock.ipynb by which all the 3 models has been applied for 2nd stage in fusion approach
- Stock_Market_prediction.ipynb is used for prediction of closing price with model LSTM, taking input paramdatasetlstm.csv.
