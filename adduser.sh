#!/bin/bash

export MENU_OPTION="1"
export CLIENT=$1
export PASS="1"

./openvpn-install.sh >/dev/null
exit
