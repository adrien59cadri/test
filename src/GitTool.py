import xml.etree.ElementTree as ET
import subprocess
#bash command
#command= "git log --pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>' 8409f6f..6f4677f > log.xml"
old="8409f6f"
new="6f4677f"
format="--pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>"

print("RUN COMMAND")
subp=subprocess.Popen(['git', 'log', format, old+".."+new], stdout=subprocess.PIPE)
outputb=subp.stdout.read()
output = "<list>\n"+str(outputb,"iso-8859-1")+"\n</list>"


print ("XML")
root=ET.XML(output)
commits=root.findall("commit")
print (commits)
