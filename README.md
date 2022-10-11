Créez un générateur de mot de passe sécurisé. Pour cela, vous laisserez le choix à l'utilisateur sur : 
* La longueur du mot de passe >= 12
* S'il est composé de de ponctuation complexe ("%;,:/&@{[]}")
* S'il y a des chiffres
* Lettres majuscules et minuscule obligatoire
Pour vous aider : 
Vous aurez besoin d'importer les modules : 
- secrets
- string 
> import secrets
> import string
Pour le module string vous utiliserez : 
* ascii_letters
* digits
* punctuation
Pour secrets, la fonction choice : secrets.choice()
Regardez la documentation associée à ces deux modules pour vous aider. 
Essayez de rendre votre script le plus simple et pratique possible.
Vous pouvez le complexifier en le rendant le plus modulaire possible et laisser l'utilisateur choisir au 
maximum ce qu'il veut comme mot de passe. Un menu de choix par exemple...
