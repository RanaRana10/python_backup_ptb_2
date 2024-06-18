'''
This will help to handle different contact processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.contact_module import contact_received_update

Usage:
    application.add_handler(MessageHandler(
        filters=filters.CONTACT,
        callback=contact_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

vcard = f"""
BEGIN:VCARD
VERSION:4.0
FN:Simon Perreault
N:Perreault;Simon;;;ing. jr,M.Sc.
BDAY:--0203
GENDER:M
EMAIL;TYPE=work:simon.perreault@viagenie.ca
END:VCARD"""


async def contact_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received contact information.'''
    user = update.message.from_user
    contact = update.message.contact

    # Extracting contact details
    phone_number = contact.phone_number
    first_name = contact.first_name
    last_name = contact.last_name if contact.last_name else ""
    user_id = contact.user_id if contact.user_id else ""
    vcard = contact.vcard if contact.vcard else ""

    # Creating a message with the extracted contact information
    message = (
        f"📞 Contact Information:\n"
        f"📱 Phone Number: {phone_number}\n"
        f"👤 First Name: {first_name}\n"
        f"👥 Last Name: {last_name}\n"
        f"🆔 User ID: {user_id}\n"
        f"📇 vCard: {vcard}"
    )

    await context.bot.send_message(user.id, message)
    await context.bot.send_contact(user.id, phone_number= "+91 0100200300", first_name= "Rana", last_name= "Universe")
    await context.bot.send_contact(user.id, phone_number, first_name, last_name,vcard=vcard)

