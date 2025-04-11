from discord.ext import commands
from discord import app_commands, Interaction

class Sleep(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="botsleep", description="Put the bot to sleep")
    async def botsleep(self, interaction: Interaction):
        await interaction.response.send_message("Bot is now sleeping. Zzz...", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Sleep(bot))
