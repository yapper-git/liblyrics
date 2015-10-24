from pyparsing import ZeroOrMore, OneOrMore, Group
from liblyrics.common import COMMENT_SIGN, WORDS, EOL
from liblyrics.section import Section


class Lyrics:
    comments = []
    sections = []

    # Class attribute
    _parser = None

    @staticmethod
    def from_string(content):
        """Import a string content."""
        parsed = Lyrics.get_parser().parseString(content, parseAll=True)
        return Lyrics()._load_data_from_parsed(parsed)

    @staticmethod
    def from_file(path):
        """Import a file content.

        path  -- Path to the file from which content must be imported. The file
                 must exist and be readable."""
        parsed = Lyrics.get_parser().parseFile(path, parseAll=True)
        return Lyrics()._load_data_from_parsed(parsed)

    @staticmethod
    def get_parser():
        """Return a lyrics file parser. @see grammar.md for the whole grammar."""
        if Lyrics._parser is None:
            # Parser not yet defined. Defining it.
            comment_line   = COMMENT_SIGN + WORDS + EOL
            comments       = Group(ZeroOrMore(comment_line))
            section        = Section.get_parser()
            sections       = section + ZeroOrMore(EOL + section)
            Lyrics._parser = comments.setResultsName("comments") \
                    + sections.setResultsName("sections")

        return Lyrics._parser

    def _load_data_from_parsed(self, parsed):
        """Load self content from a parsed lyrics file."""
        self.comments = [line for line in parsed.comments]
        self.sections = [Section()._load_data_from_parsed(sec)
                for sec in parsed.sections]
        return self

    def get_lyrics(self):
        """Return content formatted in lyrics format."""
        res = ""
        res += "".join(["#" + line + "\n" for line in self.comments])
        res += "\n".join([sec.get_lyrics() for sec in self.sections])
        return res

    def save_into(self, lyricsname):
        """Save content into a .lyrics file.

        lyricsname: path to the file to write into. Must be writable."""
        with open(lyricsname, "w") as f:
            f.write(self.get_lyrics())
