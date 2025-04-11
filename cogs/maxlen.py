from discord.ext import commands
from discord import app_commands, Interaction

class MaxLen(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="botmaxlen", description="Set the maximum response length")
    @app_commands.describe(length="Max number of tokens or characters in a response")
    async def botmaxlen(self, interaction: Interaction, length: int):
        await interaction.response.send_message(f"Max response length set to: {length}", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(MaxLen(bot))
