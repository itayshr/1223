import discord
import os
from discord.ext import commands

# הגדרת הרשאות (Intents) - חשוב להפעיל אותן גם ב-Discord Developer Portal
intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    # כאן צריך להזין את ה-ID של הערוץ שבו תרצה שההודעה תשלח
    channel_id = int(os.getenv("1449406834032250931"))
    channel = bot.get_channel(channel_id)
    
    if channel:
        guild = member.guild
        member_count = guild.member_count
        
        # יצירת ה-Embed (ההודעה המעוצבת)
        embed = discord.Embed(
            description=f"**Hey <@{member.id}>, Welcome to `Phantom-Israel | Serious Roleplay V2`! We're `{member_count}` members now.**",
            color=discord.Color.from_rgb(43, 45, 49) # צבע כהה כמו בתמונה
        )
        
        # הוספת ה-Footer (החלק התחתון)
        embed.set_footer(text="Dev: Frozen")
        
        # הוספת תמונת הלוגו של דיסקורד בצד (Thumbnail)
        # בתמונה שלך זה ורוד, אפשר לשים לינק לתמונה ספציפית
        embed.set_thumbnail(url="https://i.imgur.com/Z95303n.png") 

        await channel.send(embed=embed)

# הרצת הבוט עם הטוקן מ-Railway
bot.run(os.getenv("DISCORD_TOKEN"))
