from pyparsing import ParserElement, Suppress, Word, printables, nums

# Configuration and contants of pyparsing
ParserElement.setDefaultWhitespaceChars("")
COMMENT_SIGN, OPEN_HEAD, CLOSE_HEAD, EOL \
        = map(Suppress, "#[]\n")
allowed_chars = printables + " "
allowed_chars += " …’‘«»“”°–—ß"
allowed_chars += "àâäéèêëïîôöùûüçœ"
allowed_chars += "ÀÂÄÉÈÊËÏÎÔÖÙÛÜÇŒ"
allowed_chars += "{}×23"  # repeat chars
WORDS   = Word(allowed_chars)
INTEGER = Word(nums)
INTEGER.setParseAction(lambda s, l, toks: int(toks[0]))
