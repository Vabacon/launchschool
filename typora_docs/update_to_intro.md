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
> 2
p array
> [1, 3, 4]
```

The `.delete` method allows the removal of an element when the value is known but not the index. This method permanently deletes and modifies the array at that specific indexed value.

```ruby
array.delete(4)
> 4

p array
> [1, 2, 3]
```















