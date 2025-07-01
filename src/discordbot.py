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

# ここら辺にGeminiと繋げて喋れるようにする処理を書きたい
@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        print('mentionを検知しました, 分岐処理に移ります...')
        if message.reference:
            print('返信のため無視されました')
        else:
            print('返信ではないため，メッセージを送信します')
            await message.channel.send('スラッシュコマンドを使え！')

@bot.event(name="hensachi", description="大学の偏差値を表示します。")
async def hensachi(ctx: discord.ApplicationContext, school: str):
    print('コマンドを受信しました: hensachi')
    await ctx.send(f'{school}の偏差値は〇〇です。')

@bot.event(name="bus", description="香川高専前の次のバスの時間を取得します．")
async def TimeTableBus(ctx: discord.ApplicationContext):
    print("コマンドを受信しました: bus")
    await ctx.send('ttb')

@bot.event(name="train", description="詫間駅の次の電車の時間を取得します．")
async def TimeTableTrain(ctx: discord.ApplicationContext):
    print("コマンドを受信しました: train")
    await ctx.send('ttt')




"""
@bot.event(name="", description="")
async def name(ctx: discord.ApplicationContext):
"""