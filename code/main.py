import pygeohash as pgh
import gzip
import trie
import csv
from io import TextIOWrapper


class UniqueGeoHash:
    def is_file_compressed(self, filename: str):
        """
        Checks whether the file is compressed or not. This allows some \
        extension to the functionality by providing a check for various \
        compression standards.

            Parameters:
                filename (str): The path to the file to be imported

            Returns:
                extension (str): If the file is compressed, the extension \
                is returned e.g. 'gz'. Otherwise it returns False
        """
        extension = filename.split('.')[-1]
        if extension in ['gz']:
            return extension
        return False

    def import_compressed_file(self, filename: str, extension: str):
        """
        Imports a compressed file to the desired format. This could be \
        extended to work with other compression formats.

            Parameters:
                filename (str): The path to the file to be imported
                extension (str): The type of compression being used

            Returns:
                coords (dict): The initial coordinates dictionary \
                complete with the lat, lng, and geohash values
        """
        if extension == 'gz':
            with gzip.open(filename, 'rt') as f:
                return self.format_file(f)

    def import_non_compressed_file(self, filename: str):
        """
        Imports a non-compressed file to the desired format.

            Parameters:
                filename (str): The path to the file to be imported

            Returns:
                coords (dict): The initial coordinates dictionary \
                complete with the lat, lng, and geohash values
        """
        with open(filename, 'r') as f:
            return self.format_file(f)

    def format_file(self, open_file: TextIOWrapper):
        """
        Loops through the input file and formats the data into a \
        dictionary. The dictionary contains the values for the lat \
        and lng as provided by the input file. It also uses the \
        pygeohash package to create geohashes and stores them too.

            Parameters:
                open_file (TextIOWrapper): The file with is opened \
                by one of the import functions

            Returns:
                coords (dict): The initial coordinates dictionary \
                complete with the lat, lng, and geohash values
        """
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
        """
        Uses the trie.GenerateUniquePrefixes class to select \
        the shortest unique prefixes for the geohashes

            Parameters:
                geohashes (list): The list of geohashes generate \
                by the format_file function

            Returns:
                unique_prefixes (list): The list of the shortest \
                unique prefixes for the supplied geohashes
        """
        gup = trie.GenerateUniquePrefixes()
        res = gup.get_shortest_prefixes(geohashes)
        return res

    def create_output(self, filename: str):
        """
        Combines various other functions to import the file and \
        create a dictionary that has all four required fields

            Parameters:
                filename (str): The path to the file to be imported

            Returns:
                coords (dict): The final coordinates dictionary \
                complete with the lat, lng, geohashes, and the \
                unique geohash prefixes
        """
        compressed = self.is_file_compressed(filename)
        if compressed:
            coords = self.import_compressed_file(filename, compressed)
        else:
            coords = self.import_non_compressed_file(filename)
        prefixes = self.get_unique_prefexes(coords['geohash'])
        coords['unique_prefix'] = prefixes
        return coords

    def format_output(self, coords: dict):
        """
        Generates a staging csv from the coordinates dictionary \
        in order to properly format the output

            Parameters:
                coords (dict): The final coordinates dictionary \
                complete with the lat, lng, geohashes, and the \
                unique geohash prefixes

            Returns:
                None
        """
        with open('output.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(coords.keys())
            writer.writerows(zip(*coords.values()))

    def return_output(self):
        """
        Reads and prints the staged output.csv to meet required \
        output

            Parameters:
                None

            Returns:
                None
        """
        with open('output.csv', 'r') as f:
            for line in f:
                print(line.rstrip('\n'))

    def run(self, filename: str):
        """
        Main function for interacting with the class. \
        Handles the importing, formatting, and outputting \
        of the data set.

            Parameters:
                filename (str): The path to the file to be imported

            Return:
                None
        """
        output = self.create_output(filename)
        self.format_output(output)
        self.return_output()


if __name__ == '__main__':
    ugh = UniqueGeoHash()
    ugh.run('data/test_points.txt.gz')
