=====
Depo_Credentials
=====

Depo_Credentials is the official credential module for the Depo application.  It allows you to 
store credentials encrypted in the database using [#f1]_fernet encryption

[1] ..[fernet] `fernet fields`
.. _fernet fields link: https://django-fernet-fields.readthedocs.io/en/latest/


Quick start
-----------

1. Install depo_credentials using pip, like this::
    pip install depo_credentials
    
2. Add "depo_credentials" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'depo_credentials',
    ]

3. Run `python manage.py migrate` to create the depo_credentials models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).
   
5. You should now see a new section on the admin page.