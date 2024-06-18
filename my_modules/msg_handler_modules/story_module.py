'''
This will help to handle different story processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.story_module import story_received_update

Usage:
    application.add_handler(MessageHandler(
        filters=filters.STORY,
        callback=story_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def story_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received story update.'''
    user = update.message.from_user
    story = update.message.story

    # Extracting story details
    chat = story.chat  # This will be a Chat object
    story_id = story.id

    # Creating a message with the extracted story information
    message = (
        f"📖 Story Information:\n"
        f"👤 Chat: {chat.title}\n"
        f"🆔 Story ID: {story_id}\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, you can do further processing with the story data

    # Optionally, log that the story information was sent
    print(f"Story information sent for user: {user.id}")

# Then, add a handler for the story message
# application.add_handler(MessageHandler(filters=filters.Story, callback=story_received_update))
