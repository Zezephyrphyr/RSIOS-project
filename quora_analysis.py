import csv
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# initialization
header = []
data = []

# used for

# -------------------------------
# read from the data
with open('quora_user_stats.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = reader.next()
    print header
    for row in reader:
        data.append(row)


followers = []
followings = []

for row in data:
    if int(row[2]) > 100:
        followers.append(int(row[2]))

    if int(row[5]) > 10:
        followings.append(int(row[5]))

# ===============================
# drawing helper function
def draw_plot_hist(x, bins, xlabel, ylabel, title):
    # the histogram of the data
    n, bins, patches = plt.hist(x, bins=bins)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def draw_plot(x, y, xlabel, ylabel):
    print 'test'

draw_plot_hist(followers, 20, 'number of followers', 'user count', 'followers')

#draw_plot_hist(followings, 20, 'number of followings', 'user count', 'Followings distribution Map')
# number of views distribution -- hist

# number of followers distribution -- hist

# number of followings distribution -- hist

# x : views - y :followers: check whether they are positively relative

# views - to other plots

'''
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
'''