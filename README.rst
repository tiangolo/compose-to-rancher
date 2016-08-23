Compose to Rancher
==================

Convert Docker Compose V2 `docker-compose.yml` to a Rancher compatible Docker Compose V1 file, by default in `docker-compose-v1.yml`.

---

* Install:

.. code-block:: bash

  pip install compose-to-rancher

.. ::

* Help:

.. code-block::

  usage: compose-to-rancher [-h] [-f FILE] [-o OUTPUT]

  Convert a docker-compose.yml file version 2 to a docker-compose-v1.yml version
  1, compatible with Rancher

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  the input docker-compose.yml file in version 2
                          (default: docker-compose.yml)
    -o OUTPUT, --output OUTPUT
                          the output to write a docker-compose.yml version 1
                          compatible with Rancher (default: docker-
                          compose-v1.yml)


.. ::
