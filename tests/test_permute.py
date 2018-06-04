import unittest

# import tensorflow as tf
# import numpy as np
import hyperchamber as hc
# import hyperchamber.permute


class permute_test(unittest.TestCase):
    def test_one_permute(self):
        hc.reset()
        hc.set('x', 1)
        hc.set('y', [1])
        self.assertEqual(hc.count_configs(), 1)
        self.assertEqual(hc.configs(1, serial=True,offset=0,create_uuid=False), [{'x':1, 'y': 1}])

    def test_many_permute(self):
        hc.reset()
        hc.set('x', 1)
        hc.set('y', [1, 2, 2])
        self.assertEqual(hc.count_configs(), 3)
        self.assertEqual(hc.configs(1, serial=True,offset=0,create_uuid=False), [{'x':1, 'y': 1}])

    def test_many_to_many(self):
        hc.reset()
        hc.set('x', [1,2,3])
        hc.set('y', [1, 2, 3])
        self.assertEqual(hc.count_configs(), 9)
        configs = hc.configs(3, serial=True,create_uuid=False,offset=0)
        self.assertNotEqual(configs[0], configs[1])
        self.assertNotEqual(configs[1], configs[2])

    def test_many_to_many_nested(self):
        hc.reset()
        hc.set('x', [1, 2, 3])
        hc.set('y', [1, 2, 3])
        hc.set('z', [1, 2, 3])
        self.assertEqual(hc.count_configs(), 27)
        self.assertEqual(hc.configs(1, serial=True,offset=0,create_uuid=False), [{'x':1, 'y': 1, 'z': 1}])
        
        # TODO: These results are not in a guaranteed order since store is a dictionary.  
        # These tests dont pass reliable
        #self.assertEqual(hc.configs(1,offset=1), [{'x':1, 'y': 1, 'z': 2}])
        #self.assertEqual(hc.configs(1,offset=5), [{'x':1, 'y': 1, 'z': 2}])

    def test_only_permutation(self):
        hc.reset()
        for i in range(20):
          hc.set('a'+str(i), [1, 2, 3])
        self.assertEqual(hc.count_configs(), 3**20)
        self.assertEqual(hc.configs(1, serial=True, offset=0)[0]['a1'], 1)
        self.assertEqual(hc.configs(1, serial=True, offset=0)[0]['a2'], 1)


if __name__ == '__main__':
    unittest.main()
