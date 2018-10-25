import json
import pandas as pd

f = open('article2user.json')
data = json.load(f)

dict_avg = {}

for each_url in data:
	dict_avg[each_url] = {}
	count = 0
	url_sum = 0
	for each_user in data[each_url]:
		local_sum = 0
		for each_time in data[each_url][each_user]:
			local_sum+=each_time
		count+=1
		url_sum+=local_sum
	url_avg = float(url_sum) / count

	for each_user in data[each_url]:
		local_sum = 0
		for each_time in data[each_url][each_user]:
			local_sum+=each_time
		dict_avg[each_url][each_user] = float(local_sum) / url_avg


df = pd.DataFrame(data=dict_avg)
df.to_csv("df.csv", index=False)