import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (11, 5)  #set default figure size
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col
import seaborn as sn


pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 50)

#Load School Ranking Data
ranking = pd.read_excel(r"C:\Users\Ross Walendziak\Documents\Econometrics\Assignment 5\Data - Gender composition at ranked universities.xlsx", \
                        usecols=['Academic_ranking_rescaled', 'Faculty_total', 'EconFaculty_total', 'Faculty_female', 'ProfSalary_average', 'Student_faculty_ratio'])
#ranking.rename(columns={'AcceptanceRate_NumberAdmits_divided_by_NumberApplicants': 'AcceptRate'}, inplace=True)

#Create New Variables for regression
ranking['const'] = 1.0
ranking['Percent_Econ_Faculty'] = 100*(ranking['EconFaculty_total'] / ranking['Faculty_total'])
ranking['Percent_Female_Faculty'] = 100*(ranking['Faculty_female'] / ranking['Faculty_total'])
ranking['Avg_Prof_Salary_10k'] = ranking['ProfSalary_average']/10000

print (ranking)

#Create 5 models to regress on University Ranking
model1 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k']]).fit(cov_type='HC3')
model2 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Student_faculty_ratio']]).fit(cov_type='HC3')
model3 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Percent_Econ_Faculty']]).fit(cov_type='HC3')
model4 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Percent_Female_Faculty']]).fit(cov_type='HC3')
model5 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Student_faculty_ratio']]).fit(cov_type='HC3')
model6 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Percent_Female_Faculty']]).fit(cov_type='HC3')
model7 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Percent_Econ_Faculty']]).fit(cov_type='HC3')
model8 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Percent_Female_Faculty', 'Student_faculty_ratio']]).fit(cov_type='HC3')
model9 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Percent_Econ_Faculty', 'Percent_Female_Faculty']]).fit(cov_type='HC3')
model10 = sm.OLS(endog=ranking['Academic_ranking_rescaled'], exog=ranking[['const', 'Avg_Prof_Salary_10k', 'Percent_Econ_Faculty', 'Percent_Female_Faculty', 'Student_faculty_ratio']]).fit(cov_type='HC3')



#Creates Summary Table of models 1-5
info_dict={'No. observations' : lambda x: f"{int(x.nobs):d}"}
results_table = summary_col(results=[model1, model2, model3, model4, model5, model6, model7, model8],
                            float_format='%0.6f',
                            stars = True,
                            model_names=['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5', 'Model 6', 'Model 7', 'Model 8'],
                            info_dict=info_dict,
                            regressor_order=['Avg_Prof_Salary_10k', 'Student_faculty_ratio', 'Percent_Econ_Faculty', 'Percent_Female_Faculty'],
                            drop_omitted=True)
results_table.add_title('OLS Regression: University Academic Ranking as a Function of Faculty Attributes')
print (results_table)

#Descriptive Stats
des = ranking.describe()
des.loc['skew'] = ranking.skew().tolist()
des = des.transpose()
des = des[['mean', 'std', 'skew', 'min', '25%', '50%', '75%', 'max']]
print (des)

#Historgrams for University Ranking and Average professor Salary
RankBins = pd.cut(ranking['Academic_ranking_rescaled'], \
                     bins=[0,10,20,30,40,50,60,70,80,90,100],\
                     right=True,\
                     labels=['0-10', '10-20', '20-30', '30-40', '40-50',\
                             '50-60', '60-70', '70-80', '80-90', '90-100']\
                  ).value_counts().sort_index(ascending=True).reset_index()
RankBins.rename(columns={'index': 'ranking_range'}, inplace=True)
RankLabels = (RankBins['ranking_range']).to_list()

x_labels = [i for i, _ in enumerate(RankLabels)]
plt.bar(x_labels, RankBins['Academic_ranking_rescaled'], color='blue')
plt.xlabel('Academic Ranking', fontsize=20)
plt.ylabel('Academic Ranking Frequency', fontsize=20)
plt.title('Academic Ranking in the Year 2015', fontsize=25)
plt.xticks(x_labels, RankLabels, fontsize=15)
plt.annotate("n = 98 Universities",\
             xy = (0, -0.11),\
             xycoords='axes fraction',\
             ha='left',\
             va="center",\
             fontsize=15)
plt.annotate("Highest ranking is 100, Lowest ranking is 1",\
             xy = (0, -0.15),\
             xycoords='axes fraction',\
             ha='left',\
             va="center",\
             fontsize=15)
plt.show()

SalaryBins = pd.cut(ranking['ProfSalary_average'], \
                     bins=[85000,95000,105000,115000,125000,135000,145000,155000,165000,175000,185000,195000,205000],\
                     right=True,\
                     labels=['85k-95k', '95k-105k', '105k-115k', '115k-125k', '125k-135k', '135k-145k',\
                             '145k-155k', '155k-165k', '165k-175k', '175k-185k', '185k-195k', '195k-205k']\
                  ).value_counts().sort_index(ascending=True).reset_index()
SalaryBins.rename(columns={'index': 'salary_range'}, inplace=True)
SalaryLabels = (SalaryBins['salary_range']).to_list()

x_labels = [i for i, _ in enumerate(SalaryLabels)]
plt.bar(x_labels, SalaryBins['ProfSalary_average'], color='green')
plt.xlabel('Average Professor Salary', fontsize=20)
plt.ylabel('Average Professor Salary Frequency', fontsize=20)
plt.title('Average Professor Salary at 98 Top Universities for the Year 2015', fontsize=25)
plt.xticks(x_labels, SalaryLabels, fontsize=15)
plt.annotate("n = 98 Universities",\
             xy = (0, -0.11),\
             xycoords='axes fraction',\
             ha='left',\
             va="center",\
             fontsize=15)
plt.show()

#Scatter 4-plot in one chart: Academic Rankings vs [Salary, PercentEconFaculty, PercentFemaleFaculty, Student Faculty Ratio]
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.scatter(x = ranking['ProfSalary_average'], y = ranking['Academic_ranking_rescaled'])
ax1.set_xlabel("Average Professor Salary")
ax1.set_ylabel("Academic Ranking")
ax1.set(title='Academic Ranking vs Professor Salary')

ax2.scatter(x = ranking['Student_faculty_ratio'], y = ranking['Academic_ranking_rescaled'])
ax2.set_xlabel("Student Faculty Ratio")
ax2.set_ylabel("Academic Ranking")
ax2.set(title='Academic Ranking vs Student Faculty Ratio')

ax3.scatter(x = ranking['Percent_Econ_Faculty'], y = ranking['Academic_ranking_rescaled'])
ax3.set_xlabel("Percent of Faculty in the Economics Department")
ax3.set_ylabel("Academic Ranking")
ax3.set(title='Academic Ranking vs Percent Econ Faculty')

ax4.scatter(x = ranking['Percent_Female_Faculty'], y = ranking['Academic_ranking_rescaled'])
ax4.set_xlabel("Percent of Faculty who are Female")
ax4.set_ylabel("Academic Ranking")
ax4.set(title='Academic Ranking vs Percent Female Faculty')
plt.show()

#Create Correlation Matrix for Variables
corrData = ranking[['Academic_ranking_rescaled', 'Avg_Prof_Salary_10k', 'Student_faculty_ratio', 'Percent_Econ_Faculty', 'Percent_Female_Faculty']]
corrMatrix = corrData.corr()
sn.heatmap(corrMatrix, annot=True)
plt.title('Correlation between Academic Ranking and Explanatory Variables', fontsize=25)
plt.show()

print (model8.summary())