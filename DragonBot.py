import discord
import asyncio

description = "Derp Derp I'ma Dargon"
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as: " + str(client.user.name))
    print("Ready to BURN!")
    print("--------------")

@client.event
async def on_message(message):
    if message.content == ("Ping!"):
        await client.send_message(message.channel, "{0.author.mention} Pong! Roar!".format(message))
    if message.content == ("Dragon-kill"):
        userid = str(message.author.id)
        if userid == "123022092676366336":
            await client.send_message(message.channel, "Goodbye cruel world! Roar!")
            print("Shutting down :(")
            await client.logout()
        else:
            await client.send_message(message.channel, "You are not powerful enough to slay me, fool! Roar!")
            print("Someone else tried to slay me. It was" + str(message.author))
            return
    if message.content == ("Dragon-infoget"):
        await client.send_message(message.channel, "Your info has been stored in the console! Roar!")
        #CHANGE THESE TO BE A SPECIFIED USER INSTEAD#
        mauthor = "Message Author: " + str(message.author)
        mid = "User ID: " + str(message.author.id)
        mcreated = "Account Created Time: " + str(message.author.created_at)
        mroles = "Roles(WIP):" + str(message.author.roles)
        mjoined = "Server Joined Time: " + str(message.author.joined_at)
        mcolour = "Current Name Colour: " + str(message.author.colour)
        print(mauthor)
        print(mid)
        print(mcreated)
        print(mjoined)
        print(mroles)
        print(mcolour)
        await client.send_message(message.channel, "```"+ mauthor +"\n" + mid +"\n"+mcreated+"\n"+mjoined+"\n"+mroles+"\n"+mcolour+ "```")
    if message.content.startswith == ("Dragon-count"):
        for x in range(1,(n+1)):
            await client.send_message(message.channel, x)

client.run("MzYyNTc2Mjk2MDI4NTM2ODUz.DK1WJA.SNtRX5NQPedKStBapJh_M0Lz1f0")
