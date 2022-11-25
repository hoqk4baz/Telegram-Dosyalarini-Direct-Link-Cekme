import asyncio
import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.utils.database import Database
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"Yᴇɴɪ︎ ᴋᴜʟʟᴀɴɪ︎ᴄɪ︎ ᴋᴀᴛɪ︎ʟᴅɪ︎ : \n\n𝗜̇𝘀𝗶𝗺 : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Bᴏᴛᴜ ʙᴀsʟᴀᴛᴛɪ︎ 🙂"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__𝚄̈𝚣𝚐𝚞̈𝚗𝚞̈𝚖 𝙳𝚘𝚜𝚝𝚞𝚖 𝙺𝚞𝚕𝚕𝚊𝚗ｪ𝚖ｪ𝚗 𝚈𝚊𝚜𝚊𝚔𝚕𝚊𝚗𝚍ｪ !!__\n\n  **Yᴀᴘɪ︎ᴍᴄɪ︎ʏᴀ Uʟᴀs [@dark_enza] Sᴀɴᴀ ʏᴀʀᴅɪ︎ᴍᴄɪ︎ ᴏʟᴜᴄᴀᴋᴛɪ︎ʀ**",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>𝙺𝚞𝚕𝚕𝚊𝚗𝚖𝚊𝚔 𝚒𝚌̧𝚒𝚗 𝚐𝚛𝚞𝚋𝚞𝚖𝚞𝚣𝚊 𝚔𝚊𝚝ｪ𝚕 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("𝐒̧𝐢𝐦𝐝𝐢 𝐊𝐚𝐭𝛊𝐥🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}") ]]
                ),
                parse_mode=ParseMode.HTML
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**𝘽𝙞𝙧 𝙝𝙖𝙩𝙖 𝙤𝙡𝙪𝙨̧𝙩𝙪 𝙮𝙖𝙥𝜾𝙢𝙘𝜾𝙮𝙖 𝙪𝙡𝙖𝙨̧** @dark_enza",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        file_name = get_media_file_name(m)
        file_size = humanbytes(get_media_file_size(m))
        stream_link = "https://{}/{}/{}".format(Var.FQDN, log_msg.id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.id,
                                    file_name)

        msg_text ="""
<i><u>𝗟𝗶𝗻𝗸 𝗢𝗹𝘂𝘀̧𝘁𝘂𝗿𝘂𝗹𝗱𝘂 !</u></i>\n
<b>📂 𝔻𝕠𝕤𝕪𝕒 𝕀̇𝕤𝕞𝕚 :</b> <i>{}</i>\n
<b>📦 𝔻𝕠𝕤𝕪𝕒 𝕓𝕠𝕪𝕦𝕥𝕦 :</b> <i>{}</i>\n
<b>📥 𝕀̇𝕟𝕕𝕚𝕣𝕞𝕖 𝕃𝕚𝕟𝕜𝕚 :</b> <i>{}</i>\n
<i>🔥 𝔼𝕤𝕚𝕘𝕟 ℝ𝕖𝕡𝕠</i> <b>: <a href='http://iwishkem.tk'>[𝐓𝐈𝐊𝐋𝐀]</a></b>\n
<b>🚸 ℕ𝕠𝕥 : 𝙇𝙞𝙣𝙠𝙡𝙚𝙧 𝙠𝙖𝙡𝜾𝙘𝜾𝙙𝜾𝙧 𝙫𝙚 𝙔𝙪̈𝙠𝙨𝙚𝙠 𝙝𝜾𝙯𝙙𝙖 𝙞𝙣𝙙𝙞𝙧𝙢𝙚 𝙨𝙖𝙜̆𝙡𝙖𝙧</b>\n
<i>🍃 𝑩𝒐𝒕 𝑺𝒂𝒉𝒊𝒃𝒊 𝑮𝒓𝒖𝒑 :</i> <b>@TrappledestekCom</b>
"""

        await log_msg.reply_text(text=f"**Tᴀʟᴇᴘ ᴇᴅᴇɴ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**ᴋᴜʟʟᴀɴɪ︎ᴄɪ︎ ɪᴅ :** `{m.from_user.id}`\n**ɪɴᴅɪʀᴍᴇ ʟɪɴᴋɪ :** {stream_link}", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN, quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode=ParseMode.HTML, 
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝕀̇ℕ𝔻𝕀̇ℝ 📥", url=stream_link)]]),
            quote=True
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.value)}s")
        await asyncio.sleep(e.value)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Bᴇᴋʟᴇʏᴇɴ {str(e.value)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**Kᴜʟʟᴀɴɪ︎ᴄɪ︎ ɪ︎ᴅ :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)


@StreamBot.on_message(filters.channel & (filters.document | filters.video), group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = "https://{}/{}".format(Var.FQDN, log_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.id)
        await log_msg.reply_text(
            text=f"**Kᴀɴᴀʟ ɪsᴍɪ:** `{broadcast.chat.title}`\n**Kᴀɴᴀʟ ID:** `{broadcast.chat.id}`\n**Uʀʟ ɪ︎sᴛᴇɢɪ:** https://t.me/{(await bot.get_me()).username}?start=darkenza_{str(log_msg.id)}",
          
            quote=True,
            parse_mode=ParseMode.MARKDOWN
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝕀̇𝕟𝕕𝕚𝕣𝕞𝕖 𝕃𝕚𝕟𝕜𝕚 📥", url=f"https://t.me/{(await bot.get_me()).username}?start=darkenza_{str(log_msg.id)}")]])
            # [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ 📥", url=f"https://t.me/FxStreamBot?start=AvishkarPatil_{str(log_msg.id)}")]])
        )
    except FloodWait as w:
        print(f"Dinlen Dostum :) {str(w.value)}s")
        await asyncio.sleep(w.value)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Tᴀʟᴇᴘ ᴇᴅᴇɴ {str(w.value)}s from {broadcast.chat.title}\n\n**Kᴀɴᴀʟ ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#Hᴀᴛᴀ_ɢᴇʀɪ ɪ︎ᴢʟᴇᴍᴇ:** `{e}`", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
        print(f"Yᴀʏɪ︎ɴ ᴍᴇsᴀᴊɪ︎ɴɪ︎ ᴅᴜᴢᴇɴʟᴇʏᴇᴍɪ︎ʏᴏʀᴜᴍ!\nHᴀᴛᴀ: {e}")
