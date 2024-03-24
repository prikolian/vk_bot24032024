from vk_api.keyboard import VkKeyboard, VkKeyboardColor

settings = dict(one_time=False, inline=True)

# №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
keyboard_1 = VkKeyboard(**settings)
# pop-up кнопка
# keyboard_1.add_callback_button(label='Покажи pop-up сообщение', color=VkKeyboardColor.SECONDARY,
#                                payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
# keyboard_1.add_line()
# # кнопка с URL
# keyboard_1.add_callback_button(label='Написать администратору', color=VkKeyboardColor.POSITIVE,
#                                payload={"type": "open_link", "link": "https://t.me/NikolayBorozd1n"})
# keyboard_1.add_line()
# # кнопка по открытию ВК-приложения
# keyboard_1.add_callback_button(label='Открыть приложение', color=VkKeyboardColor.NEGATIVE,
#                                payload={"type": "open_app", "app_id": APP_ID, "owner_id": OWNER_ID,
#                                         "hash": "anything_data_100500"})
# keyboard_1.add_line()
# кнопка переключения на 2ое меню
keyboard_1.add_callback_button(label='Улица Школьная 9', color=VkKeyboardColor.PRIMARY,
                               payload={"type": "open_link", "link": "https://t.me/Pantera_Dance1"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Улица Чугунова 15А', color=VkKeyboardColor.PRIMARY,
                               payload={"type": "open_link", "link": "https://t.me/V_pantera"})



# №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
keyboard_2 = VkKeyboard(**settings)
# кнопка переключения назад, на 1ое меню.
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "back"})
