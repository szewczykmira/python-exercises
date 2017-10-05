import csv
import re

INPUT_FILE_NAME = 'input.txt'
INET = re.compile('inet ')
STATUS = re.compile('status')

def process_data():
    result = []
    with open(INPUT_FILE_NAME, 'r') as input:
        for line in input.readlines():
            if re.match('\w', line):
                if locals().get('elements'):
                    result.append(elements)
                elements = {'interface': line.split(':')[0]}
            if INET.search(line):
                elements['inet'] = line.strip().split()[1]
            if STATUS.search(line):
                elements['status'] = line.strip().split()[-1]
        result.append(elements)
    return result

def write_to_file(data):
    with open('output.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['interface', 'inet', 'status'])
        for line in data:
            interface = line.get('interface', '')
            inet = line.get('inet', '')
            status = line.get('status', '')
            csv_writer.writerow([interface, inet, status])


if __name__ == '__main__':
    data = process_data()
    write_to_file(data)
