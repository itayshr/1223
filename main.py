import discord
import os
from discord.ext import commands

# הגדרת הרשאות (Intents)
intents = discord.Intents.default()
intents.members = True          # מאפשר לזהות כניסת משתמשים
intents.message_content = True  # מאפשר לקרוא תוכן הודעות (לפקודות)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'--- הבוט מחובר בהצלחה! ---')
    print(f'שם הבוט: {bot.user.name}')
    print(f'-----------------------')

@bot.event
async def on_member_join(member):
    # כאן אנחנו מושכים את ה-ID מהמשתנה שנקרא WELCOME_CHANNEL_ID בתוך Railway
    channel_id_env = os.getenv("WELCOME_CHANNEL_ID")
    
    if channel_id_env is None:
        print("Error: WELCOME_CHANNEL_ID variable is not set in Railway!")
        return

    channel = bot.get_channel(int(channel_id_env))
    
    if channel:
        guild = member.guild
        member_count = guild.member_count
        
        # יצירת ה-Embed (הודעה מעוצבת)
        embed = discord.Embed(
            description=f"**שלום <@{member.id}>, ברוך הבא ל `GameLife |  FiveM Roleplay`! We're `{member_count}` members now.**",
            color=discord.Color.from_rgb(43, 45, 49) 
        )
        
        embed.set_footer(text="Dev: Frozen")
        embed.set_thumbnail(url="https://i.imgur.com/Z95303n.png") 

        await channel.send(embed=embed)

# פקודת בדיקה - כתוב !test בשרת
@bot.command()
async def test(ctx):
    await on_member_join(ctx.author)

# הרצת הבוט עם הטוקן מ-Railway
token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("Error: DISCORD_TOKEN variable is not set in Railway!")
