pod-porter Templates
`````````````````````````````````````````````

pod-porter uses Jinja2_ templates to render the compose files.  The templates are stored in the `templates`
directory in the map.  The templates are rendered using the values from the ``values.yaml`` file.

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/service-mongo.yaml
   :language: jinja
   :caption: Example template for MongoDB service


.. literalinclude:: ./examples/structure/multi_map/mongo/templates/service-mongo-express.yaml
   :language: jinja
   :caption: Example template for MongoDB Express service

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/volumes-mongo.yaml
   :language: jinja
   :caption: Example template for MongoDB volumes

.. literalinclude:: ./examples/structure/multi_map/mongo/templates/volumes-mongo.yaml
   :language: jinja
   :caption: Example template for MongoDB volumes

.. literalinclude:: ./examples/structure/multi_map/mongo/maps/batfish/templates/service-batfish.yaml
   :language: jinja
   :caption: Example template for Batfish service

.. literalinclude:: ./examples/structure/multi_map/mongo/maps/batfish/templates/volumes-batfish.yaml
   :language: jinja
   :caption: Example template for Batfish volumes

Using these templates and the values from the ``values.yaml`` file, pod-porter will render the compose files.

.. code-block:: bash

   pod-porter write -n thing -m docs\source\directions\examples\structure\multi_map\mongo -o docs\source\directions\examples\structure\multi_map

.. literalinclude:: ./examples/structure/multi_map/thing-mongo-1.0.0.yaml
   :language: yaml
   :caption: Example rendered compose file for MongoDB service it names itself thing-mongo-1.0.0.yaml
