import os
os.system("clear")

wl = True
while wl:
	os.system("tput setaf 255")
	os.system("figlet -c Python Automation")
	os.system("tput setaf 10")
	print("""
 Press:-
 1.For date
 2.For calender
 3.For web server Configuration
 4.For Docker 
 5.For Hadoop Configuration 
 6.For Logical Volume Mangement(LVM)
 7.For AWS
 8.For Exit""")
	os.system("tput setaf 7")
	ch = int(input("Enter Your Choice:-"))
	if ch == 1:
		os.system("date")
	elif ch == 2:
		os.system("cal")
	elif ch == 5:
		os.system("clear")
		os.system("tput setaf 255")
		os.system("figlet -c Hadoop Configuration")
		os.system("tput setaf 7")
		os.system("python3 /root/task/name_node.py")
	elif ch == 3:
		os.system("clear")
		os.system("tput setaf 255")
		os.system("figlet -c Web Server Configuration")
		os.system("tput setaf 7")
		os.system("yum install httpd -y")
		os.system("systemctl start httpd")
	elif ch == 4:
		
		os.system("python3 /root/task/dockermenu.py")
	elif ch == 6:
		os.system("clear")
		os.system("tput setaf 255")
		os.system("figlet -c LVM")
		os.system("tput setaf 7")
		
		while True:
			os.system("tput setaf 10")
			print("""
 Choose option for using LVM:-
 1.For using locally.
 2.For using remotely.
 3.For Exit""")
			os.system("tput setaf 7")
			lch = int(input("Enter Your Choice:-"))
			if lch == 1:
				os.system("python3 /root/task/lvm.py")
				break
			elif lch == 2:
				dip = input("Enter ip of remote system:")
				os.system("ssh-keygen -t rsa -b 2048")
				os.system("ssh-copy-id root@{0}".format(dip))
				os.system("ssh root@{0} mkdir /lvm_con".format(dip))
				os.system("scp lvm.py root@{0}:/lvm_con".format(dip))
				os.system("ssh root@{0} python3 /lvm_con/lvm.py".format(dip))
				break		
			elif lch == 3:
				print("Thanks for using the tool")
				break
			else:
				print("invalid option")
		
	elif ch == 7:
		
		
		os.system("python3 /root/task/aws.py")
	elif ch == 8:
		print("Thanks for using the tool")
		exit() 
	else:
		print("Invalid option")
	l = input("Do you want to continue...(y/n)")
	if l == "n":
		wl = False
		
	os.system("clear")
print("Thanks for using......")
