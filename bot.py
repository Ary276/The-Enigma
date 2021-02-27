# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import requests
import json
from discord.ext.tasks import loop
import datetime
import time
from math import inf as infinity

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
apikey = os.getenv("apikey")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='%', intents = intents)

msg_count = {}

@bot.event
async def on_command(ctx, *args):
	log = bot.get_channel(int(os.getenv('log_channel')))
	if ctx.command.name == "rant":
		return
	log_content = str(ctx.message.author) + '\n' + str(ctx.guild) + "  " + str(ctx.channel) + '\n' + str(ctx.message.content) + '\n' + str(datetime.datetime.now(IST))
	await log.send(embed=discord.Embed(title = ctx.command.name, description = log_content, color=discord.Color.random()).set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url))

@bot.event
async def on_ready():

	activity = discord.Game("%help  At your Service")
	await bot.change_presence(activity=activity)
	print("The Enigma has connected")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(os.getenv("unverified")))
    channel_1 = bot.get_channel(int(os.getenv('spam')))
    channel_2 = bot.get_channel(int(os.getenv('senior-spam')))
    await channel.send(f'Hi {member.name}, welcome to IISc UG 20!')
    await channel_1.send(f'Hi {member.name}, welcome to IISc UG 20!')
    await channel_2.send(f'Hi {member.name}, welcome to IISc UG 20!')

@bot.command(name='insult', help='Insults a person')
async def insult(ctx, name):  		
	A = ["artless","bawdy","beslubbering","bootless","churlish","cockered","clouted","craven","currish",	'dankish',	'dissembling',	'droning',	'errant',	'fawning',	'fobbing',	'froward',	'frothy',	'gleeking',	'goatish',	'gorbellied',	'impertinent',	'infectious',	'jarring',	'loggerheaded',	'lumpish',	'mammering',	'mangled',	'mewling',	'paunchy',	'pribbling',	'puking',	'puny',	'quailing',	'rank',	'reeky',	'roguish',	'ruttish',	'saucy',	'spleeny',	'spongy',	'surly',	'tottering',	'unmuzzled',	'vain',	'venomed',	'villainous',	'warped',	'wayward',	'weedy',	'yeasty']
	B = ['base-court','bat-fowling','beef-witted','beetle-headed','boil-brained','clapper-clawed','clay-brained','common-kissing','crook-pated','dismal-dreaming','dizzy-eyed','doghearted','dread-bolted','earth-vexing','elf-skinned','fat-kidneyed','fen-sucked','flap-mouthed','fly-bitten','folly-fallen','fool-born','full-gorged','guts-griping','half-faced','hasty-witted','hedge-born','hell-hated','idle-headed','ill-breeding','ill-nurtured','knotty-pated','milk-livered','motley-minded','onion-eyed','plume-plucked','pottle-deep','pox-marked','reeling-ripe','ough-hewn','rude-growing','rump-fed','shard-borne','sheep-biting','spur-galled','swag-bellied','tardy-gaited','tickle-brained','toad-spotted','urchin-snouted','weather-bitten']
	C = ['apple-john','baggage','barnacle','bladder','boar-pig','bugbear','bum-bailey','canker-blossom','clack-dish','clotpole c','oxcomb','codpiece','death-token','dewberry','flap-dragon','flax-wench','flirt-gill','foot-licker','fustilarian','giglet','gudgeon','haggard','harpy','hedge-pig','horn-beast','hugger-mugger','jolthead','lewdster','lout','maggot-pie','malt-worm','mammet','measle','minnow','miscreant','moldwarp','mumble-news','nut-hook','pigeon-egg','pignut','puttock','pumpion','ratsbane','scut','skainsmate','strumpet','varlet','vassal','whey-face','wagtail']
	response = random.choice(A) + " " + random.choice(B) + " " + random.choice(C) + ". "
	await ctx.send(name + ", thou " + response + ":poop:")

@bot.command(name="hello", help= "Says hello")
async def hello(ctx):
	await ctx.send("Hello " + str(ctx.message.author.display_name))
	await ctx.send(embed = discord.Embed().set_thumbnail(url="https://i2.wp.com/www.bestworldevents.com/wp-content/uploads/2020/05/Hello-Gif.gif?resize=498%2C498"))
@bot.command(name="henlo", help= "Says henlo")
async def henlo(ctx):
	await ctx.send("Henlo " + str(ctx.message.author.display_name))
	await ctx.send(embed = discord.Embed().set_thumbnail(url="https://media.tenor.com/images/ea99007fef8e31fdc5fb84f6f8a69db7/tenor.gif"))
@bot.command(name="heil", help= "Says heil + name")
async def heil(ctx, *, args):
	await ctx.send("Heil " + args[:])
	await ctx.send(embed = discord.Embed().set_thumbnail(url="https://media.tenor.com/images/f8e3620dd1f65faa3cfe74de23fd48b9/tenor.gif"))
@bot.command(name="ask", help= "Replies to a question")
async def ask(ctx):
	answer = ["Yes", "No", "Bruh", "Probably not", "Probably yes", "Maybe", ".....", "I'd rather jump off a buildng", "I don't think so", "Imma head out", "I'm confused", "My brain is kaputt", "Bist du doof?", "Tu eres tonto", "__--|--__", "I'd rather not answer this", "This answer has no scope", "Random fact: Black holes have no hair (wink wink)", "i would tell you the answer but it is complex", "Do you want me to roast you? Nah, I'd rather let Gordon Ramsey do it (Well, he does both forms of roasting well", "Fun Fact: The person asking me this question is dumb", "Let's say yes", "I can't decide", "Yes I guess?", "The answer as as likely to be correct as the one asking it is likely to fail", "*Mystery intensifies*", "*Visible Confusion*", "凸( ͡° ͜ʖ ͡°)"]
	await ctx.send(random.choice(answer))
@bot.command(name="meow", help= "Says meow")
async def meow(ctx):
	await ctx.send("*meow*")
	await ctx.send(embed = discord.Embed().set_thumbnail(url="https://media.tenor.com/images/eff22afc2220e9df92a7aa2f53948f9f/tenor.gif"))
@bot.command(name="fml", help= "For when you feel angry and done with life")
async def fml(ctx):
	links = ["https://media.tenor.com/images/b31834ee195edea55cefbdc57823e287/tenor.gif", "https://i.makeagif.com/media/5-09-2017/yiSLux.gif", "https://static.wikia.nocookie.net/hitlerparody/images/4/49/HitlerPencilThrowGIF.gif/revision/latest/scale-to-width-down/320?cb=20110901130348", "https://i.makeagif.com/media/5-09-2017/OCXl_s.gif", "https://i.makeagif.com/media/11-22-2014/ztpjZw.gif"]
	await ctx.send(embed = discord.Embed().set_image(url=random.choice(links)))
@bot.command(name = "aww", help= "When someone says love or something similar")
async def aww(ctx):
	await ctx.send("Can I just say....... Awwwwwwwwwww x10")
@bot.command(name = "yes", help= "yes")
async def yes(ctx):
	yes1 = "<:yes:802118244722802718>            <:yes:802118244722802718>        <:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718>        <:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718>\n"
	yes2 = "     <:yes:802118244722802718>    <:yes:802118244722802718>           <:yes:802118244722802718>					<:yes:802118244722802718>\n"
	yes3 = "          <:yes:802118244722802718>                <:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718>        <:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718> \n"
	yes4 = "          <:yes:802118244722802718>		        <:yes:802118244722802718>                                <:yes:802118244722802718>\n"
	yes5 = "          <:yes:802118244722802718>		        <:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718>		<:yes:802118244722802718><:yes:802118244722802718><:yes:802118244722802718>"
	await ctx.send(yes1+yes2+yes3+yes4+yes5)
@bot.command(name = "kill", help= "Kill someone by tagging")
async def kill(ctx, *, args):
	await ctx.send("🔪" + args[:] + "🔪")
	await ctx.send("🩸" + " " + "🩸")
@bot.command(name="rant", help="Send your rant anonymously to #rants")
async def rant(ctx, *, args):
	rant_approval = bot.get_channel(int(os.getenv('rant-approval')))
	rants = bot.get_channel(int(os.getenv('rants')))
	guild = bot.get_guild(int(os.getenv('ug20_guild')))
	
	if guild.get_member(ctx.message.author.id) is None:
		await ctx.send("You cannot send a Rant sorry :(")
		return

	def check(reaction):
		return str(reaction.emoji) == '👍' and reaction.message_id == rant.id

	def chek(message):
		return message.content.lower() in ["y", "n"] and message.author == ctx.message.author
	
	try:
		await ctx.send("Do you wish to remain Anonymous? Respond with y/n")
		msg = await bot.wait_for('message', timeout=30.0, check=chek)
	except asyncio.TimeoutError:
		await ctx.send("Your request has timed out")
	else:
		rant = await rant_approval.send(args[:])
		await ctx.send("Your rant has been sent!")
		try:
			reaction = await bot.wait_for('raw_reaction_add', timeout=3600.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send("Your rant has timed-out. Either a mod has not approved it yet, or your message violates the rules. If it the former, feel free to send again later.")
		else:
			await ctx.send("Your rant has been approved!")
			if(msg.content.lower() == "n"):
				await rants.send(embed = discord.Embed(type = "article", description = rant.content, color=discord.Color.random()).set_author(name=msg.author.display_name, icon_url=msg.author.avatar_url))
			else:
				await rants.send(embed = discord.Embed(type = "article", description = rant.content, color=discord.Color.random()).set_author(name="Anonymous", icon_url="https://blog.radware.com/wp-content/uploads/2020/06/anonymous.jpg"))

@bot.command(name = "gif", help= "sends a gif based on search term")
async def gif(ctx, search_term):
	ind = random.choice(range(20))
	r = requests.get(
    "https://api.tenor.com/v1/random?q=%s&key=%s&contentfilter=%s&locale=%s&media_filter=%s&limit=1" % (search_term, apikey, "low", "en_IN", "minimal"))
	try :
		url = json.loads(r.content)['results'][0]['media'][0]['tinygif']['url']
	except IndexError:
		await ctx.send("Sorry, there are no GIFs with that search term")
	else:
		await ctx.send(embed = discord.Embed().set_image(url=url))
@bot.command(name = "tgif", help= "sends a trending gif")
async def gif(ctx):
	ind = random.choice(range(20))
	t = requests.get(
    "https://g.tenor.com/v1/trending_terms?key=%s&locale=%s" % (apikey, "en_IN"))
	term = json.loads(t.content)['results'][ind]
	r = requests.get(
    "https://api.tenor.com/v1/random?q=%s&key=%s&contentfilter=%s&locale=%s&media_filter=%s&limit=1" % (term, apikey, "low", "en_IN", "minimal"))
	url = json.loads(r.content)['results'][0]['media'][0]['tinygif']['url']
	await ctx.send(embed = discord.Embed(description=term).set_image(url=url))

@bot.command(name="tictactoe", aliases=["ttt"], help="Play Tic Tac Toe with a friend! syntax %ttt _name1_ name2_")
async def tic_tac_toe(ctx, player_1 = "Alpha", player_2 = "Bravo"):
	
	await ctx.send("Player 1 is " + player_1+ ". Your token is X")
	await ctx.send("Player 2 is " + player_2+ ". Your token is O")
	await ctx.send("Send `exit` to quit the game once the play starts")
	await asyncio.sleep(2)

	play = [['1', '2', '3'], ['4','5','6'], ['7','8','9']]

	async def print(play):
		await ctx.send(embed = discord.Embed(description = "`_"+play[0][0]+"_|_"+play[0][1]+"_|_"+play[0][2]+"_`" + "\n" \
		+ "`_"+play[1][0]+"_|_"+play[1][1]+"_|_"+play[1][2]+"_`" + "\n" \
		+"` "+play[2][0]+" | "+play[2][1]+" | "+play[2][2]+" `"))
	
	await print(play)
	i=0
	def win(play):
		l1 = list(play[0])
		l2 = list(play[1])
		l3 = list(play[2])
		l4 = [play[0][0],play[1][0],play[2][0]]
		l5 = [play[0][1],play[1][1],play[2][1]]
		l6 = [play[0][2],play[1][2],play[2][2]]
		l7 = [play[0][0],play[1][1],play[2][2]]
		l8 = [play[0][2],play[1][1],play[2][0]]

		for l in [l1,l2,l3,l4,l5,l6,l7,l8]:
			if l == ["X", "X", "X"]:
				return 1
			elif l == ["O", "O", "O"]:
				return 2
		return 0

	def check(message):
		return message.content[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or message.content.lower() == "exit"

	while(i<9 and not win(play)):
		await ctx.send("Player {}'s Chance".format(str(i%2 +1)) + ". Go {}".format(player_1 if i%2 == 0 else player_2))
		try:
			message = await bot.wait_for('message', timeout=20.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send("No response, skipped :(")
		except (ValueError, IndexError):
			await ctx.send("Invalid response")
			continue
		else:
			if message.content == "exit":
				await ctx.send("You have chosen to exit the game. Thank you for playing!")
				return
			p1 = int(message.content[0]) -1
			if(play[p1//3][(p1)%3] == "O" or play[p1//3][(p1)%3] == "X"):
				await ctx.send("That position is already occupied, try again!")
				continue
			else:
				play[p1//3][(p1)%3] = "{}".format("X" if i%2 == 0 else "O")
				await ctx.send("Your response is " + message.content[0])
				
		await print(play)
		i+=1
	n = win(play)
	if(n == 0):
		await ctx.send("It's a Draw! Play Again!")
	else:
		await ctx.send("The Winner is Player {}".format(n) + "\n" + "Congratulations {} !!!".format(player_1 if n == 1 else player_2) + "\n" + "🎉🎉🎉🎉🎉🎉")



@bot.event
async def on_message(message):
    if message.author.bot :
        return
	
    if 'scope' in message.content.lower():
        response = "Look, there's very little scope in astronomy, we only have the telescope. Oceanography is a bit better, since they have the bathyscope and the periscope. If you're looking for maximum scope, however, I'd suggest you ditch science and take up medicine instead - they have the endoscope, the microscope, the stethoscope, the laparoscope, the gastroscope, the bronchoscope, the laryngoscope, the urethroscope, the opthalmoscope, and several other scopes!"
        await message.channel.send(response, delete_after = 10)

    if 'happy birthday' in message.content.lower():
        for i in range(3):
            await message.channel.send('Happy Birthday! 🎈🎉')
            i+=1

    if 'good night' in message.content.lower():
        await message.channel.send('Good Night!')
        await message.channel.send('Sleep Tight!')
        await message.channel.send('Sweet Dreams!')
    
    if "%meow" in message.content.lower():
        @commands.has_permissions(manage_messages=True)
        async def delete(message):
        	await message.delete()
    
    if (" love" in message.content.lower()) or (" crush" in message.content.lower()) or ("kadambaby" in message.content.lower()) or (" ship" in message.content.lower()) or (" relationship" in message.content.lower()):
        await message.channel.send("Can I just say....... Awwwwwwwwwww x10")

    if message.content == 'raise-exception':
        raise discord.DiscordException

    if bot.user.mentioned_in(message):
        if message.guild.get_role(int(os.getenv('mod_role'))) in message.author.roles:
            desc = "Heil " + message.author.display_name + " !!"
            await message.reply(embed = discord.Embed(description=desc).set_thumbnail(url="https://media.tenor.com/images/f8e3620dd1f65faa3cfe74de23fd48b9/tenor.gif"))
        else:
            await message.reply("F*cker Don't Ping!!!")
            await message.channel.send(embed = discord.Embed().set_thumbnail(url="https://media.tenor.com/images/f8a02c67648240f3eba5b3fb871e7c37/tenor.gif"))
    
    try:
        msg_count[str(message.author)] += 1
    except KeyError:
        msg_count[str(message.author)] = 1
		
    await bot.process_commands(message)

bday = json.loads(os.getenv('bday'))
date = []
for i in bday.keys():
    date.append(datetime.datetime.strptime(bday[i].strip(), '%m/%d/%Y'))
bd = {list(bday.keys())[i]: date[i] for i in range(len(date))} 
offset = datetime.timedelta(hours=5, minutes=30)
IST = datetime.timezone(offset)

@loop(hours=1)
async def birthday():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(os.getenv('spam')))
    now = datetime.datetime.now(IST)
    now_month = now.month
    now_day = now.day
    
    for i in bd.keys():
        if now_month == bd[i].month and now_day == bd[i].day:
            await channel.send("Happy Birthday " + i + " <@&{}>".format(os.getenv(bday_kid)) + "  🎂 🥂")
            await channel.send(" 🎉 🎊 🥳 🎁 🍕 ")
            pass
        else:
            continue

@bot.command(name="single_tictactoe", aliases=["sttt"], help="Play Tic Tac Toe with Enigma! syntax %sttt name")
async def tic_tac_toe(ctx, name = "Charlie"):
	p = random.choice([1,2])
	await ctx.send("Player 1 is "  "{}".format("Enigma" if p == 1 else name)  + ". Your token is X")
	await ctx.send("Player 2 is " + "{}".format("Enigma" if p == 2 else name) + ". Your token is O")
	await ctx.send("Send `exit` to quit the game once the play starts")
	await asyncio.sleep(2)

	Human = -1
	Enigma = +1
	play = [['1', '2', '3'], ['4','5','6'], ['7','8','9']]

	async def print(play):
		await ctx.send(embed = discord.Embed(description = "`_"+play[0][0]+"_|_"+play[0][1]+"_|_"+play[0][2]+"_`" + "\n" \
		+ "`_"+play[1][0]+"_|_"+play[1][1]+"_|_"+play[1][2]+"_`" + "\n" \
		+"` "+play[2][0]+" | "+play[2][1]+" | "+play[2][2]+" `"))
	
	await print(play)
	i=0

	def win(play):
		l1 = list(play[0])
		l2 = list(play[1])
		l3 = list(play[2])
		l4 = [play[0][0],play[1][0],play[2][0]]
		l5 = [play[0][1],play[1][1],play[2][1]]
		l6 = [play[0][2],play[1][2],play[2][2]]
		l7 = [play[0][0],play[1][1],play[2][2]]
		l8 = [play[0][2],play[1][1],play[2][0]]

		for l in [l1,l2,l3,l4,l5,l6,l7,l8]:
			if l == ["X", "X", "X"]:
				if p == 1:
					return 1
				else:
					return -1
			elif l == ["O", "O", "O"]:
				if p == 2:
					return 1
				else:
					return -1
		return 0

	def empty_cells(play):
		cells = []
		for i in range(3):
			for j in range(3):
				if play[i][j] in  ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
					cells.append([i,j])
		return cells

	def minimax(state, depth, player, p):
		"""
		AI function that choice the best move
		:param state: current state of the board
		:param depth: node index in the tree (0 <= depth <= 9),
		but never nine in this case (see iaturn() function)
		:param player: an human or a computer
		:return: a list with [the best row, best col, best score]
		"""
		if player == Enigma:
			best = [-1, -1, -infinity]
		else:
			best = [-1, -1, +infinity]

		if depth == 0 or win(play) != 0:
			score = win(play)
			return [-1, -1, score]

		for cell in empty_cells(play):
			x, y = cell[0], cell[1]
			n = play[x][y]
			if p == 1:
				play[x][y] = "{}".format("X" if player == 1 else "O")
			else:
				play[x][y] = "{}".format("O" if player == 1 else "X")
			score = minimax(state, depth - 1, -player, p)
			play[x][y] = n
			score[0], score[1] = x, y

			if player == Enigma:
				if score[2] > best[2]:
					best = score  # max value
			else:
				if score[2] < best[2]:
					best = score  # min value

		return best
	
	def ai_turn(p):
		"""
		It calls the minimax function if the depth < 9,
		else it choices a random coordinate.
		:param c_choice: computer's choice X or O
		:param h_choice: human's choice X or O
		:return:
		"""
		depth = len(empty_cells(play))
		if depth == 0 or win(play) != 0:
			return

		if depth == 9:
			x = random.choice([0, 1, 2])
			y = random.choice([0, 1, 2])
		else:
			move = minimax(play, depth, Enigma, p)
			x, y = move[0], move[1]

		if [x,y] in empty_cells(play):
			play[x][y] = "{}".format("X" if p == 1 else "O")

		return (x,y)

	def check(message):
		return message.content[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or message.content.lower() == "exit"

	while(i<9 and not win(play)):

		if(i%2 == p-1):
			await ctx.send("Enigma's Chance")
			X,Y = ai_turn(p)
			n = 3*X + (Y+1)
			await asyncio.sleep(2)
			await ctx.send("Enigma Played " + str(n))

		else :
			await ctx.send("Player {}'s Chance".format(str(i%2 +1)) + ". Go {}".format(name))
			try:
				message = await bot.wait_for('message', timeout=20.0, check=check)
			except asyncio.TimeoutError:
				await ctx.send("No response, skipped :(")
			except ValueError:
				await ctx.send("Invalid response, try again :(")
				continue
			else:
				if message.content == "exit":
					await ctx.send("You have chosen to exit the game. Thank you for playing!")
					return
				p1 = int(message.content[0]) -1
				if(play[p1//3][(p1)%3] == "O" or play[p1//3][(p1)%3] == "X"):
					await ctx.send("That position is already occupied, try again!")
					continue
				else:
					play[p1//3][(p1)%3] = "{}".format("O" if p == 1 else "X")
					await ctx.send("Your response is " + message.content[0])
				
		await print(play)
		await asyncio.sleep(1)
		i+=1
	n = win(play)
	if(n == 0):
		await ctx.send("It's a Draw! Play Again!")
	else:
		await ctx.send("The Winner is {}".format("Enigma" if n == 1 else name) + "\n" + "Congratulations {} !!!".format("Enigma" if n == 1 else name) + "\n" + "🎉🎉🎉🎉🎉🎉")

@bot.event
async def on_command_error(ctx, *args, **kwargs):
    await ctx.send(args[0])

@bot.listen("on_error")
async def on_error(event, *args, **kwargs):
	await bot.get_channel(int(os.getenv("log_channel"))).send(args[0])

@bot.command(name="count", help="Counts the number of messages on the channel. Takes time, so plase use sparsely")
async def count(ctx):
	count = 0
	async with ctx.typing():
		async for message in ctx.history(limit=None):
			count +=1
		await ctx.send(count)


@loop(minutes=5)
async def study():
	ch1 = await bot.fetch_channel(int(os.getenv('senior-spam')))
	ch2 = await bot.fetch_channel(int(os.getenv('spam')))
	ch3 = await bot.fetch_channel(int(os.getenv("bot-spam")))

	channels = 	[ch1, ch2, ch3]
	for name, msg in msg_count.items():
		if msg > 25:
			for channel in channels:
				for message in await channel.history(limit=10).flatten():
					if str(message.author) == name :
						await channel.send("{} You're chatting to0 much, go and study!".format(message.author))
						break
	msg_count.clear()
				
		


birthday.start()
study.start()

bot.run(TOKEN)
