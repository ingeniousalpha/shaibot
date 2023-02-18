from random import choice
from ai_services import ask_chatgpt
from main import get_bot_instance

DAILY_REQUESTS = [
    "Tell me a quote of some great person",
    "скажи какую нибудь цитату великих людей"
]


async def daily_task():
    bot = get_bot_instance()
    question = choice(DAILY_REQUESTS)
    answer = ask_chatgpt(question)
    await bot.send_message(chat_id=-770248259, text=answer)
    session = await bot.get_session()
    await session.close()
