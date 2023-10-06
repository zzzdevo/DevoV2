
#

from config import LOG_GROUP_ID, MUSIC_BOT_NAME
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{MUSIC_BOT_NAME} ئاماری پەخشکردن</b>

<b>ئایدی گرووپ :</b> <code>{message.chat.id}</code>
<b>ناوی گرووپ :</b> {message.chat.title}
<b>یوزەری گرووپ :</b> @{message.chat.username}

<b>ئایدی بەکارهێنەر :</b> <code>{message.from_user.id}</code>
<b>ناوی :</b> {message.from_user.mention}
<b>یوزەری :</b> @{message.from_user.username}

<b>ڕیزکراو :</b> {message.text.split(None, 1)[1]}
<b>جۆری پەخشکردن :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
