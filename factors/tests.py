from django.test import Client, TestCase


from django.urls import reverse


from .models import Factor


class FactorTests(TestCase):
  def setUp(self):
    self.book = Factor.objects.create(
      factor_id = "2",
      ac = "2",
      dt = "2",
      de = "2",
      kw = "2",
      os = "2",
      ra = "2",
      rt = "2",
      rl = "2",
      rd = "2",
      sq = "2",
    )
  
  def test_factor_listing(self):
    self.assertEqual(f'{self.book.factor_id}', "2")
    self.assertEqual(f'{self.book.ac}', "2")
    self.assertEqual(f'{self.book.dt}', "2")
    self.assertEqual(f'{self.book.de}', "2")
    self.assertEqual(f'{self.book.kw}', "2")
    self.assertEqual(f'{self.book.os}', "2")
    self.assertEqual(f'{self.book.ra}', "2")
    self.assertEqual(f'{self.book.rt}', "2")
    self.assertEqual(f'{self.book.rl}', "2")
    self.assertEqual(f'{self.book.rd}', "2")
    self.assertEqual(f'{self.book.sq}', "2")

  
  def test_factor_list_view(self):
    response = self.client.get(reverse('factor_list'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, '2')
    self.assertTemplateUsed(response, 'factors/factor_list.html')

  
  def test_factor_ac_view(self):
    response = self.client.get(self.book.get_absolute_url())
    no_response = self.client.get('/factors/12345/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, '2')
    self.assertTemplateUsed(response, 'factors/factor_ac.html')

