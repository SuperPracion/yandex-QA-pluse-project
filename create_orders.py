import data

def create_order(firstName = "Naruto", 
                 lastName = "Uchiha", 
                 address = "Konoha, 142 apt.", 
                 metroStation = 1, 
                 phone = "+7 800 355 35 35",
                 rentTime = 1, 
                 deliveryDate = "2023-09-23",
                 comment = "Saske, come back to Konoha", 
                 color = ["BLACK"]):
    
    pattern = data.order.copy()
    
    pattern["firstName"] = firstName
    pattern["lastName"] = lastName
    pattern["address"] = address
    pattern["metroStation"] = metroStation
    pattern["phone"] = phone
    pattern["rentTime"] = rentTime
    pattern["deliveryDate"] = deliveryDate
    pattern["comment"] = comment
    pattern["color"] = color
    
    return pattern
