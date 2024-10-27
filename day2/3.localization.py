"""
Localize a simple text-based interface for a shopping app,
translating its content from English into multiple languages
(e.g., Spanish, French, German, Chinese, etc.).
The content you will work on includes UI messages, error messages, and product descriptions.

The target localization files can be found in the data/locales folder.
Run this file to test the output of the localized messages.
"""

import json

class LocalizationManager:
    def __init__(self):
        self.translations = {}
        self.current_language = 'en'

    def load_language_file(self, language_code, file_path):
        with open(file_path, 'r') as f:
            self.translations[language_code] = json.load(f)

    def set_language(self, language_code):
        if language_code in self.translations:
            self.current_language = language_code
        else:
            raise ValueError(f"Language {language_code} not found")

    def get_translation(self, key, **kwargs):
        translation = self.translations[self.current_language].get(key, key)
        return translation.format(**kwargs)

    def print_all_selected(self):
        print("\n", f"Selected Language: {self.current_language}")
        print(self.get_translation("welcome_message", name="Alice"))
        print(self.get_translation("items_count", count=5))
        print(self.get_translation("empty_cart"))
        print(self.get_translation("discount", percent=10))
        print(self.get_translation("new_messages", count=1))
        print(self.get_translation("farewell"))

if __name__ == "__main__":
    print("Automated Localization[3]")

    manager = LocalizationManager()

    manager.load_language_file('en', 'data/locales/en.json')
    manager.load_language_file('es', 'data/locales/es.json')
    manager.load_language_file('sv', 'data/locales/sv.json')
    manager.load_language_file('zh', 'data/locales/zh.json')

    manager.set_language('en')
    manager.print_all_selected()

    manager.set_language('es')
    manager.print_all_selected()

    manager.set_language('sv')
    manager.print_all_selected()

    manager.set_language('zh')
    manager.print_all_selected()
