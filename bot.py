from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from predict import predict
import os
import pandas as pd


TOKEN = '6398934586:AAGcIvejNTvt_apa0zt7kKBdKG3Bnezk628'
BOT_USERNAME = 'group_spam_detector_bot'
SPAM_LEARNING_GROUP_ID  = -4198965690
HAM_LEARNING_GROUP_ID = -4191259453


async def on_start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Nice to meet you! I am a spam detector bot. Click /start to see this again. \nClick /help to know more about me.')

async def on_help(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
I am a spam detector bot. Add me as an admin to your group so that I can help you detect spam messages.
When I detect spam messages, I reply with "Spam Message Detected!". You can easily find these messages and delete them.
''')


def reply(message:str)->str:
    if predict(message):
        return 'Spam Message Detected!'
    else:
        return 'This is not a spam message.'

def reply_learn(is_spam, message:str)->str:
    message  = "".join(message.split('"'))
    message  = "".join(message.split(','))
    message  = "".join(message.split('/'))

    dir_path = os.path.dirname(os.path.realpath(__file__))
    if is_spam:
        file_path = os.path.join(dir_path, "data","original-data","spam_collected.csv")
        with open(file_path, "a") as file:
            file.write(f'"{message}",1\n')
    else:
        file_path = os.path.join(dir_path, "data", "original-data","ham_collected.csv")
        with open(file_path, "a") as file:
            file.write(f'"{message}",0\n')

    return 'Message learned!'
    



async def on_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type

    text = update.message.text
    if text is None: text = update.message.caption

    if text is None:
        print('update.message is ',update.message)
        await update.message.reply_text('I cannot process this type of message')
        return

    chat_id = update.message.chat.id
    print(f'Group Id: {chat_id}')

    if chat_id == SPAM_LEARNING_GROUP_ID:
        print('Learning Spam')
        reply_learn(True, text)
        await update.message.reply_text(reply_learn(False, text))
        return
    elif chat_id == HAM_LEARNING_GROUP_ID:
        print('Learning Ham')
        await update.message.reply_text(reply_learn(False, text))
        return

    if message_type == 'private':
        res_text = reply(text) 
    else:
        res_text = reply(text)  

    print(f'got message: {text}, responding with: {res_text} ')
    await update.message.reply_text(res_text)
    
async def on_error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text(f'Oops, something went wrong: {context.error}')

def main():
    print('starting...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', on_start))
    app.add_handler(CommandHandler('help', on_help))

    #Messages
    app.add_handler(MessageHandler(filters.ALL, on_message))

    #Errors
    app.add_error_handler(on_error)

    print('polling...')
    app.run_polling(poll_interval=2)

main()
