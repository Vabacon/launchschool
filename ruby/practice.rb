a_array = [1, 2, 3, 4, 5]
b_array = Array.new

b_array = a_array.map do |e|
  e + 2
end

p a_array

p b_array