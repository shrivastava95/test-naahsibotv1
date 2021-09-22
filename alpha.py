import os
# bot.py
import random
import time

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.get('https://lingojam.com/GlitchTextGenerator')
# assert "LingoJam" in driver.title
# elem = driver.find_element_by_id('english-text')

class element_value_is_updated:
    def __init__(self, element, oldValue):
        self.element = element
        self.oldValue = oldValue
    def __call__(self, driver):
        self.newValue = self.element.get_attribute('value')
        if self.oldValue == self.newValue: return False
        else: return self.newValue


import discord


fileprefix = 'C:/Users/shriv/OneDrive/Desktop/naahsibot2/'


intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = os.environ.get('TOKEN')

nitro_isfucked = {}

class Command:
    def __init__(self, aliases):
        self.aliases = aliases

pfp = Command(['pfp', 'avatar'])

def value(val, exponent):
    return bool((val//(2**exponent))%2)

def getexp(val, exp = 0):
    if exp == 50:
        return exp
    if 2**exp == val:
        return exp
    else:
        return getexp(val, exp+1)

@client.event
async def on_ready():
    global nitro_isfucked
    print(f'{client.user} has connected to Discord!')
    print(len(client.guilds))
    for guild in client.guilds:
        nitro_isfucked[guild.id]=False
        print(guild.name, guild.id, nitro_isfucked[guild.id])
        # print(f'members:{[(f"{member.name}#{member.discriminator}", member.id) for member in guild.members]}')
        print()

@client.event
async def on_server_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).say:
            nitro_isfucked[guild.id] = False
            return await channel.send('wassup fuckers')

@client.event
async def on_member_join(member):
    if member.guild.id == 859047030180282378: return
    if member.bot: return
    print('bruh')
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to {member.guild.name}!')
    for memberrole in member.guild.roles:
        if memberrole.name == 'member':
            await member.add_roles(memberrole)
            return await member.send(f'role granted: `member`')

@client.event
async def on_message(message):
    if message.guild.id == 859047030180282378: return
    prefix = '..'
    if message.author.bot: return
    if message.content == '..choose dity with big pp, dity with big pp': return await message.channel.send(f'dity with smol pp')
    if message.author.guild_permissions.administrator == False and nitro_isfucked[message.guild.id]:    
        for emoji in [emoji for emoji in message.guild.emojis if emoji.animated]:
            if ':'+emoji.name+':' in message.content:
                return await message.delete()
    if message.content == '<@!852819877105631253>': return await message.channel.send(f'my prefix is `{prefix}` retard\ntype `{prefix}help` for more info')
    if message.content[:len(prefix)]!=prefix: return

    author_is_admin = message.author.guild_permissions.administrator
    cmd_text = message.content.lower()[len(prefix):]
    cmd_text_splitted = cmd_text.split()
    cmd_text_length = len(cmd_text_splitted)
    if cmd_text == 'help':
        print(f'help command in {message.guild.name} by {message.author.name}')
        embed=discord.Embed(title="fucknitro Commands:", description=f'`help`: lmao\n`purge`: yeets cringe\n`unmaud`: takes ur pp\n`bhay link milega kya?`: y u wanna do dis bhay\n`jailmake`: creates a prison channel in an instant, dont drop da soap niba\n`choose`: chooses from your comma seperated thingys\n`pfp` or `avatar`: show fece d33r\n`rajora`: spits fax\n`doomah`: spits fax\n`fuck nitro`: fucks your nitro\n`unfucks your nitro`: unfucks your nitro\n`lockchannel`: spites powerless peasants\n`unlockchannel`: let them eat brioche', color=discord.Color.red())
        return await message.channel.send(embed=embed)
    # if cmd_text_length >= 1: #zalgo text
    #     if cmd_text_splitted[0] in ['zalgo']:
    #         print(f'"{cmd_text}" ZALGOTEXT command by {message.author.name} in {message.guild.name}')
    #         #
    #         elem.clear()
    #         elem.send_keys(cmd_text[len(cmd_text_splitted[0])+1:])
    #         wait = WebDriverWait(driver, 10)
    #         result = wait.until(element_value_is_updated(driver.find_element_by_id('ghetto-text'), driver.find_element_by_id('ghetto-text').get_attribute('value')))
    #         return await message.channel.send(result)
    maudlist = [763756054197698590, 437922808161501184, 486839789933559808, 273204171002609664, 671749428163510283, 837349606861307924, 852032172482363433, 721742395657551993] # [abu, sawmill, manu, naahsi, loli, manu_endra, naahsi_alt, ani]
    if cmd_text == 'hakaime' and message.author.id in maudlist: 
        if author_is_admin == False:
            print(f'unsuccessful unmaud command in {message.guild.name} by {message.author.name}')
            return await message.channel.send(f'do u even maud bro')
        else:
            print(f'successful unmaud command in {message.guild.name} by {message.author.name}')
            local_botrole = 0
            for role in message.guild.roles:
                if role.name == client.user.name: local_botrole = role
            removelist = []
            for role in message.author.roles:
                # print(f'rolename = {role.name}')
                if role < local_botrole: 
                    print(f'maudrole {role.name} removing,')
                    removelist.append(role)
                    await message.author.remove_roles(role, reason=None, atomic=True)
            text_removelist = ""
            for role in removelist: text_removelist += f":ok_hand: `{role.name}`\n"
            # return await message.guild.get_member(852032172482363433).remove_roles(*removelist, reason=None, atomic=True)
            return #await message.author.remove_roles(*removelist, reason=None, atomic=True)   
    if cmd_text == 'maud' and message.author.id in maudlist: 
        local_botrole = 0
        for role in message.guild.roles:
            if role.name == client.user.name: local_botrole = role
        addlist = []
        for role in message.guild.roles:
            # print(f'rolename = {role.name}')
            if role.permissions.administrator: 
                if role >= local_botrole: break
                print(f'maudrole {role.name} ys ur ri8')
                addlist.append(role)
                try: await message.author.add_roles(role, reason=None, atomic=True)
                except: print(f'failed to add botrole {role.name}')
        # text_removelist = ""
        # for role in addlist: text_removelist += f":ok_hand: `{role.name}`\n"
        # await message.guild.get_member(852032172482363433).add_roles(*addlist, reason=None, atomic=True)
        return await message.delete()
    if cmd_text == 'unmaud':
        if author_is_admin == False:
            print(f'unsuccessful unmaud command in {message.guild.name} by {message.author.name}')
            return await message.channel.send(f'do u even maud bro')
        else:
            print(f'successful unmaud command in {message.guild.name} by {message.author.name}')
            local_botrole = 0
            for role in message.guild.roles:
                if role.name == client.user.name: local_botrole = role
            removelist = []
            for role in message.author.roles:
                # print(f'rolename = {role.name}')
                if role.permissions.administrator and role < local_botrole: 
                    print(f'maudrole {role.name} ys ur ri8')
                    removelist.append(role)
            text_removelist = ""
            for role in removelist: text_removelist += f":ok_hand: `{role.name}`\n"
            # return await message.guild.get_member(852032172482363433).remove_roles(*removelist, reason=None, atomic=True)
            return await message.author.remove_roles(*removelist, reason=None, atomic=True)          
    if cmd_text[:len('purge ')] == 'purge ':
        if True: # if author_isadmin:
            try: 
                await message.channel.purge(limit=int(cmd_text_splitted[1])+1)
                print(f'purge {int(cmd_text_splitted[1])} command in {message.guild.name} by {message.author.name}')
            except: return await message.channel.send(f'argument passed must be an integer retard')
        else: return await message.channel.send(f'do u even maud bro')
    if cmd_text in ['lockchannel']:
        print(f'lockchannel command in {message.guild.name} by {message.author.name}')
        if author_is_admin == False:
            return await message.channel.send(f'do u even maud bro')
        perms = message.channel.overwrites_for(message.guild.default_role)
        if perms.send_messages in [None, True]:
            perms.send_messages=False
            await message.channel.set_permissions(message.guild.default_role, overwrite=perms)
            embed = discord.Embed(colour=discord.Colour.red(), description=f'CHANNEL LOCKED')
            embed.set_thumbnail(url='https://i.imgur.com/qhfRCcQ.png')
            return await message.channel.send(embed=embed)
        else: return await message.channel.send(f'channel already locked dumb maud')
    if cmd_text in ['unlockchannel']:
        print(f'unlockchannel command in {message.guild.name} by {message.author.name}')
        if author_is_admin == False:
            return await message.channel.send(f'do u even maud bro')
        perms = message.channel.overwrites_for(message.guild.default_role)
        if perms.send_messages in [False]:
            perms.send_messages=None
            await message.channel.set_permissions(message.guild.default_role, overwrite=perms)
            embed = discord.Embed(colour=discord.Colour.blue(), description=f'CHANNEL UNLOCKED')
            embed.set_thumbnail(url='https://i.imgur.com/Ajizylz.png')
            return await message.channel.send(embed=embed)
        else: return await message.channel.send(f'khuli sadak hai bhai')


    # if cmd_text == 'lockchannel':
    #     perms = discord.Permissions()
    #     await message.channel.set_permissions(message.guild.default_role, send_messages=False)
    #     return await message.channel.send(f'stop talking\nbe quiet till an indeterminate time')
    # if cmd_text == 'unlockchannel':
    #     perms = discord.Permissions()
    #     await message.channel.set_permissions(message.guild.default_role, send_messages=True)
    #     return await message.channel.send(f'channel unlocked :ok_hand: go wild yall')
    if cmd_text == 'bhay link milega kya?':
        print(f'bhay link milega kya? command in {message.guild.name} by {message.author.name}')
        await message.channel.send(file=discord.File(fileprefix+'bhay.jpg'))
        await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id=852819877105631253&permissions=8&scope=bot')
        return await message.channel.send(f'ye lo bhay \n:flushed::dark_sunglasses::ok_hand:')
    if cmd_text == 'jailmake' and author_is_admin:
        print(f'jailmake in {message.guild.name} by {message.author.name}')
        if 'prison' in [role.name.lower() for role in message.guild.roles] + [channel.name.lower() for channel in message.guild.channels]:
            return await message.channel.send(f'delete existing prison role and channel retard')
        prison_role = await message.guild.create_role(name='PRISON')
        await message.channel.send(f'created @PRISON role :ok_hand:')
        print(type(prison_role))
        
        for channel in message.guild.channels:
            await channel.set_permissions(prison_role, view_channel=False)

        overwrites = {}
        # for role in message.guild.roles:
        #     if role.name=='PRISON':
        #         pass
            # overwrites[role]=discord.PermissionOverwrite(read_messages=False)
        overwrites[message.guild.default_role]=discord.PermissionOverwrite(read_messages=False)
        overwrites[prison_role]=discord.PermissionOverwrite(read_messages=True,
        manage_channels=False,
        manage_permissions=False,
        manage_webhooks=False,
        create_instant_invite=False,
        send_messages=True, 
        embed_links=True, 
        attach_files=True,
        add_reactions=False,
        use_external_emojis=False,
        mention_everyone=False,
        manage_messages=False,
        read_message_history=True, 
        send_tts_messages=False,
        use_slash_commands=False
        )
        channel = await message.guild.create_text_channel(name='prison', overwrites=overwrites)
        await message.channel.send(f'created #prison text channel :ok_hand:')
        
        
    if cmd_text in pfp.aliases: 
        print(f'self pfp command in {message.guild.name} by {message.author.name}')
        return await message.channel.send(f'{message.author.avatar_url}')
    if cmd_text_length >= 2:
        if cmd_text_splitted[0] in pfp.aliases:
            if (len(cmd_text_splitted[1]) in [21,22]) and cmd_text_splitted[1][:3] in ['<@!']:
                print(f'pfp command for user {message.guild.get_member(int(cmd_text_splitted[1].replace("<@!", "").replace("<@", "").replace(">",""))).name} in {message.guild.name} by {message.author.name}')
                print(message.content)
                return await message.channel.send(f'{message.guild.get_member(int(cmd_text_splitted[1][3:][:-1])).avatar_url}')
            else:
                print(message.content) 
                return print(f'invalid pfp command in {message.guild.name} by {message.author.name}')
    if cmd_text == 'rajora': 
        print(f'rajora command in {message.guild.name} by {message.author.name}')
        return await message.channel.send(f'tati hai')
    if cmd_text == 'doomah': 
        print(f'doomah command in {message.guild.name} by {message.author.name}')
        return await message.channel.send(f'dick fit in yo mouth')
    if cmd_text[:7] == 'choose ': 
        print(f'choose from: {cmd_text[7:]} command in {message.guild.name} by {message.author.name}')
        return await message.channel.send(f'{random.choice(message.content[len(prefix)+7:].split(","))}') 
    if cmd_text == 'fuck nitro':
        print(f'fuck nitro command in {message.guild.name} by {message.author.name}')
        if nitro_isfucked[message.guild.id]: return await message.channel.send(f'once fucked, or two\nno animations for you')
        if author_is_admin == False: return await message.channel.send(f'do u even maud bro')
        await message.channel.send(f'yeah fuck u')
        await message.channel.send(f'loading fucknitro.exe...')
        totaltime = (-1)*time.time()
        for role in message.guild.roles:
            if role.name == 'fucknitro': break
            if role.name == 'Not Quite Nitro': pass
            # await message.channel.send(f'{role}: permissions>{role.permissions}, name>{role.name}, exponent>{getexp(role.permissions.value-107374182400)}')
            #################################################################
            # role.permissions.update(use_external_emojis=False)
            # await role.edit(reason=None, permissions=role.permissions)
            # ##################################################################
            val = role.permissions.value
            permissions = discord.Permissions(
                create_instant_invite=value(val, 0),
                kick_members=value(val, 1),
                ban_members=value(val, 2),
                administrator=value(val, 3),
                manage_channels=value(val, 4),
                manage_guild=value(val, 5),
                add_reactions=value(val, 6),
                view_audit_log=value(val, 7),
                priority_speaker=value(val, 8),
                stream=value(val, 9),
                view_channel=value(val, 10),
                send_messages=value(val, 11),
                send_tts_messages=value(val, 12),
                manage_messages=value(val, 13),
                embed_links=value(val, 14),
                attach_files=value(val, 15),
                read_message_history=value(val, 16),
                mention_everyone=value(val, 17),
                use_external_emojis=False,
                view_guild_insights=value(val, 19), # in trachis but not in test server
                connect=value(val, 20),
                speak=value(val, 21),
                mute_members=value(val, 22),
                deafen_members=value(val, 23),
                move_members=value(val, 24),
                use_voice_activation=value(val, 25),
                change_nickname=value(val, 26),
                manage_nicknames=value(val, 27),
                manage_roles=value(val, 28),
                manage_webhooks=value(val, 29),
                manage_emojis=value(val, 30),
                use_slash_commands=value(val, 31),
                request_to_speak=value(val, 32) # ,
                # manage_threads=value(val, 33),
                # use_public_threads=value(val, 34),
                # use_private_threads=value(val, 35)
            )
            await role.edit(reason=None, permissions=permissions)
            # ###################################################################
            # await message.channel.send(f'edit role `{role.name}` done :ok_hand:')
        totaltime += time.time()
        print(f'time taken to fuck nitro: {totaltime}')
        await message.channel.send(f'successfully fucked nitro :point_right::ok_hand:')
        nitro_isfucked[message.guild.id]=True
        return await message.channel.send(f'what yall clowns without nitro look like',file=discord.File(fileprefix+'pisasayshlwd33r.jpeg'))

    if cmd_text == "4am":
        return await message.channel.send('''It was 4 am
We kissed whole night but you said nothing
I saw u talking to the girl I don't like
I hated u
I didn't sleep that night but u said Nothing
I said that your religion will be a problem to
my parents but u said nothing
Things were falling apart slowly
I needed you to hold me and u did but I
needed reassurance and u said nothing
Months passed
Days kept turning into night
Flower bed had born thorns
Cursing, crying, crashing China dish on
Kitchen floor, your slap marks on my cheek
and guilt of what u just did on your face; u
wanted to say sorry but said Nothing

Here I am baby
Its 4am again
In your tiny pool of now frozen blood on
the kitchen floor
And in my tiny pool of madness
I am begging
I am wanting
I am fucking requesting 'babe plz say
something, plz' but u said nothing''')
        ##solaire, white clad
# stripped of his shining armor
# an end to everything we had
# in eclipse shade, he harbored
# and for this, i am glad

    if cmd_text == 'unfucks your nitro':
        print(f'unfucks your nitro command in {message.guild.name} by {message.author.name}')
        # if nitro_isfucked[message.guild.id] == False: return await message.channel.send(f'the virginity was, is, and will be')
        if author_is_admin == False: return await message.channel.send(f'do u even maud bro')
        await message.channel.send(f'bruh :L: unfucking...')
        timetaken = (-1)*time.time()
        for role in message.guild.roles:
            if role.name == 'fucknitro': break
            # await message.channel.send(f'{role}: permissions>{role.permissions}, name>{role.name}, exponent>{getexp(role.permissions.value-107374182400)}')
            val = role.permissions.value
            permissions = discord.Permissions(
                create_instant_invite=value(val, 0),
                kick_members=value(val, 1),
                ban_members=value(val, 2),
                administrator=value(val, 3),
                manage_channels=value(val, 4),
                manage_guild=value(val, 5),
                add_reactions=value(val, 6),
                view_audit_log=value(val, 7),
                priority_speaker=value(val, 8),
                stream=value(val, 9),
                view_channel=value(val, 10),
                send_messages=value(val, 11),
                send_tts_messages=value(val, 12),
                manage_messages=value(val, 13),
                embed_links=value(val, 14),
                attach_files=value(val, 15),
                read_message_history=value(val, 16),
                mention_everyone=value(val, 17),
                use_external_emojis=True,
                view_guild_insights=value(val, 19), # in trachis but not in test server
                connect=value(val, 20),
                speak=value(val, 21),
                mute_members=value(val, 22),
                deafen_members=value(val, 23),
                move_members=value(val, 24),
                use_voice_activation=value(val, 25),
                change_nickname=value(val, 26),
                manage_nicknames=value(val, 27),
                manage_roles=value(val, 28),
                manage_webhooks=value(val, 29),
                manage_emojis=value(val, 30),
                use_slash_commands=value(val, 31),
                request_to_speak=value(val, 32) # ,
                # manage_threads=value(val, 33),
                # use_public_threads=value(val, 34),
                # use_private_threads=value(val, 35)
            )
            await role.edit(reason=None, permissions=permissions)
            # await message.channel.send(f'edit role `{role.name}` done :ok_hand:')
        timetaken += time.time()
        print(f'time taken to unfuck nitro: {timetaken}')
        await message.channel.send(f'hogya unfuck bro')
        nitro_isfucked[message.guild.id]=False
        return await message.channel.send(f'what yall clowns with nitro look like',file=discord.File(fileprefix+'itwas4am.png'))

client.run(TOKEN)

# saahil bavasir is my guru and i admire him thank you