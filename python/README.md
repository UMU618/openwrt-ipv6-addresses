# openwrt-ipv6-addresses

## Requirements

Only tested on OpenWRT x86.

```bash
opkg install python
opkg install python-base
```

## Installation

config hotplug script by `vi /etc/hotplug.d/iface/99-ipv6-addresses`

```bash
[ "$ACTION" = ifup -o "$ACTION" = ifupdate ] || exit 0
[ "$ACTION" = ifupdate -a -z "$IFUPDATE_ADDRESSES" -a -z "$IFUPDATE_DATA" ] && exit 0

python index.py
logger -t ipv6-addresses "$ACTION of $INTERFACE ($DEVICE) $IFUPDATE_ADDRESSES, $IFUPDATE_DATA"
```
