import xlwt, sys
import xlrd
from xlutils.copy import copy
import time


def get_localtime():
	localtime = time.time()
	
	localTime_Day = time.strftime('%Y-%m-%d', time.localtime(localtime))
	localTime_Second = time.strftime('%H:%M:%S', time.localtime(localtime))
	localTime_Week = time.strftime('%A', time.localtime(localtime))
	return localTime_Day, localTime_Second, localTime_Week

def open_excel(file= 'file.xls'):
	try:
		data = xlrd.open_workbook(file)  #open the excel file and read data
		return data
	except Exception, e:
		print str(e)

def excel_table_byindex(file = 'file.xls', colnameindex=0, by_index=0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows
	ncols = table.ncols
	colnames = table.row_values(colnameindex)
	
	return data, nrows

	
def main():
	LeaveTime_day, LeaveTime_hour, LeaveTime_week = get_localtime()
	print "day: ", LeaveTime_day, "hour: ", LeaveTime_hour, "week: ", LeaveTime_week
	
	table_read, nrows = excel_table_byindex("LeaveTime.xls", 0)
	
	table_write = copy(table_read)
	sheet_write = table_write.get_sheet(0)

	xf = 0
	ctype = 1
	value = LeaveTime_day
	sheet_write.write(nrows, 0, value)
	
	value = LeaveTime_hour
	sheet_write.write(nrows, 1, value)
	
	value = LeaveTime_week
	sheet_write.write(nrows, 2, value)

	table_write.save("LeaveTime.xls")
	
if __name__=="__main__":
	main()