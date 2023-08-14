**Introduction**

The data contains weather statistics for Vancouver, which are recorded hourly. The initial data downloaded is for 90,000 hours, roughly 10 years. I am hoping to find trends in the data for the temperatures, especially for extreme weather spikes during the summer and winter. I would like to explore whether these temperature spikes we have been experiencing (like the recent hot days in Vancouver) have happened in the past or if they are unprecedented. The independent variable for this project will be temperature. The hope is that this project will help in predicting extreme weather spikes and help the public prepare for them. This project also has the potential to benefit stores who chose to provide discounts before a weather spike to maximize sales. This is a time series project.

Link to Data Download Page:
https://www.weatherstats.ca/faq/#term-wind-direction


**Data Dictionary**
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


**Tasks**
- [X] Confirmed Dataset "Vancouver Climate Hourly"
- [X] Preliminary cleanup through Excel.
- [X] Additional data cleaning through Python.
- [X] Initial EDA
- [ ] Collect and process more data
- [ ] EDA, analyze correlation between variables
- [ ] Split data and train AR model
- [ ] Evaluate models
