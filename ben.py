import random
import lightbulb

answers = [
    "https://cdn.discordapp.com/attachments/941414137978843176/952669091401977916/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669156128464937/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669195517194280/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669279357128704/ben.mp4"
]

bot = lightbulb.BotApp(prefix="ben ", token="", default_enabled_guilds=12345)

@bot.command
@lightbulb.option("question", "question")
@lightbulb.command("ask", "ask ben a question")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    question = ctx.options.question
    randomize = random.choice(answers)
    await ctx.respond('Question: ' + question + '\n' + randomize)

bot.run()
