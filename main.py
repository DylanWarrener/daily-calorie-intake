'''
Getting the right amount of protein per day depends on three types of training. 

Plan: 
1. Begin with the recomp phase to build muscle and lose fat at the same time.
2. Once you have the muscle and the desired fat, change to bulking phase. 
3. Finally, to reduce fat further change to cutting phase to get a defined physique.

- Cutting (increase protein): fewer calories from food, so less body fat. Much more likely to break down muscle tissue as a fuel source.
    Between 1.8 - 2.7g per kg of bodyweight
    Between 0.8 - 1.2g per lb of bodyweight
        1. 1.8 
        2. 2.0
        3. 2.2
        4. 2.3
        5. 2.5
        6. 2.7
^- Bulking (less protein): build a lot of muscle and bulk. Well fed, so your body is less likely to break down muscle tissue as a fuel source.
    Between 1.6 - 2.2g per kg of bodyweight
    Between 0.7 - 1.0g per lb of bodyweight
        1. 1.6 
        2. 1.7
        3. 1.8
        4. 2.0
        5. 2.1
        6. 2.2
^- Recomp (): build muscle and lose fat at the same time. 
    Between 1.6 - 2.2g per kg of bodyweight
    Between 0.7 - 1.0g per lb of bodyweight
        1. 1.6 
        2. 1.7
        3. 1.8
        4. 2.0
        5. 2.1
        6. 2.2

no_exercise = 1
little_to_no_exercise = 1.2
slightly_active = 1.37
moderately_active = 1.55
very_active = 1.725
extremely_active = 1.9
'''

import person as p
import ingredients as i
import recipes as r

# Work out how many calories to eat of what Macronutrient
dylan = p.Person("male", 78, 5.7, 26, 1.37, 0.15)

print(dylan.daily_calorie_intake)
print("---------------------------------------------------------------")
dylan.getDailyMacronutrientPercentage()
print("---------------------------------------------------------------")
dylan.getDailyMacronutrientCalorieIntake()
print("---------------------------------------------------------------")
dylan.getDailyMacronutrientGramsIntake()
print("---------------------------------------------------------------")
dylan.getDailyMacronutrientForMealTimeInGrams()
print("---------------------------------------------------------------")

# Work out what ingredients are needed for my food schedule
dylanRecipes = r.Recipies()
dylanIngredients = i.Ingredients()

# Get recipies for week 
week_1_recipes = {
    "monday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkSummerFruitsAndBananaSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "honeyAndMustardWithEggs"), 
        "dinner": dylanRecipes.getRecipe("dinner", "sausageAndEggOpenPancake")
    },
    "tuesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkBlackForestFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "soyBeanChilliGingerStirFry"), 
        "dinner": dylanRecipes.getRecipe("dinner", "loadedSweetPotatoeSkin")
    },
    "wednesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkMangoAndPineapppleSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "creamySpinachChicken"), 
        "dinner": {}
    },
    "thursday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkSummerFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "quinoaSaladWithHalloumi"), 
        "dinner": dylanRecipes.getRecipe("dinner", "roastedButternutSquashCurry")
    },
    "friday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkBlueberriesSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "pepperedMackerelSpaghetti"), 
        "dinner": {}
    }
}

'''
week_2_recipes = {
    "monday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkSummerFruitsAndBananaSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "tandooriPrawnNaans"), 
        "dinner": dylanRecipes.getRecipe("dinner", "turkeyStuffedTomatoes")
    },
    "tuesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkBlackForestFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "vegetablePilaf"), 
        "dinner": dylanRecipes.getRecipe("dinner", "greekPotatoesWithLemon")
    },
    "wednesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkMangoAndPineapppleSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "stickyBeefWithCashews"), 
        "dinner": dylanRecipes.getRecipe("dinner", "spinachAndCheeseOmelette")
    },
    "thursday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkSummerFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "quinoaSaladWithHalloumi"), 
        "dinner": dylanRecipes.getRecipe("dinner", "handHeldSaltAndPepperPrawns")
    },
    "friday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkBlueberriesSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "tunaButterBeanPie"), 
        "dinner": {}
    }
}

week_3_recipes = {
    "monday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkSummerFruitsAndBananaSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "codLentilBeetrootTraybake"), 
        "dinner": dylanRecipes.getRecipe("dinner", "miniPizzas")
    },
    "tuesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkBlackForestFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "roastedButternutSquashCurry"), 
        "dinner": dylanRecipes.getRecipe("dinner", "handHeldSaltAndPepperPrawns")
    },
    "wednesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkMangoAndPineapppleSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "sweetPotatoAndChickenTraybake"), 
        "dinner": dylanRecipes.getRecipe("dinner", "spinachAndCheeseOmelette")
    },
    "thursday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkSummerFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "speedyVeggieNoodles"), 
        "dinner": dylanRecipes.getRecipe("dinner", "miniPizzas")
    },
    "friday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkBlueberriesSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "troutFilletsWithAHazelnutCrust"), 
        "dinner": dylanRecipes.getRecipe("dinner", "turkeyStuffedTomatoes")
    }
}

week_4_recipes = {
    "monday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkSummerFruitsAndBananaSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "sardineAndTomatoSpaghetti"), 
        "dinner": dylanRecipes.getRecipe("dinner", "smokyChipotleAdzukiBeanChilli")
    },
    "tuesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkBlackForestFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "vegetableNasiGoreng"), 
        "dinner": dylanRecipes.getRecipe("dinner", "roastedSpicedBroccoliSoup")
    },
    "wednesday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkMangoAndPineapppleSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "kungPaoBeef"), 
        "dinner": dylanRecipes.getRecipe("dinner", "peaAndHamSoup")
    },
    "thursday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "greenMilkSummerFruitsSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "superLentilAndVegetableSoup"), 
        "dinner": dylanRecipes.getRecipe("dinner", "stuffedCeleriacWithParsnips")
    },
    "friday": {
        "breakfast": dylanRecipes.getRecipe("breakfast", "almondMilkBlueberriesSmoothie"),
        "lunch": dylanRecipes.getRecipe("lunch", "haddockWithSweetPotatoFries"), 
        "dinner": dylanRecipes.getRecipe("dinner", "sausageAndEggOpenPancake")
    }
}
'''

# Pass weekly recipes into ingredients to calculate total required ingredients
print("Week 1 ingredients")
dylanIngredients.calculateTotalIngredients(week_1_recipes)
print("---------------------------------------------------------------")

'''
print("Week 2 ingredients")
dylanIngredients.calculateTotalIngredients(week_2_recipes)
print("---------------------------------------------------------------")

print("Week 3 ingredients")
dylanIngredients.calculateTotalIngredients(week_3_recipes)
print("---------------------------------------------------------------")

print("Week 4 ingredients")
dylanIngredients.calculateTotalIngredients(week_4_recipes)
print("---------------------------------------------------------------")
'''