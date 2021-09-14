# non-destructive functions
lionelMessi = [2009, 2010, 2011, 2012, 2015, 2019]
leo = lionelMessi
laPulga  = lionelMessi # the flea
messi = lionelMessi

def nondestructiveGive2021Award(player):
    # how can I add an item without altering the original list?
    clone = player[:]
    clone.append(2021)
    return clone
    
    
lionelMessi = nondestructiveGive2021Award(laPulga)

print("lionelMessi = ", lionelMessi)
print("leo = ", leo)
print("laPulga = ", laPulga)
print("messi = ", laPulga)