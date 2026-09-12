Create CoAP service project skeleton
---------------------------------------

**gen_coap_service** is tool for creating CoAP service project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_coap_service python checker| |gen_coap_service python package| |gen_coap_service interface checker| |gen_coap_service isp checker| |gen_coap_service srp checker| |github issues| |documentation status| |github contributors|

.. |gen_coap_service python checker| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python_checker.yml

.. |gen_coap_service python package| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_package.yml

.. |gen_coap_service interface checker| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_interface_checker.yml

.. |gen_coap_service isp checker| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_isp_checker.yml

.. |gen_coap_service srp checker| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_srp_checker.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_coap_service.svg
   :target: https://github.com/vroncevic/gen_coap_service/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_coap_service.svg
   :target: https://github.com/vroncevic/gen_coap_service/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-coap-service/badge/?version=latest
   :target: https://gen-coap-service.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
-----------------

|gen_coap_service python3 build|

.. |gen_coap_service python3 build| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_coap_service/releases

To install **gen_coap_service** type the following

.. code-block:: bash

    tar xvzf gen_coap_service-x.y.z.tar.gz
    cd gen_coap_service-x.y.z/
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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_coap_service

📦 Dependencies
-----------------

**gen_coap_service** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-------------------

**gen_coap_service** is based on OOP.

Tool structure

.. code-block:: bash

    gen_coap_service/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_coap_service_command_definition.py
         │   │   ├── gen_coap_service_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_coap_service.cfg
         │   │   ├── gen_coap_service.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 44 files

✨ Features
-------------

* Automatically scaffolds CoAP service projects (coapthon, libcoap, node_coap).
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
------------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
----------

Install package

.. code-block:: bash

    pip3 install gen_coap_service

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_coap_service/main/main.py

Running tool for creating new CoAP service project

.. code-block:: bash

    python3 main.py create --name myapp --type coapthon --output ./demo/

📚 Docs
---------

More documentation and info at

* `gen_coap_service.readthedocs.io <https://gen-coap-service.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
-----------------

`Contributing to gen_coap_service <https://github.com/vroncevic/gen_coap_service/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
---------------------------

Copyright (C) 2025 - 2026 by `vroncevic.github.io/gen_coap_service <https://vroncevic.github.io/gen_coap_service>`_

**gen_coap_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
