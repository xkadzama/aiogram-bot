from aiogram import Router
from aiogram.filters import Command


payment = Router()


@payment.message(Command('buy'))
async def invoice(message: Message):
	await message.answer('Инвойс на оплату')


