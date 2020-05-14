def improved_movie_recom(string_new):
    import os

    import numpy as np
    import pandas as pd

    data_new = pd.read_csv("cleaned_movie_dataset.csv")
    #data_new_1 = data_new.apply(lambda x: x.astype(str).str.upper())
    def combine(row):
        return str(row["genres"]) + " " + str(row["keywords"]) + " " + str(row["cast"]) + " " + str(row["director"]) + " " + str(row["new_f"])

    data_new["comb"] = data_new.apply(combine, axis=1)


    def title_to_ind(my_title):
        return data_new[data_new.title == my_title]["index"].values[0]

    def ind_to_title(my_ind):
        return data_new[data_new.index == my_ind]["title"].values[0]

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    cv = CountVectorizer()
    matrix = cv.fit_transform(data_new.comb)
    mt = matrix.toarray  # to convert it into array
    cos_mat = cosine_similarity(matrix)
    # ---------------
    # my_movie="Skyfall"
    my_index = title_to_ind(string_new)
    # print("movie is at index ",my_index)
    similar_movie = list(enumerate(cos_mat[my_index]))
    sorted_sim_movie = sorted(similar_movie, key=lambda x: x[1], reverse=True)
    # sorted_sim_movie

    similar_mov_list = []

    # print("SOME SIMILAR MOVIES ARE ...\n")
    for r in range(1, 11):
        similar_mov_list.append(ind_to_title(sorted_sim_movie[r][0]))
        # print(ind_to_title(sorted_sim_movie[r][0]))
    # print(similar_mov_list)

    return similar_mov_list

