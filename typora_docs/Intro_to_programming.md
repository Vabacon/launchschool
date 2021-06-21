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

**Arrays** are ordered lists used to organize information, which the information may be made up of any data type. Ruby array syntax is `[ ]` in which data will be held within closed brackets. Each piece of data within the array is called an **Element**, and can be accessed by an **Index**. It is important to know that many programs recognize [0] indexing, which means that the computer starts counting at [0].

```Ruby
> [1, 2, 3, 4, 5]
=> [1, 2, 3, 4, 5]

>[1, 2, 3, 4, 5][0]		# Accessing element at index [0].
=> 1					# Element [1] returned at the [0] index.
```



A **Hash** (Dictionary), is a set of _Key-Value_ pairs. As referred to above, hash literal syntax is denoted by `{}` curly braces. The hash contains keys that point to a value, where the key is a symbol. Keys are used to either set or retrieve values. Ruby syntax for a hash is: `{:key => value, :key2 => value2}`. 

```ruby
> a_hash = {:dog => 'wof',		# Stacked
   :cat => 'mow',
  }
> a_hash = {:dog => 'wof', :cat => 'mow'}	# Single

> a_hash[:dog]			# Calling a value using it's key.
=> 'wof'
```



### EXPRESSIONS & RETURN

An **Expression** is anything that can be evaluated. Almost everything written in Ruby is an expression, and returns a value, an `Errortype`, or even `nil`. 

`puts` is a method telling Ruby to print something to the screen. `puts` does not return anything (meaning `nil`), and prints an evaluated expression to the screen and returns `nil`.

```ruby
> puts 'YEET!'
'YEET!'
=> nil
```



# VARIABLES



A **Variable** is a container holding a point in physical memory used to store, label, and manipulate data within a computer program. When naming variables, select names that are clear and descriptive of the containers contents and what it does. Assigning a variable a value uses the **assignment operator** `=` to store values. Ruby syntax is for assignment is: `variable_name = 'value to be stored'`

```ruby
> a_variable = 'a value!'
=> 'a value!'

> a_variable			# Referencing variable
=> 'a value!'			# Return value of referenced variable
```

The string value of `a value!` is now stored in `a_variable` in spacial memory.

```ruby
> a = 4
> b = a
> a = 7
> puts b
=> 4
```

When `a = 4`, a is assigned to an object integer `4`, so when `b = a`, `b` is assigned the same object integer that a is pointing to. When `a` gets reassigned to the object integer `7`, `b` is still pointing to the object integer `4` since `b` is not directly pointing to the variable `a` but to its value.



**GETTING DATA FROM A USER**

The `gets` method is used to retrieve string input from the user. `gets` stands for "get string" and requires the user to input information and press the enter key.

```ruby
> name = gets
Vinton
=> "Vinton\n"
```

`name` is assigned to an input method `gets` and waits for information. When data is entered it gets stored in the `name` variable. The return value of name is `Vinton\n`, where there is an appended **new line character** `\n`.  The new line character represents the enter keys input known as a **Carriage return characters**. The `.chomp` method can be appended to the `gets` method to remove carriage return characters. 

```ruby
> name = gets.chomp
Vinton
=> 'Vinton'
```



**VARIABLE SCOPE**

The availability of a programs variable is determined by the **variable scope**, where scope is defined by where it is initialized. Scope is defined by a **block** following method invocation, delimited by curly braces `{}` or `do / end` pairs. Be aware that not all `do / end` pairs imply a block.

In LaunchSchool, there is one rule that must be followed regarding what constitutes a variable's scope:

**Inner scope can access variables initialized in an outer scope, but outer scope variable cannot access inner scope variables.**

```ruby
a = 5				# Initialize var a assigned to value 5.

3.times do |i|		
   a = 3			# Reassigned var a to value 3.
end

puts a

=> 3				# Var a gets reassigned 3 times to value 3.
```

The variable `a` gets reassigned to `3` because it is accessible within the inner block scope, and when called with the `puts` method it outputs a value of `3`.

```ruby
a = 5				# Initialize var a assigned to value 5.

3.times do |i|		
   a = 3			# Reassigned var a to value 3.
   b = 5
end

puts a
puts b				# Is var b available outside the block?

=> 3	
=> scope.rb `<main>': undefined local variable or method 'b' ...
```

Variable `b` is not available outside the method invocation with a block, since the outside scope cannot see within the block scope. So Ruby throws and error stating that there is an no defined variable. Remember that the distinguishing factor deciding whether a code block crates a new scope for variables is if **a block `{}` or a `do/end` pair immediately follows a method invocation!** 

```ruby
> arr = [1, 2, 3]

> arr.method_invocation { |i| a = 5 }

> arr.method_invocation do |i|
    a = 5
> end

> for i in arr do
>    a = 5
> end

> puts a	# example puts method for each block type
```

The first two blocks create new scope for variable a since they are both blocks following method invocation. Calling `puts a` will generate an error message saying that there is an undefined variable `a` that is being called on. The last  `for` example does not create a new variable scope since it consists of a block **NOT** immediately following a method invocation. Therefore, it is available outside the block as well.

**TYPES OF VARIABLES**

There are **five** types of variables in Ruby: 

- CONSTANTS: Declared with all caps `MY_CONSTANT_VAR`, used to store data that will **never** change. While Ruby will allow changes to constant variables, it is good practice to NOT change these values. Cannot be declared in method definitions and are available throughout the applications scope.

  ```ruby
  MY_CONSTANT_VAR = "My scope is available throughout the application!!!
  ```

- $Global: Declared with a `$` sign. Are available throughout the entire application's scope, overriding all scope rules. "Rubyist" tend to stay away from this variable as it may cause complications when using them.

  ```ruby
  $global_var = "This variable is available everywhere!!!"
  ```

- @@Class:  Declared using two `@@` signs, are used to declare a class, but must be outside any method definitions, and called on using instance of that class.

  ```ruby
  @@instances = 0
  ```

- @Instance: Declared using one `@` sign, are available throughout the current instance of the parent class. 'see above'. These vars may have another set of rules regarding scope boundaries.

  ```ruby
  @instance_var = "I am only avaiable throughout this current instance of this class."
  ```

- Local: Declared with `snake_case` all lower case, and are the most common variable in Ruby.

  ```ruby
  this_variable = 'I must be passed around to cross scope boundaries!!!'
  ```

  


# METHODS



**What are Methods**

A **Method** is a piece of common code that can be executed many times within a program without needing to rewrite it over and over again. A method is defined by using the `def` **Reserve Word**, the method name after the `def`, and complete the definition by using reserve word `end`.

```ruby
def say(words)	# def reserve word, name, and parameters.
    puts words	# Method body/logic goes here.
end				# end reserve word to finish a definition.

say("Hello")	# Invocation of method / argument passed
say("Sup")		# argument "Sup" gets assigned to words variable.
```

The method definition `say` simply extracted the logic of printing out text, so that the application may have more flexibility. The act of using a method definition is to **Call** or Invoke, known as **Method Invocation**.  

The `(words)` after `def say` is called a **Parameter**, with is used so that data can be passed into the method definition's scope.

**Arguments** are pieces of information that are passed to a method invocation to be modified, or used, to return a specific result. Arguments are passed when a method definition is called. The argument is then assigned to the local variable(s) initialized at the method definition level. This entails that method definitions have their own scope and cannot be referenced outside the definition. Argument syntax is `method(object)`.



**Default Parameters**

A **Default Parameter** automatically evaluates to a predetermined value when no arguments are passed to a method invocation.

```ruby
> def say (words = 'hello')	# Assigned words default to 'hello'.
>     puts words + '.'
> end

> say()				# Invocation with no argument passed.

=> hello.			# Default value output from method def.
```



**Optional Parentheses**

Most parenthesis may be left of when writing Ruby, method invocation `say('hi')` could be written as `say 'hi'`. And `puts("WASSUP")` and `puts "WASSUP"`. For my case (the future me reading this), please use parenthesis!



**Method Definition and Local Variable Scope**

Method definitions create their own scope outside the regular flow of execution. Variables within the definition cannot be accessed from outside the definition, and variables outside cannot be access from within the definition without being passed as an argument. 

```ruby
> a = 5

> def some_method
>     a = 3
> end

> puts a
```

The value of `a` is still `5`. This is because the `a` within the definition is contained in a separate scope. Please be aware that scoping rules for method definitions and blocks are different and should not be confused.



**Obj.method or Method(obj)**

There are two ways to call methods. Method definitions require a caller and a value to be passed `method(object)` in order to invoke the method definition. Other methods are able to be called using the **Dot Operator** `.` on an object. some `object.method`.

**Mutating the caller**

Some methods can permanently alter the argument passed into the method definition called mutating the caller. This occurs when performing some action that **can** mutate the caller, at the moment there is no way to know what will and wont mutate the caller. This will have to be done by practice and research on documentation.

```ruby
> a = [1, 2, 3]

> def mutate(arr)
>    arr.pop
> end

> p "Before mutate method: #{a}"
=> "Before mutate method: [1, 2, 3]"

> mutate(arr)

> p "After mutate method: #{a}"
=> "After mutate method: [1, 2]"

```

Local variable `a` has been permanently changed from within the method definition using the `.pop` method, which has mutated the caller. Even though `a` is outside the method definition scope, `.pop` is a **destructive** method in the `Array` class and can make permanent changes to variables in and out of method definitions.

```ruby
> a = [1, 2, 3]

> def mutate(arr)
>    arr.last
> end

> p "Before mutate method: #{a}"
=> "Before mutate method: [1, 2, 3]"

> mutate(arr)
> p "After mutate method: #{a}"
=> "After mutate method: [1, 2, 3]"
```

Local variable `a` was not permanently modified in any way since the `last` method returns the last element of an array, but does not modify the array itself. The `last` method is not a destructive method, and cannot make permanent changes.



**puts vs return: The Sequel**

In Ruby, methods **always** return the evaluated result of the last line of the expression unless an **explicit** return comes before it.

```ruby
> def add_three(num)
>   num + 3				# No explicit return statment, so the last evaluated line will be returned.
> end

> returned_value = add_three(4)
> puts returned_value
=> 7							# The return value of add_three stored in returned_value.
```

To explicitly return a value, use the `return` reserve word.

```ruby
> def add_three(num)
>   return num + 3
>   num + 5			# Explicit return statment returned.
> end

> returned_value = add_three(4)
> puts returned_value
=> 7
```

When using the `return` reserve word, the method will return that statement without evaluating the next line. Thus, exiting the method definition. Note that `return` is not needed for a method definition to return a value, but is a feature of the Ruby language.



**CHAINING METHODS**

:) :)
