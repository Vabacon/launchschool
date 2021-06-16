## Please update at git after OPERATORS.



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













