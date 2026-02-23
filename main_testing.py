from endpoint.GenericModelv2 import *

columns = "name,email,password_hash,role".split(",")
columns = tuple(columns)
user = GenericModel("user", columns)

values = {
        "name" : "Madhavamamama",
        "email" : "mad@vbn",
        "password_hash" : "1212",
        } 
user.insert(values)
