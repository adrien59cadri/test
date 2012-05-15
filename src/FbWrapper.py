import urllib.request
import xml.etree.ElementTree as ET


class FbWrapper:
	def __init__(self):
		self.address="https://dzada.fogbugz.com/api.asp?"
		
	def doRequest(url):
		res=urllib.request.urlopen(url)
		print (res.status, res.reason, res.msg)
		res_body=res.read()
		res_str=str(res_body,"iso-8859-1")
		return res_str
	
	def checkError(res_str):
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
				
	def createUrl(cmd,params):
		args="cmd="+cmd
		for p in params:
			args+=+"&"+params[0]+"="+params[1]
		print ("request : "+self.address)
		print(args)
		url=self.address+args
		return url
		
	def logon(user,pwd):
		url=self.createUrl("logon",[["email",email],["password",pwd]])
		out=self.doRequest(url)
		xml=self.checkError(out)
		##now real thing
		self.token=xml.find("token").text
		print(self.token)
	
	def logoff():
		url=self.createUrl("logoff",[["token",self.token]])
		out=self.doRequest(url)
		xml=self.checkError(out)
		##now real thing
		#ras
		
	def newCheckin(bugid, files, revisions,repo):
		cmd="newCheckin"
		url=self.createUrl(cmd,[["ixBug",bugid],["sFile",files],["sPrev",revisions[0]],["sNext",revisions[1]],["ixRepository",repo]])
		out=self.doRequest(url)
		xml=self.checkError(out)

	def listCheckin(bugid):
		url=self.createUrl(cmd,[["ixBug",bugid]])
		out=self.doRequest(url)
		xml=self.checkError(out)
