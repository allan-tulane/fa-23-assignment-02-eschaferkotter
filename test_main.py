from main import *


## Feel free to add your own tests here.
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
  assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10 * 10
  assert subquadratic_multiply(BinaryNumber(200), BinaryNumber(200)) == 200 * 200