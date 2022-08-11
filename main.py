import disnake
from disnake.ext import commands
from settings import TOKEN


bot = commands.Bot(command_prefix='.', intents = disnake.Intents.all(), activity = disnake.Game('Vs code', status = disnake.Status.online))

bot.remove_command('help')

bot.load_extension("cogs.event_commands")
bot.load_extension("cogs.slash_commands")





bot.run(TOKEN)