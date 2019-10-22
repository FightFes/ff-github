import unittest
import filesys
import os

class TestFilesys(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.expanduser('~') + '/ff-github/test'

    def test_make_dir(self):
        filesys.make_dir(self.test_dir + '/make_dir')

    def test_copy(self):
        origin_path = self.test_dir + '/copy_origin'
        filesys.make_dir(origin_path)
        filesys.copy(origin_path, self.test_dir + '/copy_target')

    def test_move(self):
        origin_path = self.test_dir + '/move_target'
        filesys.make_dir(origin_path)
        filesys.move(origin_path, self.test_dir + '/move_target')

    def test_remove(self):
        target_path = self.test_dir + '/remove_dir'
        filesys.make_dir(target_path)
        filesys.remove(target_path)

    def test_write_file(self):
        filesys.write_file(self.test_dir + '/write_read.txt', 'test')

    def test_read_file(self):
        filesys.read_file(self.test_dir + '/write_read.txt')
        
if __name__ == '__main__':
    unittest.main()
