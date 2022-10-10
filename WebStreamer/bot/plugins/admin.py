import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from WebStreamer.utils.broadcast_helper import send_msg
from WebStreamer.utils.database import Database
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums.parse_mode import ParseMode
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
broadcast_ids = {}


@StreamBot.on_message(filters.command("durum") & filters.private & filters.user(Var.OWNER_ID))
async def sts(c: Client, m: Message):
    total_users = await db.total_users_count()
    await m.reply_text(text=f"**Toplam Kullanıcılar:** `{total_users}`", parse_mode=ParseMode.MARKDOWN, quote=True)


@StreamBot.on_message(filters.command("duyur") & filters.private & filters.user(Var.OWNER_ID) & filters.reply)
async def broadcast_(c, m):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"𝐃𝐮𝐲𝐮𝐫𝐮 𝐲𝐚𝐩𝛊𝐥𝐝𝛊,𝐁𝐢𝐥𝐠𝐢𝐥𝐞𝐫 𝐡𝐞𝐦𝐞𝐧 𝐠𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"𝐃𝐮𝐲𝐮𝐫𝐮 𝐓𝐚𝐦𝐚𝐦𝐥𝐚𝐧𝐝𝛊 `{completed_in}`\n\n𝚃𝚘𝚙𝚕𝚊𝚖 𝚔𝚞𝚕𝚕𝚊𝚗ｪ𝚌ｪ𝚕𝚊𝚛 {total_users}.\n𝚃𝚘𝚙𝚕𝚊𝚖 𝚞𝚕𝚊𝚜̧ｪ𝚕𝚊𝚗 {done}, {success} 𝐛𝐚𝐬̧𝐚𝐫𝛊𝐥𝛊 𝐯𝐞 {failed} 𝐛𝐚𝐬̧𝐚𝐫𝛊𝐬𝛊𝐳.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"𝐃𝐮𝐲𝐮𝐫𝐮 𝐓𝐚𝐦𝐚𝐦𝐥𝐚𝐧𝐝𝛊 `{completed_in}`\n\n𝚃𝚘𝚙𝚕𝚊𝚖 𝚔𝚞𝚕𝚕𝚊𝚗ｪ𝚌ｪ𝚕𝚊𝚛 {total_users}.\n𝚃𝚘𝚙𝚕𝚊𝚖 𝚞𝚕𝚊𝚜̧ｪ𝚕𝚊𝚗 {done}, {success} 𝐛𝐚𝐬̧𝐚𝐫𝛊𝐥𝛊 𝐯𝐞 {failed} 𝐛𝐚𝐬̧𝐚𝐫𝛊𝐬𝛊𝐳.",
            quote=True
        )
    os.remove('broadcast.txt')
