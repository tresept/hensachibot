# 環境変数のチェックと表示

import os
from dotenv import load_dotenv

load_dotenv()

dtoken = os.getenv('DISCORD_TOKEN')

print(f"DISCORD_TOKEN: {dtoken}")