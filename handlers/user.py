from aiogram import Router
from aiogram.filters import CommandStart


user = Router()


@user.message(CommandStart())
async def start(message: Message):
	await message.answer('Hello!')


@user.message(Command('info'))
async def info(message: Message):
	await message.answer('Информация о боте:')


@user.message(Command('rules'))
async def rules(message: Message):
	await message.answer('Правило пользования ботом:')
