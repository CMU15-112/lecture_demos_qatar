class Cart(object):
    
    def __init__(self, itemsStr):
        l= itemsStr.lower().split(",")
        self.items= set(l)
        self.status = 'open'
     
    def itemCount(self):
        return len(self.items)
    
    def getItems(self):
        return self.items
    
    def addItem(self, item):
        i = item.lower()
        if self.status == 'open' and (i not in self.items):
            self.items.add(i)
            return True
        
        return False
    
    def checkout(self):
        if self.status == 'open':
            self.status = 'closed'
    
    def __repr__(self):
        return f"Shopping Cart: {self.itemCount()} item(s)"
    
class WishList(Cart):
    
    def __repr__(self):
        return f"Wish List: {self.itemCount()} item(s)"

    def checkout(self):
        return

################## TEST CASES ###########################
# A (Shopping) Cart takes a string (not a list) of comma-separated items
# A cart stores items, and items are case insensitive
m1 = Cart('milk,eggs,MILK')
assert(m1.itemCount() == 2)
# milk and eggs
# The .getItems method should return a set of unique items present in the cart
assert(m1.getItems() == {'milk', 'eggs'}) # Note that these items are lowercase. Ignore case and duplicates
m2 = Cart('Tomatoes,ONION,water,chips,CHIPS')
assert(m2.getItems() == {'tomatoes','onion','water','chips'})
assert(m2.itemCount() == 4) # Still just four items
assert(str(m2) == "Shopping Cart: 4 item(s)")
m3 = Cart('MILK')
assert(str(m3) == "Shopping Cart: 1 item(s)") # You can add one new item at a time:
assert(m3.addItem('milk') == False) # Return False if the item is already present
assert(m3.addItem('eggs') == True) # Return True if we added a new item
assert(m3.itemCount() == 2)
assert(m3.getItems() == {'milk', 'eggs'})
assert((m3.getItems() == m1.getItems()) and (m3.getItems() != m2.getItems())) # Once more, but with a new item:
assert(m3.addItem('water') == True) # True means the item was added!
# and so these all change:
assert(m3.itemCount() == 3)
assert(m3.getItems() == {'milk', 'eggs','water'})
# Lastly, all carts start out open
assert(m1.status == 'open') # ...unless you pay them
m1.checkout()
assert(m1.status == 'closed')
m1.checkout()
assert(m1.status == 'closed') # still closed
# and you cannot add any more items
assert(m1.addItem('tomatoes') == False) # Return False if the cart has been checked out
assert(m1.status == 'closed') # still closed

# A Wish List is a shopping cart that it always remains open
w1 = WishList("LEMON")
assert(str(w1) == "Wish List: 1 item(s)")
assert(w1.itemCount() == 1)
assert(w1.getItems() == {'lemon'})
assert(w1.addItem("Salt") == True)
assert(w1.getItems() == {'lemon', 'salt'})
assert(w1.status == 'open')
w1.checkout() # does nothing, the wish list stays open
assert(w1.status == 'open')
print("PASSED !!")