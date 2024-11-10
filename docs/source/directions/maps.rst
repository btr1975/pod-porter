pod-porter Maps
`````````````````````````````````````````````

Just like in HELM_ the "Helmsman" uses "Charts", in pod-porter a "Porter" uses "Maps". A map is a required file.
Also it's structure is required.  The file **MUST** be named `Map.yaml` and **MUST** be located in the root of the
of the map.



.. list-table:: Map Structure
   :widths: 10 90 90
   :header-rows: 1

   * - Key
     - Description
     - Required
   * - api_version
     - The API version of the map (Currently only supports v1)
     - Yes
   * - name
     - The name of the map
     - Yes
   * - description
     - The description of the map
     - Yes
   * - version
     - The version of the map
     - Yes
   * - app_version
     - The application version the map is for
     - Yes

.. literalinclude:: ./examples/structure/multi_map/mongo/Map.yaml
   :language: yaml
   :caption: Example Map.yaml
