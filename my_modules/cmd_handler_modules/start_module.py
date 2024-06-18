
'''
Here i will defines the functions which i will call directly to exectute
so that it will perform some action when /start will came from user

** import start **
** import start_cmd_private **
** import start_cmd_group **
** import start_cmd_channel **

Just For Testing For Rana Universe
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''

import asyncio
import datetime
import html
import random


from telegram import ForceReply
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode, ChatAction

from my_modules.abc_modules import bot_config
from my_modules.database_modules.database_module import UserInformation, session

from telegram import User


def user_name_spoiler(user_obj:User):
    full_name = user_obj.full_name
    no_tag = f"<tg-spoiler><u><b>{html.escape(full_name)}</b></u></tg-spoiler>"
    return no_tag


def name_bold_link(user_obj: User):
    '''This will return full name with link'''
    bold_name = f"<b><a href='tg://user?id={user_obj.id}'>{html.escape(user_obj.full_name)}</a></b>"
    return bold_name



async def get_user_bio_design(user, context: ContextTypes.DEFAULT_TYPE):
    '''Pass the user = update.message.from_user like thsi and it will get the bio and return after makeup'''
    user_bio = (await context.bot.get_chat(user.id)).bio
    design_str = f"Your Bio is:\n\n<b><tg-spoiler>{user_bio}</tg-spoiler></b>\n\n"
    return design_str




async def start_from_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is executes when a admin send /start'''
    user = update.message.from_user
    text = (f"You are a admin, Don't worry You own this bot you can use "
            f"this bot and more admin command to edit this databse the "
            f" list will seen below ")

    await context.bot.send_message(user.id, text, parse_mode="html")






async def start_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is normal /start when a user send this to bot'''
    user = update.message.from_user
    text = (
        f"This is Private MSG\n"
        f"Hello, {name_bold_link(user)}\n"
        f"Please wait for the response back to you in 1 Second"
    )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
    await context.bot.send_chat_action(user.id, ChatAction.TYPING)
    await asyncio.sleep(1)
    text = (
        f"<b>{bot_config.BOT_NAME}</b>\n\n"
        f"This bot is made for testing purpose, You need to send a file to me.\n"
        f"I will send you a <code>file_id</code>, which you will send me later and i will send you the file back.\n"
        f"But For this first you need to add yourself in our database and you will get information about your data"
        f"Different database cmd is here will add quickly in /help section /get_my_info 😵"
    )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)



async def start_cmd_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''in group /start'''
    user = update.message.from_user
    chat = update.message.chat
    text = (
        f"Hello {html.escape(user.full_name)} You have send me <code>/start</code> in {chat.title} Group "
        f"But i cannot assist you in this group, pls return to private chat and send me <code>/start</code> again"
    )
    await context.bot.send_message(chat.id, text, parse_mode= ParseMode.HTML)



async def start_cmd_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.channel_post.chat
    name_of_sender = update.channel_post.author_signature

    channel_des = (await context.bot.get_chat(chat.id)).description
    text = (
        f"This is Channel Post For: "
        f"{chat.title}\n"
        f"This has written by <b>{name_of_sender}</b>\n"
    )
    text += (
        f"Description of This Channel is:\n"
        f"{channel_des}"
    )
    await context.bot.send_message(chat.id, text, parse_mode= "html")






