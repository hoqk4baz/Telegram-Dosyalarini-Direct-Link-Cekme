import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.enums.parse_mode import ParseMode

db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>👋 Sᴇʟᴀᴍ,</i>{}\n
<i>Bᴇɴ Tᴇʟᴇɢʀᴀᴍ Dᴏsʏᴀʟᴀʀɪ︎ɴɪ︎ ᴅɪ︎ʀᴇᴄᴛ ɪ︎ɴᴅɪ︎ʀᴍᴇ Lɪɴᴋɪɴᴇ Dᴏɴᴜsᴛᴜʀᴇɴ Bɪʀ Bᴏᴛᴜᴍ</i>\n
<i>“Yᴀʀᴅɪ︎ᴍ“ Tᴜsᴜɴᴀ Bᴀsᴀʀᴀᴋ Dᴀʜᴀ Fᴀᴢʟᴀ Bɪ︎ʟɢɪ︎ Eᴅɪɴᴇʙɪʟɪʀsɪɴ</i>\n
<i><u>𝗨𝗬𝗔𝗥𝗜 🚸</u></i>
<b>🔞 𝙋𝙤𝙧𝙣𝙤𝙜𝙧𝙖𝙛𝙞 𝙞𝙘̧𝙚𝙧𝙚𝙣 𝙙𝙤𝙨𝙮𝙖𝙡𝙖𝙧𝙖𝙧 𝙠𝙖𝙡𝜾𝙘𝜾 𝙗𝙖𝙣𝙡𝙖𝙣𝙢𝙖𝙣𝜾𝙯𝙖 𝙨𝙚𝙗𝙚𝙥 𝙤𝙡𝙪𝙧.</b>\n\n
<i><b>🍃 𝘉𝘰𝘵 𝘚𝘢𝘩𝘪𝘣𝘪 𝘎𝘳𝘶𝘱 :</b>@TrappledestekCom</i>"""

HELP_TEXT = """
<i>- Bᴀɢʟᴀɴᴛɪ︎sɪ︎ɴɪ︎ Aʟᴍᴀᴋ ⵊsᴛᴇᴅɪ︎ɢɪ︎ɴ Dᴏsʏᴀʏɪ︎ Bᴀɴᴀ ⵊʟᴇᴛ.</i>
<i>- Bᴇɴᴅᴇ Dᴏsʏᴀɴɪ︎ɴ Bᴀɢʟᴀɴᴛɪ︎sɪ︎ɴɪ︎ Sᴀɴᴀ Gᴏɴᴅᴇʀᴇʏɪᴍ!.</i>
<i>- Bᴇɴɪ Kᴀɴᴀʟɪ︎ɴɪ︎ᴢᴀ Eᴋʟᴇʀsᴇɴɪ︎ᴢ Pᴀʏʟᴀsɪ︎ʟᴀɴ Dᴏsʏᴀɴɪ︎ɴ Aʟᴛɪ︎ɴᴀ Dɪ︎ʀᴇᴄᴛ ɪ︎ɴᴅɪ︎ʀᴍᴇ Bᴜᴛᴏɴᴜ ʏᴇʀʟᴇsᴛɪ︎ʀɪ︎ʀɪ︎ᴍ</i>
<i>- Lɪ︎ɴᴋʟᴇʀ Kᴀʟɪ︎ᴄɪ︎ ᴠᴇ Yᴜᴋsᴇᴋ Hɪ︎ᴢʟɪ︎ᴅɪ︎ʀ</i>\n
<u>🔸 𝗨𝗬𝗔𝗥𝗜 🚸</u>\n
<b>🔞 𝙋𝙤𝙧𝙣𝙤𝙜𝙧𝙖𝙛𝙞 𝙞𝙘̧𝙚𝙧𝙚𝙣 𝙙𝙤𝙨𝙮𝙖𝙡𝙖𝙧𝙖𝙧 𝙠𝙖𝙡𝜾𝙘𝜾 𝙗𝙖𝙣𝙡𝙖𝙣𝙢𝙖𝙣𝜾𝙯𝙖 𝙨𝙚𝙗𝙚𝙥 𝙤𝙡𝙪𝙧.</b>\n
<i>𝙷𝚊𝚝𝚊𝚕𝚊𝚛 𝚔𝚊𝚛𝚜̧ｪ𝚜ｪ𝚗𝚍𝚊 𝚈𝚊𝚙ｪ𝚖𝚌ｪ 𝚒𝚕𝚎 𝙸̇𝚕𝚎𝚝𝚒𝚜̧𝚒𝚖𝚎 𝙶𝚎𝚌̧𝚒𝚗</i> <b>: <a href='https://t.me/dark_enza'>[ 𝐁𝐮𝐫𝐝𝐚𝐧 ]</a></b>"""
ABOUT_TEXT = """
<b>⚜ 𝐁𝐨𝐭 𝐈̇𝐬𝐦𝐢 : 🇹🇷TrAppleDestek-İPALİNK🇹🇷</b>\n
<b>🔸𝐒𝐮̈𝐫𝐮̈𝐦 : <a href='https://telegram.me/dark_enza'>1.0</a></b>\n
<b>🔹𝐘𝐚𝐩𝛊𝐦𝐜𝛊 : <a href='https://telegram.me/dark_enza'>☬𝐃𝐀𝐑𝐊 | 𝐄𝐍𝐙𝐀☬</a></b>\n
<b>🔸𝐘𝐚𝐲𝛊𝐧𝐥𝐚𝐧𝐦𝐚 𝐓𝐚𝐫𝐢𝐡𝐢 : <a href='https://telegram.me/dark_enza'>[ 10 - 𝔼𝕜𝕚𝕞 - 2022 ] </a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʏᴀʀᴅɪ︎ᴍ', callback_data='help'),
        InlineKeyboardButton('ʜᴀᴋᴋɪ︎ɴᴅᴀ', callback_data='about'),
        InlineKeyboardButton('ᴋᴀᴘᴀᴛ', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᴀɴᴀ ᴍᴇɴᴜ', callback_data='home'),
        InlineKeyboardButton('ʜᴀᴋᴋɪ︎ɴᴅᴀ', callback_data='about'),
        InlineKeyboardButton('ᴋᴀᴘᴀᴛ', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᴀɴᴀ ᴍᴇɴᴜ', callback_data='home'),
        InlineKeyboardButton('ʏᴀʀᴅɪ︎ᴍ', callback_data='help'),
        InlineKeyboardButton('ᴋᴀᴘᴀᴛ', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

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


@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Yᴇɴɪ︎ ᴋᴜʟʟᴀɴɪ︎ᴄɪ︎ ᴋᴀᴛɪ︎ʟᴅɪ︎:** \n\n__ʙᴇɴɪ︎ᴍ ʏᴇɴɪ︎ ᴀʀᴋᴀᴅᴀsɪ︎ᴍ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __ʙᴏᴛᴜɴᴜ ʙᴀsʟᴀᴛᴛɪ︎ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__ᴜᴢɢᴜɴᴜᴍ ᴅᴏsᴛᴜᴍ ᴋᴜʟʟᴀɴɪ︎ᴍɪ︎ɴ ʏᴀsᴀᴋʟᴀɴᴅɪ︎. Yᴀᴘɪ︎ᴍᴄɪ︎ ɪ︎ʟᴇ ɪ︎ʟᴇᴛɪ︎sɪ︎ᴍᴇ ɢᴇᴄ__\n\n @dark_enza **Sᴀɴᴀ ʏᴀʀᴅɪ︎ᴍᴄɪ︎ ᴏʟᴀᴄᴀᴋᴛɪ︎ʀ**",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Gʀᴜʙᴜᴍᴜᴢᴀ ᴋᴀᴛɪ︎ʟᴀʀᴀᴋ ʙᴏᴛᴜᴍᴜᴢᴜ ᴋᴜʟʟᴀɴᴀʙɪ︎ʟɪ︎ʀsɪ︎ɴ 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Sɪ︎ᴍᴅɪ︎ ᴋᴀᴛɪ︎ʟ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode=ParseMode.HTML
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>𝘽𝙞𝙧 𝙝𝙖𝙩𝙖 𝙢𝙚𝙮𝙙𝙖𝙣𝙖 𝙜𝙚𝙡𝙙𝙞 𝙔𝙖𝙥𝜾𝙢𝙘𝜾 𝙞𝙡𝙚 𝙞𝙡𝙚𝙩𝙞𝙨̧𝙞𝙢𝙚 𝙜𝙚𝙘̧/i> <b><a href='http://t.me/dark_enza'>[ 𝗕𝗨𝗥𝗗𝗔𝗡 ]</a></b>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Uᴢɢᴜɴᴜᴍ ᴅᴏsᴛᴜᴍ ᴋᴜʟʟᴀɴɪ︎ᴍɪ︎ɴ Yᴀsᴀᴋʟᴀɴᴅɪ︎ Yᴀᴘᴍᴄɪ︎ʏᴀ ᴜʟᴀs** @dark_enza",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Bᴏᴛᴜ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪ︎ᴄɪ︎ɴ ʟᴜᴛꜰᴇɴ Gʀᴜʙᴜᴍᴜᴢᴀ ᴋᴀᴛɪ︎ʟɪ︎ɴ**!\n\n**𝙰𝚜̧ｪ𝚛ｪ 𝚢𝚞̈𝚔𝚕𝚎𝚗𝚖𝚎 𝚗𝚎𝚍𝚎𝚗𝚒𝚢𝚕𝚎 𝙱𝚘𝚝𝚞𝚖𝚞𝚣𝚞 𝚂𝚊𝚍𝚎𝚌𝚎 𝚐𝚛𝚞𝚙 𝚞̈𝚢𝚎𝚕𝚎𝚛𝚒 𝙺𝚞𝚕𝚕𝚊𝚗𝚊𝚋𝚒𝚕𝚒𝚛 **!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Gʀᴜʙᴀ ᴋᴀᴛɪ︎ʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("🔄 Yᴇɴɪ︎ʟᴇ / Tᴇᴋʀᴀʀ ᴅᴇɴᴇ", url=f"https://t.me/{(await b.get_me()).username}?start=AvishkarPatil_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝘽𝙞𝙧 𝙝𝙖𝙩𝙖 𝙤𝙡𝙪𝙨̧𝙩𝙪 𝙔𝙖𝙥𝜾𝙢𝙘𝜾 𝙞𝙡𝙚 𝙄̇𝙡𝙚𝙩𝙞𝙨̧𝙞𝙢𝙚 𝙂𝙚𝙘̧** [☬𝐃𝐀𝐑𝐊 | 𝐄𝐍𝐙𝐀☬](https://t.me/dark_enza).",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "https://{}/{}/{}".format(Var.FQDN, get_msg.id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id,
                                     file_name)

        msg_text ="""
<i><u>𝗕𝗮𝗴̆𝗹𝗮𝗻𝘁𝛊𝗻 𝗢𝗹𝘂𝘀̧𝘁𝘂𝗿𝘂𝗹𝗱𝘂 !</u></i>\n
<b>📂 𝔻𝕠𝕤𝕪𝕒 𝕀̇𝕤𝕞𝕚 :</b> <i>{}</i>\n
<b>📦 𝔻𝕠𝕤𝕪𝕒 𝔹𝕠𝕪𝕦𝕥𝕦 :</b> <i>{}</i>\n
<b>📥 𝕀̇ℕ𝔻𝕀̇ℝ :</b> <i>{}</i>\n
<b>🚸 ℕ𝕠𝕥 : 𝙻𝚒𝚗𝚔𝚕𝚎𝚛𝚒 𝟸𝟺 𝚜𝚊𝚊𝚝 𝙸̇𝚌̧𝚒𝚗𝚍𝚎 𝙺𝚞𝚕𝚕𝚊𝚗𝚖𝚊𝚗ｪ𝚣 𝚃𝚊𝚟𝚜𝚒𝚢𝚎 𝚎𝚍𝚒𝚕𝚒𝚛</b>\n
<i>🍃 ʙᴏᴛ sᴀʜɪ︎ʙɪ︎ ɢʀᴜᴘ :</i> <b>@TrappledestekCom</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ⵊ̇NDⵊ̇R 📥", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**ʏᴇɴɪ︎ ᴋᴜʟʟᴀɴɪ︎ᴄɪ︎ ᴋᴀᴛɪ︎ʟᴅɪ︎ **\n\n__Bᴇɴɪ︎ᴍ ʏᴇɴɪ︎ ᴀʀᴋᴀᴅᴀsɪ︎ᴍ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __ʙᴏᴛᴜɴᴜ ʙᴀsʟᴀᴛᴛɪ︎ !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Uᴢɢᴜɴᴜᴍ ᴅᴏsᴛᴜᴍ ᴋᴜʟʟᴀɴɪ︎ᴍɪ︎ɴ ʏᴀsᴀᴋʟᴀɴᴅɪ︎, Yᴀᴘɪ︎ᴍᴄɪ︎ ɪ︎ʟᴇ ɪ︎ʟᴇᴛɪ︎sɪ︎ᴍᴇ ɢᴇᴄ</i>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Bᴏᴛᴜ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪ︎ᴄɪ︎ɴ ɢʀᴜʙᴜᴍᴜᴢᴀ ᴋᴀᴛɪ︎ʟɪ︎ɴ!**\n\n__𝙰𝚜̧ｪ𝚛ｪ 𝚢𝚞̈𝚔𝚕𝚎𝚗𝚖𝚎 𝚜𝚎𝚋𝚎𝚋𝚒 𝚒𝚕𝚎 𝚂𝚊𝚍𝚎𝚌𝚎 𝚐𝚛𝚞𝚙 𝚞̈𝚢𝚎𝚕𝚎𝚛𝚒 𝚔𝚞𝚕𝚕𝚊𝚗𝚊𝚋𝚒𝚕𝚒𝚛!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Gʀᴜʙᴀ ᴋᴀᴛɪ︎ʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__𝘽𝙞𝙧 𝙨𝙤𝙧𝙪𝙣 𝙫𝙖𝙧! 𝙔𝙖𝙥𝜾𝙢𝙘𝜾 𝙞𝙡𝙚 𝙞𝙡𝙚𝙩𝙞𝙨̧𝙞𝙢𝙚 𝙂𝙚𝙘̧__ [☬𝐃𝐀𝐑𝐊 | 𝐄𝐍𝐙𝐀☬](https://t.me/dark_enza).",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
