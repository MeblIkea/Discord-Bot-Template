# Place this where you want to invoke it:
# await loading(channel=ctx.channel)


async def loading(channel):
    embed = discord.Embed(title="Loading", description="▛", color=0x00349a)
    message = await channel.send(embed=embed)
    await asyncio.sleep(1)
    await bloading(message=message, char='▛▜', dot='.')
    await bloading(message=message, char='██', dot='..')
    await bloading(message=message, char='▗▉', dot='...')
    await bloading(message=message, char='▗▖', dot='')
    await message.delete()


async def bloading(message, char, dot):
    embed = discord.Embed(title=f"Loading{dot}", description=char, color=0x00349a)
    await message.edit(embed=embed)
    await asyncio.sleep(1)
