import xml.etree.ElementTree as ET
import subprocess
import FbWrapper

#bash command
#command= "git log --pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>' 8409f6f..6f4677f > log.xml"
old="8409f6f"
new="6f4677f"
format="--pretty=format:'<commit>%n<ref>%h</ref>%n<author>%an</author>%n<date>%ai</date>%n<message>%s</message>%n</commit>"

print("RUN COMMAND")
subp=subprocess.Popen(['git', 'log', format, old+".."+new], stdout=subprocess.PIPE)
outputb=subp.stdout.read()
output = "<list>\n"+str(outputb,"iso-8859-1")+"\n</list>"

fb = FbWrapper.FbWrapper()
fb.logon('courdava@enserg.fr','p455w04d')

print ("XML")
root=ET.XML(output)
commits=root.findall("commit")

for commit in commits:
	authorname=commit.find("author").text
	date=commit.find("date").text
	message=commit.find("message").text
	reference=commit.find("ref").text
	process=subprocess.Popen(['git', 'diff', "--name-only", reference], stdout=subprocess.PIPE)
	filelist=str(process.stdout.read(),"iso-8859-1").replace("\n",",")
	print("\nCommit : "+reference+"\nby "+authorname+" ["+date+"]\n"+message)
	print(filelist)
	case = message.find("BugzId:%d")
	if(case>0):
		#we mus look for all references
		print("we will send a requesto fogbugz")
		
	
	print("Request to fogbugz generation")
	
	my_repo_name = "my_repo"
	repo_id = "1" #saw this in fb
	bug_id = "2"
	files = filelist
	#fb.newCheckin(bug_id,files,[old,reference],repo_id)

fb.logoff()

