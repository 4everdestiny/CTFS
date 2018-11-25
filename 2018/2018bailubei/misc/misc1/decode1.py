import json
with open("pcapng.json","r") as f:
    info = f.read()
    jsons = json.loads(info)
    f.close()
print len(jsons)
res = ""
for x in jsons:
    if x["_source"]["layers"]["frame"]["frame.coloring_rule.name"] == "ICMP" and x["_source"]["layers"]["icmp"]["data"]["data.len"] == "1":
        res += x["_source"]["layers"]["icmp"]["data"]["data.data"]

with open("flag","wb") as f:
    f.write(res)
    f.close()