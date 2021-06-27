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


<<<<<<< HEAD

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



**Obj.method or Method(obj)**

There are two ways to call methods. Method definitions require a caller and a value to be passed `method(object)` in order to invoke the method definition. Other methods are able to be called using the **Dot Operator** `.` on an object. some `object.method`.



**CHAINING METHODS**

As long as an expression is returning a value, especially method definition, and not `nil`. Methods can be chained together to form complex code.

```ruby
"Hi there".length.to_s	# returns "8" - a string.
```

The code returns `"8"` as a string data type, since `.length` methods returns the length of a string as an integer, calling `.to_s` will convert it into a string.

```ruby
def add_three(n)
    puts n + 3
end

add_three(5).times {puts "Will this work"}
```

The return value of `puts` within the `add_three` method is `nil`, and returns a `NoMethodError: undefined method times' for nil:Nilclass`. the `.times` method cannot be used on the `nil` class.

```ruby
def add_three(n)
    new_value = n + 3
    puts new_value
    new_value			# No explicit return key.
end

add_three(5).times {puts "Will this work"}
```

This code returns a value to the `.times` method to be used in the block. This code works because there is an implicit return ` new_value` in the method definition.



**Method Calls as Arguments** 

Method definitions are able to be used as an argument to pass values to another method definition.

```ruby
> def add (a, b)
>     a + b
> end

> def sub (a, b)
>     a - b
> end

> def multi (num1, num2)
>     num1 * num2
> end

> multi(add(10, 40), sub(38, 21))
=> 850
```

When using nested method calls, use parentheses to prevent confusion. Know what each method is returning, the returned value is vital to understanding whether a value will be passed and modified or an error will be generated.



**The Call Stack**

A **Call Stack** is a 'to-do list' of method invocations that are ordered by function name, passed arguments/parameters, and line number. When ever function invocation occurs, that function details are saved to the top of the call stack, and when the function returns, its information is 'popped' from the top. **Last In, First Out**.

```ruby
1  def first
2    puts "first method"
3 end
4
5 def second
6    first
7    puts "second method"
8 end
9
10 second
11 puts "main method"
```



| Call Stack          |
| ------------------- |
| puts "first method" |
| first: line 2       |
| second: line 6      |
| main: line 10       |

As methods are invoked, Ruby saves its information and updates the stack frame. `main` gets it's first invocation on line `10`, where it's information is saved so that when it's method returns, execution may continue. Method def. `second` invokes the method `first` on line `6`, and it's information is updated to the call stack. Within the `first` method, the `puts` method is invoked with a string, it 'returns' completing the `first` method's execution. This will continue back down the call stack until it reaches `main` on line `10`, which the call stack will 'pop' the information from the top, and continues to execute the rest of the program.

Ruby has a stack size of at least 10,000 stack entries. If the stack were to run out of room , a `SystemStackError` exception would occur.



# FLOW CONTROL



**Flow Control** is a sequence flow that takes precedence under certain conditions, meaning a condition must be met in order for the program to execute the correct path. They are basic logical structures defined with reserve words, `if`, `else`, `elsif`, and `end`, and use logical operators, `<`, `>`, `<=`, `>=`, `==`, `!=`, `&&`, `||`.

```ruby
puts "Put in a number"
a = gets.chomp.to_i

if a == 3
    puts "a is 3"
elsif a == 4
    puts "a is 4"
else
    puts "a is neither 3, nor 4"
end
```

This `if` statement evaluates a positive integer, and compares them to the conditionals using the `==` equality operator. `else` is a default conditional in this example, which evaluates any other input, other than `3` and `4`, and prints `"a is neither 3, nor 4"`.

There are examples of valid Ruby conditionals.

1. `if` by itself.

   ```ruby
   if x == 3
       puts "x is 3"
   end
   ```

   An `elsif` condition without `else`.

2. ```ruby
   if x == 3
       puts "x is 3"
   elsif x == 4
       puts "x is 4"
   end
   ```

   `if` statement with only `else`.

3. ```ruby
   if x == 3
       puts "x is 3"
   else
       puts "x is NOT 3"
   end
   ```

   Must use "then" keyword when using 1-line syntax.

4. ```ruby
   if x == 3 then puts "x is 3" end
   ```

   An if statement may be appended to the end of an expression, or literal.

5. ```ruby
   puts "x is 3" if x == 3
   ```

   Ruby's reserve word `unless` acts opposite to `if`.

6. ```ruby
   puts "X is NOT 3" unless x == 3
   ```



**Comparisons**

**Comparison Operators** compares two **Operands** and always returns a boolean value. a **Boolean Value** is either `true` or `false`.

1. The "is equal to" operator `==`, checks the operands are equal.

   ```ruby
   5 == 5
   > true
   
   5 == "5"
   > false
   ```

2. The "not equal to" operator `!=` compares anything to the left of the symbol is not equal to the right.

   ```ruby
   4 != 4
   > false
   
   4 != "abc"
   > true
   ```

3. The "less than" symbol `<`. Anything to the left of the symbol is evaluated against anything on the right.

   ```ruby
   2 < 5
   > true
   
   8 < 2
   > false
   ```

4. The "greater than" symbol `>`. Anything to the left that has a higher value to anything on the left that has a lower value.

   ```ruby
   5 > 2
   > true
   
   6 > 7
   > false
   
   "42" < "402"
   > false
   
   "42" > "402"
   > true
   ```

   Ruby reads string operands from left to right, comparing each character with its counterpart. If both strings are equal up to the length of the shorter string, than the shorter string is considered less than the longer string.

5. The "less than or equal to" symbol `<=`.  Compares if the operand on the left of the symbol is less than or equal to the right.

6. The "more than or equal to" symbol `>=`. Compares if the operand on the left of the symbol is more than or equal to the right.

   ```ruby
   4 <= 5
   > true
   
   5 >= 5
   > true
   
   4 >= 5
   > false
   
   4 >= 3
   > true
   
   4 >= 4
   > true
   ```



**Combining Expressions**

Combining expressions makes it possible to combine multiple conditional expressions to create a more specific scenario. 

- `&&` - "and" operator. Both expressions must be true for the entire expression to be evaluated as true.

```ruby
(4 == 4) && (5 == 5)
> true
(5 == 4) && (5 == 5)
> false
```

- `||` - "or" operator. Evaluates to `true` if either expression evaluates to `true`.

```ruby
( 5 == 5) || (3 == 2)
> true
(4 == 2) || (5 == 6)
> false
```

- `!` - the "not" operator. Changes the value of a boolean expression.

```ruby
!(4 == 4)
> false
```

For clarity:

1. `<=`, `<`, `>`, `>=` - Comparison operators

2. `==`, `!=` - Equality
3. `&&` - Logical AND
4. `||` - Logical OR

```ruby
if x && y || z
    # do something
end
```

Here, the `&&` will be evaluated first, if `true` then the code will execute. If `false`, then the `||` will be evaluated. If none evaluate to `true`, the code will exit the `if` statement



**Ternary Operator**

The **Ternary Operator** is a common Ruby idiom that makes a quick `if/else` statement on one line, and uses a combination of the `?` and `:` for it's syntax.

```ruby
true ? "This is true" : "This is not true"
=> "This is true"

false ? "This is true" : "This is not true"
=> "This is not true"
```

Ternary operators work by evaluating the truthiness of the statement on the left of the `?`. If it is `true` then the code on the left of the `:` gets executed. If the statement on the left of the `?` is false, then the code on the right of the `:` gets executed. 

```ruby
expression ? true_value : false_value
```



**Case Statement**

a **Case Statement** has similar functionality as an `if/else` statement, but uses a different syntax using reserve words `case`, `when`, `else`, `end`. 

1. ```ruby
   a = 5
   
   case a
       when 5
       puts "a is 5"
       when 6
       puts "a is 6"
   else
       puts "a is neither 5, nor 6."
   end
   ```

   A case statement's result can also be saved to a variable.

2. ```ruby
   a = 5
   
   answer = case a
       when 5
      	  "a is 5"
       when 6
         "a is 6"
   	else
       puts "a is neither 5, nor 6."
   end
   
   puts answer
   ```

3. This case statement doesn't take an argument, meaning no information is added after the `case`. So each `when` statement will need to be fully tested.

   ```ruby
   a = 5
   
   case
       when a = 5
         puts "a is 5"
       when 6
         puts "a is 6"
   	else
         puts "a is neither 5, nor 6."
   end
   ```



**True and False**

When writing `if/else` statements, it needs to evaluate expressions that will return either true or false.

```ruby
a = 5

if a
    puts "how can this be true?"
else
    puts "it is not true!"
end
```

This statment will evaluate to true, since `a = 5` is a truthy value it will evaluate to `true`. 















