from pyrogram import Client, errors
import config
from ..logging import LOGGER

class Userbot:
    def __init__(self):
        self.assistants = []
        self.assistant_ids = []

        self.sessions = {
            "AnonXAss1": config.STRING1,
            "AnonXAss2": config.STRING2,
            "AnonXAss3": config.STRING3,
            "AnonXAss4": config.STRING4,
            "AnonXAss5": config.STRING5,
        }

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        for name, session in self.sessions.items():
            if not session:
                continue  # Skip if session string is missing

            client = Client(
                name=name,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=session,
                no_updates=True,
            )

            try:
                await client.start()
                bot_info = await client.get_me()  # Fetch bot info after start

                self.assistants.append(client)
                self.assistant_ids.append(bot_info.id)

                LOGGER(__name__).info(f"Assistant {bot_info.mention} Started.")

                # Join required chats
                chat_list = [
                    "AmBotYT", "AM_YTSupport", "AbhiModszYT_Return",
                    "AM_Unfban", "Logs_Gban", "About_AMBot",
                    "Fbans_Logs", "SpicyEmpireSupport", "SpicyEmpire",
                    "SpicyEmpireFban"
                ]

                for chat in chat_list:
                    try:
                        await client.join_chat(chat)
                    except errors.RPCError as e:
                        LOGGER(__name__).warning(f"Failed to join {chat}: {e}")

                # Log assistant startup in the logging group
                try:
                    await client.send_message(config.LOGGER_ID, "Assistant Started")
                except errors.RPCError as e:
                    LOGGER(__name__).error(
                        f"Assistant {bot_info.mention} failed to access the log group. "
                        "Ensure the assistant is added and promoted. Error: {e}"
                    )
                    await client.stop()
                    continue

            except Exception as e:
                LOGGER(__name__).error(f"Failed to start {name}: {e}")
                continue  # Move to the next assistant

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for client in self.assistants:
            try:
                await client.stop()
            except Exception as e:
                LOGGER(__name__).warning(f"Error stopping assistant {client.name}: {e}")
