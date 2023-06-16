from googleapiclient.discovery import Resource
import os
import json


def test_print_info(channel, channel_info, capsys):
    channel.print_info()
    captured = capsys.readouterr()
    print(channel_info[0])
    assert f"{channel_info[0]}" in captured.out
    assert f"{channel_info[1]}" in captured.out


def test_get_service(channel):
    service = channel.get_service()
    assert isinstance(service, Resource)


def test_to_json(channel, tmpdir):
    file_path = os.path.join(tmpdir, 'test_channel.json')
    channel.to_json(file_path)

    with open(file_path, 'r') as file:
        channel_data = json.load(file)

    assert channel_data['channel_id'] == channel.channel_id
    assert channel_data['channel_title'] == channel._Channel__channel_title
    assert channel_data['channel_description'] == channel._Channel__channel_description
    assert channel_data['channel_url'] == channel._Channel__channel_url
    assert channel_data['subscriberCount'] == channel._Channel__subscriber_count
    assert channel_data['videoCount'] == channel._Channel__video_count
    assert channel_data['viewCount'] == channel._Channel__view_count


def test_str(channel):
    expected_str = "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"
    assert str(channel) == expected_str


def test_eq(channel, channel_second):
    channel._Channel__subscriber_count, channel_second._Channel__subscriber_count = 1000, 1000
    assert channel == channel


def test_lt(channel, channel_second):
    channel._Channel__subscriber_count, channel_second._Channel__subscriber_count = 500, 1000
    assert channel < channel_second


def test_add(channel, channel_second):
    channel._Channel__subscriber_count, channel_second._Channel__subscriber_count = 500, 1000
    assert (channel + channel_second) == 1500


def test_rsub(channel, channel_second):
    channel._Channel__subscriber_count, channel_second._Channel__subscriber_count = 1000, 500
    assert (channel_second - channel) == -500


def test_sub(channel, channel_second):
    channel._Channel__subscriber_count, channel_second._Channel__subscriber_count = 1000, 500
    assert (channel - channel_second) == 500
