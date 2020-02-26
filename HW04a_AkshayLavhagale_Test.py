''' Akshay Lavhagale
    Homework 04a - Develop with the Perspective of the Tester in mind '''

import unittest
from unittest import mock
import HW04a_AkshayLavhagale


class TestMain(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_github_handle(self, mock_return):
        # Testing the number of commits for repositories
        mock_return.side_effect = [
            '[{"name" : "567"}, {"name" : "API-567"}]',
            '[{"1" : "richkempinski"}, {"2" : "richkempinski"}]',
            '[{"1" : "richkempinski"}, {"2" : "richkempinski"}, {"3" : "richkempinski"}]'
        ]
        self.assertEqual(HW04a_AkshayLavhagale.github_handle('richkempinski'), {'Mocks': 10, 'Project1': 2,
                                                                                'hellogitworld': 30, 'helloworld': 6,
                                                                                 'threads-of-life': 1})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
