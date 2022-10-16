import time
import telebot
import random
import ezappwrite

API_KEY = "API_KEY"
d = 0
bot = telebot.TeleBot(API_KEY)
print("Bot is running!")
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, Welcome, please write /help to see the commands available.")

@bot.message_handler(commands=['help'])
def hello(message):
  bot.send_message(message.chat.id, """Available Commands :-
  /about - This bot helps people to get to know more about the wild west
  /authenticate - Authenticate the user using appwrite 
  /location - It cam update/change your location in appwrite database
  /shop - It will let you shop based on the location, fetching it from appwrite database
  /songs - Randomly play wild west songs fetched from appwrite 
  /fact - Will randomly give wild west facts from appwrite database
  /wwc - It will tell more about wild west countries 
  /hat - It will tell about the cowboy hat
  /culture - It will tell more about cowboys culture with a video
  


**Enter Location before using shop command**
	""")


@bot.message_handler(commands=['about'])
def about(message):
  bot.send_message(message.chat.id, "We made this bot so that we can enjoy food in a different way!")

@bot.message_handler(commands=['wwc'])
def moodfood(message):
  wwc = "The American frontier, also known as the Old West or the Wild West, encompasses the geography, history, folklore, and culture associated with the forward wave of American expansion in mainland North America that began with European colonial settlements in the early 17th century and ended with the admission of the last few western territories as states in 1912."
  wwclink= "https://en.m.wikipedia.org/wiki/File:The_Cow_Boy_1888.jpg"
  bot.send_message(message.chat.id, f"{wwc}\n{wwclink}")
  
@bot.message_handler(commands=['songs'])
def nearme(message):
  x = ezappwrite.getsongs()
  cbs = random.choice(x)
  bot.send_message(message.chat.id, cbs)


@bot.message_handler(commands=['hat'])
def new(message):
  cboy_hat = "The cowboy hat, as we know it, evolved from the original Vaqueros, or Mexican Cowboys, who wore wide brimmed, high crowned sombreros while herding cattle. The cowboy hat was designed to protect working cattlemen as they toiled, all day long, under the hot western sun."
  link = "https://www.stampede.ca/wp-content/uploads/v1-1.jpg"
  bot.send_message(message.chat.id, cboy_hat)
  
@bot.message_handler(commands=['culture'])
def culture(message):
  culture = """American cowboys were drawn from multiple sources. By the late 1860s, following the American Civil War and the expansion of the cattle industry, former soldiers from both the Union and Confederacy came west, seeking work, as did large numbers of restless white men in general.[56] A significant number of African-American freedmen also were drawn to cowboy life, in part because there was not quite as much discrimination in the west as in other areas of American society at the time.[57] A significant number of Mexicans and American Indians already living in the region also worked as cowboys.[58] Later, particularly after 1890, when American policy promoted "assimilation" of Indian people, some Indian boarding schools also taught ranching skills. Today, some Native Americans in the western United States own cattle and small ranches, and many are still employed as cowboys, especially on ranches located near Indian reservations. The "Indian Cowboy" is also part of the rodeo circuit."""
  c_link = "https://youtu.be/Ak6aB5vwdiw"
  bot.send_message(message.chat.id, f"{culture}\n{c_link}")


@bot.message_handler(commands=['fact'])
def about(message):
  fac = ezappwrite.getfacts()
  fact = random.choice(fac)
  bot.send_message(message.chat.id, f"{fact}")

@bot.message_handler(commands=['authenticate'])
def auth(message):
  user = bot.send_message.getuser()
  ezappwrite.authenticate(user)
  bot.send_message(message.chat.id, f"The user {user} is authenticated using appwrite.")

@bot.message_handler(commands=['location'])
def auth(message):
  bot.send_message(message.chat.id, f"Enter you location, it will be saved to your account and you can change it anytime you want")
  location = ezappwrite.getlocation()
  ezappwrite.location_update(location)
  bot.send_message(message.chat.id, f"Location successfully changed to {location}")

@bot.message_handler(commands=['shop'])
def auth(message):
  x = ezappwrite.getlocation(user)
  shop= ezappwrite.getshop(x)
  
  bot.send_message(message.chat.id, f"{shop}")

@bot.message_handler(commands=['exit'])
def exottt(message):
  exit()

bot.polling()
