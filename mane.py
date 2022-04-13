from aiohttp import Payload
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text, KeyboardButtonColor
bot = Bot(token="ffcfcb1096a10af2546904600abe3d36956f0ff7be8706dc2c5c5e8f50d4a37cfe27f7d4896fe96fe34e8")


async def getUser(user_id):  # Позволяет получить информацию о пользователе (id, имя, фамилию и т.д.)
    try:
        return (await bot.api.users.get(user_ids=user_id))[0]
    except:
        return None

@bot.on.message(text=["Привет", "Начать"])
async def start(event: Message):
    member = await getUser(event.from_id)
    keyboadr = Keyboard(one_time=True)

    keyboadr.add(Text("Menu", {"Start": "menu"}))
    await event.answer(f"Привет, {member.first_name}", keyboard=keyboadr)


@bot.on.message(payload={"Start": "menu"})
async def menu(event: Message):
    keyboadr = Keyboard(one_time=True)

    keyboadr.add(Text("Группа"), color=KeyboardButtonColor.NEGATIVE)
    keyboadr.add(Text("Расписание"), color=KeyboardButtonColor.NEGATIVE)

    keyboadr.row()

    keyboadr.add(Text("Архив группы"), color=KeyboardButtonColor.POSITIVE)

    await event.answer("Держи!", keyboard=keyboadr)




bot.run_forever()
