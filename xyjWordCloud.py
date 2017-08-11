
# coding: utf-8

# In[4]:

from pyecharts import Bar
attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [100.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [50.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render()


# In[1]:

import pandas as pd
import numpy as np

from pyecharts import Bar

index = pd.date_range('3/8/2017', periods=6, freq='M')
df1 = pd.DataFrame(np.random.randn(6), index=index)
df2 = pd.DataFrame(np.random.randn(6), index=index)

dtvalue1 = [i[0] for i in df1.values]
dtvalue2 = [i[0] for i in df2.values]

bar = Bar('Bar chart', 'Profit and loss situation')
bar.add('profit', df1.index, dtvalue1)
bar.add('loss', df2.index,  dtvalue2)
bar.render()


# In[4]:

from pyecharts import WordCloud
import sys
reload(sys)
sys.setdefaultencoding("utf8")

fr = open('xyj.txt', 'r')
characters = []
stat = {}

for line in fr:
    line = line.strip()
    if len(line) == 0:
        continue
    line = unicode(line)
    for x in xrange(0, len(line)):
        if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
            continue
        if not line[x] in characters:
            characters.append(line[x])
        if not stat.has_key(line[x]):
            stat[line[x]] = 0
        stat[line[x]] += 1
value = []
name = stat.keys()
for x in xrange(0,len(name)):
    value.append(stat[name[x]])
fr.close()
# name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
#         'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
#         'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
#         'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
# value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
#          550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=2600, height=1240)
wordcloud.add("", name, value, word_size_range=[20, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render()

