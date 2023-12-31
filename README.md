## Introduction

The data contains weather statistics for Vancouver, which are recorded hourly. The initial data downloaded is for 90,000 hours, roughly 10 years. I am hoping to find trends in the data for the temperatures, especially for extreme weather spikes during the summer and winter. I would like to explore whether these temperature spikes we have been experiencing (like the recent hot days in Vancouver) have happened in the past or if they are unprecedented. The target variable for this project will be temperature. The hope is that this project will help in predicting extreme weather spikes and help the public prepare for them. This project also has the potential to benefit businesses in their sales of seasonal products. This is a multivariate time series project.

Link to Data Download Page:
https://vancouver.weatherstats.ca/download.html

## Observations
* Alone, each variable generally does not have a strong correlation to the temperature. For example, pressure could rise by a few kPa and the temperature would not be affected.
* The one variable that does have a strong correlation with temperature is Dew Point. This was added into the final model after tuning to increase the accuracy of the predictions.
* After the Exploratory Data Analysis and several experiments through different models, the model picked for the temperature predictions is LSTM. This Recurrent Neural Network provided the closest predictions to the hottest and coldest hours in Vancouver. 
* Temperature extremes are still outliers and the model is not able to predict them with complete accuracy. 
* The model does perform well with more common temperatures, even with completely new data. 
* Currently, the model is able to predict the temperature considering the weather statistics from the previous hour. The streamlit app in this repository has a working prototype. 

## Data Dictionary
|       Column        | Data Type | Description                                                            |
|---------------------|-----------|------------------------------------------------------------------------|
| date_time_local     | Date-Time | Index                                                                  |
| pressure_station    | float64   | The station used to measure pressure.                                  |
| pressure_sea        | float64   | The pressure at sea level.                                             |
| wind_dir            | object    | The wind's direction (NSEW).                                           |
| wind_speed          | int64     | The wind speed.                                                        |
| wind_gust           | float64   | Indicator and measurement for wind gust.                               |
| relative_humidity   | int64     | The relative humidity.                                                 |
| dew_point           | float64   | The dew point for the hour.                                            |
| temperature         | float64   | The temperature average for the hour **(Target Variable)**             |
| windchill           | float64   | Calculation for Windchill, shows 0 when temperature is over 0 Celsius. |
| humidex             | float64   | Calculation for Humidex, shows 0 when temperature below 20 Celsius.    |
| visibility          | float64   | Visibility in meters.                                                  |
| health_index        | float64   | The health index number for the hour.                                  |
| cloud_okta          | float64   | Measurement of cloud cover.                                            |
| max_air_temp_pst1hr | float64   | Maximum temperature reached for the hour.                              |
| min_air_temp_pst1hr | float64   | Minimum temperature reached for the hour.                              |

## Documents in this Repository
### Cleaning Folder:
* 1 Excel Clean Log.txt: Log of all cleaning steps taken in Excel.
* 2 Data Cleaning: Jupyter Notebook with all the cleaning steps done through python.
### Exploratory Data Analysis Folder:
* 3 Preliminary EDA Part 1.ipynb: Includes Analysis of Windchill
* 4 Preliminary EDA Part 2.ipynb: Includes Analysis of Humidex
* 5 Preliminary EDA Part 3.ipynb: Includes Monthly, Weekly, and Daily Analysis of Trends, Seasonality, and Residuals.
* 6 Exploratory Data Analysis.ipynb: Analysis of Individual Variables and Correlation
### Modeling and Evaluation:
* 7 Baseline Modeling and Evaluation Metrics: Linear Regression and Vector Autogressive Model
* 7 Modeling - FB Prophet
* 8 Modeling - LSTM
### Sprint Presentations:
* Pedro_Montano_Presentation_Capstone_Sprint_1.pdf
* Pedro_Montano_Presentation_Capstone_Sprint_2.pdf
* Pedro_Montano_Presentation_Capstone_Sprint_3.pdf
### Streamlit_App:
* app.py: Python script for the streamlit app temperature prediction prototype.
* images LSTM, Title, cold, and hot: used as visuals in the demo.
* model_6_1_dew.h5: LSTM model trained with weather statistics from 2013-07-01 through 2020-06-30.
* stdscaler.pkl: Standard Scaler used for the model. Used to scale new inputs for the prediction.

## **Task List**
- [X] Confirmed Dataset "Vancouver Climate Hourly"
- [X] Preliminary cleanup through Excel.
- [X] Additional data cleaning through Python.
- [X] Initial EDA
- [X] Sprint 1
- [X] EDA, analyze correlation between variables
- [X] Split data and fit Linear Regresssion Model
- [X] Fit Vector Autoregressive Model
- [X] Sprint 2
- [X] Research alternative model for Multivariate Time Series Analysis
- [X] Research how to apply the FB Prophet Model to multivariate analysis.
- [X] Fit FB Prophet Model on the data adding regressors for the additional variables.
- [X] Evaluate FB Prophet Model
- [X] Research LSTM (RNN) and how to apply it to this project
- [X] Fit LSTM to the data
- [X] Evaluate LSTM with time series split fro validation
- [X] Fit final model to be used, LSTM had the best results.
- [X] Evaluate the final model on the data using 7 years as training and 3 years as test. 
- [X] Save final model with Dew Point added back in
- [X] Cleaned code.
- [X] Reviewed notes for clarity on all notebooks.
- [X] Added Table of Contents to notebooks 8 and 9.
- [X] Reviewed visualizations and changed colors to be color blind friendly.
- [X] Sprint 3
- [X] Adjust model to accept unscaled weather stats as input.
- [X] Create Application to Showcase Model

## **Next Steps**
- [ ] Pull 10 to 20 more years of data and cleanup. Also add July and August 2023 to the data.
- [ ] Update and train model with new data.
- [ ] Experiment on additional time steps for LSTM to attempt to increase the prediction window for temperature.
- [ ] Continue to research additional models should they be applicable to this multivariate time series analysis.