<p align = "center"><img width="750" height="250" src="https://i.imgur.com/1uVjG7d.png"></p>
<p align = "center"><a href = "https://discord.gg/NzR8CgvVwd" target = "_blank"><img src = "https://discord.com/api/guilds/896273743318491157/embed.png"></a></p>

# hashily 0.0.6
![MIT License](https://img.shields.io/badge/License-MIT-blue) [![Downloads](https://static.pepy.tech/personalized-badge/hashily?period=month&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/hashily)

hashily is a python module that performs a variety of text decoding and encoding functions. It also various functions for encrypting and decrypting text using various ciphers.

**PyPi:** https://pypi.org/project/hashily

**Docs:** https://hashily.readthedocs.io/en/latest

## `0` Updates
- Added new function: `pigLatin`
- Changed `Integer` class's name to `ASCII`
- Bug Fixes



## `1` Installation 
You may use pip or a similar tool to install latest versions of hashily from the PyPi. To Install the Module - 

- Install the Stable Version: 
```cmd
# Linux/macOS
python3 -m pip install -U hashily

# Windows
py -3 -m pip install -U hashily
```
- Install the Beta Version:
```cmd
pip install git+https://github.com/MystYT-21/hashily.git
```
## `2` Usage 
To import the Module, you can do like this - 
```py
>>> import hashily
```
### `2.1` Examples
```py
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
```


## `3` Available Functions

The following functions are currently available:

| **Ciphers** | **Encoding** | **Transform**|
| :--------   | :----------- | :----------- |
| ROT13       | Binary       | reverse      |
| AtBash      | Hexadecimal  | titlelize    |
| Bacon       | Octal        | password     |
| A1Z26       | ASCII        | token        |
| Caesar      | UrlEncoding  | altCase      |
| MorseCode   | UnicodePoint | firstLetter  |
| -           | Base32       | pigLatin     |


## `4` Feedback

If you have any feedback, please reach out to us at our [Discord](https://discord.gg/NzR8CgvVwd)

## Show some love to these guys!
A special thanks to them; they helped me a lot throughout this entire project.

- [Co-Dev] [oliii](https://github.com/oliiiiiiiiiiiii)
- [Co-Dev] [Thuliumitation](https://github.com/Thuliumitation)


And if you are still reading this, I hope you have a wonderful day.

