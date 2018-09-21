import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

%cd 'C:/Users/Noah/DDW/open_data/StudentLoan/student_loan_landscape'

with open('debt_amt_distribution2014.csv') as f:
    df = pd.read_csv(f)

df.NumberOfBorrowers = df.NumberOfBorrowers.str.replace(',','')
df.NumberOfBorrowers = pd.to_numeric(df.NumberOfBorrowers)
df.Balance2014 = df.Balance2014.astype('category')

cols=['(1, 5,000)','[5,000, 10,000)','[10,000, 25,000)','[25,000, 50,000)',
      '[50,000, 75,000)', '[75,000, 100,000)','[100,000, 150,000)',
      '[150,000, 200,000)','[200,000, +)']

df.Balance2014 = cols


sns.set_palette("Set1", n_colors=9, desat=.5)

ylabels = ['','2,000,000','4,000,000','6,000,000','8,000,000', '10,000,000',
           '12,000,000', '14,000,000']

sns.set_style("whitegrid")
ax = sns.barplot(x='Balance2014', y='NumberOfBorrowers', data=df)
plt.xticks(rotation=45, horizontalalignment='right', fontsize=11.0)
plt.title('Distribution of Student Loan Debt Balance 2014', fontsize=14.0)
plt.ylabel('Number of Borrowers', fontsize=12.5)
locs, labels = yticks()
plt.yticks(locs,ylabels)
plt.xlabel('Amount of Debt', fontsize=12.5)
plt.subplots_adjust(bottom=0.25)


with open('non_mort_balance.csv') as f:
    df = pd.read_csv(f, header=None)
df.set_index(0, drop=True, inplace=True)
df = df.T
df.reset_index(drop=True, inplace=True)
df.Year = df.Year.str.replace(',','')
df.Year = pd.to_numeric(df.Year)
df = df.iloc[:44,:]
df['Time'] = pd.date_range('2004','2015', freq='Q')
df.drop(['Year','Quarter'], axis=1, inplace=True)

for i in df.columns[:5]:
    df[i] = df[i].str.replace(',','')
    df[i] = pd.to_numeric(df[i])
    
df.set_index('Time', inplace=True)

#df = pd.melt(df, id_vars=['Time'], value_vars=['HELOC', 'Auto Loan', 
#                'Credit Card', 'Student Loan', 'Other'], value_name='Debt',
#                var_name='Debt Type') 

#df = test.sort_values(by='Time').reset_index(drop=True)
#df.loc[:,'Debt'] = df.Debt.str.replace(',','')
#df.loc[:,'Debt'] = pd.to_numeric(df.Debt)
#df['Debt Type'] = df['Debt Type'].astype('category')

matplotlib.style.use('ggplot')

df.plot()
plt.legend(loc='best', title=None)
plt.title('Non-Mortgage Debt Balances')
plt.xticks(horizontalalignment='left', fontsize=11)
plt.xlabel('')
plt.ylabel('Dollars (Billions)', fontsize=12.5)
