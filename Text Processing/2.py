import re
import sys

EXAMPLES = [
    "Bob Dylan - 01 You're No Good (1962).mp3",
    "Bob Dylan - 02 Talkin' New York (1962).mp3",
    "Bob Dylan - 03 In My Time of Dyin' (1962).mp3",
    "Bob Dylan - 04 Man of Constant Sorrow (1962).mp3",
    "Bob Dylan - 05 Fixin' to Die (1962).mp3",
    "Bob Dylan - 06 Pretty Peggy-O (1962).mp3",
    ]

EXAMPLE_INPUT = '<album> - <track> <title> \(<year>\).mp3'
EXAMPLE_OUTPUT = 'Bob Dylan/<year> <album>/<track> <title>.mp3'

class ParseFileName:
    ARTIST = '<artist>'
    TRACK = '<track>'
    YEAR = '<year>'
    ALBUM = '<album>'
    TITLE = '<title>'
    TYPES = [ARTIST, TRACK, YEAR, ALBUM, TITLE]

    REGEXP = {
        ARTIST: '(?P<artist>.+)',
        TRACK: '(?P<track>\d+)',
        YEAR: '(?P<year>\d+)',
        TITLE: '(?P<title>.+)',
        ALBUM: '(?P<album>.+)'}

    def __init__(self, input_type, output_type):
        self.output_type = output_type
        self.input_format, self.used = self.generate_format(input_type)

    def generate_format(self, input_format):
        parsed_format = input_format
        used_types = []
        for value in self.TYPES:
            if value in parsed_format:
                parsed_format = parsed_format.replace(value, self.REGEXP[value])
                used_types.append(value)
        return parsed_format, used_types

    def get_data(self, elem):
        matching = re.match(self.input_format, elem)
        data = {}
        for use in self.used:
            data[use] = matching.group(use[1:-1])
        return data

    def put_data(self, data):
        result = self.output_type
        for elem in self.used:
            result = result.replace(elem, data[elem])
        return result

    def parse(self, elem):
        return self.put_data(self.get_data(elem))

if __name__ == '__main__':
    # input_format = sys.argv[1]
    # output_format = sys.argv[2]
    parser = ParseFileName(EXAMPLE_INPUT, EXAMPLE_OUTPUT)
    for elem in EXAMPLES:
        print(parser.parse(elem))
