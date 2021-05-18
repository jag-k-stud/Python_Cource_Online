import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from weather import get_weather
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


GROUP_ID = 204648898
TOKEN = '3df218d59261ddd1674e9b994d4c0704ab2ad7bd7557efa451c2c71f303526dfb3bc9c005712ac8456732'

vk_session = VkApi(token=TOKEN)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

keyboard_1 = VkKeyboard(one_time=False, inline=False)
keyboard_1.add_button(
    label="Погода",
    color=VkKeyboardColor.POSITIVE
)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.object.message
        print("Новое сообщение!")
        print("От:", message['from_id'])
        print("Сообщение:", repr(message['text']))
        print()

        if message['text'].lower() in ('/start', '/weather', 'погода'):
            vk.messages.send(
                random_id=random.randint(1, 2 ** 16),
                peer_id=message['peer_id'],
                message=get_weather(),
                keyboard=keyboard_1.get_keyboard(),
            )
        else:
            vk.messages.send(
                random_id=random.randint(1, 2 ** 16),
                peer_id=message['peer_id'],
                message='Я Вас не понимаю. Я могу только рассказать про погоду. Для этого напишите мне слово "погода"',
                keyboard=keyboard_1.get_keyboard(),
            )
