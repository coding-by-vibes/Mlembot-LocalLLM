from discord.ext import commands
from discord import app_commands, Interaction
from utils.bot_data import bot_data_manager
from utils.constants import BOT_DEFAULTS

class TweakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_manager = bot_data_manager

    @app_commands.command(name="settemperature", description="Set response temperature for this server.")
    async def set_temperature(self, interaction: Interaction, value: float):
        guild_id = str(interaction.guild_id)
        if not (0 <= value <= 2):
            await interaction.response.send_message("Please provide a temperature between 0.0 and 2.0.", ephemeral=True)
            return

        if guild_id in self.data_manager.channels:
            channel = self.data_manager.channels[guild_id]
            channel.temperature = value
            self.data_manager.export_config()
            await interaction.response.send_message(f"✅ Temperature set to `{value}` for this server.", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ This server has not been initialized yet.", ephemeral=True)

    @app_commands.command(name="setmaxlen", description="Set max response length (tokens) for this server.")
    async def set_max_length(self, interaction: Interaction, value: int):
        guild_id = str(interaction.guild_id)
        if value < 100 or value > 1000:
            await interaction.response.send_message("Please provide a length between 100 and 1000.", ephemeral=True)
            return

        if guild_id in self.data_manager.channels:
            channel = self.data_manager.channels[guild_id]
            channel.bot_maxlen = value
            self.data_manager.export_config()
            await interaction.response.send_message(f"✅ Max response length set to `{value}` tokens.", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ This server has not been initialized yet.", ephemeral=True)

    @app_commands.command(name="getsettings", description="Show current response settings for this server.")
    async def get_settings(self, interaction: Interaction):
        guild_id = str(interaction.guild_id)
        if guild_id not in self.data_manager.channels:
            await interaction.response.send_message("⚠️ This server has not been initialized yet.", ephemeral=True)
            return

        channel = self.data_manager.channels[guild_id]
        msg = (
            f"**Settings for this server:**\n"
            f"- Temperature: `{channel.temperature}`\n"
            f"- Max Response Length: `{channel.bot_maxlen}` tokens\n"
            f"- Persona: `{channel.bot_persona}`\n"
            f"- Memory Override: `{bool(channel.bot_override_memory)}`"
        )
        await interaction.response.send_message(msg, ephemeral=True)

    @app_commands.command(name="resetsettings", description="Reset temperature and response length for this server.")
    async def reset_settings(self, interaction: Interaction):
        guild_id = str(interaction.guild_id)
        if guild_id not in self.data_manager.channels:
            await interaction.response.send_message("⚠️ This server has not been initialized yet.", ephemeral=True)
            return

        channel = self.data_manager.channels[guild_id]
        channel.temperature = BOT_DEFAULTS["temperature"]
        channel.bot_maxlen = BOT_DEFAULTS["default_max_response_length"]
        self.data_manager.export_config()
        await interaction.response.send_message("✅ Server response settings have been reset to defaults.", ephemeral=True)

# Required setup() function
async def setup(bot):
    await bot.add_cog(TweakCog(bot))
