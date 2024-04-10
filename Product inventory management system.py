
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price
    
    def update_quantity(self, new_quant):
        self.quantity = new_quant

    @staticmethod
    def inventory_info(product):
        print("\nProduct Details:")
        for prod in product:
            print(f'Name: {prod.name}\nPrice: {prod.price}\nQuantity: {prod.quantity}\n')

    def calc_inventory(self):
        return self.price * self.quantity

    @staticmethod
    def total_inventory(product):
        total_val = 0
        for t_v in product:
           total_val += t_v.calc_inventory()
        return total_val
    
    @staticmethod
    def expensive_prod(product):
        products = []
        for p in product:
            products.append(p.price)
        max_price = max(products)

        for n in product:
            if n.price == max_price:
                return n

    
product1 = Product('Sneakers', 5000, 1)
product2 = Product('BackPack', 2200, 2)
product3 = Product('Stoler', 900, 2)
product4 = Product('Abaya', 8000, 1)

product3.update_price(500)
product3.update_quantity(7)

total_inventory = Product.total_inventory([product1,product2,product3,product4])
most_expensive = Product.expensive_prod([product1,product2,product3,product4])

Product.inventory_info([product1,product2,product3,product4])
print(f'Total Inventory: Rs.{total_inventory}')
print(f'Most Expensive Product: {most_expensive.name}\n')