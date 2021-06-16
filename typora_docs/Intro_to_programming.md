# THE BASICS



### LITERALS

The **Literal** is any notation that represents fixed values in source code.

​		Example							Literal

```ruby 
'string!'		    # String
357					# Integer
3.141528			# Float
true				# Boolean
{ 'a' => 1}			# Hash
[1, 2, 3]			# Array
:sym				# Symbol
nil					# Nil
```



### STRINGS

**Strings** are a list of characters in specific sequences. String **Literals** are represented with either single `''`or double `""` quotes. Quotes are ruby syntactical components that are not apart of the string value. The exception is the **Escape** character `\`, or backslash, which allows the addition of syntax to be added as a string literal directly following. Escape characters are not needed to use single quotes within double quotes and vice versa.

```ruby
"This is a string with double quotes"

'This string uses single quotes'

'This string uses both single quotes \'with escape characters\' within it!'

	=> "This string uses both single quotes 'with escape characters' within it!"

# Utilization of single/double quotes within each other
"Say, 'Hello there'!"		or		'Say, "Hello there"!'

```

**String Interpolation** utilizes code within string literals to return an expression concatenated with its surrounding string. This technique only works with double quotes. The ruby syntax for interpolation is `#{ruby expresion}`.

```ruby
a = "ten"
puts "My favorite number is #{a}!"
=> "My favorite number is ten!"
```



### SYMBOLS

A **Symbol** is a technically immutable reference to another ruby value. The syntax for symbols uses a colon `:` before a word. Example, `:symbol`

```ruby
# Examples of symbols
:name
:a_symbol
:"This is also a symbol!?!"
```



### NUMBERS

An **Integer** is the basic form of a number and is represented by whole numbers only.

```ruby
1, 2, 3, 4, 5 ... so on
```

**Floats** are numbers that contain decimal places.

```ruby
1.0, 2.0, 3.14, 98.1421 ... so on
```



### NIL

**nil** is Ruby's way of expressing "nothing". The `nil` value may be described as having "nothing," "empty," "no specific type." 

The `puts` method prints a string but returns nothing. Therefore the returned value is `nil`.

```ruby
> puts "Hello, World!"	# Expression using puts method
> Hello, World!			# Output of puts method
=> nil					# Return value of puts method
```

`nil` may be explicitly referred to by using the `nil` literal.

```ruby
> x = nil				# Assigning x to nil
=> nil					# Return value of assigning x to nil
```

To check if something is `nil` type, use `.nil?`.

```ruby
> "Hello, World!".nil?	# Check to see if nil value
=> false				# Boolean return value
```

`nil` is treated as a false value when used in an `if` statement, since it is absent of value. Since the `if` statement evaluates to false, the expression within it is not evaluated. Remember when using `nil` in conditional statements, it will be treated as false.

```ruby
> if nil
> puts "Hello, World!"
> end
=> nil
```

Since the integer `1` is not 'nothing' or a false value, it is evaluated to true, and the code within the if statement is evaluated.

```ruby
> if 1
> puts "Hello, World!"
> end
Hello, World!
=> nil
```

It is important to understand that while `nil` may evaluate to false in a conditional statement. `nil` is not equal to false.

```ruby
> false == nil
=> false
```



### OPERATIONS

**Operatives** are characters used to perform mathematical processes. Addition `+`, Subtraction ` -`, Multiplication `*`, Division `/`,  Equality comparison `==` , and the Modulo `%`.

```ruby
> 1 + 1
=> 2

> 1 - 1
=> 0

> 4 * 4
=> 16

> 16 / 4
=> 4

> 15 / 4		# When dividing integers that do not divide evenly, only the whole numbers are returned.
=> 3
```

 The **Modulo** operator, represented by the `%` symbol acts predominately as a remainder operator. Ruby syntax for the modulus `%` is 	`quotient % modulus`. When used with positive integers the modulo operator returns the remainder of the division operation.

```ruby
> 16 % 4
=> 0

>16 % 5		# 16 / 5 = 3, with a remainder of 1.
=> 1		# Remainder of 1 is returned.
```

The `#remainder` method returns the remainder of an integer division. However, the remainder operator returns 



## (MISSING LAST MODULO LESSON HERE)



**Multiplying and Dividing Floats** 

Whenever using **Floats** in an operation, Ruby will always return another float.

```ruby
> 9.75 * 4.32
=> 42.120
```



**Equality Comparison**

The **Equality** operator `==` test the equality of two objects, and returns a boolean value.

```ruby
> 4 == 4
=> true

4 == 5
=> false

> 'foo' == 'foo'
=> true

> 'foo' == 'bar'
=> false

> '4' == 4
=> false
```

When comparing different data types, the equality operator will return false, because a string `'4'` is not equal to the integer `4`.



### STRING CONCATENATION

When using the `+` with two string data types, the operator joins the two together with **String Concatenation**. 

```ruby
> 'Hello, ' + 'there!'
=> 'Hello, there!'

> '2' + '2'
=> '22'

> '1' + 1
=> TypeError: no implicit coversion of Integer into String
```



### TYPE CONVERSION

In order to change 'convert' a data type to another, a conversion method can be called to invoke the change. To convert a string to an integer, the `.to_i` method is called to return an integer from a string. To convert an integer whole number to a float; the `.to_f` method can be called. There is also a method to convert to strings, `.to_s` that will return a data type into a string. There are many data type conversion methods, and may be looked up in the [RubyDocs](https://ruby-doc.org/core-3.0.1/).

```ruby
> '12'.to_i
=> 12
> 12.to_f
=> 12.0
> 12.0.to_s
=> '12.0'
```



### BASIC DATA STRUCTURES

**Arrays** are ordered lists used to organize information, which the information may be made up of any data type. Ruby array syntax is `[ ]` in which data will be held within closed brackets.













