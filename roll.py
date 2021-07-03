# Roll, modules: discord.py, random, math

        channel = ctx.channel
  
        try:
            try:
                max = int(ctx.content.split(' ', 3)[1])
            
            except ValueError:
              
                embed = discord.Embed(title="Roll", description="Error: Not a number",
                                      color=0x00349a)
                embed.set_footer(text=ctx.author)
                await channel.send(embed=embed)
                return
              
        except IndexError:
            max = 6

        embed = discord.Embed(title="Roll", color=0x00349a, description=
        f"I roll {math.floor(random.uniform(1, max))}")
        embed.set_footer(text=ctx.author)
        await channel.send(embed=embed)
