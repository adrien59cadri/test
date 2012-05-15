import xml.etree.ElementTree as ET
import os
#bash command
command= "git log --pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>' 8409f6f..6f4677f > log.xml"


os.system(command)


print ("XML")
file=open("log.xml")
root=ET.XML(file.read())
commits=root.findAll("commit")
print (commits)
