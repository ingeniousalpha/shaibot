from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services import daily_task
from main import bot

scheduler = AsyncIOScheduler(timezone="Asia/Almaty")
scheduler.add_job(
    daily_task,
    trigger='cron',
    hour=9,
    minute=0,
    start_date=datetime.now()
)
