import pygeohash as pgh
import gzip
import trie
import csv


class UniqueGeoHash:
    def is_file_compressed(self, filename: str):
        extension = filename.split('.')[-1]
        if extension in ['gz']:
            return extension
        return False

    def import_compressed_file(self, filename: str, extension: str):
        if extension == 'gz':
            with gzip.open(filename, 'rt') as f:
                return self.format_file(f)

    def import_non_compressed_file(self, filename: str):
        with open(filename, 'r') as f:
            return self.format_file(f)

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
                coords['geohash'].append(pgh.encode(
                    lat_float,
                    lng_float,
                    precision=precision
                ))
        return coords

    def get_unique_prefexes(self, geohashes: list):
        gup = trie.GenerateUniquePrefixes()
        res = gup.get_shortest_prefixes(geohashes)
        return res

    def create_output(self, filename: str):
        compressed = self.is_file_compressed(filename)
        if compressed:
            coords = self.import_compressed_file(filename, compressed)
        else:
            coords = self.import_non_compressed_file(filename)
        prefixes = self.get_unique_prefexes(coords['geohash'])
        coords['unique_prefix'] = prefixes
        return coords

    def format_output(self, output: dict):
        with open('output.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(output.keys())
            writer.writerows(zip(*output.values()))

    def return_output(self):
        with open('output.csv', 'r') as f:
            for line in f:
                print(line.rstrip('\n'))

    def run(self, filename: str):
        output = self.create_output(filename)
        self.format_output(output)
        self.return_output()


if __name__ == '__main__':
    ugh = UniqueGeoHash()
    ugh.run('data/test_points.txt.gz')
