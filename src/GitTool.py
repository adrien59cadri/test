import xml.etree.ElementTree as ET
import subprocess
#bash command
command= "git log --pretty=format:\"<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>\" 8409f6f..6f4677f"


p = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
res_str = p.communicate()[0]
print (res_str)

# print ("XML")
# root=ET.XML(res_str)

# commits=root.findAll("commit")

# print (commits)