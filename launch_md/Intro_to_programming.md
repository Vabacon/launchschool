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



# LOOPS & ITERATORS



A **Loop** is a repeatable piece of code that will execute for an amount of repetitions or until a certain condition is met. Loops consist of `while`, `do/while`, `loop`, and `for` reserve words.



**A Simple Loop**

A simple `loop` uses the `loop` method. `loop` takes a block, denoted by `{}`, or `do/end`, and will execute the code within the block. The `loop` continues until it reads a `break` statement within the block, terminating the `loop`. Ctrl + c can also be used to manually cancel the iterations.

```ruby
loop do
    puts "This will keep printing Ctrl + C"
end
```

The loop continues to print using the `puts` method until Ctrl + c is pressed canceling the `loop` execution.



**Controlling Loop Execution**

The `break` keyword exits the code at any point, and any code after will not be executed. The `break` keyword only exits the `loop` and not the entire program.

```ruby
i = 0
loop do
    i = i + 1
    puts i
    break
end

> 1
```

The `loop` block executes the code and prints an output, and is then exited by the `break` statement.

```ruby
i = 0
loop do
  i = i + 2
  puts i
  if i == 10
    break
  end
end
```

This code iterates through until an `if` condition is met, where it will execute the `break` statement. This code runs a total of 5 times before the `break` statement is read.

The `next` keyword is used to exit from a current iteration,by skipping the rest of the code, and execute the next `loop`.

```ruby
i = 0
loop do
    i = i + 2
    if i == 4
        next
    end
    puts i
    if i == 10
        break
    end
end

> 2
> 6
> 8
> 10
```

When the `if i == 4` code was evaluated, `next` was executed and the rest of the code was skipped until the next iteration of the `loop`.



**Loop Scope**

Writing a `loop` with a block creates a new scope. `loop` blocks abide by ruby scoping rules, where the inside block can access outside variables, but variable data is lock within the block from the outside.

```ruby
loop do
    x = 42
    break
end
puts x	# Rasis an error -- Undefined local variable or method 'x' for main:Object.
```

```ruby
x = 42
loop do
    puts x
    x = 2
    break
end
puts x

> 42
> 2
```

When the `puts` method was called from within the block, using `x`, `42` was printed to the screen. `x` then gets reassigned from within the block `x = 2`, and break is executed exiting the loop. When `puts` is passed `x`, `2` is printed to the screen. Showing that variables outside the `loop` block are accessible, reassignable, and mutable.



**While Loops**

A **While Loop** evaluates a parameter as either true or false. Once the expression evaluates to false, the code is not executed again.

```ruby
x = gets.chomp.to_i
while x >= 0
    puts x
    x = x - 1	# Also Refactor to x -= 1
end
```

The `while loop` will continue executing the code so long as `x >= 0` evaluates to `true`. `puts` is called with the `x` as an argument, and then `x` gets reassigned to `x = x - 1`. When `while` evaluates to `false`, the the code is exited.

Refactoring from `x = x - 1` to `x -= 1` is a better way to write code brevity and make it look nice.

**While Scope**

Unlike the `loop` scope, `while` does not have it's own scope, so the entire body of the of the `while loop` occupies the same scope as the rest of the program.

```ruby
x = 0
while x < 5
    y = x * x
    x += 1
end

puts y		# => 16
```

This demonstrates how variables within the `while` body are accessed and changed during it's iterations. The `loop` will continue until the value of `x` is `5`, then the rest of the code will be skipped.



**Until Loops**

-----------------------------------------------------------------------------------------------------------------------------------------------------



**Do/While Loops**

This loop works similar to a `while` loop, except that the code gets executed once. Ruby doesn't have an actual `Do/While` loop built in, so it needs to be emulated with the `loop` and `break`.

```ruby
loop do
    puts "Do you want to do that again?"
    answer = gets.chomp
    if answer != 'y'
        break
    end
end
```

This loop continues so long as `answer` is equal to `'y'`. When the `if` statement evaluates to true, then the code is executed again, until the `if` statement evaluates to false is the code exited.

There is also the `begin` keyword that may be used to re-factor some code. However, this way of writing code is not recommended even by the creator of Ruby.

```ruby
begin
    puts "Do you want to do that again?"
    answer = gets.chomp
end while answer == "y"
```



**For Loops**

A **For Loop** is used to iterate of a collection of elements. `for` loops have a definite end since it loops over a finite number of elements, therefore it is less likely to create an infinite loop.

Ruby syntax for a `for` loop is: `for <some variable> in <collection of elements>`.

```ruby
x = gets.chomp.to_i

for i in 1..x do
    puts x - i
end
```

The `for` loop iterated through each element and printed it to the screen until the loop reached

Interestingly, the `for` loop returns the the collection of elements after execution, whereas the `while` loop returns `nil`.

```ruby
x = [1, 2, 3, 4, 5]

for i in x.reverse do
    puts i
end
```

In this example, the `for` loop iterates over an array. Using the `.reverse` 

`for` is not implemented as a method, so it does not have its own scope.



**Conditionals Within Loops**

Using conditionals within loop statements can increase complexity and alter the flow of information.

```ruby
x = 0
while x <= 10
    if x.odd?
        puts x
    end
    x += 1
end
```

Using the `next` and `break` reserve words.

```ruby
x = 0
while x <= 10
    if x == 3
        x += 1
        next
    elsif x.odd?
        puts x
    end
    x += 1
end
```

This code using the `next` reserved word to skip printing out `3`, when `x == 3` and continues to the next iteration.



**Iterators**

An **Iterator** is a method that loops over a set of data, and allows operations to be performed on each element.

```ruby
numbers = [1, 2, 3, 4, 5]

numbers.each { |num| puts num }
```

Using the `each` method, the numbers variable is iterated over saving each element to the local variable `| num |` within `|` two pipes. After, the block executes the code on the local variable. The code exits and then begins the next iteration on the next element.

```ruby
names = ['Bob', 'Joe', 'Steve', 'Janice', 'Susan', 'Helen']
x = 1

names.each do |name|
  puts "#{x}. #{name}"
  x += 1
end
```

In this example, `x` is incremented by one every iteration.



**Recursion**

**Recursions** is the act of calling a method from within itself.

```ruby
def doubler(start)
    puts start
    if start < 10
        doubler(start * 2)
    end
end
```

In the `doubler` method, it takes the `start` variable and calls the method definition from within itself, passing the modified value back to the top. The looping or recursion continues until the `if` statement is satisfied.

```ruby
def fibonacci(number)
    if number < 2
        number
    else
        fibonacci(number - 1) + fibonacci(number - 2)
    end
end

puts fibonacci(6)
```

The recursion method loops for every instance that `number < 2` is not true. The key concept of recursion is that there is some condition that returns a value, which then the recursive calls. Each successive recursive call builds up until some value is returns, and then the recursive calls can be evaluated.



# ARRAYS



An **Array** is a list of elements, ordered by index, that can be of any data type.

```ruby
array = [1, 'Bob', 4.33, nil, ['nested array']]
```

Accessing information within the array can be done using the index number on the array.

```ruby
array[3]
> nil
```

Arrays are `0` indexed, meaning that the first element starts at the `0` spot, the second element is in the `1` index spot.



**Modifying Arrays**

Method can be used to modify an array to either add, modify, or remove elements with it.

```ruby
array.pop
> ['nested array']
```

The `pop` method invoked on the `array` variable permanently removed that last element from `array`. The `pop` method is a mutating method, and returns the removed element.

The `.push` method is used to add a permanent element to an array. Syntax for this method is `variable.push(element_to_be_added)`.

```ruby
array.push('reeeet')
> [1, 'Bob', 4.33, nil, 'reeeet']
```

Another syntax for the `.push` method is the shovel operator `<<`.

```ruby
array << 28
> [1, 'Bob', 4.33, nil, 'reeeet', 28]
```

Both method mutate the caller so the original array is modified.

The `.map` method iterates over an array and applies each element to a block in which a new array, with modified value, is returned, but the original array is not mutated. This modified return value can be stored in another variable. There is also the `.collect` method which is an alias for `.map`. They are the same method.

```ruby
array = [1, 2, 3, 4]
array.map { |e| e ** 2 } # or array.collect
> [1, 4, 9, 16]

p array
> [1, 2, 3, 4]

b_array = array.map { |i| 1, 2, 3, 4}
p b_array
> [1, 4, 9, 16]
```

The `.map` method does not destroy the original array.

The `delete_at` method is used to delete an element at a certain index. This is a destructive method and will modify arrays.

```ruby
array.delete_at(1)
> 2				# Value at the index (1)p array> [1, 3, 4]
```

The `.delete` method allows the removal of an element when the value is known but not the index. This method permanently deletes and modifies the array at that specific indexed value.

```ruby
array.delete(4)
> 4				# The actual value, not the indexp array> [1, 2, 3]
```

The `.uniq` method is used to return an array with all repeating values removed. This method does not modify the array.

```ruby
array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5]
array.uniq
> [1, 2, 3, 4, 5]

p array
> [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5]
```

To modify permanently using the `.uniq` method, a bang suffix `!` is needed to destructively modify the array.

```ruby
array.uniq!
> [1, 2, 3, 4, 5]

p array
> [1, 2, 3, 4, 5]
```

The `.uniq` and `.uniq!` methods are two different methods within the Ruby Array Class. The `!` cannot be added to any method to make it destructive.



**Iterating Over an Array**

Iterating using the `.select` method iterates over an array in which it compares each element to a block, and returns any value that evaluates to `true`.

```ruby
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.select { |num| num > 4 }
> [5, 6, 7, 8, 9, 10]

p numbers
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

The `.select` method selects all elements that are `true` given the expression `num > 4` and outputs a new array with the evaluated elements. The `.select` method does not mutate the caller.



**Methods With a !**

the **Bang Suffix `(!)`**, at the end of a method **usually** indicates that it will mutate the caller. This is an indicator of a destructive method. It is good practice to be sure of the method and to check the Ruby documentation to be sure of that methods behavior. Since this is not always the case, there are destructive methods such as `.pop` and `.push` that mutate the caller that are both without the bang suffix.



**Mutating the Caller: The Sequel**

Mutating callers is an important concept to understand, since situations could occur where data is being sent to a method that may be destructive and cause significant confusion. 

```ruby
def mutate(arr)
    arr.pop
end
def not_mutate(arr)
    arr.select { |i| i > 3 }
end

a = [1, 2, 3, 4, 5, 6]
mutate(a)
not_mutate(a)
puts a
```

In this example, the `mutate` method definition permanently modified the array by using `arr.pop`, which removed `6` from the `a` variable. The `not_mutate` method used the `.select` method on the `a` variable, which returned a value, but did not modify the `a` variable. At the last line, the output is `[1, 2, 3, 4, 5]` since the `.pop` was used.



**Nested Arrays**

Since arrays can contain any data type, they can also contain nested arrays, which are arrays within arrays.

```ruby
teams = [['Joe', 'Steve'], ['Frank', 'Molly'], ['Dan', 'Sara']]
> [["Joe", "Steve"], ["Frank", "Molly"], ["Dan", "Sara"]]
```

In an example where there are separated teams, an individual team can be accessed using an array index.

```ruby
teams[1]
> ['Frank', 'Molly']
```

This is an example of accessing an array nested within another array, in which we can access the elements within it. To be continued later.



**Comparing Arrays**

Arrays can be compared using the equality operator.

```ruby
a = [1, 2, 3]
b = [2, 3, 4]
a == b
> false
```

Using the `.unshift` method allows an element to be added to the **beginning**, or start, of an Array.

```ruby
b.pop
> 4

b.unshift(1)
> [1, 2, 3]

b == a
> true
```

The modified `b` array is now equal to the `a` array, using the `.pop` and `.unshift` methods.



**`.to_s`**

The `.to_s` method converts data types, that can be converted, to a string type. When using string interpolation, Ruby does this automatically.

```ruby
a = [1, 2, 3].to_s

p a
> "[1, 2, 3]"
```



**Common Array Methods**

Refer to the Ruby documentation to view the built-in Array class methods.

- `.include?` method checks the argument given is included in the array, and returns a boolean value. These types of method are called **Predicates**.

  ```ruby
  a = [1, 2, 3]
  a.include?(2)
  > true
  
  a.include(4)
  > false
  ```

- `.flatten` is used to create a one dimensional array from a multi-dimensional, nested, array. The `.flatten` method is **NOT** destructive, and will not modify the original variable.

  ```ruby
  a = [1, 2, [3, 4], [5, 6]]
  a.flatten
  
  > [1, 2, 3, 4, 5, 6]
  
  p a
  > [1, 2, [3, 4], [5, 6]]
  ```

- `.each_index` iterates through an array like the `.each` method might have, but instead of manipulating the value at the index, the variable represents the index number.

  ```ruby
  a = [1, 2, 3]
  a.each_index { |i| puts "This is index #{i}."}
  
  > "This is index 0."
  > "This is index 1."
  > "This is index 2."
  ```

- `.each_with_index` manipulates both the value and the index using two parameters within a block. The first parameter represents the value, and the second is the index.

  ```ruby
  a = [1, 2, 3]
  a.each_with_index do |val, idx|
      "#{idx+1}. #{val}"
  end
  
  > 1. 1
  > 2. 2
  > 3. 3
  ```

- `.sort` is used to return a sorted array. The `.sort` method is not destructive, so it will not modify the original array in any way.

  ```ruby
  a = [4, 5, 6, 1, 2, 3]
  a.sort
  
  > [1, 2, 3, 4, 5, 6]
  ```

- `.product` is used to combine two arrays in an "polynomial" fashion. Each element of the first array is combined with each element of the argument, and is created in a nested fashion. Tested in irb, this method is not destructive, and the original variable is not modified.

  ```ruby
  [1, 2, 3].product([4, 5])
  > [[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]]
  ```



**`.each` vs. `.map`**

- `.each` works on objects that allow for iteration and is typically used with a block. When a block is given, the `.each` method will run each element once through the block and returns the collection it was invoked on. If no block was given, then it returns an **Enumerator**.

  ```ruby
  a = [1, 2, 3]
  a.each { |e| puts e }
  1
  2
  3
  > [1, 2, 3]
  ```

  This example shows a common `.each` use, prints local variable `e` which is used to store each element, and returns the original object.

  The `.each` can also be used to output modified values. If instead of the upper block, `a.each { |e| puts e + 2 } `was written instead, it would print out the evaluated result, but still return the original object.

- `.map` is similar to `.each` in that it iterates over objects, and applies a block for each element if a block is given. `.map` is different in the way it returns its value. It creates and returns a new object containing the values evaluated within it's block, but leaves the original object unmodified.

  ```ruby
  a = [1, 2, 3]
  a.map do |e|
      e ** 2
  end
  > [2, 4, 9]
  ```

  When evaluating `.map` using `.puts` within it's block, `.map` creates a new array consisting of all the return values from within it's block, and since the `.put` method returns `nil`, the following code will evaluate to an array of all `nil`s.

  ```ruby
  a.map do |e|
      puts e**2
  end
  > [nil, nil, nil]
  ```

  If no block is given, the `.map` method will return an Enumerator the same way `.each` will.

  ```ruby
  a.map
  >#<Enemerator: [1, 2, 3]:map>
  ```

Both `.each` and `.map` are important for iteration, and need careful attention to detail. use `.each` for iteration, and `.map` for transformation.



# Hashes



A **Hash** is a data structure that stores items by `{:key => value}`, or `{key: value}` pairs to create an associative representation of data. Hashes are usually created using _symbols_ as keys and any data type as a value.

```ruby
old_syntax_hash = {:name => 'vinton'}
> {:name => 'vinton'}					# pre Ruby 1.9

new_syntax_hash = {name: 'vinton'}
> {:name => 'vinton'}
```

Multi key value pair hash using a comma to separate each key value pair.

```ruby
individual = {
    height: '5 foot, 12 inches',
    weight: '189 lbs',
    color: 'Brown',
    hair: 'Black',
    race: 'White'
    ethnicity: 'Latino/Hispanic',
    sex: 'Male'
    }
```

To add onto an existing hash, call on the hash with the brackets `[]` containing the key and assign it to the value. Syntax is `hash_variable[location:] = 'College Station, Tx'`.

```ruby
hash = Hash.new
> {}
hash[first_key:] = "First Value!"

p hash
> {:first_key => 'First Value!'}
```

To remove a key value pair from a hash, use the syntax `hash_variable.delete(:key)`.

```ruby
hash_variable.delete(:location)
> 'College Station, Tx'
```

To retrieve a piece of information from a hash use syntax `hash_variable[:key]`.

```ruby
individual[:ethnicity]
> 'Latino/Hispanic'
```

To add another hash, use the `.merge!` method to permanently merge two hashes together. Using the `.merge` without the bang suffix will return a new hash without the destructive properties.

```ruby
individual.merge!(other_hash)
# outputs a merged key value set from individual and other_hash
```



**Iterating Over Hashes**

Iterating over hashes is similar to iterating over arrays with some differences. When iterating over a hash, it is required to use both the key and value as local variables within the block. Syntax is `hash_iteration.each { |key, value| block_logic }`, also used with the `do/end`.

```ruby
person = {name: 'bob', height: '6 feet', weight: '160 lbs', hair: 'brown'}

person.each do |key, value|
    puts "Bob's #{key} is #{value}."
end
```



**Hashes as Optional Parameters**

When giving optional parameters to a method definition, a hash can be passed to give the method more flexability.

```ruby
def greeting(name, options = {})
    if options.empty?
        puts "Hi, my name is #{name}."
    else
        puts "Hi, my name is #{name}, and I am #{options[:age]}" +
            " years old and I live in #{options[:city]}."
    end
end

greetings('Bob')
greetings('Bob', age: 62, city: 'Hempstead')
```

The hash arguments that is passed to the greetings method definition can also be written as:

```ruby
greetings('Bob', {age: 62, city: 'Hempstead'})
```

A hash does not require curly braces `{}` when it is the last argument passed. Ruby acts identically to either syntax, so long as the hash is the **last** arguement.



**Hashes vs. Arrays**

When deciding whether to use an Array or Hash:

- Does this data need to be associated with a specific lable?
  - yes? Then use a hash.
  - No? Then use an array, if the data doesn't have a natural label.
- Does order matter?
  - Yes? Then use an array.
  - Hashes also maintain order, but ordered items are usually stored in an array.
- Do I need a 'stack', or 'queue' structure?
  - Yes? Use an array. Arrays are good at mimicking simple 'first-in-first-out' queues, or 'last-in-first-out' stacks.



**A Note On Hash Keys**

The most common utilization of hashes include symbols as hash keys, however it is possible to use different data types as keys.

```ruby
many_key_types = {
    "height" => "6 feet",
    ["height"] => "6 feet",
    1 => 'one',
    45.125 => '45.125',
    {key: 'key'} => 'hash as key!?!'
    }
```

Notice when using other data types as keys in hashes, that a hash rocket `=>` must be used. When running this in irb, this code is outputs the hash as is and works with many data types.



**Common Hash Methods**

- `.key?` checks if a hash contains any specific key and returns a boolean value.

  ```ruby
  hash = {key: 'value'}
  
  hash.key?(:key)
  > true
  
  hash.key?(:some_key)
  > false
  ```

- `.select` passes key value pairs to a block and returns any pairs that evaluate to true.

  ```ruby
  ```

  













