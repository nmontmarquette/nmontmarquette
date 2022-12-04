# Thought Technology - Tele-Infiniti (2009-2012)

| Tâches | Technologies |
|--------|--------------|
| <ul><li>Conception de fonctionnalité sans fil Tele-Infiniti pour appareils d'acquisition existants.</li><li>Conception de nouvelles librairies et pilotes pour Windows.</li><li>Conception de prototype d'applications et librairies pour plateformes mobiles.</li><li>Banc de test complet automatisé (avec brouilleur multibande) pour instrumenter le débit ainsi que la fiabilité.</li><li>Établir la procédure d'obtention d'un certificat officiel auprès de Microsoft et Apple.</li><li>Établir la procédure de signature de pilote auprès de Microsoft.</li><li>Établir la procédure de signature d'application auprès d'Apple.</li><li>Établir la procédure de soumission matériel auprès d'Apple.</li></ul> | <ul><li>C/C++, Objective-C, Java</li><li>Débogage de "kernel drivers (Windows)</li><li>Protocole USB bas-niveau (HCI)</li><li>Transfert USB "bulk" et "Isochronous"</li><li>Win32, Windows DDK, WDK (pilote)</li><li>Android, iOS</li></ul> |

# Notes et détails

Le module 'Tele-Infiniti' était essentiellement un greffon sans fil (Bluetooth) pour notre gamme de produits d'acquisitions.

Nous avons contacté plusieurs manufacturiers, assemblé et testé de nombreux prototypes, au final qu'un seul module offrait le débit nécessaire en CLASSA 1 (environ 100m).

Le micrologiciel principal ayant presque atteint son maximum (sans avoir à changer de microcontrôleur) ainsi que le peu de RAM, nous ne pouvions pas utiliser un "stack" Bluetooth existant. Nous devions utiliser la couche HCI directement, nous forçait donc à écrire notre propre pilote pour Windows puisque le pilote Bluetooth standard ne recevrait pas les échanges nécessaires.

Durant cette période, l'iPhone faisait son apparition, j'ai donc exploré et prototypé avec les plateformes Apple et Android.

Pour ce projet, spécifiquement, j'ai travaillé avec la NASA ainsi que la compagnie CSR (manufacturier de puces Bluetooth). La NASA, nous ayant commandé plusieurs systèmes d'acquisition. Durant leurs tests a été découvert un bogue très occasionnel sur lequel nous devions travailler. Ainsi, environ, une fois par 24 millions de paquets il y avait conflit entre deux récepteurs Bluetooth brisant trame causant des artefacts dans les données capturées.

