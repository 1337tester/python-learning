import requests


def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def website_call(website = 'https://www.1337tester.com/'):
    return requests.get(website)
    
def test_correct():
    assert inc(3) == 4

def test_website_on():
    assert website_call().status_code == 200

def test_website_encoding():
    assert website_call().headers['content-encoding'] == 'gwzip'
