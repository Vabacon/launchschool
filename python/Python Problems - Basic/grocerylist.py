grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# for i in range(len(grocery_list)):
#     print(grocery_list[0])
#     grocery_list.pop(0)

while grocery_list:
    item = grocery_list.pop(0)
    print(item)

print(grocery_list)