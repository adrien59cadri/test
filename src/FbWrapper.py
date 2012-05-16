import urllib.request
import xml.etree.ElementTree as ET


class FbWrapper:
	def __init__(self):
		self.address="https://dzada.fogbugz.com/api.asp?"
		self.logedon=False
		
	def doRequest(self,url):
		res=urllib.request.urlopen(url)
		print (res.status, res.reason, res.msg)
		res_body=res.read()
		res_str=str(res_body,"iso-8859-1")
		return res_str
	
	def checkError(self,res_str):
		print(res_str)
		root=ET.XML(res_str)
		element=root.find("error")
		if element is not None:
			print (element.tag, element.attrib)
			if element.tag == "error":
				self.error=element.text
				print("There is an error : "+element.text)
				exit(1)#error
		return root
				
	def createUrl(self,cmd,params):
		tokens=""
		if self.logedon:
			tokens="token="+self.token+"&"
		args="cmd="+cmd
		for p in params:
			args+="&"+p[0]+"="+p[1]
		print ("request : "+self.address)
		print(tokens+args)
		url=self.address+tokens+args
		return url
		
	def logon(self,user,pwd):
		print("LOGON")
		url=self.createUrl("logon",[["email",user],["password",pwd]])
		out=self.doRequest(url)
		xml=self.checkError(out)
		##now real thing
		self.token=xml.find("token").text
		print(self.token)
		self.logedon=True
	
	def logoff(self):
		print("LOGOFF")
		url=self.createUrl("logoff",[["token",self.token]])
		out=self.doRequest(url)
		xml=self.checkError(out)
		self.logedon=False
		##now real thing
		#ras
		
	def newCheckin(self,bugid, files, revisions,repo):
		print("NEW_CHECKIN")
		cmd="newCheckin"
		url=self.createUrl(cmd,[["ixBug",bugid],["sFile",files],["sPrev",revisions[0]],["sNew",revisions[1]],["ixRepository",repo]])
		out=self.doRequest(url)
		xml=self.checkError(out)

	def listCheckin(self,bugid):
		url=self.createUrl(cmd,[["ixBug",bugid]])
		out=self.doRequest(url)
		xml=self.checkError(out)
