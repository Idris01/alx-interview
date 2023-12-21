#!/usr/bin/env python3
"""This module define a script that parses log read from standard input
"""


if __name__ == "__main__":
    import sys
    import re
    from collections import defaultdict
    import functools

    pattn = r"[0-9.]+ - \[.*?\] \".*?\" (?P<st>[0-9]{3}) (?P<sz>[0-9]+)"
    content = defaultdict(lambda: 0)

    def process_log(content=content):
        print("File size: {}".format(content["sz"]))
        rem = dict(content)
        del rem["sz"]
        for key in sorted(list(rem.keys())):
            print("{}: {}".format(key, rem[key]))

    def main():
        count = 0
        while True:
            try:
                if count == 10:
                    process_log(content)
                    count = 0
                line = input()
                result = re.search(pattn, line)

                if result:
                    result = result.groupdict()
                    content["sz"] += int(result.get("sz"))
                    content[result.get("st")] += 1
                    count += 1
            except KeyboardInterrupt:
                process_log(content)
                sys.exit(0)

    main()
