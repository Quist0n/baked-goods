#!/usr/bin/python
import sys
import os
from time import time
import datetime

args = sys.argv[1:]
files = list()

for i in args:
    files.append(open(i, 'rt', encoding='utf-8'))

def parse_cookie_files(input):
    cookies = input.split('\n')
    info_list = list()

    for cookie in cookies:
        cookie = cookie.strip()
        try:
            name, value, domain, path, expiration,size,httpOnly = cookie.split('\t')
        except:
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

    [domain, 'TRUE', path, httpOnly, expiration, name, value].join('\t')

print("# Netscape HTTP Cookie File")
for i in files:
    new_cookie = parse_cookie_files(i.read())
    i.close()
    for j in new_cookie:
        line = f"{j.get('domain')}, {j.get('include_subdomains')}, {j.get('path')}, {j.get('httpOnly')}, {j.get('expiration')}, {j.get('name')}, {j.get('value')}".replace(', ','\t')
        print(line)
