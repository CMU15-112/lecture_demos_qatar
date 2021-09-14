# function arguments are aliases
lionelMessi = [2009, 2010, 2011, 2012, 2015, 2019]
leo = lionelMessi
laPulga  = lionelMessi # the flea
messi = lionelMessi

def give2021Award(player):
    player.append(2021)

give2021Award(leo)

print("lionelMessi = ", lionelMessi)
print("leo = ", leo)
print("laPulga = ", laPulga)
print("messi = ", laPulga)
