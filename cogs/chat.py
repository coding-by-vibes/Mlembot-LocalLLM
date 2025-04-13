# chat.py

import discord
from discord import app_commands, Interaction
import time
from discord.ext import commands

from utils.bot_data import bot_data_manager
from personas.loader import load_persona
from personas.prompt_builder import build_prompt
from utils.api import query_koboldcpp
from utils.history import wipe_channel_history

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_manager = bot_data_manager
        self.processed_message_ids = set()  # ✅ Prevent double-processing

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # ✅ Skip if message is from a bot (including self)
        if message.author.bot:
            return

        # ✅ Skip if we've already processed this message
        if message.id in self.processed_message_ids:
            return
        self.processed_message_ids.add(message.id)

        guild_id = str(message.guild.id)
        channel_key = guild_id  # 👈 persona/memory now scoped by guild/server
        print(f"[DEBUG] on_message using channel_key: {channel_key}")

        if channel_key not in self.data_manager.channels:
            self.data_manager.add_channel(guild_id, None)

        is_reply_to_bot = self._is_reply_to_bot(message)
        mentions_bot = self.bot.user in message.mentions
        contains_bot_name = self._contains_bot_name(message)

        if is_reply_to_bot or mentions_bot or contains_bot_name:
            await self._process_interaction(message, channel_key)


    def _is_reply_to_bot(self, message: discord.Message) -> bool:
        if message.reference and message.reference.resolved:
            try:
                return message.reference.resolved.author == self.bot.user
            except AttributeError:
                return False
        return False

    def _contains_bot_name(self, message: discord.Message) -> bool:
        return (
            self.bot.user.display_name.lower() in message.clean_content.lower()
            or self.bot.user.name.lower() in message.clean_content.lower()
        )

    async def _process_interaction(self, message: discord.Message, channel_key: str) -> None:
        channel_data = self.data_manager.channels[channel_key]  # ⬅️ ensures you get the updated persona
        print(f"[DEBUG] _process_interaction loaded bot_persona: {channel_data.bot_persona}")

        metadata = {
            "is_reply": self._is_reply_to_bot(message),
            "mentions_bot": self.bot.user in message.mentions,
            "contains_bot_name": self._contains_bot_name(message)
        }
        channel_data.add_message(message.author.display_name, message.clean_content, metadata)
        if message.author.bot:
            channel_data.bot_botloopcount += 1
        else:
            channel_data.bot_botloopcount = 0

        if channel_data.bot_botloopcount > 4:
            return
        elif channel_data.bot_botloopcount == 4:
            if time.time() - channel_data.bot_reply_timestamp < channel_data.bot_loop_timeout:
                await message.channel.send("🛑 Bot loop detected.")
            return

        if channel_data.busy.acquire(blocking=False):
            try:
                async with message.channel.typing():
                    channel_data.bot_reply_timestamp = time.time()
                    persona = load_persona(channel_data.bot_persona)
                    print(f"[DEBUG] Loaded persona file: {persona.name}")
                    memory = channel_data.bot_override_memory or persona.memory

                    recent_history = "\n".join(
                        f"{msg.author}: {msg.content}"
                        for msg in channel_data.get_recent_messages(limit=5)
                    )

                    prompt = build_prompt(persona, recent_history, message.clean_content)

                    response = await query_koboldcpp(
                        prompt=prompt,
                        settings=persona.kobold_settings,
                        memory=memory
                    )

                    if response:
                        for tag in ["User:", f"{persona.name}:", "\nUser:", f"\n{persona.name}:"]:
                            if tag in response:
                                response = response.split(tag)[0].strip()
                                break

                    # if response:
                    #     # 1. Hard-cut at first newline (like KoboldAI client)
                    #     response = response.split("\n")[0].strip()

                    #     # 2. Cut at next speaker tag (dynamic)
                    #     for tag in ["User:", f"{persona.name}:", "\nUser:", f"\n{persona.name}:"]:
                    #         if tag in response:
                    #             response = response.split(tag)[0].strip()
                    #             break

                        # 3. Cut if it's too long for Discord
                        if len(response) > 2000:
                            print(f"[WARN] Truncating response over 2000 characters.")
                            response = response[:1990] + "… [truncated]"

                        channel_data.add_message(self.bot.user.display_name, response)
                        await message.channel.send(response)
            finally:
                channel_data.busy.release()

    @app_commands.command(name="wipememory", description="Clear this channel's chat memory (both in RAM and on disk)")
    async def wipememory(self, interaction: Interaction):
        channel_key = str(interaction.guild_id)
        if channel_key in self.data_manager.channels:
            self.data_manager.channels[channel_key].chat_history = []
            wipe_channel_history(channel_key)
            await interaction.response.send_message("🧠 Chat memory wiped for this channel.", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ This channel has no active memory.", ephemeral=True)




# ✅ Required setup() function for Discord to load the cog
async def setup(bot):
    await bot.add_cog(ChatCog(bot))
