import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from ImageLoader import ImageLoader
from RoadSignModel import RoadSignModel

class TestGUI():
           
    def __init__(self):
        self.window = tk.Tk()
        self.category = StringVar()
"""
        self.sign_name = ['Speed limit (20km/h)',
                          'Speed limit (30km/h)',      
                          'Speed limit (50km/h)',       
                          'Speed limit (60km/h)',      
                          'Speed limit (70km/h)',    
                          'Speed limit (80km/h)',      
                          'End of speed limit (80km/h)',     
                          'Speed limit (100km/h)',    
                          'Speed limit (120km/h)',     
                          'No passing',   
                          'No passing veh over 3.5 tons',     
                          'Right-of-way at intersection',     
                          'Priority road',    
                          'Yield',     
                          'Stop',       
                          'No vehicles',       
                          'Veh > 3.5 tons prohibited',       
                          'No entry',       
                          'General caution',     
                          'Dangerous curve left',      
                          'Dangerous curve right',   
                          'Double curve',      
                          'Bumpy road',     
                          'Slippery road',       
                          'Road narrows on the right',  
                          'road work',    
                          'Traffic signals',      
                          'Pedestrians',     
                          'Children crossing',     
                          'Bicycles crossing',       
                          'Beware of ice/snow',
                          'Wild animals crossing',      
                          'End speed + passing limits',      
                          'Turn right ahead',     
                          'Turn left ahead',       
                          'Ahead only',      
                          'Go straight or right',      
                          'Go straight or left',      
                          'Keep right',     
                          'Keep left',      
                          'Roundabout mandatory',     
                          'End of no passing',      
                          'End no passing veh > 3.5 tons' ]
"""

    def openFile(self):
        filename = tk.filedialog.askopenfilename()
        imageLoader = ImageLoader()
        image = imageLoader.get_image(filename)

        model = RoadSignModel()
        model.load('./models/fullset-10epochs.h5')

        category = model.predict_class(image)
        print('Category =', self.sign_name(category - 1))
        self.category.set(category)

    def showWindow(self):

        self.window.geometry('800x500')

        button = tk.Button(text = 'Select an image', command=self.openFile)
        button.pack()

        self.label = tk.Label(textvariable = self.category)
        self.label.pack()

        self.window.mainloop()

if __name__ == '__main__':
    gui = TestGUI()
    gui.showWindow()    