Flask Mongo Login Framework
===========================

Description
-----------

I got tired of trying to find a lightweight way to establish a login system, so I built one out of Flask, MongoDB, MongoEngine, Flask-Login, and WTForms.

Requirements
------------

Requirements.txt coming soon!

Settings
--------

It requires an app/config.py file with the following settings:

```python
CSRF_ENABLED = True

MONGODB_SETTINGS = {'DB': 'your-db-here'}
```

the file is in the .gitignore file again so that contributors can have their own settings.

Needs
-----

The biggest need I have at the moment is figuring out how to make it more secure. I'm learning as I go with this, so we will see. Any recommendations would be appreciated.

Items on the list:
1. Encrypt passwords
2. Make sessions more secure by storing an encrypted value of the username+password, or something to that effect