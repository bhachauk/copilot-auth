Copilot Authentication
-------------------

A Helper library to get the copilot authentication token.


Prerequisite
------------

Python environment

- python>=3.13


.. code-block:: text

    pip install requests



Installation
------------

.. code-block::

    pip install copilot-auth


Getting started
--------------------

**Steps to fetch copilot github token :**

- Fetch Github Access token using device flow
- Fetch Copilot Github token using Github Access token


.. code-block::

    import copilot_auth as ca

    # Custom token handler to process the token
    def token_handler(token):
        print(token)

    # Fetch the github access token
    ca.authenticate_github_token([token_handler])

    # Fetch the copilot token
    ca.authenticate_copilot_token([token_handler])