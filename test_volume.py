import unittest
import volume

class Testvolume(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(volume.calc_volume(5),125)

    def test_negative(self):
        with self.assertRaises(ValueError):
            volume.calc_volume(-2)
    
    def test_type(self):
        with self.assertRaises(TypeError):
            volume.calc_volume('Bolaji')

if __name__ == "__main__":
    unittest.main()