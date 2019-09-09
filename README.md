## Building Energy Consumption Physical Model

In this part of the project, a physical model was applied to the buildings gathered for the study presented [here](https://github.com/carlosdavila91/santboi_eda).

This static model provides an approximation of the amount of energy a building may consume based on its physical characteristics (the dimensions of the building and the transmittance values associated with its main envelope), solar radiation and weather data.

To simplify the explantation weather data was selected for one year (2017) and the mean temperature values for each month were used to obtain a Heat Demand value (in kWh per year) for each building.

### Variable processing

The Heat Demand values were processed to obtain a classification of buildings according to their potential energy consumption (low, middle, high). This will lead us to the final part of the project, where this variable will be used as the target variable when applying Machine Learning classification models.

This has only (auto) didactic purposes.

### Exploratory analysis

An exploratory analysis of the variable is presented on the jupyter notebook with the objective of understanding the relation between this new variable and the other ones taken into account for the study.

### Conclusions

* The older and smaller the buildings, the greater the Heat Demand Range.
* The size of the building is the most determining variable. Qualitative variables condition the response of the building in terms of Heating Demand but none is significantly determinative of the rest.
* The strategy will have to be based on this information and produce the greatest reduction in demand, involving the smallest number of buildings and benefiting as many people as possible.
* Multivariable analysis was used to identify a greater number of data entry errors.
