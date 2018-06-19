#! /usr/bin/python2
import os
import time 
import webbrowser
x='''
Press 1 --> Check date and time
Press 2 --> To create a file
Press 3 --> To create a directory
Press 4 --> Search on Google
Press 5 --> Logout user system
Press 6 --> To Shutdown OS
Press 7 --> To check internet connection
Press 9 --> To login watsapp on browser
Press 8 --> To check all connected IP in your network
'''
print (x)								#printing the menu

choice=int(raw_input("Please enter your choice"))		#taking the choice of user

if choice==1 :
	
	data=time.ctime()
	print "time : "
	print data.split()[3]
	print "date : "
	print data.split()[0:3]

elif choice==2 :
	f_name=raw_input("Apki file ka naam enter kre")
	os.system('sudo gedit' +f_name)
elif choice==3 :
	dir_name=raw_input("Apki directory ka naam enter kre")
	os.system('mkdir' +dir_name)
elif choice==4 :
	google=raw_input("De Dhana Dhan")
	webbrowser.open_new_tab('https://www.google.com/search?q='+google)
elif choice==5 :
	print 'Kya apko idhrse klti marni h'
	os.system('gnome-session-quit')
elif choice==6 :
	os.system('poweroff')
elif choice==7 :
	os.system ('ping www.google.com')
elif choice==8 :
	print os.system('sudo nmap -v -sn 198.160.10.0/24')
else:
	print 'Apka ip address h'
	print os.system('hostname -I')




