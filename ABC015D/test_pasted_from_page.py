#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """10
3 2
4 20
3 40
6 100"""
        output = """140"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10
5 4
9 10
3 7
3 1
2 6
4 5"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """22
5 3
5 40
8 50
3 60
4 70
6 80"""
        output = """210"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
