'''
This function handles processing for received photo updates.
The import of this function is:
from my_modules.msg_handler_modules.photo_module import photo_received_update
'''

from telegram import Update
from telegram.ext import ContextTypes




caption = f"""
<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
"""








async def photo_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user details of the received photo update.'''
    user = update.message.from_user
    photo = update.message.photo[-1]  # Considering only the last (highest resolution) photo

    # Extracting photo details
    file_id = photo.file_id
    file_unique_id = photo.file_unique_id
    width = photo.width
    height = photo.height
    file_size = photo.file_size

    # Creating a message with the extracted photo information
    message = (
        f"📷 Photo Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"📏 Width: {width}px\n"
        f"📐 Height: {height}px\n"
        f"📦 File Size: {file_size} bytes\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)
    if update.message.caption:
        await context.bot.send_photo(user.id, file_id, caption= update.message.caption)
        await context.bot.send_photo(user.id, file_id, caption= update.message.caption_html)
        await context.bot.send_photo(user.id, file_id, caption= update.message.caption_html, parse_mode= "html")
