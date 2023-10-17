from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from PIL import Image

from PIL import Image
import random

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]

    def load_image(self):
        self.ids.image.source = self.ids.img.text
    def vertical_lines(self,image, name, red, green, blue):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if x % 15 < 2:
                    pixels[x, y] = (red, green, blue)
        img.save(name + "_vertical.png")
        self.ids.image.source = name+"_vertical.png"

    def diagnol_lines(self,image, name, red, green, blue):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if (x - y) % 40 < 5:
                    pixels[x, y] = (red, green, blue)
        img.save(name + "_diagonal.png")
        self.ids.image.source = name + "_diagonal.png"

images = ["space.jpg"]
index = 0
PhotoGalleryApp().run()