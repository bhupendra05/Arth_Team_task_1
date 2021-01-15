import os

print("\t\t\tWelcome to the Menu")

print("\t\t\t--------------------")
print("\n\n\n")
f="y"
while True:
	if "y" in f:
		os.system("clear")
		os.system("clear")
		os.system("tput setaf 255")
		os.system("figlet -c Docker")
		os.system("tput setaf 7")
		os.system("tput setaf 10")
		print("Press 1 : to install docker")
		print("Press 2 : to check whether docker is installed or not")
		print("Press 3 : to start docker services")
		print("Press 4 : to check the docker images") 
		print("press 5 : to downlod docker image")
		print("Press 6 : to remove docker image")
		print("Press 7 : to launch the docker container")
		print("Press 8 : to ue the container terminal")
		print("Press 9 : to know how many os/containers are running under docker") 
		print("Press 10 : to terminate os")
		print("Press 11 : to remove all the running container")
		print("Press 12 : to enable docker permanently")
		print("Press 13 : to check docker state(active/inactive)")
		print("Press 14 : to configure web sever in docker container.")
		os.system("tput setaf 7")
		ch=input("Enter your choice : ")
		print(ch)
		
		if int(ch)==1:
			url=input("Enter the url of required docker : ")
			os.system("curl -sSL " +url)
			print("docker has installed pls check to confirm by pressing no two")
		elif int(ch)==2:
			os.system("rpm -q docker-ce")
		elif int(ch)==3:
			os.system("systemctl start docker")
		elif int(ch)==4:
			os.system("docker images")
		elif int(ch)==5:
			imgname=input("type the docker image name that you wish to download : ")
			os.system("docker pull" +imgname)
		elif int(ch)==6:
			img=input("type the image name alog with its version in the formate name:version that you wish to remove")
			os.system("docker rmi "+img+ "-f")
		elif int(ch)==7:
			dn=input("type image name that you wish to run : ")
			nm=input("type the name you wish to give this os : ")
			os.system("docker run -d -i -t --name " +nm+ " "+dn)
		elif int(ch)==8:
			on=input("type the os name where you wish to login : ")
			os.system("docker attach "+on)
		elif int(ch)==9:
			os.system("docker ps -a ")
		elif int(ch)==10:
			ton=input("type the docker os name that you we to terminate : ")
			os.system("docker rm -f "+ton)
		elif int(ch)==11:
			os.system("docker rm -f `docker ps -a -q`")
		elif int(ch)==12:
			os.system("systemctl enable docker")
		elif int(ch)==13:
			os.system("systemctl status docker")	
		elif int(ch) == 14:
			n = input("Enter the container name:-")
			os.system("docker exec {0} yum install -y httpd".format(n))
			os.system("docker exec {0} /usr/sbin/httpd".format(n))
		else:
			print("system has not found the specified command")
		f=input("to continue : y/n : ")
	elif "n" in f:
		break
	else:
		f=input("Do you want to continue...(y/n): ")		

		

		

