import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import time
from profanity import profanity
from tinydb import TinyDB, Query
from tinydb.operations import delete, increment
import os


# ----------------------------------------------------------------------------


bot = commands.Bot(".")

token = 'Mzk2ODAxOTkwMzkyNTQ1Mjgy.DSmuYA.60XYRdYq_OWsGpbxJJgTwgJC5AU'

client = discord.Client()

user = discord.Member


# ----------------------------------------------------------------------------


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Peçam ajuda para mim ❤", type=1))
    print('----------NeR0-----------')
    print('Bot logado com sucesso.')
    print('Nome: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('----------NeR0-----------')


# ----------------------------------------------------------------------------


@bot.command(pass_context=True)
async def sagiri(ctx):
    await bot.say('Eu sou uma bot super かわいい criada pelo meu progamador  NeR0!')


@bot.command(pass_context=True)
async def dado(ctx):
    await bot.say(random.choice(["Sim",
                                 "Não",
                                 "Talvez",
                                 "Vai se fuder",
                                 "Com certeza"]))


@bot.command(pass_context=True)
@commands.has_role("☆ G0D 神様 ☆")
async def kick(ctx, user: discord.Member):
    await bot.say("Você está encomodando, {}. Retire-se do servidor.".format(user.name))
    await bot.kick(user)


@bot.command(pass_context=True)
@commands.has_role("☆ G0D 神様 ☆")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Eu achei isso sobre ele(a).",
                          color=0x8807df)
    embed.add_field(name="Usuário:", value=user.name, inline=True)
    embed.add_field(name="ID:", value=user.id, inline=True)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Maior cargo:", value=user.top_role, inline=True)
    embed.add_field(name="Entrou em:", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name),
                          description="Eu achei isso sobre o servidor.", color=0x8807df)
    embed.add_field(name="Nome:", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Cargos:", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Membros:", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def mal(ctx):
    embed = discord.Embed(title="MyAnimeList.net", url="https://myanimelist.net/animelist/NeR0Viado", description="Entrem na lista de animes do NeR0", color=0x8807df)
    embed.set_author(name="NeR0", icon_url="https://images-ext-2.discordapp.net/external/sev7d5UZ6FAd9d1tra7ha18Xe9r2R8Z0WhdB83JJdgc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/305473992381300736/7ecc6081e133a2b29b963753805e5da6.webp?width=81&height=81")
    embed.set_thumbnail(url="https://i.imgur.com/vEy5Zaq.png")
    await bot.say(embed=embed)


@bot.listen()
async def on_member_join(member):
    embed = discord.Embed(title="Seja bem-vindo(a) ao servidor NeR0's Playground",
                          description="Leia nossas #regras ! É um prazer em recebê-lo {0}".format(member.mention, member.server.name), color=0x8807df)
    embed.add_field(name="Dono", value="NeR0", inline=True)
    embed.set_image(url="https://i.pinimg.com/originals/fb/16/5e/fb165efed3349e846fca4a3f85ae816e.gif")
    is_verified = False
    for role in member.roles:
        if role.name == "✔ MEMBROS メンバー ✔":
            is_verified = True
            break
    if is_verified == False:
        await bot.send_message(member, "Use o comando .verificar para conseguir a tag.")
        await bot.send_message(discord.Object(id='393478354243813379'), embed=embed)


@bot.command(pass_context=True)
@commands.has_role("☆ G0D 神様 ☆")
async def limpar(context, number: int):
    deleted = await bot.purge_from(context.message.channel, limit=number)
    await bot.send_message(context.message.channel, '{} mensagens foram deletados!'.format(len(deleted)))


@bot.command(pass_context=True)
async def verificar(context):
    for server in bot.servers:
        roles = server.roles
        members = server.members
        member = None
        for mem in members:
            if mem.id == context.message.author.id:
                member = mem
                break
        for role in roles:
            if role.name == "✔ MEMBROS メンバー ✔":
                await bot.add_roles(member, role)
                break


@bot.command(pass_context=True)
async def cargos(context):
    roles = context.message.server.roles
    result = "Os cargos são: "
    for role in roles:
        result += role.name + ": " + role.id + " , "
    await bot.say(result)


@bot.command(pass_context=True)
@commands.has_role("☆ G0D 神様 ☆")
async def dokidoki(ctx):
    embed = discord.Embed(title="**Doki Doki Literature Club**", description="É um jogo onde você é um estudante do ensino médio anti-social que gosta de jogar e assistir animes, quando sua amiga de infância chama você para entrar no clube de literatura que ela participa. A história gira em torno desse clube e das menininhas que vão nesse clube **>> [link](http://store.steampowered.com/app/698780/Doki_Doki_Literature_Club/) <<**. ", color=0x8807df)
    embed.set_author(name="NeR0", icon_url="https://images-ext-2.discordapp.net/external/sev7d5UZ6FAd9d1tra7ha18Xe9r2R8Z0WhdB83JJdgc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/305473992381300736/7ecc6081e133a2b29b963753805e5da6.webp?width=81&height=81")
    embed.add_field(name="Nota geral", value="9/10", inline=True)
    embed.add_field(name="Jogabilidade", value="8/10", inline=True)
    embed.add_field(name="História", value="10/10", inline=True)
    embed.add_field(name="Preço", value="R$ 0,00", inline=True)
    embed.set_thumbnail(url="https://s.mxmcdn.net/images-storage/albums4/0/8/3/7/5/4/38457380_800_800.jpg")
    embed.set_image(url="http://cdn.edgecast.steamstatic.com/steam/apps/698780/ss_3941e57f278958dd15c9855f42ab069da3a19608.1920x1080.jpg?t=1509687157")
    embed.add_field(name="Notas adicionais", value="```Jogo muito bom, com uma jogabilidade ótima, é daqueles jogos japoneses que você conversa com as menininhas da escola japonesa e a história vai de acordo com suas escolhas. Eu recomendo esse jogo, é otimo ja zerei várias vezes.```")
    embed.set_footer(text="Este jogo não é recomendado para crianças com menos de 13 anos ou para quem fica facilmente perturbado. Este jogo também não é recomendado para quem tem problemas com ansiedade e depressão.")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.has_role("☆ G0D 神様 ☆")
async def sa(ctx):
    embed = discord.Embed(title="**SuperAnimes.site**", description="Site muito bom que eu uso para assistir animes, recomendo! Os episódios saem logo depois que passa no japão. **>> [LINK](https://www.superanimes.site/) <<**", color=0x8807df)
    embed.set_author(name="NeR0", icon_url="https://images-ext-2.discordapp.net/external/sev7d5UZ6FAd9d1tra7ha18Xe9r2R8Z0WhdB83JJdgc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/305473992381300736/7ecc6081e133a2b29b963753805e5da6.webp?width=81&height=81")
    embed.set_thumbnail(url="https://i.imgur.com/DSs9Gxj.png")
    embed.add_field(name=".", value="```Vou divulgar esse site pra dar uma força para o trabalho dos caras que eles são fodas.```")
    embed.set_image(url="https://www.superanimes.site/img/logo.png")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def obradearte(ctx):
    embed = discord.Embed(title="**A melhor obra de arte já feito por NeR0.**", color=0x8807df )
    embed.set_author(name="NeR0", icon_url="https://images-ext-2.discordapp.net/external/sev7d5UZ6FAd9d1tra7ha18Xe9r2R8Z0WhdB83JJdgc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/305473992381300736/7ecc6081e133a2b29b963753805e5da6.webp?width=81&height=81")
    embed.set_image(url="https://i.imgur.com/Egmba8C.jpg")
    embed.set_footer(text="Essa imagem foi feito durante uma competição de edição de imagem entre NeR0 e chrismeister.")
    await bot.say(embed=embed)

# ----------------------------------------------------------------------------


bot.run(token)

