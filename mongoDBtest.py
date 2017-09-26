from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['5Aniem']
banime = db.BAnime

# tenanime_data = {
#     'title': '10 anime titles for testing purposes',
#     'content': 'list of 10 anime and their details',
#     'author': 'Jack and Ziad'
# }
# result = tenanime.insert_one(tenanime_data)
# print('One post: {0}'.format(result.inserted_id))

# post_1 = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# post_2 = {
#     'title': 'Virtual Environments',
#     'content': 'Use virtual environments, you guys',
#     'author': 'Scott'
# }
# post_3 = {
#     'title': 'Learning Python',
#     'content': 'Learn Python, it is easy',
#     'author': 'Bill'
# }
# new_result = tenanime.insert_many([post_1, post_2, post_3])
# print('Multiple tenanime: {0}'.format(new_result.inserted_ids))

# anime = tenanime.find_one({"name" : "Abenobashi"})
# print(anime)

# anime = tenanime.find({"name" : "Abenobashi"})
# print(anime)
# for info in anime:
#     print(info)


# anime = banime.update_many({}, {'$set': {"completed": ""}})
# anime2 = banime.update_many({}, {'$set': {"description": " "}})
# anime3 = banime.update_many({}, {'$set': {"rating": " "}})
# anime4 = banime.update_many({}, {'$set': {"date aired": " "}})
# print(anime, anime2, anime3, anime4)









for i in range(1, 133):
    banime_data = {
        'name': '',
    }
    result = banime.insert_one(banime_data)
    print('One post: {0}'.format(result.inserted_id))

anime = banime.update_many({}, {'$set': {"genre": "Action"}})
anime1 = banime.update_many({}, {'$set': {"episodes": ""}})
anime2 = banime.update_many({}, {'$set': {"type": "Tv Show"}})
anime3 = banime.update_many({}, {'$set': {"completed": True}})
anime4 = banime.update_many({}, {'$set': {"description": ""}})
anime5 = banime.update_many({}, {'$set': {"rating": " "}})
anime7 = banime.update_many({}, {'$set': {"date aired": " "}})   
print(anime, anime2, anime3, anime4, anime5, anime7)
