def test_video(video):
    assert video.video_id == "AWX4JnAnjBE"
    assert video._Video__title == "GIL в Python: зачем он нужен и как с этим жить"
    assert video._Video__title is not None
    assert video._Video__url is not None
    assert video._Video__view_count is not None
    assert video._Video__like_count is not None


def test_pl_video(pl_video):
    assert pl_video.video_id == "4fObz_qw9u4"
    assert pl_video._PLVideo__playlist_id == "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC"
    assert pl_video._Video__title == "MoscowPython Meetup 78 - вступление"
    assert pl_video._Video__title is not None
    assert pl_video._Video__url is not None
    assert pl_video._Video__view_count is not None
    assert pl_video._Video__like_count is not None
