
import requests
import json
from flask import Flask

page=1

last_page=0


def send_request(page):

    # Request
    # GET https://developers.buymeacoffee.com/api/v1/supporters
    try:
        response = requests.get(
            url="https://developers.buymeacoffee.com/api/v1/supporters",
            params={
                "page":page,
            },
            headers={
                "Authorization": "Bearer [ACCESS TOKEN GOES HERE]",
            },
        )
        jsonResponse = response.json()
        globals()['last_page']=jsonResponse["last_page"]
        suplist=""
        for data_i in range(0,len(jsonResponse["data"])):
        	print(data_i)
        	sup_name=jsonResponse["data"][data_i]["payer_name"]

        	if len(sup_name)<1:
        		sup_name="Someone"
        	print("supname is:",sup_name)
        	suplist=suplist+","+sup_name

        #print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
    #    print(response.js


    
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return suplist


firstreq=send_request(1)

supporters=""
for i in range (1,last_page+1):
	print("adding sups")
	supporters=supporters+","+send_request(i)


print("processed lastpage",last_page)
print("supdata",supporters)
supporters="[_]b by -> "+supporters

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_supp():
  return supporters

if __name__ == '__main__':
    api.run("0.0.0.0")

