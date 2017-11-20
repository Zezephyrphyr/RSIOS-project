import csv
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

# -------------------------------
# initialization
header = []
data = []

# used for data filter
edits_threshold = 0
followers_threshold = -1
questions_threshold = 0
following_threshold = 0
blogs_threshold = 0
posts_threshold = 0
topics_threshold = 0
answers_threshold = 0
views_threshold = -1


# -------------------------------
# parse helper function
def text_to_num(text):
    d = {
        'k': 3,
        'K': 3,
        'm': 6,
        'M': 6,
        'b': 9,
        'B': 9
    }
    if text == None or len(text)== 0:
        return 0
    elif text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return float(Decimal(num) * 10 ** d[magnitude])
    else:
        return float(Decimal(text))
# read from the data
with open('quora_user_stats.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    header = reader.next()
    header = header[0].split(",")
    print header
    for row in reader:
        data.append(row)

parsedData = {
    'username': [],
    'edits': [],
    'followers': [],
    'name': [],
    'questions': [],
    'following': [],
    'blogs': [],
    'posts': [],
    'topics': [],
    'answers': [],
    'views':[],
    'address': []
}

for row in data:
    #print row
    parsedData['username'].append(row[0])
    parsedData['edits'].append(int(row[1]))

    # followers
    if int(row[2]) > followers_threshold:
        parsedData['followers'].append(int(row[2]))

    parsedData['name'].append(row[3])
    parsedData['questions'].append(int(row[4]))
    if int(row[5]) > following_threshold:
        parsedData['following'].append(int(row[5]))

    parsedData['blogs'].append(int(row[6]))
    parsedData['posts'].append(int(row[7]))
    parsedData['topics'].append(int(row[8]))
    parsedData['answers'].append(int(row[9]))

    nViews = text_to_num(row[10])
    if text_to_num(row[10]) > views_threshold:
        parsedData['views'].append(nViews)

    addr = ""
    for i in row[11:]:
        addr += i
    parsedData['address'].append(addr)


# ===============================
# drawing helper function
def draw_plot_hist(x, bins, xlabel, ylabel, title, i):
    # the histogram of the data
    plt.figure(i)
    n, bins, patches = plt.hist(x, bins=bins)
    for i in range(len(n)):
        plt.text(bins[i], n[i], str(int(n[i])))

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


def draw_plot_scatter(x, y, xlabel, ylabel, title):
    plt.figure(title)
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
# ===============================
# Draw all distribution maps
# header fields: ['username', 'edits', 'followers', 'name', 'questions', 'following', 'blogs', 'posts', 'topics', 'answers', 'views', 'addr']
#                   0           1           2          3        4           5           6         7         8       9           10      11
hist_drawing_settings = [False, False, False, False, False, False, False, False, False, False, False, False]
distribution_size = 20

# number of views distribution -- hist
print header
for i in range(len(header)):
    print hist_drawing_settings[i]
    if hist_drawing_settings[i]:
        print header[i]
        draw_plot_hist(parsedData[header[i]], distribution_size, 'Number of ' + header[i], 'Number of Users','Distribution Map of '+header[i], i)

print len(parsedData['views'])
print len(parsedData['followers'])
# x : views - y :followers: check whether they are positively relative
draw_plot_scatter(parsedData['views'], parsedData['followers'], 'Number of views', 'Number of followers', 'Views & Followers Relationship')
draw_plot_scatter(parsedData['views'], parsedData['questions'], 'Number of views', 'Number of questions', 'Views & Questions Relationship')
draw_plot_scatter(parsedData['views'], parsedData['posts'], 'Number of views', 'Number of posts', 'Views & Posts Relationship')
draw_plot_scatter(parsedData['views'], parsedData['edits'], 'Number of views', 'Number of edits', 'Views & Edits Relationship')
draw_plot_scatter(parsedData['views'], parsedData['blogs'], 'Number of views', 'Number of blogs', 'Views & Blogs Relationship')
draw_plot_scatter(parsedData['views'], parsedData['answers'], 'Number of views', 'Number of answers', 'Views & Answers Relationship')
draw_plot_scatter(parsedData['views'], parsedData['topics'], 'Number of views', 'Number of topics', 'Views & Topics Relationship')

draw_plot_scatter(parsedData['followers'], parsedData['questions'], 'Number of followers', 'Number of questions', 'followers & Questions Relationship')
draw_plot_scatter(parsedData['followers'], parsedData['posts'], 'Number of followers', 'Number of posts', 'followers & Posts Relationship')
draw_plot_scatter(parsedData['followers'], parsedData['edits'], 'Number of followers', 'Number of edits', 'followers & Edits Relationship')
draw_plot_scatter(parsedData['followers'], parsedData['blogs'], 'Number of followers', 'Number of blogs', 'followers & Blogs Relationship')
draw_plot_scatter(parsedData['followers'], parsedData['answers'], 'Number of followers', 'Number of answers', 'followers & Answers Relationship')
draw_plot_scatter(parsedData['followers'], parsedData['topics'], 'Number of followers', 'Number of topics', 'followers & Topics Relationship')


# views - to other plots

plt.show()