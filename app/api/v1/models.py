
class Order:
    order_id = 1
    def __init__(self,name,description,id,price,status = "pending"):
        self.name =  name
        self.description =  description
        self.id = Order.order_id
        self.status = status
        self.price = price

        order_id = +1
     