#!/usr/bin/python3
"""This module define a script that parses log read from standard input
"""
import sys
import re
from collections import defaultdict

patt = r"([0-9.]+|\w+) ?- ?\[.*?\] \".*?\" (?P<st>[0-9]+|.*?)? ?(?P<sz>[0-9]+)"
content = defaultdict(lambda: 0)
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]


def process_log(content=content):
    print("File size: {}".format(content["sz"]))
    rem = dict(content)
    del rem["sz"]
    for key in sorted(list(rem.keys())):
        if key in codes:
            print("{}: {}".format(key, rem[key]))
    sys.stdout.flush()


count = 0
try:
    for line in sys.stdin:
        if count == 10:
            process_log(content)
            count = 0

        result = re.search(patt, line)

        if result:
            result = result.groupdict()
            key = result.get("st")
            if key in codes:
                content[key] += 1
            content["sz"] += int(result.get("sz"))
        count += 1
except KeyboardInterrupt:
    pass
finally:
    process_log(content)
