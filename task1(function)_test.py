import unittest
import task1_function



class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task1_function.count(1,1,1),0)  # add assertion here

    def test_2(self):
        self.assertEqual(task1_function.count(-1, 1, 1), 1)  # add assertion here

    def test_3(self):
        self.assertEqual(task1_function.count(-1,-1,1),2)  # add assertion here

    def test_4(self):
        self.assertEqual(task1_function.count(-1,-1,-1),3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
