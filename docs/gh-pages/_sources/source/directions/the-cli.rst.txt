pod-porter CLI
`````````````````````````````````````````````

* The pod-porter cli works like any other Unix/Linux command line tool.


.. code-block:: bash
   :caption: Example "pod-porter -h" output

   usage: pod-porter [-h] {template,write} ...

   pod-porter version: 0.1.0

   options:
     -h, --help        show this help message and exit

   commands:
     Valid commands: a single command is required

     {template,write}  CLI Help
       template        View the rendered compose file
       write           Write the rendered compose file


.. code-block:: bash
   :caption: Example "pod-porter template -h" output

   usage: pod-porter template [-h] -n NAME -m MAP [-f FILE_VALUES]

   options:
     -h, --help            show this help message and exit
     -n NAME, --name NAME  Release name
     -m MAP, --map MAP     Path to the map
     -f FILE_VALUES, --file-values FILE_VALUES
                           Path to the values you want to use instead of the map values

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
                           Path to output file
