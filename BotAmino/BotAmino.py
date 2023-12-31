
import requests
import os
import ujson as json
from pymongo import MongoClient
import urllib.parse
import ssl
from time import sleep as slp
from sys import exit
from json import dumps
from pathlib import Path
from threading import Thread
# from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from uuid import uuid4

from amino import Client
from .commands import *
from .extensions import *
from .Bot import Bot
import json
import ast
proxlist=[]
proxy = open("rproxy.txt", "r").read().splitlines()
for i in proxy:
	proxlist.append(i)

pro=proxlist[0]
proxiess={"http":f"socks5://{pro}@185.199.229.156:7492","https":f"socks5://{pro}@185.199.229.156:7492"}
monk=[]
mon= open("mongo.txt", "r").read().splitlines()
for i in mon:
	monk.append(i)

mongos=monk[0]
mongo=MongoClient(f"mongodb+srv://{mongos}/?retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://kiritovayux:aminobc@cluster0.emr3bjf.mongodb.net/?retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://lofis:lofi@cluster0.qnib4jt.mongodb.net/?retryWrites=true&w=majority")
#mongo= MongoClient("mongodb+srv://cartoons:cwaamino@cluster0.3nela.mongodb.net/?retryWrites=true&w=majority")
db=mongo['comid']

test_1=db['list2']

path_utilities = "utilities"
path_amino = f'{path_utilities}/amino_list'
path_client = "client.txt"
NoneType = type(None)

with suppress(Exception):
    for i in (path_utilities, path_amino):
        Path(i).mkdir(exist_ok=True)

def print_exception(exc):
    print(repr(exc))

class BotAmino(Command, Client, TimeOut, BannedWords):
    def __init__(self, email: str = None, password: str = None, sid: str = None,proxies=proxiess, deviceId="191F0EA15821FD7A1A577A0ABFFAE9FD2C5804DE080BA97CBCABB8E7E2EDB0B75FFD0E6AF92D9895D2", certificatePath: str = None):
        Command.__init__(self)
        Client.__init__(self, proxies=proxies, deviceId=deviceId, certificatePath=certificatePath)

        if email and password:
            self.login(email=email, password=password)
        elif sid:
            self.login_sid(SID=sid)
        else:
            try:
                with open(path_client, "r") as file_:
                    para = file_.readlines()
                self.login(email=para[0].strip(), password=para[1].strip())
            except FileNotFoundError:
                with open(path_client, 'w') as file_:
                    file_.write('email\npassword')
                print("Please enter your email and password in the file client.txt")
                print("-----end-----")
                exit(1)

        self.communaute = {}
        self.botId = self.userId
        self.len_community = 0
        self.perms_list = ["501cc6f5-1e38-4a22-9df5-cd0625b0205e","5095b75f-b92d-4d66-8ebd-9072751443dd","c928fe25-9be2-414f-8a89-d51616999faa","816d376a-29f3-4964-aa52-998517905c2b","6bba6f1b-f97d-44d6-bdb5-402d3035a060","1ff6d597-fcca-4bce-b3f6-ad7e6d79297e","172eee02-5ef8-497e-9082-e36a38e13dac","9139234a-58cc-470b-9bc0-330d023ee31a"]
        self.prefix = "!"
        self.activity = False
        self.wait = 0
        self.bio = None
        self.self_callable = False
        self.no_command_message = ""
        self.spam_message = ""
        self.lock_message = "Command locked sorry"
        self.launched = False

    def tradlist(self, sub):
        sublist = []
        for elem in sub:
            with suppress(Exception):
                val = self.get_from_code(f"http://aminoapps.com/u/{elem}").objectId
                sublist.append(val)
                continue
            sublist.append(elem)
        return sublist

    def send_data(self, data):
        self.send(data)

    def add_community(self, comId):
        self.communaute[comId] = Bot(self, comId, self.prefix, self.bio, self.activity)

    def get_community(self, comId):
        return self.communaute[comId]

    def is_it_bot(self, uid):
        return uid == self.botId and not self.self_callable

    def is_it_admin(self, uid):
        return uid in self.perms_list

    def get_wallet_amount(self):
        return self.get_wallet_info().totalCoins

    def generate_transaction_id(self):
        return str(uuid4())

    def start_screen_room(self, comId: str, chatId: str, joinType: int=1):
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = dumps(data)
        self.send(data)

        data = {
            "o": {
                "ndcId": int(comId),
                "threadId": chatId,
                "joinRole": joinType,
                "channelType": 5,
                "id": "2154531"  # Need to change?
            },
            "t": 108
        }
        data = dumps(data)
        self.send(data)

    def join_screen_room(self, comId: str, chatId: str, joinType: int=1):
        data = {
            "o":
                {
                    "ndcId": int(comId),
                    "threadId": chatId,
                    "joinRole": 2,
                    "id": "72446"
                },
            "t": 112
        }
        data = dumps(data)
        self.send(data)

    def start_voice_room(self, comId: str, chatId: str, joinType: int=1):
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = dumps(data)
        self.send(data)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "channelType": 1,
                "id": "2154531"  # Need to change?
            },
            "t": 108
        }
        data = dumps(data)
        self.send(data)

    def end_voice_room(self, comId: str, chatId: str, joinType: int = 2):
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = dumps(data)
        self.send(data)

    def show_online(self, comId):
        data = {
            "o": {
                "actions": ["Browsing"],
                "target": f"ndc://x{comId}/",
                "ndcId": int(comId),
                "id": "82333"
            },
            "t":304}
        data = dumps(data)
        slp(2)
        self.send(data)

    def upload_bubble(self,file,comId):
        data=file
        response = requests.post(f"https://service.narvii.com/api/v1/x{comId}/s/chat/chat-bubble/templates/107147e9-05c5-405f-8553-af65d2823457/generate", data=data, headers=self.headers)
        bid=json.loads(response.text)['chatBubble']['bubbleId']
        print(bid)
        response = requests.post(f"https://service.narvii.com/api/v1/x{comId}/s/chat/chat-bubble/{bid}", data=data, headers=self.headers)
        if response.status_code !=200:
            return json.loads(response.text)
        else: return bid

    def check(self, args, *can, id_=None):
        id_ = id_ if id_ else args.authorId
        foo = {'staff': args.subClient.is_in_staff,
               'bot': self.is_it_bot,'admin' : self.is_it_admin}

        for i in can:
            if foo[i](id_):
                return True

    def check_all(self):
        t = open('comid.txt','r')
        lists=[]
        for m in t.read().splitlines():
        	temp=m
        	lists.append(int(temp))
        amino_list = self.sub_clients()
        for com in lists:
            try:
                self.communaute[com].check_in()
            except Exception:
                pass

    def threadLaunch(self, commu, passive: bool=False):
        self.communaute[commu] = Bot(self, commu, self.prefix, self.bio, passive)
        slp(30)
        #if passive:
           # self.communaute[commu].passive()

    def launch(self, passive: bool = False):
        #amino_list = self.sub_clients()
        lists=[]
        results=test_1.find({},{'_id': 0})
        for i in results:
        #	print(i)
        	y=i["comid"]
        	lists.append(int(y))
        print(lists)
        #for commu in lists:
        	#self.threadLaunch(commu,passive)
        
        [Thread(target=self.threadLaunch, args=[commu, passive]).start() for commu in lists]

        if self.launched:
            return

        if self.categorie_exist("command") or self.categorie_exist("answer"):
            self.launch_text_message()

        if self.categorie_exist("on_member_join_chat"):
            self.launch_on_member_join_chat()

        if self.categorie_exist("on_member_leave_chat"):
            self.launch_on_member_leave_chat()

        if self.categorie_exist("on_other"):
            self.launch_other_message()

        if self.categorie_exist("on_remove"):
            self.launch_removed_message()

        if self.categorie_exist("on_delete"):
            self.launch_delete_message()

        if self.categorie_exist("on_all"):
            self.launch_all_message()

        if self.categorie_exist("on_event"):
            self.launch_on_event()

        self.launched = True

    def single_launch(self, commu, passive: bool = False):
        amino_list = self.sub_clients()
        self.len_community = len(amino_list.comId)
        Thread(target=self.threadLaunch, args=[commu, passive]).start()

        if self.launched:
            return

        if self.categorie_exist("command") or self.categorie_exist("answer"):
            self.launch_text_message()

        if self.categorie_exist("on_member_join_chat"):
            self.launch_on_member_join_chat()

        if self.categorie_exist("on_member_leave_chat"):
            self.launch_on_member_leave_chat()

        if self.categorie_exist("on_other"):
            self.launch_other_message()

        if self.categorie_exist("on_remove"):
            self.launch_removed_message()

        if self.categorie_exist("on_delete"):
            self.launch_delete_message()

        if self.categorie_exist("on_all"):
            self.launch_all_message()

        self.launched = True

    def message_analyse(self, data, type):
        try:
            commuId = data.comId
            subClient = self.get_community(commuId)
        except Exception:
            return

        args = Parameters(data, subClient)
        Thread(target=self.execute, args=[type, args, type]).start()

    def on_member_event(self, data, type):
        try:
            commuId = data.comId
            subClient = self.get_community(commuId)
        except Exception:
            return

        args = Parameters(data, subClient)

        if not self.check(args, "bot"):
            Thread(target=self.execute, args=[type, args, type]).start()

    def launch_text_message(self):
        @self.event("on_text_message")
        def on_text_message(data):
            try:
                commuId = data.comId
                subClient = self.get_community(commuId)
            except Exception:
                return

            args = Parameters(data, subClient)

            if "on_message" in self.commands.keys():
                Thread(target=self.execute, args=["on_message", args, "on_message"]).start()


            if not self.check(args, 'staff', 'bot','admin') and subClient.banned_words:
                self.check_banned_words(args)
                #self.check_ban_words(args)
            #if args.authorId in subClient.muted_users and args.comId in subClient.comIds:
            	#subClient.delete_message(chatId=args.chatId,messageId=args.messageId,asStaff=True,reason="muted user")
            if not self.timed_out(args.authorId) and args.message.startswith(subClient.prefix) and not self.check(args,"staff","admin", "bot"):
                subClient.send_message(args.chatId, self.spam_message)
                return

            elif "command" in self.commands.keys() and args.message.startswith(subClient.prefix) and not self.check(args, "bot"):
                print(f"{args.author} : {args.message}")
                command = args.message.lower().split()[0][len(subClient.prefix):]

                if command in subClient.locked_command and not self.check(args,"admin"):
                    subClient.send_message(args.chatId, self.lock_message)
                    return

                args.message = ' '.join(args.message.split()[1:])
                self.time_user(args.authorId, self.wait)
                if command.lower() in self.commands["command"].keys():
                    Thread(target=self.execute, args=[command, args]).start()

                elif self.no_command_message:
                    subClient.send_message(args.chatId, self.no_command_message)
                return

            elif "answer" in self.commands.keys() and args.message.lower() in self.commands["answer"] and not self.check(args, "bot"):
                print(f"{args.author} : {args.message}")
                self.time_user(args.authorId, self.wait)
                Thread(target=self.execute, args=[args.message.lower(), args, "answer"]).start()
                return

    def launch_other_message(self):
        for type_name in ("on_strike_message", "on_voice_chat_not_answered",
                          "on_voice_chat_not_cancelled", "on_voice_chat_not_declined",
                          "on_video_chat_not_answered", "on_video_chat_not_cancelled",
                          "on_video_chat_not_declined", "on_voice_chat_start", "on_video_chat_start",
                          "on_voice_chat_end", "on_video_chat_end", "on_screen_room_start",
                          "on_screen_room_end", "on_avatar_chat_start", "on_avatar_chat_end"):

            @self.event(type_name)
            def on_other_message(data):
                self.message_analyse(data, "on_other")

    def launch_all_message(self):
        for x in (self.chat_methods):
            @self.event(self.chat_methods[x].__name__)
            def on_all_message(data):
                self.message_analyse(data, "on_all")

    def launch_delete_message(self):
        @self.event("on_delete_message")
        def on_delete_message(data):
            self.message_analyse(data, "on_delete")

    def launch_removed_message(self):
        for type_name in ("on_chat_removed_message", "on_text_message_force_removed","on_delete_message"):
            @self.event(type_name)
            def on_chat_removed(data):
                self.message_analyse(data, "on_remove")

    def launch_on_member_join_chat(self):
        @self.event("on_group_member_join")
        def on_group_member_join(data):
            self.on_member_event(data, "on_member_join_chat")

    def launch_on_member_leave_chat(self):
        @self.event("on_group_member_leave")
        def on_group_member_leave(data):
            self.on_member_event(data, "on_member_leave_chat")

    def launch_on_event(self):
        for k, v in self.commands["on_event"].items():
            @self.event(k)
            def _function(data):
                v(data)
