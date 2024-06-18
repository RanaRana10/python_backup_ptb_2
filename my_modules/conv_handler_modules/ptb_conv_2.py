#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
This is full copy from example section of PTB
This module i will import 
get_conv_handler_2()
this handler will start by /ptba_2 or /2
this fun will return conv handler to use in add handler
"""

import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    PicklePersistence,
)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
# logging.getLogger('apscheduler').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["Age", "Favourite colour"],
    ["Number of siblings", "Something else..."],
    ["Done"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])
    # return "\n".join(facts)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    await update.message.reply_text(
        "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
        "Why don't you tell me something about yourself?",
        reply_markup=markup,
    )
    user_data = context.user_data
    user_data.clear()

    return CHOOSING


async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask the user for info about the selected predefined choice."""
    text = update.message.text
    if len(text) >= 100:
        text = f"Please provide a valid message within 1000 characters.\nPlease /start"
        await update.message.reply_text(f"{text}")
        return ConversationHandler.END
    
    context.user_data["choice"] = text
    await update.message.reply_text(f"Your {text.lower()}? Yes, I would love to hear about that!")

    return TYPING_REPLY



async def custom_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask the user for a description of a custom category."""
    await update.message.reply_text('Alright, please send category ex, "Most impressive skill"')

    return TYPING_CHOICE


async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    print(1, user_data)
    text = update.message.text
    category = user_data["choice"]
    user_data[category] = text
    print(2, user_data)
    del user_data["choice"]
    print(3, user_data)
    await update.message.reply_text(
        "Neat! Just so you know, this is what you already told me:"
        f"<tg-spoiler>{facts_to_str(user_data)}</tg-spoiler>You can tell me more, or change your opinion"
        " on something.",
        reply_markup=markup,
        parse_mode= "html",
    )

    return CHOOSING


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text(
        f"I learned these facts about you: {facts_to_str(user_data)}Until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )

    user_data.clear()
    return ConversationHandler.END





def get_conv_handler_1():
    '''This is the main handler example from example just to store safe i not use it'''
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(Age|Favourite colour|Number of siblings)$"), regular_choice
                ),
                MessageHandler(filters.Regex("^Something else...$"), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
        allow_reentry= True,
        conversation_timeout= 5,
    )
    return conv_handler





def get_conv_handler_2():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(["ptb_2", "2"], start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(Age|Favourite colour|Number of siblings)$"), regular_choice
                ),
                MessageHandler(filters.Regex("^Something else...$"), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    received_information,
                )
            ],
            ConversationHandler.TIMEOUT : [MessageHandler(filters.ALL, timeout)]
        },

        fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
        allow_reentry= True,
        conversation_timeout= 5,
    )
    return conv_handler


async def timeout(update, context):
    await update.message.reply_text("Sorry, it seems you took too long to respond. "
                              "Let's start over if you'd like!")
    print("Timeout has Done fully")
    await get_user_data_dict(update=update, context=context)
    return ConversationHandler.END


async def get_user_data_dict(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    user_data = context.user_data
    text = f"{user_data}"

    await context.bot.send_message(user.id, text)







def main() -> None:
    """Run the bot."""
    persistence = PicklePersistence(filepath= "ptb_2_conv_persistence_file")
    application = Application.builder().token("Token 2").persistence(persistence).build()


    application.add_handler(get_conv_handler_2())
    application.add_handler(CommandHandler(["about", "a"], get_user_data_dict))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()