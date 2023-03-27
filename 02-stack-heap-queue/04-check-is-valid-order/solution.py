#! /usr/bin/python

"""
POJ 1363
"""

def check_is_valid_order(queue: list) -> bool:
    stack = []
    length = len(queue)
    for i in range(1, length+1):
        stack.append(i)
        # stack not empty and order equal
        while stack and stack[-1] == queue[0]:
            stack.pop()
            queue.pop(0)
    
    if len(stack) > 0:
        return False
    return True

if __name__ == "__main__":
    queue = [3, 2, 5, 4, 1]
    result = check_is_valid_order(queue=queue)
    print("result:{}".format(result))
        
    