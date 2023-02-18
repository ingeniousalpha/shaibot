from aiogram.utils import executor

from main import dp
from schedule import scheduler


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
