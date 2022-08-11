import disnake
from disnake.ext import commands
from main import bot
from datetime import time

class SlashCommands (commands.Cog):
    def __init__(self, bot = commands.Bot):
        self.bot = bot


    @commands.slash_command(description='Выводит список команд')
    async def help(self, inter):
        msg = 'Это будущая команда хелп'
        await inter.response.send_message(msg)

    @commands.slash_command(description = 'Выводит информацию о сервере' )
    async def server(self, inter):
        
        date_format = "%Y-%m-%d | %H:%m"

        bots_count = len(([member for member in inter.guild.members if member.bot]))
        members_count = len(inter.guild.members) - bots_count



        embed = disnake.Embed(title='Информация о сервере')
        embed.add_field(name = '**Название сервера:**', value = f'```{inter.guild.name}```', inline = True)      
        embed.add_field(name = '**Id Владельца:**', value = f'```{inter.guild.owner_id}```', inline = True) 
        embed.add_field(name = f"**Участников сервера: {[len(inter.guild.members)]}**",value = f'```Участники: {members_count}| Боты: {bots_count}```', inline= False)
        embed.add_field(name = '**Айди сервера:**', value = f"```{inter.guild.id}```", inline = False)
        embed.add_field(name = '**Язык Сервера:**', value = f"```{inter.guild.preferred_locale}```", inline= False)
        embed.add_field(name = '**Уровень Nitro:**', value = f"```{inter.guild.premium_tier}```", inline = True )
        embed.add_field(name = '**Общее количество бустов:**', value =f"```{inter.guild.premium_subscription_count}```", inline = True)
        embed.add_field(name = '**Дата создание сервера:**', value = f"```{inter.guild.created_at.strftime(date_format)}``` ", inline = False) 
        
        await inter.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SlashCommands(bot))
    print(f"Extension {__name__} is ready")
