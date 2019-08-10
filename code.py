# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
data = pd.read_csv(path, delimiter=';')

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
data.fillna('unknown')

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
data.rename({'loan':'previous_loan_status','y':'loan_status'},axis=1,inplace=True)
print(data.columns)
print(data.head())
# Find out the information of the `job` column.
print(data['job'].value_counts())
# Check the `loan_status`  approval rate by `job`
print(data[data['loan_status']=='yes']['job'].value_counts())
# Check the percentage of loan approved by `education`
print(data[data['loan_status']=='yes']['education'].value_counts())
# Check the percentage of loan approved by `previous loan status`
print((data[data['loan_status']=='yes']['loan_status'].count()/data[data['previous_loan_status']=='yes']['loan_status'].count())*100)
# Create a pivot table between `loan_status` and `marital ` with values form `age`
pd.pivot_table(data,index=['loan_status','marital'],values='age')
# Loan status based on marital status whose status is married
print(data[data['marital']=='married']['loan_status'].value_counts())
#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
df_branch_1 = pd.DataFrame({'customer_id':[10,20,30],'first_name':['Ram','Sham','Hari'],'last_name':['Hire','Kale','Gore']})
# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
df_branch_2 = pd.DataFrame({'customer_id':[50,60,70],'first_name':['Sam','Dan','John'],'last_name':['Hat','Kat','Gat']})
# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
df_credit_score = pd.DataFrame({'customer_id':[10,20,30,50,60,70],'score':[200,300,800,700,400,600]})
# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1,df_branch_2],axis=0)
# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
result = pd.merge(df_new,df_credit_score,left_on='customer_id',right_on='customer_id')
print(result)


