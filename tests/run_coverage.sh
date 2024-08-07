#!/bin/bash
#
# @brief   gen_coap_service
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2020
# @company None, free software to use 2020
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_coap_service_coverage.xml gen_coap_service_coverage.json .coverage
rm -rf simple_project/ coap_client/ coap_server/ client.py server.py
ats_coverage_run.py -n gen_coap_service -p ../README.md
rm -rf simple_project/ coap_client/ coap_server/ client.py server.py
python3 -m coverage run -m --source=../gen_coap_service unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_coap_service_coverage.xml 
python3 -m coverage json -o gen_coap_service_coverage.json
python3 -m coverage report --format=markdown -m
