'''
This will help to handle different video note processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.video_note_module import video_note_received_update


Usage:
    application.add_handler(MessageHandler(
        filters=filters.VIDEO_NOTE,
        callback=video_note_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def video_note_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received video note update.'''
    user = update.message.from_user
    video_note = update.message.video_note

    # Extracting video note details
    file_id = video_note.file_id
    file_unique_id = video_note.file_unique_id
    length = video_note.length
    duration = video_note.duration
    file_size = video_note.file_size

    # Creating a message with the extracted video note information
    message = (
        f"🎥 Video Note Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 File Unique ID: {file_unique_id}\n"
        f"📏 Length: {length}\n"
        f"⏰ Duration: {duration} seconds\n"
        f"📦 File Size: {file_size} bytes"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)
    await context.bot.send_video_note(user.id, file_id)