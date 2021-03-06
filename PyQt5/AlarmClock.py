#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    try:
        due = QTime.currentTime()
        print(due)
        message = "Alert!"
        if len(sys.argv) < 2:
            raise ValueError
        hours, mins = sys.argv[1].split(':')
        due = QTime(int(hours), int(mins))
        if not due.isValid():
            raise ValueError
        if len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])
    except ValueError:
        message = "Usage:alert.py HH:MM [optional message]"

    while QTime.currentTime() < due:
        time.sleep(2)






