[ "$ACTION" = ifup -o "$ACTION" = ifupdate ] || exit 0
[ "$ACTION" = ifupdate -a -z "$IFUPDATE_ADDRESSES" -a -z "$IFUPDATE_DATA" ] && exit 0

case $DEVICE in
  pppoe-wan)
    zone=* # modify here
    token=* # modify here
    ;;
  # pppoe-wan2) modify here if you have more broadband lines
  *)
    exit 0
    ;;
esac

IP=$(ip -6 address show $DEVICE scope global | grep -v ' fd' | sed -n 's/.*inet6 \([0-9a-f:]\+\).*/\1/p' | head -n 1)
[ -z $IP ] && exit 0
(sleep 6; wget -O- -q --bind-address=$IP "https://dynv6.com/api/update?zone=$zone&ipv6=$IP&token=$token") &
