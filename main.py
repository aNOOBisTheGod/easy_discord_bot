import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random as r
import images as imgs
from io import BytesIO
import aiohttp
from cfg import TOKEN
import youtube_dl
import os
from pretty_help import DefaultMenu, PrettyHelp

menu = DefaultMenu(page_left="👍", page_right="👎", remove="a:python:837943828505559070", active_time=5)

ending_note = "The end of {ctx.bot.user.name}'s help command."

bot = commands.Bot(command_prefix='!!')

bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)


@bot.command()
@commands.has_permissions(ban_members = True)
async def ping(ctx, member : discord.Member, *, t = 10):
    '''ping member by id(staff only)'''
    t = int(t)
    for i in range(t):
        await ctx.send('<@' + str(member.id) + '>')


@bot.command()
async def add(ctx, a: int, b: int):
    '''slove 1 argument + 2 argument'''
    await ctx.send(a + b)


@bot.command()
async def info(ctx):
    '''now its just a test'''
    await ctx.send(ctx.guild.members)


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    '''ban member(staff only)'''
    await member.ban(reason = reason)
    await ctx.send(str(member) +  ' has been banned!')


@bot.command()
@commands.has_permissions(ban_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    '''kick member(staff only)'''
    await member.kick(reason = reason)
    await ctx.send(str(member) + ' has been kicked!')


@bot.command()
@commands.has_permissions(manage_guild = True)
async def create(ctx, name):
    '''creates text channel'''
    guild = ctx.message.guild
    await guild.create_text_channel(name)


@bot.command()
async def avatar(ctx, member : discord.Member):
    '''shows avatar of mentioned member'''
    await ctx.send(member.avatar_url)


@bot.command()
async def displayembed(ctx, member : discord.Member):
    '''display embed with mentioned user's avatar'''
    embed = discord.Embed(
        title = 'Привет',
        description = 'Hello',
        colour = discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200))
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def send(ctx):
    '''send bot creator's avatar'''
    await ctx.send('https://images-ext-1.discordapp.net/external/sY0HvQ0FmypS-xYIUcJPCGI-7QgAo-JBvaNOoxVtUDc/%3Fsize' +
                   '%3D1024/https/cdn.discordapp.com/avatars/661157502989238282/a96bb49abd23ac3ddfaea6944746c60f.webp')


@bot.command()
@commands.has_permissions(manage_roles = True)
async def give(ctx, member: discord.Member, role: discord.Role):
    '''gives member role(staff only)'''
    try:
        getrole = discord.utils.get(ctx.guild.roles, id = role.id)
        await member.add_roles(getrole)
    except Exception:
        await ctx.send(f'Неверное имя пользователя или роль! ({member}, {role})')


@bot.command()
async def play(ctx):
    '''bot will join vc'''
    await ctx.author.voice.channel.connect()
    await ctx.message.delete()


@bot.command()
async def leave(ctx):
    '''bot will leave vc'''
    await ctx.voice_client.disconnect()
    await ctx.message.delete()


@bot.command()
async def serverinfo(ctx):
    '''information about server'''
    server = ctx.message.guild
    online = 0
    for i in server.members:
        if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1
    channel_count = len([i for i in server.channels if type(i) == discord.channel.TextChannel])
    role_count = len(server.roles)
    emoji_count = len(server.emojis)
    em = discord.Embed(color=discord.Colour.from_rgb(232,111,108))
    em.add_field(name='Name', value=server.name)
    em.add_field(name='Owner', value=server.owner)
    em.add_field(name='Members', value=server.member_count)
    em.add_field(name='Currently Online', value=online)
    em.add_field(name='Text Channels', value=str(channel_count))
    em.add_field(name='Region', value=server.region)
    em.add_field(name='Verification Level', value=str(server.verification_level))
    em.add_field(name='Number of roles', value=str(role_count))
    em.add_field(name='Number of emotes', value=str(emoji_count))
    em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    em.set_thumbnail(url=server.icon_url)
    em.set_author(name='Server Info', icon_url='https://cdn.discordapp.com/avatars/828005083714814002' +
                                               '/ef1f7e01bbbf097a588ef2c78d685ebc.webp?size=1024')
    em.set_footer(text='Server ID: %s' % server.id)
    await ctx.send(embed=em)



@bot.command()
@commands.has_permissions(mute_members = True)
async def vcmute(ctx):
    '''mute all members in your in vc(staff only)'''
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)


@bot.command()
@commands.has_permissions(mute_members = True)
async def vcunmute(ctx):
    '''unmute all members in your in vc(staff only)'''
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)


@bot.command()
async def voting(ctx, *, arg=None):
    '''makes anonymous poll'''
    await ctx.message.delete()
    message = await ctx.send(arg)
    emoji = '\N{THUMBS UP SIGN}'
    emoji1 = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)
    await message.add_reaction(emoji1)



@bot.command()
async def sendfile(ctx):
    '''test'''
    await ctx.send(file=discord.File(r'C:\тут будет все\3799a749d2f405babfc5c2a2d492385c.jpg'))


@bot.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
    '''give member role named MUTED for some time'''
    roleobject = discord.utils.get(ctx.message.guild.roles, name='MUTED')
    embed = discord.Embed(
        title=f'{user} was muted for {duration} {unit}',
        colour=discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
    await ctx.send(embed=embed)
    await user.add_roles(roleobject)
    if unit == "s":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m":
        wait = 60 * duration
        await asyncio.sleep(wait)
    elif unit == "h":
        wait = 3660 * duration
        await asyncio.sleep(wait)
    await user.remove_roles(roleobject)
    embed = discord.Embed(
        title=f'{user} was unmuted',
        colour=discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
    await ctx.send(embed=embed)


@bot.command()
async def votemute(ctx, member : discord.Member, *, arg=None):
    '''creates poll to mute member in vc'''
    global c
    global message_id
    global users
    global vc
    global x
    x = member
    vc = ctx.author.voice.channel
    if x in vc.members:
        c = 0
        embed = discord.Embed(
        title=f'Should I mute {x} in voice chat for {arg}?',
        colour=discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
        message = await ctx.send(embed=embed)
        message_id = message.id
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
        users = []
        @bot.event
        async def on_raw_reaction_add(payload):
            global x
            global message_id
            global users
            global vc
            if payload.message_id == message_id:
                if payload.user_id not in users:
                    users.append(payload.user_id)
                    global c
                    c += 1
            if c > len(vc.members) // 2 + 2:
                await x.edit(mute=True)
                embed = discord.Embed(
                title= str(x) + ' has been muted!',
                colour=discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
                await ctx.send(embed=embed)


@bot.command()
async def voteunmute(ctx, member : discord.Member, *, arg=None):
    '''creates poll to unmute member in vc'''
    global c
    global message_id
    global users
    global vc
    global x
    x = member
    c = 0
    embed = discord.Embed(
    title = f'Should I unmute {x} in voice chat?',
    colour = discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
    message = await ctx.send(embed=embed)
    message_id = message.id
    emoji = '\N{THUMBS UP SIGN}'
    await message.add_reaction(emoji)
    users = []
    vc = ctx.author.voice.channel
    @bot.event
    async def on_raw_reaction_add(payload):
        global member
        global message_id
        global users
        global vc
        if payload.message_id == message_id:
            if payload.user_id not in users:
                users.append(payload.user_id)
                global c
                c += 1
        if c > len(vc.members) // 2 + 2:
            await x.edit(mute=False)
            embed = discord.Embed(
            title = str(x) + ' has been unmuted!',
            colour = discord.Colour.from_rgb(r.randint(100, 200), r.randint(100, 200), r.randint(100, 200)))
            await ctx.send(embed=embed)


@bot.command()
async def reverse(ctx):
    '''reverses image colors    '''
    for attach in ctx.message.attachments:
        try:
            await attach.save(r'C:\Users\anubis\PycharmProjects\discordbot\savedimage.png')
            imgs.imreversep()
            await ctx.send(file=discord.File(r'C:\Users\anubis\PycharmProjects\discordbot\res.png'))
        except:
            await attach.save(r'C:\Users\anubis\PycharmProjects\discordbot\savedimage.jpg')
            imgs.imreversej()
            await ctx.send(file=discord.File(r'C:\Users\anubis\PycharmProjects\discordbot\res.jpg'))


@bot.command()
@commands.has_permissions(manage_emojis = True)
async def createemoji(ctx, url: str, *, name):
    '''creates custom emoji(staff only)'''
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as r:
            try:
                img_or_gif = BytesIO(await r.read())
                b_value = img_or_gif.getvalue()
                if r.status in range(200, 299):
                    emoji = await ctx.guild.create_custom_emoji(image=b_value, name=name)
                    await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
                    await ses.close()
                else:
                    await ctx.send(f'Error when making request | {r.status} response.')
                    await ses.close()
            except discord.HTTPException:
                await ctx.send('File size is too big!')


@bot.command(pass_context = True)
@commands.has_permissions(manage_roles = True)
async def rrole(ctx, role: discord.Role):
    '''makes a kind of a rainbow role'''
    role = ctx.guild.get_role(role.id)
    try:
        while True:
            a = r.randint(0, 255)
            b = r.randint(0, 255)
            c = r.randint(0, 255)
            if a < 200 and b < 200 and c < 200:
                m = r.randint(1, 3)
                if m == 1:
                    a = 255
                elif m == 2:
                    b = 255
                else:
                    c = 255
            color = imgs.rgb_to_hex((a, b, c))
            col = int(color, 16)
            colors = discord.Color(col)
            await role.edit(colour=colors)
    except Exception as error:
        print(error)


@bot.command(pass_context = True)
async def chemist(ctx, x, y):
    '''returnrs chemical reaction equation'''
    out = imgs.parser(x, y)
    x = bot.get_emoji(837943828505559070)
    embed = discord.Embed(
        title='Done' + ' ' + str(x),
        description=out,
        colour=discord.Colour.from_rgb(r.randint(200, 255), r.randint(200, 255), r.randint(200, 255))
    )
    await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def chemistchain(ctx, *, text):
    '''returnrs chemical reaction chain'''
    out = imgs.chain(text)
    x = bot.get_emoji(837943828505559070)
    embed = discord.Embed(
        title='Done' + ' ' + str(x),
        description= '\n'.join(out),
        colour=discord.Colour.from_rgb(r.randint(200, 255), r.randint(200, 255), r.randint(200, 255))
    )
    await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def emid(ctx):
    '''returns list of server emojis and their id'''
    global coun
    a = []
    b = []
    c = []
    for emoji in ctx.guild.emojis:
        x = bot.get_emoji(emoji.id)
        a.append('\\' + str(x))
        a.append(str(x))
    if len(a) > 21:
        counter = 0
        for i in range(len(a)):
            b.append(a[i])
            if i % 21 == 0 and i != 0:
                counter += 1
                embed = discord.Embed(
                    title='Here is the list of server emojis:',
                    description='\n'.join(b),
                    colour=discord.Colour.from_rgb(r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))
                )
                b = []
                c.append(embed)
        message = await ctx.send(embed=c[0])
        message_id = message.id
        emoji = '⏩'
        emoji1 = '⏪'
        coun = 0
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji)
        @bot.event
        async def on_raw_reaction_add(payload):
            global coun
            if payload.message_id == message_id and payload.emoji.name == '⏩':
                coun += 1
            elif payload.message_id == message_id and payload.emoji.name == '⏪':
                coun -= 1
            try:
                await message.edit(embed=c[coun])
            except:
                pass


    else:
        embed = discord.Embed(
            title='Here is the list of server emojis:',
            description='\n'.join(a),
            colour=discord.Colour.from_rgb(r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))
        )
        await ctx.send(embed=embed)





@bot.command()
async def anagliph(ctx, delta):
    '''makes anagliph'''
    for attach in ctx.message.attachments:
        try:
            await attach.save(r'C:\Users\anubis\PycharmProjects\discordbot\lol.png')
            imgs.makeanagliphp(int(delta))
            await ctx.send(file=discord.File(r'C:\Users\anubis\PycharmProjects\discordbot\pc.png'))
        except:
            await attach.save(r'C:\Users\anubis\PycharmProjects\discordbot\lol.jpg')
            imgs.makeanagliphj(int(delta))
            await ctx.send(file=discord.File(r'C:\Users\anubis\PycharmProjects\discordbot\pc.jpg'))


@bot.event
async def on_ready():
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('!!help || In development...'))


bot.run(TOKEN)
