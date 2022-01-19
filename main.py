import pygeohash as pgh
import gzip

from pyparsing import col


class UniqueGeoHash:
    def is_file_compressed(self, filename):
        extension = filename.split('.')[-1]
        if extension in ['gz']:
            return extension
        return False

    def import_compressed_file(self, filename, extension):
        if extension == 'gz':
            with gzip.open(filename, 'rt') as f:
                return self.format_file(f)

    def import_non_compressed_file(self, filename):
        with open(filename, 'r') as f:
            return self.format_file(f)

    def format_file(self, open_file):
        coords = {'lat': [], 'lng': []}
        for i, line in enumerate(open_file):
            columns = line.rstrip('\n').split(',')
            if i == 0:
                lat_index = columns.index('lat')
                lng_index = columns.index('lng')
            else:
                coords['lat'].append(columns[lat_index])
                coords['lng'].append(columns[lng_index])
        return coords
