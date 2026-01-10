from aiogram import Router
from aiogram.filters import CommandStart


user = Router()


@user.message(CommandStart())
async def start(message: Message):
	await message.answer('Hello!')