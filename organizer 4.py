import discord
from discord.ext import commands

TOKEN = 'MTIxODg2NDI5NjQ2NTc5MzA2NQ.G2gybO.VgkIIhK5fxDfAHKY_wbHxi4Ugr4iwN5mouH8PU'

# Botunuzun ön ekini belirleyin
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())  

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rtb')
async def rutbe(ctx):
    # Kullanıcının rütbelerini kontrol et
    member = ctx.author
    member_roles = member.roles
    
    # Kullanıcının en yüksek rütbesini bul
    highest_role = None
    for role in member_roles:
        if role != ctx.guild.default_role:  # Varsayılan rolü atla
            if highest_role is None or role.position > highest_role.position:
                highest_role = role

    if highest_role:
        await ctx.send(f"{member.mention}, en yüksek rütbeniz: {highest_role.name}.")
    else:
        await ctx.send(f"{member.mention}, rütbeniz bulunamadı.")

bot.run(TOKEN)