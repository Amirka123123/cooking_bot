import sqlite3

from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN = "6290184537:AAHsxexwzfKz95Y_vSd51KHGIuwE9zlRVoU"

bot = TeleBot(TOKEN, parse_mode="MARKDOWN")

def main_menu(): #первоначальная клавиатура
    search_button = KeyboardButton("Search🔎")
    kitchen_button = KeyboardButton("Foreign kitchens🍜")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(search_button)
    keyboard.add(kitchen_button)

    return keyboard


@bot.message_handler(func=lambda message: message.text == "/start")
def welcome(message):
    reply = "Hi there! This bot will help you to find the ingredients for foreign meals!"
    bot.reply_to(message, reply, reply_markup=main_menu())


bot.infinity_polling()