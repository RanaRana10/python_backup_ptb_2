'''
This will help to handle different voice note processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.voice_module import voice_received_update


Usage:
    application.add_handler(MessageHandler(
        filters=filters.VOICE,
        callback=voice_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def voice_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received voice note update.'''
    user = update.message.from_user
    voice = update.message.voice

    # Extracting voice note details
    file_id = voice.file_id
    file_unique_id = voice.file_unique_id
    duration = voice.duration
    mime_type = voice.mime_type
    file_size = voice.file_size

    # Creating a message with the extracted voice note information
    message = (
        f"🎤 Voice Note Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 File Unique ID: {file_unique_id}\n"
        f"⏰ Duration: {duration} seconds\n"
        f"🎵 MIME Type: {mime_type}\n"
        f"📦 File Size: {file_size} bytes"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    await context.bot.send_voice(user.id, file_id)