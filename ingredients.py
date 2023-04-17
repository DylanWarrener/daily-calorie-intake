class Ingredients:
    def __init__(self) -> None:
        self.allUnitsForIngredients = {
            "g": {
                "dry": [
                    "babyPotato",
                    "dill",
                    "pennePasta",
                    "cashewNuts",
                    "bulgarWheat",
                    "butterBeans", 
                    "greenLentils",
                    "chickpeas",
                    "whiteBreadcrumbs",
                    "choppedHazlenuts",
                    "spaghetti",
                    "roastedPeanuts",
                    "redLentils",
                    "mixedNuts",
                    "couscous",
                    "wheatFlour",
                    "proteinPowder",
                    "oats",
                    "whitePotatoes",
                    "sweetPotatoes",
                    "ketchup"
                ],
                "fridge": [
                    "lettuce",
                    "fetaCheese",
                    "goatsCheese"
                    "stemmedBroccoli",
                    "halloumi",
                    "beetroot",
                    "pittedOlives",
                    "unsaltedButter",
                    "springGreens",
                    "whiteBread",
                    "cheese",
                    "ham",
                    "turkeyHam",
                    "turkey",
                    "sugarsnapPeas",
                    "spinach",
                    "beanSprouts",
                    "sundriedTomatoes",
                    "manchego",
                    "fineBeans",
                    "leek",
                    "radishes",
                    "tofu",
                    "redCabbage",
                    "lightCreamCheese"
                ],
                "freezer": [
                    "chickenDrumsticks",
                    "soybean",
                    "chicken",
                    "kingPrawns",
                    "carrot",
                    "peas",
                    "mixedVegetables",
                    "summerFruitsAndBanana", 
                    "blackForestFruits", 
                    "mangoAndPineapple", 
                    "summerFruits", 
                    "blueberries",
                    "mince"
                ]
            },
            "cup": {
                "dry": [
                    "rice",
                    "quinoa",
                ],
                "fridge": [
                    "kale",
                ],
                "freezer": [
                    "ice",
                ]
            },
            "tsp": {
                "dry": [
                    "chilliFlakes",
                    "garlicPaste"
                    "garlicPowder"
                    "onionPowder"
                    "oregano",
                    "cinnamon",
                    "turmeric",
                    "ginger",
                    "garlic",
                    "honey",
                    "cornflour",
                    "parsley",
                    "whiteWineVinegar",
                    "curryPowder",
                    "granulatedSugar",
                    "cuminSeeds",
                    "cumin",
                    "chilliPowder",
                    "corriander",
                    "mixedSpice",
                    "chineseFiveSpice",
                    "chipotleChilliPaste",
                    "garamMasala",
                    "poppySeeds",
                    "mixedHerbs",
                    "stockPowder",
                    "thyme",
                    "chives",
                    "nutmeg",
                    "paprika",
                    "cayennePepper",
                    "basil",
                    "mint",
                    "rainbowPeppercorns",
                    "casterSugar",
                    "vinegar",
                    "sesameSeeds"
                ],
                "fridge": [
                    "frenchMustard",
                    "horseradishSauce",
                    "chipotlePaste",
                ],
                "freezer": [
                    
                ]
            },
            "tbsp": {
                "dry": [
                    "sriracha",
                    "cidarVinegar",
                    "oliveOil",
                    "sesameOil",
                    "chiaSeeds",
                    "hempSeeds",
                    "flaxSeeds",
                    "sunflowerOil",
                    "soySauce",
                    "groundNutOil",
                    "oysterSauce"
                    "coconutOil",
                    "vegetableOil",
                    "plainFlour",
                    "riceWineVinegar",
                    "grapeseedOil"
                ],
                "fridge": [
                    "frenchDressing",
                    "cranberrySauce",
                    "sundriedTomatoPuree",
                    "coleslaw"
                ],
                "freezer": []
            },
            "ml": {
                "dry": [],
                "fridge": [
                    "souredCream",
                    "singleCream",
                    "choppedTomatoes",
                    "coconutMilk",
                    "cremeFraiche",
                    "greenMilk",
                    "almondMilk",
                    "fatFreeGreekYoghurt",
                ],
                "freezer": []
            },
            "whole": {
                "dry": [
                    "whiteWraps",
                    "brownWraps",
                    "lebaneseBread",
                    "mackerel",
                    "chickenStock",
                    "wholegrainRiceWithQuinoa",
                    "eggs",
                    "vegetableStock",
                    "herbAndTomatoeSauce",
                    "tuna",
                    "butternutSquash",
                    "sardines", 
                    "cornichons",
                    "whitePotato",
                    "thymeSprigs",
                    "tinnedButterBeans", 
                    "tinnedPlumTomatoes", 
                    "tinnedCannelliniBeans", 
                    "bakingPotato",
                    "bayLeaves",
                    "starAnise",
                    "yeast",
                    "tacoMixedBeansInTomatoSauce",
                    "noodles",
                    "sweetPotato",
                ],
                "fridge": [
                    "mozzarella",
                    "gherkins",
                    "lemon",
                    "cucumber",
                    "redChillies",
                    "redPepper",
                    "tomato",
                    "broccoli",
                    "bananaShallots",
                    "pakChoi",
                    "celeryStick",
                    "romaineLettuce",
                    "celeriac",
                    "parsnips",
                    "beefTomato",
                    "springOnion",
                    "lime",
                    "cherryTomatoes",
                    "redOnion",
                    "whiteOnion",
                    "courgette",
                ],
                "freezer": [
                    "naanBread",
                    "sirloinSteak",
                    "codFillets",
                    "troutFillets",
                    "haddockFillets",
                    "sausages",
                    "salmonFillet",
                ]
            },
            "slices": {
                "dry": [],
                "fridge": [
                    "gherkinSlices"
                ],
                "freezer": []
            }
        }
        
    def printRecipeToScreen(self, ingredients_to_print) -> None:
        for storage_key, storage_value in ingredients_to_print.items():
            print(storage_key)
            
            for items in storage_value:
                print("        " + str(items))
    
    def calculateUnitTypeForIngredients(self, bundled_ingredients):
        weekly_ingredients = {}
        
        for unitKey, unitValue in self.allUnitsForIngredients.items():
            for storageTypeKey, storageTypeValue in unitValue.items():
                # If there is nothing inside the storage type value continue, else add to list
                if not storageTypeValue:
                    continue
                else:
                    for ingredient in storageTypeValue:
                        if ingredient in bundled_ingredients:
                            if storageTypeKey in weekly_ingredients:
                                weekly_ingredients[storageTypeKey] += [
                                    (str(bundled_ingredients[ingredient]) + str(unitKey) + ' of ' + str(ingredient))
                                ]
                            else:
                                weekly_ingredients[storageTypeKey] = [
                                    str(bundled_ingredients[ingredient]) + str(unitKey) + ' of ' + str(ingredient)
                                ]
            
        return weekly_ingredients
    
    def bundleIngredients(self, weekly_recipes):
        bundled_ingredients = {}
        
        for dayKey, dayValue in weekly_recipes.items():
            for mealTypeKey, mealTypeValue in dayValue.items():
                for ingredientKey, ingredientValue in mealTypeValue.items(): 
                    if ingredientKey not in bundled_ingredients: 
                        bundled_ingredients[ingredientKey] = ingredientValue
                    else: 
                        bundled_ingredients[ingredientKey] += ingredientValue
        
        return bundled_ingredients
        
    def calculateTotalIngredients(self, weekly_recipes) -> None:
        # Loop through ingredients and compact them
        bundled_ingredients = self.bundleIngredients(weekly_recipes)
        
        # Get the unit type for each ingredient 
        ingredients_to_print = self.calculateUnitTypeForIngredients(bundled_ingredients)
        
        # Print to screen
        self.printRecipeToScreen(ingredients_to_print)