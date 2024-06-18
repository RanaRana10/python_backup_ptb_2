'''
This is the module where i will store the func which will allow the user to get his file back
'''

import asyncio
import datetime
import html

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import (ChatAction, ParseMode)

from my_modules.abc_modules import bot_config
from my_modules.database_modules.database_module import (UserInformation,
                                                         session)


async def get_file_123(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    if len(context.args) != 1:
        await context.bot.send_message(user.id, f"Please send me in correct format")
        return
    file_id = context.args[0]
    text = f"Hello <b>{html.escape(user.full_name)}</b> This is Your document\n\n"
    abc = await context.bot.send_document(user.id, file_id, caption= text, parse_mode= ParseMode.HTML)
    # Below lines are for check the doc is ok or not
    await asyncio.sleep(1)
    file_name = abc.document.file_name
    await context.bot.edit_message_caption(user.id, abc.id, caption= text + "<code>" + file_name + "</code>", parse_mode= ParseMode.HTML)
    # This is just for edit
    




async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    if len(context.args) != 1:
        await context.bot.send_message(user.id, f"Please send me in the correct format <code>/get_file file_id</code>")
        return
    
    file_id = context.args[0]
    text_document = f"Hello <b>{html.escape(user.full_name)}</b> This is your document\n\n"
    text_photo = f"Hello <b>{html.escape(user.full_name)}</b> Please Send me a correct document file id."
    error_admin_msg = f"There was a problem when {user.full_name} sent the message: '{update.message.text}'"
    
    try:
        msg_obj = await context.bot.send_document(user.id, file_id, caption=text_document, parse_mode=ParseMode.HTML)
    except Exception as e1:
        print(f"Send Document from the file id is not possible due to {e1}")
        try:
            await context.bot.send_photo(user.id, bot_config.SOMETHING_WRONG_IMAGE_ID, caption=text_photo, parse_mode=ParseMode.HTML)
        except Exception as e2:
            print(f"Send photo is not possible due to {e2}")
            try:
                await context.bot.send_message(bot_config.ADMIN_IDS[0],error_admin_msg)
            except Exception as e3:
                print(f"An error occurred at {datetime.datetime.now()} when {user.full_name} sent a message: '{update.message.text}'. Additional error: {e3}")
    else:
        await context.bot.edit_message_caption(user.id, msg_obj.id, caption= text_document + f"{msg_obj.document.file_name}")
    finally:
        print("Finally part is executing")




async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is for getting audio from the bot when user send /get_audio'''
    user = update.message.from_user
    if len(context.args) != 1:
        await context.bot.send_message(user.id, "Please send me in the correct format to get the audio")
        return
    
    file_id = context.args[0]
    text_audio = f"Hello <b>{html.escape(user.full_name)}</b> This is your Audio File\n\n"
    text_photo = f"Hello <b>{html.escape(user.full_name)}</b> Please Send me a correct audio file id."
    error_admin_msg = f"There was a problem when {user.full_name} sent the message: '{update.message.text}'"
    
    try:
        msg_obj = await context.bot.send_document(user.id, file_id, caption=text_audio, parse_mode=ParseMode.HTML)
        msg_obj = await context.bot.send_audio(user.id, file_id, caption=text_audio, parse_mode=ParseMode.HTML)
    except Exception as e1:
        print(f"Send Document from the file id is not possible due to {e1}")
        try:
            await context.bot.send_photo(user.id, bot_config.SOMETHING_WRONG_IMAGE_ID, caption=text_photo, parse_mode=ParseMode.HTML)
        except Exception as e2:
            print(f"Send photo is not possible due to {e2}")
            try:
                await context.bot.send_message(bot_config.ADMIN_IDS[0],error_admin_msg)
            except Exception as e3:
                print(f"An error occurred at {datetime.datetime.now()} when {user.full_name} sent a message: '{update.message.text}'. Additional error: {e3}")
    else:
        await context.bot.edit_message_caption(user.id, msg_obj.id, caption= text_audio + f"{msg_obj.document.file_name}")
    finally:
        print("Finally part is executing")


    




