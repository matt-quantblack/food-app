import requests
import json



def getSubstitute(RecipeURI,InputtedIngredients):
    #API Keys
    app_id = "a54a3ae5"
    app_key = "78b09548b69cd449b42676b6c1e6c1fb"
    headers = {
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"x-rapidapi-key": "1bb222a567mshc7a02d467055386p198260jsn37a44f5106fd"
    }
    
    #Getting Recipe 
    RecipeIdPos = RecipeURI.find("recipe_") + len("recipe_")
    RecipeID = RecipeURI[RecipeIdPos:]
    if RecipeID == "":
        raise ValueError("No ID")
    
    uri = f"https://api.edamam.com/search?q={RecipeID}&app_id={app_id}&app_key={app_key}"
    r = requests.get(uri)
    if r.status_code != 200:
        raise ValueError("HTTP Error")
        
    json = r.json()
    if json["count"] != 1:
        raise ValueError("Incorrect")
    
    #Getting Ingredients
    Ingredients = json["hits"][0]["recipe"]["ingredientLines"]
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


print(getSubstitute("http://www.edamam.com/ontologies/edamam.owl#recipe_280642e9ed18216826e045a9427a0839",["Orange","Chicken"]))
