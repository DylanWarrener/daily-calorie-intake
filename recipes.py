class Recipies: 
    def __init__(self) -> None:
        self.recipes = {
            "breakfast": {
                "greenMilkSummerFruitsAndBananaSmoothie": {
                    "summerFruitsAndBanana": 120,
                    "oats": 100,
                    "greenMilk": 250,
                    "honey": 3,
                    "fatFreeGreekYoghurt": 100,
                    "proteinPowder": 50,
                },
                "greenMilkBlackForestFruitsSmoothie": {
                    "blackForestFruits": 120,
                    "oats": 100,
                    "greenMilk": 250,
                    "honey": 3,
                    "fatFreeGreekYoghurt": 100,
                    "proteinPowder": 50,
                },
                "greenMilkMangoAndPineapppleSmoothie": {
                    "mangoAndPineapple": 120,
                    "oats": 100,
                    "greenMilk": 250,
                    "honey": 3,
                    "fatFreeGreekYoghurt": 100,
                    "proteinPowder": 50,
                },
                "greenMilkSummerFruitsSmoothie": {
                    "summerFruits": 120,
                    "oats": 100,
                    "greenMilk": 250,
                    "honey": 3,
                    "fatFreeGreekYoghurt": 100,
                    "proteinPowder": 50,
                },
                "greenMilkBlueberriesSmoothie": {
                    "blueberries": 120,
                    "oats": 100,
                    "greenMilk": 250,
                    "honey": 3,
                    "fatFreeGreekYoghurt": 100,
                    "proteinPowder": 50,
                }
            },
            "lunch": {
                "tandooriPrawnNaans": {
                    "curryPowder": 1,
                    "sunflowerOil": 1,
                    "fatFreeGreekYoghurt": 60,
                    "lime": 1,
                    "kingPrawns": 100,
                    "redOnion": 0.5,
                    "redPepper": 1,
                    "naanBread": 1,
                    "tomato": 1,
                    "cucumber": 0.25,
                    "granulatedSugar": 0.5,
                    "garlicPowderSeasoning": 0.5
                },
                "mackerelSaladWithBabyPotatoes": {
                    "babyPotato": 150,
                    "souredCream": 40,
                    "gherkins": 3,
                    "lemon": 0.5,
                    "dill": 5,
                    "radishes": 40,
                    "cucumber": 0.25,
                    "oliveOil": 0.5,
                    "mackerel": 1
                },
                "creamySpinachChicken": {
                    "sundriedTomatoes": 25,
                    "chicken": 150,
                    "cornflour": 1.25,
                    "redOnion": 0.5,
                    "garlicPowderSeasoning": 1,
                    "chickenStock": 2,
                    "spinach": 62.5,
                    "lemon": 0.5,
                    "souredCream": 40
                },
                "smokyCourgettePastaSalad": {
                    "courgette": 0.5,
                    "oliveOil": 0.5,
                    "pennePasta": 87.5,
                    "lemon": 0.5,
                    "cherryTomatoes": 3,
                    "fatFreeGreekYoghurt": 32,
                    "garlicPowderSeasoning": 1,
                    "fetaCheese": 50,
                    "cucumber": 0.25,
                    "parsley": 1
                },
                "tandooriPrawnNaans": {
                    "curryPowder": 1,
                    "sunflowerOil": 1,
                    "fatFreeGreekYoghurt": 68,
                    "lime": 1,
                    "kingPrawns": 100,
                    "redOnion": 75,
                    "redPepper": 1,
                    "naanBread": 1,
                    "tomato": 1,
                    "cucumber": 0.25,
                    "granulatedSugar": 0.5,
                    "garlicPowderSeasoning": 1
                },
                "vegetablePilaf": {
                    "carrots": 100,
                    "sweetPotato": 75,
                    "redOnion": 75,
                    "cuminSeeds": 1,
                    "corriander": 1,
                    "mixedSpice": 1,
                    "oliveOil": 2,
                    "cashewNuts": 20,
                    "vegetableStock": 3,
                    "rice": 0.5,
                    "garlicPowderSeasoning": 1,
                    "broccoli": 1
                },
                "stickyBeefWithCashews": {
                    "soySauce": 1,
                    "chineseFiveSpice": 0.5,
                    "sirloinSteak": 1,
                    "groundNutOil": 0.5,
                    "garlicPowderSeasoning": 1,
                    "ginger": 1,
                    "redChillies": 0.5,
                    "cashewNuts": 20,
                    "oysterSauce": 1,
                    "stemmedBroccoli": 60,
                    "lime": 1,
                    "springOnion": 2,
                    "noodles": 1
                },
                "tunaButterBeanPie": {
                    "babyPotato": 100,
                    "herbAndTomatoeSauce": 1,
                    "tuna": 1,
                    "tinnedbutterBeans": 1,
                    "springOnion": 2,
                    "oliveOil": 0.5,
                    "broccoli": 1
                },
                "codLentilBeetrootTraybake": {
                    "beetroot": 150,
                    "greenLentils": 195,
                    "garlicPowderSeasoning": 1,
                    "horseradishSauce": 1,
                    "parsley": 1,
                    "lemon": 1,
                    "oliveOil": 1,
                    "codFillets": 1
                },
                "sweetPotatoAndChickenTraybake": {
                    "sweetPotato": 125,
                    "redOnion": 75,
                    "broccoli": 1,
                    "garlicPowderSeasoning": 4,
                    "thyme": 1,
                    "rosemary": 1,
                    "oliveOil": 0.5,
                    "chicken": 170,
                    "lemon": 1,
                    "smokedPaprika": 1,
                    "chickenStock": 2
                },
                "speedyVeggieNoodles": {
                    "oliveOil": 1,
                    "mixedVegetables": 75,
                    "thymeSprigs": 1,
                    "tinnedbutterBeans": 1,
                    "vegetableStock": 2,
                    "springGreens": 75,
                    "whiteBread": 50,
                    "cheese": 15,
                    "redChillies": 1
                },
                "troutFilletsWithAHazelnutCrust": {
                    "whiteBreadcrumbs": 25,
                    "choppedHazlenuts": 25,
                    "parsley": 1,
                    "lemon": 1,
                    "troutFillets": 2
                },
                "sardineAndTomatoSpaghetti": {
                    "oliveOil": 0.5,
                    "redOnion": 37.5,
                    "garlicPowderSeasoning": 1,
                    "redChillies": 1,
                    "whiteWineVinegar": 2,
                    "cherryTomatoes": 250,
                    "spaghetti": 125,
                    "pittedOlives": 50,
                    "sardines": 1,
                    "parsley": 1
                },
                "vegetableNasiGoreng": {
                    "oliveOil": 1,
                    "rice": 1,
                    "eggs": 2,
                    "bananaShallots": 1,
                    "vegetableOil": 1,
                    "garlicPowderSeasoning": 2,
                    "redChillies": 4,
                    "roastedPeanuts": 5,
                    "ginger": 2,
                    "soySauce": 1,
                    "leek": 0.5,
                    "redPepper": 1,
                    "carrots": 1,
                    "pakChoi": 1,
                    "springOnion": 1,
                    "lime": 1
                },
                "kungPaoBeef": {
                    "rice": 80,
                    "shaohsingRiceWine": 1,
                    "darkSoySauce": 1,
                    "lightSoySauce": 1,
                    "whiteWineVinegar": 1,
                    "cornflour": 0.5,
                    "vegetableOil": 0.5,
                    "cashewNuts": 17.5,
                    "sirloinSteak": 1,
                    "garlicPowderSeasoning": 1,
                    "ginger": 1,
                    "springOnion": 2
                },
                "superLentilAndVegetableSoup": {
                    "whiteOnion": 75,
                    "carrots": 0.5,
                    "leek": 0.5,
                    "whitePotato": 1,
                    "celeryStick": 0.5,
                    "oliveOil": 0.5,
                    "plainFlour": 0.5,
                    "stockPowder": 1,
                    "redLentils": 25
                },
                "haddockWithSweetPotatoFries": {
                    "sweetPotato": 250,
                    "sunflowerOil": 1,
                    "peas": 125,
                    "unsaltedButter": 8,
                    "greenMilk": 60,
                    "haddockFillets": 1,
                    "whiteBreadcrumbs": 25,
                    "poppySeeds": 1,
                    "eggs": 1,
                    "souredCream": 25,
                    "mixedHerbs": 2,
                    "cornichons": 2,
                    "lemon": 1
                },
                "pepperedMackerelSpaghetti": {
                    "spaghetti": 75,
                    "oliveOil": 1,
                    "redPepper": 1,
                    "garlicPowderSeasoning": 1,
                    "redChillies": 0.5,
                    "cherryTomatoes": 3,
                    "parsley": 1,
                    "mackerel": 1,
                    "lemon": 0.5
                },
                "beefKebab": {
                    "mince": 200,
                    "kebabSeasoning": 1,
                    "oregano": 1,
                    "onionPowder": 1,
                    "garlicPowderSeasoning": 1,
                    "fatFreeGreekYoghurt": 100,
                    "garlicPaste": 1,
                    "brownWraps": 2,
                    "redCabbage": 25,
                    "lettuce": 25,
                    "redOnion": 0.5,
                    "cherryTomatoes": 4,
                    "cucumber": 0.25
                },
                "quinoaSaladWithHalloumi": {
                    "bulgarWheat": 20,
                    "cherryTomatoes": 3,
                    "parsley": 1,
                    "quinoa": 0.25,
                    "lemon": 1,
                    "oliveOil": 1,
                    "springOnion": 2,
                    "halloumi": 30,
                    "courgette": 0.5
                },
                "loadedSweetPotatoeSkin": {
                    "sweetPotato": 1,
                    "tacoMixedBeansInTomatoSauce": 1,
                    "springOnion": 2,
                    "manchego": 37.5,
                    "cherryTomatoes": 3
                },
            }, 
            "dinner": {
                "creamyFishPie": {
                    "whitePotatoes": 500,
                    "whiteOnion": 0.5,
                    "lightCreamCheese": 125,
                    "fishPieMix": 160,
                    "prawns": 95,
                    "parsley": 3,
                    "oliveOil": 0.5,
                    "vegetableStock": 2,
                    "cornflour": 2,
                    "greenMilk": 50
                },
                "chickenTacoRecipe": {
                    "chickenBreast": 200,
                    "lemon": 0.5,
                    "fatFreeGreekYoghurt": 200,
                    "cajun": 0.5,
                    "redOnion": 0.5,
                    "redWineVinegar": 1.5,
                    "granulatedSugar": 0.5,
                    "oliveOil": 1,
                    "redPepper": 1.5,
                    "garlicClove": 1,
                    "lettuce": 0.5,
                    "redChillies": 0.5,
                    "tacos": 1
                },
                "indianLoadedSweetPotatoe": {
                    "sweetPotato": 2,
                    "vegetableOil": 0.5,
                    "whiteOnion": 1,
                    "curryPowder": 1,
                    "carrot": 1,
                    "redPepper": 0.5,
                    "rice": 50,
                    "chickpeas": 200,
                    "vegetableStock": 2,
                    "springOnion": 1,
                    "fatFreeGreekYoghurt": 2
                },
                "sirlionSteakWithBlueCheese": {
                    "sirlionSteak": 2,
                    "oliveOil": 2,
                    "thymeSprigs": 2,
                    "garlicClove": 1,
                    "streakyBacon": 2,
                    "babySprouts": 180,
                    "cranberries": 50,
                    "balsamicVinegar": 1,
                    "packMashedPotato": 1,
                    "greenMilk": 5,
                    "horseradishSauce": 1,
                    "stilton": 50
                },
                "salmonAndLeekPastaBake": {
                    "penne": 175,
                    "oliveOil": 0.5,
                    "leek": 125,
                    "garlicClove": 2,
                    "lightCreamCheese": 50,
                    "greenMilk": 50,
                    "frozenPeas": 125,
                    "salmonFillet": 2,
                    "parsley": 2,
                    "matureCheese": 50
                },
                "spicyCreamyWrap": {
                    "brownWraps": 2,
                    "lettuce": 50,
                    "mozzarella": 1,
                    "eggs": 3,
                    "lightCreamCheese": 80,
                    "sriracha": 1,
                    "redOnion": 0.5,
                    "parsley": 3,
                    "sundriedTomatoes": 15,
                    "chilliFlakes": 1
                },
                "roastedButternutSquashCurry": {
                    "butternutSquash": 1,
                    "coconutOil": 2,
                    "redOnion": 1,
                    "garlicPowderSeasoning": 4,
                    "ginger": 4,
                    "curryPowder": 3,
                    "garamMasala": 0.5,
                    "cumin": 0.5,
                    "cuminSeeds": 0.5,
                    "turmeric": 0.25,
                    "chilliPowder": 0.25,
                    "choppedTomatoes": 400,
                    "coconutMilk": 400,
                    "vegetableStock": 2,
                    "chickpeas": 400,
                    "rice": 1
                },
                "honeyAndMustardWithEggs": {
                    "honey": 2,
                    "frenchMustard": 1,
                    "salmonFillet": 1,
                    "fineBeans": 100, 
                    "rice": 0.5,
                    "quinoa": 0.5,
                    "eggs": 2,
                    "lemon": 1,
                    "springOnion": 2,
                    "redChillies": 1
                },
                "soyBeanChilliGingerStirFry": {
                    "redChillies": 0.5,
                    "ginger": 1,
                    "garlicPowderSeasoning": 1,
                    "cidarVinegar": 1,
                    "sesameOil": 1,
                    "redOnion": 0.5,
                    "redPepper": 0.5,
                    "soybean": 60,
                    "beanSprouts": 100,
                    "honey": 1,
                    "soySauce": 1
                },
                "sausageAndEggOpenPancake": {
                    "sausages": 4,
                    "plainFlour": 2,
                    "eggs": 2,
                    "greenMilk": 60,
                    "vegetableOil": 1,
                    "cherryTomatoes": 3,
                    "springOnion": 2,
                    "redPepper": 0.5,
                    "cucumber": 0.25,
                    "frenchDressing": 0.5
                },
                "peaAndTurkeySoup": {
                    "oliveOil": 0.5,
                    "whiteOnion": 0.5,
                    "babyPotato": 50,
                    "leek": 50,
                    "parsley": 1,
                    "peas": 87.5,
                    "turkeyHam": 40,
                    "chickenStock": 2,
                    "eggs": 2
                },
                "smokyChipotleAdzukiBeanChilli": {
                    "oliveOil": 1,
                    "redOnion": 0.5,
                    "celeryStick": 1,
                    "redPepper": 0.5,
                    "garlicPowderSeasoning": 1,
                    "corriander": 3,
                    "paprika": 1,
                    "chipotleChilliPaste": 0.5,
                    "tinnedPlumTomatoes": 1,
                    "tinnedCannelliniBeans": 1,
                    "lime": 1,
                    "rice": 0.5,
                    "fatFreeGreekYoghurt": 50
                },
                "roastedSpicedBroccoliSoup": {
                    "broccoli": 1,
                    "vegetableOil": 0.5,
                    "corriander": 1,
                    "cumin": 1,
                    "cayennePepper": 0.5,
                    "whiteOnion": 0.5,
                    "celeryStick": 1,
                    "parsley": 2,
                    "babyPotato": 50,
                    "vegetableStock": 2,
                    "almondMilk": 50,
                    "lemon": 0.5,
                    "spinach": 25,
                    "mixedNuts": 20
                },
                "turkeyStuffedTomatoes": {
                    "beefTomato": 1,
                    "oliveOil": 1,
                    "redOnion": 37.5,
                    "garlicPowderSeasoning": 2,
                    "turkey": 100,
                    "sundriedTomatoPuree": 0.5,
                    "basil": 1,
                    "couscous": 25,
                    "lemon": 1,
                    "parsley": 1,
                    "mint": 1,
                    "sugarsnapPeas": 25,
                    "cucumber": 0.25
                },
                "greekPotatoesWithLemon": {
                    "babyPotato": 225,
                    "lemon": 1,
                    "garlicPowderSeasoning": 1,
                    "bayLeaves": 2,
                    "redOnion": 37.5,
                    "oliveOil": 1.5,
                    "thyme": 1
                },
                "spinachAndCheeseOmelette": {
                    "oliveOil": 1,
                    "eggs": 2,
                    "greenMilk": 15,
                    "spinach": 118.5,
                    "cheese": 20,
                    "cherryTomatoes": 50
                },
                "handHeldSaltAndPepperPrawns": {
                    "kingPrawns": 10,
                    "rainbowPeppercorns": 1,
                    "starAnise": 1,
                    "cornflour": 6,
                    "redChillies": 1,
                    "sesameOil": 1,
                    "soySauce": 1,
                    "riceWineVinegar": 1,
                    "garlicPowderSeasoning": 1,
                    "granulatedSugar": 1,
                    "lime": 1
                },
                "miniPizzas": {
                    "oliveOil": 1.5,
                    "whiteOnion": 150,
                    "sardines": 1,
                    "lemon": 1,
                    "wheatFlour": 112.5,
                    "casterSugar": 0.5,
                    "yeast": 1,
                    "greenMilk": 80,
                    "vinegar": 0.5,
                    "eggs": 1,
                    "sunflowerOil": 1.5
                },
                "tofuStirFry": {
                    "tofu": 115,
                    "grapeseedOil": 1,
                    "sesameOil": 1,
                    "soySauce": 1.5,
                    "garlicPowderSeasoning": 2,
                    "ginger": 1,
                    "springOnion": 2,
                    "beanSprouts": 100,
                    "redChillies": 1,
                    "spinach": 67.5,
                    "sesameSeeds": 1,
                    "noodles": 1
                },
                "bbqStyleChickenDrumsticks": {
                    "whitePotatoes": 150,
                    "vegetableOil": 1,
                    "chipSeasoning": 1,
                    "rosemarySeasoning": 1,
                    "chickenDrumsticks": 4,
                    "oliveOil": 1,
                    "carrots": 25,
                    "redPepper": 0.5,
                    "redOnion": 0.5,
                    "garlicSeasoning": 1,
                    "mixedHerbSeasoning": 1
                },
                "partialHomeMadePizzaDylanDani": {
                    "pizzaTomatoSauce": 1,
                    "pizzaBBQSauce": 1,
                    "mozzerella": 1,
                    "redLeicester": 1,
                    "ham": 1,
                    "redPepper": 1,
                    "sweetCorn": 1,
                    "chickenReadyToEat": 2,
                    "mushrooms": 1,
                    "redOnion": 1
                },
                "tescoCottagePie": {
                    "oliveOil": 1,
                    "whiteOnion": 1,
                    "carrots": 2,
                    "celeryStalk": 1,
                    "garlicClove": 1,
                    "mince": 500,
                    "tomatoPuree": 1,
                    "choppedTomatoes": 1,
                    "beefStockCube": 2,
                    "bayLeaf": 1,
                    "pees": 100,
                    "whitePotatoes": 1000,
                    "unsaltedButter": 50
                },
                "sausageAndMash": {
                    "whitePotatoes": 500,
                    "sausages": 4,
                    "oliveOil": 2,
                    "garlicClove": 2,
                    "rosemary": 5,
                    "redOnion": 1,
                    "djonMustard": 1,
                    "balsamicVinegar": 1,
                    "leaPerins": 1,
                    "beefStockCube": 2,
                    "whiteSugar": 1,
                    "butter": 1,
                    "unsaltedButter": 15,
                    "chives": 5
                }
            }
        }
    
    def getRecipe(self, mealType, recipe):
        for mealTypeKey, mealTypeValue in self.recipes.items():
            if mealType == mealTypeKey:
                for recipeKey, recipeValue in mealTypeValue.items():
                    if recipe == recipeKey: 
                        return recipeValue
    
    def getRecipies(self, recipies):
        return recipies