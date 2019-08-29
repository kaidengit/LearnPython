import json

with open("proxyjson.json","r") as f:
    js = f.read()

dic = json.loads(js)
print(dic)










"""
# 测试json
import json
import re
data1 = {
    "no": 1,
    "name": "Runoob",
    "url": "http://www.runoob.com"
}
json_str = json.dumps(data1)
print(type(json_str))
ks = str(data1)
print(type(ks))
print(ks)
print(json_str)

# ks = re.sub('\'','\"',ks)
# print(ks)
json.loads(ks)
"""