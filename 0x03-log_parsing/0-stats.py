#!/usr/bin/python3
"""This module define a script that parses log read from standard input
"""
import sys
import re
from collections import defaultdict

pattn = r"[0-9.]+ - \[.*?\] \".*?\" (?P<st>[0-9]{3}) (?P<sz>[0-9]+)"
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

        result = re.search(pattn, line)

        if result:
            result = result.groupdict()
            content["sz"] += int(result.get("sz"))
            content[result.get("st")] += 1
            count += 1
finally:
    process_log(content)
