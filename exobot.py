import asyncio
import logging
from aiogram.client.session.aiohttp import AiohttpSession
from datetime import datetime
from aiogram import Bot, Dispatcher, types, html
from aiogram.filters.command import Command
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7636532893:AAEMamuwIJmECTS19nuYpQZelML0b9ykY2Q")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start с именем пользователя html
@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="Каталог"),
            types.KeyboardButton(text="Менеджер")
        ],
        [
            types.KeyboardButton(text="Галерея"),
            types.KeyboardButton(text="Документация")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer(f"Здравствуйте, {(message.from_user.full_name)}!\nВы в магазине OdinWork!\nНаш магазин изготавливает изделия из натуральной кожи.\nБот поможет с выбором идеального для вас изделия!\n\nОзнакомьтесь пожалуйста с каталогом:", reply_markup=keyboard)
##button
@dp.message(F.text.lower() == "назад")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Каталог"),
            types.KeyboardButton(text="Менеджер")
        ],
        [
            types.KeyboardButton(text="Галерея"),
            types.KeyboardButton(text="Документация")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("OdinWork", reply_markup=keyboard)

# Список команд От


# command standart
@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    await message.answer("https://t.me/klvdnil")

@dp.message(Command("master"))
async def command_start_handler(message: Message) -> None:
    await message.answer("https://www.instagram.com/odinworkl?igsh=bjM0N2FyenFuNTZk")

@dp.message(Command("service"))
async def command_start_handler(message: Message) -> None:
    await message.answer("+7 (985) 5678800")

@dp.message(Command("avito"))
async def command_start_handler(message: Message) -> None:
    await message.answer("https://www.avito.ru/user/c7a41158207b7973bd185e38a78b9f81/profile?src=sharing")

@dp.message(Command("youtube"))
async def command_start_handler(message: Message) -> None:
    await message.answer("https://youtube.com/@odinwork?si=nhLUrTcjaCW3_K5f")

@dp.message(Command("free"))
async def command_start_handler(message: Message) -> None:
    await message.answer("===")
## command standart

#doc
@dp.message(F.text.lower() == "документация")
async def without_puree(message: types.Message):
    await message.reply("<b>Сертификат качества</b> \n\nНастоящий документ удостоверяет, что изделия ручной работы из натуральной кожи, изготовленные мастером компании OdinWork, соответствуют высоким стандартам качества и выполнены с соблюдением всех необходимых технологий обработки материалов.\n\n" \
    "<b>Гарантия</b>\n\nГарантийный срок составляет два года ( 2 года) со дня приобретения изделия потребителем. Гарантийные обязательства распространяются на дефекты производства и материалы, возникшие не по вине покупателя.\n\n" \
    "<b>Условия гарантийного обслуживания:</b>\n\n - Изделия подлежат бесплатному ремонту или замене в течение гарантийного срока при обнаружении дефектов производственного характера.\n - Обязательства по гарантии не действуют в случаях повреждения изделий вследствие неправильного ухода, механических повреждений, воздействия агрессивных веществ, влаги или огня.\n\n" \
    "Настоящий сертификат выдан покупателю вместе с изделием и является документом, подтверждающим качество продукции и право на бесплатное обслуживание в рамках установленного гарантийного периода.\n\n" \
    "| Сертификат № | КД 96091 |\n|--------------|-------------|\n|             | 09.12.2015 г. |    \n\nПодпись мастера: OdinWork \n\nАдрес мастерской: г.Одинцово, Можайское шоссе, 22А.\nКонтактная информация: \n+7 (985) 567-88-00", parse_mode=ParseMode.HTML)
##doc

# менеджер
@dp.message(F.text.lower() == "менеджер")
async def without_puree(message: types.Message):
    await message.reply("https://t.me/klvdnil")
## менеджер

#button 
@dp.message(F.text.lower() == "каталог")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Картхолдеры"),
            types.KeyboardButton(text="Обложки"),
        ],
        [
            types.KeyboardButton(text="Коллекции"),
            types.KeyboardButton(text="Ремни"),
        ],
        [
            types.KeyboardButton(text="Сумки муж"),
            types.KeyboardButton(text="Сумки жен"),
        ],
        [
            types.KeyboardButton(text="Назад"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выберите интересующий товар!", reply_markup=keyboard)
##button



#фото картхолдера cart.jpg
@dp.message(F.text.lower() == "картхолдеры")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы cart.jpg
    image_from_pc = FSInputFile("cart.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Яркие цвета?"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла из файловой системы cart.jpg
    image_from_pc = FSInputFile("cart-q.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Пастельные цвета?"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла из файловой системы cart.jpg
    image_from_pc = FSInputFile("cart-w.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Темные цвета?"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красный"),
            types.KeyboardButton(text="Жертый"),
            types.KeyboardButton(text="Синий")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевый"),
            types.KeyboardButton(text="Бежевый")
        ],
        [
            types.KeyboardButton(text="Черный"),
            types.KeyboardButton(text="Коричневый"),
            types.KeyboardButton(text="Серый")
        ],
        [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото сумок общее.jpg
@dp.message(F.text.lower() == "сумки муж")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы bags.jpg сумки
    image_from_pc = FSInputFile("bags.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Так же напишите мастеру для индивидуального подбора цвета!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красная"),
            types.KeyboardButton(text="Жертая"),
            types.KeyboardButton(text="Синяя")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевая"),
            types.KeyboardButton(text="Бежевая")
        ],
        [
            types.KeyboardButton(text="Черная"),
            types.KeyboardButton(text="Коричневая"),
            types.KeyboardButton(text="Серая")
        ],
        [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото ремни.jpg
@dp.message(F.text.lower() == "ремни")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы belts.jpg сумки
    image_from_pc = FSInputFile("belts.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Так же напишите мастеру для индивидуального подбора цвета!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красный"),
            types.KeyboardButton(text="Жертый"),
            types.KeyboardButton(text="Синий")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевый"),
            types.KeyboardButton(text="Бежевый")
        ],
        [
            types.KeyboardButton(text="Черный"),
            types.KeyboardButton(text="Коричневый"),
            types.KeyboardButton(text="Серый")
        ],
        [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото сумок общее.jpg
@dp.message(F.text.lower() == "сумки жен")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы bags.jpg сумки
    image_from_pc = FSInputFile("bagsw.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Так же напишите мастеру для индивидуального подбора цвета!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красная"),
            types.KeyboardButton(text="Жертая"),
            types.KeyboardButton(text="Синяя")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевая"),
            types.KeyboardButton(text="Бежевая")
        ],
        [
            types.KeyboardButton(text="Черная"),
            types.KeyboardButton(text="Коричневая"),
            types.KeyboardButton(text="Серая")
        ],
        [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото колекции .jpg
@dp.message(F.text.lower() == "коллекции")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы aaaa.jpg обложки
    image_from_pc = FSInputFile("collection.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Мастер поможет с индивидуальным выбором!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Набор mini"),
            types.KeyboardButton(text="Набор Blak")
        ],
        [
            types.KeyboardButton(text="Набор cosmos"),
            types.KeyboardButton(text="Набор Infiniti")
        ],
         [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото сумок общее.jpg
@dp.message(F.text.lower() == "сумки жен")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы bags.jpg сумки
    image_from_pc = FSInputFile("bagsw.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Так же напишите мастеру для индивидуального подбора цвета!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красная"),
            types.KeyboardButton(text="Жертая"),
            types.KeyboardButton(text="Синяя")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевая"),
            types.KeyboardButton(text="Бежевая")
        ],
        [
            types.KeyboardButton(text="Черная"),
            types.KeyboardButton(text="Коричневая"),
            types.KeyboardButton(text="Серая")
        ],
        [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button

#фото обложки общее .jpg
@dp.message(F.text.lower() == "обложки")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы aaaa.jpg обложки
    image_from_pc = FSInputFile("aaaa.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Так же напишите мастеру для индивидуального подбора цвета!!!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Красная"),
            types.KeyboardButton(text="Жертая"),
            types.KeyboardButton(text="Синяя")
        ],
        [
            types.KeyboardButton(text="Хакки"),
            types.KeyboardButton(text="Оранжевая"),
            types.KeyboardButton(text="Бежевая")
        ],
        [
            types.KeyboardButton(text="Черная"),
            types.KeyboardButton(text="Коричневая"),
            types.KeyboardButton(text="Серая")
        ],
         [
            types.KeyboardButton(text="каталог")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Выбор за Вами!!!", reply_markup=keyboard)
##button


@dp.message(F.text.lower() == "другие цвета")
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []

    # Отправка файла из файловой системы send.jpg
    image_from_pc = FSInputFile("send.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Палитра цветов!"
    )
    file_ids.append(result.photo[-1].file_id)

    kb = [
        [
            types.KeyboardButton(text="Назад"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("Напиши мастеру!\nhttps://t.me/klvdnil", reply_markup=keyboard)





#фото ГАЛЕРЕЯ
@dp.message(F.text.lower() == "галерея")
async def upload_photo(message: Message):
 #   # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []
#
    image_from_pc = FSInputFile("g1.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Украшения, Игрушки, Брелки!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g2.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Плейсматы и Столовые принадлежности!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g3.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Блокноты любой сложности!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g4.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Гравировки и оттиски!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g5.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Чехлы для карт!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g6.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Обложки из кожи!"
    )
    file_ids.append(result.photo[-1].file_id)
    image_from_pc = FSInputFile("g7.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Пеналы и косметичка!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g8.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Патронтажи!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g9.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Полотна из кожи!"
    )
    file_ids.append(result.photo[-1].file_id)
    image_from_pc = FSInputFile("g10.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Чехлы для Телефонов!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g11.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Блокноты!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g12.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Футляры для очков!"
    )
    file_ids.append(result.photo[-1].file_id)
    image_from_pc = FSInputFile("g13.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Чехлы для наушников!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g14.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="AirTag!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    image_from_pc = FSInputFile("g15.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Набор для автомобилей!"
    )
    file_ids.append(result.photo[-1].file_id)
    image_from_pc = FSInputFile("g16.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Ключницы!"
    )
    file_ids.append(result.photo[-1].file_id)
#
    kb = [
        [
            types.KeyboardButton(text="назад")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="OdinWork"
    )
    await message.answer("И много всего интересного!!!\nНапиши мастеру!\nhttps://t.me/klvdnil", reply_markup=keyboard)
##foto  g1-g16




#test
#++
@dp.message(F.text.lower() == "trest")
async def without_puree(message: types.Message):
    await message.reply("<b>хорошо</b>" \
    "ghghgjgj" \
    "fvdvffv" \
    "vfvdvdvf\n" \
    "fvvfdvdvf", parse_mode=ParseMode.HTML)
##test


#Список команд До
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# Документвция : 1

# Разница между answer и reply простая: 
#     -первый метод просто отправляет сообщение в тот же чат, 
#     -второй делает "ответ" на сообщение из message:
#   @dp.message(Command("answer"))
#   async def cmd_answer(message: types.Message):
#      await message.answer("Это простой ответ")
#
#  @dp.message(Command("reply"))
#  async def cmd_reply(message: types.Message):
#      await message.reply('Это ответ с "ответом"')
