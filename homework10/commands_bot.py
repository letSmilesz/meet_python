from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from tg_token import token
from work_lists import add_result, next, previous, like, get_liked

bot = Bot(token)
updater = Updater(token, use_context= True)
dispatcher = updater.dispatcher
base_irl = 'https://www.anekdot.ru/last'
types_of_joke = {'Jokes': '/anekdot/', 'Histories': '/story/', 'Phrases': '/aphorism/', 
    'Rhymes': '/poems/'}
ids = []


def pprint(update, context, message: str) -> None:
    context.bot.send_message(update.effective_chat.id, message)


def start(update, context) -> None:
    pprint(update, context, f'Hi, {update.message.from_user.first_name}!\nI`ll sent you jokes.\n\nWrite ' +
        'command surprize :3')
    main_menu(update, context)


def main_menu(update, context):
    keyboard = [
        [KeyboardButton('Jokes'), KeyboardButton('Histories')],
        [KeyboardButton('Phrases'), KeyboardButton('Rhymes')],
        [KeyboardButton('Liked')]
    ]
    update.message.reply_text('Choose category in menu!', reply_markup=ReplyKeyboardMarkup(keyboard, 
                                resize_keyboard= True, one_time_keyboard = True))


def show_btns(update, context):
    keyboard = [
        [KeyboardButton('Previous'), KeyboardButton('Like'),
         KeyboardButton('Next')],
        [KeyboardButton('Back')]
    ]
    update.message.reply_text('Choose reaction in menu.', reply_markup = ReplyKeyboardMarkup(keyboard, 
        resize_keyboard=True))



def show (update, context, text, new = False):
    if new: show_btns(update, context)
    pprint(update, context, text)


def show_liked(update, context):
    arr = get_liked()
    for i in arr:
        pprint(update, context, i)
    main_menu(update, context)


def line_buttons(update, context):
    text = ''
    query = update.callback_query
    query.answer()
    if query.data == '1': 
        text = previous()
    elif query.data == '2': 
        text = like()
    elif query.data == '3': 
        text = next()
    show(update, context, text)


def surprize(update, context):
    pprint(update, context, 'Happy New Year!')
    main_menu(update, context)


def unknown(update, context) -> None:
    pprint(update, context, 'I don`t know this command')


def message(update, context):
    if update.message.text in types_of_joke: 
        url = base_irl + types_of_joke[update.message.text]
        add_result(url)
        update.message.reply_text('To return to main menu - press button "Back"', reply_markup = 
            ReplyKeyboardMarkup([[KeyboardButton('Back')]], resize_keyboard= True, one_time_keyboard= True))
        show(update, context, next(), True)
    elif update.message.text == 'Back': main_menu(update, context)
    elif update.message.text == 'Liked': show_liked(update, context)
    elif update.message.text == 'Previous': show(update, context, previous())
    elif update.message.text == 'Like': like()
    elif update.message.text == 'Next': show(update, context, next())

dispatcher.add_handler(CallbackQueryHandler(line_buttons))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('main', main_menu))
dispatcher.add_handler(CommandHandler('show', show))
dispatcher.add_handler(CommandHandler('surprize', surprize))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))
dispatcher.add_handler(MessageHandler(Filters.text, message))


updater.start_polling()
updater.idle()