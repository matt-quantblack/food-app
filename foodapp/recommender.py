import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans

def train():

    # This is the same data that was plotted for similarity earlier
    # with one new user "E" who has rated only movie 1
    ratings_dict = {
        "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
        "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
        "rating": [1, 0, 0, 0, 1, 0, 1, 1, 1],
    }



    df = pd.DataFrame(ratings_dict)
    reader = Reader(rating_scale=(0, 1))

    # Loads Pandas dataframe
    data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)



    # To use item-based cosine similarity
    sim_options = {
        "name": "cosine",
        "user_based": False,  # Compute  similarities between items
    }
    algo = KNNWithMeans(sim_options=sim_options)

    algo.fit(data)

    return algo

def get_pred(algo, user, item):

    prediction = algo.predict('E', 2)

    return prediction.est


