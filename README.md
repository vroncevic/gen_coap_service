<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/gen_coap_service_logo.png" width="25%">

# Generate CoAP modules

☯️ **gen_coap_service** is tool for generation of CoAP modules.

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_coap_service python checker](https://img.shields.io/github/workflow/status/vroncevic/gen_coap_service/gen_coap_service_python_checker?style=flat&label=gen_coap_service%20python%20checker)](https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python_checker.yml) [![gen_coap_service package checker](https://img.shields.io/github/workflow/status/vroncevic/gen_coap_service/gen_coap_service_package_checker?style=flat&label=gen_coap_service%20package%20checker)](https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_coap_service.svg)](https://github.com/vroncevic/gen_coap_service/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_coap_service.svg)](https://github.com/vroncevic/gen_coap_service/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of py module](#generation-flow-of-py-module)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/debtux.png)

[![gen_coap_service python2 build](https://img.shields.io/github/workflow/status/vroncevic/gen_coap_service/gen_coap_service_python2_build?style=flat&label=gen_coap_service%20python2%20build)](https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python2_build.yml) [![gen_coap_service python3 build](https://img.shields.io/github/workflow/status/vroncevic/gen_coap_service/gen_coap_service_python3_build?style=flat&label=gen_coap_service%20python3%20build)](https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python 📦 is located at **[pypi.org](https://pypi.org/project/gen_coap_service/)**.

You can install by using pip

```bash
# python2
pip2 install gen_coap_service
# python3
pip3 install gen_coap_service
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_coap_service/releases/)** download and extract release archive 📦.

To install **gen_coap_service** 📦 type the following

```bash
tar xvzf gen_coap_service-x.y.z.tar.gz
cd gen_coap_service-x.y.z/
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py 
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install ./dist/gen_coap_service-*-py2-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_coap_service_run.py
ln -s /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_coap_service_run.py /usr/local/bin/gen_coap_service_run.py
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_coap_service-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_coap_service_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_coap_service_run.py /usr/local/bin/gen_coap_service_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_coap_service/releases)** download and extract release archive 📦.

To install **gen_coap_service** 📦 locate and run setup.py with arguments

```bash
tar xvzf gen_coap_service-x.y.z.tar.gz
cd gen_coap_service-x.y.z
# python2
pip2 install -r requirements.txt
python2 setup.py install_lib
python2 setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container 🚢.

[![gen_coap_service docker checker](https://img.shields.io/github/workflow/status/vroncevic/gen_coap_service/gen_coap_service_docker_checker?style=flat&label=gen_coap_service%20docker%20checker)](https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_docker_checker.yml)

### Dependencies

**gen_coap_service** requires next modules and libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_coap_service)

### Generation flow of py module

Base flow of generation process

![CoAP generation flow](https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/gen_coap_service_flow.png)

### Tool structure

**gen_coap_service** is based on OOP.

🧰 Generator structure

```bash
gen_coap_service/
├── conf/
│   ├── gen_coap_service.cfg
│   ├── gen_coap_service.logo
│   ├── gen_coap_service_utils.cfg
│   ├── project.yaml
│   └── template/
│       ├── coapthon/
│       │   ├── basic/
│       │   ├── basic_resources.template
│       │   ├── coap_client.template
│       │   ├── coap_server.template
│       │   └── logging.template
│       ├── libcoap/
│       │   ├── coap_client/
│       │   │   ├── AUTHORS
│       │   │   ├── autogen.sh
│       │   │   ├── build/
│       │   │   ├── ChangeLog
│       │   │   ├── configure.ac
│       │   │   ├── INSTALL
│       │   │   ├── Makefile.am
│       │   │   ├── NEWS
│       │   │   ├── README.md
│       │   │   └── src/
│       │   │       ├── client_api.h
│       │   │       ├── main.c
│       │   │       ├── Makefile.am
│       │   │       ├── print_error.c
│       │   │       ├── print_success.c
│       │   │       ├── print_usage.c
│       │   │       ├── print_verbose.c
│       │   │       ├── process_options.c
│       │   │       └── time_handler.c
│       │   └── coap_server/
│       │       ├── AUTHORS
│       │       ├── autogen.sh
│       │       ├── build/
│       │       ├── ChangeLog
│       │       ├── configure.ac
│       │       ├── INSTALL
│       │       ├── Makefile.am
│       │       ├── NEWS
│       │       ├── README.md
│       │       └── src/
│       │           ├── get_date.c
│       │           ├── get_full.c
│       │           ├── get_time.c
│       │           ├── main.c
│       │           ├── Makefile.am
│       │           ├── server_api.h
│       │           └── time_handler.c
│       ├── node_coap/
│       │   ├── client.template
│       │   └── server.template
│       ├── rpi_pico_coap/
│       ├── template_coapthon.yaml
│       ├── template_libcoap.yaml
│       ├── template_node_coap.yaml
│       └── template_rpi_pico_coap.yaml
├── __init__.py
├── log/
│   └── gen_coap_service.log
├── pro/
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_coap_service_run.py

16 directories, 52 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_coap_service/badge/?version=latest)](https://gen_coap_service.readthedocs.io/projects/gen_coap_service/en/latest/?badge=latest)

📗 More documentation and info at

- [gen_coap_service.readthedocs.io](https://gen_coap_service.readthedocs.io/en/latest/)
- [CoAP Service](overview.md)
- [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to gen_coap_service](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 by [vroncevic.github.io/gen_coap_service](https://vroncevic.github.io/gen_coap_service)

**gen_coap_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
