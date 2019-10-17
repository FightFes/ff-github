import unittest
import filesys
import os

class TestFilesys(unittest.TestCase):
    def setUp(self):
        self.home = os.path.expanduser('~')

    def test_make_dir(self):
        #  path = os.path.expanduser('~/ff-github/test/test_sub/test_sub_sub')
        filesys.make_dir(self.home + '/ff-github/test/copy_origin')
        filesys.make_dir(self.home + '/ff-github/test/copy_target')
        filesys.make_dir(self.home + '/ff-github/test/move_origin')
        filesys.make_dir(self.home + '/ff-github/test/move_target')

    def test_copy(self):
        filesys.copy(self.home + '/ff-github/test/copy_origin', self.home + '/ff-github/test/copy_target')

    def test_move(self):
        filesys.move(self.home + '/ff-github/test/move_origin', self.home + '/ff-github/test/move_target')

    def test_remove(self):
        filesys.remove(self.home + '/ff-github/test/copy_origin')
        filesys.remove(self.home + '/ff-github/test/copy_target')
        filesys.remove(self.home + '/ff-github/test/move_origin')
        filesys.remove(self.home + '/ff-github/test/move_target')

    def test_write_file(self):

    def test_read_file(self):
        
if __name__ == '__main__':
    unittest.main()
