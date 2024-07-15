import sys
import logging
from aiohttp import web
from pyrogram import Client
from datetime import datetime
from config import (API_HASH, APP_ID, TG_BOT_TOKEN, FORCE_SUB_CHANNEL, 
                    FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, 
                    CHANNEL_ID, PORT)
from plugins.web_server import web_server


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = logging.getLogger(__name__)

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        force_sub_channels = [FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4]
        self.invite_links = {}

        for i, channel in enumerate(force_sub_channels, start=1):
            if channel:
                try:
                    link = (await self.get_chat(channel)).invite_link
                    if not link:
                        await self.export_chat_invite_link(channel)
                        link = (await self.get_chat(channel)).invite_link
                    self.invite_links[f'invitelink{i}'] = link
                except Exception as a:
                    self.LOGGER.warning(a)
                    self.LOGGER.warning(f"Bot can't Export Invite link from Force Sub Channel {channel}!")
                    self.LOGGER.warning(f"Please Double check the {channel} value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {channel}")
                    self.LOGGER.info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER.warning(e)
            self.LOGGER.warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER.info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER.info(f"Bot Running..!\n\nCreated by \nhttps://t.me/CodeXBotz")
        self.LOGGER.info(f""" \n\n       
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
                                          """)
        self.username = usr_bot_me.username
        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")
