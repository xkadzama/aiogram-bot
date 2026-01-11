from aiogram.middleware import BaseMiddleware


class LogginMiddleware(BaseMiddleware):
	async def __call__(self, handler, event, data):
		await handler()



