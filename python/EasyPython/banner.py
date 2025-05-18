
def print_in_box(string):
    print('+-' + '-' * len(string) + '-+')
    print('| ' + ' ' * len(string) + ' |')
    print(f'| {string} |')
    print('| ' + ' ' * len(string) + ' |')
    print('+-' + '-' * len(string) + '-+')


print_in_box('To boldly go where no one has gone before.')

sentence = input("Sentence here: ")
print_in_box(sentence)