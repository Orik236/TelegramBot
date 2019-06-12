import os, random
import requests
import telegram
from boto3 import session
from telegram import update
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters, InlineQueryHandler

#ACCESS_ID = 'PZRDEXSHSF6V3YZWZ542'
#SECRET_KEY = 'cNaRThVExwqjuDtdMx4EC8LMstLFOAdEYz8vZkrf/M0'

#session = session.Session()
#client = session.client('s3',
 #                       region_name= 'nyc3',
  #                      endpoint_url='https://nyc3.digitaloceanspaces.com',
   #                     aws_access_key_id=ACCESS_ID,
    #                    aws_secret_access_key=SECRET_KEY)

#client.upload_file('bot236.html', 'hello-spaces', 'туц-folder/bot_file.html')

def start(bot, updater):
    contents = requests.get('https://cataas.com/cat/says/hello')
    bot.send_photo(chat_id = update.message.chat_id, photo = contents['utl'])
    pass

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

def kanat(bot, update):
    Kanat = ['Мент', 'Кана', 'Каракурт', 'Котак']
    bot.sendMessage(chat_id=update.message.chat_id, text=Kanat[random.randint(0, len(Kanat))])
    pass

def citation(bot, update):
    Citations = ["Куда один туда и все.\n(c)Нурик", "Махат поху котак бас.\n(с) Эдик",
                 "Вард на 15 секунд,\nА Абыл на час!\n(c) Канат", "Ебать, я телепортируюсь.\n(c) Нурдаудет",
                 "Главное душа.\n(c) Ара", "Свои поймут.\n(c) Нурик"]
    bot.sendMessage(chat_id=update.message.chat_id, text= Citations[random.randint(0, len(Citations))])
    pass

def vanga(bot, update):
    Today=['Сегодня ты бухаешь с Нуриком', 'Сегодня ты чувствуешь себя Арой', 'Сегодня ты дэнсер, как Аза',
           'Сегодня тя отпиздит Нурдик', 'Сегодня ты будешь играть с Кано', 'Сегодня ты спасешь мир с Ану',
           'Сегдня ты будешь спорить с Эдиком']
    bot.sendMessage(chat_id=update.message.chat_id, text= Today[random.randint(0, len(Today))])
    pass

def cancel(bot, updater):
    updater.message.reply_text('GoodByee')

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
    dispatcher.add_handler(CommandHandler('kanat', kanat))
    dispatcher.add_handler(CommandHandler('john', John))
    dispatcher.add_handler(CommandHandler('today', vanga))
    dispatcher.add_handler(CommandHandler('getdog', dog))
    dispatcher.add_handler(CommandHandler('citata', citation))

    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook('https://summerpractice2019.herokuapp.com/' + TOKEN)

    updater.idle()

bot = telegram.Bot(token=os.environ['NICKNAME_TOKEN'])


if __name__ == '__main__':
    main()
