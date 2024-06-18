

'''
This will have take some file from user and then process it and send the information back to user
so that user can also add something in the databse'''

import asyncio
import html

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import (ChatAction,
                                ParseMode)

from my_modules.abc_modules import useful_function_module
from my_modules.database_modules.database_module import (session, UserInformation)


def format_file_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 ** 2:
        size_in_kb = size_in_bytes / 1024
        return f"{size_in_kb:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        size_in_mb = size_in_bytes / (1024 ** 2)
        return f"{size_in_mb:.2f} MB"
    else:
        size_in_gb = size_in_bytes / (1024 ** 3)
        return f"{size_in_gb:.2f} GB"

# file_size_in_bytes = 10310
# formatted_size = format_file_size(file_size_in_bytes)
# print(f"File Size: {formatted_size}")





async def increase_one_file_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will execute when a single file or files will come directly without any capiton'''
    user = update.message.from_user
    document = update.message.document
    text = (f"Hello <b>{user.full_name}</b> You have send me a file,\n"
            f"YOur files information id is: <code>{document.file_id}</code>\n")
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = "You are not in database You Cannot Use it, send /help"
        await context.bot.send_message(user.id, text)
        return None
    if user_obj.is_allowed_ == 0:
        text = f"You are not allowed, you cannot use this bot is_allow = false"
        await context.bot.send_message(user.id, text)
        return None
    else:
        total_file = user_obj.total_files_
        text += (f"Till now You have send me <code>{total_file}</code> Number of files\n")
        user_obj.increase_total_files_(1)
        now_total_file = user_obj.total_files_
        text += (f"After you have send this file <code>{now_total_file}</code> Number of files")
        await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


async def increase_many_file_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    this will execute when a file have a caption
    if the file has a caption it will increase 5 token
    otherwise it will get the int from the caption and increase this
    '''
    user = update.message.from_user
    document = update.message.document
    caption_text = update.message.caption
    numbers = useful_function_module.find_int_from_string(caption_text)
    if numbers:
        number = numbers[0]
    else:
        await context.bot.send_message(user.id, text= f"You have not send me any valid int inside the string text")
        return None
    text = (f"This File have a Caption This need Minimum 5 Token to increase"
            f"Hello <b>{user.full_name}</b> You have send me a file,\n"
            f"Your files information id is: <code>{document.file_id}</code>\n")
    text = f" Owo You want to increase {number}\n" #first int will increase the value
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
    await context.bot.send_chat_action(user.id, ChatAction.UPLOAD_PHOTO)

    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = "You are not in database You Cannot Use it, send /help"
        await context.bot.send_message(user.id, text)

    if user_obj.is_allowed_ == 0:
        text = f"You are not allowed, you cannot use this bot is_allow = false"
        await context.bot.send_message(user.id, text)
        return None

    else:
        total_file = user_obj.total_files_
        text = (f"Till now You have send me <code>{total_file}</code> Number of files\n")
        user_obj.increase_total_files_(number)
        now_total_file = user_obj.total_files_
        text += (f"After you have send this file <code>{now_total_file}</code> Number of files")
        await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)




async def file_handle_with_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This is when a user send a file to the bot without any capiton
    When caption is there it will cost 10 files costs
    '''
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = f"You are not registered in our database or your data has been deleted. Please send /help"
        await context.bot.send_message(user.id, text)
        return
    
    if user_obj.is_allowed_ == 0:
        text = f"Hello <b>{html.escape(user.full_name)}</b> You are not allowed, you are blacklisted "
        text += f"You cannot use this bot features, you need to /activate_me to use this bot"
        await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
        return

    if user_obj.total_files_ <= 0:
        text = f"Hello {user.full_name}, you have already used all your files. You cannot go back to minus value. "
        text += f"Pls add some files count and then you can use it pls contact admins for increase or visit /help "
        text += f"Send /increase_total_files followed by the number to increase your file count first and then use"
        await context.bot.send_message(user.id, text)
        return None

    if user_obj.validity_ < update.message.date.replace(tzinfo= None):
        text = f"Your validity has expired. You cannot proceed.\n"
        text += f"Your Validity was: {user_obj.validity_}\n"
        text += f"You send response to me at {update.message.date.replace(tzinfo= None)}\n"
        text += f"Please contact admin to increase ur validity"
        await context.bot.send_message(user.id, text)
        return None
    
    if user_obj.validity_ < update.message.date.replace(tzinfo=None):
        text = (
            f"Your validity has expired. You cannot proceed.\n"
            f"Your Validity was: {user_obj.validity_}\n"
            f"You sent the response at: {update.message.date.replace(tzinfo=None)}\n"
            f"Please contact admin to increase your validity."
        )
        await context.bot.send_message(user.id, text)
        return None
    
    if update.message.caption:
        if user_obj.total_files_ < 10:
            text = f"Your File has a caption so it need 10 file point, but you have {user_obj.total_files_} So You cannot use more file at this moment pls increase some point /help"
            await context.bot.send_message(user.id, text)
            return
        user_obj.total_files_ -= 10
        session.commit()
        db_msg = f"Your Files has a caption so it cost 10 files point."
    else:
        user_obj.total_files_ -= 1
        session.commit()
        db_msg = f"Your File has not any capiton so it only cost 1 point."

    document = update.message.document
    text = (f"Please copy this file id and send me later to get this file which will send you"
            f"<blockquote><code>/get_file {document.file_id}</code></blockquote>This is the format you need to use.\n")
    # await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)

    doc_size_str = format_file_size(document.file_size)
    text += (f"Hello {html.escape(user.full_name)} You have send me a file with the size of "
            f"<blockquote>{doc_size_str}</blockquote> "
            f"This File is: <u>{document.file_name}</u>"
            )
    text = text + db_msg
    
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML,reply_to_message_id=update.message.id, disable_notification= True)




async def audio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This is executes when a user send a audio to bot, bot will send the file id
    Audio take minimmum 2 Point for no caption
    if caption it will take 20 point
    '''
    user = update.message.from_user

    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = f"You are not registered in our database or your data has been deleted. Please send /help"
        await context.bot.send_message(user.id, text)
        return
    
    if user_obj.is_allowed_ == 0:
        text = f"Hello <b>{html.escape(user.full_name)}</b> You are not allowed, you are blacklisted "
        text += f"You cannot use this bot to store the audio files, you need to /activate_me to use this bot"
        await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
        return

    if user_obj.total_files_ <= 0:
        text = f"Hello {user.full_name}, you have already used all your files. You cannot go back to minus value. "
        text += f"Pls add some files count and then you can use it pls contact admins for increase or visit /help "
        text += f"Send /increase_total_files followed by the number to increase your file count first and then use"
        await context.bot.send_message(user.id, text)
        return 

    if user_obj.validity_ < update.message.date.replace(tzinfo= None):
        text = f"Your validity has expired. You cannot proceed.\n"
        text += f"Your Validity was: {user_obj.validity_}\n"
        text += f"You send response to me at {update.message.date.replace(tzinfo= None)}\n"
        text += f"Please contact admin to increase ur validity"
        await context.bot.send_message(user.id, text)
        return 
    
    if user_obj.validity_ < update.message.date.replace(tzinfo=None):
        text = (
            f"Your validity has expired. You cannot proceed.\n"
            f"Your Validity was: {user_obj.validity_}\n"
            f"You sent the response at: {update.message.date.replace(tzinfo=None)}\n"
            f"Please contact admin to increase your validity."
        )
        await context.bot.send_message(user.id, text)
        return 
    
    if update.message.caption:
        if user_obj.total_files_ < 20:
            text = f"Your File has a caption so it need 20 file point, but you have {user_obj.total_files_} So You cannot use more file at this moment pls increase some point /help\n"
            await context.bot.send_message(user.id, text)
            return
        user_obj.total_files_ -= 20
        session.commit()
        db_msg = f"Your Audio File has a caption so it cost 20 files points."
    else:
        user_obj.total_files_ -= 2
        session.commit()
        db_msg = f"Your Audio File has not any capiton so it only cost 2 points."

    audio = update.message.audio

    text = (f"Please copy this audio file id and send me later to get this file which will send you"
            f"<blockquote><code>/get_audio {audio.file_id}</code></blockquote>This is the format you need to use.\n")

    aud_size_str = format_file_size(audio.file_size)
    text += (f"Hello {html.escape(user.full_name)} You have send me a audio file with the size of "
            f"<blockquote>{aud_size_str}</blockquote> "
            f"This File is: <u>{audio.file_name}</u>"
            )
    text = text + db_msg
    
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML,reply_to_message_id=update.message.id)










