# API Testing
# 1
# import requests
#
#
# response = requests.get("https://api.github.com/users/avielb/repos")
# if response.status_code == 200:
#     rep = response.json()
#     # print(f"Number of repo's:{len(rep)}")
#     assert 5 <= len(rep)
# else:
#     print(f"Repo's were unreachable. Status code: {response.status_code}")
# #



# 2

# import requests
# import names

# my_names = []
# for i in range(3):
    # # names_ido = requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()
    # # print(names_ido["name"], names_ido["age"])
    # if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
            # my_names.append(i)
# assert len(my_names) == 0



# 3
#
# import requests
#
#
# expected = 5
#
# response = requests.get("http://universities.hipolabs.com/search?country=Israel")
# if response.status_code == 200:
#     rep = response.json()
#     # print(f"Number of repo's:{len(rep)}")
#     assert expected <= len(rep)
# else:
#     print(f"Repo's were unreachable. Status code: {response.status_code}")
#

#
# # 4
# # #
# from selenium import webdriver
# dr = webdriver.Chrome()
# dr.get("https://www.ycombinator.com/")
#
# print(dr.title)
# assert dr.title == "Y Combinator"
#


# 5
#
# from selenium import webdriver
# dr = webdriver.Chrome()
# dr.get("https://hub.docker.com/")
#
# print(dr.title)
# assert dr.title == "Docker Hub Container Image Library | App Containerization"