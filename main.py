import discord
import os
from discord.ext import commands

# הגדרת הרשאות (Intents)
intents = discord.Intents.default()
intents.members = True          # מאפשר לזהות כניסת משתמשים חדשים
intents.message_content = True  # מאפשר לבוט לקרוא את הפקודה !test

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'--- הבוט {bot.user.name} מוכן לעבודה! ---')

@bot.event
async def on_member_join(member):
    # שליפת ID של הערוץ מתוך משתני הסביבה של Railway
    channel_id = os.getenv("WELCOME_CHANNEL_ID")
    if not channel_id:
        print("שגיאה: לא הוגדר WELCOME_CHANNEL_ID ב-Railway")
        return
        
    channel = bot.get_channel(int(channel_id))
    
    if channel:
        guild = member.guild
        
        # יצירת ה-Embed (הודעת הברוך הבא)
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
        
        # הגדרת לוגו השרת בצד (Thumbnail)
        if guild.icon:
            embed.set_author(name=f"{guild.name} | Serious Roleplay", icon_url=guild.icon.url)
            embed.set_thumbnail(url=guild.icon.url)
        
        # --- הוספת הבאנר החדש מ-Postimages ---
        # הקישור הישיר שסיפקת:
        embed.set_image(url="https://i.postimg.cc/GtpHf1HN/Gemini-Generated-Image-4rq61h4rq61h4rq6-(1).png")
        
        # פוטר בתחתית
        footer_icon = guild.icon.url if guild.icon else None
        embed.set_footer(text="GAMERS ISRAEL", icon_url=footer_icon)

        # שליחת ההודעה
        await channel.send(embed=embed)

# פקודת בדיקה - כתוב !test בערוץ בשרת
@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

# הרצת הבוט
bot.run(os.getenv("DISCORD_TOKEN"))
