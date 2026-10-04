import requests
import pytest

website_url = 'https://www.1337tester.com/'
accepted_encodings = ('gzip', 'br', 'deflate', 'zstd')

testdata = [(1, 0.5, 0.5),
            (5, 6, -1),
            (1, 1, 1)]

def inc(x):
    return x + 1

@pytest.mark.parametrize("a, b, expected", testdata)
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected

def test_answer():
    assert inc(4) == 5

@pytest.fixture(scope="module")
def website_response():
    return requests.get(website_url)

def test_correct():
    assert inc(3) == 4

def test_website_on(website_response):
    assert website_response.status_code == 200

def test_website_encoding(website_response):
    assert website_response.headers['content-encoding'] in accepted_encodings
