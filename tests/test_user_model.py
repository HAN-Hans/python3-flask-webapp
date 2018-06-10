import unittest

from app.models import Role, User, Permission, AnonymousUser


class UserModelTestCase(unittest.TestCase):

    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email="2@1.com", password="cat")
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
