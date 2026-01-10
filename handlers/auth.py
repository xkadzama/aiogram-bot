from aiogram import Router
from aiogram.filters import Command


auth = Router()


@auth.message(Command('register'))
async def register(message: Message):
	await message.answer('Регистрация')


