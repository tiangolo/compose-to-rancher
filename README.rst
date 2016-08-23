Compose to Rancher
==================

Convert Docker Compose V2 `docker-compose.yml` to a Rancher compatible Docker Compose V1 file, by default in `docker-compose-v1.yml`.

----

* Install:

.. code-block:: bash

  pip install compose-to-rancher

* You would have a command:

.. code-block:: bash

  compose-to-rancher

* You just have to run that command in a directory with a Docker Compose V2 file `docker-compose.yml` and it will generate a Rancher compatible Docker Compose V1 file `docker-compose-v1.yml`

* If you want to customize the you can see the command help:

.. code-block::

  $ compose-to-rancher --help
  
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
