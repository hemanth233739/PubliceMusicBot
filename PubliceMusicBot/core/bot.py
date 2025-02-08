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

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except errors.ChatAdminRequired:
            LOGGER(__name__).error("Bot lacks admin rights in the log group/channel.")
            await self.stop()
            return
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Invalid log group/channel. Ensure the bot is added."
            )
            await self.stop()
            return
        except Exception as ex:
            LOGGER(__name__).error(
                f"Failed to access the log group/channel. Reason: {type(ex).__name__}."
            )
            await self.stop()
            return

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Bot...")
        await super().stop()
