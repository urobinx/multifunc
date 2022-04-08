import requests


def get(url_get, param):
    req = requests.get(url=url_get, params=param)
    content = req.text
    return content


def port(url_port, param):
    req = requests.post(url=url_port, json=param)
    content = req.text
    return content


if __name__ == "__main__":
    # url = "http://127.0.0.1:8000/api/threesum/"
    url = "http://127.0.0.1:8000/api/primes/"
    # params = {"nums": [3, 2, 4, 5],
    #           "target": 11
    #           }
    params = {
        "primes": [50, 90, 30, 10],
        }

    req_get = get(url, params)
    print(req_get)

    req_port = port(url, params)
    print(req_port)
