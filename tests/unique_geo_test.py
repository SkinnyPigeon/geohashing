from main import UniqueGeoHash


def test_knows_if_file_is_compressed():
    ugh = UniqueGeoHash()
    assert ugh.is_file_compressed('test_points.txt.gz') == 'gz'
    assert ugh.is_file_compressed('test_points.txt') is False


def test_can_import_compressed_file():
    ugh = UniqueGeoHash()
    imported_file = ugh.import_compressed_file('test_points_test.txt.gz', 'gz')
    assert imported_file['lat'] == ['41.37484808',
                                    '41.37438124',
                                    '41.3806658',
                                    '41.389865']
    assert imported_file['lng'] == ['2.11886538',
                                    '2.11842003',
                                    '2.1647467',
                                    '2.1556433']
