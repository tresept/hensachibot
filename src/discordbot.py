# 外部ライブラリのインポート
import os
import discord
from dotenv import load_dotenv

load_dotenv()
bottoken = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.guilds = True

bot = discord.Bot(
    intents=intents, 
    activity=discord.Game("/hensachi"), 
)

@bot.event
async def on_ready():
    print(f"正常に起動しました．アカウント名: {bot.user.name}としてログインを完了しました．")

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        print('mentionを検知しました, 分岐処理に移ります...')
        if message.reference:
            print('mentionを検知しましたが,返信のため無視されました')
        else:
            print('返信ではないため，メッセージを送信します')
            await message.channel.send('スラッシュコマンドを使え！')

@bot.event(name="hensachi", discription="大学の偏差値を表示します。")
async def hensachi(ctx: discord.ApplicationContext):
    print('コマンドを受信しました: hensachi')
    await ctx.send('大学の偏差値は〇〇です。')