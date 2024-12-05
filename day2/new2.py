pc = ["hp",  "dell", "lenovo", "asus"]
print(pc)

z= len(pc)
print(z) # it will give yo the length of the list

pc.append("moto")
print(pc) # this wll add "moto" at last index

x= pc.pop()
print(pc)
print(x) # it will remove the last indexed element
print(pc)

pc.remove("hp")
print(pc) #it will remove the element we want

print(type(pc))
