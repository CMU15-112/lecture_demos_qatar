# Write a program that repeatedly asks the user
# for multiple positive integer values,
# as soon as zero is given,
# print the values in increasing order (excluding the last zero).

l = []  # l is a list

while True:
    v = int(input("Enter one positive value, zero to finish: "))
    if v == 0:
        break
    l.append(v)
    print("I have received ", len(l))
    
print("final list ", l)
print("sorted list: ", sorted(l))
print("good bye")
