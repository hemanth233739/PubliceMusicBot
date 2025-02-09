from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
import config
from ..logging import LOGGER

class PubliceMusic(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name="PubliceMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        # Fetch bot info explicitly
        bot_info = await self.get_me()
        self.id = bot_info.id
        self.name = bot_info.first_name + " " + (bot_info.last_name or "")
        self.username = bot_info.username
        self.mention = bot_info.mention

