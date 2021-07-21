import json
import sys
import re


filename = sys.argv[1]

output = []

with open(filename) as f:
    data = json.load(f)

    for d in data:
        url = re.findall(r'https:\/\/[^ >]+', d)
        for u in url:
            output.append(u)

json.dump(output, sys.stdout)