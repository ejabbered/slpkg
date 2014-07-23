#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def slack_ver():
    f = open('/etc/slackware-version', 'r')
    sv = f.read()
    f.close()
    return '.'.join(re.findall(r'\d+', sv))
