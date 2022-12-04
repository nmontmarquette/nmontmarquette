# Personnel - Émulateurs 65xx pour Uzebox (2020-2022)

| Tâches | Technologies |
|--------|--------------|
| <ul><li>Conception d'un émulateur 65xx initialement en C++17.</li><li>Générateur de "stub" d'instructions à partir des spécifications publiques (Python).</li><li>Refonte de l'émulateur 65xx en assembleur Atmel.</li><li>Émulateur partiels de machines utilisant le processeur 65xx (NES, VIC-20, C64, Apple 1).</li></ul> | <ul><li>C/C++, CMake, GDB</li><li>Python</li><li>Assembleur (Atmel)</li><li>Assembleur (MOS)</li><li>Github Actions</li></ul> |

# Notes et détails

Un ami à créer une [console retro-minimaliste](http://uzebox.org/index.php). Question d'y contribuer quelque chose, je me suis lancé le défi d'écrire un émulateur C64. La plateforme tourne sur un ATMega 8bit avec 4KB de RAM et 64KB de Flash.

C'est déjà un défi d'écrire un émulateur 65xx en assembleur, c'est un défi encore plus audacieux d'imaginer émuler un C64 au point de pouvoir y rouler certains exécutables. Le facteur le plus limitant étant le 4KB de RAM, ensuite le nombre de cycles disponibles par «scanline» dessiné. À l'instar du code sur Atari 2600, le programme à un budget limiter en cycles s'il veut représenter quoi que ce soit à l'écran.

Ma première version était tout en C++17, fort d'un visionnement [vidéo de Jason Turner](https://www.youtube.com/watch?v=EIKAqcLxtT0) j'avais tenté, d'implémenter qu'en C++. Malheureusement, au final, le code n'était pas assez compact ni suffisamment performant.

La seconde version quant à elle, tout assembleur Atmel, offre un gain de 300-400% sur la version C++. Cette version permet l’exécution du «kernal» et ROM Basic. Bien sûr j’ai dû y intégrer quelques optimisations spécifiques telles que les accès ROM (les plus fréquents), les accès à la page zéro ainsi qu’une table dédiée pour le décodage des instructions.

À moins d'avoir soit même fait un tel exercice de style, il est très difficile de mettre en mots la grande satisfaction de voir le code en ROM s'initialiser et ainsi de voir le curseur si familier clignoter sur son écran de télévision.

