#
# Copyright (C) 2021-2022 by TigerNetwork@Github, < https://github.com/TigerNetwork >.
#
# This file is part of < https://github.com/TigerNetwork/TigerMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TigerNetwork/TigerMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from TigerMusic import app
from TigerMusic.core.call import Tiger
from TigerMusic.utils.database import set_loop
from TigerMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Tiger.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
