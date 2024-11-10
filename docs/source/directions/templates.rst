pod-porter Templates
`````````````````````````````````````````````

pod-porter uses Jinja2_ templates to render the compose files.  The templates are stored in the `templates`
directory in the map.  The templates are rendered using the values from the `values.yaml` file.

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/service-mongo.yaml
   :language: jinja
   :caption: Example template for MongoDB service


.. literalinclude:: ./examples/structure/multi_map/mongo/templates/service-mongo-express.yaml
   :language: jinja
   :caption: Example template for MongoDB Express service

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/volumes-mongo.yaml
   :language: jinja
   :caption: Example template for MongoDB volumes

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/secrets.yaml
   :language: jinja
   :caption: Example template for MongoDB secrets
