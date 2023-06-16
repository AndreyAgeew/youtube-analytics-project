from datetime import timedelta


def test_playlist(playlist, duration):
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    assert str(duration) == "1:49:52"
    assert isinstance(duration, timedelta)
    assert duration.total_seconds() == 6592.0
    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
