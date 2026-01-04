import discord
import os
from discord.ext import commands

# הגדרת הרשאות
intents = discord.Intents.default()
intents.members = True          
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'--- הבוט {bot.user.name} מוכן לעבודה! ---')

@bot.event
async def on_member_join(member):
    channel_id = os.getenv("WELCOME_CHANNEL_ID")
    if not channel_id:
        return
        
    channel = bot.get_channel(int(channel_id))
    
    if channel:
        guild = member.guild
        
        # הגדרת הקישור לערוץ החוקים (החלף את ה-ID במידת הצורך)
        rules_channel_id = "1450833843690012834"
        rules_link = f"https://discord.com/channels/{guild.id}/{rules_channel_id}"
        
        # יצירת ה-Embed
        embed = discord.Embed(
            title="שלום רב !!",
            description=f"<@{member.id}>\n\n"
                        f"**ברוך/ה הבא/ה לשרת GameLife**\n"
                        f"אנו ממליצים לך לעבור על [חוקי השרת]({rules_link}) לפני כניסתך לשרת המשחק "
                        f"בכדי לאפשר עבורך ועבור שאר השחקנים חווית משחק מהנה ואיכותית יותר\n\n"
                        f"**שיהיה בהצלחה !! ❤️**",
            color=discord.Color.blue()
        )
        
        if guild.icon:
            embed.set_author(name=f"{guild.name} ", icon_url=guild.icon.url)
            embed.set_thumbnail(url=guild.icon.url)
        
        # הוספת הבאנר מהקישור שלך
        embed.set_image(url="https://i.postimg.cc/nLBxnSyv/Gemini-Generated-Image-4rq61h4rq61h4rq6-(1).png")
        
        footer_icon = guild.icon.url if guild.icon else None
        embed.set_footer(text="GameLife", icon_url=footer_icon)

        await channel.send(embed=embed)

@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

bot.run(os.getenv("DISCORD_TOKEN"))
