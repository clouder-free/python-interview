#! /usr/bin/python

def calculate(s: str) -> int:
    # stack store data, operator store operator
    stack = []
    operator = []
    sign = 1
    result = 0
    i = 0
    while i < len(s):
        if "0" <= s[i] <= "9":
            number = ""
            while i < len(s) and "0" <= s[i] <= "9":
                number += s[i]
                i += 1
            result += int(number) * sign
        elif s[i] == "+":
            sign = 1
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "(":
            # store
            stack.append(result)
            operator.append(sign)
            result, sign = 0, 1
            i += 1
        elif s[i] == ")":
            res = stack.pop()
            op = operator.pop()
            result = res + result * op
            i += 1
        else:
            i += 1
    return result

if __name__ == "__main__":
    s = "1+121-(14+(5-6))"
    result = calculate(s)
    print("result:{}".format(result))
    