#Tokens are smallest unit in program
#example
'''n=10
if n%2==0:
    print("even number")
else:
    print("odd number")'''#this all are tokens
    #types of tokens
    #from above program
'''
| Token | Type |
|---|---|
| `n` | Identifier (variable name) |
| `=` | Operator |
| `10` | Literal (integer value) |
| `if` | Keyword |
| `%` | Operator (remainder/modulus) |
| `2` | Literal |
| `==` | Operator (comparison) |
| `0` | Literal |
| `:` | Punctuator |
| `print` | Identifier / built-in function |
| `(` `)` | Punctuators |
| `"even number"` | Literal (string) |
| `else` | Keyword |
| `"odd number"` | Literal (string) |'''
#Token Type	Simple Meaning	Example
'''Keyword	:Python’s special reserved word	if, else, for
Identifier :	Name given by us	n, name, marks
Literal	:Fixed value	10, 2, "even number"
Operator:	Symbol that does work	=, %, ==, +
Punctuator	:Symbol that structures code	:, (, ), ,'''
'''import tokenize
from io import StringIO

code = '''
n = 10

if n % 2 == 0:
    print("even number")
else:
    print("odd number")
'''

for token in tokenize.generate_tokens(StringIO(code).readline):
    print(tokenize.tok_name[token.type], "->", repr(token.string))'''