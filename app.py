from twitchio.ext import commands
import 


twitchBot = commands.Bot(
    token="nr762m1qu05f4clch97pfse0737v9s", nr762m1qu05f4clch97pfse0737v9s
    nick="isbaozi", # your bot's nick
    prefix="!", # command prefix
    client_id="gp762nuuoqcoxypju8c569th9wz7q5", gp762nuuoqcoxypju8c569th9wz7q5
    initial_channels=["https://www.twitch.tv/moderator/isbaozi", "TwitchAccount2"], # The twitch channels you want the bot working at
)


@twitchBot.command(name="add") # call it at twitch chat with: !add
async def add(ctx): # you can use any function name, doesn't matter
  if len(ctx.message.content.split(" ")) == 3: # !add 1.5 2.5 (for example)
    str1 = ctx.message.content.split(" ")[1]
    str2 = ctx.message.content.split(" ")[2]
    try:
      num1 = float(str1)
      num2 = float(str2)
    except:
      await ctx.send("please enter two numbers")
      return
    result_message = "%f + %f = %f" % (num1, num2, num1 + num2)
    await ctx.send(result_message)


if __name__ == '__main__':
  keep_alive.keep_alive()
  twitchBot.run()
