# Weekly Meal Planner & Shopping List Generator

A desktop application built with **Python** and **Tkinter** that helps users plan meals for an entire week. Users choose the number and type of meals for each day, and the application randomly selects recipes and exports their ingredients to a text file.

Originally developed as a university course project.

## Features

- **Seven-day meal planning:** Plan meals from Sunday through Saturday.
- **Flexible meal count:** Choose between 1 and 10 meals for each day.
- **Five recipe categories:** Breakfast, lunch, dinner, snacks, and desserts.
- **Random recipe selection:** Generate a recipe for each chosen meal category.
- **Ingredient details:** Each recipe includes ingredient names, product codes, and listed prices in GBP (£).
- **Text-file export:** Save the weekly selections and their ingredients to `shopping_list.txt`.
- **Graphical interface:** Use dropdown menus, buttons, validation messages, and a scrollable layout.

## Built With

- **Python 3**
- **Tkinter** for the graphical user interface
- **Python standard library** (`random` and `tkinter`)
- **Text files** for recipe data and generated output

No third-party Python packages are required. Your Python installation must include Tkinter and support desktop windows.

## Getting Started

### 1. Download the project

Clone this repository, or select **Code → Download ZIP** on GitHub and extract it.

### 2. Open a terminal in the project folder

Make sure you are in the same folder as `main.py` and the five recipe `.txt` files. The application reads those files using relative paths.

### 3. Run the application

**Windows:**

```bash
py main.py
```

**macOS or Linux:**

```bash
python3 main.py
```

If `py` is not available on Windows, try `python main.py`. On Linux, you may need to install the operating system's Tkinter package (often named `python3-tk`).

## How to Use

1. Enter the **number of meals** for each day of the week (a whole number from **1 to 10**).
2. Click **Set Meals** to generate the meal-category dropdowns.
3. Choose **breakfast**, **lunch**, **dinner**, **snack**, or **dessert** for each meal.
4. Click **Generate Shopping List**.
5. Find the generated **`shopping_list.txt`** in the project folder. It contains the selected recipes and their ingredient details, grouped by day.

The app displays an error message if a daily meal count is invalid or if the user attempts to generate a list before setting the meals.

## Project Structure

```text
weekly-meal-planner/
├── main.py          # Tkinter GUI, input validation, recipe selection, and export
├── breakfast.txt    # Breakfast recipes
├── lunch.txt        # Lunch recipes
├── dinner.txt       # Dinner recipes
├── snacks.txt       # Snack recipes
├── desserts.txt     # Dessert recipes
├── README.md        # Project documentation
└── .gitignore       # Files excluded from version control
```

The program creates `shopping_list.txt` when you generate a meal plan. This output file is intentionally not included in the repository.

## Recipe Data Format

Recipes are stored in plain-text files. Each recipe begins with a name followed by a colon; each subsequent line lists an ingredient, a product code, and a listed price, separated by commas:

```text
Omelet:
Eggs, 5000326012065, £1.82
Butter, 5054781649939, £1.08
```

The included recipe files contain **42 recipes** across the five categories.

## Current Limitations

- Recipes are selected randomly, so the same recipe may appear more than once.
- The exported file lists ingredients **by selected recipe**; it does not combine duplicate ingredients into a single aggregated shopping list.
- Listed product prices are static reference data. The application does not look up live prices or calculate a total budget.
- Generating a new plan replaces the previous contents of `shopping_list.txt`.
- The application runs as a local desktop GUI, not as a web application.

## Future Improvements

Possible enhancements include ingredient consolidation, estimated cost totals, dietary filters, and saving or reloading meal plans.
