Generates CoAP modules
-----------------------

**gen_coap_service** is tool for generation of CoAP modules.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_coap_service python checker| |gen_coap_service python package| |github issues| |documentation status| |github contributors|

.. |gen_coap_service python checker| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python_checker.yml

.. |gen_coap_service python package| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_package.yml

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

Installation
-------------

|gen_coap_service python3 build|

.. |gen_coap_service python3 build| image:: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_coap_service/actions/workflows/gen_coap_service_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_coap_service/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen-coap-service-x.y.z.tar.gz
    cd gen-coap-service-x.y.z/
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
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_coap_service_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_coap_service_run.py /usr/local/bin/gen_coap_service_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_coap_service

Dependencies
-------------

**gen_coap_service** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_coap_service** is based on OOP

Code structure

.. code-block:: bash

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
           │       │   │   ├── autogen.template
           │       │   │   ├── build/
           │       │   │   │   └── editorconfig.template
           │       │   │   ├── configure.template
           │       │   │   ├── Makefile.template
           │       │   │   ├── README.template
           │       │   │   └── src/
           │       │   │       ├── client_api.template
           │       │   │       ├── main.template
           │       │   │       ├── Makefile.template
           │       │   │       ├── print_error.template
           │       │   │       ├── print_success.template
           │       │   │       ├── print_usage.template
           │       │   │       ├── print_verbose.template
           │       │   │       ├── process_options.template
           │       │   │       └── time_handler.template
           │       │   └── coap_server/
           │       │       ├── autogen.template
           │       │       ├── build/
           │       │       │   └── editorconfig.template
           │       │       ├── configure.template
           │       │       ├── Makefile.template
           │       │       ├── README.template
           │       │       └── src/
           │       │           ├── get_date.template
           │       │           ├── get_full.template
           │       │           ├── get_time.template
           │       │           ├── main.template
           │       │           ├── Makefile.template
           │       │           ├── server_api.template
           │       │           └── time_handler.template
           │       ├── node_coap/
           │       │   ├── client.template
           │       │   └── server.template
           │       ├── template_coapthon.yaml
           │       ├── template_libcoap.yaml
           │       └── template_node_coap.yaml
           ├── __init__.py
           ├── log/
           │   └── gen_coap_service.log
           ├── pro/
           │   ├── __init__.py
           │   ├── read_template.py
           │   └── write_template.py
           ├── py.typed
           └── run/
               └── gen_coap_service_run.py
    
    16 directories, 46 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2024 by `vroncevic.github.io/gen_coap_service <https://vroncevic.github.io/gen_coap_service>`_

**gen_coap_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
