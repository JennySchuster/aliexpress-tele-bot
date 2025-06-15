import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from config import BotConfig

cfg = BotConfig(".env.full")
TOKEN = cfg["TELEGRAM_BOT_TOKEN"]
bot = Bot(token=TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

# Dummy search function using local dummy results
def search_aliexpress(query):
    return [
        {"title": f"{query} - Example Product 1", "price": "$9.99", "link": "https://aliexpress.com/item1"},
        {"title": f"{query} - Example Product 2", "price": "$12.50", "link": "https://aliexpress.com/item2"},
        {"title": f"{query} - Example Product 3", "price": "$7.30", "link": "https://aliexpress.com/item3"},
        {"title": f"{query} - Example Product 4", "price": "$15.00", "link": "https://aliexpress.com/item4"},
    ][:int(cfg["MAX_RESULTS"])]

@dp.message_handler(commands=["find", "חפש", "product", "search"])
async def handle_find_command(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply("❗ נא לציין מה לחפש. לדוגמה: /find כבל USB")
        return
    query = parts[1]
    results = search_aliexpress(query)
    for item in results:
        text = f"""*{item['title']}*
💲 מחיר: {item['price']}
[לצפייה במוצר]({item['link']})"""
        await message.reply(text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)