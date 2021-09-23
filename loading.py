# Loading, modules: discord.py
#
# Place this where you want to invoke it:
# await loading(channel=ctx.channel)
color = 0x000000


async def loading(channel):
    message = await channel.send(embed=discord.Embed(title="Loading.", description="▛", color=0x00349a))
    await bloading(message=message, char='▛▜', dot='..')
    await bloading(message=message, char='██', dot='...')
    await bloading(message=message, char='▗▉', dot='.')
    await bloading(message=message, char='▗▖', dot='..')
    await message.delete()


async def bloading(message, char, dot):
    embed = discord.Embed(title=f"Loading{dot}", description=char, color=color)
    await message.edit(embed=embed)
