#Testing your code
#writing your first test
#executing your first test
import unittest

# class Testsum(unittest.TestCase):
#     def test_sum():
#         assert sum([1, 2, 3]) == 6, "Should be 6"

#     def test_sum_tuple():
#         assert sum((1, 2, 2)) == 6, "Should be 6"



target = __import__("test.py")
sum = target.sum

# if __name__ == "__main__":
#    unittest.main()

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
    
#The test results were mixed bieng half failed an dhalf no fail
#The test results mean that there is or is not a error
#When looking at what test results mean after doing the assignment was the question is the program working or not
#And it was a statment to me to fix whatevers not working