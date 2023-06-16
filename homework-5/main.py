import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.title)
    print(pl.url)
    duration = pl.total_duration
    print(duration)
    print(isinstance(duration, datetime.timedelta))
    print(duration.total_seconds())
    print(pl.show_best_video())
