from aiogram import Router
from aiogram.filters import Command


admin = Router()


@admin.message(Command('panel'))
async def admin_panel(message: Message):
	await message.answer('Добро пожаловать в админ панель!')

@admin.message(Command('ban'))
async def ban_user(message: Message):
	await message.answer('Пользователь заблокирован!')


# git init - инициализация локального репозитория
# git status - проверить не изменены ли файлы или нет ли новых
# git add . - добавить измененные файлы в индекс
# git
