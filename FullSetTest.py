from ImageLoader import ImageLoader
from RoadSignModel import RoadSignModel

imageLoader = ImageLoader()
imageLoader.load_from('C:\\Users\\RTNDZ\\archive\\Train', 43)
model = RoadSignModel(imageLoader)

model.train()
model.save()