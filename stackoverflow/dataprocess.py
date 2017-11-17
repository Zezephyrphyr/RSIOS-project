import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import seaborn as sns

df_5 = pd.read_csv('Rep_<5.csv')
df_5_10 = pd.read_csv('Rep_5-10.csv')
df_10_50 = pd.read_csv('Rep_10-50.csv')
df_50_100 = pd.read_csv('Rep_50-100.csv')
df_100_200 = pd.read_csv('Rep_100-200.csv')
df_200_500 = pd.read_csv('Rep_200-500.csv')
df_500_1k = pd.read_csv('Rep_500-1000.csv')
df_1k_2k = pd.read_csv('Rep_1000-2000.csv')
df_2k_5k = pd.read_csv('Rep_2000-5000.csv')
df_5k_10k = pd.read_csv('Rep_5000-10000.csv')
df_10k_20k = pd.read_csv('Rep_10000-20000.csv')
df_20k_50k = pd.read_csv('Rep_20000-50000.csv')
df_50k_100k = pd.read_csv('Rep_50000-100000.csv')
df_100k_500k = pd.read_csv('Rep_100000-500000.csv')
df_500k = pd.read_csv('Rep_>500000.csv')

#getattributenames
print (df_5.keys())

#Index(['id', 'DisplayName', 'reputation', 'UpVotes', 'DownVotes', 'views',
      # 'CreationDate', 'Age', 'LastAccessDate', 'NumberOFAnswers',
     #  'NumberOFQuestions'],
     # dtype='object')

#hist
plt.hist(df_5['Age'].dropna(), alpha=0.9, bins=7)
plt.xlabel('age')
plt.show()

#scatter plot
plt.scatter(df_10_50['reputation'], df_10_50['UpVotes'])
plt.scatter(df_50_100['reputation'],df_50_100['UpVotes'])
plt.scatter(df_100_200 ['reputation'],df_100_200['UpVotes'])
plt.scatter(df_500_1k['reputation'],df_500_1k['UpVotes'])
plt.scatter(df_1k_2k['reputation'],df_1k_2k['UpVotes'])
plt.scatter(df_2k_5k['reputation'],df_2k_5k['UpVotes'])
plt.scatter(df_2k_5k['reputation'],df_2k_5k['UpVotes'])
plt.scatter(df_5k_10k['reputation'],df_5k_10k['UpVotes'])
plt.scatter(df_10k_20k['reputation'],df_10k_20k['UpVotes'])
plt.scatter(df_20k_50k['reputation'],df_20k_50k['UpVotes'])
plt.scatter(df_50k_100k['reputation'],df_50k_100k['UpVotes'])
plt.scatter(df_100k_500k['reputation'],df_100k_500k['UpVotes'])
plt.scatter(df_500k['reputation'],df_500k['UpVotes'])
plt.xlabel('Reputation Score')
plt.ylabel('Number of Upvotes')

plt.show()


plt.boxplot([df_5["UpVotes"], df_5_10["UpVotes"], df_10_50["UpVotes"],
             df_50_100["UpVotes"], df_100_200["UpVotes"], df_200_500["UpVotes"],
             df_500_1k["UpVotes"], df_1k_2k["UpVotes"],df_2k_5k["UpVotes"],
             df_5k_10k["UpVotes"], df_10k_20k["UpVotes"],df_20k_50k["UpVotes"],
             df_50k_100k["UpVotes"],df_100k_500k["UpVotes"],df_500k["UpVotes"]
             ],
            labels = ['<5','5-10', '10-50',
            '50-100','100-200', '200-500',
            '500-1k','1k-2k','2k-5k',
            '5k-10k','10k-20k','20k-50k',
            '50-100k','100k-500k','>500k'],)
plt.show()


"""

cdf = pd.concat([df_5, df_5_10,
                 df_10_50,df_50_100,
                 df_100_200,df_200_500, df_500_1k,
                 df_1k_2k,df_2k_5k,df_5k_10k, df_10k_20k,
                 df_20k_50k,df_50k_100k,df_100k_500k,df_500k
                 ])

df_5.boxplot(by = 'UpVotes', meanline=True, showmeans=True, showcaps=True, showbox=True,
                 showfliers=False, return_type='axes')
df_5_10.boxplot(by = 'UpVotes', meanline=True, showmeans=True, showcaps=True, showbox=True,
                 showfliers=False,ax=ax)

mdf = pd.melt(df_5, id_vars=['reputation'], var_name=['UpVotes'])
print(mdf.head())
"""
