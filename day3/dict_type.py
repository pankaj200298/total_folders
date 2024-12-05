capital = {"maharashtra": "mumbai", "vidharbha": "nagpur", "gujrat": "ahemdabad", "DELHI": "delhi"}

print(capital)

print(type(capital))
print(capital["maharashtra"])
x = (capital["gujrat"])
print(x)

karnataka_capital = capital.get("karnataka")
print(karnataka_capital)
# One of the main advantages of using .get() is that it allows you to provide
# a default value if the key is not found. This prevents KeyError exceptions
# that would occur if you try to access a non-existent key directly.
print("printing for asam................")
print(capital.get("asam"))

print("==============================================================================")
print(" befor add ")
print(capital)
print("after add ")
capital["karnataka"] = "mysur"
# this is use to add new key and value

print(capital)
print("=============================================================================")
# option two OR method two

print("printing option two...................... ")

print(capital)
capital.update({"punjab": "amritsar"})
print(capital)

print("========================================================")

print("adding the key that already exist ......... ")
# capital["karnataka"] = "mysur"
capital["maharashtra"] = "amravati"
print(capital)
# if try to add existing  key for new value it will update for new key

capital.setdefault("A.P", "amravati")
print(capital)
print("=======================")
##################################################
#how o acsess the keys and values of dictonary
print("========++++++++++++++++++==========")
print(capital)
print("printing the keys and values")
print(capital.keys())
print(capital.values())
#keys and values of dict.  we can not acess by indexing
#so we have to convert it into the list
A = list(capital.keys())[1]
B = list(capital.values())[1]
print(A)
print(B)