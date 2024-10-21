import unittest
from url_parser import parse

class TestParseFunction(unittest.TestCase):

    def setUp(self):
        self.url = "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png?utm_source=instagram"
        self.url2 = "http://upload.wikimediainthehouse.org:8080/wikipedia/commons/6/6a/JavaScript-logo.png?utm_source=instagram"

    def test_scheme(self):
        self.assertEqual(parse(self.url)['scheme'], "https")
        self.assertEqual(parse(self.url2)['scheme'], "http")

    def test_host(self):
        self.assertEqual(parse(self.url)['host'], "upload.wikimedia.org")
        self.assertEqual(parse(self.url2)['host'], "upload.wikimediainthehouse.org")

    def test_port(self):
        self.assertEqual(parse(self.url)['port'], 80)
        self.assertEqual(parse(self.url2)['port'], 8080)

    def test_path(self):
        expected_path = "/wikipedia/commons/6/6a/JavaScript-logo.png"
        self.assertEqual(parse(self.url)['path'], expected_path)
        self.assertEqual(parse(self.url2)['path'], expected_path)

    def test_query(self):
        self.assertEqual(parse(self.url)['query'], "utm_source=instagram")
        self.assertEqual(parse(self.url2)['query'], "utm_source=instagram")

    def test_query_with_campaign(self):
        url_with_campaign = self.url2 + "&utm_campaign=feature%20launch"
        self.assertEqual(parse(url_with_campaign)['query'], "utm_source=instagram&utm_campaign=feature%20launch")


if __name__ == "__main__":
    unittest.main()
