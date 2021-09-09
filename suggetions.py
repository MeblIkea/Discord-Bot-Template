# Todo, modules: discord.py, json, pandas as pd, numpy as np, and matplotlib.pyplot as plt
# Remember to add your @client.command()
#
# "channel_inutile" is a private channel where the bot can post pictures for embeds
# Add a suggestion channel too
# You have to translate, I don't have time for it, sorry (FR to English), send me your translations on discord please.
#
# Take the suggestions.json

suggestion_channel = 000000000000000000
channel_inutile = 000000000000000000


async def todo(ctx, *, arg=None):
    channel = client.get_channel(suggestion_channel)
    guild = client.get_guild(server_id)
    role = discord.utils.get(guild.roles, name=admins)
    global idee_id
    if not channel == ctx.channel:
        await ctx.send('`Bad channel`')
    else:
        if role not in ctx.author.roles:
            await ctx.send("`You don't have the permissions for use this command`")
        else:
            if arg is None:
                return await ctx.send(
                    embed=discord.Embed(title="**Error**", description='Add an arg', color=color))
            else:
                global idee_dict
                arg = arg.lower()
                message = (await channel.history(limit=2).flatten())[1]
                if arg in ['refuser', 'refusé', 'tg']:
                    embed = discord.Embed(title='Refusé', color=color,
                                          description=f'**{message.author.mention}** votre suggestion à était '
                                                      '**refusé**.')
                    embed.add_field(name='Suggestion:', value=message.content)
                    embed.set_footer(text=f'Refusé par **{ctx.author}**')
                    await channel.purge(limit=2)
                    await ctx.send(content=message.author.mention, embed=embed)
@client.command()

                if arg in ['ok', 'accepte', 'accepter', 'accepté', 'accept']:
                    with open('suggestion.json', 'r') as file:
                        idee_dict = json.load(file)
                        idee_dict.update({message.id: {'content': message.content, 'state': 0, 'id': message.id,
                                                       'author': str(message.author), 'added_by': str(ctx.author)}})
                    with open('suggestion.json', 'w') as file:
                        json.dump(idee_dict, file, indent=6)
                    await ctx.send(embed=discord.Embed(color=color, title='Suggestion', description=f'Suggestion de '
                                                                                       f'**{message.author}** ajouté.'))

                if arg in ['liste', 'list']:
                    with open('suggestion.json', 'r') as file:
                        list_dict = json.load(file)
                        compteur = 0
                    embed = discord.Embed(title='Suggestions', description='Voici la liste des suggestions',
                                          color=color)
                    for x in list(list_dict.values()):
                        content = dict(list(list_dict.values())[compteur])['content']
                        state = dict(list(list_dict.values())[compteur])['state']
                        id = dict(list(list_dict.values())[compteur])['id']
                        embed.add_field(name='Idée:', value=content, inline=True)
                        embed.add_field(name='Status:', value=state, inline=True)
                        embed.add_field(name='Id:', value=id, inline=True)
                        compteur = compteur + 1
                    await ctx.send(embed=embed)
                if str(arg).split(' ', 2)[0] in ['info', 'infos']:
                    try:
                        idee_id = arg.split(' ', 1)[1]
                    except IndexError:
                        return await ctx.send('`Erreur: Fo mètr un argumen, débile :(`')
                    if not len(idee_id) == 18:
                        return await ctx.send('`Erreur: Il faut mettre une ID`')
                    else:
                        with open('suggestion.json', 'r') as file:
                            id_dict = json.load(file)[idee_id]
                        embed = discord.Embed(title='Info Suggestion', description=f'ID: {idee_id}', color=color)
                        embed.add_field(name='Content:', value=list(id_dict.values())[0], inline=False)
                        embed.add_field(name='Status:', value=list(id_dict.values())[1], inline=False)
                        embed.add_field(name='Id:', value=list(id_dict.values())[2], inline=False)
                        embed.add_field(name='Autheur:', value=list(id_dict.values())[3], inline=False)
                        embed.add_field(name='Ajouté par:', value=list(id_dict.values())[4], inline=False)
                        await ctx.send(embed=embed)

                if arg in ['show', 'montrer', 'montré']:
                    channel0 = client.get_channel(channel_inutile)
                    with open('suggestion.json', 'r') as file:
                        idee_dict = json.load(file)

                    fig, ax = plt.subplots()
                    fig.patch.set_visible(False)
                    ax.axis('off')
                    ax.axis('tight')
                    todo = []
                    doing = []
                    done = []

                    compteur = 0
                    for o in idee_dict.values():
                        if dict(list(idee_dict.values())[compteur])['state'] == 0:
                            todo.append(dict(list(idee_dict.values())[compteur])['content'])
                        if dict(list(idee_dict.values())[compteur])['state'] == 1:
                            doing.append(dict(list(idee_dict.values())[compteur])['content'])
                        if dict(list(idee_dict.values())[compteur])['state'] == 2:
                            done.append(dict(list(idee_dict.values())[compteur])['content'])
                        compteur = compteur + 1

                    todo_list = {'A faire': todo,
                                 'En cours': doing,
                                 'Terminé': done}

                    df = pd.DataFrame.from_dict(todo_list, orient='index')
                    df = df.transpose()
                    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
                    fig.tight_layout()
                    plt.savefig('todo.png')

                    await channel0.purge(limit=2)
                    todo_pic = await channel0.send(file=discord.File('todo.png'))

                    embed = discord.Embed(description='Voici les taches en cours', color=color, title='Taches')
                    embed.set_image(url=todo_pic.attachments[0].url)
                    await ctx.send(embed=embed)

                if str(arg).split(' ', 2)[0] in ['clean', 'remove', 'enlever', 'effacer']:
                    role = discord.utils.get(guild.roles, name=admins)
                    if role not in ctx.author.roles:
                        await ctx.send("`Vous n'avez pas les droits de faire cette commande.`")
                    else:
                        try:
                            idee_id = arg.split(' ', 1)[1]
                        except IndexError:
                            return await ctx.send('`Erreur: Fo mètr un argumen, débile :(`')
                        if not len(idee_id) == 18:
                            return await ctx.send('`Erreur: Il faut mettre une ID`')
                        else:
                            with open('suggestion.json', 'r') as file:
                                list_dict = json.load(file)
                                del list_dict[idee_id]
                            with open('suggestion.json', 'w') as file:
                                json.dump(list_dict, file, indent=6)
                            embed = discord.Embed(color=color, title='Élement supprimé',
                                                  description=f"l'objet **{idee_id}** a était supprimé avec succés")
                            embed.set_author(name=f'Commande effecté par {ctx.author}')
                            await ctx.send(embed=embed)
                if str(arg).split(' ', 2)[0] in ['move', 'set']:
                    if role not in ctx.author.roles:
                        await ctx.send("`Vous n'avez pas les droits de faire cette commande.`")
                    else:
                        try:
                            idee_id = arg.split(' ', 2)[1]
                            idee = arg.split(' ', 2)
                        except IndexError:
                            return await ctx.send('`Erreur: Fo mètr un argumen, débile :(`')
                        if not len(idee_id) == 18:
                            return await ctx.send('`Erreur: Il faut mettre une ID`')
                        else:
                            global move, change_number, change_str
                            try:
                                if idee[2] == 'up':
                                    move = 'up'
                                if idee[2] == 'down':
                                    move = 'down'
                            except IndexError:
                                move = 'up'
                            with open('suggestion.json', 'r') as file:
                                idee_dict = json.load(file)

                            change_idee = idee_dict[idee_id]
                            if move == 'up':
                                if change_idee['state'] == 0:
                                    change_number = 1
                                    change_str = 'en cours'
                                elif change_idee['state'] == 1:
                                    change_number = 2
                                    change_str = 'terminé'
                                else:
                                    change_number = 0
                                    change_str = 'à faire'
                            if move == 'down':
                                if change_idee['state'] == 2:
                                    change_number = 1
                                    change_str = 'en cours'
                                elif change_idee['state'] == 1:
                                    change_number = 0
                                    change_str = 'à faire'
                                else:
                                    change_number = 0
                                    change_str = 'à faire'

                            change_idee['state'] = change_number
                            change_line = {idee_id: change_idee}
                            print(change_line)
                            del idee_dict[idee_id]
                            idee_dict.update(change_line)
                            with open('suggestion.json', 'w') as file:
                                json.dump(idee_dict, file, indent=6)
                            await ctx.send(embed=discord.Embed(color=color, title='Tache mises à jour',
                                                               description=f'La tache **{idee_id}** est maintenant'
                                                                           f' **{change_str}**'))
