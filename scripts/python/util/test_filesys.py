import unittest
import filesys
import os

class TestFilesys(unittest.TestCase):
    def test_make_dir(self):
        filesys.make_dir('C:/User/taiki/ff-github/test')
        
if __name__ == '__main__':
    unittest.main()
