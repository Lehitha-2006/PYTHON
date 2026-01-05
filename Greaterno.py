Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("i love pyhton")
i love pyhton
x=int(input("enter a value: "))
enter a value: 5
if(x>5):
    print("Greater:)
          
SyntaxError: unterminated string literal (detected at line 2)
else:
    
SyntaxError: invalid syntax
if(x>5):
    print("Greater")
else:
    print("smaller")

...     
smaller

>>> if(x>5):
...     print("Greater:)
...           
... SyntaxError: unterminated string literal (detected at line 2)
... else:
...     
... SyntaxError: invalid syntax
... if(x>5):
...     print("Greater")
... else:
...     print("smaller")
... 
...     
... smaller
... x=int(input("enter a value: "))
... enter a value: 5
... if(x>5):
...     print("Greater")
...     
SyntaxError: unterminated string literal (detected at line 2)
>>> x=int(input("enter a value: "))
... enter a value:4
SyntaxError: multiple statements found while compiling a single statement
>>> x=int(input("enter a value: "))
enter a value: 4
>>> if(x>5):
...     printf("Greater")
...     else:
...         
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>> if(x>5):
...     printf("Greater")
... else:
...     printf("Smaller")
... 
...     
Traceback (most recent call last):
  File "<pyshell#20>", line 4, in <module>
    printf("Smaller")
NameError: name 'printf' is not defined. Did you mean: 'print'?
