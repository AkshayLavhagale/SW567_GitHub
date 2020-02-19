''' Akshay Lavhagale
    Homework 04a - Develop with the Perspective of the Tester in mind '''

import unittest
import HW04a_AkshayLavhagale


class TestMain(unittest.TestCase):
    def test_userid(self):
        # Testing whether the userid is correct or no
        self.assertEqual(HW04a_AkshayLavhagale.github_handle('AkshayLavhgale'), "The user ID does not exist")

    def test_get_total_commit(self):
        # Testing the number of commits for repositories
        self.assertEqual(HW04a_AkshayLavhagale.github_handle('richkempinski'), {'Mocks': 10, 'Project1': 2,
                                                                                'hellogitworld': 30, 'helloworld': 6,
                                                                                 'threads-of-life': 1})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
