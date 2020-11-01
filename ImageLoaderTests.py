import unittest
import numpy as np
from ImageLoader import ImageLoader
from PIL import Image

imageLocation = './test-images'

class TestImageLoader(unittest.TestCase):
    
    def test_Create_Image_Loader(self):

        loader = ImageLoader() 

    def test_load_images_from_one_category(self):

        numberOfImages = 30

        loader = ImageLoader()
        loader.load_from(imageLocation, 1)

        images = loader.get_images()
        labels = loader.get_labels()

        self.assertEqual(numberOfImages, len(images))
        self.assertIs(np.ndarray, type(images))
        self.assertIs(np.ndarray, type(images[0]))

        np.testing.assert_array_equal(np.zeros(numberOfImages), labels)
        self.assertIs(np.ndarray, type(labels))

    def test_load_images_from_two_categories(self):

        numberOfImages = 60

        loader = ImageLoader()
        loader.load_from(imageLocation, 2)

        images = loader.get_images()
        labels = loader.get_labels()

        self.assertEqual(numberOfImages, len(images))
        self.assertIs(np.ndarray, type(images))
        self.assertIs(np.ndarray, type(images[0]))
        np.testing.assert_array_equal(np.zeros(30), labels[:30])
        np.testing.assert_array_equal(np.ones(30), labels[30:numberOfImages])
        self.assertIs(np.ndarray, type(labels))

    def test_images_are_resized(self):

        loader = ImageLoader()
        loader.load_from(imageLocation, 1)

        images = loader.get_images()

        for image in images:
            self.assertEqual('(30, 30, 3)', str(image.shape))


if __name__ == '__main__':
    unittest.main()