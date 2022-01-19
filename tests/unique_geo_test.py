from main import UniqueGeoHash


def test_knows_if_file_is_compressed():
    ugh = UniqueGeoHash()
    assert ugh.is_file_compressed('test_points.txt.gz') == 'gz'
    assert ugh.is_file_compressed('test_points.txt') is False
