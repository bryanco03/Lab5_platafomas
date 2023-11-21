from PIL import Image
import cv2
import matplotlib.pyplot as plt


class Imagen:
    def __init__(self,filename,lib):
        self.filename = filename
        self.lib = lib


    def load_imagen_pil(self):
        with Image.open(self.filename) as img:
            img.load()
        return img

    def load_imagen_opencv(self):
        image = cv2.imread(self.filename)
        return image
    
    def show_imagen(self,imagen):
        if self.lib == "PIL" :
            imagen.show()
        elif self.lib == "Matplotlib":
            imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            plt.imshow(imagen_rgb)
            plt.axis('off')  
            plt.show()
        elif self.lib == "OpenCV" :
            cv2.imshow('img', imagen)
            cv2.waitKey(0)
        else:
            print("Error")