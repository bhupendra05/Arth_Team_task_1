import os
os.system("echo '<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>' > ncon.txt")
os.system("echo '<property>\n<name>dfs.name.dir</name>\n<value>/dn</value>\n</property>' > dcon.txt")
while True:
	while True:
		os.system("tput setaf 10")
		print("Press\n1.For configuring Name node locally.\n2.For configuring Name node remotelly\n3.To Exit")
		os.system("tput setaf 7")		
		loc = int(input("Enter your choice:-"))
		if loc == 1:
			print("\t\t\t\tConfiguring name node locally\n")
			lip = input("Enter the ip of local system:")
			os.system("systemctl stop firewalld.service")
			os.system("systemctl disable firewalld.service")
			os.system("echo '<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:9001</value>\n</property>' > core.txt".format(lip))
			os.system("mkdir /nn")
			os.system("rpm -i -v -h jdk-8u171-linux-x64.rpm")
			os.system("rpm -i -v -h hadoop-1.2.1-1.x86_64.rpm --force")
			os.system("sed -i '/<configuration>/r core.txt' /etc/hadoop/core-site.xml")
			os.system("sed -i '/<configuration>/r ncon.txt' /etc/hadoop/hdfs-site.xml")
			os.system("hadoop namenode -format")
			os.system("hadoop-daemon.sh start namenode")
			os.system("jps")
			break
		elif loc == 2:
			print("\t\t\t\tConfiguring Name node on server\n")
			dip = input("Enter ip of remote system:")
			os.system("ssh-keygen -t rsa -b 2048")
			os.system("ssh-copy-id root@{0}".format(dip))
			os.system("ssh root@{0} mkdir /data_con".format(dip))
			os.system("ssh root@{0} mkdir /nn".format(dip))
			os.system("ssh root@{0} systemctl stop firewalld.service".format(dip))
			os.system("ssh root@{0} systemctl disable firewalld.service".format(dip))
			os.system("scp *.rpm root@{0}:/name_con".format(dip))
			os.system("scp *.txt root@{0}:/name_con".format(dip))
			os.system("ssh root@{0} rpm -i -v -h /name_con/jdk-8u171-linux-x64.rpm".format(dip))
			os.system("ssh root@{0} rpm -i -v -h /name_con/hadoop-1.2.1-1.x86_64.rpm --force".format(dip))
			os.system('ssh root@{0} "sed -i \'/<configuration>/r /data_con/core.txt\' /etc/hadoop/core-site.xml"'.format(dip))
			os.system('ssh root@{0} "sed -i \'/<configuration>/r /data_con/dcon.txt\' /etc/hadoop/hdfs-site.xml"'.format(dip))
			os.system("ssh root@{0} hadoop namenode -format".format(dip))
			os.system("ssh root@{0} hadoop-daemon.sh start namenode".format(dip))
			os.system("ssh root@{0} jps".format(dip))
			break
		elif loc == 3:
			exit() 
	print("\n\n\t\tCongrats..Your Name Node has been successfully Configured\n")
	ch=input("Do you want to continue...(y/n):")
	if ch == "n":
		exit()
	os.system("sleep 5")
	os.system("clear")
	print("\t\t\t  Welcome to Hadoop Configuration")
	
	print("\t\t\t\tDataNode Configuration\n")
	
	nd=int(input("Enter number of data node required for the hdfs cluster:"))

	for i in range(1,nd+1):
		print("\t\t\t\t{0} DataNode\n".format(i))
		dip = input("Enter the ip of datanode:")
		os.system("ssh-keygen -t rsa -b 2048")
		os.system("ssh-copy-id root@{0}".format(dip))
		os.system("ssh root@{0} mkdir /data_con".format(dip))
		os.system("ssh root@{0} mkdir /dn{1}".format(dip,i))
		os.system("ssh root@{0} systemctl stop firewalld.service".format(dip))
		os.system("ssh root@{0} systemctl disable firewalld.service".format(dip))
		os.system("scp *.rpm root@{0}:/data_con".format(dip))
		os.system("scp *.txt root@{0}:/data_con".format(dip))
		os.system("ssh root@{0} rpm -i -v -h /data_con/jdk-8u171-linux-x64.rpm".format(dip))
		os.system("ssh root@{0} rpm -i -v -h /data_con/hadoop-1.2.1-1.x86_64.rpm --force".format(dip))	
		os.system('ssh root@{0} "sed -i \'/<configuration>/r /data_con/core.txt\' /etc/hadoop/core-site.xml"'.format(dip))
		os.system('ssh root@{0} "sed -i \'/<configuration>/r /data_con/dcon.txt\' /etc/hadoop/hdfs-site.xml"'.format(dip))
		os.system("ssh root@{0} hadoop-daemon.sh start datanode".format(dip))
		os.system("ssh root@{0} jps".format(dip))
		print("\n\t\t\t\tCongrats..Your {0} DataNode successfully Configured\n".format(i))
		ch=input("Do you want to continue...(y/n):")
		if ch == "n":
			exit()		
		os.system("sleep 5")
		os.system("clear")
	print("\t\t\t  Welcome to Hadoop Configuration")
	print("\t\t\t\tClient Configuration\n")
	nd=int(input("Enter number of user for the hdfs cluster:"))

	for i in range(1,nd+1):
		print("\t\t\t\t{0} Client\n".format(i))
		dip = input("Enter the ip of client:")
		os.system("ssh-keygen -t rsa -b 2048")
		os.system("ssh-copy-id root@{0}".format(dip))
		os.system("ssh root@{0} mkdir /data_con".format(dip))
		os.system("ssh root@{0} systemctl stop firewalld.service".format(dip))
		os.system("ssh root@{0} systemctl disable firewalld.service".format(dip))
		os.system("scp *.rpm root@{0}:/data_con".format(dip))
		os.system("scp *.txt root@{0}:/data_con".format(dip))
		os.system("ssh root@{0} rpm -i -v -h /data_con/jdk-8u171-linux-x64.rpm".format(dip))
		os.system("ssh root@{0} rpm -i -v -h /data_con/hadoop-1.2.1-1.x86_64.rpm --force".format(dip))
		os.system("ssh root@{0} sed -i '/<configuration>/r /data_con/core.txt' /etc/hadoop/core-site.xml".format(dip))
		print("\n\t\t\t\t{0} Client successfully Configured\n".format(i))
		ch=input("Do you want to continue...(y/n):")
		if ch == "n":
			exit()
		os.system("sleep 5")
		os.system("clear")

	print("\t\t\t\tHadoop Cluster configured succesfully..")
	ch=input("Press q to quit:")
	if ch == "q":
		break

	
	
exit()
	
		
