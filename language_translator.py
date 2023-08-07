import tkinter as tk
from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.source_language_label = tk.Label(root, text="Source Language:")
        self.source_language_label.pack()

        self.source_language_var = tk.StringVar()
        self.source_language_dropdown = tk.OptionMenu(root, self.source_language_var, *LANGUAGES.values())
        self.source_language_dropdown.pack()

        self.target_language_label = tk.Label(root, text="Target Language:")
        self.target_language_label.pack()

        self.target_language_var = tk.StringVar()
        self.target_language_dropdown = tk.OptionMenu(root, self.target_language_var, *LANGUAGES.values())
        self.target_language_dropdown.pack()

        self.source_text_label = tk.Label(root, text="Enter Text:")
        self.source_text_label.pack()

        self.source_text_entry = tk.Entry(root, width=50)
        self.source_text_entry.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.translated_text_label = tk.Label(root, text="Translated Text:")
        self.translated_text_label.pack()

        self.translated_text_area = tk.Text(root, height=10, width=50)
        self.translated_text_area.pack()

    def translate_text(self):
        source_language = self.source_language_var.get()
        target_language = self.target_language_var.get()
        source_text = self.source_text_entry.get()

        translation = self.translator.translate(source_text, src=source_language, dest=target_language)
        translated_text = translation.text

        self.translated_text_area.delete('1.0', tk.END)
        self.translated_text_area.insert(tk.END, translated_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
