
'''
Here i will defines the functions which i will call directly to exectute
so that it will perform some action when /help will came from user
** import help_cmd **
** import help_cmd_private **
** import help_cmd_group **

Just For Testing For Rana Universe
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''


from telegram import Update

from telegram.ext import ContextTypes
from telegram.constants import ParseMode




async def help_cmd_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''when a admin send /help'''
    user = update.message.from_user
    text = (f"You are a admin, the special command you can use are these,\n"
            f"/get_user_info_by_user_id: This need a user_id as a args to know the user information\n"
            f"/increase_the_user_files user_id token: to increase the files\n"
            f"/decrease_the_user_files user id token: to decrease the files\n"
            )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)



async def help_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''when a normal user send /help'''
    user = update.message.from_user
    text = (
        f"This is the HELP Section of this Bot- Rana Universe\n"
        f"To know the capabilities of this Bot Please Press This button\n\n"
    )
    text += (f"/add_me_to_database: Press This if you want to add yourself in our database\n"
             f"/get_my_info: Press This if you want to see YOur infromation like, your total file, validity\n"
             f"/activate_me: this if you want to activate ur data\n"
             f"/update_my_info: if you want to make recent chage of ur profile"
             f"/minus_one_value: this will -1 from the total files"
             f"/minus_many_value: Pass args as how many you want"
            #  f"/increase_total_files: With a args to increase your files count"
             f"/delete_my_data: to delete your data from our database\n"
    )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)





async def help_cmd_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is from get /help from any group'''
    chat = update.message.chat
    text = (f"You want to get help from this go to the private msg not in this:\n"
            f"<b>{chat.title}</b>")
    await context.bot.send_message(chat.id, text, parse_mode= "html")
    



