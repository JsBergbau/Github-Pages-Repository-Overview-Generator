githubusername="jsbergbau"

import urllib.request, json

def getJSON(url:str):
	return json.loads(urllib.request.urlopen(url).read().decode())

url = "https://api.github.com/users/" + githubusername + "/repos"
data = getJSON(url)
print("# All repositories created by JSBergbau")

for entry in data:
	if entry["name"] == githubusername + ".github.io": #Don't display own Webpage repository
		continue
	if entry["fork"] == False: #only own repositories
		heading = f'## [{entry["name"]}]({entry["html_url"]})'
		print(heading,"\n")
		print(f'URL: [{entry["html_url"]}]({entry["html_url"]})\n')
		print("Description:", entry["description"],"\n")
		print("Created: ",entry["created_at"],"\n")
		print("Last update:",entry["updated_at"],"\n")
