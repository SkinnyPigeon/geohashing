from main import UniqueGeoHash


def test_knows_if_file_is_compressed():
    ugh = UniqueGeoHash()
    assert ugh.is_file_compressed('test_points.txt.gz') == 'gz'
    assert ugh.is_file_compressed('test_points.txt') is False


def test_can_import_compressed_file():
    ugh = UniqueGeoHash()
    coords = ugh.import_compressed_file(
        'data/test_points_test.txt.gz',
        'gz'
    )
    assert coords['lat'] == [41.37484808,
                             41.37438124,
                             41.3806658,
                             41.389865]
    assert coords['lng'] == [2.11886538,
                             2.11842003,
                             2.1647467,
                             2.1556433]
    assert coords['geohash'] == ['sp3e2hncvnsw3r1h',
                                 'sp3e25yx4z8mwv4r',
                                 'sp3e3m07f70ns0',
                                 'sp3e3nc9qnh1u']


def test_can_import_non_compressed_file():
    ugh = UniqueGeoHash()
    coords = ugh.import_non_compressed_file(
        'data/test_points_test.txt'
    )
    assert coords['lat'] == [41.37484808,
                             41.37438124,
                             41.3806658,
                             41.389865]
    assert coords['lng'] == [2.11886538,
                             2.11842003,
                             2.1647467,
                             2.1556433]
    assert coords['geohash'] == ['sp3e2hncvnsw3r1h',
                                 'sp3e25yx4z8mwv4r',
                                 'sp3e3m07f70ns0',
                                 'sp3e3nc9qnh1u']


def test_prefixes_list_should_be_same_length():
    ugh = UniqueGeoHash()
    coords = ugh.import_compressed_file(
        'data/test_points.txt.gz', 'gz'
    )
    prefixes = ugh.get_unique_prefexes(coords['geohash'])
    assert len(coords['geohash']) == len(prefixes)


def test_prefixes_should_be_same_order():
    ugh = UniqueGeoHash()
    expected = ['sp3e2h', 'sp3e25', 'sp3e3m', 'sp3e3n']
    coords = ugh.import_non_compressed_file(
        'data/test_points_test.txt'
    )
    prefixes = ugh.get_unique_prefexes(coords['geohash'])
    assert expected == prefixes


def test_can_create_output():
    ugh = UniqueGeoHash()
    coords = ugh.create_output(
        'data/test_points_test.txt'
    )
    assert coords['lat'] == [41.37484808,
                             41.37438124,
                             41.3806658,
                             41.389865]
    assert coords['lng'] == [2.11886538,
                             2.11842003,
                             2.1647467,
                             2.1556433]
    assert coords['geohash'] == ['sp3e2hncvnsw3r1h',
                                 'sp3e25yx4z8mwv4r',
                                 'sp3e3m07f70ns0',
                                 'sp3e3nc9qnh1u']
    assert coords['unique_prefix'] == ['sp3e2h',
                                       'sp3e25',
                                       'sp3e3m',
                                       'sp3e3n']
