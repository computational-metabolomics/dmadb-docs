.. _installation:

Installation
========================================
.. role:: bash(code)
   :language: bash



Logging into DMAdb
''''''''''''''''''''''''''''''''''''''''''''''''''

Access via Google account or request access here ... todo - need to add screenshots


Running the locally
''''''''''''''''''''''''''''''''''''''''''''''''''

The following `project site <https://github.com/computational-metabolomics/django-mogisite>`_ can also
be used as a standard Django project. See below:

1. Optionally create virtual environment with venv or conda (e.g. :bash:`conda create -n mogi python=3.6.5`)

2. The functionality for the MOGI applications has been tested using MySQL and SQLite databases, however MySQL or MariaDB is the
   preferred database backend to use. Please ensure either mysqlclient is installed (e.g. :bash:`conda install mysqlcient`)  if
   using the MySQL backend.

3. :bash:`pip install django-mogi`

4. :bash:`git clone https://github.com/computational-metabolomics/django-mogisite`

5. :bash:`cd django-mogisite`

6. :bash:`python manage.py migrate` to create the mogi models.

7. Start the development server and visit http://127.0.0.1:8000/

8. Register http://127.0.0.1:8000/register/ and login http://127.0.0.1:8000/login/

If using outside of the docker, to get the full functionality you will need install and configure the messaging broker
**rabbitmq** and the result backend **redis** for the distributed task queue system **Celery**.

1. Celery should be installed alongside the mogi python packages but can also just be installed via via pip
   or conda e.g.:bash:`pip install celery` or :bash:`conda install celery`

2. Install erlang (required for rabbitmq) :bash:`sudo apt-get install -y erlang`

3. Install rabbitmq :bash:`sudo apt-get install rabbitmq-server`

4. Add user (needs to match to settings.py file) :bash:`sudo rabbitmqctl add_user admin mypass`

5. Add host (needs to match to settings.py file) :bash:`sudo rabbitmqctl add_vhost myvhost`

6. Add tags (optional) :bash:`sudo rabbitmqctl set_user_tags myuser mytag`

7. Give permission to user :bash:`sudo rabbitmqctl set_permissions -p myvhost admin ".*" ".*" ".*"`

8. Restart rabbitmq :bash:`sudo service rabbitmq-server restart`

9. Install redis (easiest way is through conda) :bash:`conda install redis-py`

10. Start redis (if not already started) :bash:`redis-server`

11. Finally, start celery from the django-mogisite directory :bash:`celery -A mogi_site.celery worker -l DEBUG -E`

Different backends can be used with Celery and should still be compatible with the applications. See the
`celery documentation <http://docs.celeryproject.org/en/latest/>`_  for more details.

Incorporating  the packages into existing projects
''''''''''''''''''''''''''''''''''''''''''''''''''
Alternatively, individual applications can be installed into existing Django projects as well, see the
**quick start** section of the documentation for each Django application.
