import asyncio
from main.bot import StreamBot
from main.utils.file_properties import gen_link
from main.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(
    filters.private
    & ~filters.user(Var.BANNED_USERS) & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def private_receive_handler(c: Client, m: Message):
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        reply_markup, Stream_Text, stream_link = await gen_link(m=m, log_msg=log_msg, from_channel=False)
        await log_msg.reply_text(text=f"**Tarafından talep edildi :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Kullanıcı ID :** `{m.from_user.id}`\n**İndirme Linki :** {stream_link}", disable_web_page_preview=True, quote=True)

        await m.reply_text(
            text=Stream_Text,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
    except FloodWait as e:
        print(f"İçin Beklemek {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Floodwait var Of {str(e.x)}s itibaren [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**Kullanıcı ID :** `{str(m.from_user.id)}`", disable_web_page_preview=True,)

@StreamBot.on_message(filters.channel & ~filters.user(Var.BANNED_USERS) & (filters.document | filters.video) & ~filters.edited, group=-1)
async def channel_receive_handler(bot, broadcast: Message):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = "https://{}/{}".format(Var.FQDN, log_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                    Var.PORT,
                                    log_msg.message_id)
        await log_msg.reply_text(
            text=f"**Kanal İsmi:** `{broadcast.chat.title}`\n**Kanal ID:** `{broadcast.chat.id}`\n**Getirilen LİNK:** https://t.me/{(await bot.get_me()).username}?start=msgid_{str(log_msg.message_id)}",
            # text=f"**Kanal İsmi:** `{broadcast.chat.title}`\n**Kanal ID:** `{broadcast.chat.id}`\n**Getirilen Link:** https://t.me/FxStreamBot?start=msgid_{str(log_msg.message_id)}",
            quote=True,            
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("İndirme Linki 📥", url=stream_link)]])
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Got Floodwait Of {str(w.x)}s from {broadcast.chat.title}\n\n**Kanal ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True,)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True)
        print(f"Yayın Mesajını Düzenleyemiyorum!\nEʀʀᴏʀ: {e}")

# Feature is Dead no New Update for Stream Link on Group
@StreamBot.on_message(filters.group & ~filters.user(Var.BANNED_USERS) & (filters.document | filters.video | filters.audio) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        reply_markup, Stream_Text, stream_link = await gen_link(m=m, log_msg=log_msg, from_channel=True)
        await log_msg.reply_text(text=f"**Tarafından talep edildi :** [{m.chat.first_name}](tg://user?id={m.chat.id})\n**Grup ID :** `{m.from_user.id}`\n**İndirme Linki :** {stream_link}", disable_web_page_preview=True, quote=True)

        await m.reply_text(
            text=Stream_Text,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Floodwait var {str(e.x)}s itibaren [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**Kullanıcı ID :** `{str(m.from_user.id)}`", disable_web_page_preview=True, )
