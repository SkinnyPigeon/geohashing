from antigravity import geohash
import pygeohash as pgh
import gzip


class UniqueGeoHash:
    def is_file_compressed(self, filename):
        extension = filename.split('.')[-1]
        if extension in ['gz']:
            return extension
        return False

    def import_compressed_file(self, filename, extension):
        if extension == 'gz':
            with gzip.open(filename, 'rt') as f:
                return self.format_file_v2(f)

    def import_non_compressed_file(self, filename):
        with open(filename, 'r') as f:
            return self.format_file_v2(f)

    # def create_unique_geohash(self, lat, lng, precision, geohashes):
    #     unique = False
    #     while not unique:
    #         geohash = pgh.encode(lat, lng, precision=precision)
    #         print(geohash)
    #         precision = precision + 1
    #         if geohash not in geohashes:
    #             unique = True
    #     return geohash

    def format_file(self, open_file):
        coords = {'lat': [], 'lng': [], 'geohash': []}
        for i, line in enumerate(open_file):
            columns = line.rstrip('\n').split(',')
            if i == 0:
                lat_index = columns.index('lat')
                lng_index = columns.index('lng')
            else:
                lat_str = columns[lat_index]
                lng_str = columns[lng_index]
                precision = len(lat_str.split('.')[1] + lng_str.split('.')[1])
                lat_float = float(lat_str)
                lng_float = float(lng_str)
                coords['lat'].append(lat_float)
                coords['lng'].append(lng_float)
                geohash = self.create_unique_geohash(
                    lat_float,
                    lng_float,
                    precision,
                    set(coords['geohash']))
                coords['geohash'].append(geohash)
                # coords['geohash'].append(pgh.encode(
                #     lat_float,
                #     lng_float,
                #     precision=precision
                # ))
        return coords

    def format_file_v2(self, open_file):
        coords = {'lat': [], 'lng': [], 'geohash': []}
        coords_set = set()
        for i, line in enumerate(open_file):
            columns = line.rstrip('\n').split(',')
            if i == 0:
                lat_index = columns.index('lat')
                lng_index = columns.index('lng')
            else:
                coords_set.add(line)
        for line in coords_set:
            columns = line.rstrip('\n').split(',')
            lat_str = columns[lat_index]
            lng_str = columns[lng_index]
            precision = len(lat_str.split('.')[1] + lng_str.split('.')[1])
            lat_float = float(lat_str)
            lng_float = float(lng_str)
            coords['lat'].append(lat_float)
            coords['lng'].append(lng_float)
            coords['geohash'].append(pgh.encode(
                lat_float,
                lng_float,
                precision=precision
            ))
        return coords

    def shortest_geohash_prefix(self, geohashes):
        return list(dict.fromkeys(geohashes))
        # sorted_hashes = sorted(geohashes)
        # copy_one = sorted_hashes[:-1]
        # copy_two = sorted_hashes[1:]
        # shortest_hashes = []
        # for i, j in zip(copy_one, copy_two):
        #     shortest_hash = ''
        #     for letter in i:
        #         shortest_hash += letter
        #         if shortest_hash == j[:len(shortest_hash)]:
        #             continue
        #         else:
        #             break
        # print(sorted_hashes)
        # print(copy_one)
        # print(copy_two)
        # return sorted_hashes
        # return geohashes


# test_hashes = ['sp3e2hncvnsw3r1h', 'sp3e25yx4z8mwv4r', 'sp3e3m07f70ns0', 'sp3e3nc9qnh1u', 'sp3e3m07f70ns0', 'sp3e3m3h4qqx6p']
# ugh = UniqueGeoHash()
# test = ugh.shortest_geohash_prefix(test_hashes)
ugh = UniqueGeoHash()
imported_file = ugh.import_compressed_file('data/test_points.txt.gz', 'gz')
ugh_prefixs = ugh.shortest_geohash_prefix(imported_file['geohash'])