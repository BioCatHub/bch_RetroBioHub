import requests

def test_retrobiohub_endpoint(url):
    ''' Test the /retrobiohub post endpoint '''
    url = url + '/retrobiohub/'

    test_data = [{"substrates": ["CC(N)c1ccccc1"],
                  "products": ["CC(=O)c1ccccc1"],
                  "cofactors": [["Amine"], ["Carbonyl"]],
                  "enzyme": "TA",
                  "reaction": "Secondary amine deamination",
                  }]

    response = requests.post(url, json=test_data)
    return response


# run flask app first, then try these tests
if __name__ == '__main__':
    test_url = 'http://127.0.0.1:5000'

    response = test_retrobiohub_endpoint(test_url)
    print(response.text)



