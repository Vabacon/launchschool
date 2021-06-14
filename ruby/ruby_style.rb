# RUBY STYLES GUIDE LINES.

# 1. The text editor ide should be set to two (2) spaces per tab. Set the tab to 'soft'.

# 2. # When using the '#' symbol, everything after it is a comment.

# 3. When defining or initalizing a variable/file, always use snake_case format.
# => Using all lower case letters and separate words with an underscore (_).

this_is_a_snake_cased_file.rb

forty_two = 42

def this_is_a_great_method
  do_stuff
end

# 4. When defining a value that will not change it is a CONSTANT variable.
#   CONSTANTS are defined using all uppercase letters.

CONSTANT = "This variable does not change."

FOUR = 'four'

FIVE = 5

# 5. Using { ... } for single line expressions, and do ... end for multi-line
#    expressions.

[1, 2, 3].each do |i|                       # Not good
  do_stuff
end

[1, 2, 3]. each do{ |i| do_stuff }          # Good

[1, 2, 3].each do |i|                       # Good
  puts i
  do_stuff
end

[1, 2, 3].each do { |i| puts i; do_stuff }  # Not good

# 6. When naming classes, use CamelCase (AKA PascalCase).

class MyFirstClass
end

class MySecondClass
end
