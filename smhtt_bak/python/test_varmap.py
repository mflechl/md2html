import unittest
from varmap import VarMap

class TestVarMap(unittest.TestCase):

    def test_1(self):
        vm = VarMap([
            ('a', 'b'),
            ('c', 'd'),
        ])
        self.assertEqual(vm.tob['a'], 'b')
        self.assertEqual(vm.toa['b'], 'a')
        vm = VarMap([
            ('a', 'b'),
            ('b', 'a'),
        ])       
        self.assertEqual(vm.tob['a'], 'b')
        self.assertEqual(vm.toa['b'], 'a')

    def test_2_load(self):
        vm = VarMap('test_vars.txt')
        self.assertEqual(vm.tob['a'], 'b')
        self.assertEqual(vm.toa['b'], 'a')
        self.assertEqual(vm.tob['c'], 'd')
        self.assertEqual(vm.toa['d'], 'c')
        self.assertEqual(vm.tob['f'], 'h')

    def test_3_raise(self):
        with self.assertRaises(ValueError) as err:
            vm = VarMap([
                ('a', 'b'),
                ('a', 'd'),
            ])
        with self.assertRaises(ValueError) as err:
           vm = VarMap([
                ('a', 'b'),
                ('c', 'b'),
            ])
           
if __name__ == '__main__':
    unittest.main()
