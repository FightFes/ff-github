import unittest
import filesys
import os

class TestFilesys(unittest.TestCase):
    def test_make_dir(self):
        path = os.path.expanduser('~/ff-github/test/test_sub/test_sub_sub')
        filesys.make_dir(path)
        
if __name__ == '__main__':
    unittest.main()
