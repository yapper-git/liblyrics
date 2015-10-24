from pyparsing import ParserElement, Suppress, Word, printables, nums

# Configuration and contants of pyparsing
ParserElement.setDefaultWhitespaceChars("")
COMMENT_SIGN, OPEN_HEAD, CLOSE_HEAD, EOL \
        = map(Suppress, "#[]\n")
allowed_chars = printables + " "
allowed_chars += " …éèêàâôœçÉÈÊÀÂÔŒÇ"  # French chars
WORDS   = Word(allowed_chars)
INTEGER = Word(nums)
INTEGER.setParseAction(lambda s, l, toks: int(toks[0]))
