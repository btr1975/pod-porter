pod-porter Values
`````````````````````````````````````````````
Just like in HELM_ the variable values are stored in a values.yaml.  A values.yaml file is required, but it
can be empty.  There is no specific structure to it at this time.  The file **MUST** be named `values.yaml`
and **MUST** be located in the root of the of the map.

.. literalinclude:: ./examples/structure/multi_map/mongo/values.yaml
   :language: yaml
   :caption: Example values.yaml
