.. _user-docs:

User docs
###########

DMAdb introduction
********************

The DMAdb site, is a web application that has been created as a way to both aid in organising, analysing and dissimentating the metabolite annotations, mass spectrometry datasets and experimental meta information on "Deep metabolome annotation" (DMA) projects. 

DMA projects consist of large scale attempts to annotate as many compounds as possible in representative sample of an organism (e.g. Daphnia magna) or a sample type of an organism. This is achieved by performing multiple physio-chemical separations (e.g. Solid Phase Extraction, Liquid Chromatography, Liquid Chromatography fractionations) and extensive mass spectrometry analysis (including multi-stage fragmentation).

Once logged in, a user can browse and search the metabolomics datasets, view the ISA details of the datasets, and view and search the metabolite annotations. 

Admin users have the ability to perform additional tasks (like interfacing with Galaxy, creating new ISA projects and uploading data and annotations).

The DMAdb site is built of from three Django applications, which are designed to be used together to provide a comprehensive solution for managing and analysing metabolomics data. The Django applications are: django-mogi, django-galaxy and django-gfiles.

Note that the data present in the current iteration of the DMAdb site is currently only derived from the Deep Metabolome Annotation of Daphnia magna.



DMAdb user guide
********************
.. toctree::
   :maxdepth: 2

   Getting started <getting-started.rst>
   ISA details <misa.rst>
   Galaxy <dma-galaxy-workflow.rst>
   Data & results <mbrowse.rst>
   Running locally <local.rst>

|  <hr>

API
********************

django-mogi
============================

Metabolome Organisation with Galaxy and ISA (imports all of the django-applications within the Django MOGI application suite)

.. toctree::
   :maxdepth: 2

   API - django-mogi <django-mogi/index.rst>


django-galaxy
============================

Django interfacing with Galaxy. Backend using the bioblend API.

.. toctree::
   :maxdepth: 2

   API - django-galaxy  <django-galaxy/index.rst>


django-gfiles
============================

Simple file management for generic files in Django

.. toctree::
   :maxdepth: 2

   API - django-gfiles <django-gfiles/index.rst>


About
*******

.. toctree::

   Contacts  <contacts.rst>


