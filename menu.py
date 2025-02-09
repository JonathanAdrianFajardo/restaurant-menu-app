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

  def remove_item(self, name):
    if name in self.menu_items:
      del self.menu_items[name]
      return True
    return False
  
  def update_price(self, name, new_price):
        if name in self.menu_items:
            self.menu_items[name] = new_price
            return True
        return False

def main():
    menu = RestaurantMenu()
    # Add initial menu items
    menu.add_item("Burger", 10.99)
    menu.add_item("Fries", 4.99)
    
    menu.display_menu()
      
    menu.remove_item("Fries")
    print("remove successfully ")

    # Update the price of an item
    updated = menu.update_price("Burger", 12.99)
    if updated:
        print("Price updated successfully.")
    else:
        print("Item not found.")

    # To verify the update
    price = menu.get_price("Burger")
    print(f"Updated price of Burger: {price}")
    
    menu.display_menu()

if __name__ == "__main__":

  main()
