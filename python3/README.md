# openwrt-ipv6-addresses

## Requirements

Only tested on OpenWRT x86.

```bash
opkg install python3
opkg install python3-base
```

## Installation

config hotplug script by `vi /etc/hotplug.d/iface/99-ipv6-addresses`

```bash
[ "$ACTION" = ifup -o "$ACTION" = ifupdate ] || exit 0
[ "$ACTION" = ifupdate -a -z "$IFUPDATE_ADDRESSES" -a -z "$IFUPDATE_DATA" ] && exit 0

python3 index.py
logger -t ipv6-addresses "$ACTION of $INTERFACE ($DEVICE) $IFUPDATE_ADDRESSES, $IFUPDATE_DATA"
```

## References

[跟 UMU 一起玩 OpenWRT（入门篇16）：Python3](https://blog.umu618.com/2020/02/23/umutech-openwrt-primer-16-python3/)
