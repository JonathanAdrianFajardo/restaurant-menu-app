class RestaurantMenu:
  def __init__(self):
    self.menu_items = {}

def add_item(self, name, price):
  self.menu_items[name] = price

def get_price(self, name):
  return self.menu_items.get(name, None)

def display_menu(self):
print("Menu Items:")
  for item, price in self.menu_items.items():
    print (f"{item}: ${price:.2f}")

def main():
  menu = RestaurantMenu()
  # Add initial menu items
  menu.add_item("Burger", 10.99)
  menu.add_item("Fries", 4.99)


# Display Menu
 menu.display_menu()
   
if __name__ == "__main__":
  main()
