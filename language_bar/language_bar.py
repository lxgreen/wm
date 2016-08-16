#!/usr/bin/python

import subprocess

def main():
    layout_map = {"us":"EN", "il":"HE", "ru":"RU"}
    layout = subprocess.Popen("/home/lxgreen/scripts/wm"
        "/language_bar/xkb-switch",
        stdout=subprocess.PIPE).stdout.read()
    print layout_map[layout[:2]]

if __name__ == '__main__':
    main()
