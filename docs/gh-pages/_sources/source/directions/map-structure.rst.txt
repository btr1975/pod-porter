pod-porter Map Structure
`````````````````````````````````````````````

* This is the basic structure of a pod-porter map.  This is what I expect most people to use.
  It is very similar to a HELM_ chart.


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
  Again it is very similar to a HELM_ chart.

.. code-block:: bash
   :caption: Multi Map Structure

   map-name
     |-> maps
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

   mogn
     |
     |-> templates
     |      |-> service-mongo.yaml
     |      |-> service-mongo-express.yaml
     |      |-> volumes-mongo.yaml
     |
     |-> Map.yaml
     |-> values.yaml
