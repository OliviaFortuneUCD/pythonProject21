import pandas
import matplotlib
import scipy
import seaborn as sns
df = sns.load_dataset('flights')
print(df.head())
#print first five records from CSV
df.head()
#print(df.head())
print(df.info)

#check if there are missing values
print(df.isna().sum())