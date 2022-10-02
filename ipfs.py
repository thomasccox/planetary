import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	out = open("output.json", "w")
	j_object = json.dump(data,out)
	files = {'json': "output.json"}

	response = requests.post("https://ipfs.infura.io:5001/api/v0/add", files=files,
							 auth=('2FPeQVd8LLXnoPVpvRa9eRo94lI', '4b1af682e8bdabfc43469ce05c41a21e'))
	dictionary = json.loads(response.text)
	cid = dictionary['Hash']
	#print(cid)
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	url = "https://ipfs.infura.io:5001/api/v0/cat?arg={" + cid + "}"
	params = {'arg': cid}
	response = requests.post("https://ipfs.infura.io:5001/api/v0/cat", params = params,
							 auth=('2FPeQVd8LLXnoPVpvRa9eRo94lI', '4b1af682e8bdabfc43469ce05c41a21e'))
	path = response.text
	read = open(path, "r")
	data = json.load(read)
	#print(path)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
