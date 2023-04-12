class Person:
    def __init__(self, gender, weight_in_kg, height_in_feet, age, exercise_level, target_fat_percentage) -> None:      
        # Person variables
        self.gender = gender
        self.weight_in_kg = weight_in_kg
        self.weight_in_pounds = self.weight_in_kg * 2.205
        self.height_in_feet = height_in_feet
        self.height_in_inches = height_in_feet * 12
        self.age = age
        self.exercise_level = exercise_level
        self.target_fat_percentage = target_fat_percentage
        self.daily_calorie_intake = 0
        
        ## Carbs
        self.calories_per_gram_of_carbs = 4
        
        self.carbs_percentage = 0
        self.carbs_calorie_intake = 0
        self.carbs_grams_intake = 0
        
        ## Protein
        self.calories_per_gram_of_protein = 4
        
        self.protein_percentage = self.target_fat_percentage * self.weight_in_kg
        self.protein_calorie_intake = 0
        self.protein_grams_intake = 0
        
        ## Fats
        self.calories_per_gram_of_fat = 9
        
        self.fat_percentage = 0
        self.saturated_fat_percentage = 0
        self.unsaturated_fat_percentage = 0
        
        self.fat_calorie_intake = 0
        self.saturated_fat_calorie_intake = 0
        self.unsaturated_fat_calorie_intake = 0
        
        self.fat_grams_intake = 0
        self.saturated_fat_grams_intake = 0
        self.unsaturated_fat_grams_intake = 0
        
        # Function calls
        self.calculateDailyCalorieIntake()
        
        self.calculateDailyCarbsPercentage()
        self.calculateDailyCarbsCalorieIntake()
        self.calculateDailyCarbsGramsIntake()
        
        self.calculateDailyProteinGramsIntake()
        self.calculateDailyProteinCalorieIntake()
        self.calculateDailyProteinPercentage()
        
        self.calculateDailyFatPercentage()
        self.calculateDailyFatCalorieIntake()
        self.calculateDailyFatGramsIntake()
        self.calculateDailySaturatedFatGramsIntake()
        self.calculateDailySaturatedFatCalorieIntake()
        self.calculateDailySaturatedFatPercentage()
        self.calculateDailyUnsaturatedFatPercentage()
        self.calculateDailyUnsaturatedFatCalorieIntake()
        self.calculateDailyUnsaturatedFatGramsIntake()
        
    # Carbs
    def calculateDailyCarbsPercentage(self):
        if self.exercise_level == 1: self.carbs_percentage = 0.40
        elif self.exercise_level == 1.2: self.carbs_percentage = 0.45
        elif self.exercise_level == 1.37: self.carbs_percentage = 0.45
        elif self.exercise_level == 1.55: self.carbs_percentage = 0.50
        elif self.exercise_level == 1.725: self.carbs_percentage = 0.55
        elif self.exercise_level == 1.9: self.carbs_percentage = 0.55
        else: self.carbs_percentage = 0
    def calculateDailyCarbsCalorieIntake(self): self.carbs_calorie_intake = round(self.daily_calorie_intake * self.carbs_percentage)
    def calculateDailyCarbsGramsIntake(self): self.carbs_grams_intake = round(self.carbs_calorie_intake / 4)
    
    # Protein
    def calculateDailyProteinPercentage(self): self.protein_percentage = round(self.protein_calorie_intake / self.daily_calorie_intake, 2)
    def calculateDailyProteinCalorieIntake(self): self.protein_calorie_intake = round(self.protein_grams_intake * 4)
    def calculateDailyProteinGramsIntake(self): 
        grams_of_protein_per_pound_of_weight = 0
        
        if self.exercise_level == 1: grams_of_protein_per_pound_of_weight = 0.7 * 2.205
        elif self.exercise_level == 1.2: grams_of_protein_per_pound_of_weight = 0.9 * 2.205
        elif self.exercise_level == 1.37: grams_of_protein_per_pound_of_weight = 1.1 * 2.205
        elif self.exercise_level == 1.55: grams_of_protein_per_pound_of_weight = 1.3 * 2.205
        elif self.exercise_level == 1.725: grams_of_protein_per_pound_of_weight = 1.5 * 2.205
        elif self.exercise_level == 1.9: grams_of_protein_per_pound_of_weight = 1.7 * 2.205
        else: print("Cannot do it")
        
        self.protein_grams_intake = round(grams_of_protein_per_pound_of_weight * (self.weight_in_kg - (self.target_fat_percentage * self.weight_in_kg)))
    
    # Fats
        # Fat percentage
    def calculateDailyFatPercentage(self): self.fat_percentage = round(1 - (self.carbs_percentage + self.protein_percentage), 2)
    def calculateDailySaturatedFatPercentage(self): self.saturated_fat_percentage = self.saturated_fat_calorie_intake / self.fat_calorie_intake
    def calculateDailyUnsaturatedFatPercentage(self): self.unsaturated_fat_percentage = round(1 - self.saturated_fat_percentage, 2)
        
        # Fat calorie
    def calculateDailyFatCalorieIntake(self): self.fat_calorie_intake = round(self.daily_calorie_intake * self.fat_percentage)
    def calculateDailySaturatedFatCalorieIntake(self): self.saturated_fat_calorie_intake = round(self.saturated_fat_grams_intake * 9)
    def calculateDailyUnsaturatedFatCalorieIntake(self): self.unsaturated_fat_calorie_intake = round(self.fat_calorie_intake * self.unsaturated_fat_percentage)
    
        # Fat grams
    def calculateDailyFatGramsIntake(self): self.fat_grams_intake = round(self.fat_calorie_intake / 9)
    def calculateDailySaturatedFatGramsIntake(self): self.saturated_fat_grams_intake = 14    # The US recommends no more than 14g of saturated fats per day (UK is 30g a day)
    def calculateDailyUnsaturatedFatGramsIntake(self): self.unsaturated_fat_grams_intake = round(self.unsaturated_fat_calorie_intake / 9)
        
    def calculateDailyCalorieIntake(self): 
        if (self.gender == 'male'): self.daily_calorie_intake = round((66 + (6.2 * self.weight_in_pounds) + (12.7 * self.height_in_inches) - (6.76 * self.age)) * self.exercise_level)
        if (self.gender == 'female'): self.daily_calorie_intake = round((655.1 + (4.35 * self.weight_in_pounds) + (4.7 * self.height_in_inches) - (4.7 * self.age)) * self.exercise_level)
        
    def getDailyMacronutrientPercentage(self):
        print("Daily carbs percentage: " + str(round(self.carbs_percentage * 100)) + "%")
        print("Daily protein percentage: " + str(round(self.protein_percentage * 100)) + "%")
        print("Daily fat percentage: " + str(round(self.fat_percentage * 100)) + "%")
        print("        of which are saturated: " + str(round(self.saturated_fat_percentage * 100)) + "%")
        print("        of which are unsaturated: " + str(round(self.unsaturated_fat_percentage * 100)) + "%")
        
    def getDailyMacronutrientCalorieIntake(self):
        print("Daily carbs calorie intake: ", str(self.carbs_calorie_intake))
        print("Daily protein calorie intake: ", str(self.protein_calorie_intake))
        print("Daily fat calorie intake: ", str(self.fat_calorie_intake))
        print("        of which are saturated: " + str(self.saturated_fat_calorie_intake))
        print("        of which are unsaturated: " + str(self.unsaturated_fat_calorie_intake))
    
    def getDailyMacronutrientGramsIntake(self):
        print("Daily carbs grams intake: " + str(self.carbs_grams_intake) + "g")
        print("Daily protein grams intake: " + str(self.protein_grams_intake) + "g")
        print("Daily fat grams intake: " + str(self.fat_grams_intake) + "g")
        print("        of which are saturated: " + str(self.saturated_fat_grams_intake) + "g")
        print("        of which are unsaturated: " + str(self.unsaturated_fat_grams_intake) + "g")
        
    def getDailyMacronutrientForMealTimeInGrams(self):
        print("Daily carbs grams intake: " + str(self.carbs_grams_intake) + "g")
        print("        Breakfast: (50%): " + str(0.5 * self.carbs_grams_intake) + "g")
        print("        Lunch:     (40%): " + str(0.4 * self.carbs_grams_intake) + "g")
        print("        Dinner:    (10%): " + str(0.1 * self.carbs_grams_intake) + "g")
        print("Daily protein grams intake: " + str(self.protein_grams_intake) + "g")
        print("        Breakfast: (40%): " + str(0.4 * self.protein_grams_intake) + "g")
        print("        Lunch:     (40%): " + str(0.4 * self.protein_grams_intake) + "g")
        print("        Dinner:    (20%): " + str(0.2 * self.protein_grams_intake) + "g")
        print("Daily fat grams intake: " + str(self.fat_grams_intake) + "g")
        print("        of which are saturated: " + str(self.saturated_fat_grams_intake) + "g")
        print("                Breakfast: (40%): " + str(round(0.4 * self.saturated_fat_grams_intake)) + "g")
        print("                Lunch:     (40%): " + str(round(0.4 * self.saturated_fat_grams_intake)) + "g")
        print("                Dinner:    (20%): " + str(round(0.2 * self.saturated_fat_grams_intake)) + "g")
        print("        of which are unsaturated: " + str(self.unsaturated_fat_grams_intake) + "g")
        print("                Breakfast: (40%): " + str(round(0.4 * self.unsaturated_fat_grams_intake)) + "g")
        print("                Lunch:     (40%): " + str(round(0.4 * self.unsaturated_fat_grams_intake)) + "g")
        print("                Dinner:    (20%): " + str(round(0.2 * self.unsaturated_fat_grams_intake)) + "g")