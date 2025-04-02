import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class DiagnoseApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="Gib deine Symptome ein:")
        self.add_widget(self.label)

        self.symptom_input = TextInput(hint_text="z. B. Fieber, Husten")
        self.add_widget(self.symptom_input)

        self.button = Button(text="Diagnose abrufen")
        self.button.bind(on_press=self.get_diagnose)
        self.add_widget(self.button)

        self.result_label = Label(text="Warte auf Eingabe...")
        self.add_widget(self.result_label)

    def get_diagnose(self, instance):
        symptome = self.symptom_input.text
        url = f"http://127.0.0.1:8000/diagnose/{symptome}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.result_label.text = response.json()["diagnose"]
            else:
                self.result_label.text = "Fehler beim Abrufen"
        except Exception as e:
            self.result_label.text = f"Netzwerkfehler: {e}"

class MeineKivyApp(App):
    def build(self):
        return DiagnoseApp()

if __name__ == "__main__":
    MeineKivyApp().run()
