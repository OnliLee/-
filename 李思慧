import pandas as pd
from math import sqrt
def get_person_rating(data):
    person_rating = {}
    for j in range(1, 5):
        personj_rating = []
        for i in range(1, 5):
            personj_rating.append(data[data["movie_id"]==i][data["user_id"]==j]
["rating"].values[0])
        person_rating[j] = personj_rating
    for i in range(1, 5):
        person_rating[i] = data[data["user_id"]==i]["rating"].values
    return person_rating

def get_distance(person_rating, index):
    me = person_rating[4] 
    it = person_rating[index]
    sum = 0
    for i in range(0, 4):
        sum = sum + pow(me[i]-it[i],2)
    return sqrt(sum)
data = pd.read_csv("movie.csv")
person_rating = get_person_rating(data)
distance = {}
for i in range(1, 4):
distance[i] = get_distance(person_rating, i)
    print(distance)
    
min_index = 0
min_value = 1000
for key, value in distance.items():
    print("key：%s, value %s" %(key,value))
    if min_value > value:
        min_value = value
        min_index = key
print(min_index)
