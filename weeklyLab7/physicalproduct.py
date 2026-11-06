from product import Product
class PhysicalProduct(Product):
    def __init__(self,product_id,name,price,stock,weight):
        super().__init__(product_id,name,price,stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.weight, "kg")
        
        
    
