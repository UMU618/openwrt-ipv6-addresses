#!/usr/bin/env python3
# Copyright 2020 UMU618.
#
# Authors: UMU618 <umu618@hotmail.com>
#
import alerts
import conf
import os
import socket
import time

INET6_PATH = '/proc/net/if_inet6'
SAVE_PATH = '/tmp/ipv6-addresses'


def net_hex_to_ipv6(h):
    ipv6 = h[0:4]
    i = 4
    while i < len(h):
        ipv6 += ':' + h[i:i+4]
        i += 4
    return ipv6


def get_ipv6_addresses():
    addresses = []
    if os.path.exists(INET6_PATH):
        with open(INET6_PATH) as f:
            for line in f:
                p = line.split()
                if p[3] == '00' and (int(p[4], 16) & 0x80) != 0x80 \
                        and not p[0].startswith('fc') and not p[0].startswith('fd'):
                    ip = net_hex_to_ipv6(p[0])
                    addresses.append(socket.inet_ntop(
                        socket.AF_INET6, socket.inet_pton(socket.AF_INET6, ip)))
            f.close()
    return addresses


def read_file(fn):
    try:
        with open(fn) as f:
            str = f.read()
            f.close()
    except:
        str = ''
    return str


def write_file(fn, str):
    with open(fn, 'w') as f:
        f.write(ips)
        f.close()


def save_if_changed(fn, ips):
    if os.path.exists(fn):
        old = read_file(fn)
        if old != ips:
            write_file(fn, ips)
            return True
    else:
        write_file(fn, ips)
        return True
    return False


if __name__ == '__main__':
    my_ipv6_addresses = get_ipv6_addresses()
    if my_ipv6_addresses:
        ips = ''
        my_ipv6_addresses.sort()
        for e in my_ipv6_addresses:
            ips += e + '\n'
        if save_if_changed(SAVE_PATH, ips):
            time.sleep(conf.sleep_sec)
            alerts.send_dingtalk(conf.dingtalk_token, conf.dingtalk_secret,
                                 socket.gethostname() + '\n' + ips)
