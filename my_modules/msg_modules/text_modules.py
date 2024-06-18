
'''
in this scripts here i will use some fun which will does from teh text received
** import echo_fun **
** import all_edited_cmd **
** import all_edited_msg **

'''



from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode, ChatAction

print("This bot will run, for any sugesstion please messaage me in my telegram",
      "https://t.me/RanaUniverse")




# message_storage = {}
# async def save_text_html(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     '''This will save the user message in html mode and save in a dictionary'''
#     user = update.message.from_user
#     # message_storage = {}
#     message_storage[user.id] = update.message.text_html
#     text = f"Your This info has been saved\n\n"
#     text += f"{message_storage[user.id]}"
#     await context.bot.send_message(user.id, text)
    

    
# async def get_saved_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     '''This will retrieve and send back the stored message'''
#     user = update.message.from_user
#     if user.id in message_storage:
#         text = message_storage[user.id]
#         await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)
#     else:
#         await context.bot.send_message(user.id, "No saved message found.")



message_storage = {}

async def save_text_html(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will save the user message in HTML mode and save it in a dictionary'''
    user = update.message.from_user
    if user.id not in message_storage:
        message_storage[user.id] = []
    message_storage[user.id].append(update.message.text_html)
    text = f"<code>Your message has been saved.</code>\n\n"
    text += f"{update.message.text_html}"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


async def get_saved_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will retrieve and send back all stored messages for the user'''
    user = update.message.from_user
    if user.id in message_storage and message_storage[user.id]:
        text = "Your saved messages:\n\n"
        for idx, message in enumerate(message_storage[user.id], start=1):
            text += f"{idx}. {message}\n"
        await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)
    else:
        await context.bot.send_message(user.id, "No saved messages found.")







import datetime
import json
from pathlib import Path

async def get_dict_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will save the dictionary to a JSON file and send it to the admin user'''
    user = update.message.from_user
    folder = Path("RanaUniverse")
    path_to_file = folder / Path('message_storage.json')
    with path_to_file.open('w') as file:
        json.dump(message_storage, file, indent=4)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_count = len(message_storage)
    caption = f"Timestamp: <code>{timestamp}</code>\nTotal Keys: {key_count}"
    await context.bot.send_document(chat_id=user.id, document=path_to_file, caption=caption, parse_mode= "html")
















async def extra_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is execute when any extra /cmd came to bot'''
    user = update.message.from_user
    user_text = update.message.text
    text = f"Hello <b>{user.full_name}</b>, You have Send me <code>{user_text}</code>\n"
    text += f"I dont understand what you want to do with this cmd pls send /help"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)




import html
async def echo_fun_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will send the same msg send to the bot'''
    user = update.message.from_user
    user_text = update.message.text
    user_t_html = update.message.text_html
    print(user_text)
    print(user_t_html)
    text = (f"Hello {html.escape(user.full_name)}\n"
            f"Hello 2{user.full_name_html}"
            f"You have send me This Text Below:\n"
            f"<u>{html.escape(user_text)}</u>\n"
            f"<u>{user_t_html}</u>")
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)

async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will execute when a normal text come to user'''
    user = update.message.from_user
    text = update.message.text_html
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)

    text = f"123 Hello things THis my name is good things is my good thinkgs Hello <blockquote>Boss</blockquote>Thanks<blockquote><b>You</b></blockquote>are<blockquote>a good</blockquote> boy"
    # text = "abc"
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


async def all_edited_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This funciton is execute when any user edit his old msg or cmd to any new /cmd'''
    chat = update.edited_message.chat
    text = update.edited_message.text
    send_text = (f"You have send me:\n<b>{text}</b>"
                 f"Sorry i am not allowed to work on edited msg command"
                 f"Please send me a <code>/command</code> freshly")
    
    await context.bot.send_message(chat.id, text= send_text, parse_mode = ParseMode.HTML)




async def all_edited_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''After anyone will edit any msg this will execute'''
    chat = update.edited_message.chat
    text = update.edited_message.text
    send_text = (f"You Have send me {text}"
                 f"I cannot Help you in this edited msg")
    await context.bot.send_message(chat.id, send_text, parse_mode= ParseMode.HTML)



