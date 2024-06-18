'''
This will help to handle different location processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.location_module import location_received_update

Usage:
    application.add_handler(MessageHandler(
        filters=filters.LOCATION,
        callback=location_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def location_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received location information.'''
    user = update.message.from_user
    location = update.message.location

    # Extracting location details
    latitude = location.latitude
    longitude = location.longitude
    accuracy = location.horizontal_accuracy
    live_period = location.live_period if location.live_period else "Not provided"
    heading = location.heading if location.heading else "Not provided"
    proximity_alert_radius = location.proximity_alert_radius if location.proximity_alert_radius else "Not provided"

    # Creating a message with the extracted location information
    message = (
        "📍 Location Information:\n"
        f"🌐 Latitude: {latitude}\n"
        f"🌐 Longitude: {longitude}\n"
        f"🎯 Horizontal Accuracy: {accuracy} meters\n"
        f"⏳ Live Period: {live_period} seconds\n"
        f"🧭 Heading: {heading} degrees\n"
        f"🚷 Proximity Alert Radius: {proximity_alert_radius} meters"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)
    await context.bot.send_location(user.id, latitude, longitude)
