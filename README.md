<div align="center">
  <a href="https://github.com/MystYT-21/hashily">
    <img src="hashily/utils/Hashily Brand.png" alt="Hashily Logo" wdith = "300" height = "200">
  </a>
</div>

# hashily 0.0.1
![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)

hashily is a python module that performs a variety of text decoding and encoding functions. It also various functions for encrypting and decrypting text using various ciphers.

**PyPi:** https://pypi.org/project/hashily

**Docs:** Not have been made yet.

## `1` Installation 
You may use pip or a similar tool to install latest versions of hashily from the PyPi. To Install the Module - 

- Install the Stable Version: 
```cmd
pip install hashily
```
- Install the Beta Version:
```cmd
pip install git+https://github.com/MystYT-21/hashily.git
```
## `2` Usage 
To import the Module You can do like this - 
```py
>>> from hashily import *
```
### `2.1` Examples
```py
>>> from hashily import *

>>> print(Caesar.encode("Hey"))
Khb

>>> print(Caesar.decode("Khb, Krz duh brx?"))
Hey, How are you?

>>> print(Octal.encode("Good! You?")) 
107 157 157 144 41 40 131 157 165 77

>>> print(Octal.decode("111 40 141 155 40 147 157 157 144 40 164 157 157 40 72 51")) 
I am good too :)
```


## `3` Available Functions

The following functions are currently available:

| **ciphers** | **encoding** | **transform**|
| :--------   | :----------- | :----------- |
| ROT13       | Binary       | reverse      |
| AtBash      | Hexadecimal  | titlelize    |
| Bacon       | Octal        | password     |
| A1Z26       | Integer      | token        |
| Caesar      | UrlEncoding  | -            |
| MorseCode   | UnicodePoint | -            |
| -           | -            | -            |


## `4` Feedback

If you have any feedback, please reach out to us at our [Discord](https://discord.gg/NzR8CgvVwd)



