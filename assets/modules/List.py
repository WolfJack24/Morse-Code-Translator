# pylint: disable=import-error, missing-module-docstring, missing-function-docstring, missing-class-docstring, C0103

# Custom List Add-on Implementation by WolfJack24

class List(list):
    def delisttify(self) -> str:
        string = ""
        if self:
            for item in self:
                string += f"{item} "
        return string
