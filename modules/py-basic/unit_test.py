import unittest


class TestStringMethod(unittest.TestCase):

    def test_strip(self):
        self.assertEqual('www.test.com'.strip('c.mow'), 'testing')

    def test_isalnum(self):
        self.assertTrue('c0ding'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    def test_index(self):
        s = 'angga'
        self.assertEqual(s.index('ga'), 4)

        with self.assertRaises(ValueError):
            s.index('go')



# more real example
def db_connect():
    print("[connected to db]")

def db_disconnect(db):
    print("[disconnnected to db {}]".format(db))


class User:
    username = ""
    is_active = False

    def __init__(self, db, username):
        self.username = username

    def set_active(self):
        self.is_active = True


class TestUser(unittest.TestCase):
    # case 1
    
    def test_default_inactive_user(self):
        db = db_connect()
        angga = User(db, "angga")
        self.assertFalse(angga.is_active) # inactive by default
        db_disconnect(db)

    def test_user_is_active(self):
        db = db_connect()
        angga = User(db, "angga")
        angga.set_active()
        self.assertTrue(angga.is_active)
        db_disconnect(db)



# test fixture, setUp() and tearDown()
class TestUser2(unittest.TestCase):
    # test fixture
    def setUp(self) -> None:
        self.db = db_connect()
        self.angga = User(self.db, "angga")

    def tearDown(self) -> None:
        db_disconnect(self.db)

    # test case 1
    def test_default_inactive_user(self):
        self.assertFalse(self.angga.is_active)


    # test case 2
    def test_user_is_active(self):
        self.angga.set_active()
        self.assertTrue(self.angga.is_active)

if __name__ == '__main__':
    unittest.main()












