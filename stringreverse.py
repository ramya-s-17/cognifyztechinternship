Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
...     s = input("Enter a string (or type 'exit' to quit): ")
...     if s.lower() == 'exit':
...         break
...     print("Reversed string:", s[::-1])
