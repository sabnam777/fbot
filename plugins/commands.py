#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import sys
import asyncio
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
thumb_url = Config.thumbnail_url
#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('⚡️ Ak Imax 2.0 ⚡️', url='https://t.me/akimax3'),
        InlineKeyboardButton('⚡️ AK IMAX HUB ⚡️', url='https://t.me/akimaxmovies1')
        ],[
        InlineKeyboardButton('💡 Owner', url='https://t.me/BATMAN_0'),
        InlineKeyboardButton('📜 Support Group', url ='https://t.me/akimaxsupport')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
        thumb_url, 
        quote=True, 
        caption=Translation.START_TXT.format(message.from_user.first_name),
        reply_markup=reply_markup
        )

#===================Help Function===================#

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('💡 Developer', url='https://t.me/BATMAN_0'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
        thumb_url, 
        quote=True,
        caption=Translation.HELP_TXT,
        reply_markup=reply_markup
        )

#=================About Function==================#

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('⚡️ AK IMAX (Buy SouceCode)⚡️', url='https://t.me/AKImaxPremium2'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
        thumb_url, 
        quote=True, 
        caption=Translation.ABOUT_TXT,
        reply_markup=reply_markup,
        
    )

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restart on AK IMAX Server's.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>AK IMAX Server's restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
