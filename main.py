import requests
import json

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from navigation_screen_manager import NavigationScreenManager

Builder.load_file("home.kv")


class MyScreenManager(NavigationScreenManager):
    pass


class PayTonKawaApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


class HomeScreen(AnchorLayout):
    pass


class InscriptionForm(BoxLayout):

    def get_inputs(self):
        inputs =[]
        for child in self.children:
            if isinstance(child, kivy.uix.textinput.TextInput):
                print("Nom :", child.text)
                inputs.append(child.text)

        # inputs[0] - mot de passe
        # inputs[1] - email
        # inputs[2] - pseudo ou username
        # inputs[3] - prenom
        # inputs[4] - nom
        # data = {'name': inputs[4], 'username': inputs[3], 'firstname': inputs[2], 'email': inputs[1], 'mot_de_passe': inputs[0]}
        #json.dumps(data)
        #print(data)
        # TODO 4 : Envoyé ces informations à l'API - input contient les informations à envoyé


class Connexion(AnchorLayout):
    pass

'''class ProductDetails(BoxLayout):

    def on_enter(self):
        print("Entrée dans MonEcran2")

    def build(self):
        print("Hello world")
        screen = Builder.template("CustomScreen")  # Load the CustomScreen defined in my.kv
        box_layout = BoxLayout('horizontal')
        screen.ids.grid.add_widget(box_layout)  # Add the BoxLayout to the screen's grid layout
        return screen
'''
# class ProductDetails(BoxLayout):

class QRcode(BoxLayout):

    def authentification(self, app_manager):
        labels = []
        for child in self.children:
            box_layout = child
            children2 = box_layout.children
            for child2 in children2:
                if isinstance(child2, kivy.uix.label.Label):
                    labels.append(child2)
        print("Label text:", labels[2].text)  # Donné dans le qrcode
        # acces = json.loads(labels[2].text)
        # print(acces)

        if (True):
            app_manager.push("product_catalog_page")

        # TODO 5 : Reception du mdp pour validation et transition ecran produit catalog


# TODO 1 : Fonction Validation mdp et inscription
# TODO 2 : Fonction AR
# TODO 3 : Fonction Affichage des produits
#





PayTonKawaApp().run()

# url = "http://54.221.230.111:8000/api/products/"
# response = requests.get(url)
# data = json.loads(response.text)



# print(r.json())
url = "https://httpbin.org/get"
#myobj = { "name": input[4],"username": input[3],"firstname": input[2],"email": input[1],"mot_de_passe": input[0]}
#x = requests.post(url, myobj)

# response = requests.get(url)
# data = json.loads(response.text)
# print(data)

# Parcourir les données et afficher chaque donnée

