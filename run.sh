#!/bin/bash
#

python3 main.py create --name "atsystem" --type "coapthon" --output "./demo_coapthon"
python3 main.py create --name "atsystem" --type "libcoap" --output "./demo_libcoap"
python3 main.py create --name "atsystem" --type "node_coap" --output "./demo_node_coap"
