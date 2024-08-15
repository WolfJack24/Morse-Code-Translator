# pylint: disable=import-error, missing-module-docstring, missing-function-docstring, missing-class-docstring
# Custom List Add-on Implementation by WolfJack24

import builtins


class List(list):
    def delisttify(self) -> str:
        string = ""
        if self:
            for item in self:
                string += f"{item} "
        return string


builtins.list = List
