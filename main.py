import discord
import os
from discord.ext import commands

# הגדרת הרשאות (Intents)
# חשוב: וודא שכל ה-Intents מופעלים ב-Discord Developer Portal
intents = discord.Intents.default()
intents.members = True          # מאפשר לזהות כניסת משתמשים
intents.message_content = True  # מאפשר לקרוא תוכן הודעות (לפקודות)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'--- הבוט מחובר בהצלחה! ---')
    print(f'שם הבוט: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'-----------------------')

@bot.event
async def on_member_join(member):
    # שליפת ה-ID של הערוץ מהמשתנים של Railway
    channel_id_env = os.getenv("1449406834032250931")
    
    if channel_id_env is None:
        print("Error: WELCOME_CHANNEL_ID variable is not set in Railway!")
        return

    channel = bot.get_channel(int(channel_id_env))
    
    if channel:
        guild = member.guild
        member_count = guild.member_count
        
        # יצירת ה-Embed (הודעה מעוצבת)
        embed = discord.Embed(
            description=f"**Hey <@{member.id}>, Welcome to `Phantom-Israel | Serious Roleplay V2`! We're `{member_count}` members now.**",
            color=discord.Color.from_rgb(43, 45, 49) # צבע רקע כהה
        )
        
        # הוספת ה-Footer
        embed.set_footer(text="Dev: Frozen")
        
        # תמונת הלוגו (השתמש בקישור ישיר לתמונה שלך אם יש)
        embed.set_thumbnail(url="https://i.imgur.com/Z95303n.png") 

        await channel.send(embed=embed)

# פקודת בדיקה - כתוב !test בערוץ כדי לראות איך ההודעה נראית
@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

# הרצת הבוט
token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("Error: DISCORD_TOKEN variable is not set in Railway!")
