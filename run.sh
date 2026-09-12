#!/bin/bash
#
# @brief   gen_coap_service
# @version 1.1.8
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "atsystem" --type "coapthon" --output "./demo_coapthon"
python3 main.py create --name "atsystem" --type "libcoap" --output "./demo_libcoap"
python3 main.py create --name "atsystem" --type "node_coap" --output "./demo_node_coap"
