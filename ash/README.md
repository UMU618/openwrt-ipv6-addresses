# openwrt-ipv6-addresses

DDNS

## Requirements

Tested on OpenWRT x86 and mipsel_24kc.

## Installation

```bash
cp expample.sh /etc/hotplug.d/iface/99-ipv6-addresses
```

If your `wget` is `uclient-fetch`:

- and you don't have multiple broadband lines, then you need to remove `--bind-address=$IP` in [expample.sh](expample.sh)

```bash
#readlink $(which wget)
/bin/uclient-fetch

# ll $(which wget)
lrwxrwxrwx    1 root     root            18 Jan 30 00:05 /usr/bin/wget -> /bin/uclient-fetch*
```

- and you have multiple broadband lines, then you need to `opkg install wget`.
