import os
import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

class PoloView(discord.ui.View):
    def __init__(self, target_message):
        super().__init__(timeout=None)
        self.target_message = target_message

    @discord.ui.button(label="Spam", style=discord.ButtonStyle.red)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("送信中...", ephemeral=True)
        for _ in range(3):
            await self.target_message.reply("@everyone discord.gg/ozeu  #Join Now !!")

@bot.tree.command(name="polo", description="Spam Message by ozeu 😈")
async def polo(interaction: discord.Interaction):
    await interaction.response.send_message("ボタンを押すとメッセージが3回返信されます", ephemeral=True)
    sent = await interaction.original_response()
    view = PoloView(sent)
    await sent.edit(view=view)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Sync error: {e}")

keep_alive()
bot.run(TOKEN)
