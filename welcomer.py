# Welcomer, modules: discord.py, PIL, io
from PIL import Image
from io import BytesIO

intents = discord.Intents.default()
intents.members = True

client = discord.Client(command_prefix='', intents=intents)

@client.event
async def on_member_join(member):
    channel = client.get_channel(859761373693214750)
    await channel.send(f'{member} join')
    
    response = requests.get(member.avatar_url)
    img = Image.open(BytesIO(response.content))
    fond = Image.open('welcome_fond.jpeg')
    img = img.resize((140, 140))
    fond.paste(img, (220, 90))
    fond.save('welcome.jpg')

    await channel.send(file=discord.File('welcome.jpg'))
