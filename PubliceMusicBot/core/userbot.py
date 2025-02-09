from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AmBotYT")
                await self.one.join_chat("AM_YTSupport")
                await self.one.join_chat("AbhiModszYT_Return")
                await self.one.join_chat("AM_Unfban")
                await self.one.join_chat("Logs_Gban")
                await self.one.join_chat("About_AMBot")
                await self.one.join_chat("Fbans_Logs")
                await self.one.join_chat("SpicyEmpireSupport")
                await self.one.join_chat("SpicyEmpire")
                await self.one.join_chat("SpicyEmpireFban")
            except:
                pass
            assistants.append(1)

