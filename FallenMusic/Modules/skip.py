# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio

from FallenMusic import BOT_USERNAME, app, fallendb, pytgcalls
from FallenMusic.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb


@app.on_message(filters.command(["atla", "skip"]) & filters.group)
@admin_check
async def skip_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    get = fallendb.get(message.chat.id)
    if not get:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text(
                text=f"➻ ʏᴀʏıɴı ɢᴇᴄ̧ᴛɪ 🥺\n│ \n└👉 : {message.from_user.mention} 🥀\n\n**» sıʀᴀᴅᴀ ᴘᴀʀᴄ̧ᴀ ʏᴏᴋ** {message.chat.title}, **ʙᴇɴᴅᴇɴ ʙᴜ ᴋᴀᴅᴀʀ.**",
                reply_markup=close_key,
            )
        except:
            return
    else:
        title = get[0]["başlık"]
        duration = get[0]["süre"]
        file_path = get[0]["dosya türü"]
        videoid = get[0]["video numarası"]
        req_by = get[0]["req"]
        user_id = get[0]["kullanıcı"]
        get.pop(0)

        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.change_stream(
                message.chat.id,
                stream,
            )
        except:
            await _clear_(message.chat.id)
            return await pytgcalls.leave_group_call(message.chat.id)

        await message.reply_text(
            text=f"➻ʏᴀʏıɴı ɢᴇᴄ̧ᴛɪ 🥺\n│ \n👉 : {message.from_user.mention} 🥀",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        return await message.reply_photo(
            photo=img,
            caption=f"**➻ ʏᴀʏıɴ ʙᴀşʟᴀᴅı**\n\n‣ **ʙᴀşʟıᴋ :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ **sᴜ̈ʀᴇ :** `{duration}` ᴅᴀᴋɪᴋᴀ\n‣ **ᴛᴀʟᴇᴘ ᴇᴅᴇɴ :** {req_by}",
            reply_markup=buttons,
        )
