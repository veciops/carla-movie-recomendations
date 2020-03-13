import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("../recommender/dataset/phones2018-2020.csv")


# Functions
def combine_features(row):
    return row['CPU'] + ' ' + row['Storage capacity'] + ' ' + row['Removable storage'] + row['RAM'] + ' ' + row['OS'] \
           + ' ' + row['Battery'] + ' ' + row['Battery'] + ' ' + row['Display'] + ' ' + row['Camera'] + ' ' \
           + row['Fingerprint scanner'] + ' ' + row['Facial recognition']


def removeNaN(featuresList):
    for feature in featuresList:
        df[feature] = df[feature].fillna('')  # filling all NaNs with blank string

    df['combined_features'] = df.apply(combine_features, axis=1)  # applying combined_features() method over each rows


def get_index_from_features(cpu, storage_capacity, removable_storage, ram, os, battery, display, camera, fingerprint
                            , facial_recognition):
    rows = df[(((cpu == None) | (cpu == df['CPU']))) &
              (((storage_capacity == None) | (storage_capacity == df['Storage capacity']))) &
              (((removable_storage == None) | (removable_storage == df['Removable storage']))) &
              (((ram == None) | (ram == df['RAM']))) &
              (((os == None) | (os == df['OS']))) &
              (((battery == None) | (battery == df['Battery']))) &
              (((display == None) | (display == df['Display']))) &
              (((camera == None) | (camera == df['Camera']))) &
              (((fingerprint == None) | (fingerprint == df['Fingerprint scanner']))) &
              (((facial_recognition == None) | (facial_recognition == df['Facial recognition'])))]

    if (len(rows) > 0):
        return rows.index[1]
    return None


def get_recommendations(cpu, storage_capacity, removable_storage, ram, os, battery, display, camera, fingerprint
                        , facial_recognition):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)

    user_preferences_index = get_index_from_features(cpu, storage_capacity, removable_storage, ram, os, battery,
                                                     display, camera, fingerprint, facial_recognition)
    similar_smartphones = list(enumerate(cosine_sim[user_preferences_index]))

    sorted_similar_smartphones = sorted(similar_smartphones, key=lambda x: x[1], reverse=True)[1:]

    max_recommendations = 10
    i = 0
    recommendations_list = []

    for element in sorted_similar_smartphones:
        if i < max_recommendations:
            recommendations_list.append(df["combined_features"][element[0]])
        else:
            return recommendations_list

        i += 1

def get_filters():
    filters = {}

    filters["cpu"] = (df["CPU"].unique()).tolist()
    filters["storage-capacity"] = (df["Storage capacity"].unique()).tolist()
    filters["removable-storage"] = (df["Removable storage"].unique()).tolist()
    filters["ram"] = (df["RAM"].unique()).tolist()
    filters["os"] = (df["OS"].unique()).tolist()
    filters["battery"] = (df["Battery"].unique()).tolist()
    filters["display"] = (df["Display"].unique()).tolist()
    filters["camera"] = (df["Camera"].unique()).tolist()
    filters["fingerprint-scanner"] = (df["Fingerprint scanner"].unique()).tolist()
    filters["facial-recognition"] = (df["Facial recognition"].unique()).tolist()

    return filters


features = ["CPU", "Storage capacity", "Removable storage", "RAM", "OS", "Battery", "Display", "Camera",
            "Fingerprint scanner", "Facial recognition"]

removeNaN(features)
