"""
persona.py – Persona selection and temporary override commands.
Includes:
- /botpersona: persona picker using a dropdown UI
- /reloadpersonas: reloads persona JSONs on disk
- /tempsona: sets temporary persona memory
"""

import discord
from discord.ext import commands
from discord import app_commands, Interaction

from utils.bot_data import bot_data_manager
from personas.loader import load_persona


class PersonaView(discord.ui.View):
    def __init__(self, guild_id: str):
        super().__init__(timeout=60)
        self.guild_id = str(guild_id)

        options = [
            discord.SelectOption(
                label=persona,
                description=f"Use the {persona} persona",
                value=persona
            )
            for persona in bot_data_manager.personas.keys()
        ]

        self.add_item(PersonaSelect(options, self.guild_id))


class PersonaSelect(discord.ui.Select):
    def __init__(self, options, guild_id: str):
        self.guild_id = str(guild_id)
        super().__init__(placeholder="Choose a persona...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]

        try:
            persona = load_persona(selected)
            key = self.guild_id
            # Ensure channel is tracked
            if key not in bot_data_manager.channels:
                bot_data_manager.add_channel(self.guild_id, None)
            print(f"[DEBUG] /botpersona selected persona '{selected}' for guild: {self.guild_id}")



            # ✅ Apply selected persona
            channel_data = bot_data_manager.channels[key]
            channel_data.bot_persona = selected
            channel_data.bot_override_memory = ""
            channel_data.chat_history = []  # Optional: fresh start
            bot_data_manager.export_config()

            print(f"[SELECT] Persona set to {selected} for channel {self.guild_id}")

            await interaction.response.send_message(
                f"✅ Persona set to **{persona.display_name or persona.name}**.",
                ephemeral=True
            )

        except Exception as e:
            await interaction.response.send_message(f"❌ Failed to load persona '{selected}': {e}", ephemeral=True)



class PersonaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_manager = bot_data_manager

    @app_commands.command(name="botpersona", description="Change or view available personas")
    async def botpersona(self, interaction: Interaction):
        guild_id = str(interaction.guild_id)
        view = PersonaView(guild_id=guild_id)
        
        await interaction.response.send_message("Choose a persona:", view=view, ephemeral=True)

    @app_commands.command(name="reloadpersonas", description="Reload all personas from disk")
    async def reloadpersonas(self, interaction: Interaction):
        try:
            self.data_manager.load_personas()
            await interaction.response.send_message("✅ Personas reloaded from disk.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Failed to reload personas: {e}", ephemeral=True)

    @app_commands.command(name="tempsona", description="Temporarily override the bot's persona for this server.")
    @app_commands.describe(memory="Custom persona memory or behavior instructions.")
    async def tempsona(self, interaction: Interaction, memory: str):
        guild_id = str(interaction.guild_id)

        if guild_id not in self.data_manager.channels:
            self.data_manager.add_channel(guild_id, None)

        channel_data = self.data_manager.channels[guild_id]
        channel_data.chat_history = []
        channel_data.bot_override_memory = memory.strip()

        self.data_manager.export_config()
        await interaction.response.send_message("✅ Temporary persona memory set for this server.", ephemeral=True)


    @commands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.bot.tree.sync()
            print(f"[persona.py] Synced {len(synced)} command(s).")
        except Exception as e:
            print(f"[persona.py] Sync failed: {e}")

print("[DEBUG] Channels currently being tracked:")
for key in bot_data_manager.channels:
    print(f" - {key}")
    
async def setup(bot):
    await bot.add_cog(PersonaCog(bot))  