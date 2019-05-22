import os
import unittest
import myapp
import pytest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        myapp.app.testing = True
        self.app = myapp.app.test_client()

    def tearDown(self):
		pass

    def test_mainmenu(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Survey Results', response.data)

# Method	Equivalent to
# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)
# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.

if __name__ == '__main__':
    unittest.main()
	
