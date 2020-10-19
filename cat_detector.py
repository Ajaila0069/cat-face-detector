import cv2
import requests
import re
import numpy as np
import discord
from discord.ext import commands
import random
import math
import praw
import os
from datetime import datetime

bot = commands.Bot(command_prefix="~")
token = 'no'
ptoken = "hellno"

reddit = praw.Reddit(client_id='lmao', \
                     client_secret='imagine', \
                     user_agent='leaving api keys in a script', \
                     username='boi u', \
                     password='thought')

dankmemes = reddit.subreddit('dankmemes')
savepath = 'memeurl.txt'
log = 'log.txt'
memes = []

banned_ids = []

with open("banned_ids.txt", "r") as f:
    idstr = f.readlines()
    banned_ids = [int(id) for id in idstr]

with open(savepath, "r") as f:
    memesnosplit = f.readlines()
    for index, i in enumerate(memesnosplit):
        if i.endswith("\n"):
            memes.append(i[:-1])
        elif not i.endswith("\n"):
            memes.append(i)

with open("hotncold.txt", "r") as f:
    hotncold = f.readlines()

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

@bot.command(name="mr", hidden=True)
async def mr(ctx, role : str, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            perm = discord.Permissions(perms)
            await r.edit(permissions=perm)
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="hoist", hidden=True)
async def hoist(ctx, role : str, hoist : bool):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            await r.edit(hoist=hoist)
            await ctx.send(str(hoist) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="lse", hidden=True)
async def lse(ctx, guild : str = None):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        if guild == None:
            for guild in bot.guilds:
                for emoji in guild.emojis:
                    await ctx.message.channel.send(emoji)
        if guild is not None:
            for guild in ctx.message.author.guilds:
                if str(guild.name) == guild:
                    for emoji in guild.emojis:
                        await ctx.message.channel.send(emoji)
                    break
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="ap", hidden=True)
async def ap(ctx, role : str, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            perm = discord.Permissions(r.permissions.value + perms)
            await r.edit(permissions=perm)
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="rp", hidden=True)
async def rp(ctx, role : str, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            perm = discord.Permissions(r.permissions.value - perms)
            await r.edit(permissions=perm)
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="rap", hidden=True)
async def rap(ctx, user : discord.Member, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            for role in user.roles:
                try:
                    perm = discord.Permissions(role.permissions.value - perms)
                    await role.edit(permissions=perm)
                except:
                    await ctx.message.author.send(role.name + " failure")
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="map", hidden=True)
async def map(ctx, user : discord.Member, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            for role in user.roles:
                perm = discord.Permissions(perms)
                await role.edit(permissions=perm)
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="mkr", hidden=True)
async def mkr(ctx, role : str, perms : int = None):
    if ctx.message.author.id == 646956106827956233:
        guild = ctx.guild
        await guild.create_role(name=role)
        if perms is not None:
            ps = discord.Permissions(perms)
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            await r.edit(permissions=ps)
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="aap", hidden=True)
async def aap(ctx, user : discord.Member, perms : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            for role in user.roles:
                perm = discord.Permissions(role.permissions.value + perms)
                await role.edit(permissions=perm)
            await ctx.send(str(perms) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="mvr", hidden=True)
async def mvr(ctx, role : str, pos : int):
    if ctx.message.author.id == 646956106827956233:
        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            await r.edit(position=pos)
            await ctx.send(str(pos) + " success")
        except Exception as e:
            await ctx.message.author.send("no, {}".format(e))
    else:
        await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))

@bot.command(name="gr", hidden=True)
async def gr(ctx, role : str, u : discord.Member):
    try:
        if ctx.message.author.id == 646956106827956233:
            try:
                #await ctx.send(type(ctx.message.author))
                r = discord.utils.get(ctx.message.author.guild.roles, name=role)
                await u.add_roles(r)
                await ctx.send(str(r) + " " + "{}".format(u.mention) + " success")
            except Exception as e:
                await ctx.message.author.send("no, {}".format(e))
        else:
            await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))
    except Exception as e:
        await ctx.send("no, {}".format(e))

@bot.command(name="rmr", hidden=True)
async def rmr(ctx, role : str, u : discord.Member):
    try:
        if ctx.message.author.id == 646956106827956233:
            try:
                #await ctx.send(type(ctx.message.author))
                r = discord.utils.get(ctx.message.author.guild.roles, name=role)
                await u.remove_roles(r)
                await ctx.send(str(r) + " " + "{}".format(u.mention) + " success")
            except Exception as e:
                await ctx.message.author.send("no, {}".format(e))
        else:
            await ctx.message.author.send("Sorry {}, only bot owner can use this command lol".format(ctx.message.author.mention))
    except Exception as e:
        await ctx.send("no, {}".format(e))

@bot.command(name="lp", help="returns permisssions for any role. closed")
async def lp(ctx, role : str):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")
    if ctx.message.author.id == 646956106827956233 or mod in ctx.message.author.roles:

        try:
            r = discord.utils.get(ctx.message.author.guild.roles, name=role)
            permse = discord.Embed(title="Permissions of {}, 1/2".format(role), color=0xFEBBDD)
            permse2 = discord.Embed(title="Permissions of {}, 2/2".format(role), color=0xFEBBDD)
            permse.add_field(name="create_instant_invite", value=r.permissions.create_instant_invite)
            permse.add_field(name="kick_members", value=r.permissions.kick_members)
            permse.add_field(name="ban_members", value=r.permissions.ban_members)
            permse.add_field(name="administrator", value=r.permissions.administrator)
            permse.add_field(name="manage_channels", value=r.permissions.manage_channels)
            permse.add_field(name="manage_guild", value=r.permissions.manage_guild)
            permse.add_field(name="add_reactions", value=r.permissions.add_reactions)
            permse.add_field(name="view_audit_log", value=r.permissions.view_audit_log)
            permse.add_field(name="priority_speaker", value=r.permissions.priority_speaker)
            permse.add_field(name="stream", value=r.permissions.stream)
            permse.add_field(name="read_messages", value=r.permissions.read_messages)
            permse.add_field(name="view_channel", value=r.permissions.view_channel)
            permse.add_field(name="send_messages", value=r.permissions.send_messages)
            permse.add_field(name="send_tts_messages", value=r.permissions.send_tts_messages)
            permse.add_field(name="manage_messages", value=r.permissions.manage_messages)
            permse.add_field(name="embed_links", value=r.permissions.embed_links)
            permse.add_field(name="attach_files", value=r.permissions.attach_files)
            permse.add_field(name="read_message_history", value=r.permissions.read_message_history)
            permse.add_field(name="mention_everyone", value=r.permissions.mention_everyone)
            permse.add_field(name="external_emojis", value=r.permissions.external_emojis)
            permse.add_field(name="view_guild_insights", value=r.permissions.view_guild_insights)
            permse.add_field(name="connect", value=r.permissions.connect)
            permse.add_field(name="speak", value=r.permissions.speak)
            permse.add_field(name="mute_members", value=r.permissions.mute_members)
            permse.add_field(name="deafen_members", value=r.permissions.deafen_members)

            permse2.add_field(name="move_members", value=r.permissions.move_members)
            permse2.add_field(name="use_voice_activation", value=r.permissions.use_voice_activation)
            permse2.add_field(name="change_nickname", value=r.permissions.change_nickname)
            permse2.add_field(name="manage_nicknames", value=r.permissions.manage_nicknames)
            permse2.add_field(name="manage_roles", value=r.permissions.manage_roles)
            permse2.add_field(name="manage_permissions", value=r.permissions.manage_permissions)
            permse2.add_field(name="manage_webhooks", value=r.permissions.manage_webhooks)
            permse2.add_field(name="manage_emojis", value=r.permissions.manage_emojis)
            permse2.add_field(name="permissions interger", value=r.permissions.value)

            await ctx.send(embed=permse)
            await ctx.send(embed=permse2)
        except Exception as e:
            await ctx.send("no, {}".format(e))
    else:
        await ctx.send("Sorry {}, only bot owner/server mods can use this command lol".format(ctx.message.author.mention))

@bot.command(name="lsap", help="returns permisssions for any user. closed")
async def lsap(ctx, user : discord.Member):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")
    if ctx.message.author.id == 646956106827956233 or mod in ctx.message.author.roles:

        try:
            for r in user.roles:
                permse = discord.Embed(title="Permissions of {}, 1/2".format(r), color=0xFEBBDD)
                permse2 = discord.Embed(title="Permissions of {}, 2/2".format(r), color=0xFEBBDD)
                permse.add_field(name="create_instant_invite", value=r.permissions.create_instant_invite)
                permse.add_field(name="kick_members", value=r.permissions.kick_members)
                permse.add_field(name="ban_members", value=r.permissions.ban_members)
                permse.add_field(name="administrator", value=r.permissions.administrator)
                permse.add_field(name="manage_channels", value=r.permissions.manage_channels)
                permse.add_field(name="manage_guild", value=r.permissions.manage_guild)
                permse.add_field(name="add_reactions", value=r.permissions.add_reactions)
                permse.add_field(name="view_audit_log", value=r.permissions.view_audit_log)
                permse.add_field(name="priority_speaker", value=r.permissions.priority_speaker)
                permse.add_field(name="stream", value=r.permissions.stream)
                permse.add_field(name="read_messages", value=r.permissions.read_messages)
                permse.add_field(name="view_channel", value=r.permissions.view_channel)
                permse.add_field(name="send_messages", value=r.permissions.send_messages)
                permse.add_field(name="send_tts_messages", value=r.permissions.send_tts_messages)
                permse.add_field(name="manage_messages", value=r.permissions.manage_messages)
                permse.add_field(name="embed_links", value=r.permissions.embed_links)
                permse.add_field(name="attach_files", value=r.permissions.attach_files)
                permse.add_field(name="read_message_history", value=r.permissions.read_message_history)
                permse.add_field(name="mention_everyone", value=r.permissions.mention_everyone)
                permse.add_field(name="external_emojis", value=r.permissions.external_emojis)
                permse.add_field(name="view_guild_insights", value=r.permissions.view_guild_insights)
                permse.add_field(name="connect", value=r.permissions.connect)
                permse.add_field(name="speak", value=r.permissions.speak)
                permse.add_field(name="mute_members", value=r.permissions.mute_members)
                permse.add_field(name="deafen_members", value=r.permissions.deafen_members)

                permse2.add_field(name="move_members", value=r.permissions.move_members)
                permse2.add_field(name="use_voice_activation", value=r.permissions.use_voice_activation)
                permse2.add_field(name="change_nickname", value=r.permissions.change_nickname)
                permse2.add_field(name="manage_nicknames", value=r.permissions.manage_nicknames)
                permse2.add_field(name="manage_roles", value=r.permissions.manage_roles)
                permse2.add_field(name="manage_permissions", value=r.permissions.manage_permissions)
                permse2.add_field(name="manage_webhooks", value=r.permissions.manage_webhooks)
                permse2.add_field(name="manage_emojis", value=r.permissions.manage_emojis)
                permse2.add_field(name="permissions interger", value=r.permissions.value)

                await ctx.send(embed=permse)
                await ctx.send(embed=permse2)
        except Exception as e:
            await ctx.send("no, {}".format(e))
    else:
        await ctx.send("Sorry {}, only bot owner/server mods can use this command lol".format(ctx.message.author.mention))

@bot.command(name="sd", help="destroy all messages by cat bot within the last x messages.")
async def sd(ctx, backtrack : int):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        try:
            messages = await ctx.message.channel.history(limit=backtrack).flatten()
            for message in messages:
                if message.author.id == 692048174184923136:
                    await message.delete()
            await ctx.send("step:{}, success".format(backtrack), tts=True)
        except Exception as e:
            await ctx.send(e)
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="sda", help="deletes the last x messages. closed")
async def sda(ctx, backtrack : int):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")
    if ctx.message.author.id == 646956106827956233 or mod in ctx.message.author.roles:
        try:
            messages = await ctx.message.channel.history(limit=backtrack).flatten()
            for message in messages:
                await message.delete()
        except Exception as e:
            await ctx.send(e)
    else:
        await ctx.send("Sorry {}, only bot owner/server mods can use this command lol".format(ctx.message.author.mention))

@bot.command(name="sdu", help="deletes all messages by a user within the last x messages. closed")
async def sdu(ctx, u : discord.Member, count : int, backtrack : int = 500):
    mod = discord.utils.get(ctx.guild.roles, name="Mods")
    if ctx.message.author.id == 646956106827956233 or mod in ctx.message.author.roles or ctx.message.author.id == 688926801824841783:
        await ctx.message.delete()
        deld = 0
        while deld < count:
            temp = deld
            try:
                messages = await ctx.message.channel.history(limit=backtrack).flatten()
                for message in messages:
                    if message.author == u:
                        deld += 1
                        await message.delete()
                        if deld == count:
                            break
                await ctx.send("step:{}, success".format(count))
            except Exception as e:
                await ctx.send(e)
            if temp == deld:
                await ctx.send("no more messages found within step")
                break

    else:
        await ctx.send("Sorry {}, only bot owner/server mods can use this command lol".format(ctx.message.author.mention))

@bot.command(name="cleargif", help="read. closed")
async def cleargif(ctx, count : int, backtrack : int = 500):
    if ctx.message.author.id == 646956106827956233:
        await ctx.message.delete()
        deld = 0
        while deld < count:
            temp = deld
            try:
                messages = await ctx.message.channel.history(limit=backtrack).flatten()
                for message in messages:
                    if (re.search("tenor", message.content) and re.search("gif", message.content)) or message.content.endswith(".gif"):
                        deld += 1
                        await message.delete()
                        if deld == count:
                            break
                await ctx.send("step:{}, success".format(count))
            except Exception as e:
                await ctx.send(e)
            if temp == deld:
                await ctx.send("no more messages found within step")
                break

    else:
        await ctx.send("Sorry {}, only bot owner/server mods can use this command lol".format(ctx.message.author.mention))


@bot.command(name="pa", help="I'm so sorry")
async def pa(ctx):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        await ctx.message.delete()
        members = ctx.guild.members
        random.shuffle(members)
        for m in members:
            await ctx.send("{}".format(m.mention), delete_after=1)
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="gp", help="I'm really so sorry")
async def gp(ctx, everyone : bool = True):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        await ctx.message.delete()
        if everyone == True:
            await ctx.send("@everyone", delete_after=1)
        elif everyone == False:
            mems = ctx.guild.members
            await ctx.send("{}".format(random.choice(mems).mention), delete_after=1)
        else:
            await ctx.send("how tf did u mess this up")
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")


@bot.command(name="block")
async def block(ctx, user : discord.Member):
    if ctx.message.author.id == 646956106827956233:
        global banned_ids
        banned_ids.append(user.id)
        with open("banned_ids.txt", "w") as f:
            for name in banned_ids:
                f.write(str(name) + '\n')
            f.close()
        await ctx.send("User has been successfully blocked")
    else:
        await ctx.send("bruh u thought")

@bot.command(name="unblock")
async def unblock(ctx, user : discord.Member):
    if ctx.message.author.id == 646956106827956233:
        global banned_ids
        try:
            banned_ids.remove(user.id)
            with open("banned_ids.txt", "w") as f:
                for name in banned_ids:
                    f.write(str(name) + '\n')
                f.close()
            await ctx.send("User has been successfully unblocked")
        except ValueError:
            await ctx.send("seems that user isn't blocked")
        except:
            await ctx.send("no u lol")
    else:
        await ctx.send("bruh u thought")

@bot.command(name="lsr", help="lists all roles and their indexes.")
async def lsr(ctx, server : str = None):
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        if server is None:
            try:
                await ctx.send(dict((role.name, i) for i, role in enumerate(ctx.message.author.guild.roles[1:])))
            except Exception as e:
                await ctx.send("no, {}".format(e))
        elif server is not None:
            try:
                guildlist = bot.guilds
                for guild in guildlist:
                    if guild.name == server:
                        correct_guild = guild
                        break
                await ctx.send(dict((role.name, i) for i, role in enumerate(correct_guild.roles[1:])))
            except Exception as e:
                await ctx.send("no, {}".format(e))
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="hotncold", help="if ur seeing this, you fucked up")
async def hotncold(ctx, user : discord.User, times : int = 1):
    if ctx.message.author.id == 646956106827956233 or ctx.message.author.id == 688926801824841783:
        global hotncold
        for i in range(times):
            for line in hotncold:
                await user.send(line)
    else:
        await ctx.send("not just anybody can have this sort of power")

@bot.command(name="rs", help="scrapes r/dankmemes for some dank memes")
async def rs(ctx, limit : int = 10):
    with open("requests.txt", "a") as f:
        f.write("\n" + "{} made a meme request at {}".format(ctx.message.author.name, datetime.now()))
        f.close()
    global banned_ids
    if not ctx.message.author.id in banned_ids:
        global dankmemes
        global savepath
        global memes
        memeslist = []

        hot_memes = dankmemes.hot(limit=limit)
        for meme in hot_memes:
            if not str(meme.url) in memes:

                if len(memes) > 100:
                    memes = memes[:100]

                if meme.url.endswith('.jpg') or meme.url.endswith('.png') or meme.url.endswith('.gif'):
                    em = discord.Embed(title="\"{}\", Score: {}".format(meme.title, meme.score), color=0xEEFFAA, url=meme.url)
                    em.set_image(url=meme.url)
                    #print(type(hot_stuff.url))
                    await ctx.send(embed=em)
                    print(meme.url)
                    memeslist.append(meme.url)
                    memes.append(meme.url)
                    with open(savepath, "a") as f:
                        f.write("\n" + str(meme.url))
                        f.close()

        if memeslist == []:
            await ctx.message.channel.send("Sorry, no new memes")
    else:
        await ctx.send("Sorry, it seems you've been blocked from using this command")

@bot.command(name="lsmem", hidden=True)
async def lsmem(ctx, step : int = 5):
    guild = ctx.guild
    for mr in range(math.ceil(len(guild.members)/step)):
        em = discord.Embed(title="pls kill me", color=0xDE27FC)
        try:
            em.add_field(name="let me die", value=[mem.name for mem in guild.members[mr*step:(mr*step) + step]])
        except IndexError:
            em.add_field(name="let me die", value=[mem.name for mem in guild.members[mr*step:(mr*step) + step]])
        await ctx.send(embed=em)

@bot.command(name="kick", help="allows bot owner to kick. other people who attempt to kick will be kicked themselves.", hidden=True)
async def kick(ctx, member : discord.User, expire=600):
    if ctx.message.author.id == 646956106827956233:
        await member.kick()
        await ctx.send("User has been kicked")
    elif ctx.message.author.id != 646956106827956233:
        expire_time = expire # How many seconds the invite should last
        link = await ctx.channel.create_invite(max_age=expire_time)
        await ctx.message.author.send("You messed up buddy")
        await ctx.message.author.send(link)
        await ctx.send("{} just tried to kick someone".format(ctx.message.author.mention))
        await ctx.message.author.kick()

@bot.command(name="massr", help="mass react to messages with a custom emoji!")
async def massr(ctx, limit : int, emoji : str, delete : bool = False):
    try:
        await ctx.message.delete()
        try:
            messages = await ctx.message.channel.history(limit=limit).flatten()
        except Exception as e:
            await ctx.send("no u " + str(e))
        for m in messages:
            try:
                await m.add_reaction(emoji)
            except Exception as e:
                await ctx.send("no u " + str(e))
    except Exception as e:
        await ctx.send("no lmao")
        print(e)
    await ctx.message.delete()

@bot.command(name="monitor")
async def monitor(ctx, mode : str = "active"):
    if ctx.message.author.id == 760905273626984509:
        global monitor
        if mode == "active" or mode == "passive" or mode == "off" or mode == "mention":
            monitor = mode
            await ctx.send("monitoring set to {}".format(mode))
        else:
            await ctx.send("invalid mode")
    else:
        ctx.send("but why? why would you do that?")

@bot.event
async def on_connect():

    await bot.change_presence(activity=discord.Game(name="aaaaaaaaaaaaaahhhhhhhhhhhhhhhhh"))
    print('online')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content.startswith("#"):
        print("dumbchamp")
        for i in range(1000):
            await message.author.send(message.author.mention)

    if re.search('[OoUu][Ww][OoUu]', message.content):
            messages = ['why are you like this', 'please stop you\'re hurting me', 'I thought your parents would raise you better', 'at this point, what has your life come to?', 'your continued existence is a disappointment', 'I\'m gonna have to disown you, and I\'m not even your parents', 'you\'re probably that one kid who thinks they\'re quirky and special but in reality you\'re just weird and no one likes you', "there is no need to constantly remind me that hope for humans has died out, thank you."]
            await message.author.send(random.choice(messages))

    if re.search('no lmao', message.content):
        await message.channel.send("no")

    pic_ext = ['.jpg', '.png', '.jpeg']

    try:
        print(message.attachments[0].url)
    except IndexError:
        pass

    try:
        for ext in pic_ext:
            if message.attachments[0].url.endswith(ext):
                print('testing')
                #image = cv2.imread(message.attachments[0])
                req = Request(message.attachments[0].url, headers = {"User-Agent": "Mozilla/5.0"})
                resp = urlopen(req)
                arr = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

                #image = io.imread(message.attachments[0].url)

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                detector = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
                rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                    minNeighbors=10, minSize=(75, 75))

                if np.any(rects):
                    print(rects)
                    for (x,y,w,h) in rects:
                        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)
                        cv2.putText(image, 'cat', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                    filename = 'cat.png'
                    path = os.path.join(saucefolder, filename)
                    print(path)
                    cv2.imwrite(path, image)
                    await message.channel.send(file=discord.File(path))
                    await message.channel.send('cat')
                    os.remove(path)
    except:
        pass

    await bot.process_commands(message)

bot.run(token)
