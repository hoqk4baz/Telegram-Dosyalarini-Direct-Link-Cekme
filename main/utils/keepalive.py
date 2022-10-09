import asyncio
import logging
import aiohttp
import traceback
from main import Var


async def ping_server():
    sleep_time = Var.PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(Var.URL) as resp:
                    logging.info("Yanıt veren ping sunucusu: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Site URL'sine bağlanılamadı..!")
        except Exception:
            traceback.print_exc()