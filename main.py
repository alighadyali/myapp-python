import nclib
import utility
import threading
import time
import devices
import argparse
import getopt
import sys


def main(args):
    args.simulate()


def usage():
    print("%s" % ("-h --help Display this menu"))


if __name__ == "__main__":
    try:
        print('ARGV:', sys.argv[1:])

        options, remainder = getopt.gnu_getopt(
            sys.argv[1:], 'o:v:bh', ['output=', 'variant=', 'build', 'help'])

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    # cmd parser
    for opt, arg in options:
        if opt in ('-o', '--output'):
            # print('Args --output.')
            output_file = arg
        elif opt == '--variant':
            # print('Args --variant.')
            variant = arg
        elif opt in ('-h', '--help'):
            # print('Args --help.')
            usage()
            sys.exit()
        elif opt in ('-v', '--verbose'):
            # print('Setting --verbose.')
            verbose = True

    motor = devices.Motor('0xDE')
    delorean = devices.TimeMachine('0xAD')
    gyroscope = devices.Gyroscope('0xBE')
    gps = devices.Gps('0xEF')
    driver = devices.Driver(motor, delorean, gyroscope, gps)

    while True:
        main(driver)
        time.sleep(1)
