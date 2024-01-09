
<h3 align = "center">
	<img width="750" height="250" src="https://i.imgur.com/1uVjG7d.png"><br>
</h3>

<p align="center">🍀 <b>hashily</b> is a utility tool that helps to performs a variety of text decoding and encoding functions. It also has various functions for encrypting and decrypting text using various ciphers</p>

<p align="center">
	<img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-Yes-%23d8dfe6?style=for-the-badge&logo=undertale&logoColor=%23d8dfe6&labelColor=%23094a97">
	<a href="https://www.pepy.tech/projects/hashily"><img alt="Pepy Total Downlods" src="https://img.shields.io/pepy/dt/hashily?style=for-the-badge&logo=9gag&logoColor=%23d8dfe6&labelColor=%23094a97&color=%23d8dfe6"></a>
	<a href="https://pypi.org/project/hashily/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/hashily?style=for-the-badge&logo=python&logoColor=%23d8dfe6&labelColor=%23094a97&color=%23d8dfe6"></a>
	<img alt="GitHub License" src="https://img.shields.io/github/license/TrueMyst/hashily?style=for-the-badge&logo=gitbook&logoColor=%23d8dfe6&labelColor=%23094a97&color=%23d8dfe6">
</p>


## 📦 Installation 
You may use pip or a similar tool to install latest versions of hashily from the PyPi. To Install the package - 

- Install the Stable Version: 
```bash
# Linux/macOS
python3 -m pip install -U hashily

# Windows
py -3 -m pip install -U hashily
```
- Install the Beta Version:
```bash
pip install git+https://github.com/TrueMyst/hashily.git
```
## 🤌 How to use? 
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

>>> print(hashily.pigLatin("Waiting for the day when pigs can fly"))
'aitingWay orfay hetay ayday henway igspay ancay lyfay'

>>> print(hashily.token())
'm3JDblPCETFyLYGGn6EdbGaIlnKk3Fq2c60wYQHHE57LC5eh'
```

For more information feel free to checkout the [**Documentation**]( https://hashily.readthedocs.io/en/latest), might come handy :)


## 🤗 Contributing

Contributions to **Hashily** are welcomed. Feel free to submit your suggestions via pull requests. Your contributions are invaluable in enhancing this tool for everyone.

## 💜 Special thanks 
A special thanks to them; they helped me a lot throughout this entire project [oliii](https://github.com/oliiiiiiiiiiiii) &  [Thuliumitation](https://github.com/Thuliumitation)


## 📋 License
🍀 **hashily** is licensed under the MIT license, which you can find in the LICENSE file.

<br>

<p align="center">
Made with 💜<br>
<b>elysianmyst, 2024</b>
</p>
