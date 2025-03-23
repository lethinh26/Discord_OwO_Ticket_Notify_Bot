import discord
from discord.ext import commands, tasks
from pymongo import MongoClient

mongo = MongoClient("mongodb+srv://")
db = mongo.OwO
noti = db.noti

bot = commands.Bot(command_prefix="*", intents=discord.Intents.default())

NOTI_CHANNEL_ID = 123  
TOKEN = ""
ROLE_ID = 123

@bot.event
async def on_ready():
    print(bot.user)
    check_ticket.start() 

async def update_embed():
    data = noti.find_one({"_id": "stock_tracker"})
    stocks = data.get("stocks", [])
    prices = data.get("prices", [])
    embed_id = data.get("embed_id", [])

    embed = discord.Embed(
        title="🎟️ Ticket",
        description="<#822972235996201021>",
        color=discord.Color.green()
    )

    if stocks and prices:
        for index, (stock, price) in enumerate(zip(stocks[:10], prices[:10]), start=1):  
            embed.add_field(
                name=f"#{index} - Stock: {stock}",
                value=f"Price: {price} OwO",
                inline=False
            )
    else:
        embed.description = "No ticket available"

    embed.set_footer(text="Automatically updated every 30 seconds")

    channel = bot.get_channel(NOTI_CHANNEL_ID)
    if not channel:
        print("Channel not found!")
        return

    if embed_id:
        for i, message_id in enumerate(embed_id):
            try:
                msg = await channel.fetch_message(message_id)
                await msg.edit(embed=embed)
            except discord.NotFound:
                msg = await channel.send(embed=embed)
                embed_id[i] = msg.id 
    else:
        msg = await channel.send(embed=embed)
        embed_id.append(msg.id)

    noti.update_one(
        {"_id": "stock_tracker"}, 
        {"$set": {"embed_id": embed_id}}
    )

    await channel.send(f"<@&{ROLE_ID}>", delete_after=15)


@tasks.loop(seconds=30)
async def check_ticket():
    data = noti.find_one({"_id": "stock_tracker"})
    
    if data and data.get("ticket", False):
        await update_embed()
        noti.update_one(
            {"_id": "stock_tracker"}, 
            {"$set": {"ticket": False}}
        )

bot.run(TOKEN)
