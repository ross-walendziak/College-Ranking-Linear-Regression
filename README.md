# College-Ranking-Linear-Regression
Using Linear Regression to explain college rankings as a function of university faculty attributes

# Project Summary:
* Used simple linear regression to estimate of effect of professor salary, student-to-faculty-ratio and percent female faculty on university ranking.

# Code and Resources Used:
* Python Version: 3.9.3
* Packages: pandas, matplotlib, statsmodels.api, statsmodels.iolib.summary2, seaborn
* Linear Regression Article: https://python.quantecon.org/ols.html
* Text: Introduction to Econometrics, Stock and Watson

# Data Source:
[National Center for Education Statistics (NCES)](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Data%20-%20Gender%20composition%20at%20ranked%20universities.xlsx)

# Exploratory Data Analysis:

* Summary statistics for pertinent variables are present below.

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Descriptive%20Statistics.png)

* The distribtions for university academic ranking and average professor salary are presented below.

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Academic%20Ranking%20Histogram.png)

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Professor%20Salary%20Historgram.png)

* Correlations between independent variables were exampined as well as the correlation between university ranking (dependent) and independent variables.  Some of these relationships are visualized in the scatter plots below.

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Correlation%20Matrix.png)

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Scatter%20-%20Academic%20Rank%20vs%20Explanatory%20Variables.png)

# Model Building:

![](https://github.com/ross-walendziak/College-Ranking-Linear-Regression/blob/main/Graphics/Model%20Results.png)

# Model Performance:
* Model 8 shows the strongest theoretically sound and statistically significant result.
* Two of the remaining three variables hold statistical significance at the 99% confidence and 90% confidence levels.  
* The adjusted R-squared in model 8 is also one of the highest among the models considered, settling at 0.44.  
* Further, the F-statistic, testing the joint significance of all three variables, is 39.68.  This F-stat indicates that we can reject the null hypothesis that all       three variables jointly have no effect on academic ranking by a wide margin (critical value 3.78 at the 1% alpha level).
* Practically, the most useful result is that a $10,000 increase in average professor salary should increase a university’s ranking by about 7.4 ranking positions -     about one third of one standard deviation in the university ranking hierarchy.

# Policy Recommendations:
* University administrations should focus on building their endowments to facilitate the ability to pay the highest earning professors, and more of them (decrease the   student-to-faculty ratio), with the end goal of increasing or retaining university ranking among peer universities.
* University administrators should also be cognizant of the bias towards hiring male faculty members at top notch schools when making faculty hiring decisions.
