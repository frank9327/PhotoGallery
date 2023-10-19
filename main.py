from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from PIL import Image

from PIL import Image
import random

from kivy.uix.widget import Widget


class PhotoGalleryApp(App):
    pass

class MouseTouch(Widget):
    txtinput = ObjectProperty(None)
    button = ObjectProperty(None)
    image = ObjectProperty(None)
    def on_touch_down(self,touch):
        x, y = touch.x, touch.y
        print("X coordinate: " + str(int(coords[0])) + " Y coordinate: " + str(int(coords[1])))
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_up(touch)

    def on_touch_up(self, touch):
        print("\nMouse Button Pressed")
        coords = touch.pos
        print("X coordinate: "+str(int(coords[0])) + " Y coordinate: "+str(int(coords[1])))
        self.button.background_color = "black"
        self.button.color = "white"
        self.button.on_press = self.say_hello()
    def say_hello(self):
        print("hello")
class Display(Screen):
    def display_image(self):
        return images[index]

    def load_image(self):
        self.ids.image.source = self.ids.img.text

    def pixelate(self,image, name, x, y, width, height):
        img = Image.open(image)
        pixels = img.load()
        for yy in range(y, y + width, 10):
            for xx in range(x, x + height, 10):
                color = pixels[xx, yy]
                for yyy in range(yy, yy + 10):
                    for xxx in range(xx, xx + 10):
                        pixels[xxx, yyy] = color
        img.save(name + "_pixelate.png")
        self.ids.image.source = name+"_pixelate.png"

    def invert(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(self.ids.image.source + "_inverted.png")
        self.ids.image.source = self.ids.image.source+"_inverted.png"

    def sepia(self, image):
        img=Image.open(image)
        pixels=img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red=pixels[x,y][0]
                green=pixels[x,y][1]
                blue=pixels[x,y][2]
                red = int(red*.393 + green*0.769 +blue*0.189)
                green = int(red*.349 + green*0.686 +blue*0.168)
                blue = int(red*.272 + green*0.534 +blue*0.131)
                pixels[x,y]=(red,green,blue)
        img.save(image+"_sepia.png")
        self.ids.image.source = self.ids.image.source+"_sepia.png"

    def black_and_white(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                pixels[x, y] = (red, red, red)
        img.save(image + "_bw.png")
        self.ids.image.source = image+"_bw.png"

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