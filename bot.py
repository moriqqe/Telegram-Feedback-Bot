import logging
import asyncio
import colorlog
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from config import API_TOKEN, CHANNEL_ID
from messages import*

log_colors = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    log_colors=log_colors
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger()

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage, fsm_strategy=FSMStrategy.CHAT)

user_feedback_type = {}

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Feedback on mechanics", callback_data='mechanics')],
        [InlineKeyboardButton(text="Feedback on design", callback_data='design')],
        [InlineKeyboardButton(text="Report a bug", callback_data='bug')]
    ])
    await message.reply(START_MESSAGE, reply_markup=keyboard)
    logger.info("New message...")

@dp.callback_query(lambda c: c.data and c.data in ['mechanics', 'design', 'bug'])
async def handle_feedback_type(callback_query: types.CallbackQuery):
    feedback_type = callback_query.data
    user_id = callback_query.from_user.id
    user_feedback_type[user_id] = feedback_type

    await callback_query.message.answer(FEEDBACK_PROMPTS[feedback_type])
    await callback_query.answer()

@dp.message()
async def handle_feedback(message: types.Message):
    user = message.from_user
    user_id = user.id

    feedback_type = user_feedback_type.get(user_id, 'unknown type')

    feedback = message.text

    feedback_message = (
        f"New feedback from {user.first_name} {user.last_name} (@{user.username}):\n"
        f"Type of feedback: {feedback_type}\n\n"
        f"{feedback}"
    )

    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=feedback_message, parse_mode='HTML')
        await message.reply(FEEDBACK_RECEIVED)
        logger.info(f"Feedback sent: {feedback_message}")
    except Exception as e:
        logger.error(f"Failed to send message to channel: {e}")
        await message.reply(FEEDBACK_ERROR)

async def main():
    logger.info("Bot Starting...")
    await dp.start_polling(bot, skip_updates=True)
    logger.info("Bot stopping...")

if __name__ == '__main__':
    asyncio.run(main())
