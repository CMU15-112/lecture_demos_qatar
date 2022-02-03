lionelMessi = [2009, 2010, 2011, 2012, 2015, 2019, 2021]
leo = lionelMessi
laPulga = lionelMessi# the flea
messi = lionelMessi


lionelMessi.append(2022)
# Assume Lionel Messi wins the ballon d'or 2022,
# if I ask
# did la pulga win the ballon d'or this year?  -> Yes
# did messi win the ballon d'or this year?  -> Yes

print("lionel messi won 2022 award?",2022 in lionelMessi)


print("la pulga won 2022 award?",2022 in laPulga)



print("lionelMessi =", lionelMessi)
print("leo =", leo)
print("laPulga =", laPulga)

print("lionelMessi == leo?", lionelMessi == leo)
print("lionelMessi == laPulga?", lionelMessi == laPulga)