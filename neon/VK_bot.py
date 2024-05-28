89890490427

import vk_api
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from vk_api.longpoll import VkLongPoll, VkEventType
banlist = [000000000,000000000] # тут писать id-шники тех кого хочешь удалять сообщения 
def auth_handler():
    key = input("Введите код для двухфакторной аутификации: ")
    remember_device = True
    return key, remember_device
def main():                       
    login, password = '89269076167','QWerTy123456'
    vk_session = vk_api.VkApi(
        login, password, token="02959d5a02959d5a02959d5a7b0185336d0029502959d5a618a0054bb57cb62533a83fb", app_id="51424823",
        auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('New message:')
            if event.from_user or event.from_chat:
                if event.user_id in banlist:
                    vk.messages.delete(message_ids=event.message_id, peer_id=event.peer_id)
                if event.from_chat:
                    print(event.user_id, 'in chat', event.chat_id)
                elif event.from_user:
                    print('from user:', event.user_id)
            print('Text: ', event.text)
            print()


if __name__ == '__main__':
    main()