user = {
    "Name": "TANMAY DAS",
    "Age": 23,
    "Address": "1353/Bhuyian Lodge, Pahartoli Signal Colony, Chattogram",
    "Email": "tanmaydas304@gmail.com",
    "id_info_verified": True
}

print(user)

print(user["Name"])
print(user["Age"])
print(user["Address"])
print(user["Email"])
print(user["id_info_verified"])

#using get method to find available values
print(user.get("password"))
print(user.get("id_info_verified"))

#changing existing values
user["Age"] = 22
print(user)

#assigning new key
user["Occupation"] = "Student"
print(user)
