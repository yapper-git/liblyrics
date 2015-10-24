Grammaire utilisée dans le parseur lyrics
=========================================

Description de la grammaire utilisée par le parseur utilisé par la librairie
`liblyrics`.

Règles
------

File                 := Comments Sections

Comments             := CommentLine*
CommentLine          := '#' AuthorizedChars* '\n'

Sections             := Section+
Section              := SectionHeader SectionContent
SectionHeader        := '[' SectionType Number ']' '\n'
SectionType          := 'V' | 'C' | '@'
SectionContent       := AuthorizedChars+ '\n'

Number               := <any integer number>
AuthorizedCharacters := <any character that can be used into a human language,
                         including spaces, any type of carriage returns>
