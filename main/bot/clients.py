import asyncio
import logging
from ..vars import Var
from pyrogram import Client
from main.utils import TokenParser
from . import multi_clients, work_loads, StreamBot


async def initialize_clients():
    SESSION_STRING_SIZE = 351
    multi_clients[0] = StreamBot
    work_loads[0] = 0
    all_tokens = TokenParser().parse_from_env()
    if not all_tokens:
        print("Varsayilan istemci kullanilarak ek istemci bulunamadi")
        return
    
    async def start_client(client_id, token):
        try:
            if len(token) >= 351:
                session_name=token
                bot_token=None
                print(f"İstemci - Baslatildi {client_id} Session Strings kullanilarak")
            else:
                session_name=":memory:"
                bot_token=token
                print(f"İstemci - Baslatildi {client_id}  Bot Tokeni kullanilarak")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                print("Bu biraz zaman alicak lutfen bekleyin..")
            client = await Client(
                session_name=session_name,
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=bot_token,
                sleep_threshold=Var.SLEEP_THRESHOLD,
                no_updates=True,
            ).start()
            work_loads[client_id] = 0
            return client_id, client
        except Exception:
            logging.error(f"İstemci baslatilma hatasi - {client_id} Error:", exc_info=True)
    
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    multi_clients.update(dict(clients))
    if len(multi_clients) != 1:
        Var.MULTI_CLIENT = True
        print("Multi-Client Mod Aktif")
    else:
        print("Varsayilen istemci kullanilarak ek istemci baslatilmadi")
