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
from PIL import Image, ImageFilter, ImageEnhance
import re
from fuzzywuzzy import process, fuzz

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
apikey = os.getenv("apikey")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='%', intents = intents)

converter = commands.EmojiConverter()

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
	#guild = bot.get_guild(int(os.getenv('ug20_guild')))

	for guild in bot.guilds:
		try:
			for webhook in await guild.webhooks():
				if webhook.name == "The Enigma":
					webhooks[webhook.channel_id] = webhook
		except:
			pass
		try:
			serv_emo[guild] = [em.name for em in guild.emojis]
		except:
			pass
	#print(webhooks)
	#print(serv_emo)
	for em in bot.emojis:
		if em.animated:
			anim_emojis[em.name] = em.id
		else:
			emojis[em.name] = em.id
	await bot.change_presence(activity=activity)
	em_chan = await bot.fetch_channel(int(os.getenv('em-chan')))
	pins = await em_chan.pins()
	for msg in pins:
		if len(msg.attachments) > 0:
			url = msg.attachments[0].url
			fi = requests.get(url)
			f = json.loads(fi.content)
			if msg.attachments[0].filename == "emojis.txt":
				emojis.update(f)
			elif msg.attachments[0].filename == "anim_emojis.txt":
				anim_emojis.update(f)


	print("The Enigma has connected")

#@bot.event
#async def on_member_join(member):
	#channel1 = bot.get_channel(int(os.getenv("unverified")))
	#channel_1 = bot.get_channel(int(os.getenv('spam')))
	#channel_2 = bot.get_channel(int(os.getenv('senior-spam')))
	#channel = await member.create_dm()
	#await channel.send(f'Hi {member.name}, welcome to the server Enigma is a part of. If you have joined IISc UG 20, kindly contact a moderator to verify your identity so that you can view the server. If you have joined IISc UG 19, kindly follow the instructions given there. Hope you have a nice time with The Enigma!')
	#await channel_1.send(f'Hi {member.name}, welcome to IISc UG 20!')
	#await channel_2.send(f'Hi {member.name}, welcome to IISc UG 20!')

#@bot.event
#async def on_member_remove(member):
	#channel1 = bot.get_channel(int(os.getenv("unverified")))
	#channel = await member.create_dm()
	#await channel.send(f'Hi {member.name}, sorry to see you leave :( Hope you will rejoin the server again! Until then, Adios!')
	#await channel_1.send(f'{member.name}, left IISc UG 20!')

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

	def ch(message):
		return message.author == ctx.message.author

	try:
		await ctx.send("Do you wish to add a title? Respond with the `title` or else reply with  `n / N / no / No` to send the rant without a title")
		title = await bot.wait_for('message', timeout=30.0, check=ch)
	except asyncio.TimeoutError:
		await ctx.send("Your message shall be sent without a title")
		title = ""
		pass
	else:
		if title.content in ["n", "no", "No", "NO", "N"]:
			title = ""
		else:
			title = title.content
		await ctx.send(f"Your rant will be titled: {title}")
		pass

	try:
		await ctx.send("Do you wish to remain Anonymous? Respond with y/n")
		msg = await bot.wait_for('message', timeout=30.0, check=ch)
	except asyncio.TimeoutError:
		await ctx.send("Your request has timed out")
	else:
		embed_non_anon = discord.Embed(type = "article", title=title, description = args[:], color=discord.Color.random()).set_author(name=msg.author.display_name, icon_url=msg.author.avatar_url)
		embed_anon = discord.Embed(type = "article",title=title, description = args[:], color=discord.Color.random()).set_author(name="Anonymous", icon_url="https://blog.radware.com/wp-content/uploads/2020/06/anonymous.jpg")
		if(msg.content.lower() == "n"):
			rant = await rant_approval.send(embed = embed_non_anon)
			await ctx.send("Your rant has been sent! This is how your rant will appear to the moderators.")
			await ctx.send(embed = embed_non_anon)

		else:
			rant = await rant_approval.send(embed = embed_anon)
			await ctx.send("Your rant has been sent! This is how your rant will appear to the moderators.")
			await ctx.send(embed = embed_anon)

		try:
			reaction = await bot.wait_for('raw_reaction_add', timeout=10800.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send("Your rant has timed-out. Either a mod has not approved it yet, or your message violates the rules. If it the former, feel free to send again later.")
		else:
			await ctx.send("Your rant has been approved!")
			if(msg.content.lower() == "n"):
				await rants.send(embed = embed_non_anon)
			else:
				await rants.send(embed = embed_anon)

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
	
	#try:
	#	guild = await bot.fetch_guild(message.guild.id)
	#except:
	#	pass
	k = 0
	n = 0
	def repl(match):
		emoji = match.group().replace(";", "").strip()
		#if emoji in serv_emo[message.guild]:
		#	k += 1
		#	return f':{emoji}:'
		#if emoji in list(emojis.keys()):
		#		return f'<:{emoji}:{emojis[emoji]}>'
		#return f'<a:{emoji}:{anim_emojis[emoji]}>'
		em = process.extract(emoji, emojis.keys(), limit=1)
		em_a = process.extract(emoji, anim_emojis.keys(), limit=1)
		#print(em + em_a)
		if max(em[0][1], em_a[0][1]) < 50:
			k += 1
			return f':{emoji}:'
		if em[0][1] >= em_a[0][1] :
			return f'<:{em[0][0]}:{emojis[em[0][0]]}>'
		return f'<a:{em_a[0][0]}:{anim_emojis[em_a[0][0]]}>'

	p = re.compile(r';\S+;')
	try:
		msg, n = p.subn(repl, message.content)
		ref = message.reference
		if ref != None:
			msg_id = ref.message_id
			ref_msg = await message.channel.fetch_message(msg_id)
			em_msg = ref_msg.content + "\n" + f"[Link to Message]({ref_msg.jump_url})"
			embed = discord.Embed(type = "article", description = em_msg, color=discord.Color.random()).set_author(name=ref_msg.author.display_name, icon_url=ref_msg.author.avatar_url)
		
		if(n-k > 0):
			#webhook = await message.channel.create_webhook(name=message.author.display_name)
			webhook = webhooks[message.channel.id]
			try:
				await webhook.send(str(msg), embed=embed, username=message.author.display_name, avatar_url=message.author.avatar_url, allowed_mentions=discord.AllowedMentions(replied_user=True))

			except:
				await webhook.send(str(msg), username=message.author.display_name, avatar_url=message.author.avatar_url, allowed_mentions=discord.AllowedMentions(replied_user=True))
			await message.delete()
			#await webhook.delete()
	except:
		pass
		
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
		try:
			await message.delete()
		except:
			pass
	
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
	
	for i in sw:
		if random.random() >= 0.75 and i.lower() in message.content.lower():
			await message.reply("You kiss your mom with that mouth b*tch!", allowed_mentions=discord.AllowedMentions.none())
			break
	
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
			await channel.send("Happy Birthday " + i + " <@&{}>".format(os.getenv('bdaykid')) + "  🎂 🥂")
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
	try:
		await ctx.send("That did not work as expected. Kindly ensure you are using the command correctly, use %help if you are unsure of the usage. If the issue persists, kindly inform or raise the issue on GitHub, and the issue will be resolved as soon as possible!", delete_after=30)
	except:
		pass
	print(args[:])
	f = open("err.log", "a")
	f.write(str(args[:]) + "\n")
	f.close()
	log = await bot.fetch_channel(os.getenv('log_channel'))
	await log.send(embed=discord.Embed(title="Error", description = str(args[:])))

@bot.listen("on_error")
async def on_error(event, *args, **kwargs):
	await bot.get_channel(int(os.getenv("log_channel"))).send(args[0])

@bot.command(name="count", help="Counts the number of messages on the channel. Takes time, so plase use sparsely")
async def count(ctx):
	count = 0
	f = open("emojis.txt", "a")
	async with ctx.typing():
		async for message in ctx.history(limit=100):
			count +=1
			f.write(message.content + "\n")
		await ctx.send(count)

@bot.command("filter", help="Modifies the Avatar to generate a filtered Image")
async def filter(ctx):
	url = ctx.author.avatar_url
	im = Image.open(requests.get(url, stream=True).raw)
	width, height = im.size
	n = random.random()
	m = random.gauss(1, n)
	for i in range(width): # for every pixel:
		for j in range(height):
			r,g,b = im.getpixel((i,j))
			r = int(r*m) % 255
			g = int(g*m) % 255
			b = int(b*m) % 255
			im.putpixel( (i,j), (r,g,b))
	im = im.filter(ImageFilter.DETAIL)
	im = im.filter(ImageFilter.EDGE_ENHANCE)
	im = im.filter(ImageFilter.SMOOTH)
	im.save("out.jpg")
	await ctx.send(file=discord.File("out.jpg"))

@bot.command("comm", help="Merges the Avatar with the Communist Flag")
async def comm(ctx):
	url = ctx.author.avatar_url
	im = Image.open(requests.get(url, stream=True).raw)
	x, y = im.size
	url2 = 'https://wallpapercave.com/wp/wp25174.jpg'
	img = Image.open(requests.get(url2, stream=True).raw).crop((1250-x//2, 840-y//2 , 1250+x//2 , 840+y//2 ))
	for i in range(0, 2*(x//2), 2): # for every pixel:
		for j in range(0,2*(y//2), 2):
			r,g,b = im.getpixel((i,j))
			img.putpixel( (i,j), (r,g,b))
	img = img.filter(ImageFilter.SMOOTH)
	img = img.filter(ImageFilter.DETAIL)
	sharpness = ImageEnhance.Sharpness(img)
	img = sharpness.enhance(0)
	brightness = ImageEnhance.Brightness(img)
	img = brightness.enhance(1.125)
	img.save("out.png")
	await ctx.send(file=discord.File("out.png"))

@loop(minutes=5)
async def study():
	ch1 = await bot.fetch_channel(int(os.getenv('senior-spam')))
	ch2 = await bot.fetch_channel(int(os.getenv('spam')))
	ch3 = await bot.fetch_channel(int(os.getenv("bot-spam")))
	sug = ["go and study", "take a stroll", "look outside", "take a sip of water", "take a break", "close your eyes and breathe", "stand up and stretch"]
	channels = 	[ch1, ch2, ch3]
	for name, msg in msg_count.items():
		if msg > 25:
			for channel in channels:
				for message in await channel.history(limit=10).flatten():
					if str(message.author) == name :
						await channel.send("{} You're chatting too much, ".format(message.author) + random.choice(sug) + "!")
						break
	msg_count.clear()
				
@bot.command("swear", help="Swear off! Usage: %swear lang, where 1st letter of language is used. Languages available: English, Hindi, Spanish, German, Russian")
async def swear(ctx, lang="e") :
	l = lang.lower()[0]
	if l == 'e':
		await ctx.send(random.choice(sw_e))
	elif l == 'h':
		await ctx.send(random.choice(sw_h))
	elif l == 's':
		await ctx.send(random.choice(sw_s))
	elif l == 'g':
		await ctx.send(random.choice(sw_g))
	elif l == 'r':
		await ctx.send(random.choice(sw_r))
	else:
		await ctx.send("The language is invalid!")
	
sw_e = ["A$$hole", "Motherf*cker", "F*ck off", "D*ckhead", "Son of a B*tch", "Shit", "Bloody Hell", "Dumbass"]
sw_s = ["Puta", "Perra", "Mierda", "Hijo de Puta", "Puta Madre", "Que cabrón", "Joder!", "Gilipollas", "Los cojones!", "La madre que te parió!", "Tonto del culo", "Coño"]
sw_h = ["Bsdk", "Ch*tiya", "BC", "G*ndu", "Maadarch*d", "Saala", "Harami", "Kutta"]
sw_g = ["Huhrensohn", "Scheiße", "Fick dich", "Leck mich am Arsch", "Küss meinen Arsch", "Arschloch", "Verpiss dich!", "Dummkopf"]
sw_r = ["Жопа", "Гавно", "лох", "хуй", "жо́па", "Трахни тебя", "су́кин сын", "муда́к", "ублю́док"]
sw = [" Puta", "Fuck", "Asshole", "Motherfucker", "Fuck off", "Dickhead", "Son of a Bitch", "Bloody Hell", "Dumbass", "Perra", "Mierda", "Hijo de Puta", "Puta Madre", "Que cabrón", "Joder!", "Gilipollas", "Los cojones!", "La madre que te parió!", "Tonto del culo", "Coño","Ch*tiya", "Gandu", "Maadarchod", "Saala ", "Harami", "Kutta","Huhrensohn", "Scheiße", "Fick dich", "Leck mich am Arsch", "Küss meinen Arsch", "Arschloch", "Verpiss dich!", "Dummkopf","Жопа", "Гавно", "лох", "хуй", "жо́па", "Трахни тебя", "су́кин сын", "муда́к", "ублю́док", "cunt", "pussy", "twat", "whore", "slut", "dick", "bhosdike", "Bsdk", "bitch"]

@bot.command("emoji", aliases=["e"], help="Reply with standard and custom emoji. Usage [%e emoji_name] or [%e list] to see all emojis")
async def emoji(ctx, emoji):
	if emoji == "list":
		start = 0
		#webhook = await ctx.channel.create_webhook(name=bot.user.name)
		webhook = webhooks[ctx.channel.id]
		msg = await webhook.send(embed=discord.Embed(title="Available Emojis"),username=bot.user.name, avatar_url=bot.user.avatar_url, wait=True)
		async def send_list(start, end, msg):
			if start < 0 or start > len(emojis.keys()):
				await webhook.send("You have reached the end of the list of emojis")
				return
			elif end > len(emojis.keys()):
				end = len(emojis.keys())
				pass
			ls = ""
			for i in range(start, end):
				em = list(emojis.keys())[i]
				ls += f"{i+1}. `{em}`  :   <:{em}:{emojis[em]}>\n"
			await msg.edit(embed=discord.Embed(title = "Available emojis", description=ls + "\n Send `next` or `prev` to view other emojis"), username=bot.user.name, avatar_url=bot.user.avatar_url)

		def check(message):
			return message.content.lower() in ["next", "prev"] and message.author == ctx.message.author
	
		await send_list(start, start+20, msg)
		while True:
			try:
				message = await bot.wait_for('message', timeout=20.0, check=check)
			except asyncio.TimeoutError:
				await ctx.send("Timeout")
				break
			else:
				if message.content.lower() == "next":
					start+= 20
					await send_list(start, start+20, msg)
				else :
					start -= 20
					await send_list(start, start+20, msg)
				await message.delete()
		return

	em = process.extract(emoji, emojis.keys(), limit=1)
	#print(type(em))	
	#for i in range(len(emojis)):
	#	if emoji in list(emojis.keys()):
	webhook = webhooks[ctx.channel.id]
	await webhook.send(f"<:{em[0][0]}:{emojis[em[0][0]]}>", username=ctx.message.author.display_name, avatar_url=ctx.message.author.avatar_url)
	await ctx.message.delete()
	return
	#await ctx.reply(f":{emoji}:", allowed_mentions=discord.AllowedMentions.none())
	#return


@bot.command("react", aliases=["r"], help="React to a post with custom emoji. Usage %r emoji_name")
async def react(ctx, emoji):
	msg = ctx.message.reference
	message = await ctx.fetch_message(msg.message_id)
	for i in range(len(bot.emojis)):
		#print(fuzz.partial_ratio(emoji, bot.emojis[i].name))
		#print(fuzz.ratio(emoji, bot.emojis[i].name))
		if fuzz.partial_ratio(emoji, bot.emojis[i].name) > 90 or fuzz.ratio(emoji, bot.emojis[i].name) > 90: 
			await message.add_reaction(bot.emojis[i])
			try:
				await ctx.message.delete()
			except:
				pass
			return
	em = process.extract(emoji, emojis.keys(), limit=1)
	em_a = process.extract(emoji, anim_emojis.keys(), limit=1)
	if em_a[0][1] > em[0][1]:
		im = requests.get(f'https://cdn.discordapp.com/emojis/{anim_emojis[em_a[0][0]]}.gif?v=1').content
		emo = await ctx.message.guild.create_custom_emoji(name=em_a[0][0], image=im)
	else:
		im = requests.get(f'https://cdn.discordapp.com/emojis/{emojis[em[0][0]]}.png?v=1').content
		emo = await ctx.message.guild.create_custom_emoji(name=em[0][0], image=im)
	
	await message.add_reaction(emo)
	await emo.delete()
	try:
		await ctx.message.delete()
	except:
		pass
	return

	
	await ctx.reply("Emoji not found", allowed_mentions=discord.AllowedMentions.none())
		
	return

@bot.command("ae", aliases=["anim_emo", "a_emoji"], help="Send animated emojis. Usage [%ae emoji size]. Size argument is optional. Use %ae list to see all available emojis.")
async def animated_emoji(ctx, name, size="m"):

	if name == "list":
		start = 0
		#webhook = await ctx.channel.create_webhook(name=bot.user.name)
		webhook = webhooks[ctx.channel.id]
		msg = await webhook.send(embed=discord.Embed(title="Available Animated Emojis"),username=bot.user.name, avatar_url=bot.user.avatar_url, wait=True)
		async def send_list(start, end, msg):
			if start < 0 or start > len(anim_emojis.keys()):
				await webhook.send("You have reached the end of the list of emojis")
				return
			elif end > len(anim_emojis.keys()):
				end = len(anim_emojis.keys())
				pass
			ls = ""
			for i in range(start, end):
				em = list(anim_emojis.keys())[i]
				ls += f"{i+1}. `{em}`  :  <a:{em}:{anim_emojis[em]}>\n"
			await msg.edit(embed=discord.Embed(title = "Available emojis", description=ls + "\n Send `next` or `prev` to view other emojis"), username=bot.user.name, avatar_url=bot.user.avatar_url)

		def check(message):
			return message.content.lower() in ["next", "prev"] and message.author == ctx.message.author
	
		await send_list(start, start+20, msg)
		while True:
			try:
				message = await bot.wait_for('message', timeout=20.0, check=check)
			except asyncio.TimeoutError:
				await ctx.send("Timeout")
				break
			else:
				if message.content.lower() == "next":
					start+= 20
					await send_list(start, start+20, msg)
				else :
					start -= 20
					await send_list(start, start+20, msg)
				await message.delete()
		return

	sizes = {"s" : 16, "n" : 32, "m" : 64, "l" : 128}
	em = process.extract(name, anim_emojis.keys(), limit=1)
	#print(em)
	message= f"https://cdn.discordapp.com/emojis/{anim_emojis[em[0][0]]}.gif?size={sizes[size.lower()[0]]}"
	#webhook = await ctx.channel.create_webhook(name=ctx.message.author.display_name)
	webhook = webhooks[ctx.channel.id]
	await webhook.send(str(message), username=ctx.message.author.display_name, avatar_url=ctx.message.author.avatar_url)
	await ctx.message.delete()
	#await webhook.delete()
	

@bot.command("add", help = "Add your favourite emojis! Usage : %add emoji1 emoji2 ...")
async def add(ctx, *args):
	p1 = re.compile(":")
	p2 = re.compile("\d+")
	for emoji in args:
		if emoji[1] == 'a':
			anim_emojis[re.findall(r':(.+?):', emoji)[0]] = re.findall(r':(\d+)>', emoji)[0]
		else:
			emojis[re.findall(r':(.+?):', emoji)[0]] = re.findall(r':(\d+)>', emoji)[0]
	em_chan = await bot.fetch_channel(int(os.getenv('em-chan')))
	pins = await em_chan.pins()
	for msg in pins:
		await msg.unpin()
	with open('emojis.txt', 'w') as e:
		e.write(json.dumps(emojis))
	with open('anim_emojis.txt', 'w') as ae:
		ae.write(json.dumps(anim_emojis))
	e_msg = await em_chan.send(file = discord.File("emojis.txt"))
	ae_msg = await em_chan.send(file = discord.File("anim_emojis.txt"))
	await e_msg.pin()
	await ae_msg.pin()

category_data = open("data.json", "r")
categories = json.load(category_data)

HANGMANPICS = ['''
  +---+  
  |   |  
      |  
      |  
      |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
      |  
      |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
  |   |  
      |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
 /|   |  
      |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
 /|\  |  
      |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
 /|\  |  
 /    |  
      |  
=========''', '''
  +---+  
  |   |  
  O   |  
 /|\  |  
 / \  |  
      |  
=========''']

@bot.command("hangman", help="Play a Game of Hangman!")
async def hangman(ctx, category = "normal"):
	if category == "list":
		await ctx.send(", ".join(categories.keys()))
		return

	word_list = categories[category]

	await ctx.send("Welcome to Hangman! All the best! Use the syntax `hm [char]` to send the letter you wish to guess. Only first character after hm will be taken. Note that all non alphabetical characters are removed so The Enigma will be the word theenigma" + f"\n Category {category}")
	await asyncio.sleep(1)

	w = random.choice(word_list)
	word = list(w)
	n = len(word)
	#print(word)
	guess = ["_" for i in range(n)]
	await ctx.send("`" + " ".join(guess) + "`")
	hangman = 0
	def check(message):
		#print(message.content.lower().split()[0])
		return message.content.lower().split()[0] == "hm" or  message.content.lower() == "exit"
	guess_list = []
	while(n>0):
		m=n
		await ctx.send("Guess a letter!")
		#char = str(input("Guess a letter: "))
		try:
			message = await bot.wait_for('message', timeout=60.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send("Timeout! Please send your response faster!")
			break
		else:
			if  message.content.lower() == "exit":
				await ctx.send("Game Exited")
				return
			char = message.content.lower().split()[1][0]
			if char.isalpha() == False:
				await ctx.send("Enter a valid character!")
				continue 
			if char in guess_list:
				await ctx.send("This leter has already been used!")
				continue
			guess_list.append(char)
			for i in range(len(word)):
				if char == word[i]:
					guess[i] = word[i]
					word[i] = "_"
					n-=1
			if m == n:
				hangman += 1
				await ctx.send("`" + "hangman"[:hangman]+ "\n" + HANGMANPICS[hangman-1] + "`")
				if hangman == 7:
					break
			await ctx.send(f"Your character was: **{char}**" + "\n" + "`" + " ".join(guess) + "`")

	if (n==0):
		await ctx.send("Congratulations! You have guessed the answer correctly!")
	else:
		await ctx.send("You ran out of guesses :( Play again!")
	await ctx.send("The Answer was: " + w + "\n" + "Game Over")

webhooks = {}
emojis = {}	
anim_emojis = {}
#emojis = {'yoda': 715232348970680322, 'coyboy': 718035317600288801, 'kalm': 730783379171311647, 'panik': 730783721099231332, 'thonk': 739083300240359466, 'OWO': 744119794567217174, 'bruh': 744123414410690640, 'PogChamp': 750273580813647942, 'jojo': 753282795899715654, 'lul': 765496519259848755, 'kappa': 765496979932577802, 'NotLikeThis': 766203362093432834, 'monkaGIGA': 767005695966838795, 'ayaya': 767077708966395906, 'shockurisu': 767312495589195826, 'happypsak': 767458214177407008, 'judgementalpsak': 767592127064440833, 'bulbaowo': 767600720316596284,'sadcatthumbsup': 775015106538635295, 'feelsbadman': 793541421923303479, 'feelsgoodman': 793541424485892126, 'stabduck': 806774313780903946, 'pepeclown': 821008459616354374, "huh":817257687104094218, 'buffDuo':763137859099426816, 'whenirunoutofnuggies':816536199366836274, 'whAT':765714966874554398, 'WeirdEyes':718720128832766032, 'walms':725122359253794886, 'tyrone':745793530827505725, 'thesimp':735438224369123358, 'kevin':779891743709331487, 'flippedWeirdEyes':773674002518114356, 'FeelsWeirdMan':718719244535201842, 'flippedFeelsHug':773674272249217044, 'FeelsCryingHug':718524236167381053, 'CryIgnore':718524186909343754, 'cryingIgnore':784986468085923871, 'FeelsCryingHugged':718524236465176606, 'pepepunch':789148149063221269, 'pausechamp':725327019881005167, 'painchamp':790562937965510667, 'galaxybrain':790435838659526716, 'blushy':725327017255370844, 'cheesedtomeetyou':755670412469469265, 'cheesedForward':758397721576734732, 'cheesedtomeetyou':755670412469469265, 'musk':817560540435054592, 'perhaps':801682306510880789, 'needahug':756061568273219665, 'GWvertiPeepoUpset':407618665907748876, 'GWvertiPeepoSalute':405951690034905089, 'GWvertiPeepoSadMan':405951684339302400, 'GWsetmyxPeepoSad':405337568901726209, 'peepoFBoy':772744445325213747, 'peepoEarsCat':757109482089087016, 'peepoHostile':756573195036917811, 'peepoWeebOut':755850389542273024, 'peepoWeebIn':755850380558073888, 'NM_ComfyPepe':740601244908781611, 'NM_Kermit':711493390260240414, 'NM_HeHeBoi':754647990404120606, 'NM_PeepoBaked':760871459081027586, 'NM_PeepoCandy':760123294186864670, 'NM_peepoCandle':760234127022227486, 'NM_peepoBusinessMan':761359798494560328, 'NM_peepoBusinessDetective':787401100080054282, 'NM_peepoBusiness':787401099753685044, 'NM_peepoBlushCap':815589193300443146, 'NM_peepoBloodGang':816680188875767858, 'NM_PeepoCookie':760871485370794084, 'NM_PeepoCryTeddy':760163097779372041, 'NM_PeepoCrySip':760123331978199040, 'NM_peepoFrobbaWow':761185966366785547, 'NM_peepoFrobbaWeird':761185979746222090, 'NM_peepoFrobbaHappy':761185962653909003, 'NM_peepoGraduate':770378991239692308, 'NM_peepoGooseLove':817702014644781078, 'NM_peepoPartyConfetti':821788735619334164, 'NM_peepoPhone':788428907439194202, 'NM_peepoPicasso':765909503732350986, 'NM_peepoPillow':766638381777813504, 'NM_peepoPaper':761359798461136927, 'NM_peepoPandaHug':766638433002979328, 'NM_peepoOfficer':762046769831215184, 'NM_peepoObese':770378970037747782, 'NM_peepoNotStonks':765909503656460298, 'NM_peepoNotBad':767039588509548544, 'NM_peepoMafia':766638364341698575, 'NM_peepoMaskSwag':763382793723314176, 'NM_peepoNight':772853894946619432, 'NM_PeepoNike':760234148412784690, 'NM_peepoMadNikeSip':762691257318637619, 'NM_peepoMadFirefighter':762691257004458005, 'NM_peepoMaddPirate':817519064091590706, 'NM_peepoLike':822465700126916698, 'NM_peepoLove2':761186000784588801, 'NM_peepoM16':770379000584339476, 'NM_peepoIndeed':786301150780588083, 'NM_peepoRapperX':761186072578228244, 'NM_peepoPumpkinHug':762563150502821908, 'NM_peepoPopCorn':767039652443586600, 'NM_peepoPoppy':771863878036226058, 'NM_PeepoPrison':760234153131114556, 'NM_PeepoPoliceSwat':760123289573130291, 'NM_peepoPoker':765909503555141633, 'NM_peepoPlease':725481690063175771, 'NM_peepoSimpSign':725024259490971680, 'NM_peepoSantaLove':785942684099018782, 'NM_peepoSipOkay':770378957782384651, 'NM_peepoShark':770359683054567454, 'NM_peepoShrugSmile':789187101547692112, 'NM_peepoSleep':817519064250318868, 'NM_peepoShyhide':761186107710504970, 'NM_peepoSimp':765906134418325515, 'NM_peepoSon':767039566862614529, 'NM_peepoSanta':761185987749347338, 'NM_peepoSadPirate':817519064099979304, 'NM_peepoRules':711493389811449896, 'NM_peepoStarWars':724703553070825622, 'NM_peepoStares':770359616361201704, 'NM_peepoStudy':766638410802528276, 'NM_peepoStop':770359629062078534, 'NM_peepoStonks':765909503383961611, 'NM_PepeSwag':711493389727694859, 'NM_PepePerfect':711935212447334424, 'NM_PepeNani':711146060466225245, 'NM_PepeLaughAtYou':711493389362921503, 'NM_PepeGlasses':718779895672602666, 'NM_PepeGenius':729788071876231231, 'NM_PepeF':718779896008278036, 'NM_PepeFBIPathetic':730561518189674524, 'NM_PepeFedora':729788071591280694, 'NM_PepeFeelsBadMan':740601245315629097, 'NM_PepeFRed':736368979467305021, 'DN_L':817259641271615518, 'deathnote':817261748293599262, 'near_smirk':817262591550291968, 'naw':817259183614328893, 'misacute':817259359720702005, 'Mellonani_':817260460470173716, 'mellodisgust':817260519027113994, 'mello_yell':817264706447343616, 'lightsigh':817257441548304416, 'LightScream':817257378923151401, 'lightlaugh':817257330298322974, 'Lightevil':817257261894205450, 'light_iamkira':817261990560006176, 'Light':817257223231242291, 'L_panic':817264805961924620, 'L_Lawliet':817262794650157078, 'L_confusion':817262837499559958, 'huh':817257687104094218, 'whte_serinityttoughtalk':753152825516752926, 'whte_serinityheartt':801444748094996510, 'whte_serinitybow':801445308093038602, 'w_heart12':801441936045113404, 'v_serinitytaatick':732918538473308170, 'v__pinkstar':805532458757783563, 'v_emoji':805561612894601268, 'v_emoji5':805560529766449182, 'v_emoji4':805560224928104510, 'v_emoji3':805560159328796722, 'lipbiting':816980525654868010, 'Wojak29':729677833810739210, 'Wojak3':729677437436428368, 'Wojak30':729677844577386546, 'Wojak31':729677863355416676, 'Wojak32':729677876642971720, 'Wojak33':729677892388257915, 'Wojak34':729677961115992075, 'Wojak28':729677823224184882, 'Wojak27':729677807738945584, 'Wojak26':729677790969987082, 'Wojak25':729677775300067358, 'Wojak24':729677747869188187, 'Wojak23':729677730182070273, 'Wojak22':729677717766799391, 'Wojak16':729677619687325696, 'Wojak17':729677636997087253, 'Wojak18':729677651995787316, 'Wojak19':729677668127342622, 'Wojak2':729677408302661703, 'Wojak20':729677679892365343, 'Wojak21':729677698477326394, 'Wojak15':729677597860167770, 'Wojak14':729677577572319312, 'Wojak13':729677564066660373, 'Wojak12':729677549713621012, 'Wojak11':729677536212287608, 'Wojak10':729677501416079400, 'Wojak1':729677399846944889, 'Wojak48':729678306743681085, 'Wojak41':729678220219121685, 'Wojak40':729678207149801583, 'Wojak47':729678297562087524, 'Wojak46':729678285847527454, 'Wojak4':729677444553900042, 'Wojak39':729678072420368407, 'Wojak45':729678270865604609, 'Wojak44':729678261461713008, 'Wojak38':729678058503536782, 'Wojak37':729678040342462534, 'Wojak43':729678247478165615, 'Wojak42':729678235348238346, 'Wojak35':729678006200565812, 'pepehype':822496200593768448, 'Wojak6':729677460974731335, 'Wojak49':729678329464225843, 'Wojak5':729677452116361327, 'Wojak50':729678347751391272, 'WojakStare36':729678022269206592, 'Wojak9':729677488791486484, 'Wojak8':729677477286379640, 'Wojak7':729677468998565938, 'rat2':809263620549902348, 'rat':808745667827859487, 'phatcat':803499760723820565, 'ladderchamp':814227808951861309, 'Him':789977768972386304, 'footlettuce':810958369870577715, 'fug_yuo':719381418664263811, 'grab2':803499635603800084, 'grab1':803499635708002324, 'gun':815506761888038974, 'hamter':813123993518342194, 'fatass':814223337613819924, 'cave_rat_2':780482631011008552, 'AAAAA':714464647390167060, 'brfurirkursds':719375404049236018, 'sergio':605830752822886420, 'quackpoggers':730858639669329951, 'pregman':628068883294715904, 'peppa':621084180918435864, 'peepoAmigo':796912814823571456, 'naenae':639312896182059018, 'croccat':646075568156311554, 'alex':626980921156829184, 'yeheboi':786140269648150539, 'wendysip':788078858665852950, 'pepewah':792088506334838805, 'bruhcat':783388854740582410, 'guncat':788475182984593468, 'WhyDidIAddThis':818531605425160222, 'ugh':826450490509492235, 'arcane_wazowskiStares':784000805031378954, 'arcane_ThinkingPepe':784018248479408148, 'arcane_stonks':782922795620892672, 'NM_peepoHappy':740596241796431923, 'fuckoff_rob':777396250378240000, 'peepoHostile':756573195036917811, 'ujoking':739691926319792260, 'squidward':739655191946592266, 'rob_pain':655002371025534987, 'gaysweat':708353542066274314, 'caturi':666830692692525066, 'edwardpout':655001867545214996, 'derpward':739655104663388272, 'bella_angry':655002289823678464, 'alice':812169418049454080, 'breaking_dawn':775216378143703050, 'aro_smile':812165193936535592, 'carlisle':812169418511089704, 'charlie':775219075918987324, 'chevy_truck':812187061493694525, 'chuckesmee_flames':775216378029539358, 'chuckesmee_stuntin':775216378349223977, 'cry_guy':813639571618267136, 'edward_done':812166805505572885, 'edward_annoyed':775216378750697482, 'edward_angry':775216376443830312, 'eclipse':775216378633781249, 'yikes':777396245894529035, 'twilight':775216378763673620, 'this_arrow':775216375324475413, 'santa_rob':784538713581551666, 'rosalie':812169419056218122, 'pensive_cowboy':777396250320044062, 'pusheen_book':777396246171090995, 'really_rob':793978519293263913, 'rob':812166899235815425, 'rob_tracksuit':812166899562971166, 'robinchristmassweater':812166902440525836, 'robinchristmassweaterfull':812166903089987594, 'ohno':816474850545106965, 'new_moon':775216379220721715, 'mike':812169419052154880, 'midnight_sun':775216379325710346, 'fuckoff_rob':777396250378240000, 'golden_onion':775216378835107881, 'hehe_cat':813639570939183154, 'jacob_shirtless':775216378536788008, 'jasper':812169419110744104, 'flightless_bird':775216379560722452, 'esme':812169419257020426, 'emmett':812169418952015872, 'edward_whoa':775216379501477899, 'edward_walking':775219076166320179, 
#'edward_sunglasses':775216379062124604, 'eclipse':775216378633781249, 'edward_annoyed':775216378750697482, 'edward_annoyed':775216378750697482, 'edward_done':812166805505572885, 'NM_peepoHappy':740596241796431923, 'fuckoff_rob':777396250378240000, 'peepoHostile':756573195036917811, 'ujoking':739691926319792260, 'squidward':739655191946592266, 'rob_pain':655002371025534987, 'gaysweat':708353542066274314, 'caturi':666830692692525066, 'edwardpout':655001867545214996, 'derpward':739655104663388272, 'bella_angry':655002289823678464, 'alice':812169418049454080, 'breaking_dawn':775216378143703050, 'aro_smile':812165193936535592, 'carlisle':812169418511089704, 'charlie':775219075918987324, 'chevy_truck':812187061493694525, 'chuckesmee_flames':775216378029539358, 'chuckesmee_stuntin':775216378349223977, 'cry_guy':813639571618267136, 'edward_done':812166805505572885, 'edward_annoyed':775216378750697482, 'edward_angry':775216376443830312, 'eclipse':775216378633781249, 'yikes':777396245894529035, 'twilight':775216378763673620, 'this_arrow':775216375324475413, 'santa_rob':784538713581551666, 'rosalie':812169419056218122, 'pensive_cowboy':777396250320044062, 'pusheen_book':777396246171090995, 'really_rob':793978519293263913, 'rob':812166899235815425, 'rob_tracksuit':812166899562971166, 'robinchristmassweater':812166902440525836, 'robinchristmassweaterfull':812166903089987594, 'ohno':816474850545106965, 'new_moon':775216379220721715, 'mike':812169419052154880, 'midnight_sun':775216379325710346, 'fuckoff_rob':777396250378240000, 'golden_onion':775216378835107881, 'hehe_cat':813639570939183154, 'jacob_shirtless':775216378536788008, 'jasper':812169419110744104, 'flightless_bird':775216379560722452, 'esme':812169419257020426, 'emmett':812169418952015872, 'edward_whoa':775216379501477899, 'edward_walking':775219076166320179, 'edward_sunglasses':775216379062124604, 'eclipse':775216378633781249, 'edward_annoyed':775216378750697482, 'edward_annoyed':775216378750697482, 'edward_done':812166805505572885, 'ye':828784391051804702, 'oh':828784873723396126, 'pepesunglasses':828784282117865472, 'no':828784353269514271, 'king':828784501856534549, 'hu':828784457573204030, 'hehe':828784413507846234, 'grease':828784894200119327, 'gun3':828784479183175702, 'gun2':828784336325050369, 'gun1':828784320168460358, 'facepalm':828784912218718208, 'areyouapproachingme':828784436266926110, 'angy2':828784852391428156, 'angy1':828784748042256416, 'SC_WoodySip':817358521355075614, 'SC_Triple':817358528532316171, 'SC_Think':817358567799521340, 'SC_PepePoggers':817358631372587039, 'SC_PepeOkay':817358649235865602, 'Pepe_think':799441560885657601, 'pepeban':710857775474933810, 'pepearmy':710857775017623574, 'withered':826143842591834173, 'YEP':813604904055996497, 'WokePepe':768124345079693332, 'withered':826143842591834173, 'widepeepoSad':802060425301983242, 'whatthe':768124048919625758, 'uno':768124043995381790, 'tiredcat':782610560779812894, 'sus':821063168767950868, 'sunset_wojak':788771561997336586, 'PepeLaugh':802225173741699143, 'pepeOK':768124344860934205, 'PepeYikes':768124344177131520, 'PogChamp':768124050878496789, 'Poggers':768124044255035403, 'pravega':824577742010843157, 'RicardoSmile':768124046621278239, 'rollsafe':768124047498018817, 'Sadge':785231435187355689, 'PepeKMS':768124345125830714, 'pepejit':803531811182739476, 'pepeJAM':802060446609178658, 'pepehype':768124339857391646, 'PepeHappy':768124344764727317, 'PepeHandsUp':803155553266171904, 'PepeHands':768124346069418001, 'PeepoPing':768124344949407775, 'peepoHeart':823633315293954110, 'monkaGiga':800991208712175637, 'monkaHmm':768124342738485299, 'monkaS':768124343230005259, 'monkaStab':768124343284006922, 'monkaW':802061908780777542, 'MonkaWae':768124343036149801, 'nickipeepo':825773952583729172, 'notSeething':816906384028467201, 'OMEGALUL':802061613175275550, 'MonkaChrist':768124342999318568, 'ez':799320668395012137, 'Copium':819293182998347796, 'madge':824577459555008533, 'KEKW':768124042120134727, 'coom':770898287976906782, 'communistpepe':801379430521241611, 'judgementalpsak':758016174469677166, 'Harold':768124049225678898, 'brainlet':816904558197604383, 'GunPepe':803155530616668222, 'festivepepe':768124342671769611, 'feelsokayman':824577722986266664, 'FeelsBadMan':774353674775429180, 'musk':817560540435054592, 'cheesedtomeetyou':755670412469469265, 'FeelsCryingHugged':718524236465176606, 'NM_Ricardo2':715525376327286825, 'AverageEulaEnjoyer':829173398105096222, 'EulaPingCry':821905247797903360, 'EulAYAYA':821670847709315082, 'EulaYay':832988078968143914, 'EulaYandere':846840070291587102, 'EulaWTF':832988078372421633, 'eulawow':841456145725653033, 'EulaWow':839333326112030760, 'eulawot':841456340283293726, 'EulaWoke':839333559264346112, 'EulaWoah':839262155916574762, 'EulaWink':821600578014412842, 'EulaWheresMyMoney':851317385578151936, 'EulaWhat':822174717536370719, 'EulaWhat':822174717536370719848431340034195456, 'EulaWave':851317697702526996, 'EulaThonk':839333610736975962, 'EulaThrowHands':846837954348712004, 'EulaThumbsDown':822190524408528907, 'EulaThumbsUp':822194301849174016842878627757424660, 'EulaThumbsUp':822194301849174016, 'EulaTissue':843803934640570408, 'EulaToArms':848937999596781629, 'EulaThink':839333844489470014, 'EulaThink':839333844489470014823124158707269642, 'EulaSweat':847540573786079292, 'EulaSunglasses':846841966159462400, 'flusteredeula':839020224157188136, 'sadgeeula':851334556418179084, 'sneezeula':841531658033430564, 'SneezeulaSupremacy':841562976997081098, 'peepoHeart':823633315293954110, 'CapyDiona_Vulpin':810356218882162738, 'boarger':821634752565739580, 'BennettThumbsDown':792310869135720448, 'BennettThumbsDown':792310869135720448, 'BennettSorry_DalasQuil':781266647381442571, 'BennettFine_yazami_plum':781266647356145705, 'BennettAhhh_kaito':831322656954646568, 'BARBARA_THUMBSUP':708170079480578098, 'BarbaraDeleteThis_ieoniq':773429973536997406, 'BarbaraPray_Ikazu401':771007037287039046, 'BeidouDrunk_Soreko':755380370316460033, 'BeidouKek_':773429974484254791, 'BeidouLewd_LagMaster':779284747830165524, 'BeidouPopping_Soreko':755380370572181574, 'BennetSupport_kaito':841899398854344714, 'BARBARA_LOVE':708170069548597248, 'Barbara_Frozen':796068814885355580, 'Baguetteknight2':727468579905208351, 'AmberReeeChibiSayu':729626327560355851, 'AyakaCelebration':673015566201651230, 'arthurfist':727561133149650945, 'angrycatto':592137862691160069, 'AMBER_EXCITED':708170038896754809, 'AMBER_HAPPY':708170070303703201, 'AmberReeeChibiSayu':729626327560355851, 'AmberSobs_weirdorobot':775132994813296660, 'Alert':795762965843410974, 'AlbedoMath_Wilock':799116606168629248, 'Aether_DESPAIR':708170076620324895, 'AcquaintFate':765132887842226186, '1Mora':795762964024131634, 'Help':795762965835546664, 'FreeWei_Kimchi':827794207396986891, 'FallAsleep':795762965923758161, 'Hehe':795762963679674369, 'DvalinKek':751038647276535868, 'Germon':750262922265100298, 'DOTTORE_WHY':708170079539429466, 'GenesisCrystal':765129133390823464, 'DOTTORE_EVILLAUGH':708177094022004836, 'DionaREE_neapurrlitan':775132995044114432, 'GanyuNotLikeThis_MelonbreadFBP':837792195418521641, 'DionaREE_neapurrlitan':775132995044114432, 'DeadSignora':731062289863671889, 'Def':775172800528252958, 'DILUC_COOL':708170074069925928, 'DILUC_COOL':708170074069925928, 'DILUC_SHY':708170080139345991, 'DilucDot_ChibiSayu':729626284493242450, 'DilucElmo_Fuu_chicolette':775905239415914527, 'DionaKono_Mirtan_Sama':781266149026693130, 'DionaPeek_Frostfeuer':804982558961827841, 'DeadPaimon':589276370127814674, 'DeadFischl':710794008993071144, 'DeadAyaka':721977165121585265, 'CrystalChunk':778617667988881408, 'coorooctoocoo':590940664783437838, 'ChongyunNo_Soreko':755380388117086266, 'ChongyunBashful_Soreko':755380388347510865, 'checkpins':766010057040068638, 'ChildeFingerGun_level_hero':775132995010035742, 'ChildeLol_Soreko':755380388934975488, 'ChildeMora_Wilock':780456673122451486, 'ChildeSmugcat_Fuu_chicolette':775905238262612018, 'KleeHug_Milkman':766139105197031435, 'KeqingGasp_yibyeol229':782410848014041108, 'KleeDerp':771104717665075221, 'KeqingDed_MelonbreadFBP':837792195691020338, 'kleecutie':710842482627313696, 'KeqingCelebrate_Frostfeuer':779666461584523274, 'KleeCry_Milkman':766139105276067841, 'KLEE_CRYING':708170080583811093, 'kekqing':785421900624822272, 'KLEE_CRYING':708170080583811093, 'Keknobi':789076905940090930, 'KLEE_CRAZY':708170079623315559, 'Keking':785419658982588416, 'KeqingHeart_Milkman':766139105645035540, 'KekDoggo':743295767262789752, 'Jean_Worried':810946663770357832, 'KAEYA_SMUG':708170059675074570, 'KAEYA_TIRED':708170051450175568, 'KaeyaSip_Tyaren':775132994235138058, 'KatheryneFacePalm':777831826835243039, 'KazuhaWow_WooYoung':850917787723366411, 'kek':732183601252139028, 'JEAN_WHAT':708170054319210547, 'IntertwinedFate':765130388032192552, 'ImStupid':831991477902639104, 'HuTao_Cute':816666890554441778, 'HuTao_Yawn':816666888960606248, 'HuTao_Suspicious':816666890554179614, 'HuTao_Smug':816666891057233930, 'HuTao_Smart':816666890038149180, 'GenesisCrystal':765129133390823464, 'HP':775215740793651220, 'HuTao_Cute':816666890554441778, 'HuTao_Nervous':816666888612085771, 'HuTao_Notes':816666890386538497, 'HuTao_Scary':816666889891348521, 'Nani':731053683625689109, 'Mora':772774919607025665, 'MonaWink':772190941070491678, 'MonaSigh_therues98':781266153304621096, 'MonaOfCulture':776613770226171945, 'MonaOfCulture':776613770226171945, 'MonaCry_Lunsama':775905236271235093, 'MonaCry_Lunsama':775905236271235093, 'LISA_SLEEPING':708170078331338833, 'LisaAraAra_ChibiSayu':729626327619076148, 'LisaShhh_GoBack':781266153116925952, 'Lumine_ANXIOUS':708170081250574377, 'LumineAngery':766171186874023956, 'LumineBlush_Natnatdraw':773429974312419339, 'LumineWat':766172087814979595, 'MadamePingSlipper_4dango_':781266151958773780, 'LISA_BORED':708170070689447988, 'LeaveItToMe':795762965814444053, 'KleePeek_GreenTea':782407867117862952, 'Kleek':803816725900165120, 'KleeOK_GreenTea':782407596778061835, 
#'PaimonDrool_Soreko':817090583100260352, 'PaimonDialogo_Vulpin':826022429993992192, 'PaimonDerp':765420139683774487, 'PaimonDeadInside':757180019742081055, 'PaimonComfy':765422802957238322, 'PaimonClap_Soreko':817090582953328713, 'PaimonChinese':727647583152898139, 'PaimonAngeryWOKE':742224122058375329, 'PaimonAngry_Milkman':766139105268334643, 'PaimonAngry_Soreko':817090581032992840, 'PaimonBaguette':727152827306082354, 'PaimonBurrito':727519491042443344, 'PaimonCalm_Soreko':817090581158428693, 'PaimonCelebrate':588150723116662795, 'PaimonCheer_Soreko':817090583243915304, 'PAIMON_HURT':708170073755615304, 'PAIMON_DEAD':708170044848472105, 'Paimon_ChibiSayu':729626327686316152, 'OuttaMyWay':795762965852192788, 'okden':590922379908087810, 'Oh':795762965265645578, 'OffTopicsmh':834219092633976863, 'NoelleYandere_Sancheck9':782390318725201940, 'NingguangFlirt_Kuurimu':772190940957507584, 'NingguangJudge_fransuushi':773429973368307733, 'NingguangLeisure_Soreko':755380388464951326, 'NingguangPlot_Soreko':755380388410687548, 'NingguangYes_djnommy':775905238435233814, 'NoelleDialogo_Vulpin':825162657488961536, 'NoelleHeh_Erizebett':827983810712698900, 'NoelleWOW_Erizebett':827983811240394772, 'NoelleWOW_Erizebett':827983811240394772, 'PaimonVN':750608439150903347, 'PaimonWAKE':742203843743580161, 'PaimonWave_Soreko':817090583033020477, 'PaimonWhat':710739171798548550, 'PaimonWineParty':727554293862891550, 'PaimonWink':737773212196274347, 'PaimonWoke':723137457855660083, 'PaimonThink':826016328150155325, 'paimontank2':749921486348746872, 'paimontank1vn':750608373040545853, 'paimontank1':749921486533427323, 'PaimonTaco':727499239944618044, 'PaimonStare_Soreko':817090583109566506, 'PaimonSauce':727519586404270081, 'PaimonScared_Soreko':817090580819345449, 'PaimonShock':737438930420629566, 'PaimonSLEEP':742203842732621846, 'PaimonSlep_Meira':812245717652602890, 'PaimonRevolution2':750014324025589840, 'PaimonRevolution1':750014322352062485, 'PaimonReally':725191163161608204, 'PaimonReally':725191163161608204, 'PaimonPlot':588150734030110723, 'PaimonOwO_Milkman':766139105750679582, 'PaimonOuiOui':727554292848001064, 'PaimonJP':742564963087810600, 'PaimonKek':737438929426448385, 'PaimonKnife':588429128932392973, 'PaimonNag_Soreko':817090583297654815, 'RazorBOI_ChatonKun':773429973389672448, 'RAZOR_HUNGRY':708170069703786496, 'RAZOR_ANGRY':708170083263971338, 'RawMeat':778616287345115186, 'Please':795762965830959164, 'PleaseDont':795762965240217601, 'Primogem':765129529802752040, 'puga':755075085374717953, 'QiqiMad_Milkman':766139105678589972, 'piemon_Nociii':820841400697749585, 'Paingon3':727554293644656710, 'Paingon2':727554292222787675, 'Paingon1':727554287479160863, 'PaimonWow_Soreko':817090581293170748, 'XianglingReckless_Soreko':755380388322476113, 'XianglingExcited_Soreko':755380388456824882, 'XianglingDrool_Milkman':766139105804943371, 'WellDone':795762965600796744, 'VisionPyro':725178213944262716, 'VisionHydro':725173420190597184, 'VisionGeo':725174020831444994, 'VisionElectro':725173420148654170, 'VENTI_SCARED':708170080290209842, 'VENTI_WONDERING':708170076607479868, 'VentiFrench':727555713475543071, 'VentiKermitSip_Fuu_chicolette':775905237512224769, 'VisionAnemo':725173419133370390, 'VisionCryo':725173419456462855, 'VisionDendro':725173419909316702, 'UID':773587748527276033, 'TooEasy':795762965491089410, 'TimmieSurprised_HM_Hmongt':775905235624394792, 'TimeToEat':795762965122908181, 'Surprised':795762965764112385, 'SucroseGlasses_yuduki_nh':781266154218979368, 'Resin':765128125301915658, 'ResinBible':782769234886787074, 'RosariaDed_MelonbreadFBP':829069222515703858, 'RosariaDisgust_MelonbreadFBP':837792195079307314, 'RosariaPout_Dong':835961127925317642, 'sadcat':592137883318747146, 'ScaramoucheDisgusted_kremnk':779288474321682432, 'ShipOut':795762965579300886, 'ZhongliWhat_Soreko':755380388972593212, 'ZhongliUh_MugsDraw':772190941465280542, 'ZhongliTooCool_MomoTaro':772190941180067890, 'ZhongliConfetti_Wilock':780456672668942356, 'YoureFunny':795762966002663445, 'YanfeiWink_drunqyaa':833566546177687562, 'XinyanWave_SUKYARU_':782411030130589726, 'XingqiuWave_SUKYARU_':781266153888022558, 'XingqiuSing_Soreko':817128739569401887, 'XingqiuFlair_Soreko':755380388091789333, 'XingqiuDoya_Soreko':755380388268081173, 'XiaoMasked_Soreko':755380370605736017, 'XiaoDelicious_Soreko':755380365451067462, 'XiaoCheems':809564593541611640, 'Xiao_AlmondTofu':816662857844392038, 'Xiao_Annoyed':816661653948858388, 'Xiao_Apathetic':816661653810053160, 'Xiao_Brood':816661653865234522, 'Xiao_Fight':816661653114060811, 'Xiao_Food':816661652652163113, 'Xiao_Meditate':816661652531052605, 'Xiao_Sleepy':816661652786774026, 'wither':849840848837410816, 'tuff_block':839540344601444373, 'steve_uwu':840245307736457268, 'steve_thinking':425381858121875459, 'steve_thumbsup':651847833699352578, 'steve_dabbing':425370892181176331, 'shocked_ghast':425377592024104960, 'snow_golem':735237008099639306, 'pinged_villager':427072148671168533, 'pinged_creeper':425374026903584779, 'ocelot':735230446086127677, 'pikachu':316976817044979712, 'mojang_old':628987335823982592, 'mojang':836472371719569458, 'mc_zombie':302439627992858624, 'mc_wolf':304704745065414666, 'mc_skeleton':302439512544509952, 'mc_sheep':302439127322722314, 'mc_pig':302439003012202496, 'microsoft':781921132591972402, 'mc_fox_sleeping':560328871887503400, 'mc_fox':594204020789477376, 'mc_heart':589630433243955205, 'mc_earth':589630396476555264, 'mc_discord':589630502588383241, 'mc_cow':302439066828406784, 'guardian':631748221424893963, 'ghast':302439828463550464, 'diamond_shovel':631758299368521749, 'diamond_pickaxe':309458671925198848, 'diamond_sword':309458615041916928, 'diamond_hoe':631758299691352074, 'diamond_axe':631758299649540097, 'diamond':591783543663886352, 'creeper':425369771026939914, 'axolotl':762311262120968202, 'alex':302438846283644930, '10_years':578822331766538240, 'angry_panda':585712635832565763, 'bucket_of_axolotl':763424254276272218, 'MumboIRL':648478973256531999, 'CH_PepeLoveKing':704999413222998056}
#anim_emojis = {"a_yes":748779850659266630, "shakey":621168721175642112, "nyanangel":725038441376776314, "vibing_cat":748408503554801704, "pika_swag":746914132984332360, "danceHYPERS":768535164368191498, "InceptionPoggers":694522612147027978, "WTF":765897190291669022, "PepeAngery":718773506304770138, "PeepoChad":760871481151455272, "catrub":801844749627031562, "Flame":816495742701142046, "anicatvibe":774225574088540171, "Dancing_roach":820323770577322005, "catcry":821221157381472297, "dissapear":678977454701805569, "Awkward_black_boi":78977451874844673, "doge_cool":745293885248372878, "a_heart":738951305875423293, "squirtle_cool":733095409630707844, "Cat_O":767392039620837437, "purple_flame":721442248239218688, "MEOW":746222520335859794, "pepe_happi":743832183483006987, "surprised_pika":739569073209213079, "pepesimp":738615019251695686, "pepebye":743368395306827858, "pepelaugh":747003391200329748, "pika_pika":746364811662721114, "wob":740086538951721052, "petthepeepo":790562587318288394, "he":821983689264463872, "bonejazz":822080091357184061, "feelsShirtRip":757165596868870235, "feelsColorcry":757314091684462693, "peepoBedJump":762070836772864000, "peepoCryJam":510005361986633731, "peepoCryBoombox":756569845767733289, "peepoClowndance":755698588503244860, "peepoClownballs":756071944826388522, "peepoClownIT":771893069846675467, "peepoCirclespin":757106547573653506, "peepoFormal":756228644128686290, "peepoFidget":763565107367510037, "peepoFlute":756057895547699241, "peepoFlowerpetals":767167040670269450, "peepoEatpopcorn":755852558328791040, "peepoHammer":756057754636124181, "peepoHonkbutt":757358697033760918, "peepoSadder":401941974304948224, "peepoTorch":755692129564622858, "NM_AngryBlob":725481689865781259, "NM_Cough":750003134151262238, "NM_DoggyDance":725694366839996436, "NM_DogDanceRGB":749585236400275526, "NM_DogDance":756238524386377820, "NM_DanceVibe":722824037293883422, "NM_CrabRave":724703097963675658, "NM_CoolDoge":729785801449406635, "NM_DuckDrunk":729785802321821818, "NM_Driving":750003769663553608, "NM_ExcuseMe":729785802275684402, "NM_GunPoint":756238524839231659, "NM_HardDance":766371288008491020, "NM_PeepoBalloons":760123299488858122, "NM_PeepoChad":760871481151455272, "NM_peepoBlush":765836527636054016, "NM_peepoBike":760460065722990632, "NM_peepoChocolates":770359692295405629, "NM_PeepoCryDrink":760460036115398656, "NM_PeepoHammer":760123374667563008, "NM_peepoGoose":755888128178520196, "NM_PeepoGuitar":760460078595178516, "NM_peepoParty":772853813757476874, "NM_peepoPizza":711512497957371904, "NM_peepoNopers":761364872897495081, "NM_peepoMarioYoshi":817519065475842058, "NM_peepoMoney":817702278109593600, "NM_peepoNerd":761186068661796885, "NM_peepoMadPing":762691259034763315, "NM_peepoMadJam":762691257427558402, "NM_peepoMadHatcopter":762691257200803840, "NM_peepoMadBed":762691257746325504, "NM_PeepoLaugh":755888128262406235, "NM_peepoLeaves":730798799286566943, "NM_peepoILY":740596242010341446, "NM_peepoHeadLove":731267735652139029, "NM_peepoIdk":729785800115355688, "NM_peepoRideKangaroo":770359658640310312, "NM_peepoReindeer":770359672485183518, "NM_peepoReindeer":770359672485183518, "NM_peepoRedAlarm":770359654370115594, "NM_peepoQuickDab":729785800308555867, "NM_peepoPopcorn":730852127257133201, "NM_peepoPoliceDog":817519064624791602, "NM_peepoPokiSimp":725861852076048445, "NM_peepoPlane":772853972246855690, "NM_peepoPizza":730852127408128010, "NM_peepoScared":822465973243215902, "NM_PeepoSip":755888128224657550, "NM_peepoSmash":799022610196856832, "NM_peepoSmoke":711493389664780339, "NM_peepoSalut":730919534772617221, "NM_peepoSadSwing":822466323203883068, "NM_peepoRudolphCookie":785941644792954880, "NM_peepoRocket":761186128664854568, "NM_peepoWine":761353851726069761, "NM_peepoWeight":817519064649039902, "NM_peepoUwU":765836527674458112, "NM_peepoToilet":761186111682117652, "NM_PeepoSwing":760122883909091369, "NM_peepoSpy":761186115876552744, "NM_PeepoSpin":760460082475040789, "NM_peepoSTRONG":770359634039930890, "NM_peepoSparkler":771863877859672104, "NM_peepoSoup":761186133270593536, "NM_PepoChonk":719287092504690700, "NM_PepeWow2":729785802229415988, "NM_PepeWow1":729785801310863433, "NM_PepeThinkOmega":729788071331102742, "NM_PepeSad2":712297969952751727, "NM_PepeSad":712297970506399844, "NM_PepeRideGoose":759040029724639252, "NM_PepeRaiseKnife":725024261168693561, "NM_PepeOhWait":725024260334157884, "NM_PepeNoU":729785800757215343, "NM_PepeHyped":711493389807255623, "NM_PepeHeadset":718368240253796393, "NM_PepeHacker":723885242972373094, "NM_PepeGun":724733130589732944, "NM_PepeFuckYou":756238524466069566, "NM_PepeFeelsCuddleMan":766638360621219840, "NM_PepeFeelsWeirdMan":727317917481435197, "NM_SonicGottaGoFast":813591337811050506, "NM_worryNani":782661438564597801, "NM_WTF":765897190291669022, "1awtf":801441053110566932, "1aruns":801441635891675166, "1pickle":801444086728622090, "near_pat":817261427957825558, "lightwritesnames":817259734901719062, "matsuda_pat":817261840618356756, "light_pat":817261879688691742, "L_pat":817262638899396679, "L_lick":817261921836859402, "L_Light":817264777424142357, "q_serinitypetcatduck":795330381988757574, "whte_serinitytzgayangry":795329404338438144, "whte_serinitytaexplain":753967226490716242, "whte_serinityt1gjkheart":769935670587293736, "whte_serinityecinnflly":753966672133750906, "whte_serinityeckeetoplay":753967598562967719, "whte_serinityecheartcakew":732919787080122390, "whte_serinityecebutterfl":732289303572512840, "whte_serinityeceheart":770815753556459521, "whte_serinityecCATHELP":732274212714315871, "whte_serinityeccatloveu":732920511771836508, "white_hearts":794668122191691787, "v_serinitytaaverify":732920962839740436, "v_serinityecmilkcart":732281855931318404, "v_serinityecheartcake":732919821968343091, "v_serinityecfloatribbon":732275595739660288, "v_serinityecbunnywelc":732817430677815316, "v_serinityeckat":732919324364505096, "v_serinityeccinnamonroll":754056890312425493, "v_serinityecebutterfly":769993023886065694, "u_serinityecwbc":732919359273435156, "u_serinityechamroll":735647947257282630, "u_serinityecpant":732920265381511219, "s_serinitytah2":770996781655261185, "s_serinityecwbc":732919243427020830, "t_serinityecbee":770817292153913366, "s_serinityecmilk":770997039060090910, "s_serinityeccinnamon":754056616839479336, "s_serinityecb_blueverify":800917092282793984, "s_serinityecb_exclamation1":772510503904739428, "s_serinityecb_sheeplove":772510255132966963, "s_serinityecb_sheeproll":772510232726339645, "s_serinityeccinna":754056760314036355, "femcel":786074058059415553, "porrij":731740921263030312, "reddit":777953431402446850, "schizoincelwojak":802755619919757343, "soyjak":802755014157795358, "soyjakshooketh":802755124094304306, "soyjakshooketh1":802755172001382440, "fatty":786074171678785537, "DoomerGirlGIF":730103754267033700, "DoomerGIF":730103745798471701, "DoomerCoupleGIF":730104130282192967, "coomerjumpy":802751215997550624, "coomer":802754125590822933, "BrainletGIF":729712965690982431, "BigBrainStill2":729712434318934098, "BigBrainGIF":729712424655257671, "Wojak60":729691848154808361, "Wojak59":729691523930652703, "Wojak58":729689600544473170, "Wojak57":729689591141105695, "Wojak56":729689580764397708, "Wojak55":729689555292258335, "Wojak51":729689503199133736, "Wojak52":729689534224269423, "Wojak53":729689541518295130, "Wojak54":729689547834654740, "WojakSadGIF":729712395575885985, "wojakcry":784595647395266591, "WojakCloseup2":729712370854920262, "WojakCloseup":729712359198687333, "wojakbruh":803028766137647156, "Wojak75":729700063005245533729700053857337465, "Wojak75":729700063005245533, "Wojak77":729700080705077358729700071721140295, "Wojak77":729700080705077358, "Wojak78":729708762574880810, "Wojak79":729708779041587213, "Wojak73":729700036543381666, "Wojak73":729700036543381666729700044441387069, "Wojak71":729700027705852007, "Wojak70":729691980077989909, "Wojak69":729691966601822218, "Wojak68":729691956845871147, "Wojak61":729691856702537729, "Wojak62":729691865581879326, "Wojak63":729691872951271495, "Wojak64":729691880287240193, "Wojak65":729691888529047592, "Wojak66":729691898092060744, "Wojak67":729691910033244292, "ratshake":820393350405292052, "kiwi_spin":820323770920206346, "hyperclap":794420408563662869, "poultry_strut":819766278079774762, "run":819766278046351370, "roach":820323770577322005, "comb":820393351379419183, "bear":819451151506079756, "yeahhhh":819766277849481237, "yeah":819469354080010250, "EuKFCDoge":621712915380305927, "carrotfish":651599662913945612, "baby":565030228229881856, "wahh":793869152154026015, "aro_happy":812178224129376277, "angela_omg":812199042053308426, "bella_possibility":812178270308925461, "bella_lochness":812181738167861258, "bella_dude":816472687639003166, "aro_smirk":812172966431293492, "charlie_rollingeyes":812185266227773440, "edward_smile":812178302487625739, "edward_shakeshead":816474580335722536, "cursed_resume":812188879683715113, "wolf_jacob":812192771104178176, "seth":812196071035502623, "mike_youregood":812193497925812245, "laurent_stare":814732131426893834, "jessica_funny":812193667599171614, "hello_emmett":814336792873926697, "its_time":812174459993063437, "excuse_me":777396250676428800, "cursed_resume":812188879683715113, "edward_shakeshead":816474580335722536, "edward_smile":812178302487625739, "aro_happy":812178224129376277, "angela_omg":812199042053308426, "bella_possibility":812178270308925461, "bella_lochness":812181738167861258, "bella_dude":816472687639003166, "aro_smirk":812172966431293492, "charlie_rollingeyes":812185266227773440, "edward_smile":812178302487625739, "edward_shakeshead":816474580335722536, "cursed_resume":812188879683715113, "wolf_jacob":812192771104178176, "seth":812196071035502623, "mike_youregood":812193497925812245, "laurent_stare":814732131426893834, "jessica_funny":812193667599171614, "hello_emmett":814336792873926697, "its_time":812174459993063437, "excuse_me":777396250676428800, "cursed_resume":812188879683715113, 
#"edward_shakeshead":816474580335722536, "edward_smile":812178302487625739, "peepoFormal":756228644128686290, "peepoFormal":756228644128686290, "NM_RicardoDance":727229019539636344, "Eulayay":832643711719440434, "EulaWinking":821608150934749195, "EulaTrailerPat":846840244648935494, "EulaSTEER":850520801912291390, "PetTheGanyu":797215709738303588, "catcry":807992803933290526, "BowingPandas":740129794586312744, "AmberRun":782407597407731763, "AmberDollDance":732057425342889994, "AmberRun":782407597407731763, "AmberSweat":782407598015250472, "amberwhat":587635066763739138, "ganyuhide_seseren":792276549810389022, "hellotickie":727746130909200476, "hellmage_emilyyeh":833496986657357824, "GanyuSleepy_Shirayuki":831131212507643936, "childespank_seseren":792276549147688980, "CatRave":757815726013677664, "childeeat_wilock":778925588320747541, "childehehe_Shirayuki":807141560646631444, "KEK":740160662721921104, "hilichurlbullied":792278521338003487, "hilichurlburning":792278522168475648, "KleeREEE":816883329583808612, "KleePlane":768128642638413847, "KleeKaboom":775742235433500682, "PaimonCookies":740300330490921042, "PaimonWave":755788648661647401, "PaimonTriggerredPing":737438932077117490, "PaimonTankWoke":749943602116952076, "paimonroadrage_seseren":792278520604393482, "PaimonSpinner":742223819636473886, "PaimonStare_seseren":792310821719769098, "PaimonPeek":728206370587017326, "PaimonKill":813188812850724874, "PaimonLove":740248885972304013, "PaimonNom":758793351180058665, "PaimonNOMMING":732171884095078420, "QiqiWink":816199884717031424, "qiqithink_seseren":792276550066241536, "qiqisnooze":721977235568984195, "QiqiSip":784121845564571669, "qiqicoconut_seseren":792276547268116512, "QiqiCry":816418544551198774, "QiqiShoot":816199908355866654, "PetThepuga":792646628099096577, "PETTHEPAIMON":758891074562555924, "PetTheGanyu":797215709738303588, "ventibullied_seseren":792276547067314196, "SucroseLove_k3lly":781667913391538226, "sissypuffs":723451063608279081, "zhonglicool_seseren":792276549315198976, "YallOfftopic":834190313571876884, "tnt_boom":588955096461606912, "strider_walk":737913909696266331, "party_potato":425383253076082701, "piglin_dance":724981924820418610, "mining_jump":587505485163397120, "minecraft_bounce":587505418406723584, "mc_dolphin":661625087367184394, "creeper_boom":591991936236126210, "dabbing_totem":532984294633766922, "burning_skeleton":589924857639338028, "precious":711797070284980281}
serv_emo = {}
birthday.start()
study.start()

bot.run(TOKEN)