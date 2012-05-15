import xml.etree.ElementTree as ET
import subprocess
#bash command
#command= "git log --pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>' 8409f6f..6f4677f > log.xml"
old="8409f6f"
new="6f4677f"
format="--pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>"

print("RUN COMMAND")
subprocess.Popen(['git', 'log', format, old+".."+new], stdout=subprocess.PIPE)
output = git.stdout.read()


print ("XML")
# file=open("log.xml")
# root=ET.XML(file.read())
# commits=root.findAll("commit")
# print (commits)
