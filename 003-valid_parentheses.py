def valid_parentheses(string):
    st = []
    pairs = {')': '(', '}': '{', ']': '['}

    for i in string:
        if i in "({[":
            st.append(i)
        elif i in ")}]":
            if not st:
                return False
            top = st[-1]
            if top == pairs[i]:
                st.pop()
            else:
                return False
    return not st

