from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("PhotoGallery.kb")

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]

images = ["space.jpg"]
index = 0
PhotoGalleryApp.run()