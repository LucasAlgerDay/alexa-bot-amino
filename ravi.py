#encoding=utf-8
#from keep_alive import keep_alive
#keep_alive()
#(J
from os import system
#system("pip install easy_pil pysocks socks json_minify websockets websocket-client==1.5.1 fancy_text names bs4 secmail google_images_search googletrans==3.1.0a praw pytz pymongo gTTS pillow wheel numpy requests_random_user_agent pyjokes")
#system("pip uninstall pytube")
from datetime import datetime as dateh
#from translate import Translator
from easy_pil import Editor, Canvas, load_image, Font
import io
from pytube import YouTube
import urllib.parse
import re
import subprocess
#from yt_dlp import YoutubeDL
from io import BytesIO
import base64
import urllib.request
#system("pip install socks pysocks gtts")
#system("pip install pyjokes")
#system("pip install websocket-client==1.5.1")
#system("pip install fancy_text")
#system("pip install secmail")
#system("pip install bs4")
#system("pip install google_images_search")
#from keep_alive import keep_alive
#keep_alive()
#system("pip install BotAmino==1.20.4")
#from Tam import l_amino
import sys
import copy
from zipfile import ZipFile
import zipfile
import os
from google_images_search import GoogleImagesSearch
#from googletrans import Translator
#from google_images_search
from bs4 import BeautifulSoup
import re
import numpy as np
import pyjokes
import unicodedata
from time import sleep
from gtts import gTTS, lang
from fancy_text import fancy
#from google_trans_new import google_translator
#from constant import LANGUAGES, DEFAULT_SERVICE_URLS
from json import dumps, load
from threading import Thread
import threading
from random import choice, randint
from pathlib import Path
from contextlib import suppress
from string import punctuation
from unicodedata import normalize
import time
import urllib
import json
import pathlib
from datetime import datetime
#from pdf2image import convert_from_path
import names
from BotAmino import *
import random
import math
from PIL import Image, ImageFont, ImageDraw
import string
import pytz
import re
import praw
import random
import json
from requests import request
from urllib.request import urlopen # To load URL's.
from PIL import Image
import shutil
import requests
import argparse
from pymongo import MongoClient
import urllib.parse
#import importlib # python 2.7 does not require this
#import BotAmin
#importlib.reload(BotAmin)
#from BotAmin import BotAmino


#keep_alive()
mongo=MongoClient("mongodb+srv://kiritovayux:cwa@cluster0.emr3bjf.mongodb.net/?retryWrites=true&w=majority")

#mongo= MongoClient("mongodb+srv://cartoons:cwaamino@cluster0.3nela.mongodb.net/?retryWrites=true&w=majority")
#db = client.test

db=mongo['comid']

test_1=db['list2']
ob=mongo["gcwel"]
gcw=ob["list3"]
si=mongo["sid"]
sit=si["sds"]
#import cleverbotfree
#keep_alive()
path_utilities='utilities'
path_amino = f'{path_utilities}/amino_list'
path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"
path_download = "news"

fs = open("sids.txt")
sidd=(fs.read())

adm=["501cc6f5-1e38-4a22-9df5-cd0625b0205e","816d376a-29f3-4964-aa52-998517905c2b","14c9eac9-ba6f-4fa8-b381-7a202422a679"]

admn=["501cc6f5-1e38-4a22-9df5-cd0625b0205e","816d376a-29f3-4964-aa52-998517905c2b"]

mdd=mongo['community']
jsonf=mdd["files"]
with suppress(Exception):
    for i in (path_utilities, path_amino):
        Path(i).mkdir(exist_ok=True)

afklist=[]
def proxyss():
	s=requests.get("http://pubproxy.com/api/proxy?https=true")
	y=json.loads(s.text)
	u=y["data"]
	for i in u:
		pr=i["ipPort"]
	return pr


ress=sit.find({},{'_id': 0})
for i in ress:
	sidss=i["sid"]


client=BotAmino("vinitaparadkar79@gmail.com","lodabhenchod")
dbs=mongo['delete']
jsn=dbs['mess']
noo=jsn.count_documents({})
if noo>=50000:
	jsn.delete_many({})

dbsh=mongo['deleted']
jsoon=dbsh['messi']
no=jsoon.count_documents({})
if no>=50000:
	jsoon.delete_many({})

dih=mongo['deleteds']
jsy=dih['messe']
file = "old_messages.json"
filed = "deleted_messages.json"

try:
    with open(file, "r") as f:
        old_messages = json.load(f)
except Exception:
    old_messages = {}

try:
    with open(filed, "r") as f:
        deleted_messages = json.load(f)
except Exception:
    deleted_messages = {}
#uyt=open("deleteds.txt","w").close()
def yoooo():
  listt=[]
  dell=open("deleteds.txt")
  for line in dell:
    listt.append(line.strip())
  return listt
#print(listt)
count=len(yoooo())
if count  >= 50000:
  open("deleteds.txt","w").close()
#uyt=open("deleted.txt","w").close()
def yoo():
  listtt=[]
  dell=open("deleted.txt")
  for line in dell:
    listtt.append(line.strip())
  return listtt
#print(listt)
count=len(yoo())
if count  >= 50000:
  open("deleted.txt","w").close()
#uyt=open("deletes.txt","w").close()
def yooo():
  listttt=[]
  dell=open("deletes.txt")
  for line in dell:
    listttt.append(line.strip())
  return listttt
#print(listt)
count=len(yooo())
if count  >= 50000:
  open("deletes.txt","w").close()
def print_exception(exc):
    print(repr(exc))

def is_staff(data):
    return data.authorId in admn

def is_black(data):
	if data.authorId in data.subClient.favorite_users:
		data.subClient.send_message(data.chatId,message="You are blocked from using Bot",replyTo=data.messageId)
		return
	else:
		return data.authorId not in data.subClient.favorite_users

def admins(data):
	return data.authorId in admn    

def join_community(comId: str = None, inv: str = None):
    if inv:
        try:
            client.join_community(comId=comId, invitationId=inv)
            return True
        except Exception as e:
            print_exception(e)
@client.command("dbm")
def dbm(data):
	jsn.delete_many({})
	jsoon.delete_many({})
	jsy.delete_many({})
	data.subClient.send_message(data.chatId,message="Deleted")
@client.command(condition=admins)
def addadmin(data):
	adm.append("{data.message}")
	data.subClient.send_message(data.chatId,message="Added {data.message} in admin list")


reddit = praw.Reddit(client_id = "l5zazwrEYIFpuhUJ1gQgzw", client_secret = "sJeGjJU5A8ooxoVXO8ya42fODif6EQ", username = "mr-cosmo-", password = "Neha@0305", user_agent = "alexa")

def get_memes(mySubreddit, posts_limit):
     posts = reddit.subreddit(mySubreddit).hot(limit = posts_limit)

     raw_list = []
     memes_links = []


     for post in posts:
         raw_list.append(post.url)

   

     for link in raw_list:
         if '.jpg' in link or '.png' in link: # Here I filter the links that contain only '.jpg' or '.png', because if we don't do this, videos are inserted into the urls.
             memes_links.append(link)

     return memes_links


@client.command('meme', condition=is_black)
def send_meme(data):


     memes = get_memes('meme', 200) # List of links.
     meme_index = random.randint(0, len(memes)) # To select random index meme.

     s=memes[meme_index]
     im=s.split("/")[-1]
     print(im)
     mem=urllib.request.urlretrieve(s, im)
     #meme = Image.open(requests.get(memes[meme_index], stream = True).raw)



     #Save meme.
     #meme.save(fr'./resources/RedditMemes/meme.{meme_index}.jpg')

     #OpenImage.
     #meme_open = open(fr'./resources/RedditMemes/meme.{meme_index}.jpg', 'rb')


     Image.open(im).resize((800,800)).save("imay.png")
     ff=open("imay.png","rb")
     msg=f"[B]Meme requested by {data.author}"
     data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
     os.remove("imay.png")
    # data.subClient.send_message(data.chatId, file = meme_open, fileType = 'image', embedTitle = f'{data.author}, a meme! haha', embedContent = f'Orslokx reddit meme', embedLink = 'htts ://reddit.com')




@client.command("choti")
def choti(data):
#	cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
	#cli.login(prox=proxies,email="ab",password="000")
	#id=(cli.get_from_code(data.message.split(' ')[0]).objectId)
	f=open("choti.mp3","rb")
	#sub=l_amino.SubClient(comId=data.comId,profile=cli.profile)
	data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
@client.command("biyah")
def biyah(data):
#	cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
	#cli.login(prox=proxies,email="ab",password="000")
	#id=(cli.get_from_code(data.message.split(' ')[0]).objectId)
	f=open("biyah.mp3","rb")
	ff=open("biya.gif","rb")
	#sub=l_amino.SubClient(comId=data.comId,profile=cli.profile)
	data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
	data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
@client.command("ily", condition=is_staff)
def ily(data):
	cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
	cli.login(prox=proxies,email="ab",password="000")
	id=(cli.get_from_code(data.message.split(' ')[0]).objectId)
	f=open("ily.mp3","rb")
	sub=l_amino.SubClient(comId=data.comId,profile=cli.profile)
	sub.send_message(chatId=id,file=f,fileType="audio")
@client.command("bhag")
def bhg(data):
	#cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
#	cli.login(prox=proxies,email="ab",password="000")
	#id=(cli.get_from_code(data.message.split(' ')[0]).objectId)
	if client.check(data,"admin"):
		f=open("bhag.mp3","rb")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)

@client.command("bol")
def bol(data):
	if client.check(data,"admin"):
		f=open("abbol.mp3","rb")
		ff=open("ab.gif","rb")
		data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)

def imggirl(data):
	y=requests.get("https://randomuser.me/api/1.4/?gender=female")
	h=(y.text)
	u=json.loads(h)
	o=(u["results"])
	for j in o:
		url=j["picture"]["large"]
		filename ="findgf.png"
		urllib.request.urlretrieve(url, filename)

def imgboy(data):
	y=requests.get("https://randomuser.me/api/1.4/?gender=male")
	h=(y.text)
	u=json.loads(h)
	o=(u["results"])
	for j in o:
		url=j["picture"]["large"]
		filename ="findbf.png"
		urllib.request.urlretrieve(url, filename)

def girlss(data):
  	p=randint(1,10)
  	listt=["Russian beautiful girl","Turkish beautiful girl","Mia Khalifa","American pretty girl","Beautiful indian girl","Pakistani beautiful girl","korean beautiful girl","russian girl","North indian girl","beautiful girl","sexy girl","chinese girl"]
  #	imfile= f"my_img{randint(1,500)}"
  	search = random.choice(listt)
  	gis = GoogleImagesSearch('AIzaSyB4Ekh8Z3Ie99Qt9V7Rui3dxbTJ0N2qXCc', '42e3ecc0e1ca6412f')
  	_search_params = {'q': search,'num': 10,'safe':'high'}
  	try:
  		gis.search(search_params=_search_params,path_to_dir='Girl')
  	except:
  		pass
  		

def boyss(data):
  #	imfile= f"my_img{randint(1,500)}"
  	listt=["Russian handsome boy","handsome indian boy","korean handsome boy","handsome american boy","korean man"]
  	search = random.choice(listt)
  	gis = GoogleImagesSearch('AIzaSyB4Ekh8Z3Ie99Qt9V7Rui3dxbTJ0N2qXCc', '42e3ecc0e1ca6412f')
  	_search_params = {'q': search,'num': 10,'safe':'high'}
  	try:
  		gis.search(search_params=_search_params,path_to_dir='Boy')
  	except:
  		pass

@client.command("findgf", condition=is_black)
def findgf(data):
	#data.subClient.send_message(data.chatId,message=
	#girlss(data)
	ship=(random.randint(18,25))
	girl=names.get_first_name(gender='female')
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if  mention!=None:
		for usd in mention:
				user=usd
	else:
		user=data.authorId
	nkkn=data.subClient.get_user_info(str(user)).nickname
	data.subClient.send_message(data.chatId,message=f"Finding girlfriend for <$@{nkkn}$> 👸",mentionUserIds=[str(user)])
	#girlss(data)
	#imggirl(data)
				#time.sleep(1)
	nkn=data.subClient.get_user_info(str(user)).nickname
	h=data.subClient.get_user_info(str(user)).icon
	response=requests.get(f"{h}")
	file=open(".axuale.png","wb")
	file.write(response.content)
	file.close()
	sel=random.choice(os.listdir("Girl"))
	img = Image.open(f"Girl/{sel}") 
	#img = Image.open("findgf.png") 
	img1 = Image.open(".axuale.png")
				#img9=Image.open("heart.png")
	img.size
	img1.size
				#img9.size
				#img91 = img9.resize((200,200))
	img_size = img.resize((400, 400))
	img1_size = img1.resize((400, 400))
	img2 = Image.new("RGB", (800, 400), "white")
	img2.paste(img_size, (0, 0))
	img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
	img2=img2.save(".img3.png")
	imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
	Image.open(imgg).resize((863,400)).save("nsks.png")
	ff=open("nsks.png","rb")
	msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Girlfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {nkn} 

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
	data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
	#os.remove("findgf.png")
	
	#shutil.rmtree("Girl")

@client.command("finjkjdgf")
def finjkdgf(data):
	#data.subClient.send_message(data.chatId,message=
	#girlss(data)
	ship=(random.randint(18,25))
	girl=names.get_first_name(gender='female')
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if  mention:
		for user in mention:
				nkkn=data.subClient.get_user_info(str(user)).nickname
				data.subClient.send_message(data.chatId,message=f"Finding girlfriend for <$@{nkkn}$> 👸",mentionUserIds=[str(user)])
				girlss(data)
				#time.sleep(1)
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axuale.png","wb")
				file.write(response.content)
				file.close()
				#x=data.subClient.get_user_info(data.authorId).icon
				#response=requests.get(f"{x}")
			#	file=open(".aikme.png","wb")
			#	file.write(response.content)
			#	file.close()
				sel=random.choice(os.listdir("Girl"))
				img = Image.open(f"Girl/{sel}") 
				img1 = Image.open(".axuale.png")
				#img9=Image.open("heart.png")
				img.size
				img1.size
				#img9.size
				#img91 = img9.resize((200,200))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nsks.png")
				ff=open("nsks.png","rb")
				msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Girlfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {nkn} 

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
				data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
				
		
		else:
				user=data.authorId
				data.subClient.send_message(data.chatId,message=f"Finding girlfriend for <$@{data.author}$> 👸",mentionUserIds=[str(user)])
				girlss(data)
				nkn=data.subClient.get_user_info(str(user)).nickname
				#h=data.subClient.get_user_info(str(user)).icon
			#	response=requests.get(f"{h}")
			#	file=open(".axuale.png","wb")
				#file.write(response.content)
				#file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aikme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aikme.png") 
				sel=random.choice(os.listdir("Girl"))
				img1 = Image.open(f"Girl/{sel}")
				#img9=Image.open("heart.png")
				img.size
				img1.size
				#img9.size
				#img91 = img9.resize((200,200))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nsks.png")
				ff=open("nsks.png","rb")
				msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Girlfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {data.author} baby 🥰

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
				data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)

@client.command("searchgirl", condition=is_black)
def searchgirl(data):
	ship=(random.randint(18,25))
	y=requests.get("https://randomuser.me/api/1.4/?gender=female")
	h=(y.text)
	u=json.loads(h)
	o=(u["results"])
	for j in o:
		url=j["picture"]["large"]
		filename ="newg.png"
		urllib.request.urlretrieve(url, filename)
		Image.open("newg.png").resize((600,600)).save("girln.png")
		ff=open("girln.png","rb")
		title=(j["name"]["title"])
		first=j["name"]["first"]
		last=j["name"]["last"]
		dob=j["dob"]["age"]
		loc=j["location"]["street"]["number"]
		adr=j["location"]["street"]["name"]
		City=j["location"]["city"]
		state=j["location"]["state"]
		coun=j["location"]["country"]
		msg=f"""[C]New Girl Found ✔️
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ Name : {title} {first} {last}
◈ Age : {ship}
◈ Address : {loc} {adr}
◈ City : {City}
◈ State : {state}
◈ Country : {coun}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
		data.subClient.full_embed("https://youtube.com/c/techvision7",ff,msg,data.chatId)
		os.remove("newg.png")
		os.remove("girln.png")
		

@client.command("divine")
def divine(data):
	f=open("divi.mp3","rb")
		
	ff=open("divine.gif","rb")
	data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
	data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	
@client.command("searchboy", condition=is_black)
def searchboy(data):
	ship=(random.randint(18,25))
	y=requests.get("https://randomuser.me/api/1.4/?gender=male")
	h=(y.text)
	u=json.loads(h)
	o=(u["results"])
	for j in o:
		url=j["picture"]["large"]
		filename ="newbb.png"
		urllib.request.urlretrieve(url, filename)
		Image.open("newbb.png").resize((600,600)).save("girlnn.png")
		ff=open("girlnn.png","rb")
		title=(j["name"]["title"])
		first=j["name"]["first"]
		last=j["name"]["last"]
		dob=j["dob"]["age"]
		loc=j["location"]["street"]["number"]
		adr=j["location"]["street"]["name"]
		City=j["location"]["city"]
		state=j["location"]["state"]
		coun=j["location"]["country"]
		msg=f"""[C]New Boy Found ✔️
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ Name : {title} {first} {last}
◈ Age : {ship}
◈ Address : {loc} {adr}
◈ City : {City}
◈ State : {state}
◈ Country : {coun}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
		data.subClient.full_embed("https://youtube.com/c/techvision7",ff,msg,data.chatId)
		os.remove("newbb.png")
		os.remove("girlnn.png")
		
	#data.subClient.full_embed("https://youtube.com/c/techvision7",ff,msg,data.chatId)
		
				
@client.command("findbf", condition=is_black)
def findbf(data):
	#data.subClient.send_message(data.chatId,message=
	#girlss(data)
	ship=(random.randint(18,25))
	girl=names.get_first_name(gender='male')
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if  mention!=None:
		for usd in mention:
				user=usd
	else:
		user=data.authorId
	nkkn=data.subClient.get_user_info(str(user)).nickname
	data.subClient.send_message(data.chatId,message=f"Finding boyfriend for <$@{nkkn}$> 😉",mentionUserIds=[str(user)])
	#imgboy(data)
				#time.sleep(1)
	nkn=data.subClient.get_user_info(str(user)).nickname
	h=data.subClient.get_user_info(str(user)).icon
	response=requests.get(f"{h}")
	file=open(".axuale.png","wb")
	file.write(response.content)
	file.close()
	sel=random.choice(os.listdir("Boy"))
	img = Image.open(f"Boy/{sel}")
	#img = Image.open("findbf.png")  
	img1 = Image.open(".axuale.png")
				#img9=Image.open("heart.png")
	img.size
	img1.size
				#img9.size
				#img91 = img9.resize((200,200))
	img_size = img.resize((400, 400))
	img1_size = img1.resize((400, 400))
	img2 = Image.new("RGB", (800, 400), "white")
	img2.paste(img_size, (0, 0))
	img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
	img2=img2.save(".img3.png")
	imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
	Image.open(imgg).resize((863,400)).save("nsks.png")
	ff=open("nsks.png","rb")
	msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Boyfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {nkn}

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
	data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
	#os.remove("findbf.png")
	#shutil.rmtree("Boy")			
@client.command("finjjdbf")
def finnndbf(data):
	#data.subClient.send_message(data.chatId,message=
	#boyss()
	ship=(random.randint(18,25))
	girl=names.get_first_name(gender='male')
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if  mention:
		for user in mention:
				nkkn=data.subClient.get_user_info(str(user)).nickname
				data.subClient.send_message(data.chatId,message=f"Finding boyfriend for <$@{nkkn}$> 🤴",mentionUserIds=[str(user)])
				boyss(data)
				#time.sleep(1)
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axuale.png","wb")
				file.write(response.content)
				file.close()
				#x=data.subClient.get_user_info(data.authorId).icon
				#response=requests.get(f"{x}")
			#	file=open(".aikme.png","wb")
			#	file.write(response.content)
			#	file.close()
				sel=random.choice(os.listdir("Boy"))
				img = Image.open(f"Boy/{sel}") 
				img1 = Image.open(".axuale.png")
				#img9=Image.open("heart.png")
				img.size
				img1.size
				#img9.size
				#img91 = img9.resize((200,200))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nsks.png")
				ff=open("nsks.png","rb")
				msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Boyfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {nkn} miss 😉

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
				data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
				
		
		else:
				user=data.authorId
				data.subClient.send_message(data.chatId,message=f"Finding boyfriend for <$@{data.author}$> 🤴",mentionUserIds=[str(user)])
				boyss(data)
				nkn=data.subClient.get_user_info(str(user)).nickname
				#h=data.subClient.get_user_info(str(user)).icon
			#	response=requests.get(f"{h}")
			#	file=open(".axuale.png","wb")
				#file.write(response.content)
				#file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aikme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aikme.png") 
				sel=random.choice(os.listdir("Boy"))
				img1 = Image.open(f"Boy/{sel}")
				#img9=Image.open("heart.png")
				img.size
				img1.size
				#img9.size
				#img91 = img9.resize((200,200))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				#img2.paste(img91,(360,150))
				
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nsks.png")
				ff=open("nsks.png","rb")
				msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[bc]♥️ Boyfriend Found ♥️

[BC]Name :{girl} 
[CB]Age : {ship}

[Bc]Message 💌 :Will you be mine {data.author} miss 😉

[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
				data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)				

@client.command("roadies")
def bhhg(data):
	if client.check(data,"admin"):
		f=open("roadies.mp3","rb")
		
		ff=open("bsdk.gif","rb")
		data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)
		
@client.command("bsdk")
def bjhg(data):
	if client.check(data,"admin"):
		f=open("chala.mp3","rb")
		
		ff=open("chal.gif","rb")
		data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)	

@client.command("nikal")
def bjhg(data):
	if client.check(data,"admin"):
		f=open("yahi.mp3","rb")
		
		ff=open("nika.gif","rb")
		data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)

@client.command("margya")
def bjhg(data):
	if client.check(data,"admin"):
		f=open("marg.mp3","rb")
		
		ff=open("mar.gif","rb")
		data.subClient.send_message(chatId=data.chatId,file=ff,fileType="gif")
		data.subClient.send_message(chatId=data.chatId,file=f,fileType="audio")
	else:
		data.subClient.send_message(data.chatId,message="Admin command",replyTo=data.messageId)

@client.command("harami", condition=is_staff)
def harami(data):
	cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
	cli.login(prox=proxies,email="ab",password="000")
	id=(cli.get_from_code(data.message.split(' ')[0]).objectId)
	f=open("harami.mp3","rb")
	sub=l_amino.SubClient(comId=data.comId,profile=cli.profile)
	sub.send_message(chatId=id,file=f,fileType="audio")
@client.command("special")
def special(data):
	#ch=open("deleteds.txt","r+")
	#cbs=ch.read()
	if client.check(data,"admin"):
		data.subClient.send_message(data.chatId,message="""
• margya
• bsdk
• biyah
• bol
• nikal 
• bhag
• roadies""")

@client.command("ravi", condition=is_staff)
def ravi(data):
	#ch=open("deleteds.txt","r+")
	#cbs=ch.read()
#	if client.check(data,"admin"):
	data.subClient.send_message(data.chatId,message="""
delmongo
cidlist
delcid""")

@client.command("sidchange",condition=is_staff)
def sidchange(data):
	try:
		sit.drop()
		time.sleep(1)
		it={"sid":data.message}
		sit.insert_one(it)
		data.subClient.send_message(chatId=data.chatId,message="Sid changed")
		#rebot()
	except:
		data.subClient.send_message(message="Error in sid",chatId=data.chatId)
def tm():
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	x=current_time=now.strftime("%H:%M")
	try:
		if x=="14:00":
			cli=l_amino.Client("425CB25E00B81AB606A3D68353F8D701FA713739CA6A3F068FC6F57357BE5F651FE6F1B6B0A1E4CE4C")
			cli.login("Loganpp2921@gmail.com","spamer123lodu")
			sid=cli.sid
			sit.drop()
			it={"sid":sid}
			sit.insert_one(it)
			print("Changed")
			#rebot()
		else:
			pass
	except:
		pass

@client.command("cdl")
def cdl(data):
	ch=open("deleteds.txt","r+")
	cbs=ch.read()
	data.subClient.send_message(data.chatId,message=cbs)
@client.command("ban", condition=is_black)
def ban(data):
        if client.check(data,"staff","admin"):
        	uid=(client.get_from_code(data.message.split(' ')[0]).objectId)
        	reason=None
        	try:
        		reason= ' '.join(data.message.split(' ')[1:])
        		if len(reason.split(' '))<3:
        			data.subClient.send_message(data.chatId,'Specify atleast 3 words for reason',replyTo=data.messageId)
        		else:
        			data.subClient.ban(uid,reason)
        			name=data.subClient.get_user_info(uid).nickname
        			data.subClient.send_message(data.chatId,f'Banned {name}',replyTo=data.messageId)
        	except:
        		data.subClient.send_message(data.chatId,'Specify reason for ban',replyTo=data.messageId)

@client.command("unban", condition=is_black)
def unban(data):
        if client.check(data,"admin","staff"):
        	uid=(client.get_from_code(data.message.split(' ')[0]).objectId)
        	reason=None
        	try:
        		reason= ' '.join(data.message.split(' ')[1:])
        		if len(reason.split(' '))<3:
        			data.subClient.send_message(data.chatId,'Specify atleast 3 words for reason',replyTo=data.messageId)
        		else:
        			data.subClient.unban(uid,reason)
        			name=data.subClient.get_user_info(uid).nickname
        			data.subClient.send_message(data.chatId,f'Unbanned {name}',replyTo=data.messageId)
        	except:
        		data.subClient.send_message(data.chatId,'Specify reason for unban',replyTo=data.messageId)

@client.command("strike", condition=is_black)
def strike_user(data):
	values=data
	if client.check(data,"admin","staff"):
		uid=(client.get_from_code(values.message.split(' ')[1]).objectId)
		reason=None
		try:
			time=int(values.message.split(' ')[0])
			reason= ' '.join(values.message.split(' ')[2:])
			if len(reason.split(' '))<3:
				data.subClient.send_message(values.chatId,'Specify atleast 3 words for reason',replyTo=values.messageId)
			elif time not in [1,3,6,12,24]:
				data.subClient.send_message(values.chatId,'Specify Valid hours for strike',replyTo=values.messageId)
			else:
				tdict={1:1,3:2,6:3,12:4,24:5}
				timd=tdict[time]
				values.subClient.strike(uid,timd,'Custom',reason)
				name=values.subClient.get_user_info(uid).nickname
				data.subClient.send_message(values.chatId,f'Striked {name} for {time} hours',replyTo=values.messageId)
		except:
			data.subClient.send_message(values.chatId,'Specify reason and time for Strike',replyTo=values.messageId)
@client.command("warn")
def warn_user(data):
	if client.check(data,"admin","staff"):
		uid=(client.get_from_code(data.message.split(' ')[0].split('/')[4]).objectId)
		reason=None
		try:
			reason= ' '.join(data.message.split(' ')[1:])
			if len(reason.split(' '))<3:
				data.subClient.send_message(data.chatId,'Specify atleast 3 words for reason',replyTo=data.messageId)
			else:
				data.subClient.warn(uid,reason)
				name=data.subClient.get_user_info(uid).nickname
				data.subClient.send_message(data.chatId,f'Warned {name}',replyTo=data.messageId)
		except:
			data.subClient.send_message(data.chatId,'Specify reason for Warn',replyTo=data.messageId)
@client.command("feature", condition=is_black)
def feature(data):
	if client.check(data,"admin","staff"):
		link=data.message.split(' ')[1]
		try:
			time=int(data.message.split(' ')[0])
			info=client.get_from_code(link.split('/')[4])
			objId=info.objectId
			objtype=info.objectType
			if objtype==0 and time in [1,2]:
				data.subClient.feature(time,userId=objId)
				data.subClient.send_message(data.chatId,f'Featured User for {time} days',replyTo=data.messageId)
			elif objtype==1 and time in [1,2,3]:
				data.subClient.feature(time,blogId=objId)
				data.lsubClient.send_message(data.chatId,f'Featured Blog for {time} days',replyTo=data.messageId)
			elif objtype==2 and time in [1,2,3]:
				data.subClient.feature(time,wikiId=objId)
				data.subClient.send_message(data.chatId,f'Featured Wiki for {time} days',replyTo=data.messageId)
			elif objtype==12 and time in [1,2,3]:
				data.subClient.feature(time,chatId=objId)
				data.subClient.send_message(data.chatId,f'Featured Chatroom for {time} hours',replyTo=data.messageId)
			elif objtype not in [0,1,2,12]:
				data.subClient.send_message(data.chatId,'Given link cannot be featured',replyTo=data.messageId)
			else:
				data.subClient.send_message(data.chatId,'Invalid time specified',replyTo=data.messageId)
		except:
			data.subClient.send_message(data.chatId,'Please specify time after the command. If you did specify a time already...then you tried featuring a post thats already featured.',replyTo=data.messageId)

@client.command("unfeature", condition=is_black)
def unfeature(data):
	values=data
	if client.check(data,"admin","staff"):
		link=values.message.split(' ')[1]
		try:
			info=client.get_from_code(link.split('/')[4])
			objId=info.objectId
			objtype=info.objectType
			if objtype==0:
				data.subClient.unfeature(userId=objId)
				data.subClient.send_message(data.chatId,f'UnFeatured User',replyTo=data.messageId)
			elif objtype==1:
				data.subClient.unfeature(blogId=objId)
				data.subClient.send_message(data.chatId,f'UnFeatured Blog',replyTo=data.messageId)
			elif objtype==2:
				data.subClient.unfeature(wikiId=objId)
				data.subClient.send_message(data.chatId,f'UnFeatured Wiki',replyTo=data.messageId)
			elif objtype==12:
				data.subClient.unfeature(chatId=objId)
				data.subClient.send_message(data.chatId,f'UnFeatured Chatroom',replyTo=data.messageId)
			elif objtype not in [0,1,2,12]:
				  data.subClient.send_message(data.chatId,'Given link cannot be Unfeatured',replyTo=data.messageId)
		except:
			data.subClient.send_message(data.chatId,'You probably tried to unfeature a post that wasnt featured.',replyTo=data.messageId)
@client.command("hide", condition=is_black)
def hide(data):
	#data=data
	if client.check(data,"admin","staff"):
		link=data.message.split(' ')[0]
		reason=None
		try:
			reason= ' '.join(data.message.split(' ')[1:])
			if len(reason.split(' '))<3:
				data.subClient.send_message(data.chatId,'Specify atleast 3 words for reason',replyTo=data.messageId)
			else:
				info=client.get_from_code(link.split('/')[4])
				objId=info.objectId
				objtype=info.objectType
				if objtype==0:
					data.subClient.hide(userId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'User Profile hidden',replyTo=data.messageId)
				elif objtype==1:
					data.subClient.hide(blogId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Blog disabled',replyTo=data.messageId)
				elif objtype==2:
					data.subClient.hide(wikiId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Wiki disabled',replyTo=data.messageId)
				elif objtype==12:
					data.subClient.hide(chatId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Chatroom Disabled',replyTo=data.messageId)
				elif objtype not in [0,1,2,12]:
					data.subClient.send_message(data.chatId,'Given link cannot be Disabled',replyTo=data.messageId)
		except:
			data.subClient.send_message(data.chatId,'Specify reason for hiding.',replyTo=data.messageId)
@client.command("unhide", condition=is_black)
def unhide(data):
	#data=data
	if client.check(data,"admin","staff"):
		link=data.message.split(' ')[0]
		reason=None
		try:
			reason= ' '.join(data.message.split(' ')[1:])
			if len(reason.split(' '))<3:
				data.subClient.send_message(data.chatId,'Specify atleast 3 words for reason',replyTo=data.messageId)
			else:
				info=client.get_from_code(link.split('/')[4])
				objId=info.objectId
				objtype=info.objectType
				if objtype==0:
					data.subClient.unhide(userId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'User Profile Enabled',replyTo=data.messageId)
				elif objtype==1:
					data.subClient.unhide(blogId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Blog enabled',replyTo=data.messageId)
				elif objtype==2:
					data.subClient.unhide(wikiId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Wiki enabled',replyTo=data.messageId)
				elif objtype==12:
					data.subClient.unhide(chatId=objId,reason=reason)
					data.subClient.send_message(data.chatId,f'Chatroom enabled',replyTo=data.messageId)
				elif objtype not in [0,1,2,12]:
					data.subClient.send_message(data.chatId,'Given link cannot be enabled',replyTo=data.messageId)
		except:
			data.subClient.send_message(data.chatId,'Specify reason for unhiding.',replyTo=data.messageId)


@client.command("sidch")
def sidch(data):
	os.remove("sids.txt")
	data.subClient.send_message(data.chatId,message="Sid removed")
	xs=client.sid
	file = open('sids.txt', 'w') 
	file.write(xs)
	file.close()
	data.subClient.send_message(data.chatId,message="sid changed")
	time.sleep(3)
	os.execv(sys.executable, ['python'] + sys.argv)
	data.subClient.send_message(data.chatId,message="Bot restarted")

@client.command("joinamino")
def join_amino(args):
    invit = None
    if not client.check(args,"admin"):
        args.subClient.send_message(args.chatId, "Admin command")
        return

    staff = args.subClient.get_staff(args.message)
    if not args.message:
        args.subClient.send_message(args.chatId, "Wrong amino ID!")
        return

    try:
        test = args.message.strip().split()
        amino_c = test[0]
        invit = test[1]
        invit = invit.replace("http://aminoapps.com/invite/", "")
    except Exception:
        amino_c = args.message
        invit = None

    try:
        val = Client().get_from_code(f"http://aminoapps.com/c/{amino_c}")
        comId=val.path[1:val.path.index("/")]
        f=open("cmds.txt","a")
        f.write(str(comId)+"\n")
        #comId = val.json["extensions"]["community"]["ndcId"]
    except Exception as e:
        print(e)
        val = ""

    isJoined = val.json["extensions"]["isCurrentUserJoined"]
    if not isJoined:
    	join_community(comId, invit)
    	val = client.get_from_code(f"http://aminoapps.com/c/{amino_c}")
    	isJoined = val.json["extensions"]["isCurrentUserJoined"]
    	if isJoined:
    	       Thread(target=client.threadLaunch, args=[comId, True]).start() 
    	       auth = client.get_community(comId).get_user_info(args.authorId).nickname 
    	       client.get_community(comId).ask_amino_staff(f"Hello! I am a bot and i can do a lot of stuff!\nI've been invited here by {auth}.\nIf you need help, you can do !help.\nEnjoy^^") 
    	       args.subClient.send_message(args.chatId, "Joined!") 
    	       return 
    	       args.subClient.send_message(args.chatId, "Waiting for join!")
    	       return
    else:
        args.subClient.send_message(args.chatId, "Allready joined!")
        return

key="68a18e14-8dec-4efb-ae37-69c0989739e4"
app_name="sumass9922"

@client.command("women", condition=is_black)
def women(data):
	f=open("women.gif","rb")
	
	data.subClient.send_message(data.chatId, file=f, fileType="gif")
	fd=open("woman.mp3","rb")
	data.subClient.send_message(chatId=data.chatId,file=fd,fileType="audio")

def calPercent(x, y, integer = True):
   percent = x / y * 100
   
   if integer:
       return int(percent)
   return percent

levels=[1,0,5,10,25,50,100,200,500,1000,2000,3000,5000,7000,10000,20000,40000,60000,100000,250000,500000]

@client.command("rank", condition=is_black)
def rank(data):
	
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if "aminoapps.com" in data.message:
	   user=(client.get_from_code(data.message.split(' ')[0]).objectId)
	elif mention!=None:
		for iix in mention:
		  user=iix
	else:
		user=data.authorId
	
	if data.chatId:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			vip=data.subClient.get_user_info(user).influencerInfo
			plus=data.subClient.get_user_info(user).accountMembershipStatus
			following=data.subClient.get_user_info(user).followingCount
			repa=data.subClient.get_user_info(user).reputation
			lvll=data.subClient.get_user_info(user).level
			frm=data.subClient.get_user_info(user).avatarFrame
			rolee=data.subClient.get_user_info(user).role
			nickss=data.subClient.get_user_info(user).nickname
			
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(user).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			levl=int(data.subClient.get_user_info(user).level)
			final=levels[(levl+1)]
			reep=int(data.subClient.get_user_info(userId=user).reputation)
			ix=reep #-int(levels[(levl)])
			iy=int(levels[(levl+1)]) #-int(levels[(levl)])
			percentage=calPercent(ix,iy)
			if frm!=None:
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,380))
			bg=Image.open("res.png").resize((800,800))
			pty="fame"
			isdir = os.path.isdir(pty)
			if isdir==True:
				fg=Image.open("fame/frame.png").resize((860,860))
				bg.paste(fg,(-30,-30),fg)
				bg.save("new.png")
				fhg="new.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			bgg.paste(bdg,(280,50),bdg)
			
			tiys=ImageFont.truetype("fonts/unifont-15.0.01.ttf",40)
			title_fot = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_font = ImageFont.truetype('fonts/ss.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{nickss}", (255, 255,255), font=tiys)
			draw.text((300,220), "Reputation :", (255, 0,0), font=title_font)
			#draw.text((540,220), "followers :", (255,0,0), font=title_font)
			draw.text((600,215), f"{repa}", (255,255,255), font=title_fn)
		#	draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
			#background = Editor("bg.png")
			bgg.save("ne.png")
			#ftf=open("ne.png","rb")
			background = Editor("ne.png")
			background.rectangle((30, 290), width=730, height=40, fill="white", radius=20)
			background.bar(
            (30, 290),
            max_width=730,
            height=40,
            percentage=percentage,
            fill="#FA8072",
            radius=20,
        )
			background.text((40,297), f"{ix}", font=ImageFont.truetype("fonts/unifont-15.0.01.ttf",40), color="black")
			background.text((645,297), f"{iy}", font=ImageFont.truetype("fonts/unifont-15.0.01.ttf",40), color="black")
			ftf=background.image_bytes
			msg=f"""[C]{nickss}"""
			data.subClient.full_embed("https://youtube.com/c/TechVision7",ftf,msg,data.chatId)
	os.remove("fame/frame.png")
	os.remove("fame/frame.webp")
	os.remove("config.json")

def restarts():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
afkdict={}
@client.command("afk", condition=is_black)
def countdown(data):
    global afkdict
    z=int(data.message)
    x=data.subClient.get_user_info(data.authorId).icon
    response=requests.get(f"{x}")
    file=open(".saue.png","wb")
    file.write(response.content)
    file.close()
    img = open(".saue.png","rb")
    afkdict[data.authorId] = data.message
    #data.subClient.add_muted_users(data.authorId)
    afklist.append(data.authorId)
    data.subClient.send_message(data.chatId,message=f"""
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
<$@{data.author}$>
you are on afk for {z} seconds
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",mentionUserIds=[data.authorId])
    t=0
    while t !=z:
    	mins, secs = divmod(t, 60)
    	timer = '{:02d}:{:02d}'.format(mins, secs)
    	print(timer, end="\r")
    	time.sleep(1)
    	t += 1
    print("timer done")
    afklist.remove(data.authorId)
    #data.subClient.remove_muted_users(data.authorId)
    data.subClient.send_message(data.chatId,message=f"""
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
<$@{data.author}‬‭$> ,Welcome Back🥳
your afk for {z} seconds completed,
You are no longer afk
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedImage=img,embedTitle=f"{data.author}",embedLink="ndc://x{data.comId}/user-profile/{data.authorId}",mentionUserIds=[data.authorId])
    
    
t=int(1)

    #rebot()
#t = int(1)

#@client.command("cbubble")
def cbuble(data):
	if not data.message:
		data.message=randint(1,80)
	if client.check(data,'staff','admin'):
		f=open("chatb.txt","r+")
		para=f.readlines()
		x=int(data.message)
		id=para[x].strip()
		data.subClient.apply_bubble(bubbleId=id,chatId=data.chatId,applyToAll=True)
		data.subClient.send_message(message="Chatbubble Applied",chatId=data.chatId,replyTo=data.messageId)
	else:
		data.subClient.send_message(message="Admin Command",chatId=data.chatId,replyTo=data.messageId)
		

		

#@client.command("snipe", condition=is_black)
def snpe(data):
    
    messages = data.subClient.get_chat_messages(data.chatId,20).messageId
    for m in messages:
    	try:
    		gy=deleted_messages[data.chatId][m]
    		#values_view = gy
    		#value_iterator = iter(values_view)
    		#first_value = next(value_iterator)
    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted message

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{gy}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    	except:
    		pass

@client.command("botstart",is_staff)
def botstart():
	os.remove("comid.txt")
	file=open("comid.txt","w")
	os.execv(sys.executable, ['python'] + sys.argv)
#@client.command("getdelete", condition=is_black)
def getdelete(data):
    
    messages = data.subClient.get_chat_messages(data.chatId,10).messageId
    for m in messages:
    	try:
    		data.subClient.send_message(data.chatId, deleted_messages[data.chatId][m])
    	except:
    		pass
@client.command("ping")
def ping(data):
	data.subClient.send_message(data.chatId,"hello")
@client.command(condition=is_black)
def startvideo(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		#data.subClient.send_message(data.chatId,message="Starting videocall in 5 seconds")
		#time.sleep(5)
		client.start_video_call(comId=data.comId,chatId=data.chatId)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats) :
			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} started Videocall in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="[i]Give me Cohost to start Videocall")
		pass


Device = "17925AEBB52F0AB6309A4D963914DD5ABBA536CE2ACC53643300942EF82983B504AF220835D92B95DB"

header  = {"NDCDEVICEID": Device}
header["NDCAUTH"] = f"sid={client.sid}"
header["Content-Type"] = "application/octet-stream"
def get_users_part_one(data,start: int):
    for s in range(0, start, 100):
        userId = data.subClient.get_all_users(start=s, size=100).profile.userId

        if not userId:
            break

        for uId in userId:
            if uId not in target_users:
                target_users.append(uId)
                print(f"[All Users List][{s}] Adding '{uId}'")

def get_users_part_two(data):
    for t in ["day", "hour", "rep", "check"]:
        userId = data.subClient.get_leaderboard_info(type=t, start=0, size=100).userId

        if not userId:
            break

        for uId in userId:
            if uId not in target_users:
                target_users.append(uId)
                print(f"[Leaderboard {t.upper()} Users List][0] Adding '{uId}'")

def get_users_part_three(data,start: int):
    for s in range(0, start, 100):
        userId = data.subClient.get_online_users(start=s, size=100).profile.userId

        if not userId:
            break

        for uId in userId:
            if uId not in target_users:
                target_users.append(uId)
                print(f"[Online Users List][{s}] Adding '{uId}'")

def Get_UrlZip_From_Message(d,comId,chatId,messageId):
	if int(comId) == 0:
		info = d.get_message_info(chatId=chatId,messageId=messageId).json
	else:
		#sub = data.subClient(comId,profile=client.profile)
		info =d.get_message_info(chatId=chatId,messageId=messageId).json
	ZipUrl = info["chatBubble"]["resourceUrl"]
	return ZipUrl

def SaveOrgBubble():
	try:
		open("org.zip").close()
	except FileNotFoundError:
		Bytes = requests.get("http://cb1.narvii.com/packages/8062/0c65bfe8bafe1efea9ea0e47280e403848cadfb9.zip").content
		file = open("org.zip","wb")
		file.write(Bytes)
		file.close()

def SaveNewBubble(Url):
	Bytes = requests.get(Url).content
	file = open("New.zip","wb")
	file.write(Bytes)
	file.close()

def CreateZip1(ReColor = False):
	api = "https://service.narvii.com/api/v1/g/s/media/upload/target/chat-bubble-thumbnail"
	headers = header
	headers["Content-Type"] = "image/*"
	Zip = zipfile.ZipFile("org.zip","r")
	Zip.extract("background.png")
	Zip = zipfile.ZipFile("New.zip","r")
	names = Zip.namelist()
	if str(names).count('.gif') > 1:
		print("\n Cannot Copy Bubble !")
	else:
		for name in set(names):
			if name.endswith(".gif") == True or name.endswith(".png") == True:
				ImgName = name
				Bytes = Zip.open(ImgName).read()
				Url = requests.post(api,headers=headers,data=Bytes).json()["mediaValue"]
		os.rename("background.png",ImgName)
		Zip.extract("config.json")
		file = open("config.json","r")
		data = json.load(file)
		data["name"] = "Banned#BubbleCopy"
		data["previewBackgroundUrl"] = Url
		data["coverImage"] = Url
		if ReColor:
			print("\n Enter Code Like This : #000000")
			color = input(" Color Code : ")
			linkColor = input(" linkColor Code : ")
			if color: data["color"] = color
			if linkColor: data["linkColor"] = linkColor
		file = open("config.json","w")
		data = json.dumps(data)
		file.write(data)
		file.close()
		Zip = zipfile.ZipFile("OldBubble.zip","w")
		Zip.write(ImgName)
		Zip.write("config.json")
		Zip.close()
		return ImgName

def CreateZip2(ImgName):
	Zip = zipfile.ZipFile("New.zip","r")
	Zip.extract(ImgName)
	Zip = zipfile.ZipFile("NewBubble.zip","w")
	Zip.write(ImgName)
	Zip.write("config.json")
	Zip.close()

def GenerateBubble():
	api1 = f"{client.api}/g/s/chat/chat-bubble/templates/949156e1-cc43-49f0-b9cf-3bbbb606ad6e/generate"
	data = open("OldBubble.zip","rb").read()
	res = requests.post(api1,headers=header,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		bubbleId = res.json()["chatBubble"]["bubbleId"]
		print(f"\n Template Done With Id ---> {bubbleId} \n")
		return bubbleId
		print(bubbleId)
	else:
		print('\n',res.json()["api:message"])

def Set_New_Bubble(bubbleId):
	api2 = f"{client.api}/g/s/chat/chat-bubble/{bubbleId}"
	data = open("NewBubble.zip","rb").read()
	res = requests.post(api2,headers=header,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		print(" Done Custom Bubble !")
	else:
		print('\n',res.json()["api:message"])
def icn(d,udd):
	try:
		d.subClient.invite_to_vc(userId=udd,chatId=d.chatId)
	except:
		pass
@client.command("setwall")
def setwall(args):
  if client.check(args,"staff","admin"):
  	data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  	reply_message = data.json['extensions']
  	if reply_message:
  		reply_message = data.json['extensions']['replyMessage']['content']
  		#print(reply_message)
  		#for msg in reply_message:
  		args.subClient.set_welcome_message(reply_message)
  		args.subClient.send_message(args.chatId,message=f"""Welcome Message Changed\n{reply_message}""")
  		rebot()
  else:
  			args.subClient.send_message(args.chatId,"Mod Command")

@client.command("banall", condition=is_staff)
def banall(data):
    data.subClient.send_message(data.chatId,"Started banning")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    	executor.submit(get_users_part_one, data, 1000)
    	time.sleep(45)
    	executor.submit(get_users_part_two)
    	executor.submit(get_users_part_three, data,1000)
    for uids in target_users:
    	try:
    		data.subClient.ban(userId=uids,reason="Admin")
    	except Exception:
    		pass
    	data.subClient.send_message(data.chatId,message=f"Banned {len(target_users)} users",replyTo=data.messageId)

def icn(d,udd):
	try:
		d.subClient.live_notify(userId=udd,chatId=d.chatId)
	except:
		pass

@client.command(condition=is_black)
def invitevc(data):
	h=data.subClient.get_online_users(start=0,size=100).profile.userId
	j=data.subClient.get_online_users(start=0,size=100).profile.nickname
	u=len(j)
	for ud in h:
		Thread(target=icn,args=(data,ud,)).start()
	data.subClient.send_message(chatId=data.chatId,message=f"Invited {u} users")
@client.command("copy",condition=is_black)
def copy(data):
	if client.check(data,"admin","staff"):
		d=data.subClient
		chatId = data.chatId
		comId = data.comId
		userId = data.authorId
		info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
		messageId = info.json["extensions"]["replyMessageId"]
		print("\n Get Message Id Done !")
		try:
			ZipUrl =  Get_UrlZip_From_Message(d,comId,chatId,messageId)
			SaveOrgBubble()
			SaveNewBubble(ZipUrl)
			ImgName = CreateZip1()
			bubbleId = GenerateBubble()
			CreateZip2(ImgName)
			Set_New_Bubble(bubbleId)
			#cb=open("chatb.txt","a+")
			#cb.write(bubbleId+"\n")
			#cb.close()
			data.subClient.send_message(data.chatId,message="Alexa Copied Bubble")
			print("\n Load Messages.. !")
		except Exception:
			data.subClient.send_message(data.chatId,message="100 Chatbubble Completed\nCan't copy more",replyTo=data.messageId)
	else:
		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)

		

Devicee = "17925AEBB52F0AB6309A4D963914DD5ABBA536CE2ACC53643300942EF82983B504AF220835D92B95DB"

def Get_Url_From_Message(d,comId,chatId,messageId):
	if int(comId) == 0:
		info = d.get_message_info(chatId=chatId,messageId=messageId).json
	else:
		#sub = data.subClient(comId,profile=client.profile)
		info =d.get_message_info(chatId=chatId,messageId=messageId).json
	ZipUrl = info["chatBubble"]["resourceUrl"]
	return ZipUrl

def SaveOrgBubble():
	try:
		open("org.zip").close()
	except FileNotFoundError:
		Bytes = requests.get("http://cb1.narvii.com/packages/8062/0c65bfe8bafe1efea9ea0e47280e403848cadfb9.zip").content
		file = open("org.zip","wb")
		file.write(Bytes)
		file.close()

def SaveNewBubble(Url):
	Bytes = requests.get(Url).content
	file = open("New.zip","wb")
	file.write(Bytes)
	file.close()

def CreateZip11(headr,ReColor = False):
	api = "https://service.narvii.com/api/v1/g/s/media/upload/target/chat-bubble-thumbnail"
	headers = headr
	headers["Content-Type"] = "image/*"
	Zip = zipfile.ZipFile("org.zip","r")
	Zip.extract("background.png")
	Zip = zipfile.ZipFile("New.zip","r")
	names = Zip.namelist()
	if str(names).count('.gif') > 1:
		print("\n Cannot Copy Bubble !")
	else:
		for name in set(names):
			if name.endswith(".gif") == True or name.endswith(".png") == True:
				ImgName = name
				Bytes = Zip.open(ImgName).read()
				Url = requests.post(api,headers=headers,data=Bytes).json()["mediaValue"]
		os.rename("background.png",ImgName)
		Zip.extract("config.json")
		file = open("config.json","r")
		data = json.load(file)
		data["name"] = "Banned#BubbleCopy"
		data["previewBackgroundUrl"] = Url
		data["coverImage"] = Url
		if ReColor:
			print("\n Enter Code Like This : #000000")
			color = input(" Color Code : ")
			linkColor = input(" linkColor Code : ")
			if color: data["color"] = color
			if linkColor: data["linkColor"] = linkColor
		file = open("config.json","w")
		data = json.dumps(data)
		file.write(data)
		file.close()
		Zip = zipfile.ZipFile("OldBubble.zip","w")
		Zip.write(ImgName)
		Zip.write("config.json")
		Zip.close()
		return ImgName

def CreateZip2(ImgName):
	Zip = zipfile.ZipFile("New.zip","r")
	Zip.extract(ImgName)
	Zip = zipfile.ZipFile("NewBubble.zip","w")
	Zip.write(ImgName)
	Zip.write("config.json")
	Zip.close()

def GenerateBubblee(cli,headr):
	api1 = f"{cli.api}/g/s/chat/chat-bubble/templates/71b41f1a-4c09-4e07-ac9e-18ef9bbbe65f/generate"
	data = open("OldBubble.zip","rb").read()
	res = requests.post(api1,headers=headr,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		bubbleId = res.json()["chatBubble"]["bubbleId"]
		print(f"\n Template Done With Id ---> {bubbleId} \n")
		return bubbleId
		print(bubbleId)
	else:
		print('\n',res.json()["api:message"])

def Set_New_Bubble1(cli,headr,bubbleId):
	api2 = f"{cli.api}/g/s/chat/chat-bubble/{bubbleId}"
	data = open("NewBubble.zip","rb").read()
	res = requests.post(api2,headers=headr,data=data)
	if res.status_code == 200 and res.json()["api:message"] == "OK":
		print(" Done Custom Bubble !")
	else:
		print('\n',res.json()["api:message"])

@client.command("copyb",condition=is_staff)
def copyb(data):
	if client.check(data,"admin"):
		#cli=l_amino.Client("426906322DE9C58CCD9453182641EE981E7CD6BE512F118A43813FF95F9CCB9CC07EE95D2C94F51B8C")
		#cli.login(prox=proxies,email="ab",password="000")
		headr  = {"NDCDEVICEID": Devicee}
		headr["NDCAUTH"] = f"sid={cli.sid}"
		headr["Content-Type"] = "application/octet-stream"
		d=data.subClient
		chatId = data.chatId
		comId = data.comId
		userId = data.authorId
		info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
		messageId = info.json["extensions"]["replyMessageId"]
		print("\n Get Message Id Done !")
		try:
			ZipUrl =  Get_Url_From_Message(d,comId,chatId,messageId)
			SaveOrgBubble()
			SaveNewBubble(ZipUrl)
			ImgName = CreateZip11(headr)
			bubbleId = GenerateBubblee(cli,headr)
			CreateZip2(ImgName)
			Set_New_Bubble1(cli,headr,bubbleId)
			#cb=open("chatb.txt","a+")
			#cb.write(bubbleId+"\n")
			#cb.close()
			data.subClient.send_message(data.chatId,message="Copied Bubble")
			print("\n Load Messages.. !")
		except Exception:
			data.subClient.send_message(data.chatId,message="100 Chatbubble Completed\nCan't copy more",replyTo=data.messageId)		
@client.command("cbubble", condition=is_black)
def cbubble(data):
	
	if client.check(data,'staff','admin'):
		list=[]
		ru=int(data.message)
		po=ru-1
		x=data.subClient.get_chat_bubbles(size=100)
		y=x["chatBubbleList"]
		for elem in y:
			z=elem["bubbleId"]
			list.append(z)
		id=list[po]
		data.subClient.apply_bubble(bubbleId=id,chatId=data.chatId,applyToAll=True)
		data.subClient.send_message(message="Chatbubble Applied",chatId=data.chatId,replyTo=data.messageId)
	else:
		data.subClient.send_message(message="Admin Command",chatId=data.chatId,replyTo=data.messageId)	
@client.command("delbubble", condition=is_black)
def delbubble(data):
	if not data.message:
		data.message=randint(1,10)
	if client.check(data,'admin'):
		list=[]
		x=data.subClient.get_chat_bubbles(size=100)
		y=x["chatBubbleList"]
		for elem in y:
			z=elem["bubbleId"]
			list.append(z)
		id=list[int(data.message)]
		data.subClient.delete_bubble(bubbleId=id)
		data.subClient.send_message(message="Chatbubble Deleted",chatId=data.chatId,replyTo=data.messageId)
	else:
		data.subClient.send_message(message="Admin Command",chatId=data.chatId,replyTo=data.messageId)
@client.command("checkbubble", condition=is_black)
def checkbubble(data):
	if not data.message:
		data.message=randint(1,10)
	if client.check(data,'staff','admin'):
		list=[]
		x=data.subClient.get_chat_bubbles(size=100)
		y=x["chatBubbleList"]
		for elem in y:
			z=elem["coverImage"]
			list.append(z)
		id=list[int(data.message)]
		#data.subClient.apply_bubble(bubbleId=id,chatId=data.chatId,applyToAll=True)
		data.subClient.send_message(message=f"""[cu]ᴄʜᴀᴛʙᴜʙʙʟᴇ ᴄᴏᴠᴇʀ ɪᴍᴀɢᴇ

{id}

""",chatId=data.chatId)
	else:
		data.subClient.send_message(message="Admin Command",chatId=data.chatId,replyTo=data.messageId)
	
#@client.command("cbid")
def cbid(data):
	ch=open("chatb.txt","r+")
	cbs=ch.read()
	data.subClient.send_message(data.chatId,message=cbs)

@client.command(condition=is_black)
def endvideo(data):
	data.subClient.send_message(data.chatId,message="Ending videocall in 5 seconds")
	time.sleep(5)
	client.end_vc(comId=data.comId,chatId=data.chatId)
	#now = datetime.now()
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
	#current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
	#current_time = now.strftime("%H:%M:%S")
	#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
	if kt!=None:
		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
	else:
		chatlink="Private Chat"
	val=data.subClient.get_chat_thread(data.chatId).title
	chats=data.subClient.favorite_chats
	if val ==None:
		val="Private Chat"
	for id, in zip(chats) :
		data.subClient.send_message(chatId=id,message=f"""[c]{data.author} ended Videocall in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")

@client.command(condition=is_black)
def endlive(data):
	data.subClient.send_message(data.chatId,message="Ending live in 5 seconds")
	time.sleep(5)
	client.end_vc(comId=data.comId,chatId=data.chatId)
	#now = datetime.now()
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
	#current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
	#current_time = now.strftime("%H:%M:%S")
	#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
	if kt!=None:
		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
	else:
		chatlink="Private Chat"
	val=data.subClient.get_chat_thread(data.chatId).title
	chats=data.subClient.favorite_chats
	if val ==None:
		val="Private Chat"
	for id, in zip(chats) :
		data.subClient.send_message(chatId=id,message=f"""[c]{data.author} ended live in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")


@client.command("rimage")
def rimage(data):
	paths="youimage.png"
	os.remove(paths)
	data.subClient.send_message(data.chatId,message="Image removed")		



def icn(d,udd):
	try:
		d.subClient.invite_to_chat(userId=udd,chatId=d.chatId)
	except:
		pass
		

@client.command(condition=is_black)
def inviteall(data):
	h=data.subClient.get_online_users(start=0,size=100).profile.userId
	j=data.subClient.get_online_users(start=0,size=100).profile.nickname
	u=len(j)
	for ud in h:
		Thread(target=icn,args=(data,ud,)).start()
	data.subClient.send_message(chatId=data.chatId,message=f"Invited {u} members in Chatroom")

@client.command("ytr")
def ytr(data):
	os.remove("youtube.txt")
	data.subClient.send_message(data.chatId,message="Link removed")




@client.command("linknew")
def linknew(data):
	k=data.message
	lin=open("youtube.txt", "w")
	lin.write(f"{k}")
	lin.close()
	data.subClient.send_message(data.chatId,message=f"Link changed to {k}")	
@client.command("muteall", condition=is_staff)
def muteall(data):
	q=data.subClient.get_chat_users(chatId=data.chatId,size=1000).userId
	for user in q:
		data.subClient.add_muted_users(user)
	data.subClient.send_message(data.chatId,message="Muted all members in chat")
	#rebot()
	
@client.command("blockall", condition=is_staff)
def blockall(data):
	q=data.subClient.get_chat_users(chatId=data.chatId,size=1000).userId
	for user in q:
		data.subClient.add_favorite_users(user)
		#data.subClient.add_muted_users(user)
	data.subClient.send_message(data.chatId,message="Blocked all members in chat")
	rebot()
	
@client.command("unmuteall", condition=is_staff)
def unmuteall(data):
	q=data.subClient.muted_users
	for user in q:
		data.subClient.remove_muted_users(user)
	data.subClient.send_message(data.chatId,message="Unmuted all members")
	rebot()
	
	
@client.command("unblockall", condition=is_staff)
def unblockall(data):
	q=data.subClient.favorite_users
	for user in q:
		data.subClient.remove_favorite_users(user)
	data.subClient.send_message(data.chatId,message="Unblocked all members")
	rebot()		

@client.command("ytv")
def ytv(data):
	filess = open('youtube.txt', 'w') 
	filess.write(f'{data.message}')
	filess.close()
	data.subClient.send_message(data.chatId,message="youtube link changed")

@client.command("fact", condition=is_black)
def fact(data):
	start = "Did you know that "
	facts = ["Banging your head against a wall for one hour burns 150 calories.",
                 "Snakes can help predict earthquakes.",
                 "7% of American adults believe that chocolate milk comes from brown cows.",
                 "If you lift a kangaroo’s tail off the ground it can’t hop.",
                 "Bananas are curved because they grow towards the sun.",
                 "Billy goats urinate on their own heads to smell more attractive to females.",
                 "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
                 "During your lifetime, you will produce enough saliva to fill two swimming pools.",
                 "Polar bears could eat as many as 86 penguins in a single sitting…",
                 "Heart attacks are more likely to happen on a Monday.",
                 "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
                 "A lion’s roar can be heard from 5 miles away.",
                 "The United States Navy has started using Xbox controllers for their periscopes.",
                 "A sheep, a duck and a rooster were the first passengers in a hot air balloon.",
                 "The average male gets bored of a shopping trip after 26 minutes.",
                 "Recycling one glass jar saves enough energy to watch television for 3 hours.",
                 "Approximately 10-20% of U.S. power outages are caused by squirrels."]
	fact_file = open("facts.txt", mode="r", encoding="utf8")
	fact_file_facts = fact_file.read().split("\n")
	fact_file.close()
	for i in fact_file_facts:
		if i == "": fact_file_facts.remove(i)
	facts = facts + fact_file_facts
	data.subClient.send_message(data.chatId,message=f"""
[C]{start}
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[i]{(random.choice(facts).lower())}

[C]𐄁𐄙??𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command("reb",condition=is_staff)
def reb(data):
	#data.subClient.send_message(data.chatId,message="Reboot started")
	restarts()
@client.command("blocklist", condition=is_black)
def blocklist(data):
	o=""
	q=data.subClient.favorite_users
	if q:
		for us in q:
			uid=data.subClient.get_user_info(us).nickname
			o=o+uid+"\n"
		data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Blocked Users
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄙𐄁""")
	else:
		data.subClient.send_message(data.chatId,message="No blocked user")
@client.command("mutelist", condition=is_black)
def mutelist(data):
	o=""
	q=data.subClient.muted_users
	if q:
		for us in q:
			uid=data.subClient.get_user_info(us).nickname
			o=o+uid+"\n"
		data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Muted Users
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄙𐄁""")
	else:
		data.subClient.send_message(data.chatId,message="No muted user")
@client.command("onlinemem", condition=is_black)
def onlinemem(data):
	o=""
	q=data.subClient.get_online_users(start=0,size=100)
	for uid in q.profile.nickname:
		o=o+uid+"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Online Members
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command("chatlist")
def chatlist(args):
    if client.check(args,'staff', 'admin'):
        o=""
        val = args.subClient.get_chats().title
        for title in val:
        	o=o+title+"\n"
        args.subClient.send_message(args.chatId, f"""
[c]CHAT LIST
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command("chatmem", condition=is_black)
def chatmem(data):
	o=""
	q=data.subClient.get_chat_users(chatId=data.chatId,size=1000).nickname
	for uid in q:
		o=o+uid+"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]GC Members
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
@client.command("kickall", condition=is_staff)
def kickall(data):
	q=data.subClient.get_chat_users(chatId=data.chatId,size=1000).userId
	for user in q:
		try:
			data.subClient.kick(chatId=data.chatId, userId=user, allowRejoin=True)
		except:
			pass
	data.subClient.send_message(data.chatId,message="Kicked all members")

from alice import chatbot

@client.command("ai", condition=is_staff)
def ai(data):
    chatbot_ai=chatbot()
    message=f"{data.message}"
    response=chatbot_ai.text(message)
    data.subClient.send_message(data.chatId, message=f"{response}", replyTo=data.messageId)

live_vc = False
@client.command("screening", condition=is_black)
def screening(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		global live_vc
		live_vc = True
		while live_vc:
			try:
				client.play_video(data.comId,data.chatId)
				time.sleep(10)
				if live_vc == False:
				    break
			except Exception:
				return
	else:
		data.subClient.send_message(data.chatId,message="I need Cohost to start")


@client.command("startsc", condition=is_black)
def startsc(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		global live_vc
		live_vc = True
		while live_vc:
			try:
				client.play_video(data.comId,data.chatId)
				time.sleep(10)
				if live_vc == False:
				    break
			except Exception:
				return
	else:
		data.subClient.send_message(data.chatId,message="I need Cohost to start")

@client.command("repinfo",condition=is_black)
def repinfo(data):
	x = data.subClient.get_vc_reputation_info(chatId=data.chatId).availableReputation
	data.subClient.send_message(data.chatId, message=f"Available Reputation : {x}")

@client.command("lurkers", condition=is_black)
def lurkers(args):
    list=[]
    members = args.subClient.get_chat_lurkers()['userInfoInThread'][args.chatId]
    names = [name['nickname'] for name in members['userProfileList']]
    count = members['userProfileCount']
    #users = args.subClient.get_live_layer().json[0]["userProfileList"]
    for user in names:
    	i=user
    	list.append(i)
    val = ""
    if list:
        for elem in list:
            val +="◈" + elem + "\n"
    else:
        val = "No Lurkers"
    args.subClient.send_message(args.chatId, message=f"""
[bc]Lurkers : {count}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command()
def lurk(data):
    members = data.subClient.get_chat_lurkers()['userInfoInThread'][data.chatId]
    names = [name['nickname'] for name in members['userProfileList']]
    count = members['userProfileCount']
    mes= f'[bc]Lurkers : {count}\n\n'
    for i in names:
        mes += f'◈ {i}\n'
    data.subClient.send_message(data.chatId,mes)


@client.command("claimrep",condition=is_black)
def claimrep(data):
    duplicates=[]
    data.subClient.send_message(data.chatId, "Claim started")
    while True:
        x = data.subClient.get_vc_reputation_info(data.chatId)
        time.sleep(5)
        rep=x.availableReputation
        duplicates.append(int(rep))
        if rep >=10:
            x = data.subClient.claim_vc_reputation(data.chatId)
            duplicates.clear()
        g=duplicates.count(rep)
        if g >=6:
          data.subClient.claim_vc_reputation(data.chatId)
          duplicates.clear()	

@client.command("qa", condition=is_black)
def qa(data):
	#data = data.subClient.get_message_info(chatId = data.chatId,messageId = data.messageId)
	#reply_message = data.json['extensions']
	lis = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful","yes","No" ,"Probably","100%", "Not sure"]
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)),replyTo=data.messageId)



@client.command(condition=is_black)
def startvc(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		#data.subClient.send_message(data.chatId,message="Starting vc in 5 seconds")
		#time.sleep(5)
		client.start_vc(comId=data.comId,chatId=data.chatId)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats) :
			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} started VC in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"Profile link",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="I need Co-Host to start VC")
		pass

@client.command(condition=is_black)
def startlive(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		#data.subClient.send_message(data.chatId,message="Starting vc in 5 seconds")
		#time.sleep(5)
		client.start_vc(comId=data.comId,chatId=data.chatId)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats) :
			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} started VC in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"Profile Link",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="I need Co-Host to start VC")
		pass

@client.command("scbnreening", condition=is_black)
def scrneening(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if client.userId in cho or client.userId==x:
		client.play_video(data.comId,data.chatId)
	else:
		data.subClient.send_message(data.chatId,message="I need Cohost to start")
		


@client.command("joinscreen", condition=is_black)
def joinscreen(data):
	client.join_screen_room(data.comId,data.chatId,joinType=1)

@client.command("endvc",condition=is_black)
def endvc(data):
	global live_vc
	live_vc = False
	data.subClient.send_message("Ending live in 5 seconds")
	time.sleep(5)
	client.end_vc(comId=data.comId,chatId=data.chatId)

@client.command(condition=is_black)
def checkin(data):
	client.check_all()
	data.subClient.send_message(data.chatId,message='Alexa Checked in all communities')

@client.command(condition=is_black)
def pm(data):
	data.subClient.start_chat(data.authorId,message=f"[i]Hey {data.author}\nAlexa here...how are you!")
	data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> check your pm",replyTo=data.messageId,mentionUserIds=[data.authorId])

@client.command(condition=is_black)
def admnlist(data):
	msg="""[c]Bot Admin
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
https://aminoapps.com/u/Ravi712
https://aminoapps.com/u/sylric
https://aminoapps.com/u/kaushikjaiswal2347
https://aminoapps.com/u/Futuredoctor806
https://aminoapps.com/u/Samiksha53
https://aminoapps.com/u/Kwel99928
https://aminoapps.com/u/Daddy59657984611
https://aminoapps.com/u/anony217887395811
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
	data.subClient.send_message(data.chatId,message=msg)

@client.command(condition=is_black)
def kicks(args):
	x=args.subClient.get_user_info(userId=client.userId).json["role"]
	with suppress(Exception):
	       if (x==100,x==101):
	       	args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Clear")
	       	list = []
	       	chatMembers = args.subClient.get_chat_users(chatId=args.chatId,start=0,size=50).nickname
	       	for i in range(5):
	       	 member = random.choice(chatMembers)
	       	 args.subClient.send_message(args.chatId,message=f"{member} has left the conversation.", messageType=109)
	       	 list.append(member)
	       else:
	      		args.subClient.send_message(args.chatId,message="[i]I don't have Curator or Leader")
	      		pass
	      		
def adver(data):
  	content=data.message
  	bnn=["t.me/"]
  	
  	if "aminoapps.com/c" in content or "aminoapps.com/p" in content:
  	 lvl=data.subClient.get_user_info(data.authorId).level
  	 info = client.get_from_code(content)
  	 comid = info.path[1:info.path.index("/")]
  	 if comid != f'{data.comId}':
  	   	 rol=data.subClient.get_user_info(userId=data.authorId).json["role"]
  	   	 if rol==0 and lvl<=13:
  	   	 	try:
  	   	 		data.subClient.ban(userId=data.authorId,reason="Advertising in community")
  	   	 		tz = pytz.timezone('Asia/Kolkata')
  	   	 		now = datetime.now(tz)
  	   	 		current_time=now.strftime("%H:%M:%S")
  	   	 		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
  	   	 		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
  	   	 		if kt!=None:
  	   	 			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
  	   	 			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
  	   	 		else:
  	   	 			chatlink="Private Chat"
  	   	 		val=data.subClient.get_chat_thread(data.chatId).title
  	   	 		chats=data.subClient.favorite_chats
  	   	 		if val ==None:
  	   	 			val="Private Chat"
  	   	 		for id, in zip(chats):
  	   	 			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} got banned for advertising
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Time : {current_time}""",embedTitle=f"Profile link",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {val}")
  	   	 	except:
  	   	 		pass


@client.command("delcid", condition=is_staff)
def delcid(data):
	c=str(data.message)
	try:
		test_1.delete_one({"comid":c})
		data.subClient.send_message(message=f"Deleted {data.message}",chatId=data.chatId,replyTo=data.messageId)
	except:
		data.subClient.send_message(message="Not working",chatId=data.chatId,replyTo=data.messageId)
		pass
		
@client.command("adminlist", condition=is_black)
def adminlist(data):
	o=""
	q=client.perms_list
	for us in q:
		AID=client.get_user_info(userId=us).aminoId
		uid=f"https://aminoapps.com/u/{str(AID)}"
		o=o+uid+"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Bot Admin
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

#@client.on_all()
def on_mage(data):
    try:
    	user_id=data.authorId
    	AID=client.get_user_info(userId=user_id).aminoId
    	val=data.subClient.get_chat_thread(data.chatId).title
    	ch=data.subClient.favorite_chats
    	tz = pytz.timezone('Asia/Kolkata')
    	now = datetime.now(tz)
    	current_time=now.strftime("%H:%M:%S")
    	chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
    	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
    	x=data.subClient.get_user_info(data.authorId).json['role']
    	y=data.subClient.get_chat_thread(data.chatId).json["uid"]
    	if user_id !=client.userId and x==0:
    		if user_id !=y and user_id not in cho:
    			mtype = data.info.message.type
    			if (mtype==109 or mtype==107):
    			     	try:
    			     		data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
    			     		for id in ch:
    			     			data.subClient.send_message(chatId=id,message=f"""[c]Ghost spam by {data.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[cu]GlobalId
[c]"https://aminoapps.com/u/"+{str(AID)}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    			     	except:
    			     		pass
    except:
    	pass


def mewt(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		if user in afklist and data.authorId!=client.userId:
			h=data.subClient.get_user_info(userId=str(user)).nickname
			data.subClient.send_message(data.chatId,message=f"<$@{h}$> is on afk mode",mentionUserIds=[str(user)],replyTo=data.messageId)
		else:
			pass
			
akf=mongo["timee"]
cfk=akf["timer"]

@client.command("afkmode", condition=is_black)
def afkmode(data):
	nowt=time.time()
	rs=cfk.find_one({"id":data.authorId})
	
	if rs==None:
		it={"id":data.authorId,"date":nowt}
		cfk.insert_one(it)
		data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> afk mode started",mentionUserIds=[data.authorId])
		#rebot()
	else:
		pass
		

def aaffk(data):
	#current=datetime.now()
	noi=time.time()
	rss=cfk.find_one({"id":data.authorId})
	usd=rss["id"]
	if data.authorId==usd:
		dd=rss["date"]
		start_ts_ = dateh.fromtimestamp(dd)
		end_ts = dateh.fromtimestamp(noi)
		delta = end_ts - start_ts_
		secon=delta.total_seconds()
		min, sec = divmod(secon, 60)
		hour, min = divmod(min, 60)
		hr=int(hour)
		mn=int(min)
		ss=int(sec)
		if secon>=5:
			data.subClient.send_message(data.chatId,message=f"""[cb]<$@{data.author}$>
[c]You were on afk for
[cb]{hr} H : {mn} M : {ss} S
""",mentionUserIds=[data.authorId])
			cfk.delete_one({"id":data.authorId})
			
		#rebot()
	else:
		pass


@client.on_all() #new created
def maihu(data):
	
	it={'ids':data.messageId,'userid':data.authorId,'link':data.message}
	jsoon.insert_one(it)
	#aaffk(data)
	try:
		x=data.info.json
		elem=(x["chatMessage"])
		mv=elem["mediaValue"]
		md=elem["messageId"]
		ud=elem["uid"]
		its={'sd':md,'userid':ud,'link':mv}
		jsn.insert_one(its)
	except:
		pass
	if data.authorId in data.subClient.muted_users:
		data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="muted user")
	else:
		pass
#	jsy.insert_one(it)
	if data.authorId in afklist:
		data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="muted user")
		#data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> your afk in on",mentionUserIds=[str(data.authorId)])
	else:
		pass
	
	#try:
	#	mewt(data)
#	except:
		pass
	nioo=jsy.count_documents({})
	if nioo>=50000:
		jsy.delete_many({})
	else:
		pass
	try:
		adver(data)
	except:
		pass
	noo=jsn.count_documents({})
	if noo>=50000:
		jsn.delete_many({})
	else:
		pass
	no=jsoon.count_documents({})
	if no>=50000:
		jsoon.delete_many({})
	else:
		pass
	
	aaffk(data)
	#with suppress(Exception):
	try:
		time.sleep(30)
		#	dm=["Chatting"]
		client.show_online(data.comId)
			#client.send_action(actions=dm,comId=data.comId,chatId=data.chatId)
	except:
		pass    	
    	    	
#@client.on_all() #real on all hai ye
def tex_mege(data):
  x=data.info.json
  elem=(x["chatMessage"])
  try:
  	mv=elem["mediaValue"]
  	md=elem["messageId"]
  	ud=elem["uid"]
  	it={'sd':md,'userid':ud,'link':mv}
  	jsn.insert_one(it)
  except:
  	pass
  if data.authorId in data.subClient.muted_users:
  	data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="muted user")
  else:
  	pass   	
#client.on_all()
def text_mege(data):
  x=data.info.json
  elem=(x["chatMessage"])
  try:
  	mv=elem["mediaValue"]
  	md=elem["messageId"]
  	ud=elem["uid"]
  	it={'sd':md,'userid':ud,'link':mv}
  	jsn.insert_one(it)
  except:
  	pass
  
  #vl=data.subClient.get_chat_thread(data.chatId).title
  try:
    	mt=[114,109,107,115,116,110,111,112,113,114,117,124,125,126,128,1,50,51,57,58,59]
    	user_id=data.authorId
    	AID=client.get_user_info(userId=user_id).aminoId
    	val=data.subClient.get_chat_thread(data.chatId).title
    	ch=data.subClient.favorite_chats
    	tz = pytz.timezone('Asia/Kolkata')
    	now = datetime.now(tz)
    	current_time=now.strftime("%H:%M:%S")
    	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
    	#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
    	if kt !=None:
    		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
    		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    	else:
    		chatlink="Private Chat"
    	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
    	rol=data.subClient.get_user_info(data.authorId).json['role']
    	if user_id !=client.userId and rol==0:
    		mtype = data.info.message.type
    		if mtype in mt and data.message != None:
    			try:
    				data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
    				data.subClient.ban(userId=data.authorId,reason="Ghost spam")
    			except:
    				pass
    			for id in ch:
    				data.subClient.send_message(chatId=id,message=f"""[c]Banned {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Reason : Ghost Spam
Chat : {chatlink}
GlobalId: https://aminoapps.com/u/{str(AID)}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
  except:
    	pass
  with suppress(Exception):
  	content=data.message
  	bnn=["t.me/"]
  	
  	if "aminoapps.com/c" in content or "aminoapps.com/p" in content:
  	 lvl=data.subClient.get_user_info(data.authorId).level
  	 info = client.get_from_code(content)
  	 comid = info.path[1:info.path.index("/")]
  	 if comid != f'{data.comId}' or bnn in content:
  	   	 rol=data.subClient.get_user_info(userId=data.authorId).json["role"]
  	   	 if rol==0 and lvl<=5:
  	   	 	try:
  	   	 		data.subClient.ban(userId=data.authorId,reason="Advertising in community")
  	   	 		tz = pytz.timezone('Asia/Kolkata')
  	   	 		now = datetime.now(tz)
  	   	 		current_time=now.strftime("%H:%M:%S")
  	   	 		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
  	   	 		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
  	   	 		if kt!=None:
  	   	 			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
  	   	 			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
  	   	 		else:
  	   	 			chatlink="Private Chat"
  	   	 		val=data.subClient.get_chat_thread(data.chatId).title
  	   	 		chats=data.subClient.favorite_chats
  	   	 		if val ==None:
  	   	 			val="Private Chat"
  	   	 		for id, in zip(chats):
  	   	 			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} got banned for advertising
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Time : {current_time}""",embedTitle=f"Profile link",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {val}")
  	   	 	except:
  	   	 		pass

@client.command(condition=is_black)
def comid(data):
	n=data.message
	fok=client.get_from_code(n)
	id=client.get_from_code(n).objectId
	cid=fok.path[1:fok.path.index("/")]
	data.subClient.send_message(chatId=data.chatId,message=f"Community Id = {cid}")

@client.command("kick")
def kick(data):
  mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
  if client.check(data,"staff","admin"):
  	if mention!=None:
  		for user in mention:
  			try:
  				data.subClient.kick(chatId=data.chatId, userId=user, allowRejoin=True)
  			except:
  				data.subClient.send_message("I don't have mod or cohost",chatId=data.chatId,replyTo=data.messageId)
  				pass
  	else:
  			data.subClient.send_message("Mention user",data.chatId,replyTo=data.messageId)
  else:
  		data.subClient.send_message("Admin/Staff Command",data.chatId,replyTo=data.messageId)


@client.command("kck", condition=is_black)
def kck(data):
  data.subClient.send_message(data.chatId,message="Turned off",replyTo=data.messageId)
@client.command("cid")
def cid(data):
  data.subClient.send_message(data.chatId,message=f"{data.comId}",replyTo=data.messageId)	    	   	
  
@client.command("announce")
def announce(args):
    if client.check(args,'staff','admin'):
    	try:
    		str=args.message
    		str_en = str.encode("ascii", "ignore")
    		str_de = str_en.decode()
    		val = args.subClient.get_chat_threads(start=0,size=100).chatId
    		#print(val)
    		val3=args.subClient.get_chat_thread(args.chatId).title
    		tz = pytz.timezone('Asia/Kolkata')
    		if val3 ==None:
    			val3="Private Chat"
    		now = datetime.now(tz)
    		current_time=now.strftime("%H:%M:%S")
    		for g in val:
            			args.subClient.send_message(chatId=g,message=f"""
[c] Announcement
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{str_de}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val3}")
    	except Exception:
    		pass

@client.command("announcement")
def announcement(args):
    if client.check(args,'staff','admin'):
    	try:
    		str=args.message
    		str_en = str.encode("ascii", "ignore")
    		str_de = str_en.decode()
    		val = args.subClient.get_chat_threads(start=0,size=100).chatId
    		#print(val)
    		val3=args.subClient.get_chat_thread(args.chatId).title
    		tz = pytz.timezone('Asia/Kolkata')
    		now = datetime.now(tz)
    		current_time=now.strftime("%H:%M:%S")
    		for g in val:
            			args.subClient.send_message(chatId=g,message=f"""{args.message}""")
    	except Exception:
    		pass


@client.command(condition=is_black)
def hack(data):
	it=randint(500,2000)
	ist=randint(50,630)
	iss=randint(10,40)
	o=randint(1,9)
	v=randint(23,98)
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		repa= data.subClient.get_user_info(userId=str(user)).reputation
		h=data.subClient.get_user_info(userId=str(user)).nickname
		lvl = data.subClient.get_user_info(userId=str(user)).level
		crttime = data.subClient.get_user_info(userId=str(user)).createdTime
		followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
		profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
		commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
		posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
		followed = data.subClient.get_user_info(userId=str(user)).followingCount
		#data.subClient.send_message(data.chatId,message="Are you sure(Y/N)")
		#time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"Started Loading {h}'s profile....")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Collecting device IP........")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"{h}'s device IP address 192.158.{o}.{v}")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"""
{h}'s profile loaded

Nickname: {h}
UserId: {str(user)}
Account created time: {crttime}
Profile changed: {profilchange}
Reputation number: {repa}
Account level: {lvl}
Number of posts created: {posts}
Number of comments on the wall: {commentz}
Number of User you follow: {followed}
Account followers: {followers}""")
		data.subClient.send_message(data.chatId,message="System files loading.....")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"{it} chats found from {h}'s account")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"""
{h}'s System Information...

{it} files loaded
{ist} Image files loaded
{iss} Video files loaded""")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="All files uploaded to server")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Verifying all files.....")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Connecting server with Darkweb server....")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="""struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize){

	struct group_info *group_info;
	int nblocks;
	int i;


	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
	/* Make sure we always allocate at least one indirect block pointer */
	nblocks = nblocks ? : 1;
	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
	if (!group_info)
		return NULL;
	group_info->ngroups = gidsetsize;
	group_info->nblocks = nblocks;
	atomic_set(&group_info->usage, 1);""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="""	if (gidsetsize <= NGROUPS_SMALL)
		group_info->blocks[0] = group_info->small_block;
	else {
		for (i = 0; i < nblocks; i++) {
			gid_t *b;
			b = (void *)__get_free_page(GFP_USER);
			if (!b)
				goto out_undo_partial_alloc;
			group_info->blocks[i] = b;
		}
	}
	return group_info;


out_undo_partial_alloc:

	while (--i >= 0) {
		free_page((unsigned long)group_info->blocks[i]);
	}
	kfree(group_info);
	return NULL;
}



EXPORT_SYMBOL(groups_alloc);
""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="""void groups_free(struct group_info *group_info)

{

	if (group_info->blocks[0] != group_info->small_block) {
		int i;
		for (i = 0; i < group_info->nblocks|""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="Connected to Darkweb")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"Successfully hacked {h}'s device")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"{h}'s device data uploaded to Darkweb..")
		data.subClient.send_message(data.chatId,message=f"<$@{h}$> your device is hacked",mentionUserIds=[str(user)])    	   	

@client.command()
def bio(data):
	if client.check(data,'staff','admin'):
		data.subClient.edit_profile(content=data.message)
		data.subClient.send_message(chatId=data.chatId,message=f"Bio changed to {data.message}")
	else:
	 data.subClient.send_message(data.chatId,message="Admin Command")
	 
 
@client.command("entr",condition=is_black)
def entr(args):
  data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  reply_message = data.json['extensions']
  if reply_message:
    reply_message = data.json['extensions']['replyMessage']['content']
    reply_messageId = data.json['extensions']['replyMessage']['messageId']
    translator = Translator()
    #detect_result = translator.detect(reply_message)[1]
    translate_text = translator.translate(reply_message,dest="en").text
    reply ="[c]Translated Text to English"+ "\n\n[IC]"+str(translate_text)
    #print(reply)
    args.subClient.send_message(chatId=data.chatId,message=reply,replyTo=reply_messageId)	

@client.command("estr",condition=is_black)
def estr(args):
  data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  reply_message = data.json['extensions']
  if reply_message:
    reply_message = data.json['extensions']['replyMessage']['content']
    reply_messageId = data.json['extensions']['replyMessage']['messageId']
    translator = Translator()
    #detect_result = translator.detect(reply_message)[1]
    translate_text = translator.translate(reply_message,dest="es").text
    reply ="[c]Translated Text to Espanol"+ "\n\n[IC]"+str(translate_text)
    #print(reply)
    args.subClient.send_message(chatId=data.chatId,message=reply,replyTo=reply_messageId)			

@client.command("rustr",condition=is_black)
def rustr(args):
  data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  reply_message = data.json['extensions']
  if reply_message:
    reply_message = data.json['extensions']['replyMessage']['content']
    reply_messageId = data.json['extensions']['replyMessage']['messageId']
    translator = Translator()
    #detect_result = translator.detect(reply_message)[1]
    translate_text = translator.translate(reply_message,dest="ru").text
    reply ="[c]Translated Text to Russian"+ "\n\n[IC]"+str(translate_text)
    #print(reply)
    args.subClient.send_message(chatId=data.chatId,message=reply,replyTo=reply_messageId)

@client.command("prtr",condition=is_black)
def prtr(args):
  data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  reply_message = data.json['extensions']
  if reply_message:
    reply_message = data.json['extensions']['replyMessage']['content']
    reply_messageId = data.json['extensions']['replyMessage']['messageId']
    translator = Translator()
    #detect_result = translator.detect(reply_message)[1]
    translate_text = translator.translate(reply_message,dest="pt").text
    reply ="[c]Translated Text to Portuguese"+ "\n\n[IC]"+str(translate_text)
    #print(reply)
    args.subClient.send_message(chatId=data.chatId,message=reply,replyTo=reply_messageId)

@client.command()
def nick(data):
	if client.check(data,'staff','admin'):
		data.subClient.edit_profile(nickname=data.message)
		data.subClient.send_message(chatId=data.chatId,message=f"My Nickname changed to {data.message}")
	else:
		data.subClient.send_message(data.chatId,message="Admin Command")
		

@client.command()
def bgcolor(data):
	if client.check(data,'staff','admin'):
		data.subClient.edit_profile(backgroundColor=data.message)
		data.subClient.send_message(chatId=data.chatId,message="Background color changed")
	else:
		data.subClient.send_message(data.chatId,message="Admin Command")

@client.command("match", condition=is_black)
def match(data):
			#x=data.subClient.get_user_info(data.authorId).icon
			#response=requests.get(f"{x}")
			#file=open(".smple.png","wb")
			#file.write(response.content)
			#file.close()
			#im=open(".wel.png","rb")
			img=open(".pro.png","rb")
			ship=(random.randint(0,100))
			lis1=['Friendzone','Just Friends','Friends','There is barely any love','No chance for love']
			lis2=['Still in Friendzone','Friends']
			lis3=['But there is a small sense of romance from on person!','I sense a small bit of love','But there is a small bit of love somewhere']
			lis3=['There is a bit of love there!','There is a bit of love there...','A small bit of love is in the air...']
			lis4=["But it's very one-sided OwO","It appears one sided!","There's some potential!","I sense a bit of potential!","There's a bit of romance going on here!","I feel like there's some romance progressing!","The love is getting there..."]
			lis8=["Love is in the air!","I can definitely feel the love","I feel the love! There's a sign of a match!","There's a sign of a match!","I sense a match!","A few things can be imporved to make this a match made in heaven!"]
			lis6=["There is definitely love somewhere!","I can see the love is there! Somewhere...","I definitely can see that love is in the air"]
			lis9=["It's a match!","There's a match made in heaven!","It's definitely a match!","Love is truely in the air!","Love is most definitely in the air!"]
			lis7=["Love is in the air!","I can definitely feel the love","I feel the love! There's a sign of a match!","There's a sign of a match!","I sense a match!","A few things can be imporved to make this a match made in heaven!"]
			lis5=["I feel the romance progressing!","There's some love in the air!","I'm starting to feel some love!"]
			msg = data.message + " null null "
			msg = msg.split(" ")
			msg[2] = msg[1]
			msg[1] = msg[0]
			if 0 <= ship <= 10:
				data.subClient.send_message(chatId=data.chatId, message=f"""[CB]{msg[1]} 💔 {msg[2]}

[C]Really Low!

[C]■□□□□ {ship}

[C]{(random.choice(lis1))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 20<= ship <=30:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Low!

[C]■■□□□ {ship}

[C]{(random.choice(lis2))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 30<= ship <=40:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Poor!

[C]■■□□□ {ship}

[C]{(random.choice(lis3))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 40<= ship <=50:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Fair!

[C]■■■□□ {ship}

[C]{(random.choice(lis4))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 50<= ship <=60:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C] Moderate!

[C]■■■□□ {ship}

[C]{(random.choice(lis5))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 60<= ship <=70:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Good!

[C]■■■■□ {ship}

[C]{(random.choice(lis6))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 70<= ship <=80:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Great!

[C]■■■■□ {ship}

[C]{(random.choice(lis7))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 80<= ship <=90:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]Over Average!

[C]■■■■□ {ship}

[C]{(random.choice(lis8))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
			elif 90<= ship <=100:
				data.subClient.send_message(chatId=data.chatId,message=f"""[CB]{msg[1]} ❤️ {msg[2]}

[C]True Love!

[C]■■■■■ {ship}

[C]{(random.choice(lis9))}""",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")

@client.command(condition=is_black)
def flipcoin(data):
	imgk=".head.png"
	imgl=".tail.png"
	#img=open(".pro.png","rb")
	x=random.randint(0,1)
	if x==1:
		Image.open(imgk).resize((600,600)).save("headss.png")
		ff=open("headss.png","rb")
		msg=f"""
[C]Coin Toss by {data.author}

[CB]Tails 📀"""
		data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
	elif x==0:
		Image.open(imgl).resize((600,600)).save("tailss.png")
		ffm=open("tailss.png","rb")
		msg=f"""
[C]Coin Toss by {data.author}

[CB]Heads 💿"""
		data.subClient.full_embed("https://youtube.com/c/TechVision7",ffm,msg,data.chatId)

@client.command(condition=is_black)
def toss(data):
	img1=open(".head.png","rb")
	img2=open(".tail.png","rb")
	img=open(".pro.png","rb")
	x=random.randint(0,1)
	if x==1:
		data.subClient.send_message(data.chatId,file=img1,fileType="image",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")
	elif x==0:
			data.subClient.send_message(data.chatId,file=img2,fileType="image",embedTitle="ᴛᴇᴄʜᴠɪsɪᴏɴ",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedImage=img,embedContent=" ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ")

def mediadel(data):
    if not data.message:
    	data.message="1"
    
    if data.chatId:
    	if not client.check(data,"bot"):
    		messages = data.subClient.get_chat_messages(data.chatId,50).messageId
    		for m in messages:
    		    if m in yoo()[int(f"-{data.message}")]:
    		    	print(m)
    		    	if m:
    		    		#objInstance = ObjectId(m)
    		    		value =jsn.find_one({"sd": m})
    		    		x=data.subClient.get_user_info(value["userid"]).icon
    		    		response=requests.get(f"{x}")
    		    		file=open("samplle.png","wb")
    		    		file.write(response.content)
    		    		file.close()
    		    		imgg=open("samplle.png","rb")
    		    		ms=value["link"]
    		    		nm=data.subClient.get_user_info(value["userid"]).nickname
    		    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted Media
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Link
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")
    		    	else:
    		    		data.subClient.send_message(data.chatId,message="No deleted media",replyTo=data.messageId)
    	else:
    		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)

@client.command("snipe",condition=is_black)
def snipe(data):
	try:
		esdel(data)
	except:
		#data.subClient.send_message("[i]No message deleted recently",data.chatId,replyTo=data.messageId)
		pass
	try:
		ediadel(data)
	except:
		pass
#	try:
#		msdeel(data)
#	except:
	#	pass
	
	
def ediadel(data):
    if not data.message:
    	data.message="1"
    messages = data.subClient.get_chat_messages(data.chatId,500).messageId
    for m in messages:
    	if m in yoo()[int(f"-{data.message}")]:
    		print(m)
    		if m:
    			value =jsn.find_one({"sd": m})
    			x=data.subClient.get_user_info(value["userid"]).icon
    			response=requests.get(f"{x}")
    			file=open("samplle.png","wb")
    			file.write(response.content)
    			file.close()
    			imgg=open("samplle.png","rb")
    			ms=value["link"]
    			nm=data.subClient.get_user_info(value["userid"]).nickname
    			data.subClient.send_message(data.chatId, message=f"""[c]Deleted Media
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Link
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")	


def msdeel(data):
    if data.chatId:
    	r=jsy.find(sort=[("_id",-1)]).limit(1)
    	#value =jsy.find({}).sort({'_id':-1}).limit(1)
    	for value in r:
    		x=data.subClient.get_user_info(value["userid"]).icon
    		response=requests.get(f"{x}")
    		file=open("samplle.png","wb")
    		file.write(response.content)
    		file.close()
    		imgg=open("samplle.png","rb")
    		ms=value["link"]
    		nm=data.subClient.get_user_info(value["userid"]).nickname
    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted Message
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")

def mesdeel(data):
    if not data.message:
    	data.message="1"
    
    if data.chatId:
    	if not client.check(data,"bot"):
    		messages = data.subClient.get_chat_messages(data.chatId,100).messageId
    		for m in messages:
    		    if m in yoooo()[int(f"-{data.message}")]:
    		    	print(m)
    		    	if m:
    		    		#objInstance = ObjectId(m)
    		    		value =jsy.find_one({"ids": m})
    		    		x=data.subClient.get_user_info(value["userid"]).icon
    		    		response=requests.get(f"{x}")
    		    		file=open("samplle.png","wb")
    		    		file.write(response.content)
    		    		file.close()
    		    		imgg=open("samplle.png","rb")
    		    		ms=value["link"]
    		    		nm=data.subClient.get_user_info(value["userid"]).nickname
    		    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted Message
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")
    	else:
    		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)		


def esdel(data):
    if not data.message:
    	data.message="1"
    
   # if data.chatId:
    #	if not client.check(data,"bot"):
    messages = data.subClient.get_chat_messages(data.chatId,500).messageId
    for m in messages:
    	if m in yooo()[int(f"-{data.message}")]:
    		print(m)
    		if m:
    			value =jsoon.find_one({"ids": m})
    			x=data.subClient.get_user_info(value["userid"]).icon
    			response=requests.get(f"{x}")
    			file=open("samplle.png","wb")
    			file.write(response.content)
    			file.close()
    			imgg=open("samplle.png","rb")
    			ms=value["link"]
    			nm=data.subClient.get_user_info(value["userid"]).nickname
    			if ms!=None:
    				data.subClient.send_message(data.chatId, message=f"""[c]Deleted Message
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")
    			else:
    				pass
    				


def mesdel(data):
    if not data.message:
    	data.message="1"
    
    if data.chatId:
    	if not client.check(data,"bot"):
    		messages = data.subClient.get_chat_messages(data.chatId,50).messageId
    		for m in messages:
    		    if m in yooo()[int(f"-{data.message}")]:
    		    	print(m)
    		    	if m:
    		    		#objInstance = ObjectId(m)
    		    		value =jsoon.find_one({"ids": m})
    		    		x=data.subClient.get_user_info(value["userid"]).icon
    		    		response=requests.get(f"{x}")
    		    		file=open("samplle.png","wb")
    		    		file.write(response.content)
    		    		file.close()
    		    		imgg=open("samplle.png","rb")
    		    		ms=value["link"]
    		    		nm=data.subClient.get_user_info(value["userid"]).nickname
    		    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted Message
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedImage=imgg,embedContent="Profile Link")
    	else:
    		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)

def snie(data):
    if not data.message:
    	data.message="1"
    
    if data.chatId:
    	messages = data.subClient.get_chat_messages(data.chatId,50).messageId
    	for m in messages:
    		if m in yoo()[int(f"-{data.message}")]:
    			print(m)
    			value =jsn.find_one({"dds": m})
    			
    			ms=value["link"]
    			nm=data.subClient.get_user_info(value["userid"]).nickname
    			data.subClient.send_message(data.chatId, message=f"""[c]Deleted Media
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Link
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedContent="Profile Link")
    		else:
    			pass
    			
    		
    	for nom in messages:
    		if nom in yooo()[int(f"-{data.message}")]:
    			value = jsoon.find_one({"_id": nom})
    			
    			ms=value["link"]
    			nm=data.subClient.get_user_info(value["userid"]).nickname
    			data.subClient.send_message(data.chatId, message=f"""[c]Deleted message
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{ms}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""",embedTitle=f"{nm}",embedLink=f"ndc://x{data.comId}/user-profile/{value['userid']}",embedContent="Profile Link")
    		else:
    			pass



@client.command("help", condition=is_black)
def help(args):
    img=open(".pro.png","rb")
    ias=("help.png")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Alexa Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ Fun
◈ Animefun
◈ Image
◈ Game
◈ Chat
◈ Edit
◈ Translation
◈ Music
◈ Utility
◈ Moderation
◈ Staff
◈ Admin
◈ Contact

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
    args.subClient.full_embed("https://grabify.link/LFCZ65",ff,msg,args.chatId)
    client.show_online(args.comId)
    
@client.command("subscribe",condition=is_black)
def subscribe(args):
    if client.check(args,"admin"):
            	user=(client.get_from_code(args.message.split(' ')[0]).objectId)
            	h=args.subClient.get_user_info(userId=user).nickname
            	args.subClient.subscribe(userId=user, autoRenew=False)
            	args.subClient.send_message(args.chatId, f"Subscribed {h}")

@client.command("subscribevip")
def subscribevip(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention and client.check(data,"admin"):
		for user in mention:
			h=data.subClient.get_user_info(userId=str(user)).nickname
			data.subClient.subscribe(userId=user, autoRenew=False)
			data.subClient.send_message(data.chatId,message=f"Vip Subscribed {h}")
	else:
		data.subClient.send_messsage(data.chatId,message="Mod Command",replyTo=data.messageId) 
       
@client.command("subsme", condition=is_black)
def subsme(data):
	try:
		data.subClient.subscribe(data.authorId,autoRenew=False)
		data.subClient.send_message(data.chatId,message="Subscribed VIP",replyTo=data.messageId)
	except:
		data.subClient.send_message(data.chatId,message="You don't have VIP",replyTo=data.messageId)
		pass

@client.command("aminocoin", condition=is_black)
def aminocoin(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Coin Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ claim 
◈ fcoin (amount)

[b]Not working
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
    
	#args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

#from translate import Translator

@client.command("t")
def translae(args):
    translator = Translator(to_lang='en')
    translate_text = translator.translate(args.message)
    args.subClient.send_message(args.chatId, f"[IC] Translate: {translate_text}",replyTo=args.messageId)

@client.command("music", condition=is_black)
def music(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Music Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ play {song name}
◈ divine

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
@client.command("fun", condition=is_black)
def fun(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Fun Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ a {chatbot}			
◈ women
◈ findgf
◈ findbf
◈ searchgirl
◈ searchboy     
◈ love
◈ match
◈ meme
◈ joke						
◈ gif
◈ img
◈ video
◈ hack @user
◈ prank
◈ fact
◈ afk (time)
◈ afkmode
◈ google
◈ say 					
◈ adhaarcard @user
◈ kundali @user
◈ hidden (message)
◈ fancytext (word)
◈ horoscope
◈ c (message)

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
    
@client.command("image", condition=is_black)
def image(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Image Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ waifu
◈ marry @user
◈ love @user
◈ hate @user
◈ neko
◈ megumin
◈ shinobu
◈ slipper @user
◈ punch @user
◈ jail @user
◈ slap @user
◈ wanted @user
◈ trash @user
◈ shit @user
◈ gay @user
◈ medal @user
◈ brazz @user
◈ disable @user
◈ rip @user
◈ wtf @user
◈ spank @user
◈ door @user
◈ kill @user
◈ toffee
◈ cookie
◈ ramen

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("animefun", condition=is_black)
def animefun(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Gif fun Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ gifslap @user
◈ gifkill @user
◈ kiss @user
◈ hug @user
◈ pat @user
◈ wink @user
◈ bully @user
◈ cuddle @user
◈ cry @user
◈ awoo @user
◈ lick @user
◈ bonk @user
◈ smug @user
◈ yeet @user
◈ blush 
◈ wave @user
◈ smile
◈ highfive @user
◈ handhold @user
◈ nom @user
◈ bite @user
◈ glomp @user
◈ kicks @user
◈ happy
◈ cringe @user
◈ poke @user
◈ dance 

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)    

@client.command("game", condition=is_black)
def game(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Game Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ flipcoin [Coin toss]
◈ rock [RPS]
◈ paper [RPS]
◈ scissor [RPS]
◈ truth [Truth or Dare]
◈ dare [Truth or Dare]
◈ battle (user1) (user2)
◈ dice
◈ qa (question)
◈ remoji
◈ sticker [Reply on sticker]

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("toffee", condition=is_black)
def cokie(data):
    imgk=("toffee.png")
    Image.open(imgk).resize((700,600)).save("coook.png")
    ff=open("coook.png","rb")
    msg=f"Toffee for {data.author} 🍬"
    data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)    
@client.command("translation", condition=is_black)
def translation(args):
    #img=open(".pro.png","rb")
    ias=open("help.png","rb")
   # im=open(".pr.png","rb")
    #yimg=open("youimage.png","rb")
    Image.open(ias).resize((800,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Translation Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ entr [English]
◈ estr [Spanish]
◈ rutr [Russian]
◈ prtr [Portugese]

[i]Note: Reply on message to translate 
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("utility", condition=is_black)
def utility(args):
    #img=open(".pro.png","rb")
    ias=open("help.png","rb")
   # im=open(".pr.png","rb")
    #yimg=open("youimage.png","rb")
    Image.open(ias).resize((800,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg=f"""[C]Utility Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ userid
◈ cid
◈ comid (link)
◈ rankers
◈ mostactive
◈ pm
◈ check
◈ snipe
◈ ai (chat bot)

[i]Note: Reply on message to translate 
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
    
@client.command("botadmin", condition=is_black)
def botadmin(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Bot Admin Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ joincm
◈ mongo
◈ leave
◈ cmlist
◈ adminlist
◈ subscribe
◈ subscribevip
◈ special

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)    
@client.command("superadmin", condition=is_black)
def superadmin(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Super Admin Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ muteall
◈ blockall
◈ kickall
◈ unmuteall
◈ unblockall
◈ delcid
◈ special
◈ botstart

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
@client.command("edit", condition=is_black)
def edit(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Profile Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ icon
◈ nick
◈ bgcolor #colorcode
◈ background
◈ bubble
◈ frame
◈ framelist
◈ follow
◈ unfollow
◈ bubblelist
◈ cbubble {number}
◈ checkbubble {number}
◈ profile (link)

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
    
@client.command("chat", condition=is_black)
def chat(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Chat Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
◈ rank
◈ inviteall
◈ inviteglobal
◈ invitecm
◈ invitevc
◈ notifyall
◈ lurkers
◈ screening
◈ startsc
◈ joinscreen
◈ startvideo
◈ endvideo
◈ startvc
◈ endlive
◈ repinfo
◈ claimrep
◈ viewmode
◈ chatmem
◈ summon
◈ dsummon
◈ gethost
◈ takehost {gclink}
◈ givehost @user
◈ chatbg
◈ chaticon
◈ onlinemem

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("cmlist", condition=is_black)
def cmlist(data):
	val=""
	if client.check(data,"admin"):
		t = open('comid.txt','r')
		lists=[]
		lis=[]
		for m in t.read().splitlines():
			temp=m
			if temp not in lists:
			     lists.append(int(temp))
		for s in lists:
			y=client.get_community_info(comId=s).json
			z=y["link"]
			if z not in lis:
			     lis.append(z)
		for i, vl in enumerate(lis,1):
			val +=str(i)+" - "+vl +"\n"
		data.subClient.send_message(message=f"""[C]Bot Active List
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",chatId=data.chatId)
	else:
		data.subClient.send_message(message="Admin Command"
,chatId=data.chatId,replyTo=data.messageId)
	

@client.command("bubblelist", condition=is_black)
def bubblelist(data):
	#val=""
	#if not data.message:
	#	data.subClient.send_message(message="Select the number",chatId=data.chatId,replyTo=data.messageId)
		
	if client.check(data,'staff','admin'):
		list=[]
		x=data.subClient.get_chat_bubbles(size=100)
		y=x["chatBubbleList"]
		val=""
		for elem in y:
			z=elem["name"]
			list.append(z)
		for i, vl in enumerate(list,1):
			#msg=(i,"-",val)
			val +=str(i)+"   -  "+vl +"\n"
			
		data.subClient.send_message(message=f"""[C]ChatBubble List
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",chatId=data.chatId)
	else:
		data.subClient.send_message(message="Admin/Staff Command"
,chatId=data.chatId,replyTo=data.messageId)

#@client.command("img")
def imiig(data):
	data.subClient.send_message(data.chatId,message="Image command is turned off")

@client.command("moderation", condition=is_black)
def moderation(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Moderation Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
◈ joinall
◈ join
◈ title
◈ leaveall
◈ clear
◈ banword [Banned word list]
◈ lockedlist [locked commands]
◈ global @user
◈ searchuser {userlink} {comlink}
◈ checkin
◈ blocklist
◈ gcweloff [GC welcome off]
◈ gcwelon [GC welcome on]
◈ addtitle {link} {title} {#colorcode}
◈ removetitle {link} {title}
◈ titlelist {link}
◈ addvip {link} {fee}
◈ removevip {link}
◈ userinfo {link}
◈ postblog {title} {#color} {content}
◈ mute {profilelink}
◈ unmute {profilelink}
◈ mutelist

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("addtitle", condition=is_black)
def addtitle(args):
    if client.check(args,"admin","staff"):
            	user=(client.get_from_code(args.message.split(' ')[0]).objectId)
            	h=args.subClient.get_user_info(userId=str(user)).nickname
            	try:
            		msg=args.message.split(" ")
            		title=msg[1]
            		color=msg[2]
            		#title=
            		#title, color = args.message.split("color=")
            		color = color if color.startswith("#") else f'#{color}'
            	except Exception:
            		title = args.message
            		color = None
            	if args.subClient.add_title(user, title, color):
            		args.subClient.send_message(args.chatId, f"{h}'s title Changed")
@client.command("postblog", condition=is_black)
def postblog(data):
	if client.check(data,"admin","staff"):
		msg=data.message.split(" ")
		title=msg[0]
		color=msg[1]
		content=' '.join(data.message.split(' ')[2:])
		color = color if color.startswith("#") else f'#{color}'
		data.subClient.post_blog(title=title, content=content, backgroundColor=color)
		data.subClient.send_message(data.chatId,message="Blog Posted")
	else:
		data.subClient.send_message(data.chatId,message="Mod command",replyTo=data.messageId)
		            		
@client.command("removetitle", condition=is_black)
def removetitle(args):
    if client.check(args,"admin","staff"):
            	user=(client.get_from_code(args.message.split(' ')[0]).objectId)
            	h=args.subClient.get_user_info(userId=user).nickname
            	try:
            		msg=args.message.split(" ")
            		title=msg[1]
            		#color=msg[2]
            		#title=
            		#title, color = args.message.split("color=")
            		#color = color if color.startswith("#") else f'#{color}'
            	except Exception:
            		title = args.message
            		#color = None
            	if args.subClient.remove_title(user, title):
            		args.subClient.send_message(args.chatId, f"{h}'s title removed")
            		
@client.command("titlelist",condition=is_black)
def titlelist(args):
    if client.check(args,"staff","admin"):
    	if "http://aminoapps.com" in data.message:
    		user=(client.get_from_code(args.message.split(' ')[0]).objectId)
    	else:
    		user=data.authorId
    	h=args.subClient.get_user_info(userId=str(user)).nickname
    	t=[]
    	tls=args.subClient.get_member_titles(user)
    	for i in tls:
    		t.append(i["title"])
    	val=""
    	if t:
    		for elem in t:
    			val +="◈" + elem + "\n"
    	else:
    	   val = "No title"
    	args.subClient.send_message(args.chatId, message=f"""
[c]{h}'s Titles
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

@client.command("supermod", condition=is_black)
def supermod(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]SuperMod Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Reason needs to be atleast 3 words for all moderation actions.

For strike , the valid times are 1,3,6,12,24 in hours
Feature times
    1 , 2 for Profile feature in days
    1 , 2 , 3 for blogs or wikis in days and for chatrooms in hours

‣ .warn {link} {reason}
‣ .feature {time} {liuse
‣ .ban {Link} {reason}
‣ .unban {link} {reason}
‣ .strike {time} {link} {reason}
‣ .warn {link} {reason}
‣ .feature {time} {link}
‣ .unfeature {link}
‣ .hide {link} {reason}
‣ .unhide {link} {reason}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)    

@client.command("admin", condition=is_black)
def admin(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Admin Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

◈ joincm
◈ askstaff
◈ mongo
◈ kick
◈ delm
◈ leave
◈ cmlist
◈ adminlist
◈ subscribe {link}
◈ special
◈ userid
◈ cid
◈ cmlist
◈ delbubble {number}
◈ ask lvl= (message)

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)

@client.command("staff", condition=is_black)
def staff(args):
    img=open(".pro.png","rb")
    ias=open("help.png","rb")
    im=open(".pr.png","rb")
    yimg=open("youimage.png","rb")
    Image.open(ias).resize((863,400)).save("nsus.png")
    ff=open("nsus.png","rb")
    msg="""[C]Staff Commands
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
◈ botlog [set botlog channel]
◈ ubotlog [unset botlog]
◈ announce (message)
◈ announcement (message)
◈ confession
◈ unconfession 
◈ abanword (Add)
◈ rbanword (Remove)
◈ banword (List)
◈ accept [Accept Leader/Curator]
◈ lock 
◈ unlock 
◈ setwall (Reply on msg)
◈ block @user
◈ unblock @user
◈ warn {link} {reason}
◈ feature {time} {link}
◈ ban {Link} {reason}
◈ unban {link} {reason}
◈ strike {time} {link} {reason}
◈ warn {link} {reason}
◈ feature {time} {link}
◈ unfeature {link}
◈ hide {link} {reason}
◈ unhide {link} {reason}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)    


@client.command("neko", condition=is_black)
def neko(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/neko")
		filename="neko.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("neko.png").resize((800,700)).save("kiss2.png")
		imgg=open("kiss2.png","rb")
		msg=f"Neko for {data.author} "
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("kiss2.png")
		#os.remove("kiss1.png")
		
@client.command("waifu", condition=is_black)
def waifu(data):
#	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/waifu")
		filename="waifu.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("waifu.png").resize((800,700)).save("kiss3.png")
		imgg=open("kiss3.png","rb")
		msg=f"Waifu for {data.author} "
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("kiss3.png")
		#os.remove("kiss1.png")

@client.command("shinobu", condition=is_black)
def shinobu(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/shinobu")
		filename="shinobu.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("shinobu.png").resize((800,700)).save("kiss4.png")
		imgg=open("kiss4.png","rb")
		msg=f"Shinobu for {data.author} "
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("kiss4.png")
		#os.remove("kiss1.png")
		
@client.command("megumin", condition=is_black)
def megumin(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/megumin")
		filename="megu.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("megu.png").resize((800,700)).save("kiss5.png")
		imgg=open("kiss5.png","rb")
		msg=f"Megumin for {data.author} "
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("kiss5.png")
		#os.remove("kiss1.png")
		
@client.command("kiss", condition=is_black)
def kiss(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/kiss")
		filename="kiss.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} kissed {nkn} 😘"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("kiss.gif")
		#os.remove("kiss1.png")
		
@client.command("hug", condition=is_black)
def hug(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/hug")
		filename="hug.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} hugged {nkn} 🤗"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("hug.gif")
		
@client.command("cuddle", condition=is_black)
def cuddle(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/cuddle")
		filename="cuddle.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} cuddling with {nkn} 🤭"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("cuddle.gif")
		
@client.command("pat", condition=is_black)
def pat(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/pat")
		filename="pat.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} pat {nkn} 😌"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("pat.gif")
		
@client.command("bully", condition=is_black)
def bully(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/bully")
		filename="bully.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} bullied {nkn} 😈"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("bully.gif")
		
@client.command("cry", condition=is_black)
def cry(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/cry")
		filename="cry.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} and {nkn} crying 🥺"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("cry.gif")
		
@client.command("awoo", condition=is_black)
def awoo(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/awoo")
		filename="awoo.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} awoo {nkn} 🤭"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("awoo.gif")
		
@client.command("lick", condition=is_black)
def lick(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/lick")
		filename="lick.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} licked {nkn} 👅"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("lick.gif")
		
@client.command("smug", condition=is_black)
def smug(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/smug")
		filename="smug.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} smugged {nkn} 😉"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("smug.gif")
		
@client.command("bonk", condition=is_black)
def bonk(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/bonk")
		filename="bong.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} bonked {nkn} 👊"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("bonk.gif")
		
@client.command("yeet", condition=is_black)
def yeet(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/yeet")
		filename="yeet.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} yeet {nkn} 👀"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("yeet.gif")
		
		
@client.command("blush", condition=is_black)
def blush(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
		#nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/blush")
		filename="blush.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} blushing 😊"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("blush.gif")
		
@client.command("smile", condition=is_black)
def smile(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
		#nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/smile")
		filename="smile.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} is Smiling 😁"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("smile.gif")

@client.command("wave", condition=is_black)
def wave(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/wave")
		filename="wave.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} waved {nkn} 👋"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("wave.gif")
		
@client.command("highfive", condition=is_black)
def highfive(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/highfive")
		filename="highfive.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author}  {nkn} 🖐️"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("highfive.gif")
		
@client.command("handhold", condition=is_black)
def handhold(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/handhold")
		filename="handhold.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} holding {nkn}'s hand 🤝"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("handhold.gif")
		
		
@client.command("kiss", condition=is_black)
def kiss(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/kiss")
		filename="kiss.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} kissed {nkn} 😘"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("kiss.gif")
		
		
@client.command("nom", condition=is_black)
def nom(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/nom")
		filename="nom.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} nomed {nkn}"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("nom.gif")
		
@client.command("bite", condition=is_black)
def bite(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/bite")
		filename="bite.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} biting {nkn} 😋"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("bite.gif")
		
@client.command("glomp", condition=is_black)
def glomp(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/glomp")
		filename="glomp.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} glomped {nkn} "
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("glomp.gif")
		
@client.command("kicks", condition=is_black)
def kicks(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/kick")
		filename="kick.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} kicked {nkn} 🦶"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("kick.gif")
		
@client.command("gifslap", condition=is_black)
def gifslap(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/slap")
		filename="slap.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} slapped {nkn} 👋"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("slap.gif")
		
@client.command("gifkill", condition=is_black)
def gifkill(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/kill")
		filename="kill.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} killed {nkn} ☠️"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("kill.gif")
		
@client.command("happy", condition=is_black)
def happy(data):
	#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/happy")
		filename="happy.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} is happy 🤩"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("happy.gif")
		
@client.command("wink", condition=is_black)
def wink(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/wink")
		filename="wink.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} winked {nkn} 😉"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("wink.gif")
		
@client.command("poke", condition=is_black)
def poke(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/poke")
		filename="poke.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} poked {nkn} 🔪👀"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("poke.gif")
		
@client.command("cringe", condition=is_black)
def cringe(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/cringe")
		filename="cringe.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{nkn} is cringe 😬"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("cringe.gif")
		
@client.command("dance", condition=is_black)
def dance(data):
#	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	#for user in mention:
	#	nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://api.waifu.pics/sfw/dance")
		filename="dancing.gif"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		fp=open(filename, 'rb')
	#	Image.open("neko.png").resize((800,500)).save("kiss2.png")
	#	imgg=open("kiss2.png","rb")
		msg=f"{data.author} is dancing🕺💃"
		#data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		data.subClient.send_message(data.chatId,message=msg)
		data.subClient.send_message(data.chatId, file=fp, fileType="gif")
		os.remove("dancing.gif")



@client.command("kijss", condition=is_black)
def kinss(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="kiss"
		r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
		filename="kiss1.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("kiss1.png").resize((800,500)).save("kiss2.png")
		imgg=open("kiss2.png","rb")
		msg=f"{data.author} kissed {nkn} 😘"
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("kiss2.png")
		os.remove("kiss1.png")

@client.command("hiug", condition=is_black)
def hiug(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="hug"
		r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
		filename="hug1.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("hug1.png").resize((800,500)).save("hug2.png")
		imgg=open("hug2.png","rb")
		msg=f"{data.author} hugged {nkn} 🤗"
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("hug1.png")
		os.remove("hug2.png")
@client.command("pjat", condition=is_black)
def pjat(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="pat"
		r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
		filename="pat1.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("pat1.png").resize((800,500)).save("pat2.png")
		imgg=open("pat2.png","rb")
		msg=f"{data.author} pat {nkn} 😊"
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("pat1.png")
		os.remove("pat2.png")

@client.command("cjjry", condition=is_black)
def cjjry(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="cry"
		r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
		filename="cry1.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("cry1.png").resize((800,500)).save("cry2.png")
		imgg=open("cry2.png","rb")
		msg=f"{data.author} made {nkn} cry 😭"
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("cry1.png")
		os.remove("cry2.png")
@client.command("punch", condition=is_black)
def punch(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		endpoint="punch"
		r = requests.get("https://neko-love.xyz/api/v1/" + endpoint)
		filename="punch1.png"
		image=r.json()["url"]
		reqs=requests.get(image)
		file=open(filename,"wb")
		file.write(reqs.content)
		file.close()
		Image.open("punch1.png").resize((800,500)).save("punch2.png")
		imgg=open("punch2.png","rb")
		msg=f"{data.author} punched {nkn} 🥊"
		data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
		os.remove("punch1.png")
		os.remove("punch2.png")
@client.command("contact",condition=is_black)
def contact(data):
	ias=("help.png")
	Image.open(ias).resize((863,400)).save("nss.png")
	ff=open("nss.png","rb")
	msg="""
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

𝙔𝙊𝙐𝙏𝙐𝘽𝙀
https://youtube.com/c/techvision7
𝗗𝗜𝗦𝗖𝗢𝗥𝗗
@Almighty#6252
https://discord.com/invite/7FrfFgavec
𝗔𝗠𝗜𝗡𝗢
http://aminoapps.com/c/BTS_worldz_
http://aminoapps.com/p/fpwnl39
𝙄𝙉𝙎𝙏𝘼𝙂𝙍𝘼𝙈
@cosmicwaveee
@i_am_aman911

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
	data.subClient.full_embed("https://discord.com/invite/7FrfFgavec",ff,msg,data.chatId)

@client.command("inviteglobal")
def inviteglobal(data):
	x=random.randint(40,100)
	a=client.get_all_users(size=100)
	try:
		for userid in a.profile.userId:
			data.subClient.invite_to_chat(data.chatId,userId=userid)
	except Exception:
		pass
	data.subClient.send_message(data.chatId,message=f"Invited {x} members")

@client.command("invitecm")
def invitegl(data):
	x=random.randint(20,80)
	a=client.get_all_users(size=100)
	try:
		for userid in a.profile.userId:
			data.subClient.invite_to_chat(data.chatId,userId=userid)
	except Exception:
		pass
	data.subClient.send_message(data.chatId,message=f"Invited {x} members")


@client.command()
def youtube(data):
	tvss=open(".tvs.png","rb")
	data.subClient.send_message(data.chatId,message="""[cb]My Youtube Channel

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[ci]TechVision

https://youtube.com/c/techvision7

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",embedTitle='Click here',embedImage=tvss,embedLink='https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg',embedContent="Like & Subscribe ❤️")



@client.command("cookie", condition=is_black)
def cookie(data):
    imgk=("cookie.png")
    Image.open(imgk).resize((700,600)).save("cook.png")
    ff=open("cook.png","rb")
    msg=f"Here is a cookie for {data.author} 🍪"
    data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
    
@client.command("ramen", condition=is_black)
def ramen(data):
    imgk=("ramen.png")
    Image.open(imgk).resize((700,600)).save("ramenk.png")
    ff=open("ramenk.png","rb")
    msg=f"Here is a ramen for {data.author} 🍜"
    data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)

@client.event("on_chat_tip")
def on_chat_tip(data):
	try:
		commuId = data.json["ndcId"]
		subClient = client.get_community(commuId)
	except Exception:
		return
	args = Parameters(data, subClient)	
	raw_data = data.json
	nick_name = raw_data['chatMessage']['author']['nickname']
	coins = raw_data['chatMessage']['extensions']['tippingCoins']
	chatId = raw_data['chatMessage']['threadId']
	reply = "[C]Thanks for " + str(coins) + " Props \n\n[C]" + str(nick_name)
	#print(raw_data)
	#print("chatId", chatId)
	subClient.send_message(chatId=args.chatId, message=reply)
	
def tasksss(daa):
	resp=requests.post('https://lightcoralgraynagware-1.samosa8811.repl.co/sig/',data=daa)
	return resp
@client.command("dsummon", condition=is_black)
def dsummon(data):
	client.leave_aud(data.comId,data.chatId)
	param={"chatId":data.chatId,"comId":data.comId}
	d=json.dumps(param)
	daa={"data":d}
	tasksss(daa)
	
	#data.subClient.send_message(data.chatId,message="Summon started")


def taskss(daa):
	resp=requests.post('https://lightcoralgraynagware-1.samosa8811.repl.co/sig-gen/',data=daa)
	return resp
@client.command("summon", condition=is_black)
def summon(data):
	param={"chatId":data.chatId,"comId":data.comId}
	d=json.dumps(param)
	daa={"data":d}
	taskss(daa)
	#client.join_screen_room(data.comId,data.chatId)
	data.subClient.send_message(data.chatId,message="Summoned")

@client.command("gcweloff")
def gcweloff(data):
	if client.check(data,"staff","admin"):
		f=open("cids.txt","w").close()
		results=gcw.find({},{'_id': 0})
		for i in results:
			y=i["comid"]
			z=open("cids.txt","a")
			z.write(str(y)+"\n")
		t = open('cids.txt','r')
		lists=[]
		for m in t.read().splitlines():
			temp=m
			if temp not in lists:
				lists.append(int(temp))
		if data.comId not in lists:
			it={"comid":data.comId}
			gcw.insert_one(it)
			data.subClient.send_message(data.chatId,message="GC welcome turned off")
		else:
			data.subClient.send_message(data.chatId,message="GC welcome already off")
	else:
		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)
	rebot()
		
@client.command("gcwelon")
def gcwelon(data):
	if client.check(data,"admin","staff"):
		gcw.delete_many({"comid":data.comId})
		data.subClient.send_message(data.chatId,message="GC welcome turned on")
	else:
		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)
	rebot()	

@client.on_member_join_chat()
def priviet(data):
	levl=int(data.subClient.get_user_info(data.authorId).level)
	#print(level)
	final=levels[(levl+1)]
	reep=int(data.subClient.get_user_info(userId=data.authorId).reputation)
	ix=reep #-int(levels[(levl)])
	iy=int(levels[(levl+1)]) #-int(levels[(levl)])
	percentage=calPercent(ix,iy)
	lists=[]
	results=gcw.find({},{'_id': 0})
	for i in results:
		y=i["comid"]
		z=open("cids.txt","a")
		z.write(str(y)+"\n")
		t = open('cids.txt','r')
		#lists=[]
		for m in t.read().splitlines():
			temp=m
			if temp not in lists:
				lists.append(int(temp))
	if data.comId not in lists:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			vip=data.subClient.get_user_info(data.authorId).influencerInfo
			plus=data.subClient.get_user_info(data.authorId).accountMembershipStatus
			following=data.subClient.get_user_info(data.authorId).followingCount
			followers=data.subClient.get_user_info(data.authorId).followersCount
			lvll=data.subClient.get_user_info(data.authorId).level
			frm=data.subClient.get_user_info(data.authorId).avatarFrame
			aiv=data.subClient.get_user_info(data.authorId).avatarFrameId
			rolee=data.subClient.get_user_info(data.authorId).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(data.authorId).icon
			response=requests.get(f"{x}")
			file=open("8ampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open("8ampl9e.png")
			
				
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,380))
			bg=Image.open("res.png").resize((800,800))
			if frm!=None and aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7":
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
				pty="fame"
				isdir = os.path.isdir(pty)
				if isdir==True or aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7" or aiv!=None:
					fg=Image.open("fame/frame.png").resize((860,860))
					bg.paste(fg,(-25,-25),fg)
					bg.save("new.png")
					fhg="new.png"
				elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
				else:
					fhg="res.png"
			elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			oii=Image.open("off.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			if plus==0:
				bgg.paste(oii,(480,45),oii)
			bgg.paste(bdg,(280,50),bdg)
			title_fot = ImageFont.truetype('fonts/unifont-15.0.01.ttf', 40)
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{data.author}", (255, 255,255), font=title_fot)
			draw.text((300,220), "Followed :", (255, 255,255), font=title_font)
			draw.text((535,220), "Followers :", (255,255,255), font=title_font)
			draw.text((450,215), f"{following}", (255,255,255), font=title_fn)
			draw.text((690,215), f"{followers}", (255,255,255), font=title_fn)
			bgg.save("ne.png")
		#	ftf=open("ne.png","rb")
			background = Editor("ne.png")
			background.rectangle((30, 290), width=730, height=40, fill="white", radius=20)
			background.bar(
            (30, 290),
            max_width=730,
            height=40,
            percentage=percentage,
            fill="#FA8072",
            radius=20,
        )
			background.text((40,297), f"{ix}", font=ImageFont.truetype("fonts/unifont-15.0.01.ttf",40), color="black")
			background.text((645,297), f"{iy}", font=ImageFont.truetype("fonts/unifont-15.0.01.ttf",40), color="black")
			ftf=background.image_bytes
			msg=f"""[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ
[BC]{data.author}
[BC]᭙ꫀꪶᥴꪮꪑꫀ ꪻꪮ
[CB]{tlt}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ"""
			data.subClient.full_embed("https://youtube.com/c/TechVision7",ftf,msg,data.chatId)
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
			
	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
	if kt !=None:
		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
	else:
		chatlink="Private Chat"
	val=data.subClient.get_chat_thread(data.chatId).title
	chats=data.subClient.favorite_chats
	if val ==None:
		val="Private Chat"
	for id in chats:
		try:
			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} joined {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[cu]Chat:
[c]{chatlink}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {val}")
			
		except:
			pass
	os.remove("fame/frame.png")
	os.remove("fame/frame.webp")
	os.remove("config.json")
	#pag="fame"
	#shutil.rmtree(pag)			

#@client.on_member_join_chat()
def privet(data):
	results=gcw.find({},{'_id': 0})
	for i in results:
		y=i["comid"]
		z=open("cids.txt","a")
		z.write(str(y)+"\n")
		t = open('cids.txt','r')
		lists=[]
		for m in t.read().splitlines():
			temp=m
			if temp not in lists:
				lists.append(int(temp))
	if data.comId not in lists:
			string_with_nonASCII =data.author
			encoded_string = string_with_nonASCII.encode("ascii", "ignore")
			decode_string = encoded_string.decode()
			dtty=decode_string
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(data.authorId).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png").resize((400,400))
			img2 = Image.open(".wel.png")
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 80)
			draw = ImageDraw.Draw(img2)
			draw.text((800,400), f"{dtty}", (237, 230, 211), font=title_font)
			img2.paste(img, (100,200))
			img2=img2.save(".iu88jh3.png")
			imgg=open(".iu88jh3.png","rb")
			Image.open(imgg).resize((863,400)).save("nss.png")
			ff=open("nss.png","rb")
			msg=(f"""[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[C]{data.author}
[BC]WELCOME
[C]TO
[C]{tlt}

[ICU]▿ Hope you enjoy your stay! ▿
[C]💐 | 🥳 | 🎪
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤""")	
			data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
			
	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
	if kt !=None:
		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
	else:
		chatlink="Private Chat"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats) :
			try:
				data.subClient.send_message(chatId=id,message=f"""[c]{data.author} joined {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[cu]Chat:
[c]{chatlink}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {val}")
			except:
				pass
		os.remove(".sampl9e.png")
		os.remove(".iu88jh3.png")
		os.remove("nss.png")

@client.command('ranks', condition=is_black)
def cavas(data):
        level=data.subClient.get_user_info(data.authorId).level
        final=levels[str(level+1)]
        rep=int(data.reputation)
        x=rep-int(levels[str(level)])
        y=int(levels[str(level+1)])-int(levels[str(level)])
        percentage=calPercent(x,y)
        background = Editor("bt.png")
        profile =load_image(str(data.authorIcon))
        #frame=data.subClient.get_user_info(data.authorId).avatarFrame
        profile = Editor(profile).resize((150, 150)).circle_image()
        poppins =ImageFont.truetype('fonts/calibril.ttf', 70)
        poppins_small = Font(path="fonts/ss.ttf").poppins(size=30)
        square = Canvas((500, 500), "#06FFBF")
        square = Editor(square)
        square.rotate(30, expand=True)
        background.paste(square.image, (600, -250))
        background.paste(profile.image, (30, 30))
        try:
            url=data.json["author"]["avatarFrame"]["resourceUrl"]
            img1=zipurl(url)
            if img1 !=None:
                av2 = Editor(img1).resize((180, 180))
                background.paste(av2, (16, 14))
        except:
            pass
        
        background.rectangle((30, 220), width=650, height=40, fill="white", radius=20)
        background.bar(
            (30, 220),
            max_width=650,
            height=40,
            percentage=percentage,
            fill="#2596be",
            radius=20,
        )
        status=data.json["author"]["accountMembershipStatus"]
        if status==1:
            plus = Editor("on.png").resize((40,40))
            background.paste(plus,(200,40))
        else:
            plus = Editor("off.png").resize((40,40))
            background.paste(plus,(200,40))
        sus=str(f"lvl/{level}.png")
        ll = Editor(sus).resize((70,70))
        background.text((254,39), data.author, font=ImageFont.truetype("fonts/unifont-15.0.01.ttf",45), color="white")
        background.paste(ll,(202,117))
        background.rectangle((200, 100), width=350, height=2, fill="#17F3F6")
        
        background.text(
            (294,136),
            f" Reputation :{rep}",
            font=ff("fonts/ss.ttf",40),
            color="white",
        )
        data.subClient.full_embed(message=f"{data.author}",chatId=data.chatId,image=background.image_bytes,link=f"ndc://user-profile/{data.authorId}")



@client.command("ioonk", condition=is_black)
def ranjjnk(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if "aminoapps.com" in data.message:
	   user=(client.get_from_code(data.message.split(' ')[0]).objectId)
	elif mention!=None:
		for x in mention:
		  user=x
	else:
		user=data.authorId
	
	if data.chatId:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			vip=data.subClient.get_user_info(user).influencerInfo
			plus=data.subClient.get_user_info(user).accountMembershipStatus
			following=data.subClient.get_user_info(user).followingCount
			repa=data.subClient.get_user_info(user).reputation
			lvll=data.subClient.get_user_info(user).level
			frm=data.subClient.get_user_info(user).avatarFrame
			rolee=data.subClient.get_user_info(user).role
			nick=data.subClient.get_user_info(user).nickname
			x=data.subClient.get_user_info(user).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			if frm!=None:
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,300))
			bg=Image.open("res.png").resize((800,800))
			pty="fame"
			isdir = os.path.isdir(pty)
			if isdir==True:
				fg=Image.open("fame/frame.png").resize((860,860))
				bg.paste(fg,(-25,-25),fg)
				bg.save("new.png")
				fhg="new.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			oii=Image.open("off.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			if plus==0:
				bgg.paste(oii,(480,45),oii)
			bgg.paste(bdg,(280,50),bdg)
			title_fot = ImageFont.truetype('fonts/unifont-15.0.01.ttf', 40)
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{nick}", (255, 255,255), font=title_fot)
			draw.text((300,220), "REPUTATION :", (255, 0,0), font=title_font)
			#draw.text((540,220), "followers :", (255,0,0), font=title_font)
			draw.text((465,215), f"{repa}", (255,255,255), font=title_fn)
		#	draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
			bgg.save("ne.png")
			ftf=open("ne.png","rb")
			msg=f"""[C]{nick}"""
			data.subClient.full_embed("https://youtube.com/c/TechVision7",ftf,msg,data.chatId)
	pag="fame"
	shutil.rmtree(pag)


@client.command("rnk", condition=is_black)
def rnk(data):
	
	if data.chatId:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			vip=data.subClient.get_user_info(data.authorId).influencerInfo
			plus=data.subClient.get_user_info(data.authorId).accountMembershipStatus
			following=data.subClient.get_user_info(data.authorId).followingCount
			repa=data.subClient.get_user_info(data.authorId).reputation
			lvll=data.subClient.get_user_info(data.authorId).level
			frm=data.subClient.get_user_info(data.authorId).avatarFrame
			rolee=data.subClient.get_user_info(data.authorId).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(data.authorId).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			if frm!=None:
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,300))
			bg=Image.open("res.png").resize((800,800))
			pty="fame"
			isdir = os.path.isdir(pty)
			if isdir==True:
				fg=Image.open("fame/frame.png").resize((860,860))
				bg.paste(fg,(-25,-25),fg)
				bg.save("new.png")
				fhg="new.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			bgg.paste(bdg,(280,50),bdg)
			title_fot = ImageFont.truetype('fonts/unifont-15.0.01.ttf', 40)
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{data.author}", (255, 255,255), font=title_fot)
			draw.text((300,220), "REPUTATION :", (255, 0,0), font=title_font)
			#draw.text((540,220), "followers :", (255,0,0), font=title_font)
			draw.text((465,215), f"{repa}", (255,255,255), font=title_fn)
		#	draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
			bgg.save("ne.png")
			ftf=open("ne.png","rb")
			msg=f"""[C]{data.author}"""
			data.subClient.full_embed("https://youtube.com/c/TechVision7",ftf,msg,data.chatId)
	pag="fame"
	shutil.rmtree(pag)
@client.command("coins")
def coins(data):
	data.subClient.send_message(data.chatId,message="Amino fixed the coins command",replyTo=data.messageId)
@client.command("dice", condition=is_black)
def dice(args):
    if not args.message:
        args.subClient.send_message(args.chatId, f"🎲 -{randint(1, 6)},- 🎲")
    else:
        try:
            n1, n2 = map(int, args.message.split('d'))
            times = n1 if n1 < 20 else 20
            max_num = n2 if n2 < 1_000_000 else 1_000_000
            numbers = [randint(1, (max_num)) for _ in range(times)]

            args.subClient.send_message(args.chatId, f'🎲 -{sum(numbers)},[ {" ".join(map(str, numbers))}](1-{max_num})- 🎲')
        except Exception as e:
            print_exception(e)

@client.command(condition=is_black)
def rock(args):
    com=random.randint(0,2)
    if com==1:
    	args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Rock🗿
    	
{args.author} vs Alexa
Match draw""",replyTo=args.messageId)
    elif com==0:
    		args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Paper📄

{args.author} vs Alexa
 Alexa won🎊""",replyTo=args.messageId)
    elif com==2:
    			args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Scissor✂️

{args.author} vs Alexa
{args.author} won🎊""",replyTo=args.messageId)
    		
@client.command(condition=is_black)
def paper(args):
    com=random.randint(0,2)
    if com==0:
    	args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Rock🗿

{args.author} vs Alexa
{args.author} won🎊""",replyTo=args.messageId)
    elif com==1:
    		args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Paper📄

{args.author} vs Alexa
Match draw""",replyTo=args.messageId)
    elif com==2:
    			args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Scissor✂️

{args.author} vs Alexa
Alexa won 🎊""",replyTo=args.messageId)

@client.command(condition=is_black)
def scissor(args):
    com=random.randint(0,2)
    if com==0:
    	args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Rock🗿

{args.author} vs Alexa
Alexa won 🎊""",replyTo=args.messageId)
    elif com==1:
    		args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Paper📄

{args.author} vs Alexa
{args.author} won 🎊""",replyTo=args.messageId)
    elif com==2:
    			args.subClient.send_message(args.chatId,message=f"""
[ci]Alexa Chose Scissor✂️

{args.author} vs Alexa
Match draw""",replyTo=args.messageId)
    			
@client.command(condition=is_black)
def gif(args):
  search = (args.message)
  response = requests.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=W05ZAoiUU7fHjXgOXU1Rs6No2CSULZUc')
  data = json.loads(response.text)
  gif_choice = randint(0, 9)
  image = data['data'][gif_choice]['images']['original']['url']
  print("URL",image)
  if image is not None:
                                              #print(image)
                                              filename = image.split("/")[-1]
                                              urllib.request.urlretrieve(image, filename)
                                              with open(filename, 'rb') as fp:
                                                                      args.subClient.send_message(args.chatId, file=fp, fileType="gif")
                                                                      os.remove(filename)

@client.command("gimg", condition=is_black)
def gimg(args):
  p=randint(1,10)
  imfile= f"my_img{randint(1,500)}"
  #imfile="sample"
  search = (args.message)
  gis = GoogleImagesSearch('AIzaSyAynK30eehfoGLNfE9M9FcLa02fkLgqHJo', '6db11cc9d8e3e8d87')
  _search_params = {'q': search,'num': 1}
  try:
  	gis.search(search_params=_search_params,path_to_dir=f'{path_download}',custom_image_name=imfile)
  	imgg=(f"{path_download}/{imfile}.jpg")
  	Image.open(imgg).resize((800,700)).save("imagi.png")
  	ff=open("imagi.png","rb")
  	msg=f"[B]{args.message} requested by {args.author}"
  	args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
  	os.remove(f"{path_download}/{imfile}.jpg")
  	#os.remove("imagi.png")
  except:
  	args.subClient.send_message(args.chatId,message="Image not found",replyTo=args.messageId)
  	pass

@client.command("img", condition=is_black)
def img(args):
  if args.message:
  	p=randint(1,10)
  #	imfile= f"my_img{randint(1,500)}"
  	search = (args.message)
  	gis = GoogleImagesSearch('AIzaSyB4Ekh8Z3Ie99Qt9V7Rui3dxbTJ0N2qXCc', '42e3ecc0e1ca6412f')
  	_search_params = {'q': search,'num': 5,'safe':'high'}
  	try:
  		gis.search(search_params=_search_params,path_to_dir='Dow')
  		h=os.listdir("Dow")
  		#=random.choice(os.listdir("Dow"))
  		s=random.choice(os.listdir("Dow"))
  	#	for i in h:
  		#	if i.endswith(".jpg"):
  			#	s=random.choice(os.listdir("Dow"))
  		#	else:
  			#	s=os.listdir("Dow")[1]
  		Image.open(f"Dow/{s}").resize((800,800)).save("imajgi.png")
  		ff=open("imajgi.png","rb")
  		msg=f"[B]{args.message}"
  		args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
  		os.remove("imajgi.png")
  		shutil.rmtree("Dow")
  	#os.remove("imagi.png")
  	except:
  		args.subClient.send_message(args.chatId,message="Image not found",replyTo=args.messageId)
  		pass
  else:
  	args.subClient.send_message(args.chatId,message="Tell me what to search",replyTo=args.messageId)


@client.command("inkmg", condition=is_black)
def ibbmg(args):
  if client.check(args,"admin"):
  	p=randint(1,10)
  	imfile= f"my_img{randint(1,500)}"
  	search = (args.message)
  	gis = GoogleImagesSearch('AIzaSyAynK30eehfoGLNfE9M9FcLa02fkLgqHJo', '6db11cc9d8e3e8d87')
  	_search_params = {'q': search,'num': 1}
  	try:
  		gis.search(search_params=_search_params,path_to_dir=f'{path_download}',custom_image_name=imfile)
  		imgg=(f"{path_download}/{imfile}.jpg")
  		Image.open(imgg).resize((800,700)).save("imagi.png")
  		ff=open("imagi.png","rb")
  		msg=f"[B]{args.message} requested by {args.author}"
  		args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
  		os.remove(f"{path_download}/{imfile}.jpg")
  	#os.remove("imagi.png")
  	except:
  		args.subClient.send_message(args.chatId,message="Image not found",replyTo=args.messageId)
  		pass
  else:
  	args.subClient.send_message(args.chatId,message="Admin command",replyTo=args.messageId)
		  	
@client.command("pics")
def pics(data):
	data.subClient.send_message(data.chatId,message="Command locked",replyTo=data.messageId)
def embfull(data):	
	if data:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			vip=data.subClient.get_user_info(data.authorId).influencerInfo
			plus=data.subClient.get_user_info(data.authorId).accountMembershipStatus
			following=data.subClient.get_user_info(data.authorId).followingCount
			repa=data.subClient.get_user_info(data.authorId).reputation
			lvll=data.subClient.get_user_info(data.authorId).level
			frm=data.subClient.get_user_info(data.authorId).avatarFrame
			rolee=data.subClient.get_user_info(data.authorId).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(data.authorId).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			if frm!=None:
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,300))
			bg=Image.open("res.png").resize((800,800))
			pty="fame"
			isdir = os.path.isdir(pty)
			if isdir==True:
				fg=Image.open("fame/frame.png").resize((860,860))
				bg.paste(fg,(-25,-25),fg)
				bg.save("new.png")
				fhg="new.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			bgg.paste(bdg,(280,50),bdg)
			title_fot = ImageFont.truetype('fonts/unifont-15.0.01.ttf', 40)
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{data.author}", (255, 255,255), font=title_fot)
			draw.text((300,220), "followed :", (255, 0,0), font=title_font)
			draw.text((540,220), "followers :", (255,0,0), font=title_font)
			draw.text((445,215), f"{following}", (255,255,255), font=title_fn)
			draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
			bgg.save("neee.png")	

def embdfull(data,user):	
	if data:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			nick=data.subClient.get_user_info(user).nickname
			vip=data.subClient.get_user_info(user).influencerInfo
			plus=data.subClient.get_user_info(user).accountMembershipStatus
			following=data.subClient.get_user_info(user).followingCount
			followers=data.subClient.get_user_info(user).followersCount
			aiv=data.subClient.get_user_info(data.authorId).avatarFrameId
			lvll=data.subClient.get_user_info(user).level
			frm=data.subClient.get_user_info(user).avatarFrame
			rolee=data.subClient.get_user_info(user).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(user).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("bt.png").resize((800,300))
			bg=Image.open("res.png").resize((800,800))
			if frm!=None and aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7":
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
				pty="fame"
				isdir = os.path.isdir(pty)
				if isdir==True or aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7" or aiv!=None:
					fg=Image.open("fame/frame.png").resize((860,860))
					bg.paste(fg,(-25,-25),fg)
					bg.save("new.png")
					fhg="new.png"
				elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
				else:
					fhg="res.png"
			elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
			else:
				fhg="res.png"
			
				
			j=Image.open(fhg).resize((230,230))
			k=Image.open("vip.png").resize((60,60))
			l=Image.open("plus.png").resize((80,80))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,60))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,60))
			else:
				bdg=Image.open("member.png").resize((150,60))
			lv=Image.open(f"level/{lvll}.png").resize((90,90))
			bgg.paste(j,(30,30),j)
			if vip!=None:
				bgg.paste(k,(560,53),k)
			bgg.paste(lv,(660,35),lv)
			if plus==1:
				bgg.paste(l,(480,45),l)
			bgg.paste(bdg,(280,50),bdg)
			title_fot = ImageFont.truetype('fonts/unifont-15.0.01.ttf', 40)
			title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
			title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
			title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
			draw = ImageDraw.Draw(bgg)
			draw.text((300,150), f"{nick}", (255, 255,255), font=title_fot)
			draw.text((300,220), "followed :", (255, 0,0), font=title_font)
			draw.text((540,220), "followers :", (255,0,0), font=title_font)
			draw.text((445,215), f"{following}", (255,255,255), font=title_fn)
			draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
			bgg.save("neeee.png")
@client.command("imkkkkg")
def imkkkg(data):
	data.subClient.send_message(data.chatId,message="Command locked",replyTo=data.messageId)
@client.command("imgn")
def imgn(args):
  search = (args.message)
  response = requests.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=W05ZAoiUU7fHjXgOXU1Rs6No2CSULZUc')
  data = json.loads(response.text)
  gif_choice = randint(0, 9)
  image = data['data'][gif_choice]['images']['original']['url']
  print("URL",image)
  if image is not None:
                                              #print(image)
                                              filename = "imageg.png"
                                              urllib.request.urlretrieve(image, filename)
                                              imgg=("imageg.png")
                                              Image.open(imgg).resize((800,700)).save("jaks.png")
                                              ff=open("jaks.png","rb")
                                              msg=f"[B]{args.message} requested by {args.author}"
                                              args.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,args.chatId)
                                              os.remove(filename)

@client.command(condition=is_black)
def prank(data):
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	current_time=now.strftime("%H:%M:%S")
	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
	if x==data.authorId:
		data.subClient.send_message(data.chatId,message="Prank is not for Host")
		pass
	else:
		data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="Clear")
		#data.subClient.transfer_host(data.chatId,userIds=[client.userId])
		#info=data.subClient.get_chat_thread(data.chatId)
		#x=info.json['extensions']['organizerTransferRequest']['requestId']
		#data.subClient.accept_organizer(chatId=data.chatId,requestId=x)
		h=data.subClient.get_chat_thread(data.chatId).title
		data.subClient.kick(data.authorId,data.chatId,allowRejoin=True)
		data.subClient.start_chat(data.authorId,message=f"""
[c]Prank

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[c]{data.author}
[c]I kicked you from {h},
[c]You can join again your GC {h}
[c]Your Chatroom is safe
[c]How was my prank :)

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}			
""")
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		if kt !=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		chats=data.subClient.favorite_chats
		for id, in zip(chats) :
			data.subClient.send_message(chatId=id,message=f"""[c]Prank command by {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {h}")

@client.command("check", condition=is_black)
def check(data):
	results=test_1.find({},{'_id': 0})
	lists=[]
	for i in results:
		#print(i)
		y=i["comid"]
		if y not in lists:
			lists.append(y)
	#f=open("comid.txt","r")
	#Counter = 0
	#Content = f.read()
	#CoList = Content.split("\n")
	#for i in CoList:
	#	if i:
			#Counter += 1
	count=len(lists)
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	xh=data.subClient.favorite_chats
	if len(xh)!=0 and data.subClient.is_in_staff(client.userId):
		j="✔"
		t="✔"
	elif len(xh)!=0 and rol==0:
		t="╳"
		j="✔"
	elif len(xh)==0 and rol!=0:
		t="✔"
		j="╳"
	elif len(xh)==0 and rol==0:
		t="╳"
		j="╳"
	ias=("help.png")
	Image.open(ias).resize((863,400)).save("nys.png")
	ff=open("nys.png","rb")
	msg=f"""
[CU]𝗔𝗟𝗘𝗫𝗔 𝗜𝗡𝗙𝗢

◈ sᴛᴀᴛᴜs :  ✔
◈ ɪɴ ᴍᴏᴅ : {t}
◈ ʙᴏᴛʟᴏɢ : {j}
◈ ᴀɴᴛɪʀᴀɪᴅ : {t}
◈ ᴀᴄᴛɪᴠᴇ ɪɴ : {count} ᴄᴏᴍᴍᴜɴɪᴛɪᴇs
◈ ʀᴇsᴘᴏɴsᴇ : 0.0{random.randint(2,4)}s
"""
	data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
	client.show_online(data.comId)

@client.command("c", condition=is_black)
def c(args):
    ms = args.message
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    current_time=now.strftime("%H:%M:%S")
    idd=args.subClient.welcome_chat
    for id in idd:
    	if len(idd)!=0:
    		cy=args.subClient.get_chat_thread(args.chatId).title
    		x=args.subClient.get_chat_thread(chatId=id).title
    		if cy!=None:
    			args.subClient.send_message(args.chatId,message="[i]Confession should be private, so better send your confession in my Pm\nI will send in chatroom",replyTo=args.messageId)
    		else:
    			args.subClient.send_message(chatId=id, message=f"""
[cu]Confession Box

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[ci]{ms}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time:{current_time}
""")
    			args.subClient.send_message(args.chatId,message=f"""
Your confession is done in {x}

Now You can delete your confession from my pm""")
    	else:
    		args.subClient.send_message(args.chatId,message="""
Set Confession GC first
Ask your Leader or Curator to set Confession GC""")
		

@client.command("join", condition=is_black)
def join(args):
    val = args.subClient.join_chatroom(args.message, args.chatId)
    if val or val == "":
        args.subClient.send_message(args.chatId, f"Chat {val} joined".strip())
    else:
        args.subClient.send_message(args.chatId, "No chat joined")


@client.command("joinall",condition=is_black)
def join_all(args):
        if client.check(args,"staff","admin"):
        	args.subClient.join_all_chat()
        	args.subClient.send_message(args.chatId, "Joined all chatrooms")
        else:
        	args.subClient.send_message(args.chatId, "Mod command",replyTo=args.messageId)
        	


@client.command()
def leaveall(args):
	if client.check(args,'admin'):
		args.subClient.send_message(args.chatId, "Leaving all chatrooms...")
		for i in range(5):
			args.subClient.leave_all_chats()


@client.command()
def leave(args):
    if args.message and (client.check(args, 'staff','admin')):
        chat_ide = args.subClient.get_chat_id(args.message)
        if chat_ide:
            args.chatId = chat_ide
    args.subClient.leave_chat(args.chatId)



@client.command("fcoin", condition=is_black)
def fcoin(args):
    x=int(args.message)
    transaction = "66ddb9b0-ac8c-4cc4-9d08-deede82fb020"
    if x<=500 or x==500:
    	args.subClient.send_coins(coins=x, chatId=args.chatId, transactionId=transaction)
    else:
    		args.subClient.send_message(chatId=args.chatId,message="[ic]Can't send more than 500 coins dear")


@client.command("ghost", condition=is_black)
def ghost(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if (rol==100,rol==101):
		data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="Clear")
		data.subClient.send_message(data.chatId,data.message,type=107)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats):
			data.subClient.send_message(chatId=id,message=f"""[c]Ghost command by {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[c]{data.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="[i]I don't have' Curator or Leader")
		pass

@client.command("wanted", condition=is_black)
def wanted(data):
			img=open(".wanted.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".wanted.png")
				img1 = Image.open(".aale.png").resize((447,447))
				img.paste(img1, (150,250))
				img=img.save("i3.png")
				imgg=open("i3.png","rb")
				try:
					#Image.open("i3.png").resize((837, 400)).save("ani.png")
					#with open("ani.png","rb") as f:
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,f"{nkn} is Wanted 🧤",data.chatId)
					os.remove("i3.png")
					os.remove(".aale.png")
				except Exception as e:
					print(e)
					pass
					
@client.command("wtf", condition=is_black)
def wtf(data):
			img=open(".wf.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aijhale.png","wb")
				file.write(response.content)
				file.close()
				Image.open(".wf.png").resize((837,736)).save("wyf.png")
				img=Image.open("wyf.png")
				img1 = Image.open(".aijhale.png").resize((150,150))
				img.paste(img1, (580,95))
				img.paste(img1, (590,530))
				img=img.save(".ihh3.png")
				imgg=open(".ihh3.png","rb")
				try:
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,f"What the f*ck {nkn}",data.chatId)
					os.remove(".ihh3.png")
					os.remove(".aijhale.png")
				except:
					pass

@client.command("rip", condition=is_black)
def rip(data):
			img=open(".ripe.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".ai8yijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".ripe.png").resize((642,806))
				img1 = Image.open(".ai8yijhale.png").resize((300,300))
				img.paste(img1, (175,385))
				#img.paste(img1, (750,1250))
				img=img.save(".yivhh3.png")
				imgg=open(".yivhh3.png","rb")
				try:
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,f"RIP {nkn} 🕯️",data.chatId)
					os.remove(".ai8yijhale.png")
					os.remove(".yivhh3.png")
				except:
					pass


@client.command("kill", condition=is_black)
def kill(data):
			img=open(".sword.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aiyijhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".sword.png")
				img1 = Image.open(".aiyijhale.png").resize((175,175))
				img.paste(img1, (295,670))
				#img.paste(img1, (750,1250))
				img=img.save(".yihh3.png")
				imgg=open(".yihh3.png","rb")
				try:
					msg=f"{data.author} killed {nkn} 🗡️"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aiyijhale.png")
					os.remove(".yihh3.png")
				except:
					pass
					
@client.command("spank", condition=is_black)
def spank(data):
			img=open(".sank.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aiy88ijhale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".a8n8ie.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".sank.png")
				img1 = Image.open(".aiy88ijhale.png").resize((140,140))
				img2 =Image.open(".a8n8ie.png").resize((160,160))
				img.paste(img1, (700,505))
				img.paste(img2, (460,100))
				img=img.save(".ybi9hh3.png")
				imgg=open(".ybi9hh3.png","rb")
				try:
					msg=f"{data.author} spanked {nkn} 😳"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aiy88ijhale.png")
					os.remove("a8n8ie.png")
					os.remove(".ybi9hh3.png")
				except:
					pass
@client.command("slipper", condition=is_black)
def slipper(data):
			#img=open("slip.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".slips.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".usere.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open("slip.png").resize((800,1000))
				img1 = Image.open(".slips.png").resize((250,250))
				img2 =Image.open(".usere.png").resize((130,130))
				img.paste(img1, (520,620))
				img.paste(img2, (570,35))
				img=img.save(".ybhh3.png")
				imgg=open(".ybhh3.png","rb")
				try:
					msg=f"{data.author} smashed {nkn} 👢"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".usere.png")
					os.remove(".ybhh3.png")
				except:
					pass					

@client.command("chappal", condition=is_black)
def slpper(data):
			#img=open("slip.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".slips.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".usere.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open("slip.png").resize((800,1000))
				img1 = Image.open(".slips.png").resize((250,250))
				img2 =Image.open(".usere.png").resize((130,130))
				img.paste(img1, (520,620))
				img.paste(img2, (570,35))
				img=img.save(".ybhh3.png")
				imgg=open(".ybhh3.png","rb")
				try:
					msg=f"{data.author} smashed {nkn} 👢"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".usere.png")
					os.remove(".ybhh3.png")
				except:
					pass

@client.command("door", condition=is_black)
def door(data):
			img=open(".door.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a0jhale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".door.png")
				img1 = Image.open(".a0jhale.png").resize((240,220))
				img.paste(img1, (405,20))
				#img.paste(img1, (750,1250))
				img=img.save(".yinhh3.png")
				imgg=open(".yinhh3.png","rb")
				try:
					msg=f"{data.author} smashed {nkn} 👻"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".a0jhale.png")
					os.remove(".yinhh3.png")
				except:
					pass				
@client.command("gay", condition=is_black)
def gay(data):
			img=open(".gay.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a7ale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".gay.png").resize((800,800))
				img1 = Image.open(".a7ale.png").resize((800,800))
				#img.size
				#img1.size 
				#img_size = img.resize((800, 400))
				#img1_size = img1.resize((447, 447))
				img.putalpha(128)
				img1.paste(img, (0,0),img)
				img1=img1.save(".img73.png")
				imgg=open(".img73.png","rb")
				try:
					msg=f"{nkn} is Gay 🙂"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".a7ale.png")
					os.remove(".img73.png")
				except:
					pass

@client.command("disable", condition=is_black)
def disable(data):
			img=open(".disability.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aa9le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".disability.png")
				img1 = Image.open(".aa9le.png").resize((175,175))
				img.paste(img1, (450,325))
				img=img.save(".i7mg3.png")
				imgg=open(".i7mg3.png","rb")
				try:
					msg=f"{nkn} is Disable 👀"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aa9le.png")
					os.remove(".i7mg3.png")
				except:
					pass

@client.command("brazz", condition=is_black)
def brazz(data):
			img=open(".braz.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aai9le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".braz.png")
				img1 = Image.open(".aai9le.png")
				aspect = img1.width / img1.height
				new_height = int(img.height * aspect)
				new_width = int(img.width * aspect)
				scale = new_width / img1.width
				size = (int(new_width / scale / 2), int(new_height / scale / 2))
				img = img.resize(size).convert('RGBA')
				img1.paste(img, (img1.width - img.width,img1.height - img.height), img)
				#img.paste(img1, (450,325))
				img1=img1.save(".img3.png")
				imgg=(".img3.png")
				Image.open(imgg).resize((800,600)).save("hes.png")
				ff=open("hes.png","rb")
				
				try:
					msg=f"{nkn} joined Brazzers 🔞"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					os.remove(".aai9le.png")
					os.remove(".img3.png")
					os.remove("hes.png")
				except:
					pass

@client.command("medal", condition=is_black)
def medal(data):
			img=open(".medal.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aa999le.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".medal.png")
				img1 = Image.open(".aa999le.png").resize((200,200)) 
				#img.size
				#img1.size 
				#img_size = img.resize((800, 400))
				#img1_size = img1.resize((75,75))
				img.paste(img1,(120,73))
				img.paste(img1, (365,0))
				img=img.save(".im88ig3.png")
				imgg=open(".im88ig3.png","rb")
				try:
					msg=f"{nkn} got medal from {nkn} 🏅"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aa999le.png")
					os.remove(".im88ig3.png")
				except:
					pass


@client.command("shit", condition=is_black)
def shit(data):
			img=open(".shit.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aokale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".shit.png")
				img1 = Image.open(".aokale.png").resize((135,135))
				img.paste(img1, (220,750))
				img=img.save(".im88g3.png")
				imgg=open(".im88g3.png","rb")
				try:
					msg=f"{nkn} is Shit 💩"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aokale.png")
					os.remove(".im88g3.png")
				except:
					pass

@client.command("slap", condition=is_black)
def slap(data):
			img=open(".slap.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".haas.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aie.png","wb")
				file.write(response.content)
				file.close()
				Image.open(".slap.png").resize((837,736)).save("slape.png")
				img=Image.open("slape.png")
				img1 = Image.open(".haas.png").resize((190,190)) 
				img2= Image.open(".aie.png").resize((180,180))
				img.paste(img1, (500,400))
				img.paste(img2, (290,100))
				img=img.save(".ijs.png")
				#imgg=open(".ijs.png")
				#Image.open(imgg).resize((1000,500)).save("heas.png")
				ff=open(".ijs.png","rb")
				try:
					msg=f"{data.author} slapped {nkn} 👋"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					os.remove(".haas.png")
					os.remove(".aie.png")
					os.remove(".slape.png")
					os.remove(".ijs.png")
				except:
					pass

								
@client.command("jail", condition=is_black)
def jail(data):
			img=open(".jail.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".aauile.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".jail.png").resize((800,800))
				img1 = Image.open(".aauile.png").resize((800,800))
				#img1.size 
				#img1_size = img1.resize((350, 3�50))
				img1.paste(img, (0,0),img)
				img1=img1.save(".i3i.png")
				imgg=open(".i3i.png","rb")
				try:
					msg=f"{nkn} is in Jail"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".aauile.png")
					os.remove(".i3i.png")
				except:
					pass					
				
							
@client.command("trash", condition=is_black)
def trash(data):
			img=open(".trash.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a77ale.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".trash.png") 
				img1 = Image.open(".a77ale.png").resize((483,483))
				img.paste(img1, (480,0))
				img=img.save(".iw83.png")
				imgg=open(".iw83.png","rb")
				try:
					msg=f"You are trash {nkn} 🗑️"
					data.subClient.full_embed("https://youtube.com/c/TechVision7",imgg,msg,data.chatId)
					os.remove(".a77ale.png")
					os.remove(".iw83.png")
				except:
					pass			

@client.command("hate", condition=is_black)
def hate(data):
			heart="💖"
			brk="💔"
			ship=(random.randint(0,100))
		
			#img9=open("heart.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open("ale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open("kme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open("kme.png") 
				img1 = Image.open("ale.png")
				img9=Image.open("brok.png")
				img.size
				img1.size
				img9.size
				img91 = img9.resize((170,170))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2.paste(img91,(317,150),img91)
				
				img2=img2.save("mg3.png")
				imgg=open("mg3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nsks.png")
				ff=open("nsks.png","rb")
				#try:
				#	if 0 <= ship <= 10:
				msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💔 {data.author}
[C]Hate
[BC]{ship} %
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
				data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
@client.command(condition=is_black)
def online(data):
  dm=["Chatting"]
  data.subClient.send_message(data.chatId,message="Alexa joined live layer")
  while True:
    client.show_online(data.comId)
    client.send_action(actions=dm,comId=data.comId,chatId=data.chatId)

@client.command("love", condition=is_black)
def love(data):
			heart="💖"
			brk="💔"
			ship=(random.randint(0,100))
			lis1=['Friendzone','Just Friends','Friends','There is barely any love','No chance for love']
			lis2=['Still in Friendzone','Friends']
			lis3=['But there is a small sense of romance from on person!','I sense a small bit of love','But there is a small bit of love somewhere']
			lis3=['There is a bit of love there!','There is a bit of love there...','A small bit of love is in the air...']
			lis4=["But it's very one-sided OwO","It appears one sided!","There's some potential!","I sense a bit of potential!","There's a bit of romance going on here!","I feel like there's some romance progressing!","The love is getting there..."]
			lis8=["Love is in the air!","I can definitely feel the love","I feel the love! There's a sign of a match!","There's a sign of a match!","I sense a match!","A few things can be imporved to make this a match made in heaven!"]
			lis6=["There is definitely love somewhere!","I can see the love is there! Somewhere...","I definitely can see that love is in the air"]
			lis9=["It's a match!","There's a match made in heaven!","It's definitely a match!","Love is truely in the air!","Love is most definitely in the air!"]
			lis7=["Love is in the air!","I can definitely feel the love","I feel the love! There's a sign of a match!","There's a sign of a match!","I sense a match!","A few things can be imporved to make this a match made in heaven!"]
			lis5=["I feel the romance progressing!","There's some love in the air!","I'm starting to feel some love!"]
			#img9=open("heart.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				nkn=data.subClient.get_user_info(str(user)).nickname
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axuale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aikme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aikme.png") 
				img1 = Image.open(".axuale.png")
				img9=Image.open("hearts.png")
				img.size
				img1.size
				img9.size
				img91 = img9.resize((170,170))
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2.paste(img91,(317,150),img91)
				
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				
				#imgg=imgg.save("vhu.png")
				Image.open(imgg).resize((863,400)).save("nskks.png")
				ff=open("nskks.png","rb")
				try:
					if 0 <= ship <= 10:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💔 {data.author}

[C]Really Low!😣
[BC]■□□□□ {ship}
[C]{(random.choice(lis1))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 20<= ship <=30:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Low!😔
[BC]■■□□□ {ship}
[C]{(random.choice(lis2))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 30<= ship <=40:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Poor!🥺
[BC]■■□□□ {ship}
[C]{(random.choice(lis3))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 40<= ship <=50:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Fair!🥰
[BC]■■■□□ {ship}
[C]{(random.choice(lis4))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 50<= ship <=60:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C] Moderate!🤗
[BC]■■■□□ {ship}
[C]{(random.choice(lis5))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 60<= ship <=70:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Good!🥳
[BC]■■■■□ {ship}
[C]{(random.choice(lis6))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 70<= ship <=80:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Great!
[BC]■■■■□ {ship}
[C]{(random.choice(lis7))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 80<= ship <=90:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]Over Average!🤩
[BC]■■■■□ {ship}
[C]{(random.choice(lis8))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
					elif 90<= ship <=100:
						msg=f"""
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤
[B]{nkn} 💖 {data.author}

[C]True Love!😍
[BC]■■■■■ {ship}
[C]{(random.choice(lis9))}
[C]⁰✧⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ຈ¤"""
						data.subClient.full_embed("https://youtube.com/c/TechVision7",ff,msg,data.chatId)
						os.remove(".axuale.png")
						os.remove(".aikme.png")
						os.remove(".img3.png")					
				except:
					pass

@client.command("ship", condition=is_black)
def ship(data):
			img9=open(".pro.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".axuale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aikme.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aikme.png") 
				img1 = Image.open(".axuale.png") 
				img.size
				img1.size 
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				msg = data.message + " null null "
				msg = msg.split(" ")
				msg[2] = msg[1]
				msg[1] = msg[0]
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image",embedTitle=f"Love match❤️ {random.randint(0,100)}% ❵",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedContent="𝑀𝑎𝑑𝑒 𝑏𝑦 ᴛᴇᴄʜᴠɪsɪᴏɴ",embedImage=img9)
				except:
					pass

@client.command("hated", condition=is_black)
def hated(data):
			img9=open(".pro.png","rb")
			mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
			for user in mention:
				h=data.subClient.get_user_info(str(user)).icon
				response=requests.get(f"{h}")
				file=open(".a11ale.png","wb")
				file.write(response.content)
				file.close()
				x=data.subClient.get_user_info(data.authorId).icon
				response=requests.get(f"{x}")
				file=open(".aike.png","wb")
				file.write(response.content)
				file.close()
				img = Image.open(".aike.png") 
				img1 = Image.open(".a11ale.png") 
				img.size
				img1.size 
				img_size = img.resize((400, 400))
				img1_size = img1.resize((400, 400))
				img2 = Image.new("RGB", (800, 400), "white")
				img2.paste(img_size, (0, 0))
				img2.paste(img1_size, (400, 0))
				img2=img2.save(".img3.png")
				imgg=open(".img3.png","rb")
				msg = data.message + " null null "
				msg = msg.split(" ")
				msg[2] = msg[1]
				msg[1] = msg[0]
				try:
					data.subClient.send_message(chatId=data.chatId,file=imgg,fileType="image",embedTitle=f"Hate💔 ❴ {random.randint(0,100)}% ❵",embedLink="https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg",embedContent="𝑀𝑎𝑑𝑒 𝑏𝑦 ᴛᴇᴄʜᴠɪsɪᴏɴ",embedImage=img9)
					os.remove(".a11ale.png")
					os.remove(".aike.png")
					os.remove(".img3.png")
				except:
					pass
@client.command("chatbg", condition=is_black)
def chatbg(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
        if image is not None:
                        	filetype = image.split(".")[-1]
                        	filename = image.split("/")[-1]
                        	urllib.request.urlretrieve(image, filename)
                        	with open(filename, 'rb') as fp:
                        	        	        	        		with suppress(Exception):
                        	        	        	        		        			if filetype!="gif":
                        	        	        	        		        				filety="image"
                        	        	        	        		        			else:
                        	        	        	        		        				filety="gif"
                        	        	        	        		        			data.subClient.send_message(data.chatId, file=fp, fileType=filety)
                        	        	        	        		        			os.remove(filename)

@client.command("chaticon", condition=is_black)
def chaticon(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).icon
        if image is not None:
                        	filetype = image.split(".")[-1]
                        	filename = image.split("/")[-1]
                        	urllib.request.urlretrieve(image, filename)
                        	with open(filename, 'rb') as fp:
                        	        	        	        		with suppress(Exception):
                        	        	        	        		        			if filetype!="gif":
                        	        	        	        		        				filetyp="image"
                        	        	        	        		        			else:
                        	        	        	        		        				filetyp="gif"
                        	        	        	        		        			data.subClient.send_message(data.chatId, file=fp, fileType=filetyp)
@client.command("sticker", condition=is_black)
def sticker(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
				   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
				   filename = image.split("/")[-1]
				   filetype = image.split(".")[-1]
				   if filetype!="gif":
				   	   	   	   	   	filetype = "image"
				   	   	   	   	   	urllib.request.urlretrieve(image, filename)
				   	   	   	   	   	with open(filename, 'rb') as fp:
				   	   	   	   	   		   		   		   	   	with suppress(Exception):
				   	   	   	   	   		   		   		   	   		   	   		data.subClient.send_message(data.chatId, file=fp, fileType=filetype)


@client.command("mention", condition=is_black)
def mention(args):
    try:
        size = int(args.message.strip().split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 1

    val = args.subClient.get_user_id(args.message)
    if not val:
        args.subClient.send_message(chatId=args.chatId, message="Username not found")
        return

    if size > 5 and not (client.check(args, 'staff', 'admin')):
        size = 5

    if val:
        for _ in range(size):
            with suppress(Exception):
                args.subClient.send_message(chatId=args.chatId, message=f"‎‏‎‏@{val[0]}‬‭", mentionUserIds=[val[1]])


@client.command("mentionall")
def mentionall(args):
    if client.check(args, 'staff', 'admin'):
        if args.message and client.check(args, 'admin'):
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId,size=1000).userId]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId,size=1000).userId])
        #print(test)

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"<$@everyone{test}$>", mentionUserIds=mention)

@client.command("all")
def mall(args):
    if client.check(args, 'staff', 'admin'):
        if args.message and client.check(args, 'staff','admin'):
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId,size=1000).userId]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId,size=1000).userId])
        #print(test)

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"<$@everyone{test}$>", mentionUserIds=mention)

@client.command("hidden", condition=is_black)
def hidden(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10 and not (client.check(args, 'staff', 'admin')):
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value, mentionUserIds=ment)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            kt=args.subClient.get_chat_thread(args.chatId). membersCanInvite
            if kt!=None:
            	op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
            	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
            else:
            	chatlink="Private Chat"
            val=args.subClient.get_chat_thread(args.chatId).title
            chats=args.subClient.favorite_chats
            if val ==None:
            	val="Private Chat"
            for id, in zip(chats) :
            	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} used hidden message in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")


@client.command("abanword")
def add_banned_word(args):
    if client.check(args, 'staff','admin'):
        if not args.message or args.message in args.subClient.banned_words:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.add_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} added to banned words")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        kt=args.subClient.get_chat_thread(args.chatId). membersCanInvite
        
        #chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        if kt!=None:
        	op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
        	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
        else:
        	chatlink="Private Chat"
        val=args.subClient.get_chat_thread(args.chatId).title
        chats=args.subClient.favorite_chats
        if val ==None:
        	val="Private Chat"
        for id, in zip(chats) :
        	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} added banned word

[c]{args.message}

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")
    rebot()


@client.command("rbanword")
def remove_banned_word(args):
    if client.check(args, 'staff','admin'):
        if not args.message:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.remove_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} removed from banned words")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time=now.strftime("%H:%M:%S")
        kt=args.subClient.get_chat_thread(args.chatId). membersCanInvite
        
        #chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        if kt!=None:
        	op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
        	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
        else:
        	chatlink="Private Chat"
        val=args.subClient.get_chat_thread(args.chatId).title
        chats=args.subClient.favorite_chats
        if val ==None:
        	val="Private Chat"
        for id, in zip(chats) :
        	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} removed banned word

[c]{args.message}

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")
    rebot()


@client.command("banword", condition=is_black)
def banned_word_list(args):
    val = ""
    if args.subClient.banned_words:
        for elem in args.subClient.banned_words:
            val +="◈" + elem + "\n"
    else:
        val = "No words in the list"
    try:
    	args.subClient.send_message(args.chatId, message=f"""
[c]Banned Words
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    except Exception:
    	args.subClient.send_message(args.chatId, message="Banword limit exceeded")
    	pass
@client.command("lurker", condition=is_black)
def lurker(args):
    list=[]
    users = args.subClient.get_live_layer().json[0]["userProfileList"]
    for user in users:
    	i=(user["nickname"])
    	list.append(i)
    val = ""
    if list:
        for elem in list:
            val +="◈" + elem + "\n"
    else:
        val = "No Lurkers"
    args.subClient.send_message(args.chatId, message=f"""
[c]Lurkers👀
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""") 	

@client.command("stickmg")
def stickmg(args):
	info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: args.subClient.send_message(args.chatId, file=fp, fileType="image")
	os.remove(filename)


@client.command()
def backround(data):
	if client.check(data,'staff','admin'):
		info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
		reply_message = info.json['extensions']
		if reply_message:
			image = info.json['extensions']['replyMessage']['mediaValue']
		if image is not None:
			filename="anime88.png"
			urllib.request.urlretrieve(image, filename)
			img=open("anime88.png","rb")
			im=[img]
			for i in range(1,5):
				try:
					data.subClient.edit_profile(imageList=im)
				except Exception:
					pass
			data.subClient.send_message(data.chatId, message="BG pic changed",replyTo=data.messageId)
			os.remove(filename)

@client.command("pam", condition=is_black)
def spm(args):
    quantity, msg = args.message.split()
    quantity = 1 if not quantity.isdigit() else int(quantity)
    quantity = 20 if quantity > 20 and not (client.check(args, 'admin')) else quantity
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    current_time=now.strftime("%H:%M:%S")
    #chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
    op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
    chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    val=args.subClient.get_chat_thread(args.chatId).title
    ch=args.subClient.favorite_chats
    if val ==None:
    	val="Private Chat"
    for id in ch:
    	for i in range(1):
    		args.subClient.send_message(chatId=id,message=f"""[c]Spam command by {args.author}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

  Quantity :{quantity}
  Message :{msg}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")

    for _ in range(quantity):
        try:
        	args.subClient.send_message(args.chatId, msg)
        except:
        	pass
										
@client.command("chatid")
def chatid(data):
	data.subClient.send_message(data.chatId,message=f"{data.chatId}",replyTo=data.messageId)
@client.command("searchuser",condition=is_black)
def searchuser(data):
	msg=data.message.split(" ")
	code1=msg[0]
	code2=msg[1]
	user=(client.get_from_code(code1).objectId)
	cd=(client.get_from_code(code2))
	cid=cd.path[1:cd.path.index("/")]
	try:
		ui=client.get_from_id(objectType=0,objectId=user,comId=cid).json
		lin=ui["extensions"]["linkInfo"]["shareURLShortCode"]
		data.subClient.send_message(data.chatId,message=f"""[cu]Alexa got user profile

Link : {lin}

""",embedTitle="Profile link",embedLink=f"{lin}",embedContent="Click here to reach user")
	except:
		data.subClient.send_message(data.chatId,message="User not available in that community",replyTo=data.messageId)
		pass
		
@client.command("chatids")
def chat_id(args):
    if client.check(args,'staff', 'admin'):
        val = args.subClient.get_chats()
        for title, chat_id in zip(val.title, val.chatId):
        	args.subClient.send_message(args.chatId, f"{title} | {chat_id}")

@client.command("global", condition=is_black)
def globall(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
	   h=data.subClient.get_user_info(userId=str(user)).nickname
	   AID=client.get_user_info(userId=str(user)).aminoId
	   data.subClient.send_message(data.chatId,message="https://aminoapps.com/u/"+str(AID),embedTitle="Global Id",embedContent=f"{h}")

@client.command("leaveamino")
def leave_amino(args):
	if client.check(args,'admin'):
		args.subClient.send_message(args.chatId, "Leaving the amino!")
		for i in range(5):
			try:
				args.subClient.leave_community(args.comId)
			except:
				pass
		args.subClient.send_message(args.chatId,message="Left community")
		del client[args.subClient.community_id]

@client.command("deljson")
def deljson(data):
	del client[args.subClient.community_id]
	data.subClient.send_message(data.chatId,message="File deleted")	

def telecharger(url):
    music = None
    if ("=" in url and "/" in url and " " not in url) or ("/" in url and " " not in url):
        if "=" in url and "/" in url:
            music = url.rsplit("=", 1)[-1]
        elif "/" in url:
            music = url.rsplit("/")[-1]

        if music in os.listdir(path_download):
            return music

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            'extract-audio': True,
            'outtmpl': f"{path_download}/{music}.webm",
            }

        with YoutubeDL(ydl_opts) as ydl:
            video_length = ydl.extract_info(url, download=True).get('duration')
            ydl.cache.remove()

        url = music+".mp3"

        return url, video_length
    return False, False


def decoupe(musical, temps):
    size = 170
    with open(musical, "rb") as fichier:
        nombre_ligne = len(fichier.readlines())

    if temps < 180 or temps > 540:
        return False

    decoupage = int(size*nombre_ligne / temps)

    t = 0
    file_list = []
    for a in range(0, nombre_ligne, decoupage):
        b = a + decoupage
        if b >= nombre_ligne:
            b = nombre_ligne

        with open(musical, "rb") as fichier:
            lignes = fichier.readlines()[a:b]

        with open(musical.replace(".mp3", "PART"+str(t)+".mp3"),  "wb") as mus:
            for ligne in lignes:
                mus.write(ligne)

        file_list.append(musical.replace(".mp3", "PART"+str(t)+".mp3"))
        t += 1
    return file_list

lgh=[]
def download_audio(video_url):
    music = None
    if ("=" in video_url and "/" in video_url and " " not in video_url) or ("/" in video_url and " " not in video_url):
        if "=" in video_url and "/" in video_url:
            music = video_url.rsplit("=", 1)[-1]
        elif "/" in video_url:
            music = video_url.rsplit("/")[-1]

        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(output_path="audio/")

        mp3_file_path = "mymus" + ".mp3"
        os.rename(audio_file_path, mp3_file_path) 
        length=yt.length
        lgh.append(length)
        #subprocess.run(["ffmpeg", "-i", audio_file_path, "-vn", "-acodec", "libmp3lame", mp3_file_path])
        
        return "done"

def dowoad_audio(video_url):
    music = None
    if ("=" in video_url and "/" in video_url and " " not in video_url) or ("/" in video_url and " " not in video_url):
        if "=" in video_url and "/" in video_url:
            music = video_url.rsplit("=", 1)[-1]
        elif "/" in video_url:
            music = video_url.rsplit("/")[-1]

        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(output_path="audio/")

        mp3_file_path = audio_file_path.split(".")[0] + ".mp3"
        subprocess.run(["ffmpeg", "-i", audio_file_path, "-vn", "-acodec", "libmp3lame", mp3_file_path])
        
        return "done"

def search_internet_music(music_name):
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return download_audio(clip2)

@client.command("plnnay", condition=is_black)
def pnnlay(data):
    data.subClient.send_message(data.chatId,message=f"""
[c]Downloading
[c]{data.message}
[cb]⇆ㅤ ||◁ㅤ❚❚ㅤ▷||ㅤ ↻
""")
    video_url = data.message
    if video_url.startswith(("https://", "http://")):
    	download_audio(video_url)
    else:
    	search_internet_music(video_url)
    fp=open('mymus.mp3', 'rb')
    data.subClient.send_message(data.chatId, file=fp, fileType="audio")
    os.remove("mymus.mp3")
    
@client.command("play", condition=is_black)
def play(args):
    args.subClient.send_message(args.chatId,message=f"""
[c]Downloading
[c]{args.message}
[bc]⇆ㅤ ||◁ㅤ❚❚ㅤ▷||ㅤ ↻
""")
    video_url = args.message
    if video_url.startswith(("https://", "http://")):
    	download_audio(video_url)
    else:
    	search_internet_music(video_url)
    music="mymus.mp3"
    for lent in lgh:
    	size=lent  
    if music:
        music = "mymus.mp3"
        val = decoupe(music, size)

        if not val:
            try:
                with open(music, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            except Exception:
                args.subClient.send_message(args.chatId, "Error! File too heavy (9 min max)")
            os.remove(music)
            return

        os.remove(music)
        for elem in val:
            with suppress(Exception):
                with open(elem, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            os.remove(elem)
        return
    args.subClient.send_message(args.chatId, "Song not found")


def stop(args):
    if client.check(args, 'admin'):
        args.subClient.send_message(args.chatId, "Stopping Bot")
        os.execv(sys.executable, ["None", "None"])



@client.command("truth", condition=is_black)
def truth(args):
  lis = ['[bi]What’s the last lie you told?',
'[bi]What was the most embarrassing thing you’ve ever done on a date?',
'[bi]Have you ever accidentally hit something (or someone!) with your car?',
'[bi]Name someone you’ve pretended to like but actually couldn’t stand.',
'[bi]What’s your most bizarre nickname?',
'[bi]What’s been your most physically painful experience?',
'[bi]What bridges are you glad that you burned?',
'[bi]What’s the craziest thing you’ve done on public transportation?',
'[bi]If you met a genie, what would your three wishes be?',
'[bi]If you could write anyone on Earth in for President of the United States, who would it be and why?',
'[bi]What’s the meanest thing you’ve ever said to someone else?',
'[bi]Who was your worst kiss ever?',
'[bi]What’s one thing you’d do if you knew there no consequences?',
'[bi]What’s the craziest thing you’ve done in front of a mirror?',
'[bi]What’s the meanest thing you’ve ever said about someone else?',
'[bi]What’s something you love to do with your friends that you’d never do in front of your partner?',
'[bi]Who are you most jealous of?',
'[bi]What do your favorite pajamas look like?',
'[bi]Have you ever faked sick to get out of a party?',
'[bi]Who’s the oldest person you’ve dated?',
'[bi]How many selfies do you take a day?',
'[bi]How many times a week do you wear the same pants?',
'[bi]Would you date your high school crush today?',
'[bi]Do you believe in any superstitions? If so, which ones?',
'[bi]What’s one movie you’re embarrassed to admit you enjoy?',
'[bi]What’s your most embarrassing grooming habit?',
'[bi]When’s the last time you apologized? What for?',
'[bi]How do you really feel about the Twilight saga?',
'[bi]Where do most of your embarrassing odors come from?',
'[bi]Have you ever considered cheating on a partner?',
'[bi]Have you ever cheated on a partner?',
'[bi]Have you ever peed in a pool?',
'[bi]What’s the weirdest place you’ve ever grown hair?',
'[bi]If you were guaranteed to never get caught, who on Earth would you murder?',
'[bi]What’s the cheapest gift you’ve ever gotten for someone else?',
'[bi]What app do you waste the most time on?',
'[bi]What’s the weirdest thing you’ve done on a plane?',
'[bi]How many gossip blogs do you read a day?',
'[bi]What is the youngest age partner you’d date?',
'[bi]Have you ever picked your nose in public?',
'[bi]Have you ever lied about your age?',
'[bi]If you had to delete one app from your phone, which one would it be?',
'[bi]What’s your most embarrassing late night purchase?',
'[bi]What’s the longest you’ve gone without showering?',
'[bi]Have you ever used a fake ID?',
'[bi]Who’s your hall pass?',
'[bi]Be honest: Do you have a favorite child?',
'[bi]Which of your family members annoys you the most and why?',
'[bi]What is your greatest fear in a relationship?',
'[bi]What’s your biggest pet peeve about the person to your left?',
'[bi]What’s the most embarrassing text in your phone right now?',
'[bi]Have you ever seen a dead body?',
'[bi]What celebrity do you think is overrated?',
'[bi]Have you ever lied to your boss?',
'[bi]Have you ever stolen something from work?',
'[bi]What’s the longest you’ve gone without brushing your teeth?',
'[bi]What’s your biggest regret in life?',
'[bi]Describe the weirdest thing you’ve ever done while inebriated.',
'[bi]Have you ever regifted a present?',
'[bi]Would you break up with your partner for $1 million?',
'[bi]Have you ever had a crush on a coworker?',
'[bi]Do you still have feelings for any of your exes?',
'[bi]What’s the smallest tip you’ve ever left at a restaurant?',
'[bi]Have you ever regretted something you did to get a crush or partner’s attention?',
'[bi]What’s one job you could never do?',
'[bi]Have you ever ghosted a friend?',
'[bi]Have you ever ghosted a partner?',
'[bi]What’s the most scandalous photo in your cloud?',
'[bi]If you switched genders for a day, what would you do?',
'[bi]How many photo editing apps do you have on your phone?',
'[bi]What’s the most childish thing you still do?',
'[bi]When’s the last time you dumped someone?',
'[bi]Would you date someone shorter than you?',
'[bi]Have you ever lied for a friend?',
'[bi]Name one thing you’d change about every person in this room.',
'[bi]When’s the last time you made someone else cry?',
'[bi]What’s the most embarrassing thing you’ve done in front of a crowd?',
'[bi]If you could become invisible, what’s the worst thing you’d do?',
'[bi]After you’ve dropped a piece of food, what’s the longest time you’ve left it on the floor before eating it?',
'[bi]What’s one thing in your life you wish you could change?',
'[bi]If you could date two people at once, would you do it? If so, who?',
'[bi]What’s something that overwhelms you?',
'[bi]What was the greatest day of your life?',
'[bi]What’s one useless skill you’d love to learn anyway?',
'[bi]If I went through your cabinets, what’s the weirdest thing I’d find?',
'[bi]What’s the worst thing you’ve ever done at work?',
'[bi]How many people have you kissed?',
'[bi]Have you ever gotten mad at a friend for posting an unflattering picture of you?',
'[bi]Who in this room would you list as your emergency contact?',
'[bi]What’s something you would die if your mom found out about?',
'[bi]What’s the scariest thing that’s ever happened to you?',
'[bi]If you could set anyone here up with your best friend, who would it be and why?',
'[bi]Who was your first love?',
'[bi]What’s the last purchase you regretted?',
'[bi]Have you ever sent a sext to the wrong person? Who?',
'[bi]What’s the weirdest dream you’ve ever had?',
'[bi]Are you scared of getting old?',
'[bi]What’s the last movie that made you cry?',
'[bi]List one positive and one negative thing about everyone online now.',
'[bi]When’s the last time you cried and why?',
'[bi]What’s your favorite possession?',
'[bi]Who in this group chat would you want to swap lives with for a week?',
'[bi]What was your biggest fear as a child?',
'[bi]What’s your biggest fear today?',
'[bi]What’s the most embarrassing thing your parents have caught you doing?',
'[bi]Name a band you only pretend to like.',
'[bi]What’s the last song that made you cry?',
'[bi]Have you ever had a wardrobe malfunction?',
'[bi]What’s the last thing you Googled?'
'[bi]What is that one thing you would never do for all the money in the world?',
'[bi]Who is your favorite person in your immediate family?',
'[bi]If you could only hear one song for the rest of your life, what would it be?',
'[bi]When’s the last time your partner embarrassed you?',
'[bi]What’s the last YouTube video you watched?',
'[bi]Who in this chat would be your one phone call if you were in jail?',
'[bi]What’s the craziest thing you’ve ever done in a movie theater?',
'[bi]What’s the craziest thing that has happened to you in a mall?',
'[bi]How long was your longest relationship?',
'[bi]What’s your biggest insecurity?',
'[bi]Have you ever been arrested?',
'[bi]Who’s the most surprising person to ever slide into your DMs?',
'[bi]Where’s one place you’re dying to visit?',
'[bi]What word do you hate the most?',
'[bi]What’s the most embarrassing thing you’ve ever posted on social media?',
'[bi]Have you ever kept a library book? For how long?',
'[bi]If you could hire someone to do one thing for you, what would it be?',
'[bi]Have you ever lied on your resume?',
'[bi]What’s the best lie you’ve ever told anyone?',
'[bi]Who’s the last person you lurked on social media?',
'[bi]What’s your most embarrassing childhood memory?',
'[bi]Have you ever pretended to not get a text to get out of doing something?',
'[bi]What’s the weirdest thing you’ve ever done in a class?',
'[bi]What’s the most insane thing you’ve done to get out of a speeding ticket?',
'[bi]Do you have any hidden talents? What are they?',
'[bi]When’s the last time you got caught in a lie?',
'[bi]What do you think happens when you die?',
'[bi]When’s the last time you watched an adult movie?',
'[bi]Have you ever been in a fight?',
'[bi]Would you marry someone rich even if you weren’t in love with them?',
'[bi]Have you ever been caught checking someone out?',
'[bi]What’s the worst advice you’ve ever given someone else?',
'[bi]What’s the worst advice someone else has ever given you?',
'[bi]Is there an ex with whom you’d consider reconciling?',
'[bi]What’s the weirdest thing you do while driving?',
'[bi]Who’s the last person who called you?',
'[bi]When’s the last time you wanted to hit somebody?',
'[bi]What’s the biggest prank you’ve ever played on someone?',
'[bi]What’s one thing about your partner that you find least attractive?',
'[bi]When was the last time you were really angry? Why?',
'[bi]What’s your least favorite memory from college?',
'[bi]What’s the grossest thing that you do alone?',
'[bi]What’s your favorite guilty pleasure song?',
'[bi]Would you ever get plastic surgery?',
'[bi]Have you ever had a near-death experience?',
'[bi]What’s a skill you wish you had?',
'[bi]Have you ever compromised your morals for money? How?',
'[bi]Who was the last person you said, “I love you” to?',
'[bi]What was your first heartbreak?',
'[bi]Have you ever broken someone’s heart?',
'[bi]What’s the most bogus rumor you’ve ever heard about yourself?',
'[bi]What’s the most bogus rumor you’ve ever spread or heard about someone else?',
'[bi]When and where was your first kiss? Who was it with?',
'[bi]Do you think cheating can ever be justified? How?',
'[bi]Have you ever thrown up in public?',
'[bi]When’s the last time you got rejected?',
'[bi]What’s the most common misconception about you?',
'[bi]Have you ever seriously injured another person?',
'[bi]When did you stop believing in Santa Claus?',
'[bi]What’s one responsibility you wish you didn’t have?',
'[bi]What’s the scariest thing you’ve ever done?',
'[bi]Have you ever had a paranormal experience?',
'[bi]Do you believe in aliens?',
'[bi]What’s the pettiest thing you’ve ever done?',
'[bi]What’s something you’ve done that you still feel guilty about?',
'[bi]What is the worst date you’ve ever been on?',
'[bi]Do you secretly dislike any of your friends’ kids?',
'[bi]What’s the weirdest thing you’ve ever collected?',
'[bi]What’s the weirdest thing you’ve ever said to a stranger?',
'[bi]Who in this room do you trust the least?',
'[bi]What’s the most inappropriate time you’ve ever laughed?',
'[bi]What’s your best pickup line?',
'[bi]What’s your sleaziest pickup line?',
'[bi]What’s the weirdest place you’ve ever given or gotten someone’s number?',
'[bi]What’s the dumbest thing you’ve ever lied about?',
'[bi]Have you ever said, “I love you” and not really meant it? To whom?',
'[bi]What’s your least favorite memory from high school?',
'[bi]What’s the worst present someone has ever given you?',
'[bi]When’s the last time you shared a toothbrush with someone else?',
'[bi]Have you ever had a crush on a boss or teacher?',
'[bi]What’s the worst present you’ve ever given someone else?',
'[bi]What song do you sing most in the shower?',
'[bi]Who’s the person you most regret hooking up with?',
'[bi]What’s something you’re embarrassed that you’re good at?',
'[bi]What was your most humbling moment?',
'[bi]Who would you bring with you on a deserted island?',
'[bi]What’s the worst decision one of the other players has ever made?',
'[bi]Have you ever been fired from a job?',
'[bi]Have you ever let someone take the blame for something you did?',
'[bi]What’s the most ridiculous thing you have an emotional attachment to?',
'[bi]What’s something you’ve done that you’d judge someone else for doing?',
'[bi]Who’s your hero?',
'[bi]What’s something you know you need to do but aren’t looking forward to at all?',
'[bi]What’s the biggest secret you’ve kept from your parents?',
'[bi]What’s the most offensive joke you’ve found funny?',
'[bi]What are you most proud of in your life?',
'[bi]If you were rescuing people from a burning building and you had to leave one person behind from this room, who would it be?']
  args.subClient.send_message(args.chatId, message=str(random.choice(lis)),replyTo=args.messageId)
  
@client.command("dare", condition=is_black)
def dare(args):
  lis = ['[bi]Sing and dance in the street like crazy.',
'[bi]Become the slave of another player of your choosing for 5 mins.',
'[bi]Embrace the first passing through the street.',
'[bi]Dance with a broom or mop.',
'[bi]Briefly walk like a lady in high heels.',
'[bi]Climb to sing in the bar of a bar.',
'[bi]Declare who is your true love.',
'[bi]Tell something very intimate.',
'[bi]Sing the alphabet without moving your mouth.',
'[bi]Do your best president impression.',
'[bi]Yell out the first word that comes to your mind right now.',
'[bi]Call the pizza place and order 300 sardine pizzas.',
'[bi]Once you have your eyes closed, feel someone’s face and guess who they are.',
'[bi]Make up a story about the item to your right.',
'[bi]Sing everything you say for the next 10 minutes.',
'[bi]Give a foot massage to someone present.',
'[bi]Give the person to your left a hickey.',
'[bi]Say the alphabet backwards in 15 seconds.',
'[bi]Eat a raw egg.',
'[bi]Bark like a dog.',
'[bi]Sing a song all the way through to the end.',
'[bi]Dance wildly to your favourite song']
  args.subClient.send_message(args.chatId, message=str(random.choice(lis)),replyTo=args.messageId)

 
@client.command("remoji", condition=is_black)
def remoji(args):
	lis = ['😰😨😱😓🤯', '??????🤕??', '🌝🥸👻🎃', '😺👹😈😇💩', '😛😉😊😘🥳', '🤣😀😆🥰🙂', '☺️😑🙃😶🤗', '🤩😋😔😌☺️', '🤫🤐🥺🙄🤔', '🧐😤😠😳🤯', '😓😥😩😖😵', '🌞🤮🤧🤒🎃', '😍😚🤭🥲😄', '😃😂🤣😭😰', '🤬😡😮😯😲', '🤓🤑🤠😇😷', '🥵🥶👺☠️👽', '😸😹😺😻😼', '😽🙀😿😾💀', '❤️🧡💛💚💙', '💜🤎🖤🤍♥️', '💘💝💖💗💓', '💞💕💌💟❣️', '💔💋👅👄👀', '🦾🦠🦷🏵️💐', '🧝🧙🧛🧟🥷', '😪😴🥱🤤🙄', '👿😈🔥⭐🌟', '🎊🎉🕳️💤💦', '🌜👻🤖💢⚡', '✨💫👁️🍂☀️', '🧠🫀🫁🩸🌡️', '👉👌🍺🍷👄', '🦁🐻🐼🐨🐹', '🐭🐷🐸🙉🐶', '🌌🌠🌉🌆🌃', '🕊️🦅🐦🦥🦏', '🐲🦖🐢🦮🐈', '🐐🦬🐖🐑🐆', '🦍🦧🐿️🦦🦈', '🐝🐠🐋🦋🐜', '🍔🍖🍗🌭🥪', '🥞🍳🫓🌮🍕', '🍉🍓🍒🫐🍎', '🧆🥙🥘🍜🦪', '🍧🍱🥟🍚🍢', '🍰🍙🍡🍣🍟', '🧇🥯🌯🥟🥡', '🍭🍩🍪🥮🍨', '🥗🍲🫕🍥🍿', '🥃🍾🍹🍸🍻', '🅿️🅾️🆘ℹ️🖕🏿', '🤏✋👊🙌👇', '👾🕹️🎮🎲🃏', '💵💴💶💷💰', '🇺🇸🇹🇨🇸🇻🇺🇦🇼🇸', '🏤🏣🏨🏥🏩']
	args.subClient.send_message(args.chatId, message=str(random.choice(lis)))
	

@client.command("profile", condition=is_black)
def profile(data):
    if data.message:
    	user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    else:
    	user=data.authorId
    	
    x=data.subClient.get_user_info(userId=client.userId).json["role"]
    
    ic=data.subClient.get_user_info(str(user)).icon
    response=requests.get(f"{ic}")
    file=open(".yays.png","wb")
    file.write(response.content)
    file.close()
    imgg=(".yays.png")
    Image.open(imgg).resize((800,800)).save("prof.png")
    ff=open("prof.png","rb")
    repa= data.subClient.get_user_info(userId=str(user)).reputation
    h=data.subClient.get_user_info(userId=str(user)).nickname
    lvl = data.subClient.get_user_info(userId=str(user)).level
    crttime = data.subClient.get_user_info(userId=str(user)).createdTime
    followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
    commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
    posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
    if x==100:
    	gstrk=data.subClient.get_user_info(userId=str(user)).globalStrikeCount
    else:
    	gstrk="0"
    glob=client.get_user_info(userId=str(user)).aminoId
    vip =data.subClient.get_user_info(userId=str(user)).accountMembershipStatus
    if x==100:
    	wrn=data.subClient.get_user_info(userId=str(user)).warningCount
    	strk=data.subClient.get_user_info(userId=str(user)).strikeCount
    else:
    	wrn= "0"
    	strk= "0"
    bg=data.subClient.get_user_info(userId=str(user)).mediaList
    followed = data.subClient.get_user_info(userId=str(user)).followingCount
    if vip==1:
    	vips="Active"
    else:
    	vips="Not Active"
    if bg ==None:
    	bgs="No Image"
    else:
    	bgs=bg[0][1]
    msg=f"""[cu]{h}'s ᴘʀᴏғɪʟᴇ

• ɴᴀᴍᴇ - {h}
• ʟᴇᴠᴇʟ - {lvl}
• ʀᴇᴘs - {repa}
• ғᴏʟʟᴏᴡᴇʀs - {followers}
• ғᴏʟʟᴏᴡᴇᴅ - {followed}
• ᴡᴀʟʟ ᴄᴏᴍᴍᴇɴᴛs - {commentz}
• ᴘᴏsᴛs - {posts}
• sᴛʀɪᴋᴇ - {strk}
• ɢʟᴏʙᴀʟ sᴛʀɪᴋᴇ - {gstrk}
• ᴡᴀʀɴɪɴɢ - {wrn}
• ᴀᴍɪɴᴏᴘʟᴜs - {vips}
• ɢʟᴏʙᴀʟɪᴅ - {glob}
• ɪᴅ ᴄʀᴇᴀᴛᴇᴅ - {crttime}
• ᴍᴏᴅɪғɪᴇᴅ - {profilchange}
• ᴜsᴇʀɪᴅ - {str(user)}
• ɪᴄᴏɴ
{ic}
• ʙᴀᴄᴋɢʀᴏᴜɴᴅ
{bgs}

"""
    embdfull(data,user)
    ftf=open("neeee.png","rb")
    data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{user}",ftf,msg,data.chatId)
    pag="fame"
    shutil.rmtree(pag)    
    #data.subClient.send_message(chatId=data.chatId,message=msg,embedTitle=f"{h}",embedLink=f"ndc://x{data.comId}/user-profile/{user}",embedContent="Profile Link",embedImage=ff)	
@client.command("pile", condition=is_black)
def pile(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention:
		for user in mention:
			ic=data.subClient.get_user_info(str(user)).icon
			response=requests.get(f"{ic}")
			file=open(".yays.png","wb")
			file.write(response.content)
			file.close()
			imgg=(".yays.png")
			Image.open(imgg).resize((800,300)).save("prof.png")
			ff=open("prof.png","rb")
			repa= data.subClient.get_user_info(userId=str(user)).reputation
			h=data.subClient.get_user_info(userId=str(user)).nickname
			lvl = data.subClient.get_user_info(userId=str(user)).level
			crttime = data.subClient.get_user_info(userId=str(user)).createdTime
			followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
			profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
			commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
			posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
			followed = data.subClient.get_user_info(userId=str(user)).followingCount
			msgg=f"""[cu]𝗨𝗦𝗘𝗥 𝗜𝗡𝗙𝗢

• NAME: {h}
• USERID: {str(user)}
• CREATED ON: {crttime}
• PROFILE CHANGED: {profilchange}
• REPUTATION: {repa}
• LEVEL: {lvl}
• POSTS: {posts}
• WALL COMMENTS: {commentz}
• FOLLOWING: {followed}
• FOLLOWERS: {followers}"""
			data.subClient.full_embed("ndc://x{data.comId}/user-profile/{str(user)}",ff,msgg,data.chatId)
	else:
		ic=data.subClient.get_user_info(data.authorId).icon
		response=requests.get(f"{ic}")
		file=open(".yayis.png","wb")
		file.write(response.content)
		file.close()
		imgu=(".yayis.png")
		Image.open(imgu).resize((800,300)).save("profi.png")
		fif=open("profi.png","rb")
		repa= data.subClient.get_user_info(userId=data.authorId).reputation
		h=data.subClient.get_user_info(userId=data.authorId).nickname
		lvl = data.subClient.get_user_info(userId=data.authorId).level
		crttime = data.subClient.get_user_info(userId=data.authorId).createdTime
		followers = data.subClient.get_user_achievements(userId=data.authorId).numberOfFollowersCount
		profilchange = data.subClient.get_user_info(userId=data.authorId).modifiedTime
		commentz = data.subClient.get_user_info(userId=data.authorId).commentsCount
		posts = data.subClient.get_user_achievements(userId=data.authorId).numberOfPostsCreated
		followed = data.subClient.get_user_info(userId=data.authorId).followingCount
		msg=f"""
[C]PROFILE INFO
[C]┅┅┅┅┅┅┅┅┅┅┅┅┅┅

• NAME: {h}
• USERID: {data.authorId}
• CREATED ON: {crttime}
• PROFILE CHANGED: {profilchange}
• REPUTATION: {repa}
• LEVEL: {lvl}
• POSTS: {posts}
• WALL COMMENTS: {commentz}
• FOLLOWING: {followed}
• FOLLOWERS: {followers}"""
		data.subClient.full_embed("ndc://x{data.comId}/user-profile/{data.authorId}",fif,msg,data.chatId)

@client.command("userid", condition=is_black)
def userid(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention!=None:
		for user in mention:
			data.subClient.send_message(data.chatId,message=user,replyTo=data.messageId)
	else:
		data.subClient.send_message(data.chatId,message=data.authorId,replyTo=data.messageId)		

@client.command("delm")
def delm(args):
  #mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
  if client.check(args,"staff","admin"):
  	data = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
  	reply_message = data.json['extensions']
  	if reply_message:
  	 reply_message = data.json['extensions']['replyMessage']['content']
  	 reply_messageId = data.json['extensions']['replyMessage']['messageId']
  	 x=args.subClient.get_user_info(userId=client.userId).json["role"]
  	 if x!=0:
  	 	args.subClient.delete_message(args.chatId, reply_messageId,asStaff=True,reason="Deleted by admin")
  	 	args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Deleted by admin")
  	 else:
  	 	try:
  	 		args.subClient.delete_message(args.chatId, reply_messageId,asStaff=False,reason="Deleted by admin")
  	 		args.subClient.delete_message(args.chatId, args.messageId,asStaff=False,reason="Deleted by admin")
  	 		
  	 	except:
  	 		args.subClient.send_message(args.chatId,message="I don't have cohost",replyTo=args.messageId)
  	 		
  	 		pass
  else:
  	 args.subClient.send_message(args.chatId,message="Admin/Staff command",replyTo=args.messageId)

@client.command("cidlist")
def cidlist(data):
	val=""
	if client.check(data,"admin"):
		t = open('comid.txt','r')
		lists=[]
		lis=[]
		for m in t.read().splitlines():
			temp=m
			if temp not in lists:
			     lists.append(int(temp))
		for i, vl in enumerate(lists,1):
			val +=str(vl) +"\n"
		data.subClient.send_message(message=f"""[C]
{val}
""",chatId=data.chatId)
	else:
		data.subClient.send_message(message="Admin Command"
,chatId=data.chatId,replyTo=data.messageId)

@client.command("delmongo", condition=is_staff)
def delmongo(data):
#	if client.check(data,"admin"):
		test_1.delete_many({})
		data.subClient.send_message("Deleted comid list",data.chatId,replyTo=data.messageId)
	#else:
	#	data.subClient.send_message("Admin Command",data.chatId,replyTo=data.messageId)	

@client.command("stopamino")
def stop_amino(args):
    if client.check(args,'admin'):
        args.subClient.stop_instance()
        del client[args.subClient.community_id]

def kund(data,user):	
	if data:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			nick=data.subClient.get_user_info(user).nickname
			vip=data.subClient.get_user_info(user).influencerInfo
			plus=data.subClient.get_user_info(user).accountMembershipStatus
			following=data.subClient.get_user_info(user).followingCount
			followers=data.subClient.get_user_info(user).followersCount
			lvll=data.subClient.get_user_info(user).level
			repa= data.subClient.get_user_info(userId=str(user)).reputation
			frm=data.subClient.get_user_info(user).avatarFrame
			glob=client.get_user_info(userId=str(user)).aminoId
			aiv=data.subClient.get_user_info(user).avatarFrameId
			rolee=data.subClient.get_user_info(user).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(user).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("kund.png").convert("RGB").resize((800,400))
			bg=Image.open("res.png").resize((800,800))
			if frm!=None and aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7":
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
				pty="fame"
				isdir = os.path.isdir(pty)
				if isdir==True or aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7" or aiv!=None:
					fg=Image.open("fame/frame.png").resize((860,860))
					bg.paste(fg,(-25,-25),fg)
					bg.save("new.png")
					fhg="new.png"
				elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
				else:
					fhg="res.png"
			elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((120,120))
			a=["105","585"]
			ii=int(random.choice(a))
			bgg.paste(j,(ii,140),j)
			bgg.save("kunda.png")

def adharr(data,user):	
	if data:
			tlt=data.subClient.get_chat_thread(data.chatId).title
			img3=open(".tvs.png","rb")
			nick=data.subClient.get_user_info(user).nickname
			vip=data.subClient.get_user_info(user).influencerInfo
			plus=data.subClient.get_user_info(user).accountMembershipStatus
			following=data.subClient.get_user_info(user).followingCount
			followers=data.subClient.get_user_info(user).followersCount
			lvll=data.subClient.get_user_info(user).level
			repa= data.subClient.get_user_info(userId=str(user)).reputation
			frm=data.subClient.get_user_info(user).avatarFrame
			glob=client.get_user_info(userId=str(user)).aminoId
			aiv=data.subClient.get_user_info(user).avatarFrameId
			rolee=data.subClient.get_user_info(user).role
		#	img2=open(".wel.png","rb")
			x=data.subClient.get_user_info(user).icon
			response=requests.get(f"{x}")
			file=open(".sampl9e.png","wb")
			file.write(response.content)
			file.close()
			img = Image.open(".sampl9e.png")
			
			height,width = img.size 
			lum_img = Image.new('L', [height,width] , 0)
			draw = ImageDraw.Draw(lum_img)
			draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
			img_arr =np.array(img)
			lum_img_arr =np.array(lum_img) 
			final_img_arr = np.dstack((img_arr,lum_img_arr)) 
			(Image.fromarray(final_img_arr)).save("res.png")
			bgg=Image.open("adhar.png").resize((800,500))
			bg=Image.open("res.png").resize((800,800))
			if frm!=None and aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7":
				E=(frm["resourceUrl"])
				rq=requests.get(E)
				zip=open("frmes.zip","wb")
				zip.write(rq.content)
				zipi=ZipFile("frmes.zip","r")
				zipi.extractall("fame")
				pt=os.listdir('fame')
				if "frame.webp" in pt:
					web=Image.open("fame/frame.webp")
					web.save("fame/frame.png")
				pty="fame"
				isdir = os.path.isdir(pty)
				if isdir==True or aiv!="04f6fbf2-85a3-45c0-bdae-cd02057617e7" or aiv!=None:
					fg=Image.open("fame/frame.png").resize((860,860))
					bg.paste(fg,(-25,-25),fg)
					bg.save("new.png")
					fhg="new.png"
				elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
				else:
					fhg="res.png"
			elif plus==1 and frm==None:
					fg=Image.open("aplus.png").resize((1100,1100))
					bg.paste(fg,(-170,-170),fg)
					bg.save("aps.png")
					fhg="aps.png"
			else:
				fhg="res.png"
				
			j=Image.open(fhg).resize((180,180))
			k=Image.open("vip.png").resize((50,50))
			l=Image.open("plus.png").resize((70,70))
			if rolee==100 or rolee==102:
				bdg=Image.open("leader.png").resize((150,50))
			elif rolee==101:
				bdg=Image.open("curator.png").resize((150,50))
			else:
				bdg=Image.open("member.png").resize((150,50))
			lv=Image.open(f"level/{lvll}.png").resize((50,50))
			bgg.paste(j,(30,200),j)
			if vip!=None:
				bgg.paste(k,(470,165),k)
			bgg.paste(lv,(550,166),lv)
			if plus==1:
				bgg.paste(l,(390,160),l)
			bgg.paste(bdg,(240,170),bdg)
			draw = ImageDraw.Draw(bgg)
			title_fot = ImageFont.truetype('arial.ttf', 35)
			title_fo= ImageFont.truetype('fonts/unifont-15.0.01.ttf', 30)
			draw.text((248,230), text="NAME :", fill=(0,0,0), font=title_fot)
			draw.text((370,230), text=f"{nick}", fill=(0,0,0), font=title_fo)
			draw.text((248,280), text="REPS :", fill=(0,0,0), font=title_fot)
			draw.text((370,280), text=f"{repa}", fill=(0,0,0), font=title_fot)
			draw.text((248,330),text= f"{glob}", fill=(0,0,0), font=title_fot)
			#draw.text((395,335), text=f"{glob}", fill=(0,0,0), font=title_fo)
			#draw.text((248,380),text= f"{user}", fill=(0,0,0), font=title_fot)
			#draw.text((375,385), text=f"{user}", fill=(0,0,0), font=title_fo)
			bgg.save("neeee.png")

@client.command("kundali", condition=is_black)
def kundali(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    if "aminoapps.com" in data.message:
    	user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    elif mention!=None:
    	for x in mention:
    		user=x
    else:
    	user=data.authorId
    	
    x=data.subClient.get_user_info(userId=client.userId).json["role"]
    
    ic=data.subClient.get_user_info(str(user)).icon
    response=requests.get(f"{ic}")
    file=open(".yays.png","wb")
    file.write(response.content)
    file.close()
    imgg=(".yays.png")
    Image.open(imgg).resize((800,800)).save("prof.png")
    ff=open("prof.png","rb")
    repa= data.subClient.get_user_info(userId=str(user)).reputation
    h=data.subClient.get_user_info(userId=str(user)).nickname
    lvl = data.subClient.get_user_info(userId=str(user)).level
    crttime = client.get_user_info(userId=str(user)).createdTime
    followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
    commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
    posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
    if x==100:
    	gstrk=data.subClient.get_user_info(userId=str(user)).globalStrikeCount
    else:
    	gstrk="0"
    glob=client.get_user_info(userId=str(user)).aminoId
    vip =data.subClient.get_user_info(userId=str(user)).accountMembershipStatus
    if x==100:
    	wrn=data.subClient.get_user_info(userId=str(user)).warningCount
    	strk=data.subClient.get_user_info(userId=str(user)).strikeCount
    else:
    	wrn= "0"
    	strk= "0"
    bg=data.subClient.get_user_info(userId=str(user)).mediaList
    followed = data.subClient.get_user_info(userId=str(user)).followingCount
    if vip==1:
    	vips="Active"
    else:
    	vips="Not Active"
    if bg ==None:
    	bgs="No Image"
    else:
    	bgs=bg[0][1]
    msg=f"""[cu]{h}'s ᴋᴜɴᴅᴀʟɪ

• ɴᴀᴍᴇ - {h}
• ʟᴇᴠᴇʟ - {lvl}
• ʀᴇᴘs - {repa}
• ғᴏʟʟᴏᴡᴇʀs - {followers}
• ғᴏʟʟᴏᴡᴇᴅ - {followed}
• ᴡᴀʟʟ ᴄᴏᴍᴍᴇɴᴛs - {commentz}
• ᴘᴏsᴛs - {posts}
• sᴛʀɪᴋᴇ - {strk}
• ɢʟᴏʙᴀʟ sᴛʀɪᴋᴇ - {gstrk}
• ᴡᴀʀɴɪɴɢ - {wrn}
• ᴀᴍɪɴᴏᴘʟᴜs - {vips}
• ɢʟᴏʙᴀʟɪᴅ - {glob}
• ɪᴅ ᴄʀᴇᴀᴛᴇᴅ - {crttime}
• ᴍᴏᴅɪғɪᴇᴅ - {profilchange}
• ᴜsᴇʀɪᴅ - {str(user)}
• ɪᴄᴏɴ
{ic}
• ʙᴀᴄᴋɢʀᴏᴜɴᴅ
{bgs}

"""
    kund(data,user)
    ftf=open("kunda.png","rb")
    data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{user}",ftf,msg,data.chatId)
    os.remove("fame/frame.png")
    os.remove("fame/frame.webp")
    os.remove("config.json")
    #shutil.rmtree(pag)

@client.command("adhaarcard", condition=is_black)
def adhaarcard(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    if "aminoapps.com" in data.message:
    	user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    elif mention!=None:
    	for x in mention:
    		user=x
    	
    else:
    	user=data.authorId
    	
    x=data.subClient.get_user_info(userId=client.userId).json["role"]
    
    ic=data.subClient.get_user_info(str(user)).icon
    response=requests.get(f"{ic}")
    file=open(".yays.png","wb")
    file.write(response.content)
    file.close()
    imgg=(".yays.png")
    Image.open(imgg).resize((800,800)).save("prof.png")
    ff=open("prof.png","rb")
    repa= data.subClient.get_user_info(userId=str(user)).reputation
    h=data.subClient.get_user_info(userId=str(user)).nickname
    lvl = data.subClient.get_user_info(userId=str(user)).level
    crttime = client.get_user_info(userId=str(user)).createdTime
    followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
    commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
    posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
    if x==100:
    	gstrk=data.subClient.get_user_info(userId=str(user)).globalStrikeCount
    else:
    	gstrk="0"
    glob=client.get_user_info(userId=str(user)).aminoId
    vip =data.subClient.get_user_info(userId=str(user)).accountMembershipStatus
    if x==100:
    	wrn=data.subClient.get_user_info(userId=str(user)).warningCount
    	strk=data.subClient.get_user_info(userId=str(user)).strikeCount
    else:
    	wrn= "0"
    	strk= "0"
    bg=data.subClient.get_user_info(userId=str(user)).mediaList
    followed = data.subClient.get_user_info(userId=str(user)).followingCount
    if vip==1:
    	vips="Active"
    else:
    	vips="Not Active"
    if bg ==None:
    	bgs="No Image"
    else:
    	bgs=bg[0][1]
    msg=f"""[cu]{h}'s ᴀᴅʜᴀᴀʀᴄᴀʀᴅ

• ɴᴀᴍᴇ - {h}
• ʟᴇᴠᴇʟ - {lvl}
• ʀᴇᴘs - {repa}
• ғᴏʟʟᴏᴡᴇʀs - {followers}
• ғᴏʟʟᴏᴡᴇᴅ - {followed}
• ᴡᴀʟʟ ᴄᴏᴍᴍᴇɴᴛs - {commentz}
• ᴘᴏsᴛs - {posts}
• sᴛʀɪᴋᴇ - {strk}
• ɢʟᴏʙᴀʟ sᴛʀɪᴋᴇ - {gstrk}
• ᴡᴀʀɴɪɴɢ - {wrn}
• ᴀᴍɪɴᴏᴘʟᴜs - {vips}
• ɢʟᴏʙᴀʟɪᴅ - {glob}
• ɪᴅ ᴄʀᴇᴀᴛᴇᴅ - {crttime}
• ᴍᴏᴅɪғɪᴇᴅ - {profilchange}
• ᴜsᴇʀɪᴅ - {str(user)}
• ɪᴄᴏɴ
{ic}
• ʙᴀᴄᴋɢʀᴏᴜɴᴅ
{bgs}

"""
    adharr(data,user)
    ftf=open("neeee.png","rb")
    data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{user}",ftf,msg,data.chatId)
    os.remove("fame/frame.png")
    os.remove("fame/frame.webp")
    os.remove("config.json")
   # shutil.rmtree(pag)

@client.command("marry", condition=is_black)
def marry(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		nkn=data.subClient.get_user_info(str(user)).nickname
		h=data.subClient.get_user_info(str(user)).icon
		response=requests.get(f"{h}")
		file=open("girls.png","wb")
		file.write(response.content)
		file.close()
		x=data.subClient.get_user_info(data.authorId).icon
		resp=requests.get(f"{x}")
		file=open("boys.png","wb")
		file.write(resp.content)
		file.close()
		img=Image.open("boys.png")
		height,width = img.size 
		lum_img = Image.new('L', [height,width] , 0)
		draw = ImageDraw.Draw(lum_img)
		draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
		img_arr =np.array(img)
		lum_img_arr =np.array(lum_img) 
		final_img_arr = np.dstack((img_arr,lum_img_arr)) 
		(Image.fromarray(final_img_arr)).save("boy.png")
		imgg=Image.open("girls.png")
		height,width = imgg.size 
		lu_img = Image.new('L', [height,width] , 0)
		draw = ImageDraw.Draw(lu_img)
		draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
		img_arrr =np.array(imgg)
		lum_img_arrr =np.array(lu_img) 
		final_img_arrr = np.dstack((img_arrr,lum_img_arrr)) 
		(Image.fromarray(final_img_arrr)).save("girl.png")
		bgg=Image.open("shdi.png").resize((800,400))
		j=Image.open("boy.png").resize((100,100))
		k=Image.open("girl.png").resize((100,100))
		bgg.paste(j,(95,150),j)
		bgg.paste(k,(630,160),k)
		bgg.save("marry.png")
		msg=f"""[c]Congratulations 🎀
[c]💍 {data.author} married to {nkn} 💍

"""
		ftf=open("marry.png","rb")
		data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{user}",ftf,msg,data.chatId)


#@client.command("kundali", condition=is_black)
def kuli(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention:
		for user in mention:
			ic=data.subClient.get_user_info(str(user)).icon
			response=requests.get(f"{ic}")
			file=open(".yays.png","wb")
			file.write(response.content)
			file.close()
			imgg=(".yays.png")
			Image.open(imgg).resize((800,300)).save("prof.png")
			ff=open("prof.png","rb")
			repa= data.subClient.get_user_info(userId=str(user)).reputation
			h=data.subClient.get_user_info(userId=str(user)).nickname
			lvl = data.subClient.get_user_info(userId=str(user)).level
			crttime = client.get_user_info(userId=str(user)).createdTime
			followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
			profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
			commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
			posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
			followed = data.subClient.get_user_info(userId=str(user)).followingCount
			msgg=f"""
[C]PROFILE INFO
[C]┅┅┅┅┅┅┅┅┅┅┅┅┅┅

• NAME: {h}
• USERID: {str(user)}
• CREATED ON: {crttime}
• PROFILE CHANGED: {profilchange}
• REPUTATION: {repa}
• LEVEL: {lvl}
• POSTS: {posts}
• WALL COMMENTS: {commentz}
• FOLLOWING: {followed}
• FOLLOWERS: {followers}"""
			data.subClient.full_embed("ndc://x{data.comId}/user-profile/{str(user)}",ff,msgg,data.chatId)
	else:
		ic=data.subClient.get_user_info(data.authorId).icon
		response=requests.get(f"{ic}")
		file=open(".yayis.png","wb")
		file.write(response.content)
		file.close()
		imgu=(".yayis.png")
		Image.open(imgu).resize((800,300)).save("profi.png")
		fif=open("profi.png","rb")
		repa= data.subClient.get_user_info(userId=data.authorId).reputation
		h=data.subClient.get_user_info(userId=data.authorId).nickname
		lvl = data.subClient.get_user_info(userId=data.authorId).level
		crttime = client.get_user_info(userId=data.authorId).createdTime
		followers = data.subClient.get_user_achievements(userId=data.authorId).numberOfFollowersCount
		profilchange = data.subClient.get_user_info(userId=data.authorId).modifiedTime
		commentz = data.subClient.get_user_info(userId=data.authorId).commentsCount
		posts = data.subClient.get_user_achievements(userId=data.authorId).numberOfPostsCreated
		followed = data.subClient.get_user_info(userId=data.authorId).followingCount
		msg=f"""
[C]PROFILE INFO
[C]┅┅┅┅┅┅┅┅┅┅┅┅┅┅

• NAME: {h}
• USERID: {data.authorId}
• CREATED ON: {crttime}
• PROFILE CHANGED: {profilchange}
• REPUTATION: {repa}
• LEVEL: {lvl}
• POSTS: {posts}
• WALL COMMENTS: {commentz}
• FOLLOWING: {followed}
• FOLLOWERS: {followers}"""
		data.subClient.full_embed("ndc://x{data.comId}/user-profile/{data.authorId}",fif,msg,data.chatId)

@client.command("block", condition=is_black)
def block(args):
    if client.check(args,'staff','admin'):
    	mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
    	for user in mention:
        	if not client.is_it_admin(user):
        		args.subClient.add_favorite_users(str(user))
        		h=args.subClient.get_user_info(userId=str(user)).nickname
        		args.subClient.client.block(userId=str(user))
        		args.subClient.block(userId=str(user))
        		args.subClient.send_message(args.chatId, f"<$@{h}$> is blocked from using Bot!",mentionUserIds=[str(user)])
        		rebot()
        	else:
        		args.subClient.send_message(args.chatId,message="Can't block Admin", replyTo=args.messageId)
    else:
        args.subClient.send_message(args.chatId,message="Mod Command",messageId=args.messageId)
        


@client.command("unblock", condition=is_black)
def unblock(args):
    if client.check(args,'staff','admin'):
    	mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
    	for user in mention:
        	if not client.is_it_admin(user):
        		h=args.subClient.get_user_info(userId=str(user)).nickname
        		args.subClient.client.unblock(userId=str(user))
        		args.subClient.remove_favorite_users(str(user))
        		args.subClient.unblock(userId=str(user))
        		args.subClient.send_message(args.chatId, f"<$@{h}$> is unblocked from using Bot!",mentionUserIds=[str(user)])
        		rebot()
    else:
        args.subClient.send_message(args.chatId,message="Mod Command",messageId=args.messageId)
        
     #else:
     #	args.subClient.send_message(args.chatId,message="Mod Command",messageId=args.messageId)


@client.command("accept")
def accept(args):
    if client.check(args, 'staff','admin'):
        if args.subClient.accept_role( args.chatId):
            args.subClient.send_message(args.chatId, "Accepted role")
            return
        val = args.subClient.get_notices(start=0, size=25)
        for elem in val:
            print(elem["title"])
        ans = None
        res = None

        for elem in val:
            if 'become' in elem['title'] or "host" in elem['title']:
                res = elem['noticeId']
            if res:
                ans = args.subClient.accept_role(res)
            if ans:
                args.subClient.send_message(args.chatId, f"Accepted",replyTo=args.messageId)
                return
        else:
            args.subClient.send_message(args.chatId, "Give leader or Curator to accept")

@client.command()
def lang(data):
	data.subClient.send_message(data.chatId,message="""
English (Australia)
en   com.au
English (United Kingdom)
en   co.uk
English (United States)
en   com
English (Canada)
en   ca
English (India)
en   co.in
English (Ireland)
en   ie
English (South Africa)
en   co.za
French (Canada)
fr  ca
French (France)
fr   fr
Mandarin (China Mainland)
zh-CN   any
Mandarin (Taiwan)
zh-TW   any
Portuguese (Brazil)
pt  com.br
Portuguese (Portugal)
pt   pt
Spanish (Mexico)
es   com.mx
Spanish (Spain)
es   es
Spanish (United States)
es   com""")

@client.command("vice")
def vice(args):
			msg = args.message + " null null "
			msg = msg.split(" ")
			msg[3] = msg[2]
			msg[2] = msg[1]
			msg[1] = msg[0]
			audiofile = f"{path_download}/ttp{randint(1,500)}.mp3"
			gTTS(text=msg[1], lang=msg[2], tld=msg[3],slow=False).save(audiofile)
			try:
			         	with open(audiofile, 'rb') as fp:
			         		args.subClient.send_message(args.chatId, file=fp, fileType="audio")
			except Exception:
			 	args.subClient.send_message(args.chatId, "Too heavy!")
			 	os.remove(audiofile)

@client.command("say",condition=is_black)
def say(args):
    audio_file = f"{path_download}/tpp{randint(1,500)}.mp3"
    #langue = list(lang.tts_langs().keys())
    if not args.message:
        args.message = args.subClient.get_chat_messages(chatId=args.chatId, size=2).content[1]
    gTTS(text=args.message, lang='en', tld='co.in',slow=False).save(audio_file)
    try:
        with open(audio_file, 'rb') as fp:
            args.subClient.send_message(args.chatId, file=fp, fileType="audio")
    except Exception:
        args.subClient.send_message(args.chatId, "Too heavy!")
    os.remove(audio_file)

@client.command("voice",condition=is_black)
def voice(args):
    audio_file = f"{path_download}/tpp{randint(1,500)}.mp3"
    #langue = list(lang.tts_langs().keys())
    if not args.message:
        args.message = args.subClient.get_chat_messages(chatId=args.chatId, size=2).content[1]
    gTTS(text=args.message, lang='en', tld='co.in',slow=True).save(audio_file)
    try:
        with open(audio_file, 'rb') as fp:
            args.subClient.send_message(args.chatId, file=fp, fileType="audio")
    except Exception:
        args.subClient.send_message(args.chatId, "Too heavy!")
    os.remove(audio_file)
@client.command("ask")
def ask_thing(args):
    if client.check(args, 'staff', 'admin'):
        lvl = ""
        boolean = 1
        if "lvl=" in args.message:
            lvl = args.message.rsplit("lvl=", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl="+lvl, "").strip()
        elif "lvl<" in args.message:
            lvl = args.message.rsplit("lvl<", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl<"+lvl, "").strip()
            boolean = 2
        elif "lvl>" in args.message:
            lvl = args.message.rsplit("lvl>", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl>"+lvl, "").strip()
            boolean = 3
        try:
            lvl = int(lvl)
        except ValueError:
            lvl = 20

        args.subClient.ask_all_members(args.message+f"\n[CUI]This message was sent by {args.author}\n[CUI]I am Alexa and have a nice day^^", lvl, boolean)
        args.subClient.send_message(args.chatId, "sending...")
        args.subClient.send_message(args.chatId, "Announced successfully...",replyTo=args.messageId)


@client.command("askstaff")
def ask_staff(args):
    if client.check(args, 'admin'):
        amino_list = client.client.sub_clients()
        for commu in amino_list.comId:
            client[commu].ask_amino_staff(message=args.message)
        args.subClient.send_message(args.chatId, "Asking...")

@client.command("cmdlist")
def cmdlist(data):
	if client.check(data,'admin'):
		c=client.commands_list()
		o=""
		for z in c:
			o=o+str(z)+"\n"
		data.subClient.send_message(data.chatId,message=o)
			

@client.command()
def lockall(args):
	if client.check(args,'admin'):
		c=client.commands_list()
		for command in c:
			list = command.lower().strip().split()
		args.subClient.add_locked_command(list)
@client.command()
def unlockall(args):
	if client.check(args,'admin'):
		c=client.commands_list()
		for command in c:
			list = command.lower().strip().split()
		args.subClient.remove_locked_command(list)

@client.command("lock", condition=is_black)
def lock_command(args):
    if client.check(args, 'staff', 'admin'):
        if not args.message or args.message in args.subClient.locked_command or args.message in ("lock", "unlock"):
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.add_locked_command(ar)
        args.subClient.send_message(args.chatId, f"{args.message} command is locked now")
        rebot()


@client.command("unlock", condition=is_black)
def unlock_command(args):
    if client.check(args, 'staff', 'admin'):
        if args.message:
            try:
                ar = args.message.lower().strip().split()
            except Exception:
                ar = [ar.lower().strip()]
            args.subClient.remove_locked_command(ar)
            args.subClient.send_message(args.chatId, f"{args.message} command is unlocked now")
            rebot()


@client.command("lockedlist", condition=is_black)
def locked_command_list(args):
    val = ""
    if args.subClient.locked_command:
        for elem in args.subClient.locked_command:
            val +="◈" + elem+"\n"
    else:
        val = "No locked command"
    args.subClient.send_message(args.chatId, message=f"""
[c]Locked Commands
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{val}
[c]𐄁𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    #args.subClient.send_message(args.chatId, val)


@client.command()
def admihnc(args):
    if client.check(args, 'admin'):
        if not args.message or args.message == "alock":
            return

        command = args.subClient.admin_locked_command
        args.message = [args.message]

        if args.message[0] in command:
            args.subClient.remove_admin_locked_command(args.message)
        else:
            args.subClient.add_admin_locked_command(args.message)

        args.subClient.send_message(args.chatId, "Locked command list updated")


@client.command("allock")
def locked_admin_command_list(args):
    if client.check(args,'admin'):
        val = ""
        if args.subClient.admin_locked_command:
            for elem in args.subClient.admin_locked_command:
                val +="•" + elem+"\n"
        else:
            val = "No locked command"
        args.subClient.send_message(args.chatId, val)

	

@client.command("keepu")
def keep_favorite_users(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff', 'admin'):
        users = args.subClient.favorite_users
        try:
            val = args.subClient.get_user_id(args.message)
            user, userId = val[0], val[1]
        except Exception:
            args.subClient.send_message(args.chatId, "Error, user not found!")
            return
        if userId not in users:
            args.subClient.add_favorite_users(userId)
            args.subClient.send_message(args.chatId, f"Added {user} to favorite users")
            with suppress(Exception):
                args.subClient.favorite(time=1, userId=userId)
        return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("unkeepu")
def unkeep_favorite_users(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff', 'admin'):
        users = args.subClient.favorite_users
        try:
            val = args.subClient.get_user_id(args.message)
            user, userId = val[0], val[1]
        except Exception:
            args.subClient.send_message(args.chatId, "Error, user not found!")
            return
        if userId in users:
            args.subClient.remove_favorite_users(userId)
            args.subClient.send_message(args.chatId, f"Removed {user} to favorite users")
            with suppress(Exception):
                args.subClient.unfavorite(userId=userId)
        return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("keepc")
def keep_favorite_chats(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff', 'admin'):
        chats = args.subClient.favorite_chats
        with suppress(Exception):
            chat = args.subClient.get_from_code(f"{args.message}")
            if chat.objectId not in chats:
                args.subClient.add_favorite_chats(chat.objectId)
                args.subClient.send_message(args.chatId, "Added to favorite chats")
            return

        val = args.subClient.get_chats()

        for title, chatId in zip(val.title, val.chatId):
            if args.message == title and chatId not in chats:
                args.subClient.add_favorite_chats(chatId)
                args.subClient.send_message(args.chatId, f"Added {title} to favorite chats")
                with suppress(Exception):
                    args.subClient.favorite(time=1, chatId=args.chatId)
                return

        for title, chatId in zip(val.title, val.chatId):
            if args.message.lower() in title.lower() and chatId not in chats:
                args.subClient.add_favorite_chats(chatId)
                args.subClient.send_message(args.chatId, f"Added {title} to favorite chats")
                with suppress(Exception):
                    args.subClient.favorite(time=1, chatId=chatId)
                return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("unkeepc")
def unkeep_favorite_chats(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff', 'admin'):
        chats = args.subClient.favorite_chats

        with suppress(Exception):
            chat = args.subClient.get_from_code(f"{args.message}")
            if chat.objectId in chats:
                args.subClient.remove_favorite_chats(chat.objectId)
                args.subClient.send_message(args.chatId, "Removed to favorite chats")
            return

        val = args.subClient.get_chats()

        for title, chatid in zip(val.title, val.chatId):
            if args.message == title and chatid in chats:
                args.subClient.remove_favorite_chats(chatid)
                args.subClient.unfavorite(chatId=chatid)
                args.subClient.send_message(args.chatId, f"Removed {title} to favorite chats")
                return

        for title, chatid in zip(val.title, val.chatId):
            if args.message.lower() in title.lower() and chatid in chats:
                args.subClient.remove_favorite_chats(chatid)
                args.subClient.unfavorite(chatId=chatid)
                args.subClient.send_message(args.chatId, f"Removed {title} to favorite chats")
                return

    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")

@client.command("google",condition=is_black)
def google(args):
    msg = args.message.split(" ")
    msg = '+'.join(msg)
    args.subClient.send_message(chatId=args.chatId, message=f"https://www.google.com/search?q={msg}",replyTo=args.messageId)

 #For welcoming members on wall
#!wel (type ur welcome message)
@client.command("gcwel")
def gcwel(data):
	data.subClient.add_favorite_user(data.message)
	data.subClient.send_message(data.chatId,message=f"""
[C]GC Welcome changed

{data.message}
""")

   
@client.command("rgcwel")
def rgcwel(data):
	data.subClient.remove_favorite_user(data.message)
	data.subClient.send_message(data.chatId,message=f"""
[C]GC Welcome changed

{data.message}
""")   
@client.command("confession", condition=is_black)
def confession_channel(args):
    if client.check(args, 'staff','admin'):
        args.subClient.set_welcome_chat(args.chatId)
        args.subClient.send_message(args.chatId, "Confession GC set!")
        rebot()
    else:
    	args.subClient.send_message(args.chatId,message="Only Leader or Curator can set Confession GC")


@client.command("unconfession", condition=is_black)
def unwelcome_channel(args):
    if client.check(args, 'staff','admin'):
        args.subClient.unset_welcome_chat(args.chatId)
        args.subClient.send_message(args.chatId, "Confession GC unset!")
        rebot()
    else:
    	args.subClient.send_message(args.chatId,message="Only Leader or Curator can set Confession GC")

cons=mongo["coin"]
coi=cons["coins"]
ttt = open('claim.txt','r')
claims=[]
for m in ttt.read().splitlines():
	temp=m
	if temp not in claims:
		claims.append(int(temp))

#@client.command("claim")
def claim(data):
	rs=coi.find_one({"id":data.authorId})
	current=datetime.now()
	dat=current.day
	wall=int(data.subClient.get_wallet_amount())
	user=data.authorId
	if data.chatId=="e37563d9-ef8e-4966-b3a1-eb233c260c98":
		rs=coi.find_one({"id":user})
		if rs==None:
			
			lvl=data.subClient.get_user_info(user).level
			blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
			if lvl==5 or lvl>=5:
				if len(blg)!=0:
					if wall>=50:
						for bid in blg:
							data.subClient.send_coins(coins=38,blogId=bid)
							data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 38 coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							it={"id":user,"date":dat}
							coi.insert_one(it)
							#rebot()
					else:
						data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
				else:
					data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
			else:
				data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
		else:
			rs=coi.find_one({"id":user})
			dd=rs["date"]
			if dat-dd!=0:
				lvl=data.subClient.get_user_info(user).level
				blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
				if lvl==5 or lvl>=5:
					if len(blg)!=0:
						if wall>=500:
							for bid in blg:
								data.subClient.send_coins(coins=38,blogId=bid)
								data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 38 coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							filter = { 'id': user}
							newvalues = { "$set": { 'date': dat}}
							coi.update_one(filter, newvalues)
							#rebot()
						else:
							data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
					else:
						data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
				else:
					data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
			else:
				data.subClient.send_message(data.chatId,message=f"""<$@{data.author}$> you already claimed today
You can claim again after 24 hours""",replyTo=data.messageId, mentionUserIds=[data.authorId])
	else:
		op=client.get_from_id(objectId="e37563d9-ef8e-4966-b3a1-eb233c260c98",objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		data.subClient.send_message(data.chatId,message=f"Claim coins in this gc \n{chatlink}",replyTo=data.messageId)

@client.command("moneybhai")
def moneybhai(data):
	rs=coi.find_one({"id":data.authorId})
	current=datetime.now()
	dat=current.day
	wall=int(data.subClient.get_wallet_amount())
	user=data.authorId
	if data.chatId=="e37563d9-ef8e-4966-b3a1-eb233c260c98":
		rs=coi.find_one({"id":user})
		if rs==None:
			
			lvl=data.subClient.get_user_info(user).level
			blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
			if lvl==5 or lvl>=5:
				if len(blg)!=0:
					if wall>=50:
						for bid in blg:
							data.subClient.send_coins(coins=38,blogId=bid)
							data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 38 coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							it={"id":user,"date":dat}
							coi.insert_one(it)
							#rebot()
					else:
						pass
						#data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
				else:
					pass
					#data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
			else:
				pass
				#data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
		else:
			rs=coi.find_one({"id":user})
			dd=rs["date"]
			if dat-dd!=0:
				lvl=data.subClient.get_user_info(user).level
				blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
				if lvl==5 or lvl>=5:
					if len(blg)!=0:
						if wall>=500:
							for bid in blg:
								data.subClient.send_coins(coins=38,blogId=bid)
								data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 38 coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							filter = { 'id': user}
							newvalues = { "$set": { 'date': dat}}
							coi.update_one(filter, newvalues)
							#rebot()
						else:
							pass
							#data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
					else:
						pass
						#data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
				else:
					pass
					#data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
			else:
				pass
				#data.subClient.send_message(data.chatId,message=f"<{data.author}> you already claimed today
	else:
		op=client.get_from_id(objectId="e37563d9-ef8e-4966-b3a1-eb233c260c98",objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		pass
		#data.subClient.send_message(data.chatId,message=f"Claim coins in this gc \n{chatlink}",replyTo=data.messageId)



@client.command("claiim",condition=is_black)
def claiim(data):
	current=datetime.now()
	dat=current.day
	wall=int(data.subClient.get_wallet_amount())
	user=data.authorId
	if data.chatId=="0adf8ace-3f56-41a3-9677-f0957a267db6":
		rs=coi.find_one({"id":user})
		if rs==None:
			
			lvl=data.subClient.get_user_info(user).level
			blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
			if lvl==5 or lvl>=5:
				if len(blg)!=0:
					if wall>=500:
						for bid in blg:
							data.subClient.send_coins(coins=40,blogId=bid)
							data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 40+ coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							it={"id":user,"date":dat}
							coi.insert_one(it)
					else:
						data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
				else:
					data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
			else:
				data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
		else:
			rs=coi.find_one({"id":user})
			dd=rs["date"]
			if dat-dd!=0:
				lvl=data.subClient.get_user_info(user).level
				blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
				if lvl==5 or lvl>=5:
					if len(blg)!=0:
						if wall>=500:
							for bid in blg:
								data.subClient.send_coins(coins=40,blogId=bid)
								data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 40+ coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",mentionUserIds=[data.authorId])
							filter = { 'id': user}
							newvalues = { "$set": { 'date': dat}}
							coi.update_one(filter, newvalues)
							#rebot()
						else:
							data.subClient.send_message(data.chatId,message="Sorry,my Wallet is empty",replyTo=data.messageId)
					else:
						data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> post a  blog, you don't have blog",mentionUserIds=[data.authorId],replyTo=data.messageId)
				else:
					data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> increase your level to 5, you are below 5",replyTo=data.messageId, mentionUserIds=[data.authorId])
			else:
				data.subClient.send_message(data.chatId,message=f"""<$@{data.author}$> you already claimed today
You can claim again after 24 hours""",replyTo=data.messageId, mentionUserIds=[data.authorId])
	else:
		data.subClient.send_message(data.chatId,message="Claim command is off for this community, talk to Alexa owner",replyTo=data.messageId)

@client.command("level")
def level(args):
    if client.check(args, 'staff', 'admin'):
        try:
            args.message = int(args.message)
        except Exception:
            args.subClient.send_message(args.chatId, "Error, wrong level")
            return
        if args.message > 20:
            args.message = 20
        if args.message < 0:
            args.message = 0
        args.subClient.set_level(args.message)
        args.subClient.send_message(args.chatId, f"Level set to {args.message}!")
        
@client.command("battle",condition=is_black)
def battle(args):
	msg = args.message + " null null "
	msg = msg.split(" ")
	try:
		rounds = int(msg[0])
	except (TypeError, ValueError):
		rounds = 5
		msg[2] = msg[1]
		msg[1] = msg[0]
		msg[0] = 5
	args.subClient.send_message(chatId=args.chatId, message=f"Starts scoring between  {msg[1]} n {msg[2]}...")
	win1 = 0
	win2 = 0
	round = 0
	agress = ''
	defens = ''
	for game in range(0, rounds):
		round = round + 1
		args.subClient.send_message(chatId=args.chatId, message=f"[bc]Round {round}/{rounds}")
		punch = randint(0, 1)
		if punch == 0:
			win1 = win1 + 1
			agress = msg[1]
			defens = msg[2]
		else:
			     	win2 = win2 + 1
			     	agress = msg[2]
			     	defens = msg[1]
		time.sleep(4)
		args.subClient.send_message(chatId=args.chatId, message=f"[ic] {agress} hit 👊 {defens}!")
		if win1 > win2:
		  args.subClient.send_message(chatId=args.chatId, message=f"[bcu]{msg[1]} Won!")
		elif win1 < win2:
		  	args.subClient.send_message(chatId=args.chatId, message=f"[bcu]{msg[2]} Won!")
		elif win1 == win2:
		  		args.subClient.send_message(chatId=args.chatId, message=f"[iC]Nobody won, a draw!.")

@client.command("translate")
def translate(args):
    translator = google_translator()
    translate_text = translator.translate(args.message)
    args.subClient.send_message(args.chatId, f"Translation: {translate_text}",replyTo=messageId)

@client.command("leavecm")
def leavecm(data):
	if client.check(data,"admin"):
		link=data.message
		xd=Client().get_from_code(link)
		cid=xd.path[1:xd.path.index("/")]
		client.leave_community(comId=cid)
		data.subClient.send_message(data.chatId,message=f"Left {link} community")
@client.command("joincom")
def joincom(data):
	if client.check(data,'admin'):
		k=data.message
		link=k
		xd=Client().get_from_code(link)
		cid=xd.path[1:xd.path.index("/")]
		if "http://aminoapps.com/invite" in link:
			inv=c.get_from_code(link).json["extensions"]["invitationId"]
			client.join_community(comId=cid, invitationId=inv)
		else:
			client.join_community(cid)
		#dat={'comid':cid}
		#test_1.insert_one(dat)
		#f=open ("comids.txt","a")
		#f.write(str(cid)+"\n")
		Thread(target=client.threadLaunch, args=[cid, True]).start()
		data.subClient.send_message(data.chatId,message=f"Joined {cid} Community")
@client.command("mongo")
def mongo(data):
	if client.check(data,'admin'):
		k=data.message
		link=k
		xd=Client().get_from_code(link)
		cid=xd.path[1:xd.path.index("/")]
		dat={'comid':cid}
		test_1.insert_one(dat)
		print("Added mongo")
		data.subClient.send_message(data.chatId,message=f"Added {cid}")
		
@client.command("joincm", condition=is_black)
def joincm(data):
	if client.check(data,'admin'):
		k=data.message
		link=k
		xd=Client().get_from_code(link)
		cid=xd.path[1:xd.path.index("/")]
		dat={'comid':cid}
		#gh=test_1.count_documents({"comid":cid})
		#if gh==0:
		test_1.insert_one(dat)
		#else:
			#pass
		print("Added mongo")
		if "http://aminoapps.com/invite" in link:
			inv=client.get_from_code(link).json["extensions"]["invitationId"]
			client.join_community(comId=cid, invitationId=inv)
		else:
			client.join_community(cid)
		
		#f=open ("comids.txt","a")
		#f.write(str(cid)+"\n")
		#Thread(target=client.threadLaunch, args=[cid, True]).start()
		data.subClient.send_message(data.chatId,message=f"Joined {cid} Community")
		us=client.get_community_info(cid)
		u=us.aminoId
		da={"_id":u,"welcome": "", "prefix": "!", "welcome_chat": [], "locked_command": [], "favorite_users": [], "favorite_chats": [], "banned_words": []}
		jsonf.insert_one(da)
		

@client.command("mfile")
def mfile(data):
	if client.check(data,"admin"):
		us=client.get_community_info(cid)
		u=us.aminoId
		da={"_id":u,"welcome": "", "prefix": "!", "welcome_chat": [], "locked_command": [], "favorite_users": [], "favorite_chats": [], "banned_words": []}
		jsonf.insert_one(da)
		data.subClient.send_message(data.chatId,message="Done")
	else:
		pass

#@client.command("launch")
def lauhnch(data):
	data.subClient.send_message(data.chatId,"Launching")
	client.launch(True)
	data.subClient.send_message(data.chatId,"Launched done")
	
	

@client.command("coinon",condition=is_black)
def coinon(data):
		 data.subClient.edit_chat(chatId=data.chatId, canTip=True)
		 tz = pytz.timezone('Asia/Kolkata')
		 now = datetime.now(tz)
		 current_time=now.strftime("%H:%M:%S")
		 #now = datetime.now()
		 #current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
		 #current_time = now.strftime("%H:%M:%S")
		 #chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		 op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		 chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		 val=data.subClient.get_chat_thread(data.chatId).title
		 chats=data.subClient.favorite_chats
		 if val ==None:
		 	val="Private Chat"
		 for id, in zip(chats) :
		 	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} enabled CoinTip in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat:
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
@client.command("coinoff",condition=is_black)
def coinoff(data):
		 data.subClient.edit_chat(chatId=data.chatId, canTip=False)
		 tz = pytz.timezone('Asia/Kolkata')
		 now = datetime.now(tz)
		 current_time=now.strftime("%H:%M:%S")
		 #now = datetime.now()
		 #current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
		 #current_time = now.strftime("%H:%M:%S")
		 #chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		 op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		 chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		 val=data.subClient.get_chat_thread(data.chatId).title
		 chats=data.subClient.favorite_chats
		 if val ==None:
		 	val="Private Chat"
		 for id, in zip(chats) :
		 	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} disabled CoinTip in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat:
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
@client.command("wallet", condition=is_black)
def wallet(data):
	x=int(data.subClient.get_wallet_amount())
	data.subClient.send_message(data.chatId,message=f"Total coins {x}")
@client.command("framelists",condition=is_black)
def framelist(data):
	data.subClient.send_message(data.chatId, message=f"""[c]Frame List
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
1. Equalizer
2. Snow Globe
3. Dragon
4. Spiderweb
5. Dwarven
6. Scribbles
7. Graveyard
8. Prism
9. Fireworks
10. Armillary
11. Atom
12. Lunar Eclipse
13. Grid
14. Flames
15. Slime
16. Shoujo
17. Bowtie
18. Devil
19. Gold Player
20. Cupid
21. Red
22. Gray
23. White
24. Yellow
25. Pink
26. Neon
27. Green
28. Transparent
29. Angel
30. Glitch

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
	data.subClient.send_message(data.chatId,message="Send !frames number")

@client.command("framelist", condition=is_black)
def frml(data):
	#val=""
	#if not data.message:
	#	data.subClient.send_message(message="Select the number",chatId=data.chatId,replyTo=data.messageId)
		
	if client.check(data,'staff','admin'):
		list=[]
		x=client.get_avatar_frames(size=100)
		y=x.json
		val=""
		for elem in y:
			z=elem["name"]
			list.append(z)
		for i, vl in enumerate(list,1):
			#msg=(i,"-",val)
			val +=str(i)+"   -  "+vl +"\n"
			
		data.subClient.send_message(message=f"""[C]Frame List
[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val}

[C]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",chatId=data.chatId)
	else:
		data.subClient.send_message(message="Admin/Staff Command"
,chatId=data.chatId,replyTo=data.messageId)


@client.command("frame", condition=is_black)
def frame(data):
	if client.check(data,'staff','admin'):
		list=[]
		ru=int(data.message)
		po=ru-1
		x=client.get_avatar_frames(size=100)
		y=x.json
		for elem in y:
			z=elem["frameId"]
			list.append(z)
	#	for i, val in enumerate(list):
			#msg=(i,"-",val)
		id=list[int(po)]
		try:
			data.subClient.apply_avatar_frame(avatarId=id,applyToAll=False)
			data.subClient.send_message(message="Frame Changed",chatId=data.chatId)
		except:
			data.subClient.send_message(message="Frame not renewed/unavailable",chatId=data.chatId)
			pass
			
	else:
		data.subClient.send_message(message="Admin/Staff Command"
,chatId=data.chatId,replyTo=data.messageId)


@client.command("frames")
def frajme(data):
	if client.check(data,"staff","admin"):
		if data.message:
			f=open("frme.txt","r+")
			para=f.readlines()
			x=int(data.message)
			id=para[x].strip()
			data.subClient.apply_avatar_frame(avatarId=id,applyToAll=False)
			data.subClient.send_message(data.chatId, message="Frame Applied")
			data.subClient.apply_avatar_frame(avatarId=id,applyToAll=False)
		else:
			data.subClient.send_message(data.chatId, message="Select frame number from framelist command")		
	else:
		data.subClient.send_message(data.chatId, message="Admin Command")		

@client.command("json")
def create_community(data):
        with open(f'{path_amino}/{data.message}.json', 'w', encoding='utf8') as file:
            dict = {"welcome": "", "prefix": "!", "welcome_chat": "", "locked_command": [], "favorite_users": [], "favorite_chats": [], "banned_words": []}
            file.write(dumps(dict, sort_keys=False, indent=4))
            data.subClient.send_message(data.chatId,message=f"{data.message} file created")
@client.command()
def welaja(data):
	if client.check(data,"staff","admin"):
		str=data.message
		data.subClient.set_welcome_message(str)
		data.subClient.send_message(data.chatId,message=f"""
[C]Welcome message changed

{str}
""")

@client.command("offwel")
def offwel(data):
	data.subClient.unset_welcome_message()
	data.subClient.send_message(data.chatId,message="wall welcome turned off")

@client.command()
def botlog(data):
	if client.check(data,'staff','admin'):
		if data.chatId not in data.subClient.favorite_chats:
			data.subClient.add_favorite_chats(data.chatId)
			data.subClient.send_message(data.chatId,message="Botlog GC set")
			rebot()
		else:
			data.subClient.send_message(data.chatId,message="Already Set",replyTo=data.messageId)
			
	else:
		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)

		
@client.command()
def ubotlog(data):
	if client.check(data,'staff','admin'):
		if data.chatId  in data.subClient.favorite_chats:
			data.subClient.remove_favorite_chats(data.chatId)
			data.subClient.send_message(data.chatId,message="Botlog GC Removed")
			rebot()
		else:
			data.subClient.send_message(data.chatId,message="Already removed",replyTo=data.messageId)
			
	else:
		data.subClient.send_message(data.chatId,message="Mod Command",replyTo=data.messageId)		
#@client.command()

@client.command("blgr")
def blgr(data):
	for x in data.subClient.favorite_chats:
		data.subClient.remove_favorite_chats(x)
	data.subClient.send_message(data.chatId,message="Removed all")

@client.command("viewmode",condition=is_black)
def viewmode(data):
	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
	if client.userId in cho:
		data.subClient.edit_chat(chatId=data.chatId, viewOnly=True)
		time.sleep(60)
		data.subClient.edit_chat(chatId=data.chatId,viewOnly=False)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		val=data.subClient.get_chat_thread(data.chatId).title
		chats=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		for id, in zip(chats) :
			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} enabled viewmode in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[cu]Chat
[c]{chatlink}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(chatId=data.chatId, message="[i]I don't have Cohost")
		pass
		

@client.command()
def takehost(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if rol !=0 and client.check(data, 'staff', 'admin'):
		n=data.message
		fok=client.get_from_code(n)
		id=client.get_from_code(n).objectId
		data.subClient.transfer_host(chatId=id,userIds=[client.userId])
		info=data.subClient.get_chat_thread(id)
		x=info.json['extensions']['organizerTransferRequest']['requestId']
		data.subClient.accept_organizer(chatId=id,requestId=x)
		data.subClient.send_message(data.chatId,message="Accepted Host")
		data.subClient.send_message(chatId=id,message="Accepted Host")
		
	else:
		data.subClient.send_message(chatId=data.chatId, message="[i]I don't have Curator or Leader")
		pass

@client.command()
def givehost(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if rol !=0 and client.check(data, 'staff', 'admin'):
		mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
		if "aminoapps.com" in data.message:
			user=(client.get_from_code(data.message.split(' ')[0]).objectId)
		elif mention!=None:
			for x in mention:
				user=x
		else:
			user=data.authorId
		data.subClient.transfer_host(data.chatId,userIds=[str(user)])
		data.subClient.send_message(data.chatId,message="Host Request sent to user")
	else:
		data.subClient.send_message(chatId=data.chatId, message="[i]I don't have Curator or Leader")
		pass

#@client.command()
def giehost(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if rol !=0 and client.check(data, 'staff', 'admin'):
		mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
		for user in mention:
			data.subClient.transfer_host(data.chatId,userIds=[str(user)])
			data.subClient.send_message(data.chatId,message="Host Request sent")
	else:
		data.subClient.send_message(chatId=data.chatId, message="[i]I don't have Curator or Leader")
		pass

@client.command()
def gethost(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if rol !=0 and client.check(data, 'staff', 'admin'):
		data.subClient.transfer_host(data.chatId,userIds=[client.userId])
		info=data.subClient.get_chat_thread(data.chatId)
		x=info.json['extensions']['organizerTransferRequest']['requestId']
		data.subClient.accept_organizer(chatId=data.chatId,requestId=x)
		data.subClient.send_message(data.chatId,message="Accepted Host")
	else:
		data.subClient.send_message(chatId=data.chatId, message="[i]I don't have Curator or Leader")
		pass
@client.command("follow",condition=is_black)
def follow(args):
    args.subClient.follow_user(args.authorId)
    args.subClient.send_message(args.chatId, f"Alexa followed <$@{args.author}$>",mentionUserIds=[args.authorId])


@client.command("unfollow",condition=is_black)
def unfollow(args):
    args.subClient.unfollow_user(args.authorId)
    args.subClient.send_message(args.chatId, f"Alexa unfollowed <$@{args.author}$>",mentionUserIds=[args.authorId])

@client.command("joke",condition=is_black)
def joke(data):
	jk=pyjokes.get_jokes(language="en", category="all")
	i=random.randint(1,100)
	jkk=jk[i]
	try:
		msg=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{jkk}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
		data.subClient.send_message(data.chatId,message=msg)
	except:
		pass

@client.command("coin",condition=is_black)
def coin(args):
    x=int(args.message)
    transaction = "929ac10e-c483-4dc7-b150-367b27fbfdc5"
    if x<=500 or x==500:
    	args.subClient.send_coins(coins=x, chatId=args.chatId, transactionId=transaction)
    else:
    		args.subClient.send_message(chatId=args.chatId,message="[ic]Can't send more than 500 coins ")
@client.command("bubble")
def bubble(data):
	if client.check(data,'staff','admin'):
		z=data.subClient.get_user_info(data.authorId).json['extensions']['defaultBubbleId']
		data.subClient.apply_bubble(bubbleId=z,chatId=data.chatId,applyToAll=True)
		data.subClient.send_message(message="Chatbubble Applied",chatId=data.chatId,replyTo=data.messageId)
	else:
		data.subClient.send_message(message="Admin Command",chatId=data.chatId,replyTo=data.messageId)

@client.command(condition=is_staff)
def custom(data):
	#z=data.subClient.get_user_info(data.authorId).json['extensions']['defaultBubbleId']
	data.subClient.apply_bubble(bubbleId=data.message,chatId=data.chatId,applyToAll=True)
	data.subClient.send_message(message="Chatbubble Applied",chatId=data.chatId,replyTo=data.messageId)

@client.command("msg",condition=is_black)
def msg(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId,asStaff=True,reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10 and not (client.check(args, 'staff')):
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value, mentionUserIds=ment)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            kt=args.subClient.get_chat_thread(args.chatId). membersCanInvite
            if kt!=None:
            	op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
            	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
            else:
            	chatlink="Private Chat"
            #chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
            val=args.subClient.get_chat_thread(args.chatId).title
            chats=args.subClient.favorite_chats
            if val ==None:
            	val="Private Chat"
            for id, in zip(chats) :
            	args.subClient.send_message(chatId=id,message=f"""[c]{args.author} used hidden message in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")

def clears(d,md):
	try:
		d.subClient.delete_message(chatId=d.chatId,messageId=md,asStaff=True,reason="Clear")
	except:
		pass

@client.command(condition=is_staff)
def blast(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if (rol==100,rol==101):
		k=data.message
		d=int(k)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		val=data.subClient.get_chat_thread(data.chatId).title
		ch=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
		for _ in range(d):
			for i in a:
				with suppress(Exception):
					Thread(target=clears,args=(data,i,)).start()
				
		for id, in zip(ch):
			data.subClient.send_message(chatId=id,message=f"""[c]Blast command by {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

 {d} Messages cleared

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="[i]I don't have leader or Curator")
		pass

@client.command()
def clear(data):
	rol=data.subClient.get_user_info(userId=client.userId).json["role"]
	if client.check(data,'staff','admin') and (rol==100,rol==101):
		k=data.message
		d=int(k)
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		if kt!=None:
			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
			chatlink="Private Chat"
		#chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
		val=data.subClient.get_chat_thread(data.chatId).title
		ch=data.subClient.favorite_chats
		if val ==None:
			val="Private Chat"
		a=data.subClient.get_chat_messages(chatId=data.chatId,size=d).messageId
		for i in a:
			with suppress(Exception):
				Thread(target=clears,args=(data,i,)).start()
		#data.subClient.send_message(chatId=data.chatId,message=f"Cleared {d} messages",messageType=107)
		for id, in zip(ch):
			data.subClient.send_message(chatId=id,message=f"""[c]Clear command by {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙

[c]Cleared {d} messages

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		data.subClient.send_message(data.chatId,message="[i]Staff command", replyTo=data.messageId)
		pass

@client.command("background")
def background(data):
	if client.check(data,'staff','admin'):
		info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
		reply_message = info.json['extensions']
		if reply_message:
			image = info.json['extensions']['replyMessage']['mediaValue']
			
			filename="mypfp"
			filet = image.split(".")[-1]
			if filet=="gif":
				filetype="gif"
			else:
				filetype="image"
			urllib.request.urlretrieve(image, filename)
			img=open(filename,"rb")
			im=[img]
			for i in range(1,5):
				try:
					data.subClient.edit_profile(imageList=im,fileType=filetype)
				except Exception:
					pass
		data.subClient.send_message(data.chatId, message="Background changed",replyTo=data.messageId)
	else:
		data.subClient.send_message(data.chatId,message="Admin Command")				
@client.command()
def icon(data):
	if client.check(data,'staff','admin'):
		info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
		reply_message = info.json['extensions']
		if reply_message:
			image = info.json['extensions']['replyMessage']['mediaValue']
			
			filename="mypfp"
			filet = image.split(".")[-1]
			if filet=="gif":
				filetype="gif"
			else:
				filetype="image"
			urllib.request.urlretrieve(image, filename)
			img=open(filename,"rb")
			for i in range(1,5):
				try:
					data.subClient.edit_profile(icon=img,fileType=filetype)
				except Exception:
					pass
		data.subClient.send_message(data.chatId, message="Profile pic changed",replyTo=data.messageId)
	else:
		data.subClient.send_message(data.chatId,message="Admin Command")
@client.command("a",condition=is_black)
def a(data):
	bid="162843&key=uyk4IpiAS3SSjWXF"
	apikey="uyk4IpiAS3SSjWXF"
	id="162843"
	if data.message:
		message=data.message
		r = requests.get(url=f"http://api.brainshop.ai/get?bid={bid}&key={apikey}&uid={id}&msg={message}")
		ans=r.json()['cnt']
		data.subClient.send_message(data.chatId,message=ans,replyTo=data.messageId)
	else:
		data.subClient.send_message(data.chatId,message="Say something!!",replyTo=data.messageId)					

					
@client.command("video", condition=is_black)
def video(args):
	if args.message:
		#print(args.message)
		search=args.message
		search = search.replace(" ","+")
		html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+search)
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
		uls="https://www.youtube.com/watch?v=" + video_ids[0]
		args.subClient.send_message(args.chatId,message=f"""
[c]{args.message} video
[c]{uls}""")
	else:
		args.subClient.send_message(args.chatId,message="Write something to search\n!video Dance\nLike this",replyTo=args.messageId)								
@client.command("spam",condition=is_black)
def spam(args):
    quantity, msg = args.message.split()
    quantity = 1 if not quantity.isdigit() else int(quantity)
    quantity = 20 if quantity > 20 and not (client.check(args, 'staff','admin')) else quantity
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    current_time=now.strftime("%H:%M:%S")
    kt=args.subClient.get_chat_thread(args.chatId). membersCanInvite
    if kt!=None:
    	op=client.get_from_id(objectId=args.chatId,objectType="12",comId=args.comId).json
    	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    else:
    	chatlink="Private Chat"
    
    val=args.subClient.get_chat_thread(args.chatId).title
    ch=args.subClient.favorite_chats
    
    if val ==None:
    	val="Private Chat"
    for id in ch:
    	for i in range(1):
    		args.subClient.send_message(chatId=id,message=f"""[c]Spam command by {args.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

  Quantity :{quantity}
  Message :{msg}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{args.author}",embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",embedContent=f"chat: {val}")

    for _ in range(quantity):
        try:
        	args.subClient.send_message(args.chatId, msg)
        except:
        	pass

def rebot():
	os.remove("comid.txt")
	file=open("comid.txt","w")
	os.execv(sys.executable, ['python'] + sys.argv)        	
@client.command()
def reboot(args):
        if client.check(args,'admin'):
        	os.remove("comid.txt")
        	file=open("comid.txt","w")
        	args.subClient.send_message(args.chatId, "Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)
        else:
        	args.subClient.send_message(args.chatId, "Admin command",replyTo=args.messageId)

@client.command()
def restartbot(args):
        if client.check(args,'admin'):
        	os.remove("comid.txt")
        	file=open("comid.txt","w")
        	#args.subClient.send_message(args.chatId, "Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)

def magicnum():
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime        	
        
@client.command()
def prefix(args):
    if args.message and client.check(args,'staff','admin'):
        args.subClient.set_prefix(args.message)
        args.subClient.send_message(args.chatId, f"My prefix set as {args.message}")
     
#@client.on_all() #on message tha phle ye
def mesge(data):
	it={'ids':data.messageId,'userid':data.authorId,'link':data.message}
	jsoon.insert_one(it)
#	jsy.insert_one(it)
	nioo=jsy.count_documents({})
	if nioo>=5000:
		jsy.delete_many({})
	else:
		pass
	noo=jsn.count_documents({})
	if noo>=5000:
		jsn.delete_many({})
	else:
		pass
	no=jsoon.count_documents({})
	if no>=5000:
		jsoon.delete_many({})
	else:
		pass
	if data.authorId in data.subClient.muted_users:
		data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True,reason="muted user")
	else:
		pass
	#tm()
	#with suppress(Exception):
	try:
		time.sleep(30)
		#	dm=["Chatting"]
		client.show_online(data.comId)
			#client.send_action(actions=dm,comId=data.comId,chatId=data.chatId)
	except:
		pass

@client.command("wallw",condition=is_black)
def wallw(data):
	try:
		data.subClient.welcome_new_member()
	except:
		pass
	
def iucn(d,udd):
	try:
		d.subClient.live_notify(userId=udd,chatId=d.chatId)
	except:
		pass
		

@client.command(condition=is_black)
def notifyall(data):
	h=data.subClient.get_online_users(start=0,size=100).profile.userId
	j=data.subClient.get_online_users(start=0,size=100).profile.nickname
	u=len(j)
	for ud in h:
		Thread(target=iucn,args=(data,ud,)).start()
	data.subClient.send_message(chatId=data.chatId,message=f"Notified {u} members")
	
@client.command("bnan")
def bjan(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention and client.check(data,"admin"):
		for user in mention:
			h=data.subClient.get_user_info(userId=str(user)).nickname
			data.subClient.ban(userId=user,reason="Abuse")
			data.subClient.send_message(data.chatId,message=f"Banned {h}")
	else:
		data.subClient.send_messsage(data.chatId,message="Mod Command",replyTo=data.messageId)

@client.command("unbban")
def unjban(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention and client.check(data,"admin"):
		for user in mention:
			h=data.subClient.get_user_info(userId=str(user)).nickname
			data.subClient.unban(userId=user,reason="spam")
			data.subClient.send_message(data.chatId,message=f"Unbanned {h}")
	else:
		data.subClient.send_messsage(data.chatId,message="Mod Command",replyTo=data.messageId)		
@client.command("giveco")
def giveco(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	if mention and client.check(data,"staff","admin"):
		for user in mention:
			list=[]
			list.append(str(user))
			h=data.subClient.get_user_info(userId=str(user)).nickname
			data.subClient.edit_chat(data.chatId,coHosts=[user])
			data.subClient.send_message(data.chatId,message=f"<${h}$> set as Cohost")
	else:
		data.subClient.send_messsage(data.chatId,message="I don't have Host",replyTo=data.messageId)
@client.command("userinfo", condition=is_black)
def userinfo(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    if data.message:
    	user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    elif mention!=None:
    	for x in mention:
    		user=x
    else:
    	user=data.authorId
    x=data.subClient.get_user_info(userId=client.userId).json["role"]
    #user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    ic=data.subClient.get_user_info(str(user)).icon
    response=requests.get(f"{ic}")
    file=open(".yays.png","wb")
    file.write(response.content)
    file.close()
    imgg=(".yays.png")
    Image.open(imgg).resize((800,800)).save("prof.png")
    ff=open("prof.png","rb")
    repa= data.subClient.get_user_info(userId=str(user)).reputation
    h=data.subClient.get_user_info(userId=str(user)).nickname
    lvl = data.subClient.get_user_info(userId=str(user)).level
    crttime = client.get_user_info(userId=str(user)).createdTime
    followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
    commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
    posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
    if x==100:
    	gstrk=data.subClient.get_user_info(userId=str(user)).globalStrikeCount
    else:
    	gstrk="0"
    glob=client.get_user_info(userId=str(user)).aminoId
    vip =data.subClient.get_user_info(userId=str(user)).accountMembershipStatus
    if x==100:
    	wrn=data.subClient.get_user_info(userId=str(user)).warningCount
    	strk=data.subClient.get_user_info(userId=str(user)).strikeCount
    else:
    	wrn= "0"
    	strk= "0"
    bg=data.subClient.get_user_info(userId=str(user)).mediaList
    followed = data.subClient.get_user_info(userId=str(user)).followingCount
    if vip==1:
    	vips="Active"
    else:
    	vips="Not Active"
    if bg ==None:
    	bgs="No Image"
    else:
    	bgs=bg[0][1]
    msg=f"""[cu]{h}'s ᴘʀᴏғɪʟᴇ

• ɴᴀᴍᴇ - {h}
• ʟᴇᴠᴇʟ - {lvl}
• ʀᴇᴘs - {repa}
• ғᴏʟʟᴏᴡᴇʀs - {followers}
• ғᴏʟʟᴏᴡᴇᴅ - {followed}
• ᴡᴀʟʟ ᴄᴏᴍᴍᴇɴᴛs - {commentz}
• ᴘᴏsᴛs - {posts}
• sᴛʀɪᴋᴇ - {strk}
• ɢʟᴏʙᴀʟ sᴛʀɪᴋᴇ - {gstrk}
• ᴡᴀʀɴɪɴɢ - {wrn}
• ᴀᴍɪɴᴏᴘʟᴜs - {vips}
• ɢʟᴏʙᴀʟɪᴅ - {glob}
• ɪᴅ ᴄʀᴇᴀᴛᴇᴅ - {crttime}
• ᴍᴏᴅɪғɪᴇᴅ - {profilchange}
• ɪᴄᴏɴ - {ic}
• ʙᴀᴄᴋɢʀᴏᴜɴᴅ - {bgs}
• ᴜsᴇʀɪᴅ - {str(user)}

"""
    data.subClient.send_message(chatId=data.chatId,message=msg,embedTitle=f"{h}",embedLink=f"ndc://x{data.comId}/user-profile/{user}",embedContent="Profile Link",embedImage=ff)
@client.command("horoscope",condition=is_black)
def horoscope(data):
	if data.message:
		try:
			ic=data.subClient.get_user_info(data.authorId).icon
			response=requests.get(f"{ic}")
			file=open("hor.png","wb")
			file.write(response.content)
			file.close()
			ff=open("hor.png","rb")
			msg=data.message.split(" ")
			signs=msg[0]
			dy=msg[1]
			params = (('sign', signs),('day', dy),)
			z=requests.post('https://aztro.sameerkumar.website/', params=params)
			s=(z.text)
			j=json.loads(s)
			nu=j["lucky_number"]
			tim=j["lucky_time"]
			color=j["color"]
			desc=j["description"]
			mood=j["mood"]
			comp=j["compatibility"]
			mg=f"""[c]{data.author}'s {dy}'s Horoscope
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

ʟᴜᴄᴋʏ ɴᴜᴍʙᴇʀ : {nu}
ᴄᴏʟᴏʀ : {color}
ʟᴜᴄᴋʏ ᴛɪᴍᴇ : {tim}
ᴍᴏᴏᴅ : {mood}
ᴄᴏᴍᴘᴀᴛɪʙɪʟɪᴛʏ : {comp}

[cu]ʜᴏʀᴏsᴄᴏᴘᴇ

[c]{desc}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁"""
			data.subClient.send_message(chatId=data.chatId,message=mg,embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent="Profile Link",embedImage=ff)
		except Exception:
			mggg="""[cu]Enter your zodiac sign and day

[u]Example: 
[b]!horoscope aries today

[u]List of Zodiac signs
aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces

[u]Day
Today
Yesterday
Tomorrow
"""
			data.subClient.send_message(chatId=data.chatId,message=mggg)
			pass
			
	else:
		mgg="""[cu]Enter your zodiac sign and day

[u]Example: 
[b]!horoscope aries today

[u]List of Zodiac signs
aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces

[u]Day
Today
Yesterday
Tomorrow
"""
		data.subClient.send_message(chatId=data.chatId,message=mgg)

@client.command("uo", condition=is_black)
def ufo(data):
    user=(client.get_from_code(data.message.split(' ')[0]).objectId)
    ic=data.subClient.get_user_info(str(user)).icon
    response=requests.get(f"{ic}")
    file=open(".yays.png","wb")
    file.write(response.content)
    file.close()
    imgg=(".yays.png")
    Image.open(imgg).resize((800,800)).save("prof.png")
    ff=open("prof.png","rb")
    repa= data.subClient.get_user_info(userId=str(user)).reputation
    h=data.subClient.get_user_info(userId=str(user)).nickname
    lvl = data.subClient.get_user_info(userId=str(user)).level
    crttime = client.get_user_info(userId=str(user)).createdTime
    followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
    commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
    posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
    gstrk=data.subClient.get_user_info(userId=str(user)).globalStrikeCount
    glob=client.get_user_info(userId=str(user)).aminoId
    vip =data.subClient.get_user_info(userId=str(user)).accountMembershipStatus
    wrn=data.subClient.get_user_info(userId=str(user)).warningCount
    strk=data.subClient.get_user_info(userId=str(user)).strikeCount
    bg=data.subClient.get_user_info(userId=str(user)).mediaList
    followed = data.subClient.get_user_info(userId=str(user)).followingCount
    if vip==1:
    	vips="Active"
    else:
    	vips="Not Active"
    msg=f"""[cu]{h}'s ᴘʀᴏғɪʟᴇ

• ɴᴀᴍᴇ - {h}
• ʟᴇᴠᴇʟ - {lvl}
• ʀᴇᴘs - {repa}
• ғᴏʟʟᴏᴡᴇʀs - {followers}
• ғᴏʟʟᴏᴡᴇᴅ - {followed}
• ᴡᴀʟʟ ᴄᴏᴍᴍᴇɴᴛs - {commentz}
• ᴘᴏsᴛs - {posts}
• sᴛʀɪᴋᴇ - {strk}
• ɢʟᴏʙᴀʟ sᴛʀɪᴋᴇ - {gstrk}
• ᴡᴀʀɴɪɴɢ - {wrn}
• ᴀᴍɪɴᴏᴘʟᴜs - {vips}
• ɢʟᴏʙᴀʟɪᴅ - {glob}
• ɪᴅ ᴄʀᴇᴀᴛᴇᴅ - {crttime}
• ᴍᴏᴅɪғɪᴇᴅ - {profilchange}
• ɪᴄᴏɴ - {ic}
• ʙᴀᴄᴋɢʀᴏᴜɴᴅ - {bg[0][1]}
• ᴜsᴇʀɪᴅ - {str(user)}

"""
    data.subClient.send_message(chatId=data.chatId,message=msg,embedTitle=f"{h}",embedLink=f"ndc://x{data.comId}/user-profile/{user}",embedContent="Profile Link",embedImage=ff)			
@client.command("mentionco")
def mentionco(args):
    if client.check(args, 'staff', 'admin'):
        if args.message and client.check(args, 'admin'):
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_thread(args.chatId).json['extensions']['coHost']]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_thread(args.chatId).json['extensions']['coHost']])
        #print(test)

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"<$@Cohosts{test}$>", mentionUserIds=mention)

#@client.on_remove()
def reonve(data):
  #  print(data.comId)
    #client.show_online(data.comId)
    if data.chatId:
    	du={}#b[.messageIdatad]="deleted"  
    	si="echo "+f"{data.messageId}"+f">>deletes.txt"
    	system(si)
    	messages = data.subClient.get_chat_messages(data.chatId,50).messageId
    	for m in messages:
    	     if m in yooo()[int(f"-1")]:
    	     	print(m)
    	     	value = jsoon.find_one({"ids": m})
    	     	tz = pytz.timezone('Asia/Kolkata')
    	     	now = datetime.now(tz)
    	     	current_time=now.strftime("%H:%M:%S")
    	     	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
    	     	if kt!=None:
    	     	 	op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
    	     	 	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    	     	else:
    	     	 	chatlink="Private Chat"
    	     	val=data.subClient.get_chat_thread(data.chatId).title
    	     	chats=data.subClient.favorite_chats
    	     	if val==None:
    	     	 	val="Private Chat"
    	     	mis=value["link"]
    	     	for id in chats:
    	     	 	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted message in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{mis}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    	     else:
    	     	pass          


def medex(data):
	d={}#b[.messageIdatad]="deleted"  
	s="echo "+f"{data.messageId}"+">>deleted.txt"
	system(s)
	messages = data.subClient.get_chat_messages(data.chatId,20).messageId
	for m in messages:
		if m in yoo()[int(f"-1")]:
			print(m)
			if m:
				value = jsn.find_one({"sd": m})
				tz = pytz.timezone('Asia/Kolkata')
				now = datetime.now(tz)
				current_time=now.strftime("%H:%M:%S")
				kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
				val=data.subClient.get_chat_thread(data.chatId).title
				chats=data.subClient.favorite_chats
				if kt !=None:
				        op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
				        chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
				else:
					chatlink="Private Chat"
				if val==None:
				        val="Private Chat"
				ms=value['link']
				if ms.startswith("ndc"):
					vat="Default Sticker"
					name="Sticker"
				elif ms.endswith("jpg"):
					vat=f"""[c]Image Link
{ms}"""
					name="Image"
				elif ms.endswith("jpeg"):
					vat=f"""[c]Sticker Link
{ms}"""
					name="Sticker"
				elif ms.endswith("gif"):
					vat=f"""[c]Gif Link
{ms}"""
					name="gif"
				elif ms.endswith("png"):
					vat=f"""[c]Image Link
{ms}"""
					name="Image"
				else:
					vat=f"""[c]Video Link
{ms}"""
					name="Video"
				for id, in zip(chats):
					if ms!=None:
						data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted {name} in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{vat}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
					else:
						pass
						


def newre(data):
  #  print(data.comId)
    #client.show_online(data.comId)
  #  if data.chatId:
    	du={}#b[.messageIdatad]="deleted"  
    	si="echo "+f"{data.messageId}"+f">>deletes.txt"
    	system(si)
    	messagess = data.subClient.get_chat_messages(data.chatId,20).messageId
    	for nm in messagess:
    	     if nm in yooo()[int(f"-1")]:
    	     	print(nm)
    	     	valuee = jsoon.find_one({"ids": nm})
    	     	tz = pytz.timezone('Asia/Kolkata')
    	     	now = datetime.now(tz)
    	     	current_time=now.strftime("%H:%M:%S")
    	     	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
    	     	if kt!=None:
    	     	 	op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
    	     	 	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    	     	else:
    	     	 	chatlink="Private Chat"
    	     	val=data.subClient.get_chat_thread(data.chatId).title
    	     	chats=data.subClient.favorite_chats
    	     	if val==None:
    	     	 	val="Private Chat"
    	     	mis=valuee["link"]
    	     	for id in chats:
    	     	 	if mis!=None:
    	     	 		data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted message in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{mis}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    #	     else:
    	     #	pass 

@client.on_remove()
def rema(data):
	try:
		newre(data)
	except:
		pass
	try:
		medex(data)
	except:
		pass


#@client.on_remove()
def remooove(data):
    newre(data)
    print(data.comId)
    if data.chatId:
      d={}#b[.messageIdatad]="deleted"  
      s="echo "+f"{data.messageId}"+">>deleted.txt"
      system(s)
      messages = data.subClient.get_chat_messages(data.chatId,20).messageId
    for m in messages:
    	if m in yoo()[int(f"-1")]:
          print(m)
          if m:
            #objInstance = ObjectId(m)
            #u=jsonf.find_one({"_id": objInstance})
            value = jsn.find_one({"sd": m})
            
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time=now.strftime("%H:%M:%S")
            kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
            	
            	
           # except:
            	#chatlink="Private Chat"
           # 	pass

            #chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
            
            val=data.subClient.get_chat_thread(data.chatId).title
            chats=data.subClient.favorite_chats
            if kt !=None:
            	op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
            	
            	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
            else:
            	chatlink="Private Chat"
            if val==None:
            	val="Private Chat"
            
            #if not chatlink:
            #	chatlink="Private Chat"
            	
            ms=value['link']
            if ms.startswith("ndc"):
            	vat="Default Sticker"
            	name="Sticker"
            elif ms.endswith("jpg"):
            	vat=f"""[c]Image Link
{ms}"""
            	name="Image"
            elif ms.endswith("jpeg"):
            	vat=f"""[c]Sticker Link
{ms}"""
            	name="Sticker"
            elif ms.endswith("gif"):
            	vat=f"""[c]Gif Link
{ms}"""
            	name="gif"
            elif ms.endswith("png"):
            	vat=f"""[c]Image Link
{ms}"""
            	name="Image"
            else:
            	name="Video"
            	vat=f"""[c]Video Link
{ms}"""
			         
            #ms=str(value).split(" ",1)
            for id, in zip(chats):
            	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted {name} in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{vat}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")


#@client.on_delete()
def reove(data):
    print(data.comId)
    if data.chatId:
    	du={}#b[.messageIdatad]="deleted"  
    	si="echo "+f"{data.messageId}"+">>deletes.txt"
    	system(si)
    	messages = data.subClient.get_chat_messages(data.chatId,5).messageId
    	for m in messages:
    	     if m in yooo()[int(f"-1")]:
    	     	print(m)
    	     	value = jsoon.find_one({"_id": m})
    	     	tz = pytz.timezone('Asia/Kolkata')
    	     	now = datetime.now(tz)
    	     	current_time=now.strftime("%H:%M:%S")
    	     	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
    	     	if kt!=None:
    	     	 	op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
    	     	 	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    	     	else:
    	     	 	chatlink="Private Chat"
    	     	val=data.subClient.get_chat_thread(data.chatId).title
    	     	chats=data.subClient.favorite_chats
    	     	if val==None:
    	     	 	val="Private Chat"
    	     	mis=value["link"]
    	     	for id, in zip(chats):
    	     	 	data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted message in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{mis}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    	     else:
    	     	pass
    if data.chatId:
      d={}#b[.messageIdatad]="deleted"  
      s="echo "+f"{data.messageId}"+">>deleted.txt"
      system(s)
      messages = data.subClient.get_chat_messages(data.chatId,5).messageId
    for um in messages:
    	if um in yoo()[int(f"-1")]:
    		value = jsn.find_one({"_id": um})
    		tz = pytz.timezone('Asia/Kolkata')
    		now = datetime.now(tz)
    		current_time=now.strftime("%H:%M:%S")
    		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
    		val=data.subClient.get_chat_thread(data.chatId).title
    		chats=data.subClient.favorite_chats
    		if kt !=None:
    			op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
    			chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
    		else:
    		      chatlink="Private Chat"
    		if val==None:
    		      val="Private Chat"
    		ms=value['link']
    		if ms.startswith("ndc"):
    			vat="Default Sticker"
    			name="Sticker"
    		elif ms.endswith("jpg"):
    			name="Image"
    			vat=f"[c]Image Link\n{ms}"
    		elif ms.endswith("jpeg"):
    			vat=f"[c]Sticker Link\n{ms}"
    			name="Sticker"
    		elif ms.endswith("gif"):
    			vat=f"[c]Gif Link\n{ms}"
    			name="gif"
    		elif ms.endswith("png"):
    			vat=f"[c]Image Link\n{ms}"
    			name="Image"
    		else:
    			name="Video"
    			vat=f"[c]Video Link\n{ms}"
    		for id, in zip(chats):
    			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted {name} in {val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{vat}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    	else:
    	       pass
@client.command("addvip")
def addvip(args):
    if client.check(args,"admin","staff"):
            	user=(client.get_from_code(args.message.split(' ')[0]).objectId)
            	h=args.subClient.get_user_info(userId=user).nickname
            	
            	msg=args.message.split(" ")
            	coin=int(msg[1])
            	args.subClient.add_influencer(user, coin)
            	args.subClient.send_message(args.chatId, f" Added {h} to VIP")
            		
@client.command("removevip")
def removevip(args):
    if client.check(args,"admin","staff"):
            	user=(client.get_from_code(args.message.split(' ')[0]).objectId)
            	h=args.subClient.get_user_info(userId=user).nickname
            	args.subClient.remove_influencer(user)
            	args.subClient.send_message(args.chatId, f" Removed {h} from VIP")
#@client.on_delete()
def getdel(data):
    if data.chatId not in deleted_messages.keys():
        deleted_messages[data.chatId] = {}
    try:
        deleted_messages[data.chatId][data.messageId] = old_messages[data.chatId][data.messageId]
        with open(filed, "w") as f:
        	json.dump(deleted_messages, f, indent=4)
    except KeyError:
        pass
    messages = data.subClient.get_chat_messages(data.chatId, 10).messageId
    for m in messages:
                try:
                	tz = pytz.timezone('Asia/Kolkata')
                	now = datetime.now(tz)
                	current_time=now.strftime("%H:%M:%S")
                	kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
                	if kt!=None:
                		op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
                		chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
                	else:
                		chatlink="Private Chat"
                	
                	val=data.subClient.get_chat_thread(data.chatId).title
                	if val ==None:
                		val="Private Chat"
                	chats=data.subClient.favorite_chats
                	for id, in zip(chats) :
                		data.subClient.send_message(chatId=id,message=f"""[c]{data.author} deleted message in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Deleted message

{deleted_messages[data.chatId][m]}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
                except:
                	pass


@client.command("rankers", condition=is_black)
def rankers(data):
	try:
		ranktoday(data)
		rankweek(data)
	except:
		pass
	


def rankweek(data):
	nicka=[]
	acti=[]
	val=""
	cal=""
	dal=""
	q=data.subClient.get_leaderboard_info(type="day",size=5).json
	for x in q:
		nick=x["nickname"]
#		actii=x["activeTime"]
	#	act=actii/3600
		nicka.append(nick)
	#	acti.append(int(act))
		
	for i, vl in enumerate(nicka,1):
		val +=str(i)+" - "+vl+"\n"
#	for vli in merged_list:
	#	cal =vli +" Hr"+"\n"
	#dal=dal + +"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Top Active users - Weekly
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")

def ranktoday(data):
	nicka=[]
	acti=[]
	val=""
	cal=""
	dal=""
	q=data.subClient.get_leaderboard_info(type="hour",size=5).json
	for x in q:
		nick=x["nickname"]
	#	actii=x["activeTime"]
	#	act=actii/3600
		nicka.append(nick)
		#acti.append(int(act))
		
	
	for i, vl in enumerate(nicka,1):
		val +=str(i)+" - "+vl +"\n"
	#for vli in acti:
		#cal =cal+ str(vli) +" Hr"+"\n"
	#dal=dal + val+ " - " + cal +"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Top Active users - Daily
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val} 
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")


@client.command("mostactive", condition=is_black)
def mostactive(data):
	try:
		rtoday(data)
		rweek(data)
	except:
		pass
	


def rweek(data):
	nicka=[]
	acti=[]
	val=""
	cal=""
	dal=""
	q=data.subClient.get_leaderboard_info(type="day",size=1).json
	for x in q:
		nick=x["nickname"]
		actii=x["activeTime"]
		acto=actii/3600
		act=int(acto)
		#nicka.append(nick)
	#	acti.append(int(act))
		
	#for i, vl in enumerate(nicka,1):
		#val +=str(i)+" - "+vl+"\n"
#	for vli in merged_list:
	#	cal =vli +" Hr"+"\n"
	#dal=dal + +"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Most active weekly
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
× {nick}

× Active : {act} hrs
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙""")

def rtoday(data):
	nicka=[]
	acti=[]
	val=""
	cal=""
	dal=""
	q=data.subClient.get_leaderboard_info(type="hour",size=1).json
	for x in q:
		nick=x["nickname"]
		actii=x["activeTime"]
		acto=actii/3600
		act=int(acto)
		#nicka.append(nick)
		#acti.append(int(act))
		
	
	for i, vl in enumerate(nicka,1):
		val +=str(i)+" - "+vl +"\n"
	#for vli in acti:
		#cal =cal+ str(vli) +" Hr"+"\n"
	#dal=dal + val+ " - " + cal +"\n"
	data.subClient.send_message(chatId=data.chatId,message=f"""
[c]Most active Today
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
• {nick}

• Active : {act} hrs 
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙""")


@client.command("fancytext",condition=is_black)
def fancytext(args):
	msg = args.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	args.subClient.send_message(args.chatId, message=fancy.light(msg[1]))
	args.subClient.send_message(args.chatId, message=fancy.bold(msg[1]))
	args.subClient.send_message(args.chatId, message=fancy.box(msg[1]))
	args.subClient.send_message(args.chatId, message=fancy.sorcerer(msg[1]))
@client.command("mute", condition=is_black)
def mute(data):
        if client.check(data,"staff","admin"):
        	if "aminoapps.com" in data.message:
        		uid=(client.get_from_code(data.message.split(' ')[0]).objectId)
        		if uid not in adm and not client.is_it_admin(uid):
        			if uid not in data.subClient.muted_users:
        				h=data.subClient.get_user_info(userId=uid).nickname
        				data.subClient.add_muted_users(uid)
        				data.subClient.send_message(data.chatId, f"<$@{h}$> is muted in this Community ",mentionUserIds=[uid])
        				rebot()
        			else:
        				data.subClient.send_message(data.chatId,message="User is already mute")
        		else:
        			data.subClient.send_message(data.chatId,message="You cannot mute Admins")
        	else:
        		mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds  
        		for uid in mention:
        			if uid not in adm and not client.is_it_admin(uid):
        				if uid not in data.subClient.muted_users:
        					h=data.subClient.get_user_info(userId=uid).nickname
        					data.subClient.add_muted_users(uid)
        					data.subClient.send_message(data.chatId, f"<$@{h}$> is muted in this Community ",mentionUserIds=[uid])
        					rebot()
        				else:
        					data.subClient.send_message(data.chatId,message="User is already mute")
        			else:
        				data.subClient.send_message(data.chatId,message="You cannot mute Admins")
        else:
        	data.subClient.send_message(data.chatId,message="Mod command",replyTo=data.messageId)
        	
@client.command("unmute", condition=is_black)
def unmute(data):
        if client.check(data,"staff","admin"):
        	if "aminoapps.com" in data.message:
        		uid=(client.get_from_code(data.message.split(' ')[0]).objectId)
        	else:
        		mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
        		for x in mention:
        			uid=x
        	if uid in data.subClient.muted_users:
        		h=data.subClient.get_user_info(userId=uid).nickname
        		data.subClient.remove_muted_users(uid)
        		#data.subClient.remove_comids(data.comId)
        		data.subClient.send_message(data.chatId, f"<$@{h}$> is unmuted in this Community ",mentionUserIds=[uid])
        		rebot()
        	else:
        		data.subClient.send_message(data.chatId,message="User not in mutelist")        		
        else:
        	data.subClient.send_message(data.chatId,message="Mod command",replyTo=data.messageId)        	
@client.command()
def taxe(args):
        coins = args.subClient.get_wallet_amount()
        if coins >= 1 and client.check(args,'admin'):
            amt = 0
            while coins > 500:
                args.subClient.pay(500, chatId=args.chatId)
                coins -= 500
                amt += 500
            args.subClient.pay(int(coins), chatId=args.chatId)
            args.subClient.send_message(args.chatId, f"Sending {coins+amt} coins...")
        else:
            args.subClient.send_message(args.chatId, "Account is empty!")
#ravi
#keep_alive()

import sys
def maintenance():
    print("launch maintenance")
    i = 0
    while i < 7200:
        i += 10
        time.sleep(10)
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])


client.launch(True)
print("ready")
#threading.Thread(target=maintenance).start()
def reconsocketloop():
    while True:
        client.close()
        client.run_amino_socket()
        sleep(120)

socketloop = threading.Thread(target=reconsocketloop, daemon=True)
socketloop.start()
