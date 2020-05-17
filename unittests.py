import unittest
import gmail_bot_functions as gb

#Sources:
# testing an exception: https://nickolaskraus.org/articles/how-to-test-a-function-that-raises-an-exception/

class Tests(unittest.TestCase):

#	def setUp(self):
#		self.service = 

	def test_auth_averneus(self):
		self.assertRaises(Exception, gb.auth_service_to("averneus"))

	def test_auth_alihandikel(self):
		self.assertRaises(Exception, gb.auth_service_to("alihandikel"))


if __name__ == '__main__':
	unittest.main()


