from .mock_lists import mock_recipes

userIngredients = mock_recipes.get("q").split(",")

# print(mock_recipes.get("hits")[0].get("recipe").get("ingredientLines"))
dic = {} #stores index of recipes and amount of needed ingredient

#initialise dic to have values of 0
def initialiseDic(recipes):
    for i in range(len(recipes.get("hits"))): # loops through each recipes
        dic[i] = 0 #sets initial score of each recipe to 0
        # print(recipes.get("hits")[i].get("recipe").get("label"))

#used for updating scores for number of additional ingredients needed for each recipe
def findSimilarIngred(ingred, recipes, weight):
    for i in range(len(recipes.get("hits"))): # loops through each recipes
        amountOfRecipeIngred = len(recipes.get("hits")[i].get("recipe").get("ingredientLines"))
        ingredientInRecipe = [False]*amountOfRecipeIngred
        print(amountOfRecipeIngred)

        for n in range(len(recipes.get("hits")[i].get("recipe").get("ingredientLines"))): #loops through each recipe ingredient

            currentRecipeIngred = recipes.get("hits")[i].get("recipe").get("ingredientLines")[n] #gets current ingredient in recipe
            for m in range(len(ingred)): #loops through ingredient from user
                if ingred[m] in currentRecipeIngred: #checks if user ingredient is in current ingredient
                    ingredientInRecipe[m] = True
                    print(ingred[m])

        counter = 0 #counter for number of ingredients that user has
        for val in ingredientInRecipe:
            if val == True:
                counter += weight

        dic[i] = amountOfRecipeIngred - counter

#This function returns recipes from least additional ingredient to most additional ingredient
def leastNeededIngredient(ingred, recipes):
    findSimilarIngred(ingred, recipes, 1)


def priorityIngredient(p_ingred, recipes):
    findSimilarIngred(p_ingred, recipes, 1)

def getOrderedRecipes(recipes):
    new_ls = [] #stores list of ordered recipes

    for key in sorted(dic.items(), key=lambda item: item[1]): #loops through dic sorted from small to big
        new_ls.append(recipes.get("hits")[key[0]].get("recipe").get("label")) #add recipe in order
    return new_ls #return ordered recipes
#
# testing
# ls1 = ["a", "b", "c", "d"]
# ls2 = [["d", "e", "f"],
#        ["a", "b", "c"],
#        ["d", "e", "f"]]
# ls3 = ["a"]
#
# initialiseDic(mock_recipes)
# leastNeededIngredient(userIngredients, mock_recipes)
# print(dic)
# print(getOrderedRecipes(mock_recipes))
#
# print(leastNeededIngredient(ls1, ls2))
# print(dic)
# print(priorityIngredient(ls3, ls2))
# print(dic)
