# s = '01234'
# print(s.index('2'))

# a = [0, 1, 2, 3, 4]
# print(a.index(4))

# s = '01234'

# # find index of a character in a string

# def get_index(s, c):
#     for i in range(len(s)):
#         if s[i] == c:
#             return i
#     return -1

# print(type(get_index(s, '2')))

def checkBraket(a, b):
    if a == "(" and b == ")":
        return True
    elif a == "{" and b == "}":
        return True
    if a == "[" and b == "]":
        return True
    return False
        
    
