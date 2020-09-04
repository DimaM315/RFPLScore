import unittest

from app import app

client = app.test_client()


class Test(unittest.TestCase):
	def setUp(self):
		pass
	
	@unittest.skip('skip')	
	def test_main(self):
		pass


if __name__ == '__main__':
	#unittest.main()
	res = client.get('/')
	print(dir(res))
	#print(client.get_json())
	print(client.post('/', json={'par':'val'}))