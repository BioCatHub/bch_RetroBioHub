import requests
import json

def test_retrobiohub_endpoint(url):
    """ Test the /retrobiohub post endpoint """

    url = url + '/retrobiohub/'

    test_data = [{"substrates": ["CC(N)c1ccccc1"],
                  "products": ["CC(=O)c1ccccc1"],
                  "cofactors": [["Amine"], ["Carbonyl"]],
                  "enzyme": "TA",
                  "reaction": "Secondary amine deamination",
                  }]

    response = requests.post(url, json=test_data)
    return json.loads(response.text)


def test_minimongo_endpoint(url, db_id):
    """ Test the /retrobiohub/minimongo get endpoint """

    url = url + '/retrobiohub/minimongo/'

    response = requests.post(url, json={'id': db_id})
    return json.loads(response.text)


# run flask app first, then try these tests
if __name__ == '__main__':
    test_url = 'http://127.0.0.1:5000'

    response_dict1 = test_retrobiohub_endpoint(test_url)
    response_dict1 = json.loads(response_dict1)
    print(response_dict1)

    db_id = response_dict1['id']
    print(db_id)

    response_dict2 = test_minimongo_endpoint(test_url, db_id)
    print(response_dict2)


