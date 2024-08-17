# pylint: disable=import-error, missing-module-docstring, missing-function-docstring, missing-class-docstring
from json import load as json_load
from sys import exit as sys_exit
from typing import Any
from customtkinter import (
    CTk,
    CTkEntry,
    CTkComboBox,
    CTkButton,
    CTkFont,
    FontManager,
    ThemeManager,
    set_default_color_theme as color_theme
)
from assets.modules.List import List


class Gui(CTk):
    def __init__(self):
        super().__init__()

        self.morse_code: None | Any = None
        self.source_code_pro: CTkFont = CTkFont("Source Code Pro", 14)

        self.title("Morse Code Translator")
        self.geometry("300x200")
        self.resizable(False, False)
        # self.iconbitmap("./assets/icons/icon.ico")

        self.input_field: CTkEntry = CTkEntry(
            self, width=136, height=26, corner_radius=3,
            border_width=1, font=self.source_code_pro)
        self.input_field.place(x=82, y=41)

        self.combo_select: CTkComboBox = CTkComboBox(
            self, width=136, height=26, corner_radius=3,
            border_width=1, font=self.source_code_pro,
            values=["To Morse", "To Text"])
        self.combo_select.set("To Morse")
        self.combo_select.place(x=82, y=76)

        self.submit_button: CTkButton = CTkButton(
            self, width=136, height=26, corner_radius=3,
            text="Translate", font=self.source_code_pro,
            command=self.translate)
        self.submit_button.place(x=82, y=111)

    def load_morse_code(self, morse_code: Any) -> None:
        self.morse_code = morse_code

    def translate(self) -> None:
        input_text: str = self.input_field.get()
        translate: str = self.combo_select.get()
        result: List = List()

        if input_text == "":
            print("Input cannot be empty!")
        else:
            if " " in input_text:
                input_list: list[str] = input_text.split(" ")
            else:
                input_list: list[str] = [input_text]

            match translate:
                case "To Morse":
                    morse: Any = self.morse_code["Morse"]

                    for word in input_list:
                        for char in word:
                            char = char.upper()
                            for item in morse:
                                if char != " " and char == item:
                                    result.append(morse[item])

                case "To Text":
                    text: Any = self.morse_code["Text"]

                    for _i, value in enumerate(input_list):
                        for item in text:
                            if item == value:
                                result.append(text[item])

        print(f"Input: {input_text}")
        print(f"Translate: {translate}")
        print(f"Result: {result.delisttify()}")
        print("---------------------------")


def main() -> None:
    if not FontManager.load_font("./assets/fonts/SourceCodePro-Medium.otf"):
        print("Font did not load!")
    ThemeManager.load_theme("./assets/theme/blue_in_hex.json")
    color_theme("./assets/theme/blue_in_hex.json")

    app: Gui = Gui()

    morse_code: Any | None = None
    morse_code_json: str = "./assets/json/morsecode.json"

    try:
        with open(morse_code_json, "r", encoding="utf-8") as code:
            morse_code = json_load(code)
            code.close()
    except OSError:
        print(f"Failed to open/find `{morse_code_json}`")
        sys_exit(1)

    if morse_code:
        app.load_morse_code(morse_code)

    app.mainloop()


if __name__ == "__main__":
    main()
