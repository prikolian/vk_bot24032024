import asyncio
import logging

import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime



from config.config import Config_vk, load_vk_config
from keyboards.vk.user_menu import keyboard_1, keyboard_2
import json

logger = logging.getLogger(__name__)

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config_vk: Config_vk = load_vk_config()

    vk_session = vk_api.VkApi(token=config_vk.vk_bot.token)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, config_vk.vk_bot.id_group)
    last_message_time = {}

    for event in longpoll.listen():
        # отправляем меню 1го вида на любое текстовое сообщение от пользователя
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message['from_id']
            if event.obj.message['text'] != '':
                current_time = datetime.datetime.now()
                if user_id in last_message_time and (current_time - last_message_time[user_id]).days < 1:
                    continue
                if event.from_user:
                    # await send_message(event.message.from_id, 'Привет, я бот!')

                    # Если клиент пользователя не поддерживает callback-кнопки,
                    # нажатие на них будет отправлять текстовые
                    # сообщения. Т.е. они будут работать как обычные inline кнопки.
                    if 'callback' not in event.obj.client_info['button_actions']:
                        print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')

                    vk.messages.send(
                        user_id=user_id,
                        current_time=datetime.datetime.now(),
                        random_id=0,
                        last_message_time={},
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message='Вас приветствует Бот школы танцев V-Pantera Dance. '
                                'Для получения информации выберите наиболее удобную студию ❤️')
                    last_message_time[user_id] = current_time
        # обрабатываем клики по callback кнопкам
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            # если это одно из 3х встроенных действий:
            if event.object.payload.get('type') in CALLBACK_TYPES:
                # отправляем серверу указания как какую из кнопок обработать. Это заложено в
                # payload каждой callback-кнопки при ее создании.
                # Но можно сделать иначе: в payload положить свои собственные
                # идентификаторы кнопок, а здесь по ним определить
                # какой запрос надо послать. Реализован первый вариант.
                r = vk.messages.sendMessageEventAnswer(
                    event_id=event.object.event_id,
                    user_id=event.object.user_id,
                    peer_id=event.object.peer_id,
                    event_data=json.dumps(event.object.payload))
            # если это наша "кастомная" (т.е. без встроенного действия) кнопка, то мы можем
            # выполнить edit сообщения и изменить его меню. Но при желании мы могли бы
            # на этот клик открыть ссылку/приложение или показать pop-up. (см.анимацию ниже)
            elif event.object.payload.get('type') == 'school1':
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message='ola',
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=(keyboard_2).get_keyboard())

            elif event.object.payload.get('type') == 'back':
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message='ola',
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=(keyboard_1).get_keyboard())




if __name__ == '__main__':
    asyncio.run(main())
