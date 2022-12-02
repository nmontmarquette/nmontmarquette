# Thought Technology - FlexComp Infiniti (2000-2009)

| Descriptions | Technologies |
|--------------|--------------|
| Conception et implémentation de micrologiciels. | <ul><li>C, Assembleur (Intel)</li><li>Microcontrôleurs Atmel, Intel, Qualcomm (SnapDragon)<li><li>Compilateur IAR</li></ul> |
| Conception d'un API pour Windows utilisant les technologies COM. | <ul><li>C++</li><li>Win32, COM, COM+</li><li>Pocket PC, Window CE, Palm OS</li></ul> |
| Conception et documentation d'un kit du développeur (SDK) incluant un guide de plus 120 pages. | <ul><li>Doxygen</li><li>C/C++</li><li>Win32, COM, COM+, .NET, VBA</li><li>National Instrument LabView</li><li>MatLab</li></ul> |
| Banc de test complet pour la production ainsi que débogage des unités produites. | <ul><li>C++</li><li>COM</li><li>National Instrument LabView</li></ul> |

---------------------------------------------------------------------------------------------------------------------

# Détaillé

Du côté du micrologiciel principal, il y avait aussi la fonctionnalité très attendue permettant à un usager de mettre le microgiciel à jour.(IAP (In-Application-Programmable). Pour ce genre d'équipement, à l'époque, ce n'était pas encore quelque chose de courant. J'avais moins de 4KB d'espace Flash puisque nous ne pouvions pas amputer d'avantage microgiciel principal. Plus précisément, je n'avais que 7 pages de 512 octets (une page étant réservée comme pseudo EEPROM) pour implémenter le code qui saurait lire un Compact Flash formaté en FAT32, le vérifier, effacer et reprogrammer une page à la fois (faute de RAM), implémenter un LFSR 16 bits et gérer les détails du pseudo EEPROM.

Notre interface USB maison représentait un certain défi d'optimisation. En effet, il n'y avait que peu de cycle disponible par transaction USB. Bien que ça augmentait le coût, j'ai dû suggérer une variante où la plupart des instructions prenaient 6 cycles machines plutôt que le 12 avec la version de base du microcontrôleur, nous permettant de descendre sous la barre des 100% avec une utilisation processeur de 95-98 %

Le travail impliquait aussi beaucoup d'outils et de code nécessaires aux testages et débogages des unités produites par notre département de production.

Finalement, pour permettre aux développeurs d'applications d'utiliser nos appareils, nous fournissions SDK complet permettant de communiquer avec tous nos appareils via un API unique. J'ai eu bonne implication dans le design ainsi que toute l'implémentation de l'API, de sa documentation et multiples exemples en différents langages. Je balançais donc entre le code micrologiciel et le code WIN32 sur une base régulière.

# Liens externes

Ci-bas, le modèle phare à l'époque de nos produits d'acquisition biomédicaux:

* https://thoughttechnology.com/flexcomp-system-with-biograph-infiniti-software-t7555m