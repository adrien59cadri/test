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
file=open("answer.xml","w")
res_str=str(res_body,"iso-8859-1")
file.write(res_str)


print(res_str)
import xml.etree 
root=xml.etree.ElementTree.ElementTree(res_str)

element=root.find("error")
if element :
	print (element.name, element.tag, element.attribute)
if element.tag is "error":
	print("There is an error : "+element.text)