# Le format `.lyrics`

Le format de fichier `.lyrics` est destiné à stocker les paroles de cantiques ou
les vers de poèmes.

Un fichier `.lyrics` est divisé en plusieurs sections (au moins une). Les
sections sont séparées entre elles par un double retour à la ligne (voir plus
bas). Les sections sont ordonnées, selon l'ordre d'apparition dans le fichier.
Chaque section _doit_ posséder un en-tête de section, et _peut_, dans certains
cas _doit_ (voir plus bas) posséder un contenu.

Un fichier `.lyrics` _doit_ être encodé en UTF-8.


## Les commentaires

En début de fichier, il _peut_ y avoir un certain nombre de lignes, toutes
commençant par le symbole `#`. Ces lignes sont considérées comme des
commentaires et sont ignorées. Les lignes commentées _doivent_ commencer dès la
première ligne et être consécutives. Il _ne doit pas_ y avoir de ligne vide
entre la dernière ligne de commentaire et l'en-tête de la première section.



## L'en-tête de section

Un en-tête de section permet de décrire le type de la section. Il doit être
écrit sur une ligne seule (terminée par le caractères `\n`), et son contenu se
trouve entre les caractères `[` et `]`. Rien d'autre ne doit être présent sur
la ligne.

La première lettre décrit le type de section dont il s'agit. Cela _doit_ être
`V` pour une strophe (verse), `C` pour un refrain (chorus), et `@` pour l'appel
à un refrain.

+ Dans le cas d'une strophe, un numéro (entier positif) _peut_ suivre le
symbole `V`. Il indique le numéro de la strophe dans les paroles. Il _peut_
être omis, dans le cas où la strophe ne possède pas de numéro (par exemple, un
petit passage parlé en début ou en fin de cantique). S'il est donné, il _doit_
être unique dans le cantique. Les numéros indiqués _devraient_ suivre par ordre
incrémental, en commençant à 1.

+ Dans le cas d'un refrain, un numéro (entier positif) _peut_ également suivre
le symbole. L'omettre revient à préciser le numéro 1. Il ne possède aucun sens
dans les paroles, et ne sert qu'à distinguer les refrains entre eux. Ce numéro
_doit_ être unique dans tout le fichier. Les numéros _devraient_ se suivre par
ordre incrémental, en commençant à 1. Ils n'ont aucune relation avec les
numéros utilisés dans les strophes.

+ Dans le cas d'un appel à un refrain, une référence vers un refrain déjà écrit
_doit_ suivre le `@`. Cette référence est le caractère `C` suivi du numéro du
refrain appelé. Ne préciser aucun numéro revient à préciser le numéro 1.


## Le contenu de section

### Son format

Le contenu d'une section est une succession de lignes, terminées par le
caractères `\n`. Toutes les lignes _doivent_ contenir au moins un caractère.
Une ligne ne contenant aucun caractère indique la fin de la section et le début
de la suivante.

La dernière section _ne doit pas_ être suivie d'une ligne vide. Seul un `\n`
achevant la dernière ligne de la section est accepté, immédiatement suivi de la
fin du fichier.

Le contenu d'une section _devrait_ suivre des règles de syntaxe logique : pas
de doublement d'espaces blancs, pas d'espaces en début ou en fin de lignes… Ces
règles peuvent être étendues en fonction de la langue (par exemple, en
français, un espace insécable précède certains signes de ponctuation).


### Les répétitions

Le contenu de la section _peut_ (dans certains cas, _ne doit pas_, voir plus
bas) contenir des portions répétées (bis, ter…). Ces portions sont délimitées,
au début, par le caractère `{`, et à la fin, par les caractères et `}*`. Il _ne
doit pas_ y avoir d'espace, ni entre l'accolade ouvrante et le contenu, ni entre
le contenu et l'accolade fermante. Une portion répétée peut commencer et se
terminer à n'importe quel endroit de la section. Deux portions répétées
peuvent être emboîtées les unes dans les autres. Toutefois, elles _ne doivent
pas_ se chevaucher.

Un nombre _doit_ suivre les caractères `}*` marquant la fin d'une portion
répétée (sans espace séparateur). Ce nombre, soit 2 (pour bis), soit 3 (pour
ter), indique le nombre de fois que la portion doit être répétée.

Une portion marquée par `{` et `}`, où le `}` final n'est pas suivi d'un `*`
n'est pas une portion répétée. Cette séquence permet d'insérer des accolades
dans le texte.

Le texte pouvant suivre un appel à un refrain _ne doit pas_ contenir de portion
répétée.


### Sa présence

Dans le cas d'une strophe ou d'un refrain (symboles `V` ou `C`), le contenu de
la section _doit_ exister, c'est-à-dire qu'il _doit_ y avoir au moins une ligne
non-vide dans le contenu de la section.

Dans le cas d'un appel à un refrain (symbole `@`), le contenu _peut_ être
présent. S'il l'est, il s'agit d'un texte introductif, permettant de rappeler
au lecteur le refrain (le numéro du refrain _ne doit pas_ être visible pour le
lecteur, il s'agit uniquement d'une référence interne). Lors de l'affichage, le
logiciel utilisant le fichier _peut_ afficher ce texte d'introduction ou le
remplacer par le contenu du refrain appelé.


## Notes sur ce document

+ Ce document doit le moins possible être modifié. Il sert de référence à
l'utilisation du format `.lyrics`. Toutefois, il peut être amené à changer,
avec accord des auteurs et participants. Dans tous les cas, les modifications
devront s'efforcer à conserver la rétro-compatibilité, autant que cela est
possible.

+ Le mot _doit_ est utilisé à propos d'un caractère requis. Tout fichier valide
est sensé avoir ce caractère.

+ Le mot _peut_ indique un caractère optionnel. Un fichier a la possibilité
d'avoir ou de ne pas avoir le caractère décrit, sans que cela ne lève aucune
erreur d'interprétation.

+ Le mot _devrait_ indique un caractère attendu, mais ne gênant pas la
compréhension du document. Le caractère décrit est attendu, et des messages
d'alerte peuvent être donnés lors de la lecture d'un fichier ne le possédant
pas. Toutefois, si le caractère n'est pas comme décrit, la compréhension
globale du document n'en est pas détruite.
