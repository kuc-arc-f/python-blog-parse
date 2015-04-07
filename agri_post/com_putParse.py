# -*- coding: utf-8 -*- 
import requests
import json
import com_appConst

#com_putParse
class putParseClass:

	def __init__(self):
		print ""

	def send_parse(self, dict, sTime):
		clsConst  = com_appConst.appConstClass()
		headers = {
		  "X-Parse-Application-Id": clsConst.mParse_APP_ID ,
		  "X-Parse-REST-API-Key": clsConst.mParse_REST_ID ,
		  "Content-Type": "application/json"
		}
		dtParam ={'mc_id': int(dict["mc_id"]) }
		dtParam["snum1"] = int(dict["snum_1"])
		dtParam["snum2"] = int(dict["snum_2"])
		dtParam["snum3"] = int(dict["snum_3"])
		dtParam["snum4"] = int(dict["snum_4"])
		dtParam["dtnum"] = int(sTime)
		
		try:
			r = requests.post('https://api.parse.com/1/classes/SenObject1', headers=headers , data=json.dumps(dtParam), timeout=30)
			print r.status_code
			print r.json()
		except:
			print "failue, send_parse"
			raise
		finally:
			print "End ,send_parse"
