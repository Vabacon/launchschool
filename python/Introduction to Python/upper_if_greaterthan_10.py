def upper_if_gt_10(string):
    print(string.upper() if len(string) > 10 else string)

# def upper_if_gt_10(string):
#     if len(string) > 10:
#         print(string.upper())
#     else:
#         print(string)

upper_if_gt_10("Hello World")
upper_if_gt_10("Howdy")