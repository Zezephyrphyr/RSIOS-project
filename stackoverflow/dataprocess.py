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
def getScatterPlot(xlabel,ylabel):
    plt.scatter(df_5[xlabel],df_5[ylabel])
    plt.scatter(df_5_10[xlabel],df_5_10[ylabel])
    plt.scatter(df_10_50[xlabel], df_10_50[ylabel])
    plt.scatter(df_50_100[xlabel],df_50_100[ylabel])
    plt.scatter(df_100_200 [xlabel],df_100_200[ylabel])
    plt.scatter(df_200_500 [xlabel],df_200_500[ylabel])
    plt.scatter(df_500_1k[xlabel],df_500_1k[ylabel])
    plt.scatter(df_1k_2k[xlabel],df_1k_2k[ylabel])
    plt.scatter(df_2k_5k[xlabel],df_2k_5k[ylabel])
    plt.scatter(df_5k_10k[xlabel],df_5k_10k[ylabel])
    plt.scatter(df_10k_20k[xlabel],df_10k_20k[ylabel])
    plt.scatter(df_20k_50k[xlabel],df_20k_50k[ylabel])
    plt.scatter(df_50k_100k[xlabel],df_50k_100k[ylabel])
    plt.scatter(df_100k_500k[xlabel],df_100k_500k[ylabel])
    plt.scatter(df_500k[xlabel],df_500k[ylabel])
    plt.xlabel(xlabel)
    plt.ylabel('Number of '+ylabel)

    plt.show()


def getBoxPlot(label):
    plt.boxplot([df_5[label], df_5_10[label], df_10_50[label],
             df_50_100[label], df_100_200[label], df_200_500[label],
             df_500_1k[label], df_1k_2k[label],df_2k_5k[label],
             df_5k_10k[label], df_10k_20k[label],df_20k_50k[label],
             df_50k_100k[label],df_100k_500k[label],df_500k[label]
             ],
            labels = ['<5','5-10', '10-50',
            '50-100','100-200', '200-500',
            '500-1k','1k-2k','2k-5k',
            '5k-10k','10k-20k','20k-50k',
            '50-100k','100k-500k','>500k'],)
    plt.ylabel(label)
    plt.xlabel('Reputation')
    plt.show()

def scatterDifferencePlot(xLabel,yAttribute1, yAttribute2):
    plt.scatter(df_5[xLabel],df_5[yAttribute1]-df_5[yAttribute2])
    plt.scatter(df_5_10[xLabel],df_5_10[yAttribute1]-df_5_10[yAttribute2])
    plt.scatter(df_10_50[xLabel], df_10_50[yAttribute1]-df_10_50[yAttribute2])
    plt.scatter(df_50_100[xLabel],df_50_100[yAttribute1]-df_50_100[yAttribute2])
    plt.scatter(df_100_200 [xLabel],df_100_200[yAttribute1]-df_100_200[yAttribute2])
    plt.scatter(df_200_500 [xLabel],df_200_500[yAttribute1]-df_200_500[yAttribute2])
    plt.scatter(df_500_1k[xLabel],df_500_1k[yAttribute1]-df_500_1k[yAttribute2])
    plt.scatter(df_1k_2k[xLabel],df_1k_2k[yAttribute1]-df_1k_2k[yAttribute2])
    plt.scatter(df_2k_5k[xLabel],df_2k_5k[yAttribute1]-df_2k_5k[yAttribute2])
    plt.scatter(df_5k_10k[xLabel],df_5k_10k[yAttribute1]-df_5k_10k[yAttribute2])
    plt.scatter(df_10k_20k[xLabel],df_10k_20k[yAttribute1]-df_10k_20k[yAttribute2])
    plt.scatter(df_20k_50k[xLabel],df_20k_50k[yAttribute1]-df_20k_50k[yAttribute2])
    plt.scatter(df_50k_100k[xLabel],df_50k_100k[yAttribute1]-df_50k_100k[yAttribute2])
    plt.scatter(df_100k_500k[xLabel],df_100k_500k[yAttribute1]-df_100k_500k[yAttribute2])
    plt.scatter(df_500k[xLabel],df_500k[yAttribute1]-df_500k[yAttribute2])
    plt.xlabel(xLabel)
    plt.ylabel('Number of Differences of '+yAttribute1 + " and "+yAttribute2)

    plt.show()

def differenceBoxPlot(attribute1, attribute2):
    plt.boxplot([df_5[attribute1]-df_5[attribute2],
             df_5_10[attribute1]-df_5[attribute2],
             df_10_50[attribute1]-df_10_50[attribute2],
             df_50_100[attribute1]-df_50_100[attribute2],
             df_100_200[attribute1]-df_100_200[attribute2],
             df_200_500[attribute1]-df_200_500[attribute2],
             df_500_1k[attribute1]-df_500_1k[attribute2],
             df_1k_2k[attribute1]-df_1k_2k[attribute2],
             df_2k_5k[attribute1]-df_2k_5k[attribute2],
             df_5k_10k[attribute1]-df_5k_10k[attribute2],
             df_10k_20k[attribute1]-df_10k_20k[attribute2],
             df_20k_50k[attribute1]-df_20k_50k[attribute2],
             df_50k_100k[attribute1]-df_50k_100k[attribute2],
             df_100k_500k[attribute1]-df_100k_500k[attribute2],
             df_500k[attribute1]-df_500k[attribute2]
             ],
            labels = ['<5','5-10', '10-50',
            '50-100','100-200', '200-500',
            '500-1k','1k-2k','2k-5k',
            '5k-10k','10k-20k','20k-50k',
            '50-100k','100k-500k','>500k'],)
    plt.ylabel('Number of '+attribute1+ "-"+attribute2)
    plt.xlabel('Reputation')
    plt.show()

getScatterPlot('reputation','UpVotes')
getScatterPlot('reputation','NumberOFAnswers')
getBoxPlot('UpVotes')
differenceBoxPlot('UpVotes','DownVotes')
scatterDifferencePlot('reputation','UpVotes','DownVotes')
getBoxPlot('NumberOFAnswers')

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
