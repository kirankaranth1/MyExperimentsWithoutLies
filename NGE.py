def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def printNGE(arr):
    s = createStack()
    element = 0
    next = 0
    push(s, arr[0])

    for i in range(1, len(arr)):
        next = arr[i]

        if not isEmpty(s):
            element = pop(s)

            while element < next:
                print(str(element)+" -- "+str(next))
                if isEmpty(s):
                    break
                element = pop(s)

            if element >= next:
                push(s, element)

        push(s, next)

    while not (isEmpty(s)):
        e = pop(s)
        print(str(e) + " -- " + "-1")

arr = [11, 13, 21, 3, 6, 27, 20, 22]
printNGE(arr)