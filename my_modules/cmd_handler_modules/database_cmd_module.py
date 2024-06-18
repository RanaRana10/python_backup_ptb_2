

'''
This is for some specefic type of cmd handler update
/add_me_to_databse:
/get_my_info:
/delete_my_data:
/activate_me:
'''

from pathlib import Path #this is here used for send the file form my storage
import asyncio
import datetime
import html # This is for make my full name to escape < > 
import random

from telegram import Update
from telegram.ext import ContextTypes

from telegram.constants import (ChatAction,
                                ParseMode
                                )


from my_modules.abc_modules import bot_config
from my_modules.database_modules.database_module import (UserInformation,
                                                         session)
from my_modules.cmd_handler_modules import start_module



async def send_db_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    - /send_db_files PASSWORD
    When a user will send this cmd it will check the args for the password
    and then it will check again the user name and id
    if both matches then it will send the current .db file to user back
    '''

    user = update.message.from_user
    if user.id not in bot_config.ADMIN_IDS:
        text = f"You are not a admin, You cannot get this .db file ❌❌❌"
        await context.bot.send_message(user.id, text)
        return None



async def send_db_no_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    - /send_db_files 
    this will trigger when no args is present and from admin
    '''
    user = update.message.from_user
    text = f"Sorry Admin You have not passed the password pls send in this format\n"
    text += "/send_db_files PASSWORD"
    await context.bot.send_message(user.id, text)




async def send_db_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    this is second
    - /send_db_files PASSWORD
    this will trigger only when the args = true means i not check the args present here
    admin only can trigger so checking the admin here is not need
    '''
    user = update.message.from_user

    password = context.args[0]
    if password != bot_config.DB_FILE_PASSWORD:
        text = f"You have press the wrong password Please try again"
        await context.bot.send_message(user.id, text)
        return
    text = (f"You have Given the correct data, wait sometime, i am fetching "
            f"the current .db file and sending you after 5 second")
    await context.bot.send_message(user.id, text)
    await asyncio.sleep(5)
    await context.bot.send_chat_action(user.id, "upload_document")
    file_path = Path("RanaUniverse") / "database_file.db"
    caption_str = f"Hello {user.full_name} I have send you the database file"
    await context.bot.send_document(user.id, file_path, caption= caption_str)




async def add_me_to_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will add the user if he is not already added'''
    user = update.message.from_user
    if user.id in bot_config.ADMIN_IDS:
        text = f"You are admin you can control all of the users you not need this for urself. "
        text += f"You dont need thsi command, but still i am trying adding you in the database"
        await context.bot.send_message(user.id, text)
        
    his_row_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()

    if his_row_obj:
        row_id_ = his_row_obj.id_
        text = (f"You are already in our database with {row_id_}, " #This is sensetive i will not use this directly
                f"To know your full info, /get_my_info"
                )
    else:
        send_time = update.message.date.replace(tzinfo= None)
        new_user_obj = UserInformation(user.id, user.username, user.full_name, False, send_time, 0)
        inserted_id_ = new_user_obj.add_user_return_id_()
        text = (f"You r a new user you has just inserted in our database with the row id_ <b>{inserted_id_}</b> "
                f"To know about your information send me /get_my_info")
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)





async def get_my_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Retrieve and display user information from the database."""
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()

    if user_obj:
        # username = f"@{user_obj.username_}" if user_obj.username_ else "Not available"
        text = (f"Your information:\n"
                f'- Username: {f"@<b>{user_obj.username_}</b>" if user_obj.username_ else "Not available ❌"}\n'
                f"- Full Name: {user_obj.full_name_}\n"
                f"- Allowed Status: {'Allowed' if user_obj.is_allowed_ else 'Not Allowed'}\n"
                f"- Validity Until: {user_obj.validity_}\n"
                f"- Total Files Left: {user_obj.total_files_}\n")
    else:
        text = (f"You are not in our database, maybe you are removed or not registered"
                f" Please open /help to see more info")

    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


 
async def update_my_info(update:Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    When user will send /update_my_info 
    This will update his latest name and username from tg and insert
    '''
    user = update.message.from_user
    row_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not row_obj:
        text = f"You are not in our database, send /help"
        context.bot.send_message(user.id, text)
        return
    else:
        text = f"Your old data is: Username & FullName {row_obj.username_, row_obj.full_name_}\n"
        row_obj.username_ = user.username
        row_obj.full_name_ = user.full_name
        session.commit()
        text += f"Your New Updated Data is: Username & FullName {row_obj.username_, row_obj.full_name_}\n"
        await context.bot.send_message(user.id, text)



async def activate_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is for if the user wants to make the column is_allowed_ from false to true, i.e., 0 to 1'''
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = (f"You are not registered in our database or your data has been deleted. So you "
                f"cannot activate yourself Please send /help")
        await context.bot.send_message(user.id, text)
        return
    if user_obj.is_allowed_ == 0:
        user_obj.is_allowed_ = 1
        session.commit()
        text = f"Your account has been activated Now at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ."
        await context.bot.send_message(user.id, text)
        await context.bot.send_message(bot_config.ADMIN_GROUPS_ID[0], text= f"<a href='tg://user?id={user.id}'>{html.escape(user.full_name)}</a> Has just changed his is_allowed status to YES.", parse_mode= ParseMode.HTML)
        return
    if user_obj.is_allowed_ == 1:
        text = "You are already activated.✅✅✅"
        await context.bot.send_message(user.id, text)
        return


async def delete_my_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This executes when the user sends this cmd, and it needs admin activation'''
    user = update.message.from_user
    text = (
        f"You want to delete your info from this service to stop using this bot. "
        f"Your request has been successfully forwarded to the administrators.\n"
        f"We will let you know after this request has been successful or not. "
        f"Because this request requires an admin to check."
    )

    await context.bot.send_message(user.id, text)
    admin_group_id = bot_config.ADMIN_GROUPS_ID[0]  # This is the group id
    await context.bot.forward_message(admin_group_id, user.id, update.message.id)
    await asyncio.sleep(1)
    
    text = (
        f"This user whose name is: <a href='tg://user?id={user.id}'>"
        f"<b><u>{html.escape(user.full_name)}</u></b></a> wants to delete "
        f"his data from the database. Please check this with appropriate functions."
    )
    await context.bot.send_message(admin_group_id, text, parse_mode=ParseMode.HTML)

    



async def activate_me_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is for if the user wants to make the column is_allowed_ from false to true, i.e., 0 to 1'''
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = f"You are not registered in our database or your data has been deleted. Please send /help"
        await context.bot.send_message(user.id, text)
        return
    if user_obj.is_allowed_ == 0:
        user_obj.is_allowed_ = 1
        session.commit()  # Save the changes to the database
        text = "Your account has been activated."
        await context.bot.send_message(user.id, text)
    else:
        text = "You are already activated."
        await context.bot.send_message(user.id, text)
    await context.bot.send_message(bot_config.ADMIN_IDS[0], text= f"{user.full_name} Has just changed his is_allowed status")



async def delete_my_data_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Delete user data from the database."""
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if user_obj:
        text = f"{user_obj}: this information will delete"
        await context.bot.send_message(user.id, text)
        deletion_info= user_obj.delete_user_row()
        if deletion_info:
            text = "Your data has been successfully deleted from our database."
        else:
            text = "An error occurred while deleting your data from the database."
    else:
        text = "You are not registered in our database."
    await context.bot.send_message(user.id, text)





async def minus_one_value(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /minus_one_value
    if any user will send this it will go to the database 
    then check for token and then check for the validity is available or not
    This fun wil check some and reduce the value is ongoing
    """
    user = update.message.from_user
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    await context.bot.send_chat_action(user.id, ChatAction.TYPING)
    if not user_obj:
        text = f"You are not allowed search /help and add yourself in this base"
        await context.bot.send_message(user.id, text)
        return
    
    if user_obj.is_allowed_ == 0:
        text = f"You are not allowed, pls activater yourself in /activate_me"
        await context.bot.send_message(user.id, text)
        return

    if user_obj.total_files_ <= 0:
        text = f"Hello {user.full_name}, you have already used all your files. You cannot go back to minus value. "
        text += f"Pls add some files count and then you can use it pls contact admins for increase or visit /help"
        await context.bot.send_message(user.id, text)
        return

    if user_obj.validity_ < update.message.date.replace(tzinfo= None):
        text = f"Your validity has expired. You cannot proceed.\n"
        text += f"Your Validity was: {user_obj.validity_}\n"
        text += f"You send response to me at {update.message.date.replace(tzinfo= None)}"
        await context.bot.send_message(user.id, text)
        return
    
    text = (f"Your old files value was, {user_obj.total_files_}\n")
    user_obj.total_files_ -= 1
    session.commit()
    text += (f"Your New files value is, {user_obj.total_files_}")
    await context.bot.send_message(user.id, text)


async def minus_many_value(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - /minus_many_value Integer
    if any user will send this with only 1 args it will go to the database 
    then check for token and then check for the validity is available or not
    This fun wil check some and reduce the value is ongoing
    """
    user = update.message.from_user
    how_many = context.args[0]
    try:
        how_many = int(how_many)
    except ValueError:
        text = (
            f"{html.escape(user.full_name)}, you provided an invalid input. "
            f"Please provide a valid integer. You sent me "
            f"<u><b>{how_many}</b></u>, but I need an integer value, e.g., "
            f"<code>/minus_many_value {random.randint(1, 100)}</code>"
        )
        await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
        return
    if how_many < 0:
        text = "Hello Genious Boss, You are not allowd to increaase the file by using this cmd 🤣🤣🤣"
        await context.bot.send_message(user.id, text)
        return
    
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user.id).first()
    if not user_obj:
        text = f"You are not allowed search /help and add yourself in this base"
        await context.bot.send_message(user.id, text)
        return

    if user_obj.is_allowed_ == 0:
        text = f"You are banned to use this bot pls contact admin"
        await context.bot.send_message(user.id, text)
        return
    
    if user_obj.total_files_ < how_many:
        text = "You cannot have negative total files count."
        text += f"You send {how_many} But you have total {user_obj.total_files_}"
        await context.bot.send_message(user.id, text)
        return


    time_now = update.message.date.replace(tzinfo= None)
    if user_obj.validity_ < time_now:
        text = (
            f"Your validity has expired. You cannot proceed.\n"
            f"Your Validity was: {user_obj.validity_}\n"
            f"You sent a response to me at {time_now}"
        )
        await context.bot.send_message(user.id, text)
        return
    text = (
        f"You are going to change your files at "
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Your old files value was: {user_obj.total_files_}\n"
    )
    user_obj.total_files_ -= how_many
    session.commit()
    text += (f"Your New files value is, {user_obj.total_files_}\n")
    await context.bot.send_message(user.id, text)



async def minus_many_value_wrong(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''2nd logic This will trigger when user forgets to pass the args'''
    user = update.message.from_user
    text = (f"You have forget to passed the args value like how many"
            f" you want to decrease example: <code>/minus_many_value {random.randint(1,100)}</code>")
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)




async def get_user_info_by_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This will trigger when admin sends 
    - /get_user_info_by_id user_id
    '''
    user = update.message.from_user
    if user.id not in bot_config.ADMIN_IDS:
        text = "You are not an admin, You cannot get user's information 😢😢😢"
        await context.bot.send_message(chat_id=user.id, text=text)
        return

    # Check if an argument is not provided
    if not context.args:
        text = "Please provide a user ID."
        await context.bot.send_message(chat_id=user.id, text=text)
        return

    try:
        user_id = int(context.args[0])
    except ValueError:
        text = "Invalid user ID provided. Please enter a valid numeric user ID."
        await context.bot.send_message(chat_id=user.id, text=text)
        return

    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user_id).first()
    if not user_obj:
        text = f"The user ID you provided, <a href='tg://user?id={user_id}'><u>{user_id}</u></a>, is not present in our database."
        await context.bot.send_message(chat_id=user.id, text=text, parse_mode=ParseMode.HTML)
        return

    text = (f"<a href='tg://user?id={user_id}'><b>This user</b></a> Press Here\n"
            f"Username: <b>{user_obj.username_ if user_obj.username_ else 'No Username in database'}</b>\n"
            f"Full Name: {user_obj.full_name_}\n"
            f"Allowed Status: {'Allowed' if user_obj.is_allowed_ else 'Not Allowed'}\n"
            f"Validity: {user_obj.validity_}\n"
            f"Total Files: {user_obj.total_files_}\n")
    
    await context.bot.send_message(chat_id=user.id, text=text, parse_mode=ParseMode.HTML)



async def increase_total_files_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is executes when a person wants to increase his total files limit'''
    user = update.message.from_user
    
    if not context.args:
        await context.bot.send_message(user.id, "You must provide a number after the cmd to increase your file limit.")
        return None
    try:
        value = int(context.args[0])
    except ValueError:
        await context.bot.send_message(user.id, "Please provide a valid number to increase your file limit.")
        return None
    text = (f"You wants to increase <code>{value}</code> amount of files to use later"
            f"Please wait your files need to increase but need a admin verification, so they will accept the "
            f"Your request and then your data will increase, after the accept by admin, i will msg u")
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)
    text_admin = (f"{start_module.name_bold_link(user)} Wants to increase his files to "
                  f"<b><u>{value}</u></b>. Check This see the user info below \n")
    text_admin += (f"User Id: <code>{user.id}</code>\n"
                   f"Time of Req: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
                   f"<code>/get_user_info_by_user_id {user.id}</code> To Check the user details first\n"
                   f"<code>/increase_the_user_files {user.id} {value}</code>: and i will replace the token and send back"
                   )
    await context.bot.send_message(bot_config.ADMIN_GROUPS_ID[0], text_admin, parse_mode= ParseMode.HTML)



async def increase_total_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    - increase_total_files count_number
    This executes when a person wants to increase their total file limit
    '''
    user = update.message.from_user

    if not context.args:
        await context.bot.send_message(user.id, "You must provide a number after the command to increase your limit.")
        return
    try:
        value = int(context.args[0])
    except ValueError:
        await context.bot.send_message(user.id,"Please provide a valid number to increase your file limit.")
        return
    text = (
        f"You want to increase your file limit by <code>{value}</code> files. "
        f"Please wait for admin verification. After approval, I will notify you."
    )
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)

    text_admin = (
        f"{start_module.name_bold_link(user)} wants to increase their file limit "
        f"by <b><u>{value}</u></b>. Please verify the request.\n"
        f"User ID: <code>{user.id}</code>\n"
        f"Request Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"<code>/get_user_info_by_user_id {user.id}</code> to check user details.\n"
        f"<code>/increase_the_user_files {user.id} {value}</code> to approve."
    )
    await context.bot.send_message(
        bot_config.ADMIN_GROUPS_ID[0], text_admin, parse_mode=ParseMode.HTML
    )




# async def increase_the_user_files_normal(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     '''This is for when a normal not admin user send /increase_the_user_files to bot'''
#     user = update.message.from_user
#     text = f"You are not any admin to use this bot, You cannot use this"
#     if user.id not in bot_config.ADMIN_IDS:
#         await context.bot.send_message(user.id, text)





async def increase_the_user_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    This is come when a admin send this
    To increase a user total files limit you need to use this cmd
    - /increase_the_user_files user_id how_many_token
    '''
    user = update.message.from_user
    if len(context.args) != 2:
        await context.bot.send_message(user.id, f"You must exactly provide both the user ID and the number of tokens to increase. \n\nUsage: /increase_the_user_files user_id how_many_tokens")
        return
    try:
        user_id = int(context.args[0])
        token_increase = int(context.args[1])
    except ValueError:
        await context.bot.send_message(user.id, "Both user ID and number of tokens must be valid numbers. Usage: /increase_the_user_files user_id how_many_tokens")
        return
    if token_increase <= 0:
        await context.bot.send_message(user.id, f"The number of tokens must be a positive number. Usage: /increase_the_user_files user_id how_many_tokens.\nRather, you can use /decrease_the_user_files with the positive value. For example: <code>/decrease_the_user_files {user_id} {abs(token_increase)}</code>", parse_mode= ParseMode.HTML)
        return
    
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user_id).first()
    if not user_obj:
        await context.bot.send_message(user.id, "The specified user ID is not registered in our database or the user has been removed from the database already.")
        return
    user_obj.total_files_ += token_increase
    session.commit()
    await context.bot.send_message(bot_config.ADMIN_GROUPS_ID[0], f"User {user_id}'s file limit has been increased by {token_increase} tokens. This is done by {user.full_name} His new files value is {user_obj.total_files_}")
    await context.bot.send_message(user_id, f"Your file limit has been increased by {token_increase} tokens.")




async def decrease_the_user_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    To decrease a user's total files limit you need to use this command:
    - /decrease_the_user_files user_id how_many_tokens
    '''
    user = update.message.from_user
    if len(context.args) != 2:
        await context.bot.send_message(user.id, "You must exactly provide both the user ID and the number of tokens to decrease. \n\nUsage: /decrease_the_user_files user_id how_many_tokens")
        return
    try:
        user_id = int(context.args[0])
        token_decrease = int(context.args[1])
    except ValueError:
        await context.bot.send_message(user.id, "Both user ID and number of tokens must be valid numbers. Usage: /decrease_the_user_files user_id how_many_tokens")
        return
    if token_decrease <= 0:
        await context.bot.send_message(user.id, f"The number of tokens must be a positive number. Usage: /decrease_the_user_files user_id how_many_tokens. Rather, you can use /increase_the_user_files with the positive value. For example: <code>/increase_the_user_files {user_id} {abs(token_decrease)}</code>", parse_mode= ParseMode.HTML)
        return
    user_obj = session.query(UserInformation).filter(UserInformation.user_id_ == user_id).first()
    if not user_obj:
        await context.bot.send_message(user.id, "The specified user ID is not registered in our database or the user has been removed from the database already.")
        return
    if user_obj.total_files_ < token_decrease:
        await context.bot.send_message(user.id, "The user does not have enough files to decrease by that amount.")
        return
    user_obj.total_files_ -= token_decrease
    session.commit()
    await context.bot.send_message(bot_config.ADMIN_GROUPS_ID[0], f"User {user_id}'s file limit has been decreased by {token_decrease} tokens. This is done by {user.full_name} His new files value is {user_obj.total_files_}")
    await context.bot.send_message(user_id, f"Your file limit has been decreased by {token_decrease} tokens. Your new value is {user_obj.total_files_}")









if __name__ == "__main__":
    """Here will some lists of functions will added here"""


