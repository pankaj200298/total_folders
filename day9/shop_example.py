from cloudinit.util import append_file

products = [
    {"id":1, "name":"t-shirt", "price": "$12.99" , "created_date": "2022-01-01", "is_on_sale": False, "sale_price" : None},
    {"id":2, "name":"shoes", "price": "$22.45" , "created_date" : "2022-01-01" , "is_on_sale": True, "sale_price" : None},
    {"id":3, "name":"pant", "price": "$43.00" , "created_date" : "2022-01-01" , "is_on_sale": False, "sale_price" : None},
    {"id":4, "name":"shirt", "price": "$14.95", "created_date": "2022-01-01", "is_on_sale": True, "sale_price": 7.99},
    {"id":5, "name":"phone", "price": "$32.50", "created_date": "2022-01-01", "is_on_sale": True, "sale_price": None},
    {"id":6, "name":"bag", "price": "$160.00", "created_date": "2022-01-01", "is_on_sale": False, "sale_price": None},
]
print("printing example 1 =============")
print("========== printing the name of products ===================")

for product in products:
    print(product["name"])

print("printing example 2 =============")
print("===printing the products name which on sale with price ===== ")

for sale in products :
    if sale["is_on_sale"]:
        print(sale["name"])
        print(sale["price"])

print("printing example 3 =============")
print("===== printing the products wich are below 25 $ ======")


for low in products :
    temp_price = low["price"].replace("$","")
 #   temp_price = low["price"][1:] both are same option 
    price = float(temp_price )
    if price < 25.00 :
        print(low["name"])
        print(low["price"])

print("=if sale price is avilable then name of products in list ")
sale_price = []
for available in products :
    if available["sale_price"] :
       sale_price.append(available["name"])
print(sale_price)
