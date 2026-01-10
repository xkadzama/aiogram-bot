from aiogram import Router
from aiogram.filters import Command


admin = Router()


@admin.message(Command('panel'))
async def admin_panel(message: Message):
	await message.answer('Добро пожаловать в админ панель!')



