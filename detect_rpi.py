#!/usr/bin/env python3

import sys

# TODO: Find RPI 5 and add to this table
VERSION_STRING_MAPPING = {
    "Raspberry Pi Zero":   ("0x20000000", 400000000),
    "Raspberry Pi Zero 2": ("0x3F000000", 400000000),
    "Raspberry Pi 1":      ("0x20000000", 400000000),
    "Raspberry Pi 2":      ("0x3F000000", 250000000),
    "Raspberry Pi 3":      ("0x3F000000", 250000000),
    "Raspberry Pi 4":      ("0xFE000000", 250000000),
}

def detect_rpi_version(override):

    if not override:
        try:
            with open("/sys/firmware/devicetree/base/model", "r") as f:
                id_string = f.read()
        except FileNotFoundError:
            print("Not running on a Raspberry Pi, quitting")
            sys.exit(-1)
    else:
        id_string = override

    for version_string in VERSION_STRING_MAPPING:
        if id_string.startswith(version_string):
            return VERSION_STRING_MAPPING[version_string]

    print("Could not determine rasperry pi version")
    sys.exit(-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        override = sys.argv[1]
    else:
        override = ""
    addr, freq = detect_rpi_version(override)
    print("-DPHYS_REG_BASE=%s -DCLOCK_HZ=%d" % (addr, freq)) 