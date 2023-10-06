#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
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
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
