import requests
user_age = {'User-agent': "1e5"}
url ="http://web.darkarmy.xyz/"
res = requests.get(url,headers=user_age)
print(res.text)



# flag darkCTF{changeing_http_user_agent_is_easy}