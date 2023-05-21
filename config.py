#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
#Get this value from https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "25666579"))
 #Get this value from https://my.telegram.org  
    API_HASH = os.environ.get("API_HASH", "d0119c6adf24fc7984e7052dd94cea7a")
 #Your bot token from @BotFather   
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6098827341:AAGjCjQP6WTBB9LtSCIfZ_RLCmNp4ITGGv0") 
#leave-it
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
#If you want to add a caption to the forwarded file, enter it here
    CAPTION = os.environ.get("CAPTION", "")
#Type Of filters (document , audio , photo , video , animation) else type empty to forward almost everything 
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
#Enter Your Telegram id with space, use one user at a time otherwise will get banned 
    OWNER_ID = os.environ.get("OWNER_ID", "5933750923").split()
    thumbnail_url="https://graph.org/file/1ad207a54e5ccc51f3243.jpg"
#Pyrogram string Seccion - https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1 or any updated pyrogram string session 
    SESSION = os.environ.get("SESSION", "BQGHpBMAqrRsVRzD876DCd8MTgr4AGnyxKQ6uveLWm6DvDbd4fXUyKtG3nY7n-B7KPG_GKWIvID1vF9m4Dr2Kd9OYDEo2rpsDLRyKqE11SSIRkexG7CBr5V9usHXqEbSPgSKVuIWtCIBIGcMHsK3dvkSTqo-TBI0YtztDRdNaVByos-uQLmx-AkRYhwCNemEcgP4SBQVD9u4yDVrkEUFu9HbjGvu3us7-9-Hpm-5phPZq-ljp2OUvdw40vLxeeFCnCC_VQXzClNjnCCeF6E-vYTsUzP197-LvxBDS-D42b71_NLwoUeggwm6dAqA5by7Pv_kUyelKfIG5dNdg4eMVBZZhiDgSAAAAAF0tZqFAA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
