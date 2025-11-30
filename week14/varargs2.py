def myFlexibleFunc0(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
    boring = kwargs.get('boring', False)
    if not boring:
        print("I'm glad you are not bored")
    else:
        print(":(")
        
        
def myFlexibleFunc1(first, *args, boring=False, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
    if len(args):
        print(f'first one is {args[0]}')
    if not boring:
        print("I'm glad you are not bored")
    else:
        print(":(")

#myFlexibleFunc1(happy=True, 3, boring=False)  # it won't work
myFlexibleFunc1(42, 4,6,8,9, happy=True, boring=False)
myFlexibleFunc0(42, 4,6,8,9, happy=True)
    
        

        
