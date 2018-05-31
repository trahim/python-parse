import requests
import json
import argparse
import textwrap

def get_inventory(url):
    endpoint = ("http://%s/output" % url)
    r = requests.get(endpoint)
    return r.json()

def get_values(invent):
    inventory = json.loads(invent)
    count = inventory["count"]
    text = inventory["text"]
    return count, text


def print_inventory(count, text):
    lines = textwrap.wrap(text, count)
    for line in lines:
        print line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query inventory api')
    parser.add_argument('--url', help='Inventory url', required=True)
    args = parser.parse_args()

    request = get_inventory(args.url)
    count, text = get_values(request)
    print_inventory(count, text)




