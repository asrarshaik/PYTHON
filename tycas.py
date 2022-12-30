>>>float(10)
10.0
>>>float(10+5j)
TypeError:cant convert complex to int
>>>int(True)
1
>>>int(False)
0
>>>int("10")
10
>>>int("10.5")
ValueError:invalid literal for int()with base 10:'10.5'
>>>int("ten")
ValueError:invalid literal for int()with base 10:'ten'
>>>intl("0B1111")
ValueError:invalid literal for int()with base 10:0B1111
x=[10,20,30,40]
  b = bytes(x)
  type(b)
