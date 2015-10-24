from pyparsing import Literal, OneOrMore, Group
from liblyrics.common import OPEN_HEAD, INTEGER, CLOSE_HEAD, WORDS, EOL


class Section:
    type = None
    id = None
    content = []

    # Class attribute
    _parser = None

    @staticmethod
    def get_parser():
        """Return a section parser. @see grammar.md for the whole grammar."""
        if Section._parser is None:
            # Parser not yet defined. Defining it.
            head_type       = Literal("V") | Literal("C") | Literal("@")
            head            = OPEN_HEAD \
                    + head_type.setResultsName("type") \
                    + INTEGER.setResultsName("id") \
                    + CLOSE_HEAD + EOL
            content_line    = WORDS + EOL
            content         = OneOrMore(content_line)
            Section._parser = Group(head + content.setResultsName("content"))
        return Section._parser

    def _load_data_from_parsed(self, parsed):
        """Load self content from a parsed section."""
        self.type = parsed.type
        self.id = parsed.id
        self.content = [vers for vers in parsed.content]
        return self

    def get_lyrics(self):
        """Return content formatted in lyrics format."""
        res = ""
        res += "[" + self.type + str(self.id) + "]\n"
        res += "".join([line + "\n" for line in self.content])
        return res
