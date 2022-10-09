import random
from main.bot import StreamBot
from main.utils.file_properties import gen_link, get_media_file_unique_id
from main.vars import Var
from main.utils.Translation import Language, BUTTON
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageDeleteForbidden


deldbtnmsg=["Zaten Linki Sildiniz", "İşlemi Geri Alamazsınız", "Yeni Link Oluşturmak İçin Dosyayı Tekrar Gönderebilirsiniz", "Bana Tıkladığınızda Linkiniz Öldü", "Bu Sadece Linkinizi Gösteren Bir Butondur.  silindi"]

@StreamBot.on_callback_query()
async def cb_data(bot, update: CallbackQuery):
    # lang = getattr(Language, update.from_user.language_code)
    lang = getattr(Language, "en")
    if update.data == "Geri":
        await update.message.edit_text(
            text=lang.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=BUTTON.START_BUTTONS
        )
    elif update.data == "Yardım":
        await update.message.edit_text(
            text=lang.HELP_TEXT.format(Var.UPDATES_CHANNEL),
            disable_web_page_preview=True,
            reply_markup=BUTTON.HELP_BUTTONS
        )
    elif update.data == "Hakkında":
        await update.message.edit_text(
            text=lang.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=BUTTON.ABOUT_BUTTONS
        )
    elif update.data == "Kapat":
        await update.message.delete()
    elif update.data == "msgdeleted":
        await update.answer(random.choice(deldbtnmsg), show_alert=True)
    else:
        usr_cmd = update.data.split("_")
        if usr_cmd[0] == "msgdelconf2":
            await update.message.edit_text(
            text=update.message.text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅", callback_data=f"msgdelyes_{usr_cmd[1]}_{usr_cmd[2]}"), InlineKeyboardButton("❌", callback_data=f"msgdelno_{usr_cmd[1]}_{usr_cmd[2]}")]])
        )
        elif usr_cmd[0] == "msgdelno":
            get_msg = await bot.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd[1]))
            if get_media_file_unique_id(get_msg) == usr_cmd[2]:
                reply_markup, Stream_Text, stream_link = await gen_link(m=update, log_msg=get_msg, from_channel=False)

                await update.message.edit_text(
                text=Stream_Text,
                disable_web_page_preview=True,
                reply_markup=reply_markup
                )            
            else:
                await update.answer("Message id and file_unique_id miss match", show_alert=True)
        elif usr_cmd[0] == "msgdelyes":
            try:
                resp = await bot.get_messages(Var.BIN_CHANNEL, int(usr_cmd[1]))
                if get_media_file_unique_id(resp) == usr_cmd[2]:
                    await bot.delete_messages(
                        chat_id=Var.BIN_CHANNEL,
                        message_ids=int(usr_cmd[1])
                    )
                    await update.message.edit_text(
                    text=update.message.text,
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Link Silindi", callback_data="msgdeleted")]])
                    )
                elif resp.empty:
                    await update.answer("Sorry Your File is Missing from the Server", show_alert=True)
                else:
                    await update.answer("Message id and file_unique_id miss match", show_alert=True)
            except MessageDeleteForbidden as e:
                print(e)
                await bot.send_message(
                    chat_id=Var.BIN_CHANNEL,
                    text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`\n#Delete_Link", disable_web_page_preview=True, 
                )
                await update.answer(text='Message too old', show_alert=True)
            except Exception as e:
                print(e)
                error_id=await bot.send_message(
                    chat_id=Var.BIN_CHANNEL,
                    text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`\n#Delete_Link", disable_web_page_preview=True, 
                )
                await update.message.reply_text(
                    text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `message-id={error_id.message_id}`\nYardım için[Dark Enza](https://t.me/dark_enza)", disable_web_page_preview=True,
                )
        else:
            await update.message.delete()