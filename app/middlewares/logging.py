from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

# ID вашего канала для логов
LOG_CHAT_ID = -1004372855613  # Замените на свой ID

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        # Пересылаем сообщение в лог-канал
        try:
            await event.forward(chat_id=LOG_CHAT_ID)
        except Exception:
            pass  # Игнорируем ошибки пересылки
        
        return await handler(event, data)
