#!/usr/bin/env python
import argparse
import time
import sys


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--rps', type=int, default=10, help='Requests per second')
    return parser.parse_args()


def main():
    args = parse_args()

    last_check = time.time()
    counter = 1
    sleep = None
    rps = args.rps
    try:
        while True:
            now = time.time()
            if sleep is None or now - 1 > last_check:
                delta = now - last_check
                rate = 1 / (delta / counter)
                sleep *= rate/rps
                counter = 1
                last_check = now

            print "Timestamp=%d" % time.time()
            sys.stdout.flush()

            counter += 1
            time.sleep(sleep)

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
