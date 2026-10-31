import unittest
from urllib.request import urlopen
from app import create_server
from threading import Thread


class TestDevOpsApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = create_server(port=8001)

        cls.thread = Thread(
            target=cls.server.serve_forever,
            daemon=True
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_homepage_status_code(self):
        response = urlopen("http://127.0.0.1:8001")

        self.assertEqual(response.status, 200)

    def test_homepage_content(self):
        response = urlopen("http://127.0.0.1:8001")
        html = response.read().decode("utf-8")

        self.assertIn(
            "Welcome to My DevOps Application!",
            html
        )


if __name__ == "__main__":
    unittest.main()