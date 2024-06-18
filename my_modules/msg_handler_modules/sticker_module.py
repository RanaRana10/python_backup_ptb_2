"""
This module contains the handler function for processing received Sticker messages.

Usage:

    application.add_handler(MessageHandler(
        filters=filters.Sticker.ALL,
        callback=sticker_received_update,
        block=False
    ))

The handler function `sticker_received_update` processes received Sticker messages and sends back information about the sticker.
"""


import random

from telegram import Update
from telegram.ext import ContextTypes


async def sticker_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    sticker = update.message.sticker

    # Extracting sticker details
    file_id = sticker.file_id
    file_unique_id = sticker.file_unique_id
    sticker_type = sticker.type
    width = sticker.width
    height = sticker.height
    is_animated = sticker.is_animated
    is_video = sticker.is_video
    thumbnail = sticker.thumbnail  # This will be a PhotoSize object
    emoji = sticker.emoji
    set_name = sticker.set_name
    premium_animation = sticker.premium_animation
    mask_position = sticker.mask_position
    custom_emoji_id = sticker.custom_emoji_id
    needs_repainting = sticker.needs_repainting
    file_size = sticker.file_size

    # Creating a message with the extracted sticker information
    message = (
        f"🎨 Sticker Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"🏷️ Type: {sticker_type}\n"
        f"📏 Width: {width}\n"
        f"📐 Height: {height}\n"
        f"🔄 Animated: {is_animated}\n"
        f"📹 Video Sticker: {is_video}\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
        f"😀 Emoji: {emoji}\n"
        f"🖼️ Set Name: {set_name}\n"
        f"💎 Premium Animation: {premium_animation}\n"
        f"🎭 Mask Position: {mask_position}\n"
        f"🆔 Custom Emoji ID: {custom_emoji_id}\n"
        f"🎨 Needs Repainting: {needs_repainting}\n"
        f"📦 File Size: {file_size} bytes\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    await context.bot.send_sticker(user.id, file_id)





# from my_modules.database_modules.database_main_class_1_checking import UserDetails, session


# async def sticker_logic(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     '''Here i will try to add some logic about the stickers on how to work with database'''
#     user = update.message.from_user
#     user_obj_db = session.query(UserDetails).filter(UserDetails.user_id_ == user.id).first()
#     if not user_obj_db:
#         text = (f"You are not in our database, Please Join our databse and try again")
#         await context.bot.send_message(user.id, text)

#     else:
#         sticker = update.message.sticker
#         message = (f"Your Row is: {user_obj_db.id_}\n")

#         message += (f"You have send me a sticker form the link is:"
#                     f"<code>{sticker.set_name}</code>\n"
#                     f"https://t.me/addstickers/{sticker.set_name}")
#         await context.bot.send_message(user.id, message, parse_mode= "html")
#         await context.bot.send_sticker(user.id, sticker.file_id)

#         if not sticker.set_name:
#             await context.bot.send_message(user.id ,f"This sticker has not set bye")
#             return
#         sticker_set_info = await context.bot.get_sticker_set(sticker.set_name)
#         message = (
#         f"🎨 Sticker Set Information:\n"
#         f"🏷️ Name: {sticker_set_info.name}\n"
#         f"📜 Title: {sticker_set_info.title}\n"
#         f"🖼️ Sticker Type: {sticker_set_info.sticker_type}\n"
#         f"🖼️ Thumbnail: {sticker_set_info.thumbnail}\n"
#         )
#         await context.bot.send_message(user.id, message, parse_mode= "html")
#         stickers_array = sticker_set_info.stickers
#         sticker_count = len(stickers_array)
#         for i in range(sticker_count):
#             a1 = stickers_array[i].file_id
#             await context.bot.send_sticker(user.id, a1)


# banned_sticker_list = ["Sexvideos2_by_IllIlIlbot",]
# sticker_set_id = ["CAACAgEAAxkBAAJvD2Y0ShVJW5Q1OWUlauw2mi8U3d1dAAKJAwACdOcrAmY71QU0ZSv6NAQ","CAACAgEAAxkBAAJvEGY0SwSSRsKrgeFB-eA9C5nGIpxFAAKLAwACdOcrAokhlBgxFsB8NAQ"]

# async def papai_sticker_logic(update: Update, context: ContextTypes.DEFAULT_TYPE):

#     user = update.message.from_user
#     sticker = update.message.sticker
#     if not sticker.set_name:
#         await context.bot.send_message(user.id, f"You have not any set sticker")
#         return
#     if sticker.set_name in banned_sticker_list:
#         await context.bot.send_message(user.id, f"This sticker is banned, send another one")
#         await context.bot.send_sticker(user.id, random.choice(sticker_set_id))
#         return
#     sticker_set = await context.bot.get_sticker_set(sticker.set_name)
#     all_stickers_array = sticker_set.stickers
#     total_sticker_count = len(all_stickers_array)
#     await context.bot.send_message(user.id, f"This sticker has {total_sticker_count} Sticker")
#     random_sticker_no = random.randint(0,total_sticker_count)
#     random_sticker_file_id = all_stickers_array[random_sticker_no].file_id
#     await context.bot.send_sticker(user.id, random_sticker_file_id)




