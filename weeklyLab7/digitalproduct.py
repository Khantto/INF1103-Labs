from product import Product

class DigitalProduct(Product):
    def __init__(self,product_id,name, price, stock,download_size):
        super().__init__(product_id,name,price,stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download size:", self.download_size,"MB\n")

    def get_download_size(self):
            return self.download_size

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

        

