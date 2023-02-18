import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import settings
from ai_services import ask_chatgpt


def get_bot_instance():
    return Bot(settings.BOT_API_KEY)


bot = get_bot_instance()
dp = Dispatcher(bot)


# Communicating in Groups
@dp.message_handler(lambda message: message.text.startswith('/bot'))
async def call_by_command(msg: types.Message):
    print('from group')
    print("msg obj: ", msg)
    # TODO save user to usersdb
    resp_text = ask_chatgpt(msg.text.removeprefix("/bot "))
    await msg.answer(resp_text)


# Communicating in Private
@dp.message_handler()
async def call_by_direct(msg: types.Message):
    print('from private')
    print("msg obj: ", msg)
    # TODO check if user in use>rsdb
    question_text = msg.text
    if msg.reply_to_message:
        question_text = msg.reply_to_message.text + "\n\n" + question_text
    resp_text = ask_chatgpt(msg.text)
    await msg.answer(resp_text)
