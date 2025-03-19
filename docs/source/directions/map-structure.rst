pod-porter Map Structure
`````````````````````````````````````````````

* This is the basic structure of a pod-porter map.  This is what I expect most people will use.
  It is very similar to a HELM_ chart.  It is a top level map with no sub maps.


.. code-block:: bash
   :caption: Basic Map Structure

   map-name
     |-> templates
     |      |-> template1.yaml
     |      |-> template2.yaml
     |
     |-> Map.yaml
     |-> values.yaml

* This is the multi map structure of a pod-porter map.  Yes you can have child maps.
  Again it is very similar to a HELM_ chart. This map has 2 sub maps. One called map-name-2 which is not packaged,
  and one packaged map called map-name-0.1.0.tar.gz.  A packaged map will be unpacked and the contents will be
  placed in the maps directory.

.. code-block:: bash
   :caption: Multi Map Structure

   map-name
     |-> maps
     |      |-> map-name-0.1.0.tar.gz
     |      |-> map-name-2
     |              |-> templates
     |              |      |-> template1.yaml
     |              |      |-> template2.yaml
     |              |
     |              |-> Map.yaml
     |              |-> values.yaml
     |
     |-> templates
     |      |-> template1.yaml
     |      |-> template2.yaml
     |
     |-> Map.yaml
     |-> values.yaml


.. code-block:: bash
   :caption: Example map of a MongoDB and MongoDB-Express Deployment

   mongo
     |
     |-> templates
     |      |-> service-mongo.yaml
     |      |-> service-mongo-express.yaml
     |      |-> volumes-mongo.yaml
     |
     |-> Map.yaml
     |-> values.yaml
