# -*- coding: UTF-8 -*-
from pandas import Series, DataFrame
import pandas as pd


UartPacket = [
	[u'包头', "1B", "0x5A"], 
	[u"包长度H", "1B", "0x??"], 
	[u"包长度L", "1B", "??"], 
	[u"包序号", "1B", "0x??"], 
	[u"附加码", "1B", "0x??"], 
	[u"功能码", "1B", "0x??"], 
	[u"数据", "nB", "0x??"], 
	[u"校验和", "1B", "0x01"], 
	[u"包尾", "1B", "0x5A"]]
	

def convertToHtml(result,title):
	#将数据转换为html的table
	#result是list[list1,list2]这样的结构
	#title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
	d = {}
	index = 0
	for t in title:
		d[t]=result[index]
		index = index+1
	df = pd.DataFrame(d)
	df = df[title]
	h = df.to_html(index=False, justify = 'justify-all')
	return h

if __name__ == '__main__':
	
	title = ["字节数", "描述", "值"]
	Length = []
	Description = []
	value = []
	for member in UartPacket:
		Length.append(member[1])
		Description.append(member[0])
		value.append(member[2])
	
	result = [Length, Description, value]
	print(convertToHtml(result,title))