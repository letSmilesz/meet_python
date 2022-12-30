from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from tg_token import token

bot = Bot(token)
updater = Updater(token, use_context = True)
dispatcher = updater.dispatcher

def printt(update, context, message: str):
    context.bot.send_message(update.effective_chat.id, message)


def start(update, context):
    #context.bot.send_message(update.effective_chat.id, 'Hello')
    printt(update, context, 'Hello')


def message(update, context):
    if update.message.text == '1':
        context.bot.send_message(update.effective_chat.id, 'Goodbye')


def help_message(update, context):
    context.bot.send_message(update.effective_chat.id, 'I don`t know this command :(')


def get_day(update, context):
    keyboard =[
        [InlineKeyboardButton('Monday', callback_data = '1'), InlineKeyboardButton('Tuesday', callback_data = '2'), \
        InlineKeyboardButton('Wednesday', callback_data = '3'), InlineKeyboardButton('Thursday', callback_data = '4')], 
        [InlineKeyboardButton('Friday', callback_data = '5'), InlineKeyboardButton('Saturday', callback_data = '6'), \
        InlineKeyboardButton('Sunday', callback_data = '7')]
    ]

    update.message.reply_text('Choose the day!', reply_markup = InlineKeyboardMarkup(keyboard))


def button(update, context):
    querry = update.callback_query
    querry.answer()
    if querry.data == '1': printt(update, context, 'Monday')
    elif querry.data == '2': printt(update, context, 'Tuesday')
    elif querry.data == '3': printt(update, context, 'Wednesday')
    elif querry.data == '4': printt(update, context, 'Thursday')
    elif querry.data == '5': printt(update, context, 'Friday')
    elif querry.data == '6': printt(update, context, 'Saturday')
    elif querry.data == '7': printt(update, context, 'Sunday')


buttons_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start) #первые обязательно команды
get_day_handler = CommandHandler('get_day', get_day)
unknown_handler = MessageHandler(Filters.command, help_message) #после unknown при наличии
message_handler = MessageHandler(Filters.text, message) #и только потом сообщения

dispatcher.add_handler(start_handler)
dispatcher.add_handler(buttons_handler)
dispatcher.add_handler(get_day_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
