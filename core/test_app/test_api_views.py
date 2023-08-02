from django.test import TestCase , Client
from product.api.views import ProductVersionCreateAPIView
from django.urls import reverse_lazy




class ProductVersionCreateAPIViewTest(TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('products')
        client = Client()
        cls.response = client.get(cls.url)


    def test_url(self):
        self.assertEqual(self.url , '/api/products/')


    def test_request_status_code(self):
        self.assertEqual(self.response.status_code , 200)




    @classmethod
    def tearDownClass(cls) -> None:
        pass
