#!/usr/bin/env python3

import time
from smbus2 import SMBusWrapper, i2c_msg


class DigitalClock:

    def __init__(self):
        with SMBusWrapper(1) as bus:
            msg = i2c_msg.write(0x70, [0x21])
            bus.i2c_rdwr(msg)

            msg = i2c_msg.write(0x70, [0xa0])
            bus.i2c_rdwr(msg)

            msg = i2c_msg.write(0x70, [0x81])
            bus.i2c_rdwr(msg)

            for i in range(4):
                self.digit(i, -1)

    def digit(self, digit, fig):

        if digit < -1 or digit > 3:
            return

        if fig < -1 or fig > 9 or (digit == 3 and fig > 1):
            return

        a = [0x00, 0x02, 0x04, 0x06]
        v = [0x00, 0x6f, 0x28, 0x5d, 0x7c, 0x3a, 0x76, 0x77, 0x2c, 0x7f, 0x7e]

        if digit == 3 and fig <= 0:
            msg = i2c_msg.write(0x70, [0x06, 0x00])
        else:
            msg = i2c_msg.write(0x70, [a[digit], v[fig + 1]])

        with SMBusWrapper(1) as bus:
            bus.i2c_rdwr(msg)


def main():

    dc = DigitalClock()

    # dc.digit(0, 4)
    # dc.digit(1, 3)
    # dc.digit(2, 2)
    # dc.digit(3, 1)


if __name__ == "__main__":
    main()
