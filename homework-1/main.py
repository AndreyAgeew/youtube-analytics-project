from src.channel import Channel
from src.config import CHANNEL_ID
if __name__ == '__main__':
    moscowpython = Channel(CHANNEL_ID)
    moscowpython.print_info()
