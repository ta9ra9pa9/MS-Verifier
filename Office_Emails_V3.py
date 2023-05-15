#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os , time , json , platform
from datetime import date
from threading import *

try:
	import requests
except:
	print( "Please follow this command or contact me ! 'pip install requests' OR 'python3 install requests' ")
	exit()
try:
	from colorama import Fore, Back, Style
except:
	print( "Please follow this command or contact me ! 'pip install colorama' OR 'python3 install colorama' ")
	exit()

try:
	from queue import Queue
except:
	print( "Please follow this command or contact me ! 'pip install queue' OR 'python3 install queue' ")
	exit()

def Logo( ):
    print("""
    ***************************************************************
	  __  __  _____   ______ __  __          _____ _      
	 |  \/  |/ ____| |  ____|  \/  |   /\   |_   _| |     
	 | \  / | (___   | |__  | \  / |  /  \    | | | |     
	 | |\/| |\___ \  |  __| | |\/| | / /\ \   | | | |     
	 | |  | |____) | | |____| |  | |/ ____ \ _| |_| |____ 
	 |_|  |_|_____/  |______|_|  |_/_/    \_\_____|______| MS EMAIL VERIFIER AND FINDER v3
                                                      																						 
	Hacking tools - 0day , Welcome User {} !
    
    ***************************************************************
    """.format( USERNAMEHANYA )  )

class Worker(Thread):
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try:
				func(*args, **kargs)
			except Exception as e:
				print(e)
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()


def set_terminal_title(title):
    if platform.system() == "Windows":
        os.system(f"title {title}")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f"echo -en '\033]0;{title}\a'")
    elif platform.system() == "SunOS":
        os.system(f"echo -n '\033]l{title}\033\\'")
    elif platform.system() == "FreeBSD":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "AIX":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "HP-UX":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "OSF1":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "SCO_SV":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "IRIX64":
        os.system(f"echo -n '\033]0;{title}\007'")

def make_dirs():
	global i , USERNAMEHANYA , MySubDomain , BLACKLISTDOMAIN
	
	BLACKLISTDOMAIN = ["test.com"]
	
	set_terminal_title( "Microsoft Email Verifer And Finder V3 -- BY HACKING TOOLS 0DAY" )

	try:
		with open('token.json', 'r') as file:
			data = json.load(file)
			USERNAMEHANYA = data['USERNAME']
			MySubDomain = data['MySubDomain']
	except:
		print( "Missing token.json !" )
		exit()
	
	rr = requests.get( "{}/{}/ChecksTatus".format( MySubDomain , USERNAMEHANYA ) , headers={ "User-agent": "User-%s" % USERNAMEHANYA } ).json()
			
	Logo( )

	if not rr["Working"]:
		
		print("Sorry , {} , Please Cotact me !".format( rr["Status"] ) )
		exit()
		
	else:
		pass
	
	i = "./{0}/".format( date.today().strftime("MSEmails-%m-%d-%Y") )
	
	if not os.path.exists(i):
		os.makedirs(i)
		
		lists = [ "Microsoft/" , "OtherISP/" ]
		for n in lists:
			z = i + n
			os.makedirs( z )
			
		return i
	else:
		pass
		
	time.sleep(1)


def Action( email ):
	
	domainIT = email.split("@")[1]
	
	def save_as( inputs  , saveAs , saveString ):
		with open( saveAs , "a" ) as ff:
			ff.write( "%s\n" % saveString )
		print( inputs )

	def REQ_( email , PassCheck = None ,  Endpoint="Ms-Domain" , USERNAME=USERNAMEHANYA ):
		
		if not PassCheck:
			return requests.get( "{3}/{2}/{1}/{0}".format( email , Endpoint , USERNAME , MySubDomain ) , headers={ "User-agent": "User-%s" % USERNAME } , timeout=60 )
		else:
			return requests.get( "{}/{}?email={}".format( MySubDomain , USERNAME , email ) , headers={ "User-agent": "User-%s" % USERNAME } , timeout=60 )


	if "@" in email or domainIT in BLACKLISTDOMAIN :
		
		First_ = REQ_( email ).json()
		if First_["Valid"]:			
			SECOND_ = REQ_( email , True ).text
			
			MESSAGE = Back.GREEN + "[+] >> {} >> {}".format( email  , SECOND_ ) + Back.RESET
			save_as( MESSAGE , "{}{}{}.txt".format(  i , "Microsoft/"  , SECOND_ )  , email  )
			
		else:
			# ~ print( BLACKLISTDOMAIN )
			BLACKLISTDOMAIN.append(  domainIT  ) 
			
			MESSAGE = Back.RED + "[-] >> {} >> {}".format( email  , First_["Type_domain"] ) + Back.RESET
			save_as( MESSAGE , "{}{}{}.txt".format(  i , "OtherISP/"  , First_["Type_domain"] )  , email  )
	else:
		print( Fore.RED + "%s <<<< Email Format Error ! <<<<" % email + Fore.RESET ) 
			

def main():
	make_dirs()
	
	Emails = [ ]
	
	readsplit = open( input("[x] ListName : ") , encoding="utf-8" , errors="ignore" ).read().splitlines()
	
	for fullemail in readsplit:
		if "@" in fullemail:
			domain = fullemail.split("@")[1]
			Emails += [ "admin@%s" % domain , "administrator@%s" % domain, "webmaster@%s" % domain , fullemail ]
		else:
			pass

	
	set_red = set(Emails)
	print(  Back.BLUE + " >>>> CREAT NEW USERS AND REMOVE DUPLICATE {} >> TO >> {}".format( len(Emails) , len(set_red)  )  + Back.RESET )
	
	pool = ThreadPool( int( 5 ) )
	for email in set_red :
		pool.add_task( Action , email )

if __name__ == "__main__":
	main()
