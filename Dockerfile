# Copyright 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:10
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python \
    python-dev \
    python3 \
    python3-dev \
    libyaml-dev

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python2 get-pip.py
RUN python2 -m pip install --upgrade setuptools
RUN python2 -m pip install --upgrade pip
RUN python2 -m pip install --upgrade build
RUN rm -f get-pip.py
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade build
RUN rm -f get-pip.py
COPY requirements.txt /
RUN pip2 install -r requirements.txt
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN mkdir /gen_coap_service/
COPY gen_coap_service /gen_coap_service/
COPY setup.py /
COPY README.md /
RUN python2 setup.py install_lib
RUN python2 setup.py install_egg_info
RUN python2 setup.py install_data
RUN python3 setup.py install_lib
RUN python3 setup.py install_data
RUN python3 setup.py install_egg_info
RUN rm -rf /gen_coap_service/
RUN rm -f setup.py
RUN rm -f README.md

