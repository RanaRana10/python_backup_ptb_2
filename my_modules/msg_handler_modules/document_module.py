'''
This function handles processing for received document updates.
The import of this function is:
from my_modules.msg_handler_modules.document_module import document_received_update
'''

from telegram import Update
from telegram.ext import ContextTypes

async def document_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user details of the received document update.'''
    user = update.message.from_user
    document = update.message.document

    # Extracting document details
    file_id = document.file_id
    file_unique_id = document.file_unique_id
    file_name = document.file_name if document.file_name else "Untitled"
    mime_type = document.mime_type if document.mime_type else "application/octet-stream"
    file_size = document.file_size if document.file_size else 0
    thumbnail = document.thumbnail  # This will be a PhotoSize object

    # Creating a message with the extracted document information
    message = (
        f"📄 Document Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"📁 File Name: {file_name}\n"
        f"📝 MIME Type: {mime_type}\n"
        f"📦 File Size: {file_size} bytes\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    await context.bot.send_document(user.id, file_id, caption= f"{update.message.caption if update.message.caption else 'No Captionn avaialbe'}")