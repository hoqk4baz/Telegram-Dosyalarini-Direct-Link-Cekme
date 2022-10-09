from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Selam, {}**\n
<i>Ben Telegram Dosyaları için Doğrudan Bağlantı Üreticisiyim</i>\n
<i>Daha Fazla Bilgi Almak İçin Yardıma Tıklayın</i>\n
<b><i><u>Uyarı 🚸</u></i></b>\n
<b>🔞 Porn İçeriği Kalıcı Olarak Yasaklanmanıza Yol Açar.</b>"""

        HELP_TEXT = """🔰 **Beni Nasıl Kullanırsın?**
<i>- Bana Telegram'dan Herhangi Bir Dosya veya Medya Gönder.</i>
<i>- Senin için Harici Direct İndirme Bağlantısı Sağlayacağım!</i>
**Bağlantılarda Download Mb/s Sınırı yoktur ⚡️**
<b><i><u>Uyarı🚸</u></i></b>
<b>🔞 Porn İçeriği Kalıcı Olarak Yasaklanmanıza Yol Açar.</b></b>\n
<i>Hatalar karşısında Yapımcı ile İletişime geçin</i> <b>: <a href='https://t.me/dark_enza'>[ TIKLA ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ BoT İSMİ : 🇹🇷TrAppleDestek-IPA-Link🇹🇷</b>\n
<b>⚜ Username : @trappledestekipalink_bot</b>\n
<b>🔸Version : 1.0</b>\n
<b>🔹Last Updated : [ 09-Ekim-22 ]</b>
"""

        stream_msg_text ="""
<u>**Link Başarı ile Oluşturuldu !**</u>\n
<b>📂 Dosya İsmi :</b> {}\n
<b>📦 Dosya Boyutu :</b> {}\n
<b>📥 İNDİRME Linki :</b> {}\n
<b>🖥 Kısa Link :</b> {}"""

        ban_text="Üzgünüm Dostum Kullanımın Yasaklandı\n\n**[Yapımcı ile İletişime Geç](https://t.me/dark_enza) Sana Yardımı olucaktır**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],        
        [InlineKeyboardButton("Grubumuz İçin Tıkla", url='https://t.me/TrappledestekCom'),
        InlineKeyboardButton("Repo", url='https://github.com/hoqk4baz/Telegram-Dosyalarini-Direct-Link-Cekme')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
