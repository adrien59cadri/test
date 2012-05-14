import urllib.request



address="https://dzada.fogbugz.com"
address+="/api.asp?"

command_="logon"
command = "cmd="+command_
param1_="courdava@enserg.fr"
param1="email="+param1_
param2_="p455w04d"
param2="password="+param2_

args=command+"&"+param1+"&"+param2
print ("request : "+address)
print(args)
url=address+args
res=urllib.request.urlopen(url)

print (res.status, res.reason, res.msg)
res_body=res.read()
res_str=str(res_body,"iso-8859-1")


print(res_str)
import xml.etree.ElementTree as ET
root=ET.XML(res_str)
element=root.find("error")
if element is not None:
	print (element.tag, element.attrib)
	if element.tag == "error":
		print("There is an error : "+element.text)
		exit(1)#error bad login
token = root.find("token").text

print( token)



print("\nlog off")
command_="logoff"
command = "cmd="+command_
param1_=token
param1="token="+param1_

args=command+"&"+param1
print ("request : "+address)
print(args)
url=address+args
res=urllib.request.urlopen(url)

print (res.status, res.reason, res.msg)
res_body=res.read()
res_str=str(res_body,"iso-8859-1")


print(res_str)
import xml.etree.ElementTree as ET
root=ET.XML(res_str)
element=root.find("error")
if element is not None:
	print (element.tag, element.attrib)
	if element.tag == "error":
		print("There is an error : "+element.text)
		exit(1)#error bad logoff
