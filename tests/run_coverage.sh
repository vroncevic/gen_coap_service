#!/bin/bash
#
# @brief   gen_coap_service
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2020
# @company None, free software to use 2020
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf simple_project/ coap_client/ coap_server/ client.py server.py
python3 -m coverage run -m --source=../gen_coap_service unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
