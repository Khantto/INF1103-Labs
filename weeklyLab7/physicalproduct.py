from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product):
    def __init__(self,product_id,name,price,stock,weight):
        super().__init__(product_id,name,price,stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.weight, "kg\n")

    def get_weights(self):
        return self.weight

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_cost = self.weight * 0.25
        return shipping_cost
    



        
    
