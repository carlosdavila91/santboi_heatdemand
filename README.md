# Sant Boi Building Renovation Strategy (II)

This is the second part of the Sant Boi project ([See univariate EDA here](https://github.com/carlosdavila91/santboi_eda)).

It consists of a multivariate analysis to understand the relationship between the physical conditions of buildings (including variables related to location and year of construction) and a Heat Demand estimation associated to each one of the buildings within the scope.

## Building Energy Consumption Physical Model

Heat Demand estimations were obtained through a physical static model. This model provides an approximation of the amount of energy a building may consume based on its physical characteristics (the dimensions of the building and the transmittance values associated with its main envelope surfaces), and also solar radiation and weather data.

Weather data was selected for one year (2017) and the mean temperature values for each month were used to obtain a Heat Demand value (in kWh per year) for each building.

Credits to [Serra Florensa and Coch Roura](https://books.google.es/books/about/Arquitectura_y_energ%C3%ADa_natural.html?id=p_zMDwAAQBAJ&source=kp_book_description&redir_esc=y) for the Heat Demand Model.

## Variable processing (feature engineering?)

The Heat Demand values were processed to obtain a classification of buildings according to their potential energy consumption: low, middle or high.

## Multivariate Exploratory analysis

An exploratory analysis of the variable is presented on the jupyter notebook with the objective of understanding the relation between the target and the other variables taken into account for the study.

This is a key step to get insights from the natural groups that arise from data.

[Download the html notebook version](https://github.com/carlosdavila91/santboi_heatdemand/blob/master/heat_demand.html) for a more friendly readablity. Otherwise see the the jupyter notebook with the full code.

## Conclusions

* The older and smaller the buildings, the greater the Heat Demand Range.
* The size of the building is the most determining variable. Qualitative variables condition the response of the building in terms of Heating Demand but none is significantly determinative of the rest.
* A energy saving strategy should have to be based on this information and produce the greatest reduction in demand, involving the smallest number of buildings and benefiting as many people as possible.
* Multivariable analysis was used to identify a greater number of data entry errors.
