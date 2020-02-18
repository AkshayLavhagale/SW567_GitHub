''' Akshay Lavhagale
    Homework 04a - Develop with the Perspective of the Tester in mind '''

import unittest
import HW04a_AkshayLavhagale


class TestMain(unittest.TestCase):
    def test_userid(self):
        # Testing whether the userid is correct or no
        self.assertEqual(HW04a_AkshayLavhagale.github_handle('AkshayLavhgale'), "The user id does not exist")

    def test_get_total_commit(self):
        # Testing the number of commits for repositories
        self.assertEqual(HW04a_AkshayLavhagale.github_handle('AkshayLavhagale'), {'Fractions': 1, 'helloworld': 1,
                                                                                  'knn': 1, 'K_Means_Clustering': 1,
                                                                                  'Linear-Regression': 1, 'SE_540': 1,
                                                                                  'svm': 1, 'SW567_GitHub': 2,
                                                                                  'SW_567_HW_01': 2,
                                                                                  'Testing': 1, 'Triangle567': 5})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
