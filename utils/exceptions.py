"""
MIT License

Copyright (c) 2022 TrueMyst

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class NoSpaceError(Exception):
    """
    An exception raised when there are no whitespaces in a certain string.
    """

    def __init__(self, text: str) -> None:
        self.text = text
        self.message = f'There were no spaces identified in the Variable\'s Value | Value: "{self.text}"'
        super().__init__(self.message)


class CharLengthShort(Exception):
    """
    An exception raised when the length of the a certain string doesn't match the length of the base string.
    """

    def __init__(self, cls, function, charLen: int) -> None:
        self.message = f"The 'char' received a very short length. The {cls}'s {function}: Requires a length of {charLen}."
        super().__init__(self.message)
