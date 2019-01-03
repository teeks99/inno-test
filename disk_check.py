import binascii
import os
import sys
import datetime

def check_dir(target):
    for root, dirs, files in os.walk(target):
        for file in files:
            filename = os.path.join(root, file)
            with open(filename, 'rb') as f:
                crc = binascii.crc32(f)

def time_check(target):
    start = datetime.datetime.now()
    check_dir(target)
    stop = datetime.datetime.now()
    print("Elapsed: {}".format(stop-start))

if __name__ == "__main__":
    target = sys.argv[1]

    print("Checking: " + target)
    time_check(target)
