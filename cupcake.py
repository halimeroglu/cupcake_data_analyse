#import the pandas module
import pandas as pd

#import the csv file
df = pd.read_csv("cupcake.csv")

#for see first five line of data
df.head()


#add year , month and day columns
def get_year(year):
    return year.split('-')[0]

def get_month(month):
    return month.split('-')[1]

def get_day(day):
    return day.split('-')[2]

df['Year'] = df['Date'].apply(lambda x:get_year(x))
df['Month'] = df['Date'].apply(lambda x:get_month(x))
df['Day'] = df['Date'].apply(lambda x:get_day(x))
df.head()


#q1 : What is the most searched year?
result = df.groupby('Year').sum()
result['Cupcake']

#plot the data
import matplotlib.pyplot as plt

years = [year for year,db in df.groupby('Year')]

plt.bar(years,result['Cupcake'])
plt.xticks(years)
plt.xlabel('Year')
plt.ylabel('Cupcake')
plt.show()


#q2 : What is the most searched month?
result = df.groupby('Month').sum()
result

months = [months for months,db in df.groupby('Month')]

plt.bar(months,result['Cupcake'])
plt.xticks(months)
plt.xlabel('Months')
plt.ylabel('Cupcake')
plt.show()


#q3 : Average in five years
result = df.groupby('Year').mean()
x = round(result['Cupcake'], 2)

years = [year for year,db in df.groupby('Year')]

plt.bar(years,x)
plt.xticks(years)
plt.xlabel('Years')
plt.ylabel('Cupcake')
plt.show()


#q4 : Average of the months
result = df.groupby('Month').mean()
x = round(result['Cupcake'],2)

month = [month for month,df in df.groupby('Month')]
plt.bar(month,x)
plt.xticks(month)
plt.xlabel('Months')
plt.ylabel('Cupcake')
plt.show()


#q5 : Sum of 5 years

result = df.groupby('Year').sum()
sum_of_cupcake = result['Cupcake'].sum()
sum_of_cupcake

