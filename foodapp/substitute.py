import requests
import json



def getSubstitute(Ingredients,InputtedIngredients):
    #API Keys
    headers = {
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"x-rapidapi-key": "1bb222a567mshc7a02d467055386p198260jsn37a44f5106fd"
    }
    
    SubsDict = {}
    for I in Ingredients:
        is_match = False
        
        #Skipping over Ingredients that the user has on hand
        for i in InputtedIngredients:
            I = I.lower()
            i = i.lower()
            if I.find(i) != -1: 
                is_match = True
        if is_match:
            continue
        
        #Finding Ingredients substitutes
        SubstituteApi = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/substitutes?ingredientName={I}&number=2", headers = headers)
        
        if SubstituteApi.status_code != 200:
            print(SubstituteApi.status_code)
            raise ValueError("HTTP Error")
        SubsJson = SubstituteApi.json()
        if SubsJson["status"] == "success":
            SubsDict[I] = SubsJson["substitutes"]
    return SubsDict


print(getSubstitute(["sesame seeds, for sprinkling"],["Orange","Chicken"]))
