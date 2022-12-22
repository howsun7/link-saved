import unittest
from unittest import TestCase

from src.core import Link

class LinkTest(TestCase):

	def test_is_valid_link_return_false_for_invalid_link(self):
		bad_link = Link('bad link')
		self.assertEqual(bad_link.is_valid_link(), False)

	def test_is_valid_link_return_true_for_valid_link(self):
		link = Link('https://www.python.org')
		self.assertEqual(link.is_valid_link(), True)
		
if __name__ == '__main__':
	unittest.main()