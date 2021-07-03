# rainbow role, modules: discord.py

from discord.ext import tasks
from discord.utils import get

r = g = 0
b = 255

@client.event
async def on_ready():
    global rainbowrolee
    roleguild = client.get_guild(743426357958148136) # Your guild
    rainbowrolee = get(roleguild.roles, id=860817065559982091) # Your rainbow role
    rainbowrole.start()

    
@tasks.loop()
async def rainbowrole():
    global r, g, b
    print(f'R:{r}, G:{g}, B:{b}')
    if r <= 255 and g == 0:
        r = r + 15
        b = b - 15
    if g <= 255 and b == 0:
        g = g + 15
        r = r - 15
    if b <= 255 and r == 0:
        b = b + 15
        g = g - 15
    await rainbowrolee.edit(colour=discord.Color.from_rgb(r, g, b))
