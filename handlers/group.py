from aiogram import Router
from aiogram.filters import CommandStart


group = Router()


@group.message(Command('start_game'))
async def game(message: Message):
	await message.answer('Игра началась!')