#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

fr = open('学生端1.txt','r')
# fw = open('result.txt', 'w')

nameDict={}

for line in fr:
	line = unicode(line)
	print line[:-3]
	# line=line.strip('\n')
	# nameStr = line.split(',')[0]
	# if not nameDict.has_key(nameStr):
	# 	nameDict[nameStr] = 0
	# nameDict[nameStr] += 1
	# if nameDict[nameStr] > 1:
	# 	print nameStr	
	# fw.write(line + ',1' + '\n')

# fw.close()
fr.close()