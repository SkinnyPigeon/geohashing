import pygeohash as pgh


class UniqueGeoHash:
    def is_file_compressed(self, filename):
        extension = filename.split('.')[-1]
        if extension in ['gz', 'zip']:
            return extension
        return False
