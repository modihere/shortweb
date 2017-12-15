import json

from django.test import TestCase
from django.urls import reverse

from .views import is_already_short

# Create your tests here.
class IndexViewTests(TestCase):
	def test_default_index(self):
		'''
			test whether default home page is rendered or not
		'''
		response = self.client.get(reverse('shorturl:home'))
		self.assertEquals(response.status_code,200)

class MakeShortViewTests(TestCase):
	def test_shortening_normal_url(self):
		'''
			test whether normal URL is shortened or not.
		'''
		url = "https://www.github.com"
		response = self.client.post(reverse('shorturl:shortenurl'),data={'url':url})
		# Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes to make it valid JSON
		str_content = response.content.decode('utf8').replace("'", '"')
		json_content = json.loads(str_content)
		self.assertNotEquals(json_content['url'],"")
		self.assertEquals(response.status_code,200)

	def test_shortening_empty_url(self):
		'''
			test whether empty URL generates error or not
		'''
		url = ""
		response = self.client.post(reverse('shorturl:shortenurl'),data={'url':url})
		# Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes to make it valid JSON
		str_content = response.content.decode('utf8').replace("'", '"')
		json_content = json.loads(str_content)
		self.assertEquals(json_content['valid_url'],False)

	def test_shortening_shorteded_url(self):
		'''
			test whether already shorteded URL generates error or not
		'''
		url = "bit.ly/xyz"
		response = self.client.post(reverse('shorturl:shortenurl'),data={'url':url})
		# Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes to make it valid JSON
		str_content = response.content.decode('utf8').replace("'", '"')
		json_content = json.loads(str_content)
		self.assertEquals(json_content.get('already_short'),True)

'''
To test all the support function in views
'''
class ViewFunctionsTests(TestCase):
	def test_is_already_short_function(self):
		url = "https://www.github.com"
		self.assertEquals(is_already_short(url),False)
		url = "bit.ly/xyz"
		self.assertEquals(is_already_short(url),True)