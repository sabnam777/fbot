#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
#Get this value from https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", ""))
 #Get this value from https://my.telegram.org  
    API_HASH = os.environ.get("API_HASH", "")
 #Your bot token from @BotFather   
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
#leave-it
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
#If you want to add a caption to the forwarded file, enter it here
    CAPTION = os.environ.get("CAPTION", "")
#Type Of filters (document , audio , photo , video , animation) else type empty to forward almost everything 
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
#Enter Your Telegram id with space, use one user at a time otherwise will get banned 
    OWNER_ID = os.environ.get("OWNER_ID", "").split()
    thumbnail_url="https://graph.org/file/1ad207a54e5ccc51f3243.jpg"
#Pyrogram string Seccion - https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1 or any updated pyrogram string session 
    SESSION = os.environ.get("SESSION", "")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
