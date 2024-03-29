#!/usr/bin/python
import sys
import os
from time import time
import datetime

def parse_cookie_files(input):
    cookies = input.splitlines()
    info_list = list()

    for cookie in cookies:
        help_message = f"#Failed to parse cookie:\n#'{cookie}'\n#It may be a blank line, remove it if it is"
        cookie = cookie.strip()
        try:
            name, value, domain, path, expiration, size, httpOnly = [c for c in cookie.split('\t') if c][:7]
        except ValueError:
            print(help_message, file=sys.stderr)
            continue
        if name == False:
            continue
        if domain[0] != '.':
            domain = '.' + domain

        httpOnly = ('TRUE' if httpOnly == '✓' else 'FALSE')
        if expiration == 'Session':
            expiration = int((time() + (86400 * 1000)))
        else:
            expiration = expiration.replace('Z', '')
            expiration = int(datetime.datetime.fromisoformat(expiration).timestamp())

        info_list.append(
        {
        'name': name,
        'value': value,
        'domain': domain,
        'include_subdomains': 'TRUE',
        'path': path,
        'expiration': expiration,
        'size': size,
        'httpOnly': httpOnly
        })

    return info_list

args = sys.argv[1:]
cookies = list()

print("# Netscape HTTP Cookie File")
for i in args:
    with open(i, 'rt', encoding='utf-8') as f:
        cookie = parse_cookie_files(f.read())
    for j in cookie:
        line = f"{j.get('domain')}, {j.get('include_subdomains')}, {j.get('path')}, {j.get('httpOnly')}, {j.get('expiration')}, {j.get('name')}, {j.get('value')}".replace(', ','\t')
        print(line)
