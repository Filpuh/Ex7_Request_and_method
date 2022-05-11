import requests

#1 GET http-запрос без параметра method
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"сообщение в пункте 1: {response1.text}")

#2 PATCH http-запрос (запрос не из списка)
response2 = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"сообщение в пункте 2: {response2.text}")

#3 запрос с правильным значением method
response3_1 = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PATCH"})
print(f"сообщение в пункте 3 при запросе не из списка (PATCH), с правильным method: {response3_1.text}")

response3_2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(f"сообщение в пункте 3 при запросе из списка (GET), с правильным method: {response3_2.text}")

#4 С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method
params= [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for i in [0,1,2,3]:

    response_4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params= params[i])
    print(f"сообщение в пункте 4.{i} для GET запроса с {params[i]}: {response_4.text}")

    response_5 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params[i])
    print(f"сообщение в пункте 5.{i} для POST запроса с {params[i]}: {response_5.text}")

    response_6 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params[i])
    print(f"сообщение в пункте 6.{i} для PUT запроса с {params[i]}: {response_6.text}")

    response_7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data= params[i])
    print(f"сообщение в пункте 7.{i} для DELETE запроса с {params[i]}: {response_7.text}")
