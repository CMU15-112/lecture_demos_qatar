def f(x):
    print(x)
    return 42

def ct(x):
    counter = 0
    target = x
    for i in range(5, -1, -2):
        if counter == target:
            print("meet", counter)
            target += 1
        else:
            print("miss", target)
        counter += 2
    return f(counter)

ct(2)  # starts here
