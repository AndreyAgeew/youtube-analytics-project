def test_print_info(channel, channel_info, capsys):
    channel.print_info()
    captured = capsys.readouterr()
    print(channel_info[0])
    assert f"{channel_info[0]}" in captured.out
    assert f"{channel_info[1]}" in captured.out
