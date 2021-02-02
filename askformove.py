################################################################################################
#                                                                                              #
#                             Ask for move bot by AnnikenYT                                    #
#      ___      .__   __. .__   __.  __   __  ___  _______ .__   __. ____    ____ .___________.#
#     /   \     |  \ |  | |  \ |  | |  | |  |/  / |   ____||  \ |  | \   \  /   / |           |#
#    /  ^  \    |   \|  | |   \|  | |  | |  '  /  |  |__   |   \|  |  \   \/   /  `---|  |----`#
#   /  /_\  \   |  . `  | |  . `  | |  | |    <   |   __|  |  . `  |   \_    _/       |  |     #
#  /  _____  \  |  |\   | |  |\   | |  | |  .  \  |  |____ |  |\   |     |  |         |  |     #
# /__/     \__\ |__| \__| |__| \__| |__| |__|\__\ |_______||__| \__|     |__|         |__|     #
#                               (c) All rights Reserved                                        #
#                                                                                              #
################################################################################################



import discord
from discord.ext import commands
PREFIX = 'afm!'
INTENTS = discord.Intents.default()
INTENTS.members = True
INTENTS.presences = True
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

#Config

# Paste your discord token from http://discord.com/developers/applications
TOKEN = 'ODA1MTc3MDQwOTk1MjIxNTM0.YBXFjg.XZNRq8-gPN-4DVxGPo_ceEqAD3Q'

# Change these variables for your Server
# If you dont know where to find the Server ID, see this: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

# Paste the SERVER ID here
server_id = 792468889707085856

# Paste the ID of the channel, where you want users to join
channel_id = 793240226700722197

# A list of all of your Staff Members seperated by ",". This may be replaced in a Future Version
staff_ids = [781869496759484426]

# Whether the bot should use the staff_ids list, or build the list automatically based on the "Move Members" permission.
custom_list = False

# The message that is send to your staff members
move_message = "{} is waiting"

# Do not touch this
staff_members = []


#Code (Do not touch this unless you know what your doing.)
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    guild = bot.get_guild(server_id)
    if custom_list:
        for staff_id in staff_ids:
            staff_member = guild.get_member(staff_id)
            if staff_member is not None and staff_member not in staff_members:
                staff_members.append(staff_member)
                print("Added {} to staff members".format(staff_member))
    else:
        for user in guild.members:
            if user.guild_permissions.move_members and not user.bot:
                staff_members.append(user)
                print("Added {} to staff members".format(user))


@bot.command()
async def ping(ctx):
    await ctx.send('pong! {}'.format(round(bot.latency,3)))

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        if after.channel.id == channel_id:
            for staff_member in staff_members:
                if str(staff_member.status) == "online" or str(staff_member.status) == "idle":
                    dm = await staff_member.create_dm()
                    await dm.send(move_message.format(member))

        # for staff_id in staff:
        #     staff_user = bot.get_user(staff_id)
        #     print(str(staff_member))
        #     print(staff_member.status)
        #     if str(staff_member.status) == "offline":
        #         dm = await staff_member.create_dm()
        #         await dm.send(str(member) + " möchte gemoved werden")

bot.run(TOKEN)