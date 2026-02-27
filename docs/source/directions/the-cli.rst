pod-porter CLI
`````````````````````````````````````````````

* The pod-porter cli works like any other Unix/Linux command line tool.

pod-porter CLI Help
~~~~~~~~~~~~~~~~~~~~~

* This is just help for the CLI, it will show you the commands you can run.

.. code-block:: bash
   :caption: Example "pod-porter -h" output

   usage: pod-porter [-h] {template,write,package,un-package,create,validate-compose,validate-values} ...

   pod-porter version: 1.0.0

   options:
     -h, --help            show this help message and exit

   commands:
     Valid commands: a single command is required

     {template,write,package,un-package,create,validate-compose,validate-values}
                           CLI Help
       template            View the rendered compose file
       write               Write the rendered compose file
       package             Package the map (tar.gz) the map
       un-package          Un-Package the map extract (tar.gz)
       create              Create a new map, with some examples
       validate-compose    Validate a compose file
       validate-values     Validate a values file against a schema

pod-porter CLI template command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The template command will render the map with the values from the values.yaml file.

.. code-block:: bash
   :caption: Example "pod-porter template -h" output

   usage: pod-porter template [-h] -n NAME -m MAP [-f FILE_VALUES]

   options:
     -h, --help            show this help message and exit
     -n NAME, --name NAME  Release name
     -m MAP, --map MAP     Path to the map
     -f FILE_VALUES, --file-values FILE_VALUES
                           Path to the values you want to use instead of the map values

pod-porter CLI write command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The write command will render the map with the values from the values.yaml file, and write it to
  a directory.

..  warning::

   pod-porter is opinionated about the name of the file, so you only need to provide the directory
   where you want to write the file.

.. code-block:: bash
   :caption: Example "pod-porter write -h" output

   usage: pod-porter write [-h] -n NAME -m MAP [-f FILE_VALUES] -o OUTPUT

   options:
     -h, --help            show this help message and exit
     -n NAME, --name NAME  Release name
     -m MAP, --map MAP     Path to the map
     -f FILE_VALUES, --file-values FILE_VALUES
                           Path to the values you want to use instead of the map values
     -o OUTPUT, --output OUTPUT
                           Path to output file/files

pod-porter CLI package command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The package command will tar.gz the map in a named tar.gz.

..  warning::

   pod-porter is opinionated about the name of the tar.gz, so you only need to provide the directory
   where you want to write the file.

.. code-block:: bash
   :caption: Example "pod-porter package -h" output

   usage: pod-porter package [-h] -m MAP -o OUTPUT
   
   options:
     -h, --help            show this help message and exit
     -m MAP, --map MAP     Path to the map
     -o OUTPUT, --output OUTPUT
                           Path to output file/files

pod-porter CLI un-package command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The un-package command will extract the tar.gz the map in a named tar.gz.

.. code-block:: bash
   :caption: Example "pod-porter un-package -h" output

   usage: pod-porter un-package [-h] -m MAP -o OUTPUT

   options:
     -h, --help            show this help message and exit
     -m MAP, --map MAP     Path to the map
     -o OUTPUT, --output OUTPUT
                           Path to output file/files

pod-porter CLI create command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The create command will create a new map with some examples.

.. code-block:: bash
   :caption: Example "pod-porter create -h" output

   usage: pod-porter create [-h] -m MAP
   
   options:
     -h, --help         show this help message and exit
     -m MAP, --map MAP  Path to the map


pod-porter CLI validate-compose command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The create command will create a new map with some examples.

.. code-block:: bash
   :caption: Example "pod-porter validate-compose -h" output

   usage: pod-porter validate-compose [-h] -f FILE

   options:
     -h, --help       show this help message and exit
     -f, --file FILE  Path to the compose file


pod-porter CLI validate-values command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The create command will create a new map with some examples.

.. code-block:: bash
   :caption: Example "pod-porter validate-values -h" output

   usage: pod-porter validate-values [-h] -f FILE -s SCHEMA

   options:
     -h, --help            show this help message and exit
     -f FILE, --file FILE  Path to the values file
     -s SCHEMA, --schema SCHEMA
                           Path to the values-schema.json
