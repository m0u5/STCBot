import os

from aiogram import Bot, Dispatcher, executor
from aiogram import types
bot = Bot(token=os.environ['API_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    answer = message.text
    await bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)