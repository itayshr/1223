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
                        f"**Gamers-Israel | 🇬**\n\n"
                        f"אנו ממליצים לך לעבור על [חוקי השרת](https://google.com) לפני כניסתך לשרת המשחק "
                        f"בכדי לאפשר עבורך ועבור שאר השחקנים חווית משחק מהנה ואיכותית יותר\n\n"
                        f"**שיהיה בהצלחה !! ❤️**",
            color=discord.Color.blue()
        )
        
        # לוגו השרת בצד ימין למעלה
        if guild.icon:
            embed.set_author(name=f"{guild.name} | Serious Roleplay", icon_url=guild.icon.url)
            embed.set_thumbnail(url=guild.icon.url)
        
        # --- הוספת הבאנר של GameLife מתחת לכיתוב (התמונה הגדולה) ---
        embed.set_image(url="https://storage.googleapis.com/public-assets-x/image_10a2a3.jpg")
        
        # פוטר בתחתית
        embed.set_footer(text="GAMERS ISRAEL", icon_url=guild.icon.url if guild.icon else None)

        await channel.send(embed=embed)

# פקודת בדיקה - כתוב !test בשרת
@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

bot.run(os.getenv("DISCORD_TOKEN"))
