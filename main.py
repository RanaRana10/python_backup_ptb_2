
'''
This is my main file to run all things are connected mainly with this
The Database System has not implimented Yet

Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse
'''

import sys
sys.dont_write_bytecode = True


from telegram import Update
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters


from my_modules.abc_modules import bot_config
from my_modules.abc_modules.bot_config import BOT_TOKEN


from my_modules.cmd_handler_modules import help_module
from my_modules.cmd_handler_modules import start_module
from my_modules.cmd_handler_modules import database_cmd_module
from my_modules.cmd_handler_modules import get_files_module

from my_modules.logger_modules.logger_module import setup_logger


from my_modules.msg_handler_modules import(
    animation_module,
    audio_module,
    contact_module,
    dice_module,
    document_module,
    location_module,
    photo_module,
    sticker_module,
    story_module,
    video_module,
    video_note_module,
    voice_module
    )

from my_modules.msg_modules import file_handler_module
from my_modules.msg_modules import text_modules

from telegram.ext import ContextTypes


'''
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Below will my special coding started
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
'''


logger = setup_logger()












def main() -> None:
    """Start the bot."""

    application = Application.builder().token(BOT_TOKEN).build()



    application.add_handler(MessageHandler(
        filters=filters.UpdateType.EDITED & filters.Command(),
        callback=text_modules.all_edited_cmd,
        block=False
    ))

    application.add_handler(MessageHandler(
        filters=filters.UpdateType.EDITED,
        callback=text_modules.all_edited_msg,
        block=False
    ))

    # application.add_handler(CommandHandler(
    #     command= ["start", "st"],
    #     callback= start_module.start_from_admin,
    #     filters= filters.Chat(bot_config.ADMIN_IDS),
    #     block= False
    # ))


    # application.add_handler(CommandHandler("get_dict_admin", text_modules.get_dict_admin, filters.Chat(1895194333)))
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_modules.save_text_html))
    # application.add_handler(CommandHandler("start", text_modules.get_saved_text))












    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_module.start_cmd_private,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_module.start_cmd_group,
        filters= filters.ChatType.GROUPS,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_module.start_cmd_channel,
        filters= filters.ChatType.CHANNEL,
        block= False
    ))

    application.add_handler(CommandHandler(
        command= ["help", "helps"],
        callback= help_module.help_cmd_admin,
        filters= filters.ChatType.PRIVATE & filters.Chat(bot_config.ADMIN_IDS),
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["help", "helps"],
        callback= help_module.help_cmd_private,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["help", "helps"],
        callback= help_module.help_cmd_group,
        filters= filters.ChatType.GROUPS,
        block= False
    ))

    #When i admin forget to send password
    application.add_handler(CommandHandler(
        command= ["send_db_file"],
        callback= database_cmd_module.send_db_no_password,
        filters= filters.Chat(chat_id= bot_config.ADMIN_IDS),
        block= False,
        has_args=False
    ))

    # When i admin send password send with this cmd
    application.add_handler(CommandHandler(
        command= ["send_db_file"],
        callback= database_cmd_module.send_db_admin,
        filters= filters.Chat(chat_id= bot_config.ADMIN_IDS),
        block= False,
        has_args=1
    ))

    # When anyone send this other than the admin also
    application.add_handler(CommandHandler(
        command= ["send_db_file"],
        callback= database_cmd_module.send_db_file,
        filters= filters.ChatType.PRIVATE & ~ filters.FORWARDED,
        block= False,
    ))

    application.add_handler(CommandHandler(
        command= ["add_me_to_database"],
        callback= database_cmd_module.add_me_to_database,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))

    application.add_handler(CommandHandler(
        command= ["get_my_info"],
        callback= database_cmd_module.get_my_info,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))

    application.add_handler(CommandHandler(
        command= ["update_my_info"],
        callback= database_cmd_module.update_my_info,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["activate_me"],
        callback= database_cmd_module.activate_me,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))

    application.add_handler(CommandHandler(
        command= ["delete_my_data"],
        callback= database_cmd_module.delete_my_data,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))


    application.add_handler(CommandHandler(
        command= ["minus_one_value"],
        callback= database_cmd_module.minus_one_value,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["minus_many_value"],
        callback= database_cmd_module.minus_many_value,
        filters= filters.ChatType.PRIVATE,
        block= False,
        has_args= 1
    ))
    application.add_handler(CommandHandler(
        command= ["minus_many_value"],
        callback= database_cmd_module.minus_many_value_wrong,
        filters= filters.ChatType.PRIVATE,
        block= False,
    ))

    # Below is the when a admin wants a user info
    application.add_handler(CommandHandler(
        command= ["get_user_info_by_user_id"],
        callback= database_cmd_module.get_user_info_by_user_id,
        filters= filters.Chat(bot_config.ADMIN_IDS),
        block= False,
    ))
    # this will execute when a normal user want ot increase it will check by admin
    application.add_handler(CommandHandler(
        command= ["increase_total_files"],
        callback= database_cmd_module.increase_total_files,
        filters= filters.ChatType.PRIVATE,
        block= False,
    ))

    application.add_handler(CommandHandler(
        command= ["increase_the_user_files"],
        callback= database_cmd_module.increase_the_user_files,
        filters= filters.ChatType.PRIVATE & filters.Chat(bot_config.ADMIN_IDS),
        block= False,
    ))

    application.add_handler(CommandHandler(
        command= ["decrease_the_user_files"],
        callback= database_cmd_module.decrease_the_user_files,
        filters= filters.ChatType.PRIVATE & filters.Chat(bot_config.ADMIN_IDS),
        block= False,
    ))

    application.add_handler(CommandHandler(
        command= ["get_file"],
        callback= get_files_module.get_file,
        filters= filters.ChatType.PRIVATE,
        block= False,
    ))

    application.add_handler(CommandHandler(
        command= ["get_audio"],
        callback= get_files_module.get_audio,
        filters= filters.ChatType.PRIVATE,
        block= False,
    ))




    application.add_handler(MessageHandler(
        filters= filters.Document.ALL & filters.CAPTION,
        callback= file_handler_module.file_handle_with_caption,
        block= False
    ))

    application.add_handler(MessageHandler(
        filters= filters.Document.ALL & ~filters.CAPTION,
        callback= file_handler_module.file_handle_with_caption,
        block= False
    ))

    application.add_handler(MessageHandler(
        filters=filters.AUDIO,
        callback=file_handler_module.audio_handler,
        block=False
    ))



    # The Below are not useful for us this is just for handld and checking

    '''This below is just for only response no need just these are for testing '''

    
    application.add_handler(MessageHandler(
        filters=filters.ANIMATION,
        callback=animation_module.animation_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.AUDIO,
        callback=audio_module.audio_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.CONTACT,
        callback=contact_module.contact_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.Dice.ALL,
        callback=dice_module.dice_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.Document.ALL,
        callback=document_module.document_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.LOCATION,
        callback=location_module.location_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.PHOTO,
        callback=photo_module.photo_received_update,
        block=False
    ))
    # application.add_handler(MessageHandler(
    #     filters=filters.Sticker.ALL & filters.Chat(6172360795),
    #     callback=sticker_module.papai_sticker_logic,
    #     block=False
    # ))
    application.add_handler(MessageHandler(
        filters=filters.Sticker.ALL,
        callback=sticker_module.sticker_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.STORY,
        callback=story_module.story_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VIDEO,
        callback=video_module.video_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VIDEO_NOTE,
        callback=video_note_module.video_note_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VOICE,
        callback=voice_module.voice_received_update,
        block=False
    ))

    '''Still this uppers all are optional'''



    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_modules.echo_fun))
    application.add_handler(MessageHandler(filters.Command(), text_modules.extra_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()







