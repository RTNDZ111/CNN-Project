import unittest
from RoadSignModel import RoadSignModel
from ImageLoader import ImageLoader
import os

class TestRoadSignModel(unittest.TestCase):

    def xtest_InstantiateModel(self):

        model = RoadSignModel(None)

    def xtest_TrainModel(self):
        
        imageLoader = ImageLoader()
        imageLoader.load_from('./test-images', 1)
        model = RoadSignModel(imageLoader)

        self.assertEqual(False, model.is_trained())

        model.train()

        self.assertEqual(True, model.is_trained())

    def test_SaveModel(self):

        imageLoader = ImageLoader()
        imageLoader.load_from('./test-images', 1)
        model = RoadSignModel(imageLoader)

        os.remove('model.h5')

        model.train()
        model.save()

        self.assertEqual(True, os.path.exists('model.h5'))
        



if __name__ == '__main__':
    unittest.main()