import disnake
from disnake.ext import commands
from main import bot

class Events(commands.Cog):
    def __init__(self, bot = commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'\nИмя бота: {bot.user}\n')
        print(f'Id Бота: {bot.user.id}\n')
        print(f'Сервера бота: {len(bot.guilds)}\n')
        print(f'Disnake Версия: {disnake.__version__}')
    
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = bot.get_channel( 777231861445296185 )
        role = disnake.utils.get(member.guild.roles, id = 777231860685078597 )
        await member.add_roles(role)
        await channel.send(embed = disnake.Embed(description = 'Пользователь' f"{member.mention}" ' , присоединился к нам!'))


def setup(bot:commands.Bot):
    bot.add_cog(Events(bot))
    print(f"Extension {__name__} is ready")

