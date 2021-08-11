def com_Data(left, rt):
    if left == '[' and rt==']':
        return True
    elif left == '{' and rt=='}':
        return True
    elif left == '(' and rt==')':
        return True
    else:
        return False

def checker(data):
    st_bracket = []
    br_index = []
    for i, next in enumerate(data):
        if next in ["[","{","("]:
            st_bracket.append(next)
            br_index.append(i)

        if next in ["]","}",")"]:
            if not st_bracket:
                return i+1 ,next,"opened"
            left = st_bracket[-1]
            lf_index = br_index[-1]
            if com_Data(left,next):
                st_bracket.pop()
                br_index.pop()
            else:
                return lf_index+1,left,"closed"
    return -1, None, None

data = input()
index, chr, rsn = checker(data)
if index== -1:
    print("This expression is correct")
else:
    print("This expression is NOT correct.")
    print("ERROR at character #{} '{}' not {}".format(index, chr, rsn))