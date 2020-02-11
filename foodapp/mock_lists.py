#https://api.edamam.com/api/food-database/parser?ingr=ban&app_id=fbd440e6&app_key=136f60c5db1a10c7dc8aab22aaccf545

class Object(object):

    def json(self):
        return self.j

def getMockResponse():

    mockResponse = Object()
    mockResponse.status_code = 200
    mockResponse.j = mock_ac

    return mockResponse

mock_ac = {
    "text": "ban",
    "parsed": [],
    "hints": [
        {
            "food": {
                "foodId": "food_bvqs95ubdp30o1a1cwn1fabv2rpt",
                "label": "Straw/Ban Smoothie",
                "nutrients": {
                    "ENERC_KCAL": 39.683207193277966,
                    "PROCNT": 0.44092452436975516,
                    "CHOCDF": 10.361726322689247
                },
                "brand": "Grand Traverse Pie Company",
                "category": "Fast foods",
                "categoryLabel": "meal"
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_serving",
                    "label": "Serving"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_bu1gpe1btascayabsek7bab2843w",
                "label": "ICHI-BAN TAKO-SENBEI",
                "nutrients": {
                    "ENERC_KCAL": 427,
                    "PROCNT": 3.3299999237060547,
                    "FAT": 10,
                    "CHOCDF": 76.66999816894531
                },
                "brand": "SHONAN CHIGASAKIYA JUDAI",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "POTATO STARCH; SQUID; OCTOPUS; SUGAR; SALT; VEGETABLE OIL; SOY SAUCE; SWEET SAKE; FERMENTED SEASONING; RED PEPPER; DEXTRIN; BONITO EXTRACT; HYDROLYZED PROTEIN (FROM SOY BEAN); CRAB EXTRACT POWDER; TAPIOKA STARCH; MONOSODIUM GLUTAMATE; ACESULFAME POTASSIUM"
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_a7j4pvkb6kgjpjayxrivvbzf7puo",
                "label": "BAN APPETIT, APPLE DANISH",
                "nutrients": {
                    "ENERC_KCAL": 352,
                    "PROCNT": 5.630000114440918,
                    "FAT": 19.719999313354492,
                    "CHOCDF": 39.439998626708984,
                    "FIBTG": 1.399999976158142
                },
                "brand": "Bon Appetit Danish Co.",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "WHEAT FLOUR ENRICHED (NIACIN; REDUCED IRON; THIAMINE MONONITRATE; RIBOFLAVIN; MALTED BARLEY FLOUR; ASCORBIC ACID; FOLIC ACID); PALM OIL (WITH MONO & DIGLYCERIDES; POLYSORBATE 60; CITRIC ACID); WATER; SUGAR; EGGS; YEAST; SOY FLOUR; WHEY; NONFAT DRY MILK; INVERT SUGAR; WHEAT FLOUR; DATEM DEXTROSE; SOY BEAN OIL; L-CYSTEINE; AZODICARBONAMIDE (ADA); ENZYMES; SALT; POTASSIUM SORBATE; SODIUM STEAROYL LACTYLATE; CALCIUM PROPIONATE; FD&C RED 40; RED 3; YELLOW 5; YELLOW 6; BLUE 1; BLUE 2; TITANIUM DIOXODE; MODIFIED CORN STARCH; VEGETABLE GUM; SODIUM BENZOATE; APPLE FILLING (SUGAR; APPLE; WATER; MODIFIED CORN STARCH; CONTAINS 2% OF LESS OF THE FOLLOWING: APPLE JUICE CONCENTRATE; LEMON JUICE; NATURAL AND ARTIFICIAL FLAVORS; CINNAMON; SODIUM BENZOATE).",
                "image": "https://www.edamam.com/food-img/633/63358c3b2998ead354652971d1a7e55f.jpg"
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pastry",
                    "label": "Pastry"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_aj62eefb3ey8yubfj7ih7avluyu9",
                "label": "GARBANZO BANS CHICKS PEAS",
                "nutrients": {
                    "ENERC_KCAL": 96,
                    "PROCNT": 4.800000190734863,
                    "FAT": 0.800000011920929,
                    "CHOCDF": 17.600000381469727,
                    "FIBTG": 4.800000190734863
                },
                "brand": "The Kroger Co.",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "PREPARED GARBANZO BEANS; WATER; SALT; CALCIUM CHLORIDE; SODIUM METABISULFITE AND DISODIUM EDTA (FOR COLOR RETENTION)."
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_cup",
                    "label": "Cup"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_bchha8cata5jqkbfpej90afrn4ze",
                "label": "Yang Ban Sea Veggies Hot Chili",
                "nutrients": {
                    "ENERC_KCAL": 671.8850104930623,
                    "PROCNT": 16.797125262326556,
                    "FAT": 50.391375786979665,
                    "CHOCDF": 33.59425052465311
                },
                "brand": "Dw Global Inc.",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "Seaweed; Hot Chili Pepper Oil; Rapeseed Oil; Red Pepper; Onion; Sea Salt."
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_a0524a7btonf1xb8e1vxabyjms3y",
                "label": "Hime Green Tea Ban Cha, 8.0 oz",
                "nutrients": {},
                "brand": "Hime",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "Green Tea.",
                "image": "https://www.edamam.com/food-img/0fb/0fbe0b3bac5e948720f3f474cd8ce646.jpg"
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_fluid_ounce",
                    "label": "Fluid ounce"
                }
            ]
        },
        {
            "food": {
                "foodId": "food_ag9culwbkv31i0a1y4of8ajbh2q8",
                "label": "NAT VLY SFT BKD OATMEAL SQUARES BAN BRD DRK CHOC",
                "nutrients": {
                    "PROCNT": 5.710000038146973,
                    "FAT": 17.139999389648438,
                    "CHOCDF": 65.70999908447266,
                    "FIBTG": 5.699999809265137
                },
                "brand": "GENERAL MILLS SALES INC.",
                "category": "Packaged foods",
                "categoryLabel": "food",
                "foodContentsLabel": "WHOLE GRAIN OATS; WHOLE WHEAT FLOUR; SUGAR; VEGETABLE OIL (CANOLA; PALM KERNEL; PALM); SEMISWEET CHOCOLATE CHUNKS (SUGAR; CHOCOLATE LIQUOR; COCOA BUTTER; SOY LECITHIN; NATURAL FLAVOR); TAPIOCA SYRUP; DRIED BANANAS; VEGETABLE GLYCERIN; CHICORY ROOT EXTRACT; EGG YOLK; MOLASSES; RAISIN JUICE CONCENTRATE; BAKING SODA; GUM ARABIC; COCOA; EGG WHITE; SALT; NATURAL FLAVOR; SOY LECITHIN; MILK; OIL OF ROSEMARY."
            },
            "measures": [
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_bar",
                    "label": "Bar"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_gram",
                    "label": "Gram"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_ounce",
                    "label": "Ounce"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_pound",
                    "label": "Pound"
                },
                {
                    "uri": "http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram",
                    "label": "Kilogram"
                }
            ]
        }
    ]
}

mock_food_list = [
    "acorn",
    "squash",
    "alfalfa sprouts",
    "almond",
    "anchovy",
    "anise",
    "apple",
    "apricot",
    "artichoke",
    "asparagus",
    "aspicate",
    "avocado",
    "bacon",
    "bagel",
    "bamboo shoots",
    "banana",
    "basil",
    "beans",
    "beef",
    "cheese",
    "cream",
    "tomato"
]

mock_recipes = [
    {
        'id': '0',
        'name': 'Beef Stew',
        'cooktime': '30min',
        'preptime': '10min',
        'image': 'https://www.onceuponachef.com/images/2011/02/beef-stew-with-carrots-potatoes-768x534.jpg',
        'ingredients': ['beef', 'carrot', 'basil']
    },
    {
        'id': '1',
        'name': 'Banana Pie',
        'cooktime': '10min',
        'preptime': '5min',
        'image': 'https://cdn.sallysbakingaddiction.com/wp-content/uploads/2016/07/Banana-Cream-Pie-8.jpg',
        'ingredients': ['banana', 'cheese', 'tomato']
    },
    {
        'id': '2',
        'name': 'Bean Pie',
        'cooktime': '10min',
        'preptime': '5min',
        'image': 'https://images.media-allrecipes.com/userphotos/560x315/1672943.jpg',
        'ingredients': ['cream', 'beans']
    }
]
