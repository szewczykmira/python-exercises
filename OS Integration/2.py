import io
import re
import subprocess

TAB = '\t'

def process_ifconfig():
    process = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
    output = io.StringIO(process.stdout.decode('utf-8'))
    current_interface = False
    for line in output:
        if not line.startswith(TAB):
            interface = line.split(':')[0]
            if current_interface:
                current_interface.close()
            current_interface = open(interface, 'w')
        current_interface.write(line)


if __name__ == '__main__':
    process_ifconfig()
