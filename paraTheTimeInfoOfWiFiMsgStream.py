# -*- coding: UTF-8 -*-
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
	
	print("----****\tmessage stream information of WiFi\t****----\n")
	
	index = 0
	
	MsgNum = TimeStampInfo[index]
	print("Msg number: %d\n\n" %(MsgNum))
	index+=2
	
	for msgIndex in range(0, MsgNum):
		print("\nMsg %d Info" %(msgIndex))
		
		MsgSn = TimeStampInfo[index]
		print("\tMsgSn is ", MsgSn)
		index+=1
		
		MsgDir = TimeStampInfo[index]
		print("\tMsgDir is ", MsgDirection[MsgDir])
		index+=1
		
		TimeStamp = TimeStampInfo[index]*pow(2,8*3) + TimeStampInfo[index+1]*pow(2,8*2) + TimeStampInfo[index+2]*pow(2,8) + TimeStampInfo[index+3]
		timeArray = time.localtime(TimeStamp)		
		index+=4

		timeArray = time.localtime(timeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print("\ttimeStamp is ", otherStyleTime)

def ParaRedirectorInfo(RedirectorInfo):
	print("----**** redirector information ****----\n")
	
	index = 0
	
	DomainNameLen = RedirectorInfo[index]
	print("domain name len is %d\n" %(DomainNameLen))
	index+=1
	
	PublicKeyLen = RedirectorInfo[index]
	print("cloud public key len is %d\n" %(PublicKeyLen))
	index+=1	

	Port_int = RedirectorInfo[index]*256 + RedirectorInfo[index+1]
	print("redirector port is %d\n" %(Port_int))
	index+=2
	
	DomainName = "".join(chr(ascInt) for ascInt in  RedirectorInfo[index:index+DomainNameLen])
	print("redirector's domain name is %s \n\t"  %(DomainName))
	index+=DomainNameLen
	
	Publickey = []
	for i in range(index, index+PublicKeyLen):
		Publickey.append(hex(RedirectorInfo[i]))
	print("redirector's public key is %s \n\t"  %(Publickey))
	
	
def ParaRebootAndOfflineInfo(RebootAndOfflineInfo):
	print("----****\treboot and offline information of WiFi\t****----\n")
	
	index = 0
	
	RebootInfoNum = RebootAndOfflineInfo[index]
	print("reboot info number: %d\n\n" %(RebootInfoNum))
	index += 1

	OfflineInfoNum = RebootAndOfflineInfo[index]
	print("offline info number: %d\n\n" %(OfflineInfoNum))
	index += 1
	
	RebootInfoIndex = RebootAndOfflineInfo[index]
	print("reboot info index: %d\n\n" %(RebootInfoIndex))
	index += 1
	
	OfflineInfoIndex = RebootAndOfflineInfo[index]
	print("offline info index: %d\n\n" %(OfflineInfoIndex))
	index += 1
	
	for RebootIndex in range(0, RebootInfoNum):
		print("Reboot info %d Info \n" %(RebootIndex))
		
		TimeStamp = RebootAndOfflineInfo[index]*pow(2,8*3) + RebootAndOfflineInfo[index+1]*pow(2,8*2) + RebootAndOfflineInfo[index+2]*pow(2,8) + RebootAndOfflineInfo[index+3]
		timeArray = time.localtime(TimeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print("\ttimeStamp is ", otherStyleTime)
		index+=4
		
		#ReabootReason info: 1Byte
		RbtReason = RebootAndOfflineInfo[index]
		print("\tRbtReason is ", WiFiRebootReason[RbtReason])
		index+=1
		
		#extra info: 1Byte
		ExtraInfo = RebootAndOfflineInfo[index]
		print("\tExtra is ", ExtraInfo)
		index+=1
		
	for OfflineIndex in range(0, OfflineInfoNum):
		print("offline info %d Info \n" %(OfflineIndex))
		
		#timestamp: 4Byte
		
		TimeStamp = RebootAndOfflineInfo[index]*pow(2,8*3) + RebootAndOfflineInfo[index+1]*pow(2,8*2) + RebootAndOfflineInfo[index+2]*pow(2,8) + RebootAndOfflineInfo[index+3]
		timeArray = time.localtime(TimeStamp)
		otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
		print("\ttimeStamp is ", otherStyleTime)
		
		index+=4
		
		#offline Reason: 1Byte
		OfflineReason = RebootAndOfflineInfo[index]
		print("\tRbtReason is ", WiFiOfflineReason[OfflineReason])
		index+=1
		
		#extra info: 1Byte
		ExtraInfo = RebootAndOfflineInfo[index]
		print("\tExtra is ", ExtraInfo)
		index+=1
		
		
if __name__ == '__main__':
	
	DbgInfoStr = "01061124238c746573742e61626c65636c6f75642e636eb8d935e4d6d8f2d6c8282f9fd96248c796a9ed5b5a1a9559d23cbb5f1b03073f01000100"
	n = 0
	DbgInfoInt = []
	while n < len(DbgInfoStr):
		DbgInfoInt.append(int(DbgInfoStr[n:n+2], 16))
		n += 2
	print(DbgInfoInt)
	index = 0
	for i in range(0, len(DbgInfoInt)):
		if DbgInfoInt[i] == 1:
			break;
	index = i+1
	DbgType = DbgInfoInt[index]
	
	if DbgType == WiFiRmtDbgType.eZCWRDT_GetMsgStreamInfo:
		ParaMsgStreamTimeInfo(DbgInfoInt[index+1:])
	elif DbgType == WiFiRmtDbgType.eZCWRDT_GetRedirectorInfo:
		ParaRedirectorInfo(DbgInfoInt[index+1:])
	elif DbgType == WiFiRmtDbgType.eZCWRDT_GetRbtAndOfflineInfo:
		ParaRebootAndOfflineInfo(DbgInfoInt)
	else:
		print("invalid debug type %d" %(DbgType))
