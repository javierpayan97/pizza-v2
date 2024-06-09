class Pizza:
    def __init__(self, name, price, ingredients,vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGETARIAN"
        print(f"PIZZA {self.name} : {self.price}$" + veg_str)
        print(", ".join(self.ingredients))
        print()

def pizza_sort(e):
    return len(e.ingredients)

class CustomPizza(Pizza):
    last_number = 0
    def __init__(self):
        CustomPizza.last_number +=1
        self.number = CustomPizza.last_number
        super().__init__("Custom " + str(self.number), 0, [])
        self.ask_user_for_ingredients()
        self.ask_user_for_price()
    
    def ask_user_for_ingredients(self):
        while True:
            ingredient = input(f"Add an ingredient for pizza number {self.number} (or press ENTER to finish): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def ask_user_for_price(self):
        while True:
            price_str = input("Add price: ")
            try:
                price_float = float(price_str)
                self.price = price_float
                return
            except:
                print("ERROR: Please enter a number")
           
pizzas = [
    Pizza("4 cheeses",8.99,("blue cheese", "brie", "emmental","mozarella")),
    Pizza("marinara", 9.90,("marinara souce","garlic", "olive oil", "basil", "oregano")),
    Pizza("bolognese", 7.99,("bolognese sauce", "mozzarella")),
    Pizza("calzone",13.99,("Folded pizza", "ingredients vary")),
    Pizza("vegetarian",6.99,("tomato", "lettuce", "onion"),True),
    CustomPizza(),
    CustomPizza()
]

pizzas.sort(key=pizza_sort)
#filters
#1 - Display only vegetarian
#2 - Display only non-vegetarian
#3 - Only pizzas that has tomato
#4 - Only pizzas less than 10$
filter_int = 0
while filter_int <= 0 or filter_int>=5:
    filter_str = input("Select an option\n1 - Display only vegetarian\n2 - Display only non-vegetarian\n3 - Only pizzas that has tomato\n4 - Only pizzas less than 10$\n")
    try:
        filter_int = int(filter_str)
    except:
        print("Error, please select a correct option")

for i in pizzas:
    if filter_int == 1:
        if i.vegetarian == True:
            i.display() 
    elif filter_int == 2:
        if i.vegetarian == False:
            i.display() 
    elif filter_int == 3:
        if "tomato" in i.ingredients:
            i.display()
    elif filter_int == 4:
        if i.price < 10:
            i.display()  
