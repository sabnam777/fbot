#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa
#script received by @nobody_ismy_name
import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation
import traceback
if Config.FILTER_TYPE == "document":
  FILTER=enums.MessagesFilter.DOCUMENT
elif Config.FILTER_TYPE == "empty":
  FILTER=enums.MessagesFilter.EMPTY
elif Config.FILTER_TYPE == "photo":
  FILTER=enums.MessagesFilter.PHOTO
elif Config.FILTER_TYPE == "video":
  FILTER=enums.MessagesFilter.VIDEO
elif Config.FILTER_TYPE == "audio":
  FILTER=enums.MessagesFilter.AUDIO

IS_CANCELLED = False
lock = asyncio.Lock()
#print (FILTER)
@Client.on_callback_query(filters.regex(r'^start_public$'))
async def pub_(bot, message):
    
    global files_count, IS_CANCELLED
    await message.answer()
    await message.message.delete()
    from plugins.public import FROM, TO, SKIP, LIMIT
    if lock.locked():
        await message.message.reply_text('__Previous process running 🥺..__', parse_mode="md")
    else:
        #print (message.message)
        m = await message.message.reply_text(
            text="<i>Processing...⏳</i>"
        )
        total_files=0
        async with lock:
            try:
                pling=0
                print (FILTER) 
                print (type(FILTER))
                async for message in bot.USER.search_messages(chat_id=int(FROM),offset=int(SKIP),limit=int(LIMIT),filter=FILTER):
                    if IS_CANCELLED:
                        IS_CANCELLED = False
                        break
                    try:
                        if message.video:
                            file_name = message.caption
                        elif message.document:
                            file_name = message.caption
                        elif message.audio:
                            file_name = message.audio.file_name
                        else:
                            file_name = None
                        await bot.USER.copy_message(
                            chat_id=TO,
                            from_chat_id=FROM,
                            #caption=Translation.CAPTION.format(file_name),
                            message_id=message.id
                        )
                        total_files += 1
                        await asyncio.sleep(6)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        await bot.USER.copy_message(
                            chat_id=TO,
                            from_chat_id=FROM,
                            #caption=Translation.CAPTION.format(file_name),
                            message_id=message.id
                        )
                        total_files += 1
                        await asyncio.sleep(10)
                    except Exception as e:
                        print(e)
                        pass
                    pling += 1
                    if pling == 10: 
                        buttons = [[
                            InlineKeyboardButton('Cancel🚫', 'terminate_frwd')
                        ]]
                        reply_markup = InlineKeyboardMarkup(buttons)
                        await m.edit_text(
                            text=f'<b><u>FORWARD STATUS</b></u>\n\n<b>Succefully forwarded file count :</b> <code>{total_files} files</code>',
                            reply_markup=reply_markup, 
                            
                        )
                        pling -= 10
            except Exception as e:
                traceback.print_exc()
                print(e)
                await m.edit_text(f'Error: {e}')
            else:
                buttons = [[
                    InlineKeyboardButton('⚡️ AK IMAX HUB ⚡️', url='https://t.me/Akimaxmovies1')
                    ],[
                    InlineKeyboardButton('📡 Update Channel', url='https://t.me/Akimaxsupport')
                ]]
                reply_markup = InlineKeyboardMarkup(buttons)
                await m.edit_text(
                    text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded Files:-</b> <code>{total_files}</code> <b>Files</b>\n<b>Thanks For Using AK IMAX services❤️</b>",
                    reply_markup=reply_markup,
                    )
      
@Client.on_callback_query(filters.regex(r'^terminate_frwd$'))
async def terminate_frwding(bot, update):
    global IS_CANCELLED
    IS_CANCELLED = True
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
