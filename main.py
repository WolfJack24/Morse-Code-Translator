# pylint: disable=import-error, missing-module-docstring, missing-function-docstring, missing-class-docstring
import json
from typing import Any
from customtkinter import CTk, CTkEntry, CTkComboBox, CTkButton


class Gui(CTk):
    def __init__(self):
        super().__init__()

        self.morse_code: None | Any = None

        self.title("Morse Code Translator")
        self.geometry("300x200")

        self.input_field = CTkEntry(
            self, width=136, height=26, corner_radius=3, border_width=1)
        self.input_field.place(x=82, y=41)

        self.combo_select = CTkComboBox(
            self, width=136, height=26, corner_radius=3,
            border_width=1, values=["To Text", "To Morse"])
        self.combo_select.set("To Text")
        self.combo_select.place(x=82, y=76)

        self.submit_button = CTkButton(
            self, width=136, height=26, corner_radius=3, text="Translate", command=self.translate)
        self.submit_button.place(x=82, y=111)

    def load_morse_code(self, morse_code: Any) -> None:
        self.morse_code = morse_code

    def translate(self) -> None:
        input_text = self.input_field.get()
        translate = self.combo_select.get()
        result = []

        if input_text == "":
            print("Input cannot be empty!")
        else:
            input_list: list[str] = input_text.split(" ")
            match translate:
                case "To Text":
                    text = self.morse_code["Text"]

                    for item in text:
                        if item in input_list:
                            result.append(text[item])

                case "To Morse":
                    morse = self.morse_code["Morse"]

                    for item in morse:
                        if item in input_list:
                            result.append(morse[item])

        print(f"Input: {input_text}")
        print(f"Translate to: {translate}")
        print(f"Result: {result}")
        print("---------------------------")


def main() -> None:
    app = Gui()

    try:
        with open("morsecode.json", "r", encoding="utf-8") as code:
            morse_code: Any = json.load(code)
    except OSError:
        print("Failed to open/find `morsecode.json`")
    finally:
        code.close()

    app.load_morse_code(morse_code)

    app.mainloop()


if __name__ == "__main__":
    main()
