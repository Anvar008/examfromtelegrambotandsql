import random

from aiogram import Bot, Dispatcher, F, types, filters
import asyncio
from database2 import Database

bot = Bot(token="7820051002:AAEljNB37qGwKjzczUXpX_B4Ud_B84Hy4Sw")
dp = Dispatcher(bot=bot)
db = Database()

# Savollar
#  1. Aiogram kutubxonasi nima va u Telegram botlarini yaratishda nima uchun ishlatiladi?
#     aiogram but kutubxona uni ichida telegram botni yaratish uchun hamma narsalari bogan uchun uni ishlatishadi
#  2. Aiogram yordamida botni qanday yaratish mumkin?
#     kereli narsalani import qilish kere masalan Bot, Dispatcher, filters, types keyin yozgan narsalarini qayta ishlidigan qilish kere
#  3. Botni aiogram’ga ulash uchun BotFather’dan qanday turdagi token olish kerak?
#     API TOKEN
#  4. Aiogram yordamida foydalanuvchilardan kiruvchi xabarlarni qanday qayta ishlash mumkin?
#     @dp.message()
#  5. Bot orqali foydalanuvchiga matnli xabar qanday yuboriladi?
#     await message.answer("text")
#  6. Aiogram yordamida yana qanday turdagi xabarlarni (foto, audio, video va h.k.) yuborish mumkin?
#     animation, dice, audio, contact, document, game, invoice, location, media_group,
#  7. Bot orqali foydalanuvchi bilan muloqot qilish uchun tugmachali klaviatura qanday amalga oshiriladi?
#     ReplyMarkup import qilish kere kegin keyboard yaratish kere kegin osha keyboardni reply_markup qilish kere
#  8. Chat va xabar yuborgan foydalanuvchi haqida qanday ma'lumot olsam bo'ladi?
#     message.from_user.
#  9. SQLite3 ma'lumotlar bazasi nima va unda qanday asosiy operatsiyalarni bajarish mumkin?
#     sqlite3 bu kutubxona u python bilan birga sqlni ishlashga beradi unda CREATE, UPDATE, INSERT, SELECT, DROP, DELETE
#  10. Pythonda SQLite3 ma'lumotlar bazasini qanday ulash va yaratish mumkin?
#      import sqlite3, db = sqlite3.connect("database.db")
#  11. Bot foydalanuvchilari haqidagi ma'lumotlarni saqlash uchun jadval yaratish uchun qanday SQL so'rovlarini bajarish kerak?
#      create_table():
#           cursor.execute("""
#           CREATE TABLE IF NOT EXISTS user(
#               name VARCHAR(255)
#           """)
#           db.commit()
#      create_table()
#  12. Bot orqali ro'yxatdan o'tishda SQLite3 ma'lumotlar bazasiga yangi foydalanuvchi qanday qo'shiladi?
#      INSERT yordamida
#  13. SQLite3 ma'lumotlar bazasida foydalanuvchi ma'lumotlarini qanday yangilash mumkin, masalan, profil o'zgarganda?
#      UPDATE yordamida
#  14. SQLite3 ma'lumotlar bazasi bilan ishlashda ma'lumotlar xavfsizligini qanday ta'minlash mumkin?
#      LIMIT yordamida
#  15. GPT-3 dan aiogram kutubxonasi bilan birgalikda ijodiy bot yaratish uchun qanday foydalanish mumkin?
#      pip install openai, import openai, keyin api key olish kere, keyin yozgan textlarini qayta ishlidigan qilish kere
# Mini-amaliy vazifa:
# Foydalanuvchidan matnli xabar oladigan va ijodiy javob bilan javob beradigan mini-bot yarating.  Aiogramda suhbatlar tarixini saqlash uchun “SQLite3” dan foydalaning. Bot bir necha turdagi xabarlarga javob bera olishi kerak, masalan, “salom”, “qalaysan?”, “menga hazil ayt”. Har bir savolning ma'lumotlar bazasidan o'ziga xos javobi bo'lishi kerak.


@dp.message(filters.Command("start"))
async def salom(message: types.Message):
    db.create_table()
    await message.answer("Hech balo chiqmidi")


@dp.message(F.text == "salom")
async def salom(message: types.Message):
    db.create_table()
    await message.answer("Qalaysan")


@dp.message(F.text == "qalaysan")
async def salom(message: types.Message):
    # db.drop()
    db.create_table()
    # db.delete()
    # db.insert("— Рыбалка — это спорт или искусство? — Когда ловят рыбу — спорт, а когда рассказывают об этом — искусство!")
    await message.answer("Salom")


@dp.message(F.text == "manga xazl ayt")
async def joke(message: types.Message):
    random_num = random.randint(1, 2)
    data = db.select()
    if random_num == 1:
        await message.answer(f"Mana xazl: \n{data[0]}")
    elif random_num == 2:
        await message.answer(f"Mana xazl: \n{data[1]}")
    else:
        await message.answer(f"Mana xazl: \n{data[2]}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
