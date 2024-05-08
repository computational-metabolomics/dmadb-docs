.. _dma-galaxy-workflow-docs:
Galaxy
##########

`dmadb.bham.ac.uk/galaxy/ <https://dmadb.bham.ac.uk/galaxy/>`_

DMA Galaxy Workflow
******************************************

Details of the DMA Galaxy workflow....









Galaxy interactions (Admin only)
******************************************

Register Galaxy instance (Admin only)
''''''''''''''''''''''''''''''''''''''''''''''''''

A Galaxy instance needs to be registered before any of the django-galaxy functionality can be used. The Galaxy
instance should be accessible directly (or via symbolic link) on the file system that is running the Django instance.

.. figure:: images/galaxy1.png

Register Galaxy user (Admin only)
''''''''''''''''''''''''''''''''''''''''''''''''''
Each admin user can be registered to any of the registered Galaxy instance. The API key that has is
provided by the user allows permission of the Galaxy instance API to be used.

.. figure:: images/galaxy2.png

Upload ISA projects to Galaxy data library (Admin only)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''
If a ISA project has be created and data has been uploaded into an assay. This data can be uploaded into the Galaxy
Data libraries. If the Galaxy instance is on the same file system (or accessible by a symbolic link) then the files
can be uploaded as symbolic links. This is useful if there is limited space available for Galaxy instance. 

.. figure:: images/galaxy3.png

Run Workflows (Admin only)
''''''''''''''''''''''''''''''''''''''''''''''''''
All workflows for each Galaxy instances can be synced with Django file system so they can be run directly from the django
interface. In cases where there are multiple file inputs and paramaters this is not practical and not advised.

.. figure:: images/galaxy4.png



View Galaxy histories (Admin only)
''''''''''''''''''''''''''''''''''''''''''''''''''
All histories for each Galaxy instances are summarised.

.. figure:: images/galaxy6.png




