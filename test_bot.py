import os, random
import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler

TAG, SEND = range(2)
def start(bot, update):
    bot.send_photo(chat_id = update.message.chat_id, photo ="https://cataas.com/cat/says/hello" )
    pass

def select_tag(bot, update):
    keyboard = [['cute', 'happy', 'pirate'],
                ['sleep', 'fat', 'halloween'],
                ['loaf', 'wtf', 'facecat']]
    tag = ReplyKeyboardMarkup(keyboard)
    bot.send_message(chat_id = update.message.chat_id, text = "Select tag", reply_markup = tag)
    return TAG

def cat_with_tag(bot, update):
    user_say = update.message.text + '/'
    tag = ReplyKeyboardRemove()
    bot.send_message(chat_id = update.message.chat_id,
                     text = "Nice choice. Do you want to write any message on a photo ?\nIf you don`t want to"
                              "write message yo need to use /skip",
                     reply_markup= tag)
    return SEND

def end(bot, update):
    update.message.reply_text("Thanks user :3")
    return CommandHandler.END

def send_photo_with_tag(bot, update):
    tag = ReplyKeyboardRemove()
    bot.send_photo(chat_id= update.message.chat_id,
                   photo= "https://cataas.com/cat/" + user_say + "says/" + update.message.text)
    return CommandHandler.END

def skip(bot, update):
    tag = ReplyKeyboardRemove()
    bot.send_photo(chat_id = update.message.chat_id, photo= "https://cataas.com/cat/" + user_say)
    return CommandHandler.END

def cat(bot, update, args):
    if len(args) == 0:
        bot.send_photo(chat_id = update.message.chat_id, photo = "https://cataas.com/cat")
    else:
        user_says = " ".join(args)
        bot.send_photo(chat_id=update.message.chat_id, photo="https://cataas.com/cat/says/" + user_says)

def cat_gif(bot, update, args):
    if len(args) == 0:
        bot.send_animation(chat_id = update.message.chat_id, animation="https://cataas.com/cat/gif")
    else:
        bot.send_animation(chat_id = update.message.chat_id, animation = "https://cataas.com/cat/gif/says/" + " ".join(args))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(bot, update):
    url = get_url()
    bot.send_photo(chat_id = update.message.chat_id, photo = url)
    pass

def girlfriend(bot, update):
    girl = ['Собака', 'Няшка', 'Любимая', 'Хозяйка', 'Госпожа', 'Овца', 'Дура', 'Милашка', 'Бегемотик', 'Стерва']
    bot.sendMessage(chat_id=update.message.chat_id, text = girl[random.randint(0, len(girl))])
    pass

def boyfriend(bot, update):
    boy = ['Господин', 'Любовь', 'Защитник', 'Баран', 'Козел', 'Жаным', 'Албасты', 'Кобель', 'Солнышко', 'Любимый']
    bot.sendMessage(chat_id=update.message.chat_id, text=boy[random.randint(0, len(boy))])
    pass

def citation(bot, update):
    Citations = ["Куда один туда и все.\n(c)Нурик", "Махат поху котак бас.\n(с) Эдик",
                 "Вард на 15 секунд,\nА Абыл на час!\n(c) Канат", "Ебать, я телепортируюсь.\n(c) Нурдаудет",
                 "Главное душа.\n(c) Ара", "Свои поймут.\n(c) Нурик", "Я б ее оставил\nПрост по пути было\n(c) Ара"]
    bot.sendMessage(chat_id=update.message.chat_id, text= Citations[random.randint(0, len(Citations))])
    pass

def vanga(bot, update):
    Today=['Сегодня ты бухаешь с Нуриком', 'Сегодня ты чувствуешь себя Арой', 'Сегодня ты дэнсер, как Аза',
           'Сегодня тя отпиздит Нурдик', 'Сегодня ты будешь играть с Кано', 'Сегодня ты спасешь мир с Ану',
           'Сегдня ты будешь спорить с Эдиком']
    bot.sendMessage(chat_id=update.message.chat_id, text= Today[random.randint(0, len(Today))])
    pass


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="unknown stuff.")
    pass

def John(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ВАЧА ВАЧА ВАЧА, JOHN CENA!!!!!!")

def main():
    TOKEN = os.environ['NICKNAME_TOKEN']
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('girlfriend', girlfriend))
    dispatcher.add_handler(CommandHandler('boyfriend', boyfriend))
    dispatcher.add_handler(CommandHandler('john', John))
    dispatcher.add_handler(CommandHandler('today', vanga))
    dispatcher.add_handler(CommandHandler('getdog', dog))
    dispatcher.add_handler(CommandHandler('citata', citation))
    dispatcher.add_handler((CommandHandler('cat', cat, pass_args=True)))
    dispatcher.add_handler((CommandHandler("cat_gif", cat_gif, pass_args=True)))
    conv = ConversationHandler(
        entry_points= [CommandHandler('cat_tag', select_tag)],
        states={
            TAG: [RegexHandler('^(cute|pirate|happy|sleep|fat|halloween|loaf|wtf|facecat)$', cat_with_tag)],
            SEND: [MessageHandler(Filters.text, send_photo_with_tag), CommandHandler('skip', skip)],
        },
        fallbacks= [CommandHandler('cancel', end)]
    )

    dispatcher.add_handler(conv)
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook('https://summerpractice2019.herokuapp.com/' + TOKEN)

    updater.idle()

bot = Bot(token=os.environ['NICKNAME_TOKEN'])
user_say = ""

if __name__ == '__main__':
    main()
