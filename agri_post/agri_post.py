import serial
import datetime
import sys
import traceback

import com_getparam
import com_func
import com_putParse
import com_logging2

mDevice = "/dev/ttyACM0"

mOK_CODE=1
mNG_CODE=0

mTimeMax= 300

if __name__ == "__main__":
    ser=serial.Serial(mDevice ,9600)
    clsParam = com_getparam.getparamClass()
    clsCom  = com_func.funcClass()
    clsParse =com_putParse.putParseClass()
    clsLog = com_logging2.loggingClass()
    from datetime import datetime
    tmBef = datetime.now()

    while True:
        val=ser.readline()
        bFrom = clsParam.Is_fromMC(val)
        if bFrom==True:
        	dic= clsParam.getDict(val)
        	sTime = datetime.now().strftime("%Y%m%d%H%M%S")
        	
        	tmNow = datetime.now()
        	tmSpan = tmNow - tmBef
        	iSpan = tmSpan.total_seconds()
        	print "iSpan="+ str(iSpan)
        	if iSpan > mTimeMax:
        		tmBef = datetime.now()
        		try:
	        		clsParse.send_parse(dic, sTime)
	        	except:
					print "--------------------------------------------"
					print traceback.format_exc(sys.exc_info()[2])
					print "--------------------------------------------"
					clsLog.debug( traceback.format_exc(sys.exc_info()[2]) )
        		
        print("IN :"  + val)
