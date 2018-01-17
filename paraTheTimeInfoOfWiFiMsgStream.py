# -*- coding: UTF-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import time
import binascii

def enum(**enums):
    return type('Enum', (), enums)
 
WiFiRmtDbgType = enum(
	eZCWRDT_AT=1, 
	eZCWRDT_LowPowerSwitch=2, 
	eZCWRDT_GetLinkQuality=3, 
	eZCWRDT_GetMsgStreamInfo=4, 
	eZCWRDT_GetErrStatic=5, 
	eZCWRDT_GetRedirectorInfo=6, 
	eZCWRDT_GetRbtAndOfflineInfo=7)


MsgDirection = ["min", "RecvFromCloud", "SendToMCU", "RecvFromMCU", "SendToCloud"]
WiFiRebootReason = ["Poweroff", "WatchDog", "SmartConfig", "OTAFinish", "OTAFailed", "SetAP", "SetStation", "RebootByMcu"]
WiFiOfflineReason = ["Poweroff", "Reboot", "RecvErr", "WiFiDisconnect", "HeartBeatLoss"]



def ParaMsgStreamTimeInfo(TimeStampInfo):
	
	print "----****\tmessage stream information of WiFi\t****----\n"
	
	index = 0
	for i in range(0, len(TimeStampInfo)):
		if i%2 != 0:
			continue
		if int(TimeStampInfo[i:i+2],16) == WiFiRmtDbgType.eZCWRDT_GetMsgStreamInfo:
			i+=2
			break;
	index = i
		
	print len(TimeStampInfo)
	MsgNum = int(TimeStampInfo[index:index+2], 16)
	print "Msg number: %d\n\n" %(MsgNum)
	index+=2
	
	for msgIndex in range(0, MsgNum):
		print "\nMsg %d Info" %(msgIndex)
		
		MsgSn = int(TimeStampInfo[index:index+2], 16)
		print "\tMsgSn is ", MsgSn
		index+=2
		
		MsgDir = int(TimeStampInfo[index:index+2], 16)
		print "\tMsgDir is ", MsgDirection[MsgDir]
		index+=2
		
		timeStamp = int(TimeStampInfo[index:index+8], 16)
		index+=8

		timeArray = time.localtime(timeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print "\ttimeStamp is ", otherStyleTime

def ParaRedirectorInfo(RedirectorInfo):
	print "----**** redirector information ****----\n"
	print "total len is %d\n" %(len(RedirectorInfo))
	
	index = 0
	for i in range(0, len(RedirectorInfo)):
		if i%2 != 0:
			continue
		if int(RedirectorInfo[i:i+2],16) == WiFiRmtDbgType.eZCWRDT_GetRedirectorInfo:
			i+=2
			break;
	index = i
	
	DomainNameLen = int(RedirectorInfo[index:index+2], 16)
	print "domain name len is %d\n" %(DomainNameLen)
	index+=2
	
	PublicKeyLen = int(RedirectorInfo[index:index+2], 16)
	print "cloud public key len is %d\n" %(PublicKeyLen)
	index+=2	

	Port_int = int(RedirectorInfo[index:index+4], 16)
	print "redirector port is %d\n" %(Port_int)
	index+=4
	
	DomainName = binascii.a2b_hex(RedirectorInfo[index:index+DomainNameLen*2])
	print "redirector's domain name is %s \n\t"  %(DomainName)
	index+=DomainNameLen*2
	
	print "redirector's public key is %s \n\t"  %(RedirectorInfo[index:index+PublicKeyLen*2])
	
	
		
def ParaRebootAndOfflineInfo(RebootAndOfflineInfo):
	print "----****\treboot and offline information of WiFi\t****----\n"
	print len(RebootAndOfflineInfo)
	
	index = 0
	for i in range(0, len(RebootAndOfflineInfo)):
		if i%2 != 0:
			continue
		if int(RebootAndOfflineInfo[i:i+2],16) == WiFiRmtDbgType.eZCWRDT_GetRbtAndOfflineInfo:
			i+=2
			break;
	index = i
	
	RebootInfoNum = int(RebootAndOfflineInfo[index:index+2], 16)
	print "reboot info number: %d\n\n" %(RebootInfoNum)
	index+=2

	OfflineInfoNum = int(RebootAndOfflineInfo[index:index+2], 16)
	print "offline info number: %d\n\n" %(OfflineInfoNum)
	index+=2
	
	RebootInfoIndex = int(RebootAndOfflineInfo[index:index+2], 16)
	print "reboot info index: %d\n\n" %(RebootInfoIndex)
	index+=2
	
	OfflineInfoIndex = int(RebootAndOfflineInfo[index:index+2], 16)
	print "offline info index: %d\n\n" %(OfflineInfoIndex)
	index+=2
	
	for RebootIndex in range(0, RebootInfoNum):
		print "Reboot info %d Info \n" %(RebootIndex)
		
		TimeStamp = int(RebootAndOfflineInfo[index:index+8], 16)
		timeArray = time.localtime(TimeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print "\ttimeStamp is ", otherStyleTime		
		index+=8
		
		#ReabootReason info: 1Byte
		RbtReason = int(RebootAndOfflineInfo[index:index+2], 16)
		print "\tRbtReason is ", WiFiRebootReason[RbtReason] 
		index+=2
		
		#extra info: 1Byte
		ExtraInfo = int(RebootAndOfflineInfo[index:index+2], 16)
		print "\tExtra is ", ExtraInfo
		index+=2
		
	for OfflineIndex in range(0, OfflineInfoNum):
		print "offline info %d Info \n" %(OfflineIndex)
		
		#timestamp: 4Byte
		
		TimeStamp = int(RebootAndOfflineInfo[index:index+8], 16)
		timeArray = time.localtime(TimeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print "\ttimeStamp is ", otherStyleTime	
		
		index+=8		
		
		#offline Reason: 1Byte
		OfflineReason = int(RebootAndOfflineInfo[index:index+2], 16)
		print "\tRbtReason is ", WiFiOfflineReason[OfflineReason] 
		index+=2
		
		#extra info: 1Byte
		ExtraInfo = int(RebootAndOfflineInfo[index:index+2], 16)
		print "\tExtra is ", ExtraInfo
		index+=2
		
		
if __name__ == '__main__':
	
	DbgInfo = "01061124238c746573742e61626c65636c6f75642e636eb8d935e4d6d8f2d6c8282f9fd96248c796a9ed5b5a1a9559d23cbb5f1b03073f01000100"
	index = 0
	for i in range(0, len(DbgInfo)):
		if DbgInfo[i] == '1':
			break;
	index = i+1
	DbgType = int(DbgInfo[index+1], 16)
	
	if DbgType == WiFiRmtDbgType.eZCWRDT_GetMsgStreamInfo:
		ParaMsgStreamTimeInfo(DbgInfo)
	elif DbgType == WiFiRmtDbgType.eZCWRDT_GetRedirectorInfo:
		ParaRedirectorInfo(DbgInfo)		
	elif DbgType == WiFiRmtDbgType.eZCWRDT_GetRbtAndOfflineInfo:
		ParaRebootAndOfflineInfo(DbgInfo)
	else:
		print "invalid debug type %d" %(DbgType)
