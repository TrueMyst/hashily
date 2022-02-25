Hashily | Documentation
==================================

``1`` Overview
-----------------

``Hashily`` is a Python module that performs a variety of text decoding and encoding functions. It also has various functions for encrypting and decrypting text using various ciphers.

.. warning::

   This module requires Python 3.6 or above to work properly.

Hashily is designed to be simple and easy to use. The functions are really easy, however if you need more information, check out the documentation here!

``2`` Installation
------------------
You may use pip or a similar tool to install latest versions of hashily from the PyPi. To Install the Module:

- Install the Stable Version: 

.. code-block::
   
   # Linux/macOS
   python3 -m pip install -U hashily

   # Windows
   py -3 -m pip install -U hashily


- Install the Beta Version:

.. code-block::

   $ git clone https://github.com/TrueMyst/hashily

``3`` Basic Usage
-----------------
To import the Module, you can do like this - 

.. code-block:: python

   >>> import hashily

``3.1`` Examples
~~~~~~~~~~~~~~~~

.. code-block:: python 

   >>> import hashily

   # Use the .encode() function to Encode the Text
   >>> print(hashily.Caesar.encode("Hey"))
   'Khb'

   # Use the .decode() function to Decode the Text
   >>> print(hashily.Caesar.decode("Khb, Krz duh brx?"))
   'Hey, How are you?'

   >>> print(hashily.Octal.encode("Good! You?")) 
   '107 157 157 144 41 40 131 157 165 77'

   >>> print(hashily.Octal.decode("111 40 141 155 40 147 157 157 144 40 164 157 157 40 72 51")) 
   'I am good too :)'


``4`` Documentation
-------------------
.. toctree::
   :maxdepth: 1
   :caption: Tables of Content 🧾

   ./ciphers
   ./encoding
   ./transform


``5`` Misc 
----------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

