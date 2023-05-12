import os
from db import database
from aiogram import Bot, Dispatcher, executor
from aiogram import types


bot = Bot(token='6179981662:AAEIWWPNE0cx4rt8FD8r2T5Tg5B7fzCnA1g')
dp = Dispatcher(bot)
secret_phrase = 'kek'


def get_all_users():
    result = ''
    users = database.Users
    for user in users.find():
        result += f'user id: {user["id"]}, first visit: {user["firstVisit"]}, last visit: {user["lastVisit"]}\n'
    return result


def update_last_visit(date, id):
    database.Users.update_one({'id': id}, {'$set': {'lastVisit': date}})


def add_user(user_id, date):
    users = database.Users
    user = {
        'id': user_id,
        'firstVisit': date,
        'lastVisit': date,
    }
    users.insert_one(user)


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    user_id = message.from_user.id
    date = message.date
    add_user(user_id, date)


@dp.message_handler()
async def on_message_recieve(message: types.Message):
    if message.text == secret_phrase:
        all_users = get_all_users()
        await bot.send_message(message.chat.id, all_users)
    update_last_visit(message.date, message.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)