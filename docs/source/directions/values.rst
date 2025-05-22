pod-porter Values
`````````````````````````````````````````````

Just like in HELM_ the variable values are stored in a ``values.yaml``.  A values.yaml file is required, but it
can be empty.  There is no specific structure to it at this time.  The file **MUST** be named ``values.yaml``
and **MUST** be located in the root of the of the map for the 'default' values.  If you are rendering a map
the file can be called anything and located anywhere.

* The is a basic form of the values.yaml file.

.. literalinclude:: ./examples/structure/multi_map/mongo/values.yaml
   :language: yaml
   :caption: Example values.yaml

* The is a more complex form of the values.yaml file, that includes values for a sub map.

.. literalinclude:: ./examples/values-with-sub-maps.yaml
   :language: yaml
   :caption: Example values.yaml with Sub Map values

pod-porter Values Schema Validation
`````````````````````````````````````````````

Just like in HELM_ the ``values.yaml`` can use JSON schema validation.  Just create a file called ``values-schema.json``
in the root of the map where the ``values.yaml`` file is located.  The schema will be used to validate the
``values.yaml`` file.  You can reference how to create a JSON schema here `JSON Schema Docs`_.

.. literalinclude:: ./examples/values-schema-validation/values.yaml
   :language: yaml
   :caption: Example values.yaml with schema validation

.. literalinclude:: ./examples/values-schema-validation/values-schema.json
   :language: json
   :caption: Example values-schema.json for schema validation
