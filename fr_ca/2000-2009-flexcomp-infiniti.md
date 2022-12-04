# Thought Technology - FlexComp Infiniti (2000-2009)

| Tâches | Technologies |
|--------|--------------|
| <ul><li>Conception et implémentation de micrologiciels.</li><li>Conception d'un API pour Windows utilisant les technologies COM.</li><li>Conception et documentation d'un kit du développeur (SDK) incluant un guide de plus 120 pages.</li><li>Banc de test complet pour la production ainsi que débogage des unités produites.</li></ul> | <ul><li>C, Assembleur (Intel)</li><li>Microcontrôleurs Atmel, Intel, Qualcomm (SnapDragon)</li><li>Compilateur IAR</li><li>C++, Win32, COM, COM+, .NET, VBA (Windows)</li><li>Pocket PC, Windows CE, Palm OS</li><li>LabView (National Instrument)</li><li>MatLab (Mathworks)</li></ul> |

# Notes et détails

Notre interface USB maison représentait un certain défi d'optimisation. En effet, il n'y avait que peu de cycle disponible par transaction USB. Bien que ça augmentait le coût, j'ai dû suggérer une variante où la plupart des instructions prenaient 6 cycles machines plutôt que le 12 avec la version de base du microcontrôleur, nous permettant de descendre sous la barre des 100% avec une utilisation processeur de 95-98 %

Le travail impliquait aussi beaucoup d'outils et de code nécessaires aux testages et débogage des unités produites par notre département de production.

Finalement, pour permettre aux développeurs d'applications d'utiliser nos appareils, nous fournissions SDK complet permettant de communiquer avec tous nos appareils via un API unique. J'ai eu bonne implication dans le design ainsi que toute implémentation de l'API, de sa documentation et multiples exemples en différents langages. Je balançais donc entre le code micrologiciel et le code WIN32 sur une base régulière.

