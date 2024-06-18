'''
This function handles processing for received video updates.
The import of this function is:
from my_modules.msg_handler_modules.video_module import video_received_update
'''

from telegram import Update
from telegram.ext import ContextTypes

async def video_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user details of the received video update.'''
    user = update.message.from_user
    video = update.message.video

    # Extracting video details
    file_id = video.file_id
    file_unique_id = video.file_unique_id
    width = video.width
    height = video.height
    duration = video.duration
    file_name = video.file_name if video.file_name else "Untitled"
    mime_type = video.mime_type if video.mime_type else "video/mp4"
    file_size = video.file_size if video.file_size else 0
    thumbnail = video.thumbnail  # This will be a PhotoSize object

    # Creating a message with the extracted video information
    message = (
        f"📹 Video Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"📏 Width: {width}px\n"
        f"📐 Height: {height}px\n"
        f"⏱ Duration: {duration} seconds\n"
        f"📁 File Name: {file_name}\n"
        f"📝 MIME Type: {mime_type}\n"
        f"📦 File Size: {file_size} bytes\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)
    await context.bot.send_video(user.id, file_id)