from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)
api = Api(app)

df = pd.read_csv("recommender/dataset/netflix.csv")

features = ['title','cast','country', 'release_year', 'director', 'listed_in', 'duration']

class Recommendations(Resource):
    # return a list of recommendations
    def get(self):
        self.removeNaN(features)
        return jsonify(
            self.get_recommendations(request.args.get('title'),
                                     request.args.get('cast'),
                                     request.args.get('country'),
                                     request.args.get('release_year'),
                                     request.args.get('director'),
                                     request.args.get('listed_in'),
                                     request.args.get('duration')))

    def removeNaN(self, featuresList):
        for feature in featuresList:
            df[feature] = df[feature].fillna('')  # filling all NaNs with blank string

        df['combined_features'] = df.apply(self.combine_features, axis=1)  # applying combined_features() method over each rows


    def combine_features(self, row):
        return row['title'] + ' ' + row['cast'] + ' ' + row['country'] + ' ' + str(row['release_year']) + ' ' + row['director'] + ' ' + row['listed_in'] + ' ' + row['duration']


    def get_recommendations(self, title, cast, country, release_year, director, listed_in, duration):
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df["combined_features"])
        cosine_sim = cosine_similarity(count_matrix)

        user_preferences_index = self.get_index_from_features(title, cast, country, release_year, director, listed_in, duration)
                
        similar_movies = list(enumerate(cosine_sim[user_preferences_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

        max_recommendations = 20
        i = 0
        recommendations_list = []

        for element in sorted_similar_movies:
            if i < max_recommendations:
                recommendations_list.append(df["combined_features"][element[0]])
            else:
                return recommendations_list

            i += 1

    def get_index_from_features(self, title, cast, country, release_year, director, listed_in, duration):
        rows = df[(((title == None) | (title == df['title']))) &
              (((cast == None) | (cast == df['cast']))) &
              (((country == None) | (country == df['country']))) &
              (((release_year == None) | (release_year == str(df['release_year'])))) &
              (((director == None) | (director == df['director']))) &
              (((listed_in == None) | (listed_in == df['listed_in']))) &
              (((duration == None) | (duration == df['duration'])))]
        
        if (len(rows) > 0):
            return rows.index[0]
        
        return None


class Filters(Resource):
    # return a list of filters
    def get(self):
        return jsonify(self.get_filters())

    def get_filters(self):
        filters = {}

        filters["title"] = (df["title"].unique()).tolist()
        filters["cast"] = (df["cast"].unique()).tolist()
        filters["country"] = (df["country"].unique()).tolist()
        filters["release_year"] = ((df["release_year"]).unique()).tolist()
        filters["director"] = (df["director"].unique()).tolist()
        filters["listed_in"] = (df["listed_in"].unique()).tolist()
        filters["duration"] = (df["duration"].unique()).tolist()

        return filters


api.add_resource(Recommendations, '/recommendations')
api.add_resource(Filters, '/filters')

if __name__ == '__main__':
    app.run()



