import tkinter as tk
from tkinter import messagebox
import random

meal_type_vars = []
recipe_categories = ["breakfast", "lunch", "dinner", "snack", "dessert"]
meal_plans = {day: [] for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}
day_meal_entries = {}

def data_base(file_name): #takes recipes from text files in sepcific format
    recipes = []
    current_recipe = None
    ingredients_list = []
    with open (file_name) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.endswith(':'):
                if current_recipe:
                    current_recipe['ingredients'] = ingredients_list
                    recipes.append(current_recipe)
                recipe_name = line[:-1]
                current_recipe = {'name': recipe_name}
                ingredients_list = []
            else:
                ingredients = line.split(',')
                item = ingredients[0].strip()
                product_code = ingredients[1].strip()
                price = ingredients[2].strip()
                ingredients_list.append({'item': item, 'product code': product_code, 'price': price})

     
        if current_recipe:
            current_recipe['ingredients'] = ingredients_list
            recipes.append(current_recipe)
    return recipes

def choice_list(file_name): #returns recipes for each type of meal (breakfast, lunch, dinner, snack, dessert)
    return data_base(file_name)

breakfast_recipes = choice_list("breakfast.txt")
lunch_recipes = choice_list("lunch.txt")
dinner_recipes = choice_list("dinner.txt")
dessert_recipes = choice_list("desserts.txt")
snack_recipes = choice_list("snacks.txt")

def create_meal_blocks(): #verifies user input (number of meals), resets widgets and input for each run & takes type of meals for each day from user
   day_meal_numbers = {}
   for day, entry in day_meal_entries.items():
        try:
            meals = int(entry.get())
            if meals < 1 or meals > 10:
                raise ValueError
            day_meal_numbers[day] = meals
        except ValueError:
            messagebox.showerror("Error", f"Enter a valid number of meals for {day}")
            return
   for widget in meals_frame.winfo_children():
        widget.destroy()
   meal_type_vars.clear()
   for day in meal_plans:
        meal_plans[day] = []
   for day in meal_plans.keys():
        meals = day_meal_numbers.get(day, 1)
        tk.Label(meals_frame, text=f"{day}:", fg="#6C548C", bg="#B4A0C3", font=("Arial", 14, "bold")).pack(anchor="w")
        day_vars = []
        for _ in range(meals):
            var = tk.StringVar(value=recipe_categories[0])
            tk.OptionMenu(meals_frame, var, *recipe_categories).pack(fill="x", pady=2)
            day_vars.append(var)
        meal_type_vars.append(day_vars)

def generate_shopping_list(): #generates shopping list containing random recipes
    if not meal_type_vars:
         messagebox.showerror("Error", "Set meals first")
         return

    with open("shopping_list.txt", "w") as f:
        for day, day_vars in zip(meal_plans.keys(), meal_type_vars):
            f.write(f"\nMeals for {day}:\n")

            for var in day_vars:
                recipe_type = var.get()
                if recipe_type == "breakfast":
                    chosen = random.choice(breakfast_recipes)
                elif recipe_type == "lunch":
                    chosen = random.choice(lunch_recipes)
                elif recipe_type == "dinner":
                    chosen = random.choice(dinner_recipes)
                elif recipe_type == "snack":
                    chosen = random.choice(snack_recipes)
                else:
                    chosen = random.choice(dessert_recipes)

                meal_plans[day].append(chosen)  

                f.write(chosen["name"] + "\n")
                for ing in chosen["ingredients"]:
                    f.write(f" - {ing['item']}, {ing['product code']}, {ing['price']}\n")
                f.write("\n")  

    messagebox.showinfo("Success", "Shopping list saved to shopping_list.txt")


root=tk.Tk() #main application window
root.title("Random Recipe Selector")
root.geometry("450x550")
root.configure(bg="#B4A0C3")

top_frame = tk.Frame(root)
top_frame.pack(pady=10, fill="x")
top_frame.configure(bg="#B4A0C3")

tk.Label(top_frame, text="Number of meals per day:", bg="#6C548C" , fg="#FFFFFF", font=("Arial", 18, "bold")).pack(anchor="w")
for day in meal_plans.keys(): #display input boxes for each day (number of meals)
    frame = tk.Frame(top_frame)
    frame.pack(anchor="w", pady=2)
    tk.Label(frame, text=f"{day}: ", bg="#FFFFFF", fg="#6C548C", font=("Arial",12, "bold" )).pack(side="left")
    entry = tk.Entry(frame, width=5, bg="#FFFFFF", fg="#6C548C", insertbackground="#B4A0C3", font=("Arial", 12))
    entry.pack(side="left", padx=5)
    day_meal_entries[day] = entry


tk.Button(top_frame, text="Set Meals", command=create_meal_blocks,bg="#6C548C", fg="#FFFFFF", font=("Arial", 12, "bold")).pack(side="left", padx=10)

middle_frame = tk.Frame(root)
middle_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(middle_frame)
scrollbar = tk.Scrollbar(middle_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set, bg="#B4A0C3") #setting a scrollbar to middle_frame

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event): #updates middle frame regularly whenever user scrolls
   canvas.configure(scrollregion=canvas.bbox("all"))
    
scrollable_frame.bind("<Configure>", on_frame_configure)

meals_frame = tk.Frame(scrollable_frame)
meals_frame.pack(pady=10, fill="x")
meals_frame.configure(bg="#B4A0C3")


tk.Button(root, text="Generate Shopping List", command=generate_shopping_list, width=25, fg="#FFFFFF", bg="#6C548C", font=("Arial", 14, "bold")).pack(pady=10)

root.mainloop()