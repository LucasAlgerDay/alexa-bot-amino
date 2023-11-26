from time import sleep as slp
from threading import Thread
# from concurrent.futures import ThreadPoolExecutor
from os import system
from contextlib import suppress
from unicodedata import normalize
from string import punctuation
import time
from amino import objects
from .Bot import Bot
import argparse
from pymongo import MongoClient
import urllib.parse

import ssl
monk=[]
mon= open("mongo.txt", "r").read().splitlines()
for i in mon:
	monk.append(i)

mongos=monk[0]
mongo=MongoClient(f"mongodb+srv://{mongos}/?retryWrites=true&w=majority")
#mongo = MongoClient("mongodb://alexa:aman@cluster0-shard-00-00.3nela.mongodb.net:27017,cluster0-shard-00-01.3nela.mongodb.net:27017,cluster0-shard-00-02.3nela.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ngo3g6-shard-0&authSource=admin&retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://cartoons:cwaamino@cluster0.3nela.mongodb.net/?retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://lofis:lofi@cluster0.qnib4jt.mongodb.net/?retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://kiritovayux:aminobc@cluster0.emr3bjf.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#mongo = MongoClient("mongodb://levi:ravi@cluster0-shard-00-00.jm6ez.mongodb.net:27017,cluster0-shard-00-01.jm6ez.mongodb.net:27017,cluster0-shard-00-02.jm6ez.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-4586d7-shard-0&authSource=admin&retryWrites=true&w=majority")
dih=mongo['deleteds']
jsy=dih['messe']
class TimeOut:
    users_dict = {}

    def time_user(self, uid, end: int = 5):
        if uid not in self.users_dict.keys():
            self.users_dict[uid] = {"start": 0, "end": end}
            Thread(target=self.timer, args=[uid]).start()

    def timer(self, uid):
        while self.users_dict[uid]["start"] <= self.users_dict[uid]["end"]:
            self.users_dict[uid]["start"] += 1
            slp(1)
        del self.users_dict[uid]

    def timed_out(self, uid):
        if uid in self.users_dict.keys():
            return self.users_dict[uid]["start"] >= self.users_dict[uid]["end"]
        return True


class BannedWords:
    def filtre_message(self, message, code):
        try:
        	para = normalize('NFD', message).encode(code, 'ignore').decode("utf8").strip().lower()
        	para = para.translate(str.maketrans("", "", punctuation))
        except:
        	pass
        return para

    def check_banned_words(self, args):
        for word in ("ascii", "utf8"):
            with suppress(Exception):
                parat = self.filtre_message(args.message, word).split()
        if parat != [""]:
        	print(parat)
        with suppress(Exception):
        	for elem in parat:
        		if elem in args.subClient.banned_words:
        			
        			it={'userid':args.authorId,'link':args.message}
        			jsy.insert_one(it)
        			#print(args.messageId)
        	[args.subClient.delete_message(args.chatId, args.messageId, reason=f"Banned word : {elem}", asStaff=True) for elem in parat if elem in args.subClient.banned_words]
        	[args.subClient.send_message(args.chatId,message=f"<$@{args.author}$> don't use banned words",mentionUserIds=[args.authorId]) for elem in parat if elem in args.subClient.banned_words]
    def check_ban_words(self, args):
            for word in ("ascii", "utf8"):
                with suppress(Exception):
                	parat = self.filtre_message(args.message, word).split()
            if parat != [""]:
            	print(parat)
            with suppress(Exception):
            	for elem in parat:
            		if elem in args.subClient.banned_words:
            			si="echo "+f"{args.messageId}"+">>deleteds.txt"
            			system(si)
            			print(args.messageId)

class Parameters:
    __slots__ = (
                    "subClient", "chatId", "authorId", "author", "message", "messageId","level","reputation","json",
                    "authorIcon", "comId", "replySrc", "replyMsg", "replyId", "info"
                 )

    def __init__(self, data: objects.Event, subClient):
        self.subClient = subClient
        self.chatId = data.message.chatId
        self.authorId = data.message.author.userId
        self.author = data.message.author.nickname
        self.message = data.message.content
        self.messageId = data.message.messageId
        self.authorIcon = data.message.author.icon
        try: self.level = data.message.json["author"]["level"]
        except: pass
        try: self.json = data.message.json
        except: pass
        try: self.reputation = data.message.json["author"]["reputation"]
        except: pass
        self.comId = data.comId

        self.replySrc = None
        self.replyId = None
        if data.message.extensions and data.message.extensions.get('replyMessage', None) and data.message.extensions['replyMessage'].get('mediaValue', None):
            self.replySrc = data.message.extensions['replyMessage']['mediaValue'].replace('_00.', '_hq.')
            self.replyId = data.message.extensions['replyMessage']['messageId']

        self.replyMsg = None
        if data.message.extensions and data.message.extensions.get('replyMessage', None) and data.message.extensions['replyMessage'].get('content', None):
            self.replyMsg = data.message.extensions['replyMessage']['content']
            self.replyId = data.message.extensions['replyMessage']['messageId']

        self.info: objects.Event = data