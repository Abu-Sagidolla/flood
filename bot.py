from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import subprocess as sb
from v import dos,stop


token = '1215967200:AAF13HgSZ_BkaBvXqupMygdvNdxEidDZu98'

bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply('Hello take 1 to UDP, 2 to TCP , 3 to ICMP\n example: <ip> <port> <choice>')

@dp.message_handler()
async def echo_message(msg: types.Message):

    s = msg.text.split(' ')
    if s[2] == '1':
        await bot.send_message(msg.from_user.id, dos(s[0],s[1],'1'))
    elif s[2] == '2':
        await bot.send_message(msg.from_user.id, dos(s[0],s[1],'2'))
    elif s[2] == '3':
        await bot.send_message(msg.from_user.id, dos(s[0],s[1],'3'))
    elif s[0] == 'stop':
        await bot.send_message(msg.from_user.id, stop())
if __name__ == '__main__':
    executor.start_polling(dp)
