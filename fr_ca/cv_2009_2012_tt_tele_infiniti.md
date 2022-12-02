# Thought Technology - Tele-Infiniti (2009-2012)

| Descriptions | Technologies |
|--------------|--------------|
| Conception de fonctionnalité sans fil Télé-Inifniti pour appareils d'acquisition existants. | <ul><li>Spécification matérielle de Bluetooth</li><li>Protocol USB bas-niveau (HCI)</li><li>Tranfert USB "bulk" et "Isochronous"</li><li>C/C++</li></ul> |
| Ajout de librairies et pilotes Windows à API et SDK | <ul><li>Déboguage de "kernel drivers"</li><li>Tranfert USB "bulk" et "Isochronous"</li><li>C++</li><li>Win32, Windows DDK, WDK (pilote)</li><li>Obtentient d'un certificat</li><li>Procédure de signature auprès de Microsoft</li></ul> |
| Conception de prototype d'applications et libraries pour plateforme mobiles. | <ul><li>C++, Ojective-C, Java</li><li>Android, iOS</li><li>Procédure de soumission d'application au App-Store d'Apple</li><li>Procédure de soumission matériel auprès d'Apple</li></ul> |
| Banc de test complet automatisé (avec brouilleur multibandes) pour instrumenter le débit ainsi que la fiabilité. | <ul><li>C++</li><li>COM</li><li>National Instrument LabView</li></ul> |

---------------------------------------------------------------------------------------------------------------------

## Détaillé

Le module 'Tele-Infiniti' était essentiellement un greffon sans fil (Bluetooth) pour notre gamme de produits d'acquisitions.

Nous avons contacté plusieurs manufacturiers, assemblé et testé de nombreux prototypes, au final qu'un seul module offrait le débit nécessaire en CLASS 1 (environ 100m).

Le micrologiciel principal ayant presque atteint son maximum (sans avoir à changer de microcontrôleur) ainsi que le peu de RAM, nous ne pouvions pas utiliser un "stack" Bluetooth existant. Nous devions utiliser la couche HCI directement, nous forçait donc à écrire notre propre pilote pour Windows puisque le pilote Bluetooth standard ne recevrait pas les échanges nécessaires.

Durant cette période, l'iPhone faisait son apparition, j'ai donc exploré et prototypé avec les plateformes Apple et Android.

Pour ce projet, spécifiquement, j'ai travaillé avec la NASA ainsi que la compagnie CSR (manufacturier de puces Bluetooth). La NASA, nous ayant commandé plusieurs systèmes d'acquisition. Durant leurs tests a été découvert un bogue très occasionnel sur lequel nous devions travailler. Ainsi, environ, une fois par 24 millions de paquets il y avait conflit entre deux récepteurs Bluetooth brisant trame causant des artefacts dans les données capturées.

## Liens externes

* https://thoughttechnology.com/tele-infiniti-compact-flash-t9600/
