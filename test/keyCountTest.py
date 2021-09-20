import unittest
from keyCount import *

class MyTestCase(unittest.TestCase):
    def test_readfile(self):
        path = "./test_read.c"
        ans = "int main(){ } "
        self.assertEqual(read_file(path), ans)

    def test_count_keys(self):
        code = read_file("./test_matchCode.c")
        self.assertEqual(count_keys(code),53)

    def test_count_switch(self):
        code = read_file("./test_matchCode.c")
        self.assertEqual(count_switch(code), (2, [3, 2]))

    def test_count_if_else(self):
        code = read_file("./test_matchCode.c")
        self.assertEqual(count_if_else(code), (4, 4))

if __name__ == '__main__':
    unittest.main()