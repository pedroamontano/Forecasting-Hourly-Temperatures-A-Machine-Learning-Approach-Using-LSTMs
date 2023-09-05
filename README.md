## Introduction

The data contains weather statistics for Vancouver, which are recorded hourly. The initial data downloaded is for 90,000 hours, roughly 10 years. I am hoping to find trends in the data for the temperatures, especially for extreme weather spikes during the summer and winter. I would like to explore whether these temperature spikes we have been experiencing (like the recent hot days in Vancouver) have happened in the past or if they are unprecedented. The independent variable for this project will be temperature. The hope is that this project will help in predicting extreme weather spikes and help the public prepare for them. This project also has the potential to benefit stores who chose to provide discounts before a weather spike to maximize sales. This is a time series project.

Link to Data Download Page:
https://www.weatherstats.ca/faq/#term-wind-direction


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
* 2 Capstone Project - Cleaning.ipynb: Jupyter Notebook with all the cleaning steps done through python.
### Exploratory Data Analysis Folder:
* 3 Capstone - Preliminary EDA Part 1.ipynb: Includes Analysis of Windchill
* 4 Capstone - Preliminary EDA Part 2.ipynb: Includes Analysis of Humidex
* 5 Capstone - Preliminary EDA Part 3.ipynb: Includes Monthly, Weekly, and Daily Analysis of Trends, Seasonality, and Residuals.
* 6 Capstone - EDA and Baseline Model
### Modeling and Evaluation:
* 7 Modeling - FB Prophet
* 8 Modeling - LSTM
### Sprint Presentations:
* Pedro_Montano_Presentation_Capstone_Sprint_1.pdf
* Pedro_Montano_Presentation_Capstone_Sprint_2.pdf

**Tasks**
- [X] Confirmed Dataset "Vancouver Climate Hourly"
- [X] Preliminary cleanup through Excel.
- [X] Additional data cleaning through Python.
- [X] Initial EDA
- [X] Sprint 1
- [X] EDA, analyze correlation between variables
- [X] Split data and fit Linear Regresssion Model
- [X] Fit Vector Autoregressive Model
- [X] Sprint 2
- [ ] Research VAR parameter tuning
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
