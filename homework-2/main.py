from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Получаем значения атрибутов
    print(moscowpython._Channel__channel_title)  # MoscowPython
    print(moscowpython._Channel__video_count)  # 685 (может уже больше)
    print(moscowpython._Channel__channel_url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')
