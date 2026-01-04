import discord
import os
from discord.ext import commands

# הגדרת הרשאות (Intents)
intents = discord.Intents.default()
intents.members = True          
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'--- הבוט {bot.user.name} מחובר! ---')

@bot.event
async def on_member_join(member):
    # שליפת ID של הערוץ מ-Railway
    channel_id = os.getenv("WELCOME_CHANNEL_ID")
    if not channel_id:
        return
        
    channel = bot.get_channel(int(channel_id))
    
    if channel:
        guild = member.guild
        
        # יצירת ה-Embed
        embed = discord.Embed(
            title="שלום רב !!",
            description=f"<@{member.id}>\n\n"
                        f"**ברוך/ה הבא/ה לשרת ה Fivem Roleplay של קהילת**\n"
                        f"**{guild.name}**\n\n"
                        f"אנו ממליצים לך לעבור על [חוקי השרת](https://google.com) לפני כניסתך לשרת המשחק "
                        f"בכדי לאפשר עבורך ועבור שאר השחקנים חווית משחק מהנה ואיכותית יותר\n\n"
                        f"**שיהיה בהצלחה !! ❤️**",
            color=discord.Color.blue()
        )
        
        # הגדרת כותרת עליונה עם שם השרת והלוגו שלו
        embed.set_author(name=f"{guild.name} | Serious Roleplay", icon_url=guild.icon.url if guild.icon else None)
        
        # הגדרת התמונה בצד (Thumbnail) כתמונת השרת
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        # פוטר עם שם השרת
        embed.set_footer(text=guild.name, icon_url=guild.icon.url if guild.icon else None)

        await channel.send(embed=embed)

# פקודת בדיקה - כתוב !test בשרת
@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

# הרצת הבוט
bot.run(os.getenv("DISCORD_TOKEN"))
