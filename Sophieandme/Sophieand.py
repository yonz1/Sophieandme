import json
import sqlite3
import sys
import os
import argparse
import base64
from os import utime

con_i = sqlite3.connect("data_restored.db")
cur_i = con_i.cursor()

class util:
    def name(n):
        dico = L["fields"]
        for i in dico.keys():
            if int(n) == int(i):
                return dico[i]["value"]
        return "unkwnow"



L =  {
"userEmail": "bastienpelle223@gmail.com",
"fields": {
"23": {
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
},
"19": {
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
},
"11": {
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
},
"60": {
"id": "60",
"value": "EE",
"created_at": "2017-10-03 14:15:25",
"updated_at": "2017-10-03 14:15:25",
"deleted_at": "null",
"color": "duck",
"icon": "book"
},
"129": {
"id": "129",
"value": "electricit\u00e9",
"created_at": "2019-10-13 13:52:21",
"updated_at": "2019-10-13 13:52:21",
"deleted_at": "null",
"color": "duck",
"icon": "1"
}
},
"courses": {
"72": {
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"115": {
"id": "115",
"value": "Signaux",
"field_id": "23",
"created_at": "2017-08-21 12:25:59",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"117": {
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"112": {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"114": {
"id": "114",
"value": "Atomistique",
"field_id": "23",
"created_at": "2017-08-21 12:25:31",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"110": {
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"118": {
"id": "118",
"value": "Optique",
"field_id": "23",
"created_at": "2017-08-21 12:30:19",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"109": {
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"54": {
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
},
"256": {
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"55": {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
},
"498": {
"id": "498",
"value": "Analyse",
"field_id": "19",
"created_at": "2020-02-07 08:54:39",
"updated_at": "2020-02-07 08:54:39",
"deleted_at": "null",
"level_id": "6"
},
"496": {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
},
"53": {
"id": "53",
"value": "Alg\u00e8bre",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
},
"24": {
"id": "24",
"value": "Mod\u00e9lisation des liaisons",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"18": {
"id": "18",
"value": "Cin\u00e9matique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"33": {
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
},
"243": {
"id": "243",
"value": "Distribution d'\u00e9nergie",
"field_id": "60",
"created_at": "2017-10-23 14:06:51",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "10"
},
"306": {
"id": "306",
"value": "Stockage d'\u00e9nergie",
"field_id": "60",
"created_at": "2017-11-30 08:17:15",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "10"
},
"21": {
"id": "21",
"value": "Energ\u00e9tique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"147": {
"id": "147",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-09-14 10:20:37",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "6"
},
"151": {
"id": "151",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-14 10:22:40",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "7"
},
"50": {
"id": "50",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "7"
},
"48": {
"id": "48",
"value": "Machines",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"23": {
"id": "23",
"value": "Hacheur",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"435": {
"id": "435",
"value": "machines",
"field_id": "129",
"created_at": "2019-10-13 14:54:06",
"updated_at": "2019-10-13 14:54:06",
"deleted_at": "null",
"level_id": "28"
},
"438": {
"id": "438",
"value": "Sinuso\u00efdal",
"field_id": "129",
"created_at": "2019-10-13 14:54:51",
"updated_at": "2019-10-13 14:54:51",
"deleted_at": "null",
"level_id": "28"
},
"406": {
"id": "406",
"value": "Analogique",
"field_id": "11",
"created_at": "2018-02-04 15:16:07",
"updated_at": "2018-02-04 15:16:07",
"deleted_at": "null",
"level_id": "6"
},
"17": {
"id": "17",
"value": "Capteurs",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"25": {
"id": "25",
"value": "Num\u00e9rique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"16": {
"id": "16",
"value": "Automatique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
},
"31": {
"id": "31",
"value": "Statique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
},
"49": {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"155": {
"id": "155",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-15 10:21:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
},
"69": {
"id": "69",
"value": "Autre",
"field_id": "19",
"created_at": "2017-07-19 18:22:20",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}
},
"quizzs": {
"729": {
"id": "729",
"name": "Quizz 01 : Chapitre 0",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/729\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 615,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-06",
"questions": [{
"id": "729-2552",
"position": 0,
"duration": 30,
"question": {
"id": "2552",
"question": "Quelles sont les 7 unit\u00e9s de base du syst\u00e8me international ?",
"answer": "Le m\u00e8tre (m), la seconde (s), le kilogramme (kg), le kelvin (K), la mole (mol), l'amp\u00e8re (A) et le candela (cd).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2553",
"position": 1,
"duration": 60,
"question": {
"id": "2553",
"question": "Exprimer en unit\u00e9s de base du SI le newton (N), unit\u00e9 de force.",
"answer": "1 N = 1 kg.m.s$^{-2}$.\nOn peut par exemple utiliser la formule donnant le poids d'un objet de masse $m$ en pr\u00e9sence d'un champ de pesanteur d'acc\u00e9l\u00e9ration $g$ : $P = mg$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2554",
"position": 2,
"duration": 60,
"question": {
"id": "2554",
"question": "Exprimer en unit\u00e9 de base du SI le watt, unit\u00e9 de puissance.",
"answer": "1 W = 1kg.m$^2$.s$^{-3}$.\nOn peut par exemple utiliser le fait qu'une puissance est une \u00e9nergie divis\u00e9e par une dur\u00e9e, et la formule de l'\u00e9nergie cin\u00e9tique $E = \\frac12 m v^2$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "729-2555",
"position": 3,
"duration": 60,
"question": {
"id": "2555",
"question": "D\u00e9terminer par analyse dimensionnelle la hauteur atteinte par un projectile de masse $m$ lanc\u00e9 verticalement avec la vitesse $v$ dans un champ de pesanteur uniforme d'acc\u00e9l\u00e9ration $g$.",
"answer": "On cherche une hauteur $h$ en m\u00e8tre ($[h]$ =m), et les donn\u00e9es sont en $[m]$= kg, $v$ =m.s$^{-1}$ et $g$ = m.s$^{-2}$.\nA une constante multiplicative pr\u00e8s, on trouve $h = \\frac{v^2}{g}$. (la vraie formule est $h = \\frac{v^2}{2g}$ mais on ne peut d\u00e9terminer le facteur 2 par analyse dimensionnelle).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "729-2556",
"position": 4,
"duration": 120,
"question": {
"id": "2556",
"question": "D\u00e9terminer par analyse dimensionnelle la p\u00e9riode d'un pendule simple constitu\u00e9 d'un fil de longueur $L$ auquel on attache une masse $m$, dans un champ de pesanteur d'acc\u00e9l\u00e9ration $g$.",
"answer": "On cherche une p\u00e9riode $T$ telle que $[T]$ =s, et pour les donn\u00e9es $[L]$ = m, $[m]$ =kg et $[g]$ = m.s$^{-2}$.\nOn peut alors chercher \u00e0 exprimer $T = L^\\alpha m^\\beta g^\\gamma$, ce qui donne alors pour l'unit\u00e9 de $T$ : $[T] = m^{\\alpha+\\gamma} kg^\\beta s^{-2 \\gamma}$.\nOn a alors un syst\u00e8me de 3 \u00e9quations \u00e0 3 inconnues \u00e0 r\u00e9soudre, et on trouve $\\beta =0$, $\\gamma = -1\/2$ et $\\alpha=1\/2$.\nL'analyse dimensionnelle permet donc d'\u00e9crire que $T = \\sqrt{\\frac{L}{g}}$. (Cette formule n'est vraie qu'\u00e0 un facteur multiplicatif pr\u00e8s, le r\u00e9sultat r\u00e9el \u00e9tant $T = 2 \\pi \\sqrt{L\/g}$, mais le facteur 2 \\pi ne peut \u00eatre d\u00e9termin\u00e9 par analyse dimensionnelle.)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "729-2560",
"position": 5,
"duration": 20,
"question": {
"id": "2560",
"question": "Quelle est l'incertitude associ\u00e9e \u00e0 $c=a+b$, la somme de la grandeur $a$ d'incertitude $u(a)$ et de la grandeur $b$ d'incertitude $u(b)$ ?",
"answer": "$u(c) = \\sqrt{u(a)^2 + u(b)^2}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2561",
"position": 6,
"duration": 20,
"question": {
"id": "2561",
"question": "Quelle est l'incertitude relative associ\u00e9e \u00e0 $c = a \\times b$, le produit de la grandeur $a$ d'incertitude $u(a)$ et de la grandeur $b$ d'incertitude $u(b)$ ?",
"answer": "$\\frac{u(c)}{c} = \\sqrt{ \\left(\\frac{u(a)}{a} \\right)^2 + \\left(\\frac{u(b)}{b} \\right)^2}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2562",
"position": 7,
"duration": 90,
"question": {
"id": "2562",
"question": "Quelle est la valeur d'une r\u00e9sistance $R$ qui pr\u00e9sente une chute de tension $U = (2,45 \\pm 0,05)$ V \u00e0 ses bornes lorsqu'elle est parcourue par un courant $I = 125 \\pm 5)$ mA ?",
"answer": "On utilise d'abord la formule $R = \\frac{U}{I}$ pour d\u00e9terminer la meilleure estimation de cette r\u00e9sistance et on trouve $R = 19,6 \\ \\Omega$.\nOn utilise ensuite la formule de propagation des incertitudes dans le cas d'un produit et on trouve $\\frac{u(R)}{R} = \\sqrt{\\left(\\frac{u(U)}{U} \\right)^2 + \\left(\\frac{u(I)}{I} \\right)^2 } = 0.045$, donc une incertitude associ\u00e9e $u(R) = 0.9 \\ \\Omega$ en gardant un seul chiffre significatif pour l'incertitude.\n\nLe r\u00e9sultat demand\u00e9 est donc $R = (19,6 \\pm 0,9) \\ \\Omega$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "729-2563",
"position": 8,
"duration": 20,
"question": {
"id": "2563",
"question": "Donner le r\u00e9sultat de $l + L$ avec $l = 234$ cm et $L = 4,5$ m  en pr\u00e9cisant la r\u00e8gle utilis\u00e9e.",
"answer": "$l+ L$ = 6,8 m , car pour une somme, la grandeur avec la moins bonne pr\u00e9cision (ici $L$, pr\u00e9cise au d\u00e9cim\u00e8tre pr\u00e8s) fixe la pr\u00e9cision du r\u00e9sultat.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "729-2564",
"position": 9,
"duration": 20,
"question": {
"id": "2564",
"question": "Donner le r\u00e9sultat de $l \\times L$ avec $l$ = 57 cm et $L$ = 11,2 m, en pr\u00e9cisant la r\u00e8gle utilis\u00e9e.",
"answer": "$l \\times L$ = 6,4 m$^2$, car pour un produit, le nombre de chiffres significatifs du r\u00e9sultat est \u00e9gal \u00e0 celui des nombres utilis\u00e9s qui en a le moins (ici $l$ qui en a deux).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "729-2565",
"position": 10,
"duration": 15,
"question": {
"id": "2565",
"question": "Donner le nombre de chiffres significatifs de : \n 1013\n1,100\n0,0012\n 0,100",
"answer": "On trouve dans l'ordre 4, 4 , 2 et 3 chiffres significatifs.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2566",
"position": 11,
"duration": 20,
"question": {
"id": "2566",
"question": "Ecrire en notation scientifique :\n1200\n0,00107\n100000",
"answer": "1,200 . 10$^3$\n1,07 . 10$^{-3}$\n1,00000 . 10$^5$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-2567",
"position": 12,
"duration": 20,
"question": {
"id": "2567",
"question": "Convertir en m\u00e8tre :\n1,7 km\n37 cm\n0,17 \u00b5m\n589 nm",
"answer": "1,7 . 10$^3$ m\n0,37 m (ou 3,7 . 10$^{-1}$ m)\n1,7 . 10$^{-7}$ m\n5,89 . 10$^{-7}$ m",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "729-5928",
"position": 13,
"duration": 30,
"question": {
"id": "5928",
"question": "Quelle conclusion tirer d'une exp\u00e9rience de mesure d'indice optique de l'eau o\u00f9 l'on trouve $n = 1,32$ avec l'incertitude-type associ\u00e9e $u(n) = 0,06$ sachant que la valeur tabul\u00e9e est $n_{eau} = 1,333$ ?",
"answer": "On peut calculer le $z$-score associ\u00e9e \u00e0 la comparaison de ces deux valeurs $z = \\frac{n_{eau} - n}{u(n)} \\simeq 0,2$. On peut donc conclure \u00e0 un bon accord entre th\u00e9orie et exp\u00e9rience.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "729-5929",
"position": 14,
"duration": 30,
"question": {
"id": "5929",
"question": "Le compteur de vitesse \u00e0 aiguille d'une voiture indique 90 km\/h (avec des graduations de 5 km\/h). La mesure avec un radar indique 26,7 m\/s avec une pr\u00e9cision de 1 %. Les mesures sont-elles compatibles ?",
"answer": "La vitesse avec le compteur est $v_1 = 25,0$ m\/s avec son incertitude-type $u(v_1) = \\frac{5000\/3600}{\\sqrt{12}} \\simeq 0,4$. Celle mesur\u00e9e par le radar est $v_2 = 26,2$ et $u(v_2) = 0,01 v_2 = 0,3$ m\/s.\n\nLa compatibilit\u00e9 entre les deux mesures s'obtient avec le calcul du $z$-score associ\u00e9 $z = \\frac{v_2 -v_1}{\\sqrt(u(v_1)^2+u(v_2)^2)} \\simeq 3,4$. Les deux mesures ne sont pas compatibles.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 4
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"737": {
"id": "737",
"name": "Quizz 05 : Signal sinuso\u00efdal",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/737\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "115",
"value": "Signaux",
"field_id": "23",
"created_at": "2017-08-21 12:25:59",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-03",
"questions": [{
"id": "737-2574",
"position": 0,
"duration": 60,
"question": {
"id": "2574",
"question": "Quelle est la nature du signal transport\u00e9 par une onde acoustique ? \nDonner des ordres de grandeur de fr\u00e9quence pour le domaine audible, ainsi que de la vitesse du son dans l'air.",
"answer": "Le signal transport\u00e9 par une onde acoustique est une surpression du fluide dans lequel l'onde se propage (par exemple l'air).\nLe domaine audible correspond \u00e0 des fr\u00e9quences allant approximativement de 20 Hz \u00e0 20 kHz.\nLa vitesse du son dans l'air est de l'ordre de 340 m\/s.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "737-2575",
"position": 1,
"duration": 60,
"question": {
"id": "2575",
"question": "Quelle est la nature du signal transport\u00e9 par une onde \u00e9lectromagn\u00e9tique ?\nDonner un ordre de grandeur de fr\u00e9quence pour le domaine visible, ainsi que la vitesse de la lumi\u00e8re dans le vide.",
"answer": "Le signal transport\u00e9 par une onde \u00e9lectromagn\u00e9tique est un champ \u00e9lectromagn\u00e9tique.\nLe domaine visible correspond \u00e0 une fr\u00e9quence de l'ordre de 6 . 10$^{14}$ Hz (0,6 PHz).\nLa vitesse de la lumi\u00e8re dan le vide est environ \u00e9gale 3.10$^8$ m\/s.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "737-2576",
"position": 2,
"duration": 60,
"question": {
"id": "2576",
"question": "Donner l'\u00e9criture  g\u00e9n\u00e9rale d'un signal sinuso\u00efdal, et le nom de chacun des param\u00e8tres intervenant.",
"answer": "On peut \u00e9crire un signal sinuso\u00efdal $s(t)$ comme $s(t) = A \\cos (\\omega t + \\phi)$ avec :\n$A$ l'amplitude du signal,\n$\\omega$ sa pulsation,\n$\\phi$ la phase initiale. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "737-2577",
"position": 3,
"duration": 30,
"question": {
"id": "2577",
"question": "Quel est le lien entre p\u00e9riode $T$, fr\u00e9quence $f$ et pulsation $\\omega$ d'un signal sinuso\u00efdal ?",
"answer": "$f = \\frac{1}{T} = \\frac{\\omega}{2 \\pi}$\n$T = \\frac{1}{f} = \\frac{2 \\pi}{\\omega}$\n$\\omega = 2 \\pi f = \\frac{2 \\pi}{T}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "737-2578",
"position": 4,
"duration": 90,
"question": {
"id": "2578",
"question": "Donner la valeur de la fr\u00e9quence, de l'amplitude et de la phase initiale du signal suivant.",
"answer": "L'amplitude est de 3 A ; la fr\u00e9quence est de 0,4 Hz et la phase initiale vaut $- \\pi\/2$.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/63eca450-96e5-11e8-9bff-91800420ea59",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"772": {
"id": "772",
"name": "Quizz 07 : Transformations de la mati\u00e8re",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/772\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-17",
"questions": [{
"id": "772-2607",
"position": 0,
"duration": 30,
"question": {
"id": "2607",
"question": "Quelle est la d\u00e9finition d'un corps pur ?\nD'un corps simple ?",
"answer": "Un corps pur est un corps compos\u00e9 uniquement d'un seul type de mol\u00e9cules (par exemple l'eau).\nUn corps simple est un corps compos\u00e9 d'un seul \u00e9l\u00e9ment chimique (par exemple un m\u00e9lange d'ozone et de dioxyg\u00e8ne).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2608",
"position": 1,
"duration": 30,
"question": {
"id": "2608",
"question": "Quelle est la diff\u00e9rence entre transformation chimique et transformation nucl\u00e9aire ?",
"answer": "Lors d'une transformation chimique, seulement les structures \u00e9lectroniques des atomes sont chang\u00e9es : les \u00e9l\u00e9ments chimiques sont conserv\u00e9s.\nAu cours d'une transformation nucl\u00e9aire, les noyaux des atomes sont transform\u00e9s, il n'y a pas conservation des \u00e9l\u00e9ments chimiques.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2609",
"position": 2,
"duration": 30,
"question": {
"id": "2609",
"question": "Qu'est-ce qu'une transformation allotropique ?",
"answer": "Une transformation allotropique est une transformation physique o\u00f9 on observe un changement de la structure cristalline d'un corps pur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2610",
"position": 3,
"duration": 30,
"question": {
"id": "2610",
"question": "Quelle est la quantit\u00e9 de mati\u00e8re contenue dans 1,0 L d'eau ?\nM(O) = 16,0 g\/mol ; M(H) = 1,0 g\/mol",
"answer": "La masse d'un litre d'eau est $m = 1,0$ kg.\nLa masse molaire de l'eau est $M(H_2O) = 18,0$ g\/mol, on trouve donc une quantit\u00e9 de mati\u00e8re $n = \\frac{m}{M} = 56$ mol.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2611",
"position": 4,
"duration": 30,
"question": {
"id": "2611",
"question": "Quelle est la quantit\u00e9 de mati\u00e8re des ions pr\u00e9sents obtenus par dissolution de 0,3 mol de $CaCl_2$ dans 300 mL d'eau ?",
"answer": "On obtient 0,3 mol d'ions $Ca^{2+}$ et 0,6 mol d'ions $Cl^-$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2612",
"position": 5,
"duration": 30,
"question": {
"id": "2612",
"question": "Comment est d\u00e9finie la pression partielle d'un gaz ? Que vaut la pression partielle de l'atmosph\u00e8re en dioxyg\u00e8ne ?",
"answer": "Dans un m\u00e9lange de gaz \u00e0 la pression totale $P$, la pression partielle en l'esp\u00e8ce $i$ est $P_i = P x_i$ o\u00f9 $x_i = \\frac{n_i}{n}$ est la fraction molaire en l'esp\u00e8ce $i$ ($n_i$ est la quantit\u00e9 de mati\u00e8re de $i$ et $n$ la quantit\u00e9 de mati\u00e8re totale).\nDans l'atmosph\u00e8re, $P_{O_2} \\simeq 0,2$ bar.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2613",
"position": 6,
"duration": 30,
"question": {
"id": "2613",
"question": "Ecrire la r\u00e9action de combustion du m\u00e9thane $CH_4$ en pr\u00e9sence de dioxyg\u00e8ne formant de l'eau et du dioxyde de carbone.\nEcrire le tableau d'avancement de la combustion de 1,0 mol de m\u00e9thane en pr\u00e9sence de 0,5 mol de dioxyg\u00e8ne.\nQuel est le r\u00e9actif limitant ?",
"answer": "$CH_4 + 2O_2 = CO_2 + 2H_2O$\nLe dioxyg\u00e8ne est le r\u00e9actif limitant.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/7cffb410-955f-11e8-8f06-f9fae872b4af",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "772-2614",
"position": 7,
"duration": 30,
"question": {
"id": "2614",
"question": "Quelle est la concentration des ions en solution pour une solution d'acide chlorhydrique de titre massique $p=37 \\%$ et de densit\u00e9 1,19 ?\n$M(H)$ = 1,0 g\/mol et $M(Cl)$ = 35,5 g\/mol.",
"answer": "Consid\u00e9rons un volume $V = 1,0$ de cette solution.\nLa masse totale est donc $m = 1,19$ kg, dont une masse $m_{HCl} = p \\times m = 0,44$ kg.\n\nLa quantit\u00e9 de mati\u00e8re d'acide chlorhydrique est alors $n_{HCl} = \\frac{m_{HCl}}{M(HCl)} = 12$ mol.\n\nOn trouve alors pour concentration des ions $[H^+] = [Cl^-] = 12$ g\/mol. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "772-2615",
"position": 8,
"duration": 30,
"question": {
"id": "2615",
"question": "Ecrire le quotient de r\u00e9action pour la r\u00e9action $CH_3COOH_{(aq)} + H_2O = CH_3COO^-_{(aq)} + H_3O^+_{(aq)}$.",
"answer": "$Q = \\frac{[CH_3COO^-][H_3O^+]}{[CH_3COOH] c^0}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2616",
"position": 9,
"duration": 30,
"question": {
"id": "2616",
"question": "Ecrire le quotient de r\u00e9action pour la r\u00e9action $Al(OH)_{3(s)} = Al^{3+}_{(aq)} + 3 HO^-_{(aq)}$.",
"answer": "$Q = \\frac{[Al^{3+}][HO^-]^3}{(c^0)^4}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "772-2617",
"position": 10,
"duration": 30,
"question": {
"id": "2617",
"question": "Quelle est la concentration des ions en solution lorsque l'on dissout 34 g de nitrate d'argent ($AgNO_3$ formant les ions $Ag^+$ et $NO_3^-$) dans 250 mL d'eau ?\nOn ajoute 500 mL d'eau sal\u00e9e ($NaCl$) \u00e0 la concentration de 1,0 mol\/L. Les ions argent et les ions chlorure r\u00e9agissent totalement pour former du chlorure d'argent $AgCl$.\nFaire un tableau d'avancement et donner les concentrations de chaque ion apr\u00e8s m\u00e9lange.\nM(N) = 14,0 g\/mol ; M(O) = 16,0 g\/mol ; M(Ag) = 107,9 g\/mol",
"answer": "Il faut d'abord calculer la masse molaire du nitrate d'argent $M(AgNO_3) = 169,9$ g\/mol.\nIl y a donc une quantit\u00e9 de mati\u00e8re $n_{AgNO_3} = 34\/169,9 = 0,20$ mol, et on trouve donc comme concentrations des ions form\u00e9s $[Ag^+]=[NO_3^-] = 0,80$ mol\/L.\n\nIl y a dans l'eau sal\u00e9e une quantit\u00e9 de mati\u00e8re d'ions chlorure $n_{Cl^-} = 0,50$ mol,ce seront donc les ions argent qui seront le r\u00e9actif limitant (voir le tableau d'avancement).\nOn trouve ensuite les concentrations en divisant par le volume total (de 750 mL, attention !) et on trouve\n$[Ag^+] \\simeq 0$ ; $[Cl^-] = \\frac{0,30 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,40$ mol\/L ; $[NO_3^-] = \\frac{0,20 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,27$ mol\/L et $[Na^+] = \\frac{0,50 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,67$ mol\/L. ",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a8aaa9f0-962b-11e8-bdd6-872b1e76e3ac",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "772-2618",
"position": 11,
"duration": 30,
"question": {
"id": "2618",
"question": "Ecrire le quotient de r\u00e9action de la r\u00e9action de pr\u00e9cipitation du chlorure d'argent (les r\u00e9actifs sont les ions $Ag^+$ et les ions $Cl^-$).",
"answer": "La r\u00e9action \u00e9tudi\u00e9e est $Ag^+_{(aq)} + Cl^-_{(aq)} = AgCl_{(s)}$ donc on trouve le quotient de r\u00e9action :\n$$ Q = \\frac{(c^0)^2}{[Ag^+][Cl^-]} .$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"778": {
"id": "778",
"name": "Quizz 09 : Mod\u00e8le de Th\u00e9venin, ponts diviseurs. Structure atomique",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/778\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "114",
"value": "Atomistique",
"field_id": "23",
"created_at": "2017-08-21 12:25:31",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 420,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-28",
"questions": [{
"id": "778-2621",
"position": 0,
"duration": 30,
"question": {
"id": "2621",
"question": "Enoncer les lois de Kirschhoff.",
"answer": "Loi des n\u0153uds : la somme des courants entrants dans un n\u0153ud est \u00e9gale \u00e0 la somme des courants sortants.\nLoi des mailles : la somme de toutes les tensions le long d'une maille est nulle.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2623",
"position": 1,
"duration": 30,
"question": {
"id": "2623",
"question": "Quand deux dip\u00f4les sont ils mont\u00e9s en s\u00e9rie ?",
"answer": "Ils sont en s\u00e9rie quand ils sont travers\u00e9s par le m\u00eame courant.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2624",
"position": 2,
"duration": 30,
"question": {
"id": "2624",
"question": "Quand deux dip\u00f4les sont-ils mont\u00e9s en parall\u00e8le ?",
"answer": "Ils sont en parall\u00e8le quand il ont la m\u00eame tension \u00e0 leurs bornes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2625",
"position": 3,
"duration": 30,
"question": {
"id": "2625",
"question": "D\u00e9montrer la formule donnant la r\u00e9sistance \u00e9quivalente \u00e0 $n$ r\u00e9sistances en s\u00e9rie.",
"answer": "Puisque les $n$ r\u00e9sistances sont en s\u00e9rie, elles sont travers\u00e9es par le m\u00eame courant $I$. Chaque r\u00e9sistance $R_i$ pr\u00e9sente une tension $U_i =R_i I$, en cons\u00e9quent, le montage pr\u00e9sente une tension $U = \\sum_i U_i = (\\sum_i R_i) I$ \u00e0 ses bornes.\nCette tension est proportionnelle au courant, donc le montage est \u00e9quivalent \u00e0 une r\u00e9sistance, de r\u00e9sistance \u00e9quivalente $R = \\sum_i R_i$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2626",
"position": 4,
"duration": 30,
"question": {
"id": "2626",
"question": "D\u00e9montrer la formule donnant la r\u00e9sistance \u00e9quivalente \u00e0 $n$ r\u00e9sistances en parall\u00e8le.",
"answer": "Puisque les $n$ r\u00e9sistances sont en parall\u00e8le, elles ont la m\u00eame tension \u00e0 leurs bornes $U$. Chaque r\u00e9sistance $R_j$ est alors travers\u00e9e par un courant $I_j =U\/R_j $, en cons\u00e9quent, le montage est travers\u00e9 par un courant $I = \\sum_j I_j = (\\sum_j 1\/R_j) U$ \u00e0 ses bornes.\nCe courant est proportionnel \u00e0 la tension, donc le montage est \u00e9quivalent \u00e0 une r\u00e9sistance, de r\u00e9sistance \u00e9quivalente $R$ telle que $\\frac1R = \\sum_i \\frac{1}{R_i}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "778-2628",
"position": 5,
"duration": 30,
"question": {
"id": "2628",
"question": "Quelle est la puissance \u00e9lectrique re\u00e7ue par un dip\u00f4le en convention r\u00e9cepteur ?",
"answer": "$P = U I$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2629",
"position": 6,
"duration": 30,
"question": {
"id": "2629",
"question": "Quelle est la puissance \u00e9lectrique fournie par un dip\u00f4le en convention r\u00e9cepteur ?",
"answer": "$P = - U I$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2631",
"position": 7,
"duration": 30,
"question": {
"id": "2631",
"question": "Qu'est-ce que le mod\u00e8le de Th\u00e9venin pour un g\u00e9n\u00e9rateur ?",
"answer": "Un g\u00e9n\u00e9rateur r\u00e9el peut \u00eatre mod\u00e9lis\u00e9 par un g\u00e9n\u00e9rateur de Th\u00e9venin, qui est l'association en s\u00e9rie d'une source de tension id\u00e9ale et d'une r\u00e9sistance interne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2632",
"position": 8,
"duration": 30,
"question": {
"id": "2632",
"question": "Qu'est-ce qu'un pont diviseur de tension ?\nD\u00e9montrer la formule du pont diviseur de tension.",
"answer": "Un pont diviseur de tension est l'association de deux r\u00e9sistances en s\u00e9rie.\nSi le pont diviseur de tension est constitu\u00e9 des deux r\u00e9sistances $R_1$ et $R_2$ et est soumis \u00e0 une tension $U$, alors le courant qui traverse les deux r\u00e9sistances est $I = \\frac{U}{R_1+R_2}$, et la tension aux bornes de la r\u00e9sistance $R_2$ est :\n$$ U_2 = \\frac{R_2}{R_1+R_2} U $$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "778-2633",
"position": 9,
"duration": 30,
"question": {
"id": "2633",
"question": "Qu'est-ce qu'un pont diviseur de courant ?\nD\u00e9montrer la formule du pont diviseur de courant.",
"answer": "Un pont diviseur de courant est l'association de deux r\u00e9sistances en parall\u00e8le.\nSi le pont diviseur de courant est constitu\u00e9 des deux r\u00e9sistances $R_1$ et $R_2$ et est travers\u00e9 par un courant $I$, alors la tension aux bornes des deux r\u00e9sistances est $U = \\frac{R_1R_2}{R_1+R_2} I$, et le courant qui traverse la r\u00e9sistance $R_2$ est :\n$$ I_2 = \\frac{R_1}{R_1+R_2} I $$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "778-2634",
"position": 10,
"duration": 30,
"question": {
"id": "2634",
"question": "De quelles particules \u00e9l\u00e9mentaires est compos\u00e9 un atome et comment sont-elles r\u00e9parties ?",
"answer": "Un atome est compos\u00e9 de protons, de neutrons et d'\u00e9lectrons. Les protons et les neutrons sont dans le noyau, autour duquel gravitent les \u00e9lectrons (dispos\u00e9 sur des couches \u00e9lectroniques).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2635",
"position": 11,
"duration": 30,
"question": {
"id": "2635",
"question": "Que se passe t'il lorsque un \u00e9lectron change d'orbite, faisant passer un atome d'un \u00e9tat excit\u00e9 \u00e0 un \u00e9tat d\u00e9sexcit\u00e9 ?",
"answer": "Lors de la d\u00e9sexcitation d'un atome il y a \u00e9mission d'un photon.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2636",
"position": 12,
"duration": 30,
"question": {
"id": "2636",
"question": "Que se passe t'il lorsqu'un atome absorbe un photon ?",
"answer": "L'atome atteint un \u00e9tat d'\u00e9nergie sup\u00e9rieur (il est excit\u00e9), obtenu par le changement d'orbite d'un \u00e9lectron.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "778-2637",
"position": 13,
"duration": 30,
"question": {
"id": "2637",
"question": "Lorsqu'un photon est \u00e9mis ou absorb\u00e9 par un atome, quel est le lien entre sa longueur d'onde et les \u00e9tats d'\u00e9nergie de l'atome ?",
"answer": "Lors de l'\u00e9mission ou de l'absorption d'un photon, l'atome passe d'un \u00e9tat d'\u00e9nergie $E_n$ \u00e0 un \u00e9tat d'\u00e9nergie $E_m$. La longueur d'onde du photon $\\lambda$ est telle que $\\frac{hc}{\\lambda} = |E_n -E_m|$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"820": {
"id": "820",
"name": "Quizz 21 : Cin\u00e9matique. M\u00e9canique newtonienne.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/820\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 270,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-23",
"questions": [{
"id": "820-2708",
"position": 0,
"duration": 30,
"question": {
"id": "2708",
"question": "Exprimer le vecteur-position, le vecteur-vitesse et le vecteur-acc\u00e9l\u00e9ration d'un point en coordonn\u00e9es cylindriques.",
"answer": "$\\vec{OM} = r \\vec{u}_r + z \\vec{u}_z$\n$\\vec{v} = \\dot{r} \\vec{u}_r + r \\dot{\\theta} \\vec{u}_{\\theta} + \\dot{z} \\vec{u}_z$\n$\\vec{a} = \\left(\\ddot{r} - r\\dot{\\theta}^2 \\right) \\vec{u}_r + \\left( r \\ddot{\\theta} + 2 \\dot{r} \\dot{\\theta} \\right) \\vec{u}_\\theta + \\ddot{z} \\vec{u}_z$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "820-2709",
"position": 1,
"duration": 30,
"question": {
"id": "2709",
"question": "A un instant $t$, un point mat\u00e9riel a une vitesse $\\vec{v}$ et une acc\u00e9l\u00e9ration $\\vec{a}$, que l'on d\u00e9compose en une partie parall\u00e8le \u00e0 la vitesse, et une partie perpendiculaire : $\\vec{a} = a_{\/\/} \\vec{u}_{\/\/} + a_{\\perp} \\vec{u}_{\\perp}$.\nQuel est l'effet sur le vecteur-vitesse de chacune de ces composantes ?",
"answer": "La composante parall\u00e8le a pour effet de modifier la norme du vecteur-vitesse, la composante perpendiculaire modifie sa direction.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "820-2711",
"position": 2,
"duration": 30,
"question": {
"id": "2711",
"question": "Quelle doit-\u00eatre la longueur du bras d'une centrifugeuse telle que l'acc\u00e9l\u00e9ration subie par l'astronaute soit de 18 $g$ quand la cabine a une vitesse de 60 m\/s ?",
"answer": "On prend comme syst\u00e8me la cabine, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre muni d'un syst\u00e8me de coordonn\u00e9es cylindriques, l'axe $z$ \u00e9tant l'axe de rotation du bras, de longueur $L$, et l'origine du rep\u00e8re tel que la c\u00f4te $z$ de la cabine soit nulle.\n\nLa position de la cabine est alors $\\vec{OM} = L \\vec{u}_r$. En d\u00e9rivant une premi\u00e8re fois on trouve le vecteur-vitesse de la cabine $\\vec{v} = L \\dot{\\theta} \\vec{u}_\\theta$ (car $\\dot{L} =0$). On en d\u00e9duit que $\\dot{\\theta} = cte$ puisque $v$ et $L$ sont constants et en d\u00e9rivant une seconde fois, on a le vecteur-acc\u00e9l\u00e9ration $\\vec{a} = - L \\dot{\\theta}^2 \\vec{u}_r$.\n\nEn norme, on obtient alors $v = L \\dot{\\theta}$ et $a = L \\dot{\\theta}^2 = \\frac{v^2}{L}$.\nOn d\u00e9duit donc la longueur du bras recherch\u00e9e $L = \\frac{v^2}{a} = 20$ m.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "820-2712",
"position": 3,
"duration": 30,
"question": {
"id": "2712",
"question": "Quel est le temps de chute et la distance horizontale parcourue par un objet l\u00e2ch\u00e9 depuis une altitude de 100 km avec une vitesse initiale verticale de 800 m\/s et une vitesse horizontale de 1,7 km\/s.",
"answer": "On prend comme syst\u00e8me l'objet \u00e9tudi\u00e9, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre avec les coordonn\u00e9es cart\u00e9siennes, l'axe $z$ vertical vers le haut, et l'axe $x$ horizontal dirig\u00e9 le long de la vitesse horizontale lors du l\u00e2cher. L'origine des temps est fix\u00e9e au l\u00e2cher.\n\nOn a alors $\\vec{a} (t) = - g \\vec{u}_z$, mais on ne sait pas calculer directement avec les vecteurs. On projette donc sur chacun des axes, et on obtient les trois \u00e9quations $\\ddot{x} = \\ddot{y} = 0$ et $\\ddot{z} = -g$.\nOn int\u00e8gre deux fois ces trois relations et on trouve $y(t) =0$ , $x(t) = v_h t$ et $z(t) = - \\frac{1}{2} g t^2 + v_v (t) + h_0$.\nLe temps de vol s'obtient en d\u00e9terminant le temps au bout duquel $z(t_v) = 0$, on trouve alors les deux possibilit\u00e9s $t_{1\/2} = \\frac{v_v \\pm \\sqrt{v_v^2 + 2 g h_0}}{g}$, dont on ne retient que la positive $t_v =  \\frac{v_v + \\sqrt{v_v^2 + 2 g h_0}}{g} = 2,0$ min.\nL'objet tombera donc $x(t_v) = 4,1.10^5$ m (environ 400 km) plus loin que le point o\u00f9 il a \u00e9t\u00e9 l\u00e2ch\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "820-2713",
"position": 4,
"duration": 30,
"question": {
"id": "2713",
"question": "Quelles sont les 4 interactions fondamentales ? Quelles sont leurs port\u00e9es ?",
"answer": "Il y a :\n- l'interaction gravitationnelle de port\u00e9e infinie ;\n- l'interaction \u00e9lectromagn\u00e9tique, de port\u00e9e infinie \u00e9galement ;\n- l'interaction faible, de port\u00e9e limit\u00e9e au noyau des atomes ;\n- l'interaction (nucl\u00e9aire) forte, de port\u00e9e limit\u00e9e au noyau.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "820-2714",
"position": 5,
"duration": 30,
"question": {
"id": "2714",
"question": "Qu'est-ce que la pouss\u00e9e d'Archim\u00e8de ? Comment la calcule t'on ?",
"answer": "La pouss\u00e9e d'Archim\u00e8de est une force due aux diff\u00e9rences de pression d'un fluide caus\u00e9es par la gravit\u00e9.\nCette force est dirig\u00e9e vers le haut, et est d'intensit\u00e9 \u00e9gale au poids du volume de fluide d\u00e9plac\u00e9 : pour un solide dont le volume immerg\u00e9 est $V$ dans un fluide de masse volumique $\\rho$ et dans un champ d epesenteur d'acc\u00e9l\u00e9ration $\\vec{g}$, la pouss\u00e9e d'Archim\u00e8de s'\u00e9crit $\\vec{P}_A = - \\rho V \\vec{g}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "820-2716",
"position": 6,
"duration": 30,
"question": {
"id": "2716",
"question": "Lors de frottements entre deux solides, quelle est la relation math\u00e9matique entre la composante tangentielle \u00e0 la surface de contact $T$ et la composante normale $N$ de la force exerc\u00e9e en cas de glissement ? En cas de non-glissement ?",
"answer": "Si on appelle $\\mu$ le coefficient de frottement, en cas de glissement $T = \\mu N$, en cas de non-glissement $T \\leq \\mu N$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "820-2721",
"position": 7,
"duration": 30,
"question": {
"id": "2721",
"question": "Pour un solide se d\u00e9pla\u00e7ant \u00e0 la vitesse $\\vec{v}$ dans un fluide, donner l'expression de la force exerc\u00e9e par le fluide dans le cas de frottements de type fluide visqueux et dans le cas d(un \u00e9coulement turbulent.",
"answer": "Fluide visqueux : $\\vec{F} = - \\alpha \\vec{v}$\nEcoulement turbulent : $\\vec{F} = - \\beta v \\vec{v}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "820-2725",
"position": 8,
"duration": 30,
"question": {
"id": "2725",
"question": "Comment d\u00e9finit-on un r\u00e9f\u00e9rentiel galil\u00e9en ?\nSi on vous donne un r\u00e9f\u00e9rentiel galil\u00e9en $\\mathcal{R}$, \u00e0 quelle condition un r\u00e9f\u00e9rentiel $\\mathcal{R'}$ peut-il \u00eatre consid\u00e9r\u00e9 comme galil\u00e9en ?",
"answer": "Un r\u00e9f\u00e9rentiel galil\u00e9en est un r\u00e9f\u00e9rentiel dans lequel un syst\u00e8me isol\u00e9 (ou pseudo-isol\u00e9) a un mouvement de translation rectiligne uniforme.\n\n$\\mathcal{R'}$ sera galil\u00e9en si et seulement s'il est en translation rectiligne uniforme par rapport \u00e0 $\\mathcal{R}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"809": {
"id": "809",
"name": "Quizz 18 : R\u00e9sonance.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/809\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2025-01-16",
"questions": [{
"id": "809-2686",
"position": 0,
"duration": 30,
"question": {
"id": "2686",
"question": "Quelle est la grandeur complexe $\\underline{u} (t)$ associ\u00e9e \u00e0 la grandeur r\u00e9elle $u(t) = U \\cos (\\omega t + \\phi)$ ?",
"answer": "Il s'agit de $\\underline{u} (t) = \\underline{U_0} e^{j \\omega t}$, avec $\\underline{U_0} = U e^{j \\phi}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "809-2687",
"position": 1,
"duration": 30,
"question": {
"id": "2687",
"question": "Quelle est la d\u00e9finition de l'imp\u00e9dance complexe d'un dip\u00f4le ?\nQue vaut-elle \u00e0 la pulsation $\\omega$ pour une r\u00e9sistance $R$? un condensateur de capacit\u00e9 $C$ ? une bobine d'inductance $L$ ?",
"answer": "L'imp\u00e9dance est la rapport de la tension complexe aux bornes du dip\u00f4le par l'intensit\u00e9 complexe du courant qui le traverse : $\\underline{Z} = \\frac{\\underline{U}}{\\underline{I}}$.\n\nPour la r\u00e9sistance, $\\underline{Z}(\\omega) = R$, pour un condensateur $\\underline{Z}(\\omega) = \\frac{1}{jC\\omega}$ et pour la bobine $\\underline{Z} (\\omega) = j L \\omega$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "809-2689",
"position": 2,
"duration": 30,
"question": {
"id": "2689",
"question": "Trouver l'amplitude des oscillations d'un oscillateur amorti soumis \u00e0 une excitation sinuso\u00efdale, ob\u00e9issant \u00e0 l'\u00e9quation diff\u00e9rentielle $\\frac{d^2x}{dt^2} + \\frac{\\omega_0}{Q} \\frac{dx}{dt} + \\omega_0^2 x = \\omega_0^2 x_m \\cos(\\omega t)$.",
"answer": "On introduit la notation complexe $\\underline{x} (t) = \\underline{X} e^{j\\omega t}$, alors l'\u00e9quation diff\u00e9rentielle devient pour $\\underline{x}$ :\n$$ (- \\omega^2 + j \\frac{\\omega \\omega_0}{Q} + \\omega_0^2) \\underline{x} = \\omega_0^2 x_m e^{j \\omega t} $$\n\net donc on obtient $\\underline{X} = x_m \\frac{\\omega_0^2}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q}$.\n\nL'amplitude des oscillations $X$ est alors $X = \\vert \\underline{X} \\vert$ donc\n$$ X = x_m \\frac{\\omega_0^2}{\\sqrt{(\\omega^2 - \\omega_0^2)^2 + \\frac{\\omega^2 \\omega_0^2}{Q^2}}} = \\frac{x_m}{\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}}$$.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "809-2690",
"position": 3,
"duration": 30,
"question": {
"id": "2690",
"question": "L'amplitude des oscillations d'un oscillateur amorti de pulsation propre $\\omega_0$ et de facteur de qualit\u00e9 $Q$, soumis \u00e0 une excitation de pulsation $\\omega$ est donn\u00e9e par $ X(\\omega) = \\frac{x_m}{\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}}$.\nA quelle condition sur $Q$ observera t'on une r\u00e9sonance ? Que vaut alors la pulsation de r\u00e9sonance ?\n",
"answer": "On cherche \u00e0 d\u00e9terminer si $X(\\omega)$ pr\u00e9sente un maximum pour $\\omega>0$. Ce sera le cas si $\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}$ pr\u00e9sente un minimum, donc si $f(\\omega) = \\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2$ pr\u00e9sente un minimum.\nPosons le polyn\u00f4me du second degr\u00e9 $P(x) = (1-x)^2 + \\frac{x}{Q^2} = x^2 + \\left(\\frac{1}{Q^2}-2 \\right) x +1$ tel que $f(\\omega) = P(\\frac{\\omega^2}{\\omega_0^2})$.\nIl faut donc d\u00e9terminer si $P(x)$ admet un minimum pour $x>0$.\nLe minimum de $P$ est atteint pour $\\frac{-\\left(\\frac{1}{Q^2}-2 \\right)}{2}$, donc il y aura bien r\u00e9sonance si $\\left(\\frac{1}{Q^2}-2 \\right)<0$, donc si $Q>\\frac{1}{\\sqrt{2}}$.\n\nLe minimum de $P$ est alors atteint en $x = 1 - \\frac{1}{2Q^2}$, donc le minimum de $f(\\omega)$ est atteint pour $\\omega_r$ tel que $\\left(\\frac{\\omega_r}{\\omega_0} \\right)^2 = 1 - \\frac{1}{2Q^2}$, donc la pulsation de r\u00e9sonance est :\n$$ \\omega_r = \\omega_0 \\sqrt{1- \\frac{1}{2Q^2}} $$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "809-2691",
"position": 4,
"duration": 30,
"question": {
"id": "2691",
"question": "L'amplitude complexe des oscillations d'un oscillateur amorti de pulsation propre $\\omega_0$ et de facteur de qualit\u00e9 $Q$, soumis \u00e0 une excitation de pulsation $\\omega$ est donn\u00e9e par $\\underline{X} = x_m \\frac{\\omega_0^2}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q}$.\nMontrer que l'amplitude complexe des oscillations de la vitesse s'exprime sous la forme :\n$$ \\underline{v_0} = \\frac{Q \\omega_0 x_m}{1 + j Q \\left( \\frac{\\omega}{\\omega_0} - \\frac{\\omega_0}{\\omega} \\right)^2} .$$\n\nA quelle condition sur $Q$ observera t'on une r\u00e9sonance ? A quelle pulsation ?",
"answer": "On sait que la vitesse est la d\u00e9riv\u00e9e de la position, $v = \\frac{dx}{dt}$, donc avec les notations complexes, $\\underline{v} = j \\omega \\underline{x}$, et donc $$\\underline{v_0} = j \\omega \\underline{X} =  \\frac{j \\omega \\omega_0^2 x_m}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q} $$\nOn divise alors num\u00e9rateur et d\u00e9nominateur par $j \\omega \\omega_0\/Q$ pour trouver le r\u00e9sultat demand\u00e9.\n\nOn aura alors r\u00e9sonance si $\\vert \\underline{v_0} \\vert = \\frac{Q \\omega_0 x_m}{\\sqrt{1 +  Q^2 \\left( \\frac{\\omega}{\\omega_0} - \\frac{\\omega_0}{\\omega} \\right)^4}}$ pr\u00e9sente un maximum. C'est toujours le cas, quelque soit la valeur de $Q$, et la pulsation de r\u00e9sonance est $\\omega_r = \\omega_0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "809-2692",
"position": 5,
"duration": 30,
"question": {
"id": "2692",
"question": "Quelle est la d\u00e9finition de la bande passante ? Que vaut-elle en fonction de $\\omega_0$ et $Q$ ?",
"answer": "La bande passante est l'intervalle de pulsations (ou de fr\u00e9quences) pour lesquelles l'amplitude des oscillations entretenues est sup\u00e9rieure ou \u00e9gale \u00e0 l'amplitude des oscillations \u00e0 la r\u00e9sonance divis\u00e9 par $\\sqrt{2}$.\nOn a $\\Delta \\omega = \\frac{\\omega_0}{Q}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "809-2693",
"position": 6,
"duration": 30,
"question": {
"id": "2693",
"question": "Montrer que pour un circuit RLC s\u00e9rie aliment\u00e9 en tension sinuso\u00efdale d'apmplitude $E_m$, l'amplitude complexe du courant traversant le circuit peut se mettre sous la forme :\n$$ \\underline{i_0} =  \\frac{E_m\/R}{1+jQ \\left( \\frac{\\omega}{\\omega_0} - \\frac{\\omega_0}{\\omega} \\right)} .$$\nExpliquer alors pourquoi le mode XY de l'oscilloscope permet de rep\u00e9rer la r\u00e9sonance. ",
"answer": "L'imp\u00e9dance totale du circuit est obtenu en sommant les imp\u00e9dances des 3 dip\u00f4les (montage s\u00e9rie), donc $\\underline{Z} = R + j L \\omega + \\frac{1}{j C \\omega}$.\n\nOn a alors $\\underline{i} (t) = \\frac{\\underline{u}(t)}{\\underline{Z}}$ et donc en divisant par $e^{j \\omega t}$ on trouve :\n$$\\underline{i_0} = \\frac{E_m}{R+j ( L\\omega - \\frac{1}{C \\omega})},$$ \nce qui correspond \u00e0 la formule demand\u00e9e avec $\\omega_0 = \\sqrt{\\frac{1}{LC}}$ et $Q = \\frac{\\sqrt{L\/C}}{R}$.\n\nLa r\u00e9sonance se produit alors \u00e0 la pulsation $\\omega_r = \\omega_0$, et on a alors $\\underline{i_0} = \\frac{E_m}{R}$ ( ou de mani\u00e8re \u00e9quivalente $\\underline{Z} = R \\in \\mathbb{R}$), donc l'intensit\u00e9 du courant est en phase avec la tension appliqu\u00e9e : sur l'oscilloscope en mode XY, la courbe obtenue est un segment de droite au lieu d'une ellipse.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"785": {
"id": "785",
"name": "Quizz 11 : Mol\u00e9cules, cristaux. Condensateur, bobine.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/785\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "114",
"value": "Atomistique",
"field_id": "23",
"created_at": "2017-08-21 12:25:31",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-28",
"questions": [{
"id": "785-2648",
"position": 0,
"duration": 30,
"question": {
"id": "2648",
"question": "Le fer $\\gamma$ cristallise selon une structure cubique faces centr\u00e9es. Dessiner une maille et dire combien il y a d'atomes de fer par maille.",
"answer": "Chaque maille compte $8 \\times \\frac18 + 6 \\frac12 =4$ atomes de fer.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/315570e0-966d-11e8-b104-9da36e698c3e",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "785-2649",
"position": 1,
"duration": 30,
"question": {
"id": "2649",
"question": "Le lithium cristallise selon un syst\u00e8me cubique centr\u00e9, avec une maille de longueur $a \\simeq 346 $ pm. Sachant que le contact se fait le long de la diagonale du cube, quel est le rayon d'un atome de lithium ?",
"answer": "Si on appelle $R$ le rayon de l'atome de lithium, le long de la diagonale du cube, on a l'\u00e9galit\u00e9 $4R = \\sqrt{3} a$, donc $R = \\frac{\\sqrt{3}a}{4} \\simeq 150 $ pm.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "785-2652",
"position": 2,
"duration": 30,
"question": {
"id": "2652",
"question": "Qu'est-ce que l'approximation des r\u00e9gimes quasi-stationnaires ? Quelles sont ses cons\u00e9quences ?",
"answer": "L'approximation des r\u00e9gimes quasi-stationnaires consiste \u00e0 consid\u00e9rer que les variations des grandeurs \u00e9lectriques sont suffisamment lentes. Les lois de Kirchhoff et la loi d'Ohm sont alors toujours valables.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2653",
"position": 3,
"duration": 30,
"question": {
"id": "2653",
"question": "A quelle condition sur la fr\u00e9quence $f$ des variations des grandeurs \u00e9lectriques peut-on consid\u00e9rer qu'un circuit \u00e9lectrique de taille caract\u00e9ristique $l$ est dans l'ARQS ?",
"answer": "On peut consid\u00e9rer que l'on est dans l'ARQS si $lf \\ll c$, et en pratique on se satisfera de $lf < c\/10$, $c$ \u00e9tant la vitesse de la lumi\u00e8re dans le vide.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2654",
"position": 4,
"duration": 30,
"question": {
"id": "2654",
"question": "A quelle condition sur la dur\u00e9e $\\tau$ d'un r\u00e9gime transitoire peut-on consid\u00e9rer qu'un circuit \u00e9lectrique de taille caract\u00e9ristique $l$ est dans l'ARQS ?",
"answer": "On pourra consid\u00e9rer que l'ARQS est valable si $l\/\\tau \\ll c$, et en pratique si $l\/\\tau < c\/10$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2655",
"position": 5,
"duration": 30,
"question": {
"id": "2655",
"question": "Peut-on consid\u00e9rer l'ARQS valable pour le r\u00e9seau EDF ?",
"answer": "La r\u00e9seau EDF a une taille caract\u00e9ristique $l$ de l'ordre de 1000 km et la fr\u00e9quence $f$ est de 50 Hz. On a donc $lf = 5.10^7$ m\/s, donc $lf \\simeq c\/6$, et l'ARQS n'est pas valable.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2656",
"position": 6,
"duration": 30,
"question": {
"id": "2656",
"question": "Quel est le lien entre tension et courant pour un condensateur ? A quoi est-il \u00e9quivalent en r\u00e9gime permanent ?",
"answer": "Pour un condensateur de capacit\u00e9 $C$ aliment\u00e9 par la tension \u00e0 ses bornes $U$, le courant qui le traverse v\u00e9rifie $ i = C \\frac{dU}{dt} $.\nEn r\u00e9gime permanent, $i \\to 0$, donc il est \u00e9quivalent \u00e0 un coupe-circuit (ou un interrupteur ouvert).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2657",
"position": 7,
"duration": 30,
"question": {
"id": "2657",
"question": "Quel est le lien entre tension et courant pour une bobine ? A quoi est-elle \u00e9quivalente en r\u00e9gime permanent ?",
"answer": "Pour une bobine d'inductance $L$ parcourue par un courant $i$, la tension \u00e0 ses bornes $U$ v\u00e9rifie $ U = L \\frac{di}{dt} $.\nEn r\u00e9gime permanent, $U \\to 0$, donc elle est \u00e9quivalente \u00e0 un court-circuit (ou un fil).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2658",
"position": 8,
"duration": 30,
"question": {
"id": "2658",
"question": "Quelle grandeur \u00e9lectrique est continue pour un condensateur ?",
"answer": "La tension aux bornes d'un condensateur est continue.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "785-2659",
"position": 9,
"duration": 30,
"question": {
"id": "2659",
"question": "Quelle grandeur \u00e9lectrique est continue pour une bobine ?",
"answer": "Le courant qui traverse une bobine est continu.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"788": {
"id": "788",
"name": "Quizz 12 : Circuits RL, RC",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/788\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.9,
"shared_at": "2024-12-04",
"questions": [{
"id": "788-2652",
"position": 0,
"duration": 30,
"question": {
"id": "2652",
"question": "Qu'est-ce que l'approximation des r\u00e9gimes quasi-stationnaires ? Quelles sont ses cons\u00e9quences ?",
"answer": "L'approximation des r\u00e9gimes quasi-stationnaires consiste \u00e0 consid\u00e9rer que les variations des grandeurs \u00e9lectriques sont suffisamment lentes. Les lois de Kirchhoff et la loi d'Ohm sont alors toujours valables.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "788-2653",
"position": 1,
"duration": 30,
"question": {
"id": "2653",
"question": "A quelle condition sur la fr\u00e9quence $f$ des variations des grandeurs \u00e9lectriques peut-on consid\u00e9rer qu'un circuit \u00e9lectrique de taille caract\u00e9ristique $l$ est dans l'ARQS ?",
"answer": "On peut consid\u00e9rer que l'on est dans l'ARQS si $lf \\ll c$, et en pratique on se satisfera de $lf < c\/10$, $c$ \u00e9tant la vitesse de la lumi\u00e8re dans le vide.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "788-2654",
"position": 2,
"duration": 30,
"question": {
"id": "2654",
"question": "A quelle condition sur la dur\u00e9e $\\tau$ d'un r\u00e9gime transitoire peut-on consid\u00e9rer qu'un circuit \u00e9lectrique de taille caract\u00e9ristique $l$ est dans l'ARQS ?",
"answer": "On pourra consid\u00e9rer que l'ARQS est valable si $l\/\\tau \\ll c$, et en pratique si $l\/\\tau < c\/10$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "788-2658",
"position": 3,
"duration": 30,
"question": {
"id": "2658",
"question": "Quelle grandeur \u00e9lectrique est continue pour un condensateur ?",
"answer": "La tension aux bornes d'un condensateur est continue.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "788-2659",
"position": 4,
"duration": 30,
"question": {
"id": "2659",
"question": "Quelle grandeur \u00e9lectrique est continue pour une bobine ?",
"answer": "Le courant qui traverse une bobine est continu.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "788-2660",
"position": 5,
"duration": 30,
"question": {
"id": "2660",
"question": "Etablir l'expression de la tension aux bornes d'un condensateur d'un circuit RC s\u00e9rie lors de la charge par une source de tension id\u00e9ale.",
"answer": "On appelle $i$ le courant traversant le circuit, $u$ la tension aux bornes du condensateur recherch\u00e9e, $u_R$ la tension aux bornes de la r\u00e9sistance et $E$ la tension d\u00e9livr\u00e9e par la source de tension.\nOn applique alors les lois \u00e0 notre disposition :\n- loi des mailles $E = u + u_R$ ;\n- loi d'Ohm $u_R = R i$ ;\n- caract\u00e9ristique du condensateur $i = C\\frac{du}{dt}$\n\nEn combinant ces trois \u00e9quations on trouve l'\u00e9quation diff\u00e9rentielle suivie par $u$ :\n$$ u + RC \\frac{du}{dt} = E $$\nque l'on r\u00e9\u00e9crit sous forme canonique en posant $\\tau = RC$ :\n$$ \\frac{du}{dt} + \\frac{u}{\\tau} = \\frac{E}{\\tau} $$\nOn peut donc r\u00e9soudre, et on trouve comme solution g\u00e9n\u00e9rale, la somme de la solution de l'\u00e9quation diff\u00e9rentielle sans second membre et d'une solution particuli\u00e8re :\n$$ u(t) = \\lambda e^{-t\/\\tau} + E $$\n\nLa condition initiale $u(t=0) = 0$, d\u00e9termin\u00e9e gr\u00e2ce \u00e0 la continuit\u00e9 de la tension aux bornes du condensateur, fixe $\\lambda = - E$ et on trouve finalement :\n$$ u(t) = (1 - e^{-t\/\\tau}) E .$$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "788-2661",
"position": 6,
"duration": 30,
"question": {
"id": "2661",
"question": "Etablir l'expression de la tension aux bornes d'un condensateur de capacit\u00e9 $C$, pr\u00e9alablement charg\u00e9 \u00e0 la tension $E$ lors de sa d\u00e9charge dans une r\u00e9sistance $R$.",
"answer": "On appelle $i$ le courant traversant le circuit, $u$ la tension aux bornes du condensateur recherch\u00e9e (en convention g\u00e9n\u00e9rateur), $u_R$ la tension aux bornes de la r\u00e9sistance.\nOn applique alors les lois \u00e0 notre disposition :\n- loi des mailles $u = u_R$ ;\n- loi d'Ohm $u_R = R i$ ;\n- caract\u00e9ristique du condensateur $i = - C\\frac{du}{dt}$\n\nEn combinant ces trois \u00e9quations on trouve l'\u00e9quation diff\u00e9rentielle suivie par $u$ :\n$$ u + RC \\frac{du}{dt} = 0 $$\nque l'on r\u00e9\u00e9crit sous forme canonique en posant $\\tau = RC$ :\n$$ \\frac{du}{dt} + \\frac{u}{\\tau} = 0$$\nOn peut donc r\u00e9soudre, et on trouve comme solution g\u00e9n\u00e9rale :\n$$ u(t) = \\lambda e^{-t\/\\tau} $$\n\nLa condition initiale $u(t=0) = E$, d\u00e9termin\u00e9e gr\u00e2ce \u00e0 la continuit\u00e9 de la tension aux bornes du condensateur, fixe $\\lambda = E$ et on trouve finalement :\n$$ u(t) = E  e^{-t\/\\tau} .$$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "788-2662",
"position": 7,
"duration": 30,
"question": {
"id": "2662",
"question": "Combien de temps dure la d\u00e9charge d'un condensateur de capacit\u00e9 $C = 1,0$ \u00b5F charg\u00e9 \u00e0 une tension $E=$ 3,0 V dans une r\u00e9sistance $R = 5,0$ k$\\Omega$ ?",
"answer": "Si on appelle $u$ la tension aux bornes du condensateur, on montre qu'elle suit l'\u00e9quation diff\u00e9rentielle :\n$$ \\frac{du}{dt} + \\frac{u}{RC} =0 $$,\non a donc un syst\u00e8me du premier ordre, avec un temps caract\u00e9ristique $\\tau = RC$.\nOn trouve alors $u(t) = E e^{-t\/\\tau}$, et donc on peut estimer que la d\u00e9charge est termin\u00e9e au bout d'un temps $T_{5\\%} = 3 \\tau$ ou d'un temps $T_{1\\%} = 5 \\tau$. On trouve respectivement $T_{5\\%} = 15$ ms et $T_{1\\%} = 25$ ms, et ce ind\u00e9pendamment de la valeur de la tension.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "788-2663",
"position": 8,
"duration": 30,
"question": {
"id": "2663",
"question": "Un circuit RL parall\u00e8le est aliment\u00e9 depuis longtemps par une source de courant id\u00e9ale $I_0$. A $t=0$ on ouvre l'interrupteur \u00e0 l'entr\u00e9e du circuit. Donner la valeur \u00e0 $t=0^-$, \u00e0 $t=0^+$ et \u00e0 $t \\to \\infty$ :\n- du courant traversant la bobine $i_L$ ;\n- du courant traversant la r\u00e9sistance $i_R$;\n- de la tension aux bornes de la r\u00e9sistance $u_R$;\n- de la tension aux bornes de la bobine $u_L$.\nQuelles grandeurs sont continues ?",
"answer": "Juste avant l'ouverture de l'interrupteur, on est en r\u00e9gime permanent, donc la bobine est \u00e9quivalent \u00e0 un fil, on a donc $u_L(t=0^-) = 0$, or la r\u00e9sistance et la bobine \u00e9tant en parall\u00e8le, les tensions \u00e0 leurs bornes sont \u00e9gales donc $u_R (t=0^-) = 0$. On utilise ensuite la loi d'Ohm pour d\u00e9terminer $i_R (t=0^-) =0$ et la loi des n\u0153uds pour trouver $i_L(t=0^-) = I_0$.\n\nOn utilise la continuit\u00e9 du courant traversant une bobine pour trouver $i_L (t=0^+) = i_L(t=0^-) = I_0$.\nLa loi des n\u0153uds fixe apr\u00e8s ouverture de l'interrupteur $i_R = -i_L$, donc $i_R(t=0^+) = - I_0$, et avec la loi d'Ohm, on trouve $u_R(t=0^+) = - R I_0$ et donc $u_L(t=0^+) = - R I_0$.\n\nEn r\u00e9gime permanent \u00e0 $t \\to \\infty$, la bobine est \u00e9quivalent \u00e0 un fil, donc $u_L (t \\to \\infty) = 0$, d'o\u00f9 $u_R (t \\to \\infty) =0$ et gr\u00e2ce \u00e0 la loi d'Ohm puis la loi des n\u0153uds, on d\u00e9duit $i_R(t \\to \\infty) = 0$ et $i_L (t \\to \\infty)$.\n\nOn voit alors que seul $i_L$ est continue car c'est la seule grandeur v\u00e9rifiant $i_L(t=0^-) = i_L (t=0^+)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "788-2664",
"position": 9,
"duration": 30,
"question": {
"id": "2664",
"question": "Lors de la charge commen\u00e7ant \u00e0 l'instant $t=0$ d'une bobine d'inductance $L$ en parall\u00e8le avec une r\u00e9sistance $R$ par une source id\u00e9ale de courant $I_0$, on montre que le courant traversant la bobine est $i_L (t>0) = I_0 (1 - e^{-t\/\\tau})$ et la tension \u00e0 ses bornes est $u_L(t) = R I_0 e^{-t\/\\tau}$ avec $\\tau = L \/R$.\nExprimer la puissance fournie par le g\u00e9n\u00e9rateur, stock\u00e9e dans la bobine et dissip\u00e9e dans la r\u00e9sistance puis effectuer le bilan de puissance.\nCalculer le rendement de cette charge.",
"answer": "La puissance fournie par le g\u00e9n\u00e9rateur est $P_f (t) = u_L (t) I_0$ puisque la tension \u00e0 ses bornes est la m\u00eame que celle aux bornes de la bobine (les trois dip\u00f4les sont en parall\u00e8le).\nLa puissance stock\u00e9e dans la bobine est $P_s (t) = u_L(t) i_L (t)$ , et gr\u00e2ce \u00e0 la loi des n\u0153uds, la puissance dissip\u00e9e dans la r\u00e9sistance est $P_d(t) = u_L(t) (I_0 - i_L(t))$.\n\nOn obtient donc :\n$P_f (t) = RI_0^2 e^{-t\/\\tau}$ ;\n$P_s (t) = RI_0^2 (e^{-t\/\\tau} - e^{-2t\/\\tau})$ ;\n$P_d (t) = RI_0^2 e^{-2t\/\\tau}$ .\n\nOn a donc bien un bilan de puissance \u00e9quilibr\u00e9 $P_f(t) = P_s (t) + P_d (t)$.\n\nCalculons alors l'\u00e9nergie fournie par le g\u00e9n\u00e9rateur au cours de la charge :\n$E_f = \\int_0^\\infty P_f(t) dt = R I_0^2 \\int_0^\\infty e^{-t\/\\tau} dt = R I_0^2 [ - \\tau e^{-t\/\\tau}]_0^\\infty = \\tau R I_0^2 = LI_0^2$\n\nL'\u00e9nergie stock\u00e9e dans une bobine d'inducatnce $L$ parcourue par un courant $I_0$ est donn\u00e9e par la formule $E_s = \\frac12 L I_0^2$.\n\nOn a donc $E_s = \\frac{E_f}{2}$, donc le rendement de cette charge est de 50 % (ind\u00e9pendamment de la valeur de la r\u00e9sistance choisie !)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"791": {
"id": "791",
"name": "Quizz 13 : RL,RC. Cin\u00e9tique chimique.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/791\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-12",
"questions": [{
"id": "791-2661",
"position": 0,
"duration": 30,
"question": {
"id": "2661",
"question": "Etablir l'expression de la tension aux bornes d'un condensateur de capacit\u00e9 $C$, pr\u00e9alablement charg\u00e9 \u00e0 la tension $E$ lors de sa d\u00e9charge dans une r\u00e9sistance $R$.",
"answer": "On appelle $i$ le courant traversant le circuit, $u$ la tension aux bornes du condensateur recherch\u00e9e (en convention g\u00e9n\u00e9rateur), $u_R$ la tension aux bornes de la r\u00e9sistance.\nOn applique alors les lois \u00e0 notre disposition :\n- loi des mailles $u = u_R$ ;\n- loi d'Ohm $u_R = R i$ ;\n- caract\u00e9ristique du condensateur $i = - C\\frac{du}{dt}$\n\nEn combinant ces trois \u00e9quations on trouve l'\u00e9quation diff\u00e9rentielle suivie par $u$ :\n$$ u + RC \\frac{du}{dt} = 0 $$\nque l'on r\u00e9\u00e9crit sous forme canonique en posant $\\tau = RC$ :\n$$ \\frac{du}{dt} + \\frac{u}{\\tau} = 0$$\nOn peut donc r\u00e9soudre, et on trouve comme solution g\u00e9n\u00e9rale :\n$$ u(t) = \\lambda e^{-t\/\\tau} $$\n\nLa condition initiale $u(t=0) = E$, d\u00e9termin\u00e9e gr\u00e2ce \u00e0 la continuit\u00e9 de la tension aux bornes du condensateur, fixe $\\lambda = E$ et on trouve finalement :\n$$ u(t) = E  e^{-t\/\\tau} .$$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "791-2662",
"position": 1,
"duration": 30,
"question": {
"id": "2662",
"question": "Combien de temps dure la d\u00e9charge d'un condensateur de capacit\u00e9 $C = 1,0$ \u00b5F charg\u00e9 \u00e0 une tension $E=$ 3,0 V dans une r\u00e9sistance $R = 5,0$ k$\\Omega$ ?",
"answer": "Si on appelle $u$ la tension aux bornes du condensateur, on montre qu'elle suit l'\u00e9quation diff\u00e9rentielle :\n$$ \\frac{du}{dt} + \\frac{u}{RC} =0 $$,\non a donc un syst\u00e8me du premier ordre, avec un temps caract\u00e9ristique $\\tau = RC$.\nOn trouve alors $u(t) = E e^{-t\/\\tau}$, et donc on peut estimer que la d\u00e9charge est termin\u00e9e au bout d'un temps $T_{5\\%} = 3 \\tau$ ou d'un temps $T_{1\\%} = 5 \\tau$. On trouve respectivement $T_{5\\%} = 15$ ms et $T_{1\\%} = 25$ ms, et ce ind\u00e9pendamment de la valeur de la tension.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "791-2663",
"position": 2,
"duration": 30,
"question": {
"id": "2663",
"question": "Un circuit RL parall\u00e8le est aliment\u00e9 depuis longtemps par une source de courant id\u00e9ale $I_0$. A $t=0$ on ouvre l'interrupteur \u00e0 l'entr\u00e9e du circuit. Donner la valeur \u00e0 $t=0^-$, \u00e0 $t=0^+$ et \u00e0 $t \\to \\infty$ :\n- du courant traversant la bobine $i_L$ ;\n- du courant traversant la r\u00e9sistance $i_R$;\n- de la tension aux bornes de la r\u00e9sistance $u_R$;\n- de la tension aux bornes de la bobine $u_L$.\nQuelles grandeurs sont continues ?",
"answer": "Juste avant l'ouverture de l'interrupteur, on est en r\u00e9gime permanent, donc la bobine est \u00e9quivalent \u00e0 un fil, on a donc $u_L(t=0^-) = 0$, or la r\u00e9sistance et la bobine \u00e9tant en parall\u00e8le, les tensions \u00e0 leurs bornes sont \u00e9gales donc $u_R (t=0^-) = 0$. On utilise ensuite la loi d'Ohm pour d\u00e9terminer $i_R (t=0^-) =0$ et la loi des n\u0153uds pour trouver $i_L(t=0^-) = I_0$.\n\nOn utilise la continuit\u00e9 du courant traversant une bobine pour trouver $i_L (t=0^+) = i_L(t=0^-) = I_0$.\nLa loi des n\u0153uds fixe apr\u00e8s ouverture de l'interrupteur $i_R = -i_L$, donc $i_R(t=0^+) = - I_0$, et avec la loi d'Ohm, on trouve $u_R(t=0^+) = - R I_0$ et donc $u_L(t=0^+) = - R I_0$.\n\nEn r\u00e9gime permanent \u00e0 $t \\to \\infty$, la bobine est \u00e9quivalent \u00e0 un fil, donc $u_L (t \\to \\infty) = 0$, d'o\u00f9 $u_R (t \\to \\infty) =0$ et gr\u00e2ce \u00e0 la loi d'Ohm puis la loi des n\u0153uds, on d\u00e9duit $i_R(t \\to \\infty) = 0$ et $i_L (t \\to \\infty)$.\n\nOn voit alors que seul $i_L$ est continue car c'est la seule grandeur v\u00e9rifiant $i_L(t=0^-) = i_L (t=0^+)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "791-2664",
"position": 3,
"duration": 30,
"question": {
"id": "2664",
"question": "Lors de la charge commen\u00e7ant \u00e0 l'instant $t=0$ d'une bobine d'inductance $L$ en parall\u00e8le avec une r\u00e9sistance $R$ par une source id\u00e9ale de courant $I_0$, on montre que le courant traversant la bobine est $i_L (t>0) = I_0 (1 - e^{-t\/\\tau})$ et la tension \u00e0 ses bornes est $u_L(t) = R I_0 e^{-t\/\\tau}$ avec $\\tau = L \/R$.\nExprimer la puissance fournie par le g\u00e9n\u00e9rateur, stock\u00e9e dans la bobine et dissip\u00e9e dans la r\u00e9sistance puis effectuer le bilan de puissance.\nCalculer le rendement de cette charge.",
"answer": "La puissance fournie par le g\u00e9n\u00e9rateur est $P_f (t) = u_L (t) I_0$ puisque la tension \u00e0 ses bornes est la m\u00eame que celle aux bornes de la bobine (les trois dip\u00f4les sont en parall\u00e8le).\nLa puissance stock\u00e9e dans la bobine est $P_s (t) = u_L(t) i_L (t)$ , et gr\u00e2ce \u00e0 la loi des n\u0153uds, la puissance dissip\u00e9e dans la r\u00e9sistance est $P_d(t) = u_L(t) (I_0 - i_L(t))$.\n\nOn obtient donc :\n$P_f (t) = RI_0^2 e^{-t\/\\tau}$ ;\n$P_s (t) = RI_0^2 (e^{-t\/\\tau} - e^{-2t\/\\tau})$ ;\n$P_d (t) = RI_0^2 e^{-2t\/\\tau}$ .\n\nOn a donc bien un bilan de puissance \u00e9quilibr\u00e9 $P_f(t) = P_s (t) + P_d (t)$.\n\nCalculons alors l'\u00e9nergie fournie par le g\u00e9n\u00e9rateur au cours de la charge :\n$E_f = \\int_0^\\infty P_f(t) dt = R I_0^2 \\int_0^\\infty e^{-t\/\\tau} dt = R I_0^2 [ - \\tau e^{-t\/\\tau}]_0^\\infty = \\tau R I_0^2 = LI_0^2$\n\nL'\u00e9nergie stock\u00e9e dans une bobine d'inducatnce $L$ parcourue par un courant $I_0$ est donn\u00e9e par la formule $E_s = \\frac12 L I_0^2$.\n\nOn a donc $E_s = \\frac{E_f}{2}$, donc le rendement de cette charge est de 50 % (ind\u00e9pendamment de la valeur de la r\u00e9sistance choisie !)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "791-2665",
"position": 4,
"duration": 30,
"question": {
"id": "2665",
"question": "Pour la r\u00e9action de combustion du m\u00e9thane $CH_4 + 2 O_2 = CO_2 + 2 H_2O$, donner en fonction des concentrations des esp\u00e8ces chimiques l'expression :\n- de la vitesse de formation des produits ;\n- de la vitesse de disparition des r\u00e9actifs ;\n- de la vitesse de r\u00e9action.\n\nExprimer la vitesse de r\u00e9action en fonction des 4 vitesses de formation ou de disparition.\n",
"answer": "On a :\n- $v_{CO_2} = \\frac{d[CO_2]}{dt}$ et $v_{H_2O} = \\frac{d[H_2O]}{dt}$ ;\n- $v_{CH_4} = - \\frac{d[CH_4]}{dt}$ et $v_{O_2} = - \\frac{d[O_2]}{dt}$ ;\n- $v = -\\frac{d[CH_4]}{dt} = - \\frac12 \\frac{d[O_2]}{dt} = \\frac{d[CO_2]}{dt} = \\frac12 \\frac{d[H_2O]}{dt}$\n- $v = v_{CH_4} = \\frac12 v_{O_2} = v_{CO_2} = \\frac12 v_{H_2O}$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "791-2666",
"position": 5,
"duration": 30,
"question": {
"id": "2666",
"question": "En quelle unit\u00e9 SI s'exprime une vitesse de r\u00e9action chimique ?",
"answer": "Elle s'exprime en mol.L$^{-1}$.s$^{-1}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "791-2667",
"position": 6,
"duration": 30,
"question": {
"id": "2667",
"question": "Citer deux param\u00e8tres qui influencent une vitesse de r\u00e9action.",
"answer": "On peut citer la temp\u00e9rature, la concentration des esp\u00e8ces chimiques (en solution), les pressions (en phase gazeuse), la surface de contact (en phase solide), etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "791-2668",
"position": 7,
"duration": 30,
"question": {
"id": "2668",
"question": "Que peut-on dire sur la vitesse de r\u00e9action si la r\u00e9action $\\alpha A + \\beta B = \\gamma C + \\delta D$ admet un ordre ?",
"answer": "Si cette r\u00e9action admet un ordre, alors sa vitesse de r\u00e9action s'\u00e9crit sous la forme $v= k [A]^{n_A} [B]^{n_B}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "791-2669",
"position": 8,
"duration": 30,
"question": {
"id": "2669",
"question": "La r\u00e9action $CO + Cl_2 = COCl_2$ a pour vitesse de r\u00e9action $v = k [CO] [Cl_2]^{3\/2}$.\nComment s'appelle et quelle est l'unit\u00e9 de $k$ ?\nQue vaut l'ordre global de cette r\u00e9action ?",
"answer": "$k$ est la constante de vitesse.\nPour cette r\u00e9action, $k$ s'exprime en mol$^{-3\/2}$.L$^{3\/2}$.s$^{-1}$.\nL'ordre global de cette r\u00e9action est 5\/2.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "791-2670",
"position": 9,
"duration": 30,
"question": {
"id": "2670",
"question": "On souhaite \u00e9tudier la cin\u00e9tique de la r\u00e9action $CO + Cl_2 = COCl_2$, dont on sait qu'elle admet un ordre : $v = k [CO]^\\alpha [Cl_2]^\\beta$.\nD\u00e9crire les deux m\u00e9thodes permettant d'exprimer la vitesse de la r\u00e9action en fonction de la seule concentration en $Cl_2$, et qui permet donc de faciliter l'\u00e9tude. Pr\u00e9ciser pour chaque m\u00e9thode quelle grandeur peut-\u00eatre calcul\u00e9e.",
"answer": "Premi\u00e8re m\u00e9thode :on se place dans les conditions st\u0153chiom\u00e9triques, donc telles qu'\u00e0 tout instant $[CO]=[Cl_2]$. On peut alors \u00e9crire $v = k [CO]^\\alpha [Cl_2]^\\beta = k [Cl_2]^{\\alpha+\\beta}$. On peut donc d\u00e9terminer $\\alpha+\\beta$, c'est-\u00e0-dire l'ordre global de la r\u00e9action.\n\nDeuxi\u00e8me m\u00e9thode (m\u00e9thode de la d\u00e9g\u00e9n\u00e9rescence de l'ordre) : on introduit $CO$ en grand exc\u00e8s, donc $[CO] \\simeq [CO]_0$. On a donc $v = k [CO]^\\alpha [Cl_2]^\\beta \\simeq k' [Cl_2]^\\beta$ en posant $k' = k [CO]_0^\\alpha$. On peut avec cette m\u00e9thode d\u00e9terminer $\\beta$, l'ordre partiel de la r\u00e9action par rapport \u00e0 $Cl_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"801": {
"id": "801",
"name": "Quizz 16 : Oscillateurs amortis",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/801\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 150,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-19",
"questions": [{
"id": "801-2681",
"position": 0,
"duration": 30,
"question": {
"id": "2681",
"question": "On consid\u00e8re un circuit RLC s\u00e9rie pr\u00e9alablement charg\u00e9 sous la tension $E$. D\u00e9terminer l'\u00e9quation diff\u00e9rentielle suivie par la tension aux bornes du condensateur lors de la r\u00e9ponse libre, et exprimer le facteur de qualit\u00e9 et la pulsation propre en fonction de $R$, $L$ et $C$.",
"answer": "Appelons $i$ le courant qui traverse le montage, $u$ la tension aux bornes du condensateur, $u_L$ celle aux bornes de la bobine et $u_R$ celle aux bornes de la r\u00e9sistance, choisies toutes trois en convention r\u00e9cepteur.\nLa loi des mailles nous dit que $u_L + u_R +u= 0$, et les caract\u00e9ristiques des dip\u00f4les que $i = C \\frac{du}{dt}$ (pour le condensateur), $u_L = L \\frac{di}{dt}$ (pour la bobine) et $u_R = R i$ (pour la r\u00e9sistance).\nOn en d\u00e9duit donc que $LC \\frac{d^2u}{dt^2} + RC \\frac{du}{dt} + u = 0$, que l'on met sous forme canonique $\\frac{d^2u}{dt^2} + \\frac{\\omega_0}{Q} \\frac{du}{dt} + \\omega_0^2 u = 0$ en posant pour la pulsation propre $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ et $Q = \\frac{\\sqrt{L\/C}}{R}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "801-2682",
"position": 1,
"duration": 30,
"question": {
"id": "2682",
"question": "Un oscillateur amorti pr\u00e9sente une r\u00e9ponse suivant l'\u00e9quation diff\u00e9rentielle $\\frac{d^2y}{dt^2} + \\frac{\\omega_0}{Q} \\frac{dy}{dt} + y =0$. Quelle est la nature du r\u00e9gime en fonction de la valeur du facteur de qualit\u00e9 ?",
"answer": "Si $Q < 1\/2$, r\u00e9gime ap\u00e9riodique, si $Q>1\/2$ r\u00e9gime pseudo-p\u00e9riodique et si $Q=1\/2$, r\u00e9gime critique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "801-2683",
"position": 2,
"duration": 30,
"question": {
"id": "2683",
"question": "La r\u00e9ponse d'un oscillateur amorti s'\u00e9crit de la forme \n$$y(t) = e^{-\\frac{\\omega_0 t}{2Q}} \\left[ A \\cos \\left(\\omega_0 t\\sqrt{1-\\frac{1}{4Q^2}}\\right) + B \\sin \\left(\\omega_0 t\\sqrt{1-\\frac{1}{4Q^2}}\\right) \\right] $$\nQuelle est la nature du r\u00e9gime et la valeur du facteur de qualit\u00e9 ?\nDonner une estimation de la dur\u00e9e du r\u00e9gime transitoire.",
"answer": "Il s'agit d'un r\u00e9gime pseudo-p\u00e9riodique, donc $Q>1\/2$.\nL'enveloppe des oscillations est exponentiellement d\u00e9croissante avec un temps caract\u00e9ristique $\\tau = \\frac{2Q}{\\omega_0}$, donc on peut estimer une dur\u00e9e du r\u00e9gime transitoire de l'ordre de $5 \\tau = \\frac{10Q}{\\omega_0}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "801-2684",
"position": 3,
"duration": 30,
"question": {
"id": "2684",
"question": "La r\u00e9ponse d'un oscillateur amorti s'\u00e9crit de la forme \n$$y(t) = e^{-\\frac{\\omega_0 t}{2Q}} \\left[ A e^{\\omega_0 t\\sqrt{\\frac{1}{4Q^2}-1}} + B e^{- \\omega_0 t\\sqrt{\\frac{1}{4Q^2}-1}} \\right] $$\nQuelle est la nature du r\u00e9gime et la valeur du facteur de qualit\u00e9 ?\nDonner une estimation de la dur\u00e9e du r\u00e9gime transitoire.\nRappel : pour $x$ petit, $\\sqrt{1-x} \\simeq 1 - \\frac{x}{2}$",
"answer": "Il s'agit d'un r\u00e9gime ap\u00e9riodique, donc $Q<1\/2$.\nIl est la somme de deux signaux exponentiellement d\u00e9croissante. Le signal qui d\u00e9croit le plus lentement d\u00e9cro\u00eet avec un temps caract\u00e9ristique $\\tau$ tel que $\\frac{1}{\\tau} = \\frac{\\omega_0}{2Q} - \\omega_0 \\sqrt{\\frac{1}{4Q^2}-1}$.\n\nOn a alors $\\frac{1}{\\tau} \\simeq \\frac{\\omega_0}{2Q} \\left( 1 - 1+ 2 Q^2 \\right) = Q \\omega_0$.\n\nOn trouve donc un r\u00e9gime transitoire d'une dur\u00e9e de l'ordre de $\\frac{5}{Q \\omega_0}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "801-2685",
"position": 4,
"duration": 30,
"question": {
"id": "2685",
"question": "Pour quelle valeur du facteur de qualit\u00e9 le r\u00e9gime transitoire d'un oscillateur amorti de pulsation propre fix\u00e9e le r\u00e9gime transitoire dure le moins longtemps ?",
"answer": "Le r\u00e9gime qui a le transitoire le plus court est le r\u00e9gime critique, c'est donc la valeur $Q =1\/2$ qu'il faut choisir.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"805": {
"id": "805",
"name": "Quizz 17 : Oscillateurs amortis. R\u00e9sonances.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/805\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-16",
"questions": [{
"id": "805-2683",
"position": 0,
"duration": 30,
"question": {
"id": "2683",
"question": "La r\u00e9ponse d'un oscillateur amorti s'\u00e9crit de la forme \n$$y(t) = e^{-\\frac{\\omega_0 t}{2Q}} \\left[ A \\cos \\left(\\omega_0 t\\sqrt{1-\\frac{1}{4Q^2}}\\right) + B \\sin \\left(\\omega_0 t\\sqrt{1-\\frac{1}{4Q^2}}\\right) \\right] $$\nQuelle est la nature du r\u00e9gime et la valeur du facteur de qualit\u00e9 ?\nDonner une estimation de la dur\u00e9e du r\u00e9gime transitoire.",
"answer": "Il s'agit d'un r\u00e9gime pseudo-p\u00e9riodique, donc $Q>1\/2$.\nL'enveloppe des oscillations est exponentiellement d\u00e9croissante avec un temps caract\u00e9ristique $\\tau = \\frac{2Q}{\\omega_0}$, donc on peut estimer une dur\u00e9e du r\u00e9gime transitoire de l'ordre de $5 \\tau = \\frac{10Q}{\\omega_0}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "805-2684",
"position": 1,
"duration": 30,
"question": {
"id": "2684",
"question": "La r\u00e9ponse d'un oscillateur amorti s'\u00e9crit de la forme \n$$y(t) = e^{-\\frac{\\omega_0 t}{2Q}} \\left[ A e^{\\omega_0 t\\sqrt{\\frac{1}{4Q^2}-1}} + B e^{- \\omega_0 t\\sqrt{\\frac{1}{4Q^2}-1}} \\right] $$\nQuelle est la nature du r\u00e9gime et la valeur du facteur de qualit\u00e9 ?\nDonner une estimation de la dur\u00e9e du r\u00e9gime transitoire.\nRappel : pour $x$ petit, $\\sqrt{1-x} \\simeq 1 - \\frac{x}{2}$",
"answer": "Il s'agit d'un r\u00e9gime ap\u00e9riodique, donc $Q<1\/2$.\nIl est la somme de deux signaux exponentiellement d\u00e9croissante. Le signal qui d\u00e9croit le plus lentement d\u00e9cro\u00eet avec un temps caract\u00e9ristique $\\tau$ tel que $\\frac{1}{\\tau} = \\frac{\\omega_0}{2Q} - \\omega_0 \\sqrt{\\frac{1}{4Q^2}-1}$.\n\nOn a alors $\\frac{1}{\\tau} \\simeq \\frac{\\omega_0}{2Q} \\left( 1 - 1+ 2 Q^2 \\right) = Q \\omega_0$.\n\nOn trouve donc un r\u00e9gime transitoire d'une dur\u00e9e de l'ordre de $\\frac{5}{Q \\omega_0}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "805-2686",
"position": 2,
"duration": 30,
"question": {
"id": "2686",
"question": "Quelle est la grandeur complexe $\\underline{u} (t)$ associ\u00e9e \u00e0 la grandeur r\u00e9elle $u(t) = U \\cos (\\omega t + \\phi)$ ?",
"answer": "Il s'agit de $\\underline{u} (t) = \\underline{U_0} e^{j \\omega t}$, avec $\\underline{U_0} = U e^{j \\phi}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "805-2688",
"position": 3,
"duration": 30,
"question": {
"id": "2688",
"question": "On consid\u00e8re les oscillations d'une masse $m$ attach\u00e9e \u00e0 un ressort horizontal de constante de raideur $k$ soumise \u00e0 une force variable $F(t) = F_m \\cos (\\omega t)$, en pr\u00e9sence de frottements fluides de coefficient $h$. Ecrire l'\u00e9quation diff\u00e9rentielle suivie la position de la masse puis la mettre sous la forme $\\frac{d^2x}{dt^2} + \\frac{\\omega_0}{Q} \\frac{dx}{dt} + \\omega_0^2 x = \\omega_0^2 x_m \\cos(\\omega t)$ en pr\u00e9cisant les valeurs de chaque notation introduite.",
"answer": "On applique le PFD \u00e0 la masse :\n- son acc\u00e9l\u00e9ration est $\\frac{d^2x}{dt^2}$ ;\n- la force exerc\u00e9e par le ressort est $- kx$ ;\n- la force exerc\u00e9e par les frottements fluides est $ - h \\frac{dx}{dt}$ ;\n- la force ext\u00e9rieure est $F_m \\cos (\\omega t)$.\n\nOn applique le PFD et on trouve :\n$$ m \\frac{d^2x}{dt^2} = - k x - h \\frac{dx}{dt} + F_m \\cos (\\omega t) $$\n\nCette \u00e9quation se met alors sous la forme demand\u00e9e en posant $\\omega_0 = \\sqrt{\\frac{k}{m}}$ , $Q = \\frac{\\sqrt{km}}{h}$ et $x_m = \\frac{F_m}{m \\omega_0^2} = \\frac{F_m}{k}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "805-2689",
"position": 4,
"duration": 30,
"question": {
"id": "2689",
"question": "Trouver l'amplitude des oscillations d'un oscillateur amorti soumis \u00e0 une excitation sinuso\u00efdale, ob\u00e9issant \u00e0 l'\u00e9quation diff\u00e9rentielle $\\frac{d^2x}{dt^2} + \\frac{\\omega_0}{Q} \\frac{dx}{dt} + \\omega_0^2 x = \\omega_0^2 x_m \\cos(\\omega t)$.",
"answer": "On introduit la notation complexe $\\underline{x} (t) = \\underline{X} e^{j\\omega t}$, alors l'\u00e9quation diff\u00e9rentielle devient pour $\\underline{x}$ :\n$$ (- \\omega^2 + j \\frac{\\omega \\omega_0}{Q} + \\omega_0^2) \\underline{x} = \\omega_0^2 x_m e^{j \\omega t} $$\n\net donc on obtient $\\underline{X} = x_m \\frac{\\omega_0^2}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q}$.\n\nL'amplitude des oscillations $X$ est alors $X = \\vert \\underline{X} \\vert$ donc\n$$ X = x_m \\frac{\\omega_0^2}{\\sqrt{(\\omega^2 - \\omega_0^2)^2 + \\frac{\\omega^2 \\omega_0^2}{Q^2}}} = \\frac{x_m}{\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}}$$.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "805-2690",
"position": 5,
"duration": 30,
"question": {
"id": "2690",
"question": "L'amplitude des oscillations d'un oscillateur amorti de pulsation propre $\\omega_0$ et de facteur de qualit\u00e9 $Q$, soumis \u00e0 une excitation de pulsation $\\omega$ est donn\u00e9e par $ X(\\omega) = \\frac{x_m}{\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}}$.\nA quelle condition sur $Q$ observera t'on une r\u00e9sonance ? Que vaut alors la pulsation de r\u00e9sonance ?\n",
"answer": "On cherche \u00e0 d\u00e9terminer si $X(\\omega)$ pr\u00e9sente un maximum pour $\\omega>0$. Ce sera le cas si $\\sqrt{\\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2}$ pr\u00e9sente un minimum, donc si $f(\\omega) = \\left(1 - \\left(\\frac{\\omega}{\\omega_0}\\right)^2\\right)^2+ \\left(\\frac{\\omega}{Q\\omega_0}\\right)^2$ pr\u00e9sente un minimum.\nPosons le polyn\u00f4me du second degr\u00e9 $P(x) = (1-x)^2 + \\frac{x}{Q^2} = x^2 + \\left(\\frac{1}{Q^2}-2 \\right) x +1$ tel que $f(\\omega) = P(\\frac{\\omega^2}{\\omega_0^2})$.\nIl faut donc d\u00e9terminer si $P(x)$ admet un minimum pour $x>0$.\nLe minimum de $P$ est atteint pour $\\frac{-\\left(\\frac{1}{Q^2}-2 \\right)}{2}$, donc il y aura bien r\u00e9sonance si $\\left(\\frac{1}{Q^2}-2 \\right)<0$, donc si $Q>\\frac{1}{\\sqrt{2}}$.\n\nLe minimum de $P$ est alors atteint en $x = 1 - \\frac{1}{2Q^2}$, donc le minimum de $f(\\omega)$ est atteint pour $\\omega_r$ tel que $\\left(\\frac{\\omega_r}{\\omega_0} \\right)^2 = 1 - \\frac{1}{2Q^2}$, donc la pulsation de r\u00e9sonance est :\n$$ \\omega_r = \\omega_0 \\sqrt{1- \\frac{1}{2Q^2}} $$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "805-2691",
"position": 6,
"duration": 30,
"question": {
"id": "2691",
"question": "L'amplitude complexe des oscillations d'un oscillateur amorti de pulsation propre $\\omega_0$ et de facteur de qualit\u00e9 $Q$, soumis \u00e0 une excitation de pulsation $\\omega$ est donn\u00e9e par $\\underline{X} = x_m \\frac{\\omega_0^2}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q}$.\nMontrer que l'amplitude complexe des oscillations de la vitesse s'exprime sous la forme :\n$$ \\underline{v_0} = \\frac{Q \\omega_0 x_m}{1 + j Q \\left( \\frac{\\omega}{\\omega_0} - \\frac{\\omega_0}{\\omega} \\right)^2} .$$\n\nA quelle condition sur $Q$ observera t'on une r\u00e9sonance ? A quelle pulsation ?",
"answer": "On sait que la vitesse est la d\u00e9riv\u00e9e de la position, $v = \\frac{dx}{dt}$, donc avec les notations complexes, $\\underline{v} = j \\omega \\underline{x}$, et donc $$\\underline{v_0} = j \\omega \\underline{X} =  \\frac{j \\omega \\omega_0^2 x_m}{\\omega_0^2 - \\omega^2 + j (\\omega \\omega_0)\/Q} $$\nOn divise alors num\u00e9rateur et d\u00e9nominateur par $j \\omega \\omega_0\/Q$ pour trouver le r\u00e9sultat demand\u00e9.\n\nOn aura alors r\u00e9sonance si $\\vert \\underline{v_0} \\vert = \\frac{Q \\omega_0 x_m}{\\sqrt{1 +  Q^2 \\left( \\frac{\\omega}{\\omega_0} - \\frac{\\omega_0}{\\omega} \\right)^4}}$ pr\u00e9sente un maximum. C'est toujours le cas, quelque soit la valeur de $Q$, et la pulsation de r\u00e9sonance est $\\omega_r = \\omega_0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"813": {
"id": "813",
"name": "Quizz 19 : Filtrage.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/813\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "115",
"value": "Signaux",
"field_id": "23",
"created_at": "2017-08-21 12:25:59",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-20",
"questions": [{
"id": "813-2694",
"position": 0,
"duration": 30,
"question": {
"id": "2694",
"question": "Qu'est-ce que la fonction de transfert d'un filtre ? Son gain, son d\u00e9phasage ? Son gain en d\u00e9cibel ?",
"answer": "Un filtre ayant pour signal de sortie $s(t)$ lorsqu'on lui envoie le signal d'entr\u00e9e $e(t)$ est caract\u00e9ris\u00e9 par sa fonction de transfert $\\underline{H} (\\omega)$, donn\u00e9 par le rapport entre l'amplitude complexe de $\\underline{s}$ et celle de $\\underline{e}$ lorsque l'entr\u00e9e est un signal sinuso\u00efdal de pulsation $\\omega$.\n\nOn a \u00e0 la pulsation $\\omega$, $\\underline{H} (\\omega) = G(\\omega) e^{j \\phi(\\omega)}$, donc on d\u00e9finit le gain (lin\u00e9aire) comme le module de la fonction de transfert $G(\\omega) = \\vert \\underline{H} (\\omega) \\vert$, et le d\u00e9phasage comme son argument $\\phi(\\omega) = \\textrm{Arg} \\left( \\underline{H} (\\omega) \\right)$.\n\nLe gain en d\u00e9cibel est obtenu en prenant 20 fois le logarithme d\u00e9cimal du gain lin\u00e9aire : $G_{deb} (\\omega) = 20 \\log_{10} G(\\omega)$.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "813-2695",
"position": 1,
"duration": 30,
"question": {
"id": "2695",
"question": "Qu'est-ce que la diagramme de Bode d'un filtre ?",
"answer": "C'est le trac\u00e9 de deux courbes, celles donnant le gain en d\u00e9cibel en fonction de la pulsation (ou de la fr\u00e9quence), et celle donnant le d\u00e9phasage.\nOn utilise g\u00e9n\u00e9ralement une \u00e9chelle logarithmique pour la pulsation ou la fr\u00e9quence.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "813-2699",
"position": 2,
"duration": 30,
"question": {
"id": "2699",
"question": "Quel type de filtre est r\u00e9alis\u00e9 par un circuit RC quand on regarde la tension aux bornes de la r\u00e9sistance ?",
"answer": "On utilise un pont diviseur de tension et on trouve directement la fonction de transfert :\n$\\underline{H} (\\omega) = \\frac{R}{R+\\frac{1}{jC\\omega}} = \\frac{j RC \\omega}{1 + j RC \\omega}$.\n\nOn voit alors que $\\underline{H} (\\omega) \\to 0$ quand $\\omega \\to 0$, et $\\underline{H} (\\omega) \\to 1$ quand $\\omega \\to \\infty$, il s'agit donc d'un filtre passe-haut.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "813-2702",
"position": 3,
"duration": 30,
"question": {
"id": "2702",
"question": "Quel type de filtre est r\u00e9alis\u00e9 par un circuit RL quand on regarde la tension aux bornes de la bobine ?",
"answer": "On utilise un pont diviseur de tension et on trouve directement la fonction de transfert :\n$\\underline{H} (\\omega) = \\frac{j L \\omega }{R+jL\\omega} = \\frac{j \\frac{L}{R} \\omega}{1 + j \\frac{L}{R} \\omega}$.\n\nOn voit alors que $\\underline{H} (\\omega) \\to 0$ quand $\\omega \\to 0$, et $\\underline{H} (\\omega) \\to 1$ quand $\\omega \\to \\infty$, il s'agit donc d'un filtre passe-haut.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "813-2703",
"position": 4,
"duration": 30,
"question": {
"id": "2703",
"question": "Quel type de filtre est r\u00e9alis\u00e9 par un circuit RLC quand on regarde la tension aux bornes de la r\u00e9sistance ?",
"answer": "On utilise un pont diviseur de tension et on trouve directement la fonction de transfert :\n$\\underline{H} (\\omega) = \\frac{R}{R+jL \\omega + \\frac{1}{jC\\omega}} = \\frac{j RC \\omega}{1 + j RC \\omega - LC\\omega^2}$.\n\nOn voit alors que $\\underline{H} (\\omega) \\to 0$ quand $\\omega \\to 0$, et $\\underline{H} (\\omega) \\to 0$ quand $\\omega \\to \\infty$, avec une valeur $\\underline{H} (\\frac{1}{\\sqrt{LC}}) = 1$ il s'agit donc d'un filtre passe-bande.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "813-2704",
"position": 5,
"duration": 30,
"question": {
"id": "2704",
"question": " Comment rep\u00e9rer sur un diagramme de Bode le caract\u00e8re d\u00e9rivateur d'un filtre (en d\u00e9montrant ce r\u00e9sultat) ?\n",
"answer": "Un filtre d\u00e9rivateur est tel que la sortie est proportionnelle \u00e0 la d\u00e9riv\u00e9e de l'entr\u00e9e $s(t) = \\alpha \\frac{de}{dt}$, donc en r\u00e9gime sinuso\u00efdal, sa fonction de transfert complexe est $\\underline{H} (\\omega) = j \\frac{\\omega}{\\omega_0}$ en posant $\\alpha = \\frac{1}{\\omega_0}$.\n\nAinsi, son gain est $G (\\omega) = \\frac{\\omega}{\\omega_0}$, et son gain en d\u00e9cibel est $G_{dB} = 20 \\log_{10} \\left( \\frac{\\omega}{\\omega_0} \\right)$.\n\nOn a de plus $\\phi(\\omega) = \\pi\/2$ pour le d\u00e9phasage.\n\nUn filtre aura donc un comportement d\u00e9rivateur si son diagramme de Bode en gain pr\u00e9sente une pente de + 20dB\/d\u00e9cade, et que sur le diagramme de Bode en phase, son d\u00e9phasage est constant et \u00e9gal \u00e0 $\\pi\/2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "813-2705",
"position": 6,
"duration": 30,
"question": {
"id": "2705",
"question": " Comment rep\u00e9rer sur un diagramme de Bode le caract\u00e8re int\u00e9grateur d'un filtre (en d\u00e9montrant ce r\u00e9sultat) ?",
"answer": "Un filtre int\u00e9grateur est tel que la sortie est proportionnelle \u00e0 l'int\u00e9grale de l'entr\u00e9e $s(t) = \\alpha \\int e(t) dt$, donc en r\u00e9gime sinuso\u00efdal, sa fonction de transfert complexe est $\\underline{H} (\\omega) = \\frac{1}{j \\frac{\\omega}{\\omega_0}}$ en posant $\\alpha = \\omega_0$.\n\nAinsi, son gain est $G (\\omega) = \\frac{\\omega_0}{\\omega}$, et son gain en d\u00e9cibel est $G_{dB} = - 20 \\log_{10} \\left( \\frac{\\omega}{\\omega_0} \\right)$.\n\nOn a de plus $\\phi(\\omega) = - \\pi\/2$ pour le d\u00e9phasage.\n\nUn filtre aura donc un comportement int\u00e9grateur si son digramme de Bode en gain pr\u00e9sente une pente de - 20dB\/d\u00e9cade, et que sur le diagramme de Bode en phase, son d\u00e9phasage est constant et \u00e9gal \u00e0 $- \\pi\/2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"814": {
"id": "814",
"name": "Quizz 20 : Cin\u00e9matique.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/814\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-23",
"questions": [{
"id": "814-2706",
"position": 0,
"duration": 30,
"question": {
"id": "2706",
"question": "Citer deux syst\u00e8mes de coordonn\u00e9es diff\u00e9rents.",
"answer": "On peut citer les syst\u00e8mes de coordonn\u00e9es cart\u00e9siennes, et cylindriques que vous devez savoir utiliser.\nIl existe aussi les coordonn\u00e9es sph\u00e9riques couramment utilis\u00e9es pour les probl\u00e8mes \u00e0 sym\u00e9trie sph\u00e9rique, et de s syst\u00e8mes plus exotiques comme les coordonn\u00e9es ellipso\u00efdales, parabolo\u00efdales, toro\u00efdales, etc avec chacun leurs avantages pour un probl\u00e8me donn\u00e9...)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "814-2707",
"position": 1,
"duration": 30,
"question": {
"id": "2707",
"question": "Exprimer le vecteur-position, le vecteur-vitesse et le vecteur-acc\u00e9l\u00e9ration d'un point en coordonn\u00e9es cart\u00e9siennes.",
"answer": "$\\vec{OM} = x \\vec{u}_x + y \\vec{u}_y + z \\vec{u}_z$\n$\\vec{v} = \\dot{x} \\vec{u}_x + \\dot{y} \\vec{u}_y + \\dot{z} \\vec{u}_z$\n$\\vec{a} = \\ddot{x} \\vec{u}_x + \\ddot{y} \\vec{u}_y  + \\ddot{z} \\vec{u}_z$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "814-2708",
"position": 2,
"duration": 30,
"question": {
"id": "2708",
"question": "Exprimer le vecteur-position, le vecteur-vitesse et le vecteur-acc\u00e9l\u00e9ration d'un point en coordonn\u00e9es cylindriques.",
"answer": "$\\vec{OM} = r \\vec{u}_r + z \\vec{u}_z$\n$\\vec{v} = \\dot{r} \\vec{u}_r + r \\dot{\\theta} \\vec{u}_{\\theta} + \\dot{z} \\vec{u}_z$\n$\\vec{a} = \\left(\\ddot{r} - r\\dot{\\theta}^2 \\right) \\vec{u}_r + \\left( r \\ddot{\\theta} + 2 \\dot{r} \\dot{\\theta} \\right) \\vec{u}_\\theta + \\ddot{z} \\vec{u}_z$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "814-2709",
"position": 3,
"duration": 30,
"question": {
"id": "2709",
"question": "A un instant $t$, un point mat\u00e9riel a une vitesse $\\vec{v}$ et une acc\u00e9l\u00e9ration $\\vec{a}$, que l'on d\u00e9compose en une partie parall\u00e8le \u00e0 la vitesse, et une partie perpendiculaire : $\\vec{a} = a_{\/\/} \\vec{u}_{\/\/} + a_{\\perp} \\vec{u}_{\\perp}$.\nQuel est l'effet sur le vecteur-vitesse de chacune de ces composantes ?",
"answer": "La composante parall\u00e8le a pour effet de modifier la norme du vecteur-vitesse, la composante perpendiculaire modifie sa direction.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "814-2710",
"position": 4,
"duration": 30,
"question": {
"id": "2710",
"question": "Le moteur de fus\u00e9e au d\u00e9collage lui procure une acc\u00e9l\u00e9ration de 14,0 m.s$^{-2}$ pendant 150 secondes. Quelle sont la vitesse et l'altitude atteintes \u00e0 la fin de la pouss\u00e9e ?",
"answer": "On prend comme syst\u00e8me la fus\u00e9e, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre, muni des coordonn\u00e9es cart\u00e9siennes (axe $z$ vertical vers le haut) et avec l'origine des temps au d\u00e9collage.\nL'acc\u00e9l\u00e9ration de la fus\u00e9e est alors $\\vec{a} = a \\vec{u}_z$, donc les coordonn\u00e9es du vecteur-position $(x,y,z)$ v\u00e9rifient $\\ddot{x} = 0$, $\\ddot{y} = 0$ et $\\ddot{z} = a$ avec $a = 14 \\textrm{ m.s}^{-2}$.\n\nEn int\u00e9grant une premi\u00e8re fois, on trouve :\n$\\dot{x} = v_x$\n$\\dot{y} = v_y$\n$\\dot{z} = at + v_z$\no\u00f9 $v_x,v_y,v_z$ sont trois constantes. A l'instant $t=0$, le vecteur-vitesse a alors pour coordonn\u00e9es $(v_x,v_y,v_z)$ or le vecteur-vitesse \u00e0 $t=0$ est nul, on a donc $v_x=v_y=v_z=0$.\nAinsi, le vecteur-vitesse \u00e0 l'instant $t$ a pour expression $\\vec{v} (t) = a t \\vec{u}_z$. En particulier, \u00e0 $t=150$ s, la vitesse est de 2,10 km\/s.\n\nEn int\u00e8grant une seconde fois pour avoir la position, on va devoir introduire \u00e0 nouveau 3 constantes d'int\u00e9gration, correspondant \u00e0 la position initiale de la fus\u00e9e, donc ces trois constantes seront nulles et on a directement :\n$x(t) = y(t) =0$ (attendu, la fus\u00e9e d\u00e9collant \u00e0 la verticale restant donc toujours au-dessus du pas de tir)\n$z(t) = \\frac12 a t^2$.\nEn particulier, pour $t=150$ s on trouve une altitude de 158 km. \n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "814-2711",
"position": 5,
"duration": 30,
"question": {
"id": "2711",
"question": "Quelle doit-\u00eatre la longueur du bras d'une centrifugeuse telle que l'acc\u00e9l\u00e9ration subie par l'astronaute soit de 18 $g$ quand la cabine a une vitesse de 60 m\/s ?",
"answer": "On prend comme syst\u00e8me la cabine, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre muni d'un syst\u00e8me de coordonn\u00e9es cylindriques, l'axe $z$ \u00e9tant l'axe de rotation du bras, de longueur $L$, et l'origine du rep\u00e8re tel que la c\u00f4te $z$ de la cabine soit nulle.\n\nLa position de la cabine est alors $\\vec{OM} = L \\vec{u}_r$. En d\u00e9rivant une premi\u00e8re fois on trouve le vecteur-vitesse de la cabine $\\vec{v} = L \\dot{\\theta} \\vec{u}_\\theta$ (car $\\dot{L} =0$). On en d\u00e9duit que $\\dot{\\theta} = cte$ puisque $v$ et $L$ sont constants et en d\u00e9rivant une seconde fois, on a le vecteur-acc\u00e9l\u00e9ration $\\vec{a} = - L \\dot{\\theta}^2 \\vec{u}_r$.\n\nEn norme, on obtient alors $v = L \\dot{\\theta}$ et $a = L \\dot{\\theta}^2 = \\frac{v^2}{L}$.\nOn d\u00e9duit donc la longueur du bras recherch\u00e9e $L = \\frac{v^2}{a} = 20$ m.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "814-2712",
"position": 6,
"duration": 30,
"question": {
"id": "2712",
"question": "Quel est le temps de chute et la distance horizontale parcourue par un objet l\u00e2ch\u00e9 depuis une altitude de 100 km avec une vitesse initiale verticale de 800 m\/s et une vitesse horizontale de 1,7 km\/s.",
"answer": "On prend comme syst\u00e8me l'objet \u00e9tudi\u00e9, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre avec les coordonn\u00e9es cart\u00e9siennes, l'axe $z$ vertical vers le haut, et l'axe $x$ horizontal dirig\u00e9 le long de la vitesse horizontale lors du l\u00e2cher. L'origine des temps est fix\u00e9e au l\u00e2cher.\n\nOn a alors $\\vec{a} (t) = - g \\vec{u}_z$, mais on ne sait pas calculer directement avec les vecteurs. On projette donc sur chacun des axes, et on obtient les trois \u00e9quations $\\ddot{x} = \\ddot{y} = 0$ et $\\ddot{z} = -g$.\nOn int\u00e8gre deux fois ces trois relations et on trouve $y(t) =0$ , $x(t) = v_h t$ et $z(t) = - \\frac{1}{2} g t^2 + v_v (t) + h_0$.\nLe temps de vol s'obtient en d\u00e9terminant le temps au bout duquel $z(t_v) = 0$, on trouve alors les deux possibilit\u00e9s $t_{1\/2} = \\frac{v_v \\pm \\sqrt{v_v^2 + 2 g h_0}}{g}$, dont on ne retient que la positive $t_v =  \\frac{v_v + \\sqrt{v_v^2 + 2 g h_0}}{g} = 2,0$ min.\nL'objet tombera donc $x(t_v) = 4,1.10^5$ m (environ 400 km) plus loin que le point o\u00f9 il a \u00e9t\u00e9 l\u00e2ch\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"822": {
"id": "822",
"name": "Quizz 22 : M\u00e9canique newtonienne",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/822\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-30",
"questions": [{
"id": "822-2714",
"position": 0,
"duration": 30,
"question": {
"id": "2714",
"question": "Qu'est-ce que la pouss\u00e9e d'Archim\u00e8de ? Comment la calcule t'on ?",
"answer": "La pouss\u00e9e d'Archim\u00e8de est une force due aux diff\u00e9rences de pression d'un fluide caus\u00e9es par la gravit\u00e9.\nCette force est dirig\u00e9e vers le haut, et est d'intensit\u00e9 \u00e9gale au poids du volume de fluide d\u00e9plac\u00e9 : pour un solide dont le volume immerg\u00e9 est $V$ dans un fluide de masse volumique $\\rho$ et dans un champ d epesenteur d'acc\u00e9l\u00e9ration $\\vec{g}$, la pouss\u00e9e d'Archim\u00e8de s'\u00e9crit $\\vec{P}_A = - \\rho V \\vec{g}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "822-2715",
"position": 1,
"duration": 30,
"question": {
"id": "2715",
"question": "Calculer le d\u00e9bit massique $D_m$ d'\u00e9jection des gaz d'un moteur de fus\u00e9e de masse $m = 1400$ tonnes, acc\u00e9l\u00e9rant \u00e0 14,0 m.s$^{-2}$, sachant que la force de pouss\u00e9e s'\u00e9crit $\\vec{F}_p = - D_m \\vec{v}_e$, avec $\\vec{v}_e$ la vitesse d'\u00e9jection des gaz, de norme $v_e = 4,0$ km\/s.",
"answer": "On prend comme syst\u00e8me la fus\u00e9e, \u00e0 laquelle on applique le PFD dans le r\u00e9f\u00e9rentiel terrestre, suppos\u00e9 galil\u00e9en.\nLes forces appliqu\u00e9es \u00e0 la fus\u00e9e sont la pouss\u00e9e du moteur et son poids $\\vec{P}$, et on trouve $m \\vec{a} = \\vec{F}_p + \\vec{P}$.\n\nOn projette alors le long de l'axe vertical dirig\u00e9 vers le haut et on obtient $m a = D_m v_e - m g$, donc le d\u00e9bit massique des gaz s'\u00e9crit comme :\n$D_m = \\frac{m( a+ g)}{v_e} = 8,4.10^3$ kg\/s.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "822-2716",
"position": 2,
"duration": 30,
"question": {
"id": "2716",
"question": "Lors de frottements entre deux solides, quelle est la relation math\u00e9matique entre la composante tangentielle \u00e0 la surface de contact $T$ et la composante normale $N$ de la force exerc\u00e9e en cas de glissement ? En cas de non-glissement ?",
"answer": "Si on appelle $\\mu$ le coefficient de frottement, en cas de glissement $T = \\mu N$, en cas de non-glissement $T \\leq \\mu N$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "822-2721",
"position": 3,
"duration": 30,
"question": {
"id": "2721",
"question": "Pour un solide se d\u00e9pla\u00e7ant \u00e0 la vitesse $\\vec{v}$ dans un fluide, donner l'expression de la force exerc\u00e9e par le fluide dans le cas de frottements de type fluide visqueux et dans le cas d(un \u00e9coulement turbulent.",
"answer": "Fluide visqueux : $\\vec{F} = - \\alpha \\vec{v}$\nEcoulement turbulent : $\\vec{F} = - \\beta v \\vec{v}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "822-2722",
"position": 4,
"duration": 30,
"question": {
"id": "2722",
"question": "D\u00e9terminer les \u00e9quations horaires du mouvement d'un ballon de basket-ball lors d'un lancer-franc.\nEn d\u00e9duire l'\u00e9quation de la trajectoire, et sa nature.",
"answer": "On prend comme syst\u00e8me le ballon, dans le r\u00e9f\u00e9rentiel terrestre suppos\u00e9 galil\u00e9en. L'axe $x$ est pris comme l'axe le long du quel se fait le lancer, $y$ l'axe vertical vers le haut. L'origine de l'espace est prise \u00e0 la ligne de lancer-franc et l'origine des temps au moment du lancer.\n\nLa seule force \u00e0 consid\u00e9rer est le poids d'expression $\\vec{P} = - m g \\vec{u}_y$ avec $m$ la masse du ballon.\nOn applique le PFD et on obtient $\\vec{a} = - g \\vec{u}_y$, d'o\u00f9 l'on d\u00e9duit les trois \u00e9quations $\\ddot{x} =0$, $\\ddot{y} = - g$ et $\\ddot{z} =0$.\n\nOn int\u00e8gre deux fois et avec les conditions initiales $v_x (t=0) = v_{x,0}$, $v_y (t=0) = v_{y,0}$, $v_z (t=0) = 0$, $x (t=0) = 0$, $y (t=0) = y_0$ et $z (t=0) = 0$ on obtient les \u00e9quations horaires du mouvement :\n$x(t) = v_{x,0} t$\n$y (t) = - \\frac12 gt^2 + v_{y,0} t + y_0$\n$z(t) = 0$\n\nLa trajectoire est alors donn\u00e9e par :\n$y(x) = - \\frac12 g \\left( \\frac{x}{v_{x,0}} \\right)^2 + \\frac{v_{y,0}}{v_{x,0}} x + y_0$\nOn reconnait un polyn\u00f4me du second degr\u00e9, la trajectoire est donc une parabole.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "822-2724",
"position": 5,
"duration": 30,
"question": {
"id": "2724",
"question": "Etablir l'\u00e9quation diff\u00e9rentielle r\u00e9gissant le mouvement d'un pendule simple.\nLa mettre sous la forme de l'\u00e9quation d'un oscillateur harmonique en effectuant l'approximation des petits angles.",
"answer": "On prend comme syst\u00e8me la masse, comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre (galil\u00e9en), muni d'un syst\u00e8me de coordonn\u00e9es cylindriques, ayant comme axe $z$ l'axe de rotation du pendule.\nSi on appelle $L$ la longueur du fil (inextensible) du pendule, alors le vecteur-position du pendule est $\\vec{OM} = L \\vec{u}_r$, et son vecteur-acc\u00e9l\u00e9ration est $\\vec{a} = - L \\dot{\\theta}^2 \\vec{u}_r + L \\ddot{\\theta} \\vec{u}_\\theta$.\n\nLes forces qui s'exercent sur le syst\u00e8me son le poids $\\vec{P} = m \\vec{g} = mg \\left( \\cos \\theta \\vec{u}_r - \\sin(\\theta) \\vec{u}_\\theta \\right)$ et la tension du fil $\\vec{T} = - T \\vec{u}_r$.\n\nOn applique alors le PFD au syst\u00e8me, et on projette sur $\\vec{u}_\\theta$, on obtient alors :\n$m L \\ddot{\\theta} = - mg \\sin \\theta .$\nOn en d\u00e9duit l'\u00e9quation diff\u00e9rentielle suivie par le pendule simple :\n$$ L \\ddot{\\theta} + g \\sin \\theta =0.$$\n\nDans l'approximation des petites angles $\\sin \\theta \\simeq \\theta$, donc l'\u00e9quation diff\u00e9rentielle devient $ L \\ddot{\\theta} + g \\theta =0$, qui se met sous la forme :\n$$ \\frac{d^2 \\theta}{dt^2} + \\omega_0^2 \\theta =0, $$\nen posant $\\omega_0 = \\sqrt{\\frac{g}{L}}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "822-2725",
"position": 6,
"duration": 30,
"question": {
"id": "2725",
"question": "Comment d\u00e9finit-on un r\u00e9f\u00e9rentiel galil\u00e9en ?\nSi on vous donne un r\u00e9f\u00e9rentiel galil\u00e9en $\\mathcal{R}$, \u00e0 quelle condition un r\u00e9f\u00e9rentiel $\\mathcal{R'}$ peut-il \u00eatre consid\u00e9r\u00e9 comme galil\u00e9en ?",
"answer": "Un r\u00e9f\u00e9rentiel galil\u00e9en est un r\u00e9f\u00e9rentiel dans lequel un syst\u00e8me isol\u00e9 (ou pseudo-isol\u00e9) a un mouvement de translation rectiligne uniforme.\n\n$\\mathcal{R'}$ sera galil\u00e9en si et seulement s'il est en translation rectiligne uniforme par rapport \u00e0 $\\mathcal{R}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"826": {
"id": "826",
"name": "Quizz 23 : Approche \u00e9nerg\u00e9tique",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/826\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-06",
"questions": [{
"id": "826-2726",
"position": 0,
"duration": 30,
"question": {
"id": "2726",
"question": "D\u00e9finir la puissance et le travail d'une force $\\vec{F}$.",
"answer": "La puissance d'une force $\\vec{F}$ appliqu\u00e9 \u00e0 un syst\u00e8me se d\u00e9pla\u00e7ant \u00e0 la vitesse $\\vec{v}$ est $\\mathcal{P} = \\vec{F}.\\vec{v}$.\n\nLe travail d'une force entre deux instants $t_A$ et $t_B$ est l'int\u00e9grale de la puissance : $W = \\int_{t_A}^{t_B} \\vec{F}.\\vec{v} dt$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2727",
"position": 1,
"duration": 30,
"question": {
"id": "2727",
"question": "Donner l'expression du travail d'une force entre le point $A$ \u00e0 $t_A$ et le point $B$ en $t_B$ dans les deux cas suivants :\n- force constante ,\n- force toujours perpendiculaire \u00e0 la vitesse.",
"answer": "Force constante :\n$ W = \\int_{t_A}^{t_B} \\vec{F}.\\vec{v} dt = \\vec{F} . \\left( \\int_{t_A}^{t_B} \\vec{v} dt \\right) = \\vec{F}.\\vec{AB}$\n\nForce perpendiculaire : $\\vec{F}.\\vec{v} =0$, donc $W =0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2728",
"position": 2,
"duration": 30,
"question": {
"id": "2728",
"question": "Enoncer le th\u00e9or\u00e8me de la puissance cin\u00e9tique et le th\u00e9or\u00e8me de l'\u00e9nergie cin\u00e9tique.",
"answer": "Le th\u00e9or\u00e8me de la puissance cin\u00e9tique stipule que dans un r\u00e9f\u00e9rentiel gali\u00e9len, la puissance cin\u00e9tique d'un syst\u00e8me (la d\u00e9riv\u00e9e de son \u00e9nergie cin\u00e9tique par rapport au temps) est \u00e9gale \u00e0 la somme des puissances des forces appliqu\u00e9es :\n$$\\mathcal{P}_{cin} = \\frac{dE_c}{dt} = \\sum_i \\mathcal{P}_i =\\sum_i \\vec{f}_i.\\vec{v} .$$\n\nLe th\u00e9or\u00e8me de l'\u00e9nergie cin\u00e9tique est l'int\u00e9grale du th\u00e9or\u00e8me de la puissance cin\u00e9tique : il stipule que la variation d'\u00e9nergie cin\u00e9tique d'un syst\u00e8me entre deux instants, dans un r\u00e9f\u00e9rentiel galil\u00e9en, est \u00e9gale \u00e0 la somme des travaux des forces appliqu\u00e9es :\n$$ \\Delta E_c = E_{c,2} - E_{c,1} = \\sum_i W_i .$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2729",
"position": 3,
"duration": 30,
"question": {
"id": "2729",
"question": "Qu'est-ce qu'une force conservative ? \nDonner un exemple de force conservative et un de force non-conservative.",
"answer": "C'est une force dont le travail entre deux points ne d\u00e9pend pas du chemin suivi.\nOn peut citer le poids, la force de rappel d'un ressort ou une force \u00e9lectrostatique comme forces conservatives, et les frottements comme force non-conservative.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2730",
"position": 4,
"duration": 30,
"question": {
"id": "2730",
"question": "D\u00e9finir une \u00e9nergie potentielle. \nDonner la valeur de l'\u00e9nergie potentielle de pesanteur et l'\u00e9nergie potentielle \u00e9lastique d'un ressort.",
"answer": "L'\u00e9nergie potentielle en un point $M$ d'une force est d\u00e9finie $\\textbf{pour une force conservative}$ comme l'oppos\u00e9 du travail de cette force entre une origine arbitraire $O$ et le point $M$ : $E_p(M) = E_p (O) - W_{O \\to M}$.\n\nPour le poids, on a $E_p (M) = m g h$ avec $h$ l'altitude du point $M$ (l'origine \u00e9tant prise en $O$).\n\nPour le ressort, si sa longueur est $l$, sa constante de raideur est $k$ et sa longueur \u00e0 vide $l_0$, et que l'on prend comme origine la position o\u00f9 l'allongement $l-l_0$ est nul, on a  $E_p (l) = \\frac12 k (l - l_0)^2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "826-2731",
"position": 5,
"duration": 30,
"question": {
"id": "2731",
"question": "D\u00e9finir l'\u00e9nergie m\u00e9canique d'un syst\u00e8me.\nCiter la loi de l'\u00e9nergie m\u00e9canique, et l'appliquer dans le cas de forces uniquement conservatives.",
"answer": "L'\u00e9nergie m\u00e9canique d'un syst\u00e8me est la somme de son \u00e9nergie cin\u00e9tique et de toutes les \u00e9nergies potentielles des forces qui lui sont appliqu\u00e9es.\n\nLa variation d'\u00e9nergie m\u00e9canique entre deux instants est \u00e9gale au travail de toutes les forces qui ne sont pas conservatives : $\\Delta E_m = \\sum_{i \\in n.c.} W_i$.\nDans le cas de forces uniquement conservatives, $\\Delta E_m = 0$ : l'\u00e9nergie m\u00e9canique est conserv\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "826-2732",
"position": 6,
"duration": 30,
"question": {
"id": "2732",
"question": "En n\u00e9gligeant les frottements, appliquer le th\u00e9or\u00e8me de l'\u00e9nergie m\u00e9canique pour d\u00e9terminer l'altitude $h$ atteinte par un projectile lanc\u00e9 verticalement depuis le sol avec une vitesse $v_0$.",
"answer": "On prend comme syst\u00e8me le projectile, et comme r\u00e9f\u00e9rentiel le r\u00e9f\u00e9rentiel terrestre consid\u00e9r\u00e9 galil\u00e9en. On va appliquer le th\u00e9or\u00e8me de l'\u00e9nergie m\u00e9canique au syst\u00e8me entre le moment du lancer (1) et le moment o\u00f9 l'altitude est maximale (2).\n\nLa seule force qui s'exerce sur le projectile est le poids, c'est une force conservative, donc l'\u00e9nergie m\u00e9canique est conserv\u00e9e $E_{m,1} = E_{m,2}$.\n\nAu moment du lancer $E_{m,1} = E_{c,1} + E_{p,1} = \\frac12 mv_0^2 + 0$.\nA l'apog\u00e9e de la trajectoire $E_{m,2} = E_{c,2} + E_{p,2} = 0 + mgh$.\n\nOn en d\u00e9duit donc $\\frac12 m v_0^2 = mg h$ d'o\u00f9 $h = \\frac{v_0^2}{2g}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "826-2733",
"position": 7,
"duration": 30,
"question": {
"id": "2733",
"question": "Exprimer l'\u00e9nergie potentielle du pendule simple (avec une tige rigide de longueur $L$) en fonction de l'angle $\\theta$.",
"answer": "On prend comme origine le point d'altitude minimale, quand $\\theta =0$.\nL'altitude de la masse quand la tige fait un angle $\\theta$ est alors $h(\\theta) = L (1 - \\cos \\theta)$.\n\nOn a donc :\n$$ E_{p} (\\theta) = m g L (1 - \\cos \\theta) .$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2734",
"position": 8,
"duration": 30,
"question": {
"id": "2734",
"question": "Sachant que l'\u00e9nergie potentielle du pendule simple s'exprime en fonction de $\\theta$ comme $E_p(\\theta) = m g L (1 - \\cos \\theta)$, retrouver l'\u00e9quation diff\u00e9rentielle r\u00e9gissant le mouvement du pendule.",
"answer": "L'\u00e9nergie cin\u00e9tique du pendule simple est $E_c = \\frac12 m L^2 \\dot(\\theta)^2$.\n\nL'\u00e9nergie m\u00e9canique est donc $E_m (\\theta) = \\frac12 m L^2 \\dot{\\theta}^2 + m g L (1 -\\cos \\theta)$.\n\nL'\u00e9nergie m\u00e9canique est conserv\u00e9e donc $\\frac{dE_m}{dt} = 0$, on en d\u00e9duit donc :\n$m L ^2 \\ddot{\\theta}  \\dot{\\theta} + m g L \\dot{\\theta} \\sin \\theta = 0$ et on retrouve l'\u00e9quation du pendule simple en divisant par $ m L \\dot{\\theta}$ :\n$$ L \\ddot{\\theta} + g \\sin \\theta = 0.$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "826-2735",
"position": 9,
"duration": 30,
"question": {
"id": "2735",
"question": "Donner la d\u00e9finition d'une position d'\u00e9quilibre.\nComment d\u00e9finit-on une position d'\u00e9quilibre stable ou instable ?",
"answer": "Une position d'\u00e9quilibre est une position telle qu'un syst\u00e8me m\u00e9canique l\u00e2ch\u00e9 sans vitesse initiale dans cette position y reste ind\u00e9finiment.\n\nPour d\u00e9terminer la stabilit\u00e9 d'une position d'\u00e9quilibre on regarde si le syst\u00e8me m\u00e9canique se rapproche ou s'\u00e9loigne de la position d'\u00e9quilibre lorsqu'il est l\u00e2ch\u00e9 \u00e0 proximit\u00e9 : s'il se rapproche la position d'\u00e9quilibre est stable, s'il s'\u00e9loigne, elle est instable.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "826-2736",
"position": 10,
"duration": 30,
"question": {
"id": "2736",
"question": "Pour un syst\u00e8me m\u00e9canique unidimensionnel conservatif, caract\u00e9ris\u00e9 par l'\u00e9nergie potentielle $E_p(x)$, comment d\u00e9termine t'on les positions d'\u00e9quilibre ?\nComment faire pour d\u00e9terminer si une position d'\u00e9quilibre est stable ?",
"answer": "Les position s'\u00e9quilibre correspondent \u00e0 des extrema de la fonction $E_p (x)$, il faut donc chercher les valeurs o\u00f9 la d\u00e9riv\u00e9e s'annulle : $\\frac{dE_p}{dx} =0$.\n\nPour d\u00e9terminer la stabilit\u00e9 d'une position d'\u00e9quilibre $x_0$ telle que $\\frac{dE_p}{dx} (x=x_0) =0$, il faut calculer la d\u00e9riv\u00e9e seconde de $E_p$ en $x_0$ :\n- si $\\frac{d^2E_p}{dx^2} (x =x_0) > 0$, la position d'\u00e9quilibre est stable ;\n- si $\\frac{d^2E_p}{dx^2} (x =x_0) < 0$, la position d'\u00e9quilibre est instable.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"831": {
"id": "831",
"name": "Quizz 24 : Solide en rotation",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/831\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 270,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-13",
"questions": [{
"id": "831-2737",
"position": 0,
"duration": 30,
"question": {
"id": "2737",
"question": "D\u00e9finir le moment d'une force $\\vec{F}$ par rapport \u00e0 un axe fixe $\\Delta$.",
"answer": "Il faut calculer la distance $d$ entre la direction de la force et l'axe $\\Delta$, aussi appel\u00e9 bras de levier.\nIl faut ensuite ne garder que la composante de $\\vec{F}$ perpendiculaire \u00e0 l'axe de rotation, $F_\\perp$.\nLe moment de cette force est alors $\\mathcal{M}_\\Delta (\\vec{F}) = \\pm F_\\perp d$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "831-2738",
"position": 1,
"duration": 30,
"question": {
"id": "2738",
"question": "Quel est le moment cin\u00e9tique d'un solide en rotation \u00e0 la vitesse angulaire $\\omega$ autour d'un axe fixe $\\Delta$, sachant que le moment d'inertie du solide autour de cet axe est $J_\\Delta$.",
"answer": "$L_\\Delta = J_\\Delta \\omega$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2739",
"position": 2,
"duration": 30,
"question": {
"id": "2739",
"question": "Comment d\u00e9terminer si un solide est en translation ?",
"answer": "Tous les points du solide ont \u00e0 chaque instant le m\u00eame vecteur-vitesse.\nLes trajectoires de tous les points du solide sont superposables (s'obtiennent les unes des autres par translation).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2740",
"position": 3,
"duration": 30,
"question": {
"id": "2740",
"question": "Comment d\u00e9terminer si un solide est en rotation autour d'un axe fixe ?",
"answer": "Toutes les trajectoires d'un point du solide sont des arcs de cercles de m\u00eame centre.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2741",
"position": 4,
"duration": 30,
"question": {
"id": "2741",
"question": "Qu'est-ce qu'un couple de forces ?",
"answer": "C'est un ensemble de forces dont la r\u00e9sultante est nulle $\\sum_i \\vec{f}_i = \\vec{0}$ mais dont la somme des moments est non-nulle $\\sum_i \\mathcal{M}_{\\Delta,i} \\neq 0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2742",
"position": 5,
"duration": 30,
"question": {
"id": "2742",
"question": "Quelle est l'\u00e9nergie cin\u00e9tique d'un solide en rotation \u00e0 la vitesse $\\omega$ autour d'un axe fixe $\\Delta$ sachant que le moment d'inertie du solide par rapport \u00e0 cet axe est $J_\\Delta$ ?",
"answer": "$E_c = \\frac12 J_\\Delta \\omega^2$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2743",
"position": 6,
"duration": 30,
"question": {
"id": "2743",
"question": "Quelle est la puissance d'une force appliqu\u00e9e sur un solide en rotation \u00e0 la vitesse $\\omega$ autour d'un axe fixe $\\Delta$ ?",
"answer": "Si on appelle $\\mathcal{M}_\\Delta (\\vec{F})$ le moment de cette force par rapport \u00e0 $\\Delta$, la puissance de cette force est : $\\mathcal{P}_{\\vec{F}} = \\mathcal{M}_\\Delta (\\vec{F}) \\omega$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "831-2744",
"position": 7,
"duration": 30,
"question": {
"id": "2744",
"question": "Enoncer le th\u00e9or\u00e8me du moment cin\u00e9tique pour un solide en rotation autour d'un axe fixe $\\Delta$.",
"answer": "Le th\u00e9or\u00e8me du moment cin\u00e9tique dit que la d\u00e9riv\u00e9e par rapport au temps du moment cin\u00e9tique d'un solide en rotation autour d'un axe fixe est, dans un r\u00e9f\u00e9rentiel galil\u00e9en, \u00e9gal \u00e0 la somme des moments des forces appliqu\u00e9es par rapport \u00e0 cet axe :\n$$ \\frac{d L_\\Delta}{dt} = \\sum_i \\mathcal{M}_{\\Delta,i} .$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "831-2745",
"position": 8,
"duration": 30,
"question": {
"id": "2745",
"question": "Enoncer le th\u00e9or\u00e8me de la puissance cin\u00e9tique pour un solide en rotation autour d'un axe fixe $\\Delta$.",
"answer": "Le th\u00e9or\u00e8me de la puissance cin\u00e9tique stipule que pour un solide en rotation autour d'un axe fixe $\\Delta$ dans un r\u00e9f\u00e9rentiel galil\u00e9en, la puissance cin\u00e9tique est \u00e9gale \u00e0 la somme des puissances des forces appliqu\u00e9es :\n$P_{cin} = \\frac{dE_c}{dt} = \\sum_i \\mathcal{P}_i.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"760": {
"id": "760",
"name": "Quizz 03 : Lentilles minces",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/760\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "118",
"value": "Optique",
"field_id": "23",
"created_at": "2017-08-21 12:30:19",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 450,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-23",
"questions": [{
"id": "760-2587",
"position": 0,
"duration": 30,
"question": {
"id": "2587",
"question": "Quelles sont les hypoth\u00e8ses de travail de l'optique g\u00e9om\u00e9trique ?",
"answer": "- Les rayons lumineux se propagent en ligne droite dans les milieux homog\u00e8nes ;\n- les rayons lumineux n'interagissent pas entre eux ;\n- principe du retour inverse de la lumi\u00e8re (si un rayon va de A \u00e0 B, il peut aussi aller de B \u00e0 A en suivant le m\u00eame chemin)\n- les objets sont suffisamment grands par rapport \u00e0 la longueur d'onde de la lumi\u00e8re utilis\u00e9e pour ne pas avoir de diffraction.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2588",
"position": 1,
"duration": 30,
"question": {
"id": "2588",
"question": "Dans la cadre d'une exp\u00e9rience de diffraction, donner la relation entre la largeur de l'ouverture $D$, la longueur d'onde $\\lambda$ et le demi angle d'ouverure $\\theta$.",
"answer": "$\\theta \\simeq \\frac{\\lambda}{D}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2589",
"position": 2,
"duration": 30,
"question": {
"id": "2589",
"question": "Citer les trois lois de Snell-Descartes pour un dioptre.",
"answer": "Lors de l'arriv\u00e9e d'un rayon lumineux sur un dioptre :\n- les rayons r\u00e9fl\u00e9chi et r\u00e9fract\u00e9 sont situ\u00e9s dans le plan d'incidence ;\n- l'angle de r\u00e9flexion est \u00e9gal et oppos\u00e9 \u00e0 l'angle d'incidence ;\n- l'angle de r\u00e9fraction $i_2$ et l'angle d'incidence $i_1$ sont li\u00e9s par la relation $n_1 \\sin i_1 = n_2 \\sin i_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2590",
"position": 3,
"duration": 30,
"question": {
"id": "2590",
"question": "Donner la d\u00e9finition de l'angle limite de r\u00e9flexion totale et sa valeur pour un dioptre s\u00e9parant deux milieux d'indices optiques $n_1$ et $n_2$.",
"answer": "L'angle limite de r\u00e9flexion totale est la valeur de l'angle d'incidence \u00e0 partir de laquelle il n'est plus possible d'observer un rayon r\u00e9fract\u00e9 dans le milieu d'indice $n_2 < n_1$.\n\nPour pouvoir observer un rayon r\u00e9fract\u00e9 avec un angle de r\u00e9fraction $i_2$, on doit pouvoir avoir $n_1 \\sin i_1 = n_2 \\sin i_2$, donc $\\frac{n_1}{n_2} \\sin i_1 = \\sin i_2 \\leq 1$.\nOn trouve donc l'angle limite de r\u00e9flexion totale $i_{lim}$ tel que $\\sin i_{lim} = \\frac{n_2}{n_1}$ ou $i_{lim} = \\textrm{Arcsin} \\frac{n_2}{n_1}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "760-2591",
"position": 4,
"duration": 30,
"question": {
"id": "2591",
"question": "En optique, quelle est la d\u00e9finition d'une image r\u00e9elle ? d'une image virtuelle ?",
"answer": "Une image r\u00e9elle se forme apr\u00e8s la face de sortie du syst\u00e8me optique, une image virtuelle se forme avant.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2592",
"position": 5,
"duration": 30,
"question": {
"id": "2592",
"question": "En optique, quelle est la d\u00e9finition d'un objet r\u00e9el ? d'un objet virtuel ?",
"answer": "Un objet r\u00e9el est situ\u00e9 avant la face d'entr\u00e9e du syst\u00e8me optique, un objet virtuel est situ\u00e9 apr\u00e8s.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2593",
"position": 6,
"duration": 30,
"question": {
"id": "2593",
"question": "Quelle est la d\u00e9finition d'un syst\u00e8me optique stigmatique ? Aplan\u00e9tique ?",
"answer": "L'image d'un point par un syst\u00e8me optique stigmatique est un point.\nL'image d'un objet perpendiculaire \u00e0 l'axe optique par un syst\u00e8me aplan\u00e9tique est perpendiculaire \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "760-2594",
"position": 7,
"duration": 30,
"question": {
"id": "2594",
"question": "Enoncer les conditions de Gauss.\nQuel est leur int\u00e9r\u00eat pour les lentilles minces ?",
"answer": "Pour \u00eatre dans les conditions de Gauss, on ne consid\u00e8re que des rayons lumineux proches de l'axe optique et faiblement inclin\u00e9s par rapport \u00e0 l'axe optique.\n\nDans les conditions de Gauss, une lentille mince est stigmatique et aplan\u00e9tique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2595",
"position": 8,
"duration": 30,
"question": {
"id": "2595",
"question": "Donner la d\u00e9finition du foyer objet et du foyer image d'une lentille mince.",
"answer": "Le foyer objet est le point par lequel passent tous les rayons incidents qui sortent parall\u00e8les \u00e0 l'axe optique.\nLe foyer image est le point par lequel passent tous les rayons (apr\u00e8s travers\u00e9e de la lentille) qui arrivaient parall\u00e8les \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2596",
"position": 9,
"duration": 30,
"question": {
"id": "2596",
"question": "O\u00f9 est situ\u00e9 l'image \u00e0 travers une lentille mince d'un objet ponctuel situ\u00e9 \u00e0 l'infini ?",
"answer": "Elle est situ\u00e9e dans le plan focal image.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2597",
"position": 10,
"duration": 30,
"question": {
"id": "2597",
"question": "O\u00f9 est situ\u00e9e l'image d'un objet ponctuel situ\u00e9 dans le plan focal objet ?",
"answer": "Elle est situ\u00e9e \u00e0 l'infini.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2598",
"position": 11,
"duration": 30,
"question": {
"id": "2598",
"question": "On appelle $A'$ l'image du point $A$ par une lentille mince de centre $O$. Comment s'appelle $\\gamma = \\frac{\\overline{OA'}}{\\overline{OA}}$ ?\nQue peut-on dire si $\\gamma <0 $ ?\net si $\\vert \\gamma \\vert > 1$ ?",
"answer": "$\\gamma$ s'appelle le grandissement.\nSi $\\gamma < 0$, l'image est renvers\u00e9e par rapport \u00e0 l'objet.\nSi $\\vert \\gamma \\vert > 1$, l'image est plus grande que l'objet.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2986",
"position": 12,
"duration": 30,
"question": {
"id": "2986",
"question": "Que peut-on dire du rayon \u00e9mergent d'une lentille mince correspondant \u00e0 un rayon incident passant par son centre optique ?",
"answer": "Il n'est pas d\u00e9vi\u00e9 en traversant la lentille.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2987",
"position": 13,
"duration": 30,
"question": {
"id": "2987",
"question": "Que peut-on dire du rayon incident d'une lentille mince correspondant \u00e0 un rayon \u00e9mergent passant par son foyer image ?",
"answer": "Il arrive parall\u00e8le \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "760-2988",
"position": 14,
"duration": 30,
"question": {
"id": "2988",
"question": "Que peut-on dire du rayon \u00e9mergent d'une lentille mince correspondant \u00e0 un rayon incident passant par son foyer objet ?",
"answer": "Il ressort parall\u00e8le \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"798": {
"id": "798",
"name": "Quizz 14 : Cin\u00e9tique chimique.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/798\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-12",
"questions": [{
"id": "798-2665",
"position": 0,
"duration": 30,
"question": {
"id": "2665",
"question": "Pour la r\u00e9action de combustion du m\u00e9thane $CH_4 + 2 O_2 = CO_2 + 2 H_2O$, donner en fonction des concentrations des esp\u00e8ces chimiques l'expression :\n- de la vitesse de formation des produits ;\n- de la vitesse de disparition des r\u00e9actifs ;\n- de la vitesse de r\u00e9action.\n\nExprimer la vitesse de r\u00e9action en fonction des 4 vitesses de formation ou de disparition.\n",
"answer": "On a :\n- $v_{CO_2} = \\frac{d[CO_2]}{dt}$ et $v_{H_2O} = \\frac{d[H_2O]}{dt}$ ;\n- $v_{CH_4} = - \\frac{d[CH_4]}{dt}$ et $v_{O_2} = - \\frac{d[O_2]}{dt}$ ;\n- $v = -\\frac{d[CH_4]}{dt} = - \\frac12 \\frac{d[O_2]}{dt} = \\frac{d[CO_2]}{dt} = \\frac12 \\frac{d[H_2O]}{dt}$\n- $v = v_{CH_4} = \\frac12 v_{O_2} = v_{CO_2} = \\frac12 v_{H_2O}$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-2666",
"position": 1,
"duration": 30,
"question": {
"id": "2666",
"question": "En quelle unit\u00e9 SI s'exprime une vitesse de r\u00e9action chimique ?",
"answer": "Elle s'exprime en mol.L$^{-1}$.s$^{-1}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-2667",
"position": 2,
"duration": 30,
"question": {
"id": "2667",
"question": "Citer deux param\u00e8tres qui influencent une vitesse de r\u00e9action.",
"answer": "On peut citer la temp\u00e9rature, la concentration des esp\u00e8ces chimiques (en solution), les pressions (en phase gazeuse), la surface de contact (en phase solide), etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-2668",
"position": 3,
"duration": 30,
"question": {
"id": "2668",
"question": "Que peut-on dire sur la vitesse de r\u00e9action si la r\u00e9action $\\alpha A + \\beta B = \\gamma C + \\delta D$ admet un ordre ?",
"answer": "Si cette r\u00e9action admet un ordre, alors sa vitesse de r\u00e9action s'\u00e9crit sous la forme $v= k [A]^{n_A} [B]^{n_B}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-2669",
"position": 4,
"duration": 30,
"question": {
"id": "2669",
"question": "La r\u00e9action $CO + Cl_2 = COCl_2$ a pour vitesse de r\u00e9action $v = k [CO] [Cl_2]^{3\/2}$.\nComment s'appelle et quelle est l'unit\u00e9 de $k$ ?\nQue vaut l'ordre global de cette r\u00e9action ?",
"answer": "$k$ est la constante de vitesse.\nPour cette r\u00e9action, $k$ s'exprime en mol$^{-3\/2}$.L$^{3\/2}$.s$^{-1}$.\nL'ordre global de cette r\u00e9action est 5\/2.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-2670",
"position": 5,
"duration": 30,
"question": {
"id": "2670",
"question": "On souhaite \u00e9tudier la cin\u00e9tique de la r\u00e9action $CO + Cl_2 = COCl_2$, dont on sait qu'elle admet un ordre : $v = k [CO]^\\alpha [Cl_2]^\\beta$.\nD\u00e9crire les deux m\u00e9thodes permettant d'exprimer la vitesse de la r\u00e9action en fonction de la seule concentration en $Cl_2$, et qui permet donc de faciliter l'\u00e9tude. Pr\u00e9ciser pour chaque m\u00e9thode quelle grandeur peut-\u00eatre calcul\u00e9e.",
"answer": "Premi\u00e8re m\u00e9thode :on se place dans les conditions st\u0153chiom\u00e9triques, donc telles qu'\u00e0 tout instant $[CO]=[Cl_2]$. On peut alors \u00e9crire $v = k [CO]^\\alpha [Cl_2]^\\beta = k [Cl_2]^{\\alpha+\\beta}$. On peut donc d\u00e9terminer $\\alpha+\\beta$, c'est-\u00e0-dire l'ordre global de la r\u00e9action.\n\nDeuxi\u00e8me m\u00e9thode (m\u00e9thode de la d\u00e9g\u00e9n\u00e9rescence de l'ordre) : on introduit $CO$ en grand exc\u00e8s, donc $[CO] \\simeq [CO]_0$. On a donc $v = k [CO]^\\alpha [Cl_2]^\\beta \\simeq k' [Cl_2]^\\beta$ en posant $k' = k [CO]_0^\\alpha$. On peut avec cette m\u00e9thode d\u00e9terminer $\\beta$, l'ordre partiel de la r\u00e9action par rapport \u00e0 $Cl_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "798-2671",
"position": 6,
"duration": 30,
"question": {
"id": "2671",
"question": "On consid\u00e8re la r\u00e9action $A = B + C$, d'ordre 0.\nComment s'exprime alors la vitesse de r\u00e9action ? Quelle est l'unit\u00e9 de la constante de r\u00e9action ?\nQue vaut $[A](t)$ ? Quelle fonction de $[A](t)$ est une fonction affine du temps ?\nQue vaut le temps de demi-r\u00e9action en fonction de $[A](t=0)$ ?",
"answer": "On peut \u00e9crire $v = k [A]^0 = k$.\n$k$ s'exprime alors en mol.L$^{-1}$.s$^{-1}$.\nLa vitesse de r\u00e9action s'\u00e9crit en fonction de la vitesse de disparition de $A$ comme $v = - \\frac{d[A]}{dt}$, on a donc $\\frac{d[A]}{dt} = - k$, donc en int\u00e9grant on trouve :\n$[A](t) = [A] (t=0) - k t$\n$[A](t)$ est donc une fonction affine du temps.\nLe temps de demi-r\u00e9action est alors $t_{1\/2} = \\frac{[A](t=0)}{2 k}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "798-2672",
"position": 7,
"duration": 30,
"question": {
"id": "2672",
"question": "On consid\u00e8re la r\u00e9action $A = B + C$, d'ordre 1.\nComment s'exprime alors la vitesse de r\u00e9action ? Quelle est l'unit\u00e9 de la constante de r\u00e9action ?\nQue vaut $[A](t)$ ? Quelle fonction de $[A](t)$ est une fonction affine du temps ?\nQue vaut le temps de demi-r\u00e9action en fonction de $[A](t=0)$ ?",
"answer": "On peut \u00e9crire $v = k [A]^1 = k [A](t)$.\n$k$ s'exprime alors en s$^{-1}$.\nLa vitesse de r\u00e9action s'\u00e9crit en fonction de la vitesse de disparition de $A$ comme $v = - \\frac{d[A]}{dt}$, on a donc $\\frac{d[A]}{dt} = - k [A](t)$, donc en r\u00e9solvant cette \u00e9quation diff\u00e9rentielle du premier ordre on trouve :\n$[A](t) = [A] (t=0) e^{-kt}$\n$\\ln([A](t))$ est donc une fonction affine du temps.\nLe temps de demi-r\u00e9action est alors $t_{1\/2} = \\frac{\\ln(2)}{k}$, ind\u00e9pendant de $[A](t=0)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "798-2673",
"position": 8,
"duration": 30,
"question": {
"id": "2673",
"question": "On consid\u00e8re la r\u00e9action $A = B + C$, d'ordre 2.\nComment s'exprime alors la vitesse de r\u00e9action ? Quelle est l'unit\u00e9 de la constante de r\u00e9action ?\nQue vaut $[A](t)$ ? Quelle fonction de $[A](t)$ est une fonction affine du temps ?\nQue vaut le temps de demi-r\u00e9action en fonction de $[A](t=0)$ ?",
"answer": "On peut \u00e9crire $v = k [A]^2$.\n$k$ s'exprime alors en mol$^{-1}$.L.s$^{-1}$.\nLa vitesse de r\u00e9action s'\u00e9crit en fonction de la vitesse de disparition de $A$ comme $v = - \\frac{d[A]}{dt}$, on a donc $\\frac{d[A]}{dt} = - k [A]^2$.\nCette \u00e9quation diff\u00e9rentielle n'est pas lin\u00e9aire, mais on peut utiliser la m\u00e9thode de s\u00e9paration des variables et \u00e9crire $\\frac{- d[A]}{[A]^2} = k dt$ et trouver en int\u00e9grant :\n$$\\frac{1}{[A](t)} -\\frac{1}{[A] (t=0)} = k t$$\net finalement $[A](t) = \\frac{[A](t=0)}{1 + kt [A](t=0)}$.\n$\\frac{1}{[A](t)}$ est donc une fonction affine du temps.\nLe temps de demi-r\u00e9action est alors $t_{1\/2} = \\frac{1}{k[A](t=0)}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "798-5658",
"position": 9,
"duration": 30,
"question": {
"id": "5658",
"question": "Exprimer la loi d'Arrh\u00e9nius et donner l'unit\u00e9 de l'\u00e9nergie d'activation ainsi que son interpr\u00e9tation.",
"answer": "La loi 'dArrh\u00e9nius lie la constante de vitesse $k(T)$ d'une r\u00e9action \u00e0 la temp\u00e9rature selon $k(T) = A e^{E_A\/RT}$ avec $E_A$ l'\u00e9nergie d'activation en J\/mol. Cette \u00e9nergie d'activation correspond \u00e0 l'\u00e9nergie n\u00e9cessaire pour rompre et cr\u00e9er les liaisons chimiques par \"mole\" de r\u00e9action.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "798-5659",
"position": 10,
"duration": 30,
"question": {
"id": "5659",
"question": "Expliquer la r\u00e9gression lin\u00e9aire \u00e0 effectuer pour d\u00e9terminer l'\u00e9nergie d'activation d'une r\u00e9action dont on a d\u00e9termin\u00e9 la constante de vitesse \u00e0 plusieurs temp\u00e9ratures.",
"answer": "En exploitant la loi d'Arrh\u00e9nius et prenant son logarithme, on obtient $\\ln(k) = \\ln(A) - E_A\/RT$, donc en tra\u00e7ant $\\ln(k)$ en fonction de $1\/T$ (ou $1\/RT$) les points de mesure doivent se situer sur une droite de pente $-E_A\/R$ (ou $-E_A$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"800": {
"id": "800",
"name": "Quizz 15 : Oscillateurs harmoniques.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/800\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "110",
"value": "M\u00e9canique",
"field_id": "23",
"created_at": "2017-08-21 12:18:46",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-19",
"questions": [{
"id": "800-2674",
"position": 0,
"duration": 30,
"question": {
"id": "2674",
"question": "Ecrire l'\u00e9quation diff\u00e9rentielle d'un oscillateur harmonique de pulsation propre $\\omega_0$ sous forme canonique.\nDonner l'unit\u00e9 de la pulsation propre.",
"answer": "$\\frac{d^2y}{dt^2} + \\omega_0^2 y = 0$\n$\\omega_0$ s'exprime en rad\/s (ou en s$^{-1}$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "800-2675",
"position": 1,
"duration": 30,
"question": {
"id": "2675",
"question": "Quelle est la forme g\u00e9n\u00e9rale des solutions de l'\u00e9quation diff\u00e9rentielle $\\frac{d^2y}{dt^2} + \\omega_0^2 y = 0$ ?\nCombien faut-il de conditions initiales pour d\u00e9terminer l'unique solution d'un probl\u00e8me ?",
"answer": "$y(t) = A \\cos (\\omega_0t) + B \\sin(\\omega_0 t)$ ou $y(t) = A' \\cos(\\omega_0 t +\\phi)$\nIl faut deux conditions initiales pour trouver les deux valeurs $A$ et $B$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "800-2676",
"position": 2,
"duration": 30,
"question": {
"id": "2676",
"question": "On consid\u00e8re un circuit LC s\u00e9rie pr\u00e9alablement charg\u00e9 sous la tension $E$. D\u00e9terminer l'\u00e9quation diff\u00e9rentielle suivie par la tension aux bornes du condensateur lors de la r\u00e9ponse libre, et exprimer la p\u00e9riode des oscillations en fonction de $L$ et $C$.",
"answer": "Appelons $i$ le courant qui traverse le montage, $u$ la tension aux bornes du condensateur et $u_L$ celle aux bornes de la bobine, chosies toutes deux en convention r\u00e9cepteur.\nLa loi des mailles nous dit que $u_L= -u$, et les caract\u00e9ristiques des dip\u00f4les que $i = C \\frac{du}{dt}$ (pour le condensateur) et $u_L = L \\frac{di}{dt}$ pour la bobine.\nOn en d\u00e9duit donc que $- u = LC \\frac{d^2u}{dt^2}$, que l'on met sous forme canonique $\\frac{d^2u}{dt^2} + \\omega_0^2 u = 0$ en posant $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.\n\nOn va donc observer des oscillations avec une p\u00e9riode $T_0 = \\frac{2 \\pi}{\\omega_0} = 2 \\pi \\sqrt{LC}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "800-2677",
"position": 3,
"duration": 30,
"question": {
"id": "2677",
"question": "Etablir l'\u00e9quation diff\u00e9rentielle suivie par l'allongement d'un ressort horizontal de constante de raideur $k$ attach\u00e9 \u00e0 une masse $m$. D\u00e9terminer la p\u00e9riode des oscillations.",
"answer": "On applique le PFD \u00e0 la masse le long de l'axe horizontal, en prenant comme origine des positions la position o\u00f9 la longueur du ressort est sa longueur \u00e0 vide : $m \\ddot{x} = - k x$\nOn en d\u00e9duit donc que l'allongement du ressort $x$ suit l'\u00e9quation diff\u00e9rentielle $\\frac{d^2x}{dt^2} + \\omega_0^2 x = 0$ en posant $\\omega_0 = \\sqrt{\\frac{k}{m}}$.\n\nOn en d\u00e9duit donc que les oscillations auront une p\u00e9riode $T_0 = \\frac{2 \\pi}{\\omega_0} = 2 \\pi \\sqrt{\\frac{m}{k}}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "800-2678",
"position": 4,
"duration": 30,
"question": {
"id": "2678",
"question": "Lors de la r\u00e9ponse libre d'un circuit LC s\u00e9rie, on peut montrer que le courant dans le circuit $i(t)$ et la tension aux bornes du condensateur $u(t)$ (en convention r\u00e9cepteur) s'\u00e9crivent comme :\n$u(t) = U \\cos (\\omega t)$ et $i(t) = C \\frac{du}{dt} = - U C \\omega \\sin(\\omega t)$, \no\u00f9 $\\omega = \\sqrt{\\frac{1}{LC}}$.\nMontrer qu'il y a conservation de l'\u00e9nergie \u00e9lectrique stock\u00e9e dans le circuit. ",
"answer": "L'\u00e9nergie stock\u00e9e dans la bobine est $E_L (t) = \\frac12 L i(t)^2$ et celle stock\u00e9e dans le condensateur est $E_C (t) = \\frac12 C u(t)^2$. On a donc pour l'\u00e9nergie totale stock\u00e9e :\n$E(t) = E_L(t) + E_C (t) = \\frac12 \\left(  L C^2 \\omega^2 U^2 \\sin^2(\\omega t) + C U^2 \\cos^2(\\omega t) \\right) = \\frac12 C U^2 (\\cos^2(\\omega t) + \\sin^2(\\omega t)) = \\frac12 C U^2$, donc l'\u00e9nergie totale stock\u00e9e est bien conserv\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "800-2679",
"position": 5,
"duration": 30,
"question": {
"id": "2679",
"question": "Lors de l'\u00e9tude des oscillations libres d'un syst\u00e8me masse-ressort, on peut montrer que l'allongement du ressort peut s'\u00e9crire de la forme :\n$x(t) = X \\cos (\\omega t)$, \no\u00f9 $\\omega = \\sqrt{\\frac{k}{m}}$.\nMontrer qu'il y a conservation de l'\u00e9nergie m\u00e9canique. ",
"answer": "L'\u00e9nergie potentielle \u00e9lastique stock\u00e9e dans le resssort est $E_p (t) = \\frac12 k x(t)^2$ et l'\u00e9nergie cin\u00e9tique est $E_c (t) = \\frac12 m v(t)^2$. On a donc pour l'\u00e9nergie m\u00e9canique :\n$E(t) = E_p(t) + E_c (t) = \\frac12 \\left( k X^2 \\cos^2(\\omega t) +  m \\omega^2 X^2 \\sin^2(\\omega t) \\right) = \\frac12 k X^2 (\\cos^2(\\omega t) + \\sin^2(\\omega t)) = \\frac12 k X^2$, donc l'\u00e9nergie m\u00e9canique est bien conserv\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "800-2680",
"position": 6,
"duration": 30,
"question": {
"id": "2680",
"question": "Dire quelle grandeur est repr\u00e9sent\u00e9e en fonction de quelle autre grandeur pour le portrait de phase lors de l'\u00e9tude d'un syst\u00e8me masse-ressort sans frottement. D\u00e9crire le portrait de phase alors obtenu.",
"answer": "On trace la vitesse en fonction de la position.\nOn obtient alors une ellipse, parcourue dans le sens des aiguilles d'une montre ayant les axes du graphique comme grand et petit axe.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "110",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"752": {
"id": "752",
"name": "Quizz 02 : r\u00e9fraction, diffraction",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/752\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "118",
"value": "Optique",
"field_id": "23",
"created_at": "2017-08-21 12:30:19",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 210,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-23",
"questions": [{
"id": "752-2584",
"position": 0,
"duration": 30,
"question": {
"id": "2584",
"question": "Donner la vitesse de la lumi\u00e8re dans l'air, et les longueurs d'onde fronti\u00e8res du domaine visible.",
"answer": "$c \\simeq 3.10^8$ m\/s\nLe domaine visible s'\u00e9tend en longueurs d'onde entre 400 nm (bleu) et 800 nm (rouge).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2585",
"position": 1,
"duration": 30,
"question": {
"id": "2585",
"question": "Rappeler la d\u00e9finition de l'indice optique, et sa valeur pour le vide, l'air, l'eau et pour un verre typique.",
"answer": "L'indice optique $n$ d'un milieu transparent est le rapport entre la vitesse de la lumi\u00e8re dans le vide $c$ et sa vitesse dans le milieu consid\u00e9r\u00e9 $v$ : $n = \\frac{c}{v}$.\n\nOn a comme valeurs typiques :\n$n_{vide} = 1$\n$n_{air} \\simeq 1$\n$n_{eau} \\simeq 4\/3 \\simeq 1,33$\n$n_{verre} \\simeq 1,5$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2586",
"position": 2,
"duration": 30,
"question": {
"id": "2586",
"question": "Quelles sont les trois types de sources lumineuses utilis\u00e9es en TP ? Comment les reconnaitre ?",
"answer": "On utilise en TP :\n- les sources thermiques ;\n- les sources spectrales ;\n- les lasers.\n\nOn diff\u00e9rencie ces sources gr\u00e2ce \u00e0 leurs spectres : spectre continu pour les lampes thermiques, spectre \u00e0 raies pour les sources spectrales et spectre \u00e0 une seule raie pour les lasers.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2587",
"position": 3,
"duration": 30,
"question": {
"id": "2587",
"question": "Quelles sont les hypoth\u00e8ses de travail de l'optique g\u00e9om\u00e9trique ?",
"answer": "- Les rayons lumineux se propagent en ligne droite dans les milieux homog\u00e8nes ;\n- les rayons lumineux n'interagissent pas entre eux ;\n- principe du retour inverse de la lumi\u00e8re (si un rayon va de A \u00e0 B, il peut aussi aller de B \u00e0 A en suivant le m\u00eame chemin)\n- les objets sont suffisamment grands par rapport \u00e0 la longueur d'onde de la lumi\u00e8re utilis\u00e9e pour ne pas avoir de diffraction.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2588",
"position": 4,
"duration": 30,
"question": {
"id": "2588",
"question": "Dans la cadre d'une exp\u00e9rience de diffraction, donner la relation entre la largeur de l'ouverture $D$, la longueur d'onde $\\lambda$ et le demi angle d'ouverure $\\theta$.",
"answer": "$\\theta \\simeq \\frac{\\lambda}{D}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2589",
"position": 5,
"duration": 30,
"question": {
"id": "2589",
"question": "Citer les trois lois de Snell-Descartes pour un dioptre.",
"answer": "Lors de l'arriv\u00e9e d'un rayon lumineux sur un dioptre :\n- les rayons r\u00e9fl\u00e9chi et r\u00e9fract\u00e9 sont situ\u00e9s dans le plan d'incidence ;\n- l'angle de r\u00e9flexion est \u00e9gal et oppos\u00e9 \u00e0 l'angle d'incidence ;\n- l'angle de r\u00e9fraction $i_2$ et l'angle d'incidence $i_1$ sont li\u00e9s par la relation $n_1 \\sin i_1 = n_2 \\sin i_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "752-2590",
"position": 6,
"duration": 30,
"question": {
"id": "2590",
"question": "Donner la d\u00e9finition de l'angle limite de r\u00e9flexion totale et sa valeur pour un dioptre s\u00e9parant deux milieux d'indices optiques $n_1$ et $n_2$.",
"answer": "L'angle limite de r\u00e9flexion totale est la valeur de l'angle d'incidence \u00e0 partir de laquelle il n'est plus possible d'observer un rayon r\u00e9fract\u00e9 dans le milieu d'indice $n_2 < n_1$.\n\nPour pouvoir observer un rayon r\u00e9fract\u00e9 avec un angle de r\u00e9fraction $i_2$, on doit pouvoir avoir $n_1 \\sin i_1 = n_2 \\sin i_2$, donc $\\frac{n_1}{n_2} \\sin i_1 = \\sin i_2 \\leq 1$.\nOn trouve donc l'angle limite de r\u00e9flexion totale $i_{lim}$ tel que $\\sin i_{lim} = \\frac{n_2}{n_1}$ ou $i_{lim} = \\textrm{Arcsin} \\frac{n_2}{n_1}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"783": {
"id": "783",
"name": "Quizz 10 : Architecture de la mati\u00e8re",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/783\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "72",
"value": "Autre",
"field_id": "23",
"created_at": "2017-07-19 18:22:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "114",
"value": "Atomistique",
"field_id": "23",
"created_at": "2017-08-21 12:25:31",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 510,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-07",
"questions": [{
"id": "783-2634",
"position": 0,
"duration": 30,
"question": {
"id": "2634",
"question": "De quelles particules \u00e9l\u00e9mentaires est compos\u00e9 un atome et comment sont-elles r\u00e9parties ?",
"answer": "Un atome est compos\u00e9 de protons, de neutrons et d'\u00e9lectrons. Les protons et les neutrons sont dans le noyau, autour duquel gravitent les \u00e9lectrons (dispos\u00e9 sur des couches \u00e9lectroniques).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2640",
"position": 1,
"duration": 30,
"question": {
"id": "2640",
"question": "De quoi est compos\u00e9 un atome d'uranium 235 dont le noyau se note ${}^{235}_{92}U$ ?",
"answer": "Il est compos\u00e9 de 235 nucl\u00e9ons parmi lesquels il y a 92 protons. Il contient donc 235-92 =143 neutrons, et aussi 92 \u00e9lectrons pour assurer l'\u00e9lectroneutralit\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2636",
"position": 2,
"duration": 30,
"question": {
"id": "2636",
"question": "Que se passe t'il lorsqu'un atome absorbe un photon ?",
"answer": "L'atome atteint un \u00e9tat d'\u00e9nergie sup\u00e9rieur (il est excit\u00e9), obtenu par le changement d'orbite d'un \u00e9lectron.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2637",
"position": 3,
"duration": 30,
"question": {
"id": "2637",
"question": "Lorsqu'un photon est \u00e9mis ou absorb\u00e9 par un atome, quel est le lien entre sa longueur d'onde et les \u00e9tats d'\u00e9nergie de l'atome ?",
"answer": "Lors de l'\u00e9mission ou de l'absorption d'un photon, l'atome passe d'un \u00e9tat d'\u00e9nergie $E_n$ \u00e0 un \u00e9tat d'\u00e9nergie $E_m$. La longueur d'onde du photon $\\lambda$ est telle que $\\frac{hc}{\\lambda} = |E_n -E_m|$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2638",
"position": 4,
"duration": 30,
"question": {
"id": "2638",
"question": "Comment s'appelle la r\u00e8gle permettant de d\u00e9terminer la structure \u00e9lectronique d'un atome dans son \u00e9tat fondamental et que dit-elle ?",
"answer": "Il s'agit de la r\u00e8gle de Klechkowski, qui dit que l'on remplit les sous-couches \u00e9lectroniques dans l'ordre 1s, 2s, 2p, 3s, 3p, 4s, 3s, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, etc",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e62da580-9d0e-11ef-a6ba-cf34ffe28136",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2635",
"position": 5,
"duration": 30,
"question": {
"id": "2635",
"question": "Que se passe t'il lorsque un \u00e9lectron change d'orbite, faisant passer un atome d'un \u00e9tat excit\u00e9 \u00e0 un \u00e9tat d\u00e9sexcit\u00e9 ?",
"answer": "Lors de la d\u00e9sexcitation d'un atome il y a \u00e9mission d'un photon.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2641",
"position": 6,
"duration": 30,
"question": {
"id": "2641",
"question": "Quelle est la structure \u00e9lectronique de valence des halog\u00e8nes ? O\u00f9 se situent-ils dans la classification p\u00e9riodique des \u00e9l\u00e9ments ?",
"answer": "Leur structure \u00e9lectronique de valence est $ns^2np^5$.\nIls sont situ\u00e9s dans l'avant-derni\u00e8re colonne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2642",
"position": 7,
"duration": 30,
"question": {
"id": "2642",
"question": "Quelle est la structure \u00e9lectronique de valence des alcalins ? O\u00f9 se situent-ils dans la classification p\u00e9riodique des \u00e9l\u00e9ments ?",
"answer": "Leur structure \u00e9lectronique de valence est $ns^1$.\nIls sont situ\u00e9s dans la premi\u00e8re colonne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2643",
"position": 8,
"duration": 30,
"question": {
"id": "2643",
"question": "Quelle est la structure \u00e9lectronique de valence des gaz nobles ? O\u00f9 se situent-ils dans la classification p\u00e9riodique des \u00e9l\u00e9ments ?",
"answer": "Leur structure \u00e9lectronique de valence est $ns^2np^6$.\nIls sont situ\u00e9s dans la derni\u00e8re colonne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2639",
"position": 9,
"duration": 30,
"question": {
"id": "2639",
"question": "Quelle est la structure \u00e9lectronique d'un atome d'oxyg\u00e8ne (Z=8) dans son \u00e9tat fondamental ?",
"answer": "$1s^22s^22p^4$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-2646",
"position": 10,
"duration": 30,
"question": {
"id": "2646",
"question": "Donnez la structure \u00e9lectronique du potassium (Z= 19) dans son \u00e9tat fondamental.\nQuelle est sa position dans la classification p\u00e9riodique (ligne, colonne) ? A quelle famille appartient-il ? S'agit-il d'un m\u00e9tal ?\nQuel ion monoatomique va t'il former ?",
"answer": "La structure \u00e9lectronique d'un atome de potassium dans son \u00e9tat fondamental est $1s^22s^22p^63s^23p^64s^1$.\nIl est situ\u00e9 dans la 4\u00e8me ligne et dans la premi\u00e8re colonne. Il s'agit donc d'un alcalin, et c'est un m\u00e9tal.\nIl formera l'ion $K^+$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "783-2647",
"position": 11,
"duration": 30,
"question": {
"id": "2647",
"question": "Repr\u00e9senter la structure de Lewis de l'atome d'hydrog\u00e8ne (Z=1), de l'atome d'oxyg\u00e8ne (Z=8), de la mol\u00e9cule de dioxyg\u00e8ne et de la mol\u00e9cule d'eau.",
"answer": "R\u00e9ponse :\n$H \\cdot$\n\n$\\cdot \\underline{\\bar{O}} \\cdot$\n\n$\\underline{\\bar{O}} = \\underline{\\bar{O}} $\n\n$H - \\underline{\\bar{O}} - H$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "783-2645",
"position": 12,
"duration": 30,
"question": {
"id": "2645",
"question": "Donnez la structure \u00e9lectronique du fluor (Z=9) dans son \u00e9tat fondamental.\nQuelle est sa position dans la classification p\u00e9riodique (ligne, colonne) ? A quelle famille appartient-il ? \nQuel ion monoatomique va t'il former ?",
"answer": "La structure \u00e9lectronique d'un atome de fluor dans son \u00e9tat fondamental est $1s^22s^22p^5$.\nIl est situ\u00e9 dans la 2\u00e8me ligne et dans la septi\u00e8me colonne (l'avant-derni\u00e8re). Il s'agit donc d'un halog\u00e8ne.\nIl formera l'ion $F^-$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "114",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "783-5932",
"position": 13,
"duration": 30,
"question": {
"id": "5932",
"question": "Quelle est la g\u00e9om\u00e9trie d'une mol\u00e9cule de $CO_2$ ? ",
"answer": "Cette mol\u00e9cule est compos\u00e9e d'un atome de carbone au centre faisant deux doubles liaisons avec chaque atome d'oxyg\u00e8ne. Il y a deux groupes de doublets ind\u00e9pendants, elle est donc lin\u00e9aire.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-5933",
"position": 14,
"duration": 30,
"question": {
"id": "5933",
"question": "Quelle est la g\u00e9om\u00e9trie d'une mol\u00e9cule d'ammoniac $NH_3$ ?",
"answer": "L'atome d'azote poss\u00e8de 3 doublets liants vers les $H$ et un doublet non-liant, donc 4 groupes de doublets ind\u00e9pendants, il s'agit d'une structure t\u00e9tra\u00e9drique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-5934",
"position": 15,
"duration": 30,
"question": {
"id": "5934",
"question": "Classer dans l'ordre les \u00e9lectron\u00e9gativit\u00e9s de l'azote, du carbone, de l'oxyg\u00e8ne et de l'hydrog\u00e8ne.",
"answer": "$\\chi(H) \\simeq \\chi(C) < \\chi(N) < \\chi (O)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "783-5935",
"position": 16,
"duration": 30,
"question": {
"id": "5935",
"question": "Expliquer pourquoi la mol\u00e9cule d'eau est polaire et celle de dioxyde de carbone ne l'est pas.",
"answer": "La mol\u00e9cule de dioxyde de carbone a une structure lin\u00e9aire (car deux doubles liaisons entre le C et les O). Les liaisons sont polaris\u00e9es avec une charge $\\delta_+$ sur le carbone et une charge $\\delta_-$ sur l'oxyg\u00e8ne (car l'oxyg\u00e8ne est plus \u00e9lectron\u00e9gatif que le carbone). Les deux barycentres des charges sont toutefois confondus, il n'y a pas de moment dipolaire donc la mol\u00e9cule est apolaire.\n\nPour la mol\u00e9cule d'eau, la g\u00e9om\u00e9trie est coud\u00e9e (l'oxyg\u00e8ne a 2 doublets non-liants et 2 liaisons simples donc g\u00e9om\u00e9trie t\u00e9tra\u00e9drique). Les liaisons sont polaris\u00e9es avec une charge $\\delta_+$ sur les hydrog\u00e8ne et une charge $\\delta_-$ sur l'oxyg\u00e8ne (car l'oxyg\u00e8ne est plus \u00e9lectron\u00e9gatif que l'hydrog\u00e8ne). Les barycentres ne sont pas confondus \u00e0 cause de la g\u00e9om\u00e9trie de la mol\u00e9cule, il y a donc un moment dipolaire et la mol\u00e9cule est polaire.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "72",
"level_id": "6",
"difficulty": 4
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"775": {
"id": "775",
"name": "Quizz 08 : Quotients de r\u00e9action",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/775\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 180,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-17",
"questions": [{
"id": "775-2615",
"position": 0,
"duration": 30,
"question": {
"id": "2615",
"question": "Ecrire le quotient de r\u00e9action pour la r\u00e9action $CH_3COOH_{(aq)} + H_2O = CH_3COO^-_{(aq)} + H_3O^+_{(aq)}$.",
"answer": "$Q = \\frac{[CH_3COO^-][H_3O^+]}{[CH_3COOH] c^0}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "775-2616",
"position": 1,
"duration": 30,
"question": {
"id": "2616",
"question": "Ecrire le quotient de r\u00e9action pour la r\u00e9action $Al(OH)_{3(s)} = Al^{3+}_{(aq)} + 3 HO^-_{(aq)}$.",
"answer": "$Q = \\frac{[Al^{3+}][HO^-]^3}{(c^0)^4}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "775-2617",
"position": 2,
"duration": 30,
"question": {
"id": "2617",
"question": "Quelle est la concentration des ions en solution lorsque l'on dissout 34 g de nitrate d'argent ($AgNO_3$ formant les ions $Ag^+$ et $NO_3^-$) dans 250 mL d'eau ?\nOn ajoute 500 mL d'eau sal\u00e9e ($NaCl$) \u00e0 la concentration de 1,0 mol\/L. Les ions argent et les ions chlorure r\u00e9agissent totalement pour former du chlorure d'argent $AgCl$.\nFaire un tableau d'avancement et donner les concentrations de chaque ion apr\u00e8s m\u00e9lange.\nM(N) = 14,0 g\/mol ; M(O) = 16,0 g\/mol ; M(Ag) = 107,9 g\/mol",
"answer": "Il faut d'abord calculer la masse molaire du nitrate d'argent $M(AgNO_3) = 169,9$ g\/mol.\nIl y a donc une quantit\u00e9 de mati\u00e8re $n_{AgNO_3} = 34\/169,9 = 0,20$ mol, et on trouve donc comme concentrations des ions form\u00e9s $[Ag^+]=[NO_3^-] = 0,80$ mol\/L.\n\nIl y a dans l'eau sal\u00e9e une quantit\u00e9 de mati\u00e8re d'ions chlorure $n_{Cl^-} = 0,50$ mol,ce seront donc les ions argent qui seront le r\u00e9actif limitant (voir le tableau d'avancement).\nOn trouve ensuite les concentrations en divisant par le volume total (de 750 mL, attention !) et on trouve\n$[Ag^+] \\simeq 0$ ; $[Cl^-] = \\frac{0,30 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,40$ mol\/L ; $[NO_3^-] = \\frac{0,20 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,27$ mol\/L et $[Na^+] = \\frac{0,50 \\textrm{ mol}}{0,750 \\textrm{ L}} = 0,67$ mol\/L. ",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a8aaa9f0-962b-11e8-bdd6-872b1e76e3ac",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "775-2618",
"position": 3,
"duration": 30,
"question": {
"id": "2618",
"question": "Ecrire le quotient de r\u00e9action de la r\u00e9action de pr\u00e9cipitation du chlorure d'argent (les r\u00e9actifs sont les ions $Ag^+$ et les ions $Cl^-$).",
"answer": "La r\u00e9action \u00e9tudi\u00e9e est $Ag^+_{(aq)} + Cl^-_{(aq)} = AgCl_{(s)}$ donc on trouve le quotient de r\u00e9action :\n$$ Q = \\frac{(c^0)^2}{[Ag^+][Cl^-]} .$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "775-2619",
"position": 4,
"duration": 30,
"question": {
"id": "2619",
"question": "La r\u00e9action $CH_3COOH_{(aq)} + H_2O = CH_3COO^-_{(aq)} + H_3O^+_{(aq)}$ a pour constante d'\u00e9quilibre $K = 10^{-4,8}$.\nQuels sont les esp\u00e8ces qui vont se former si $[CH_3COO^-]=[CH_3COOH]=[H_3O^+] = 0,1$ mol\/L ?",
"answer": "Il faut calculer le quotient de r\u00e9action dans les conditions initiales et le comparer \u00e0 la constante d'\u00e9quilibre :\n$$ Q = \\frac{[CH_3COO^-][H_3O^+]}{[CH_3COOH]c^0} = 0,1 > K$$\n\nPuisque le quotient de r\u00e9action est plus grand que la constante d'\u00e9quilibre, il va devoir diminuer, donc la r\u00e9action a lieu dans le sens indirect : il y aura formation de $CH_3COOH$ et $H_2O$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "775-2620",
"position": 5,
"duration": 30,
"question": {
"id": "2620",
"question": "La r\u00e9action $CH_3COOH_{(aq)} + H_2O = CH_3COO^-_{(aq)} + H_3O^+_{(aq)}$ a pour constante d'\u00e9quilibre $K = 10^{-4,8}$.\nQuels sont les esp\u00e8ces qui vont se former si $[CH_3COO^-]=[H_3O^+] = 1$ mmol\/L et $[CH_3COOH] = 63 mmol\/L ?",
"answer": "Il faut calculer le quotient de r\u00e9action dans les conditions initiales et le comparer \u00e0 la constante d'\u00e9quilibre :\n$$ Q = \\frac{[CH_3COO^-][H_3O^+]}{[CH_3COOH]c^0} \\simeq 1,6.10^{-5} \\simeq K$$\n\nPuisque le quotient de r\u00e9action est \u00e9gal la constante d'\u00e9quilibre, la r\u00e9action est \u00e0 l'\u00e9quilibre : il y aura autant formation de $CH_3COO^-$ et $H_3O^+$ que de $CH_3COOH$ et $H_2O$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"838": {
"id": "838",
"name": "Quizz 25 : Acides, bases",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/838\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 450,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5666666666666667,
"shared_at": "2025-03-13",
"questions": [{
"id": "838-2746",
"position": 0,
"duration": 30,
"question": {
"id": "2746",
"question": "Comment d\u00e9finit-on un acide ? une base ?",
"answer": "Un acide est une esp\u00e8ce chimique capable de c\u00e9der un (ou plusieurs) proton(s) $H^+$.\nUne base est une esp\u00e8ce chimique capable de capter un (ou plusieurs) proton(s) $H^+$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2747",
"position": 1,
"duration": 30,
"question": {
"id": "2747",
"question": "Comment d\u00e9finit-on le $pH$ d'une solution aqueuse ?",
"answer": "Le $pH$ est l'oppos\u00e9 du logarithme d\u00e9cimal de l'activit\u00e9 des ions $H_3O^+$ : $pH = - \\log_{10} \\left( \\frac{[H_3O^+]}{c^0} \\right)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2748",
"position": 2,
"duration": 30,
"question": {
"id": "2748",
"question": "Qu'est-ce qu'une solution acide ? Donner un exemple.\nQu'est-ce qu'une solution basique ? Donner un exemple.",
"answer": "Solution acide : solution telle que $pH < 7$. Exemples : vinaigre, coca-cola, jus de citron, etc\n\nSolution basique : solution telle que $pH >7$. Exemples : eau de Javel, Destop, etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2749",
"position": 3,
"duration": 30,
"question": {
"id": "2749",
"question": "Ecrire la r\u00e9action d'autoprotolyse de l'eau, et donner sa constante d'\u00e9quilibre.",
"answer": "$2 H_2O = H_3O^+ + HO^-$\n$K_e = 10^{-14}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2750",
"position": 4,
"duration": 30,
"question": {
"id": "2750",
"question": "Qu'est ce qu'un acide fort ? Donner un exemple, avec la formule chimique.",
"answer": "Un acide fort est un acide qui est totalement dissoci\u00e9 dans l'eau : toutes les mol\u00e9cules de l'acide consid\u00e9r\u00e9 c\u00e8dent leur proton.\n\nExemples : acide chlorhydrique $HCl$, acide nitrique $HNO_3$, acide sulfurique $H_2SO_4$, etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2751",
"position": 5,
"duration": 30,
"question": {
"id": "2751",
"question": "Quelle est la concentration en ions $H_3O^+$ et en ions $HO^-$ d'une solution aqueuse de $pH = 9$ ?",
"answer": "On sait que $pH = - \\log_{10} \\left( \\frac{[H_3O^+]}{c^0} \\right)$ donc en inversant la relation $[H_3O^+] = 10^{-pH} c^0$.\nDonc pour cette solution, $[H_3O^+] = 10^{-9}$ mol\/L.\n\nEn solution aqueuse, la r\u00e9action d'autoprotolyse de l'eau, de constante d'\u00e9quilibre $K_e = 10^{-14}$ assure que :\n$$ \\frac{[H_3O^+][HO^-]}{(c^0)^2} = K_e. $$\nOn en d\u00e9duit donc que $[HO^-] = \\frac{K_e(c^0)^2}{[H_3O^+]} = c^0 K_e 10^{pH} = 10^{-5}$ mol\/L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2752",
"position": 6,
"duration": 30,
"question": {
"id": "2752",
"question": "Pour un couple acido-basique $AH\/A^-$, d\u00e9finir constante d'acidit\u00e9 $K_a$ et $pK_a$.",
"answer": "$K_a$ est la constante d'\u00e9quilibre associ\u00e9 \u00e0 la r\u00e9action de l'acide avec l'eau : $AH + H_2O = A^- + H_3O^+$.\n$pK_a = - \\log_{10} K_a$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2753",
"position": 7,
"duration": 30,
"question": {
"id": "2753",
"question": "L'ammoniac $NH_3$ appartient au couple acido-basique $NH_4^+\/NH_3$ de $pK_a = 9,2$. Ecrire la r\u00e9action de l'ammoniac avec l'eau et exprimer sa constante d'\u00e9quilibre en fonction de $K_e$ et $K_a$, puis la calculer.",
"answer": "$NH_3 + H_2O = HO^- + NH_4^+$\n\nSi on appelle $K$ la constante d'\u00e9quilibre de cette r\u00e9action, \u00e0 l'\u00e9quilibre on a :\n$$ K = \\frac{[HO^-][NH_4^+]}{c^0[NH_3]} = \\frac{[HO^-][H_3O^+]}{(c^0)^2} \\frac{[NH_4^+] c^0}{[H_3O^+][NH_3]} = \\frac{K_e}{K_a} = 10^{-14 -(-9,2)} = 10^{-4,8}. $$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "838-2754",
"position": 8,
"duration": 30,
"question": {
"id": "2754",
"question": "Quelle est la concentration en solut\u00e9 apport\u00e9 d'un vinaigre de $pH =2,7$, sachant que le vinaigre est une solution d'acide \u00e9thano\u00efque appartenant au couple $CH_3COOH\/CH_3COO^-$ de $pK_a = 4,8$ ?",
"answer": "Si on appelle $c$ la concentration recherch\u00e9e, alors la r\u00e9action d'acidit\u00e9 $CH_3COOH + H_20 = CH_3COO^- + H_3O^+$, \u00e0 l'\u00e9quilibre, nous dit que $[CH_3COO^-]=[H_3O^+] =c_1$ et $[CH_3COOH]= c- c_1$.\n\nOr $[H_3O^+] = c^0 10^{-pH}$, donc $c_1 = 10^{-2,7}$ mol\/L.\n\nOn sait de plus que $pH = pK_a + \\log_{10} \\left( \\frac{[CH_3COO^-]}{[CH_3COOH]} \\right)$, donc $[CH_3COOH] = 10^{pKa-pH} c_1 = 10^{-0,6}$ mol\/L.\n\nOn d\u00e9duit finalement $c = [CH_3COOH] + [CH_3COO^-] \\simeq [CH3COOH] = 10^{-0,6}$ mol\/L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "838-2755",
"position": 9,
"duration": 30,
"question": {
"id": "2755",
"question": "Une solution d'ammoniac $NH_3$ de concentration $c =0,01$ mol\/L est telle que $pH = 10,6$. Que vaut le $pK_a$ du couple $NH_4^+\/NH_3$ ?",
"answer": "On consid\u00e8re la r\u00e9action de l'ammoniac avec l'eau $NH_3 + H_2O = HO^- + NH_4^+$.\nA l'\u00e9quilibre, on a $[NH_4^+] = [HO^-]$, or $[HO^-] = c^0 K_e 10^{pH}$ car la r\u00e9action d'autoprotolyse de l'eau est \u00e9quilibr\u00e9e.\n\nOn a donc $[HO^-] = 10^{-3,4} \\textrm{ mol\/L} \\simeq 0,4$ mmol\/L. \n\nPar conservation de l'\u00e9lement azote $N$, on a $[NH_3] + [NH_4^+] = c$, d'o\u00f9 l'on d\u00e9duit $[NH_3] = 9,6$ mmol\/L.\n\nOn sait enfin que $pH = pK_a + \\log_{10} \\left( \\frac{[NH_3]}{[NH_4^+]} \\right)$ d'o\u00f9 l'on d\u00e9duit $pK_a = pH - \\log_{10} \\left( \\frac{[NH_3]}{[NH_4^+]} \\right) = 10,6 - \\log_{10} \\left(9,6\/0,4\\right) \\simeq 9,2$.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "838-2756",
"position": 10,
"duration": 30,
"question": {
"id": "2756",
"question": "Lors d'un dosage acido-basique suivi par pH-m\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "L'\u00e9quivalence est rep\u00e9r\u00e9e par un saut de $pH$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2757",
"position": 11,
"duration": 30,
"question": {
"id": "2757",
"question": "Lors d'un dosage acido-basique suivi par colorim\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "La solution titr\u00e9e change de couleur \u00e0 l'\u00e9quivalence.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2758",
"position": 12,
"duration": 30,
"question": {
"id": "2758",
"question": "Lors d'un dosage acido-basique suivi par conductim\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "La courbe $\\sigma(V)$ pr\u00e9sente une rupture de pente \u00e0 l'\u00e9quivalence.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "838-2759",
"position": 13,
"duration": 30,
"question": {
"id": "2759",
"question": "Quelle est la concentration $c$ d'une solution d'acide chlorhydrique $HCl$ si en effectuant le dosage de $V_a=10$ mL de cette solution par une solution de soude $NaOH$ de concentration $c_b = 0,10$ mol\/L on rep\u00e8re un volume \u00e9quivalent $V_{eq} = 17$ mL ?",
"answer": "La r\u00e9action support du titrage est $H^+ + OH^- \\to H_2O$ (ou $H_3O^+ + HO^- \\to 2 H_2O$), qui est la r\u00e9action inverse de l'autoprotolyse de l'eau, donc de constante d'\u00e9quilibre $K = \\frac{1}{K_e} = 10^{14} \\gg 1$, on peut donc consid\u00e9rer cette r\u00e9action comme totale. \n\nA l'\u00e9quivalence, vu que les coefficients st\u0153chiom\u00e9triques sont \u00e9gaux, on a $n_{H^+} = n_{HO^-}$ donc on doit avoir $c V_a = c_b V_{eq}$ d'o\u00f9 l'on d\u00e9duit la concentration recherch\u00e9e $c = \\frac{c_b V_{eq}}{V_a} = 0,17$ mol\/L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "838-2762",
"position": 14,
"duration": 30,
"question": {
"id": "2762",
"question": "Quelle grandeur peut-on mesurer \u00e0 la demi-\u00e9quivalence d'un dosage acido-basique, et comment ?",
"answer": "A la demi-\u00e9quivalence, le $pH$ de la solution est \u00e9gal au $pK_a$ du couple de la solution titr\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"839": {
"id": "839",
"name": "Quizz 26 : Dosage. Oxydor\u00e9duction.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/839\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-03-20",
"questions": [{
"id": "839-2756",
"position": 0,
"duration": 30,
"question": {
"id": "2756",
"question": "Lors d'un dosage acido-basique suivi par pH-m\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "L'\u00e9quivalence est rep\u00e9r\u00e9e par un saut de $pH$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2757",
"position": 1,
"duration": 30,
"question": {
"id": "2757",
"question": "Lors d'un dosage acido-basique suivi par colorim\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "La solution titr\u00e9e change de couleur \u00e0 l'\u00e9quivalence.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2758",
"position": 2,
"duration": 30,
"question": {
"id": "2758",
"question": "Lors d'un dosage acido-basique suivi par conductim\u00e9trie, comment rep\u00e8re t'on l'\u00e9quivalence ?",
"answer": "La courbe $\\sigma(V)$ pr\u00e9sente une rupture de pente \u00e0 l'\u00e9quivalence.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2759",
"position": 3,
"duration": 30,
"question": {
"id": "2759",
"question": "Quelle est la concentration $c$ d'une solution d'acide chlorhydrique $HCl$ si en effectuant le dosage de $V_a=10$ mL de cette solution par une solution de soude $NaOH$ de concentration $c_b = 0,10$ mol\/L on rep\u00e8re un volume \u00e9quivalent $V_{eq} = 17$ mL ?",
"answer": "La r\u00e9action support du titrage est $H^+ + OH^- \\to H_2O$ (ou $H_3O^+ + HO^- \\to 2 H_2O$), qui est la r\u00e9action inverse de l'autoprotolyse de l'eau, donc de constante d'\u00e9quilibre $K = \\frac{1}{K_e} = 10^{14} \\gg 1$, on peut donc consid\u00e9rer cette r\u00e9action comme totale. \n\nA l'\u00e9quivalence, vu que les coefficients st\u0153chiom\u00e9triques sont \u00e9gaux, on a $n_{H^+} = n_{HO^-}$ donc on doit avoir $c V_a = c_b V_{eq}$ d'o\u00f9 l'on d\u00e9duit la concentration recherch\u00e9e $c = \\frac{c_b V_{eq}}{V_a} = 0,17$ mol\/L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "839-2760",
"position": 4,
"duration": 30,
"question": {
"id": "2760",
"question": "D\u00e9terminer le pH d\u2019un m\u00e9lange de $V_1 = 100$ mL de solution d\u2019ammoniac $NH_3$ de concentration $c = 1, 0.10^{\u22123}$ mol\/L ($pK_a(NH^+_4 \/NH_3) = 9, 2$) et de $V_2 = 50$ mL de solution d\u2019acide formique de concentration $c = 0, 01$ mol\/L ($pKa(HCOOH\/HCOO^\u2212) = 3, 8$).",
"answer": "La r\u00e9action qui va se produire est la r\u00e9action acido-basique $NH_3 + HCOOH = HCOO^-+NH_4^+$, de constante de r\u00e9action $K = \\frac{K_a (HCOOH\/HCOO^-)}{K_a(NH_4^+\/NH_3)} = 10^{5,4}$, que l'on peut donc consid\u00e9rer comme totale.\nOn remplit alors un tableau d'avancement. \n\nOn voit alors que le r\u00e9catif en exc\u00e8s est $HCOOH$, et on utilise alors la relation $pH = pK_a(HCOOH\/HCOO^-) + \\log_{10} \\left( \\frac{[HCOO^-]}{[HCOOH]} \\right) = 3,2.$",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/26e375e0-a2e3-11e8-b309-23003c675c76",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "839-2762",
"position": 5,
"duration": 30,
"question": {
"id": "2762",
"question": "Quelle grandeur peut-on mesurer \u00e0 la demi-\u00e9quivalence d'un dosage acido-basique, et comment ?",
"answer": "A la demi-\u00e9quivalence, le $pH$ de la solution est \u00e9gal au $pK_a$ du couple de la solution titr\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "839-2761",
"position": 6,
"duration": 30,
"question": {
"id": "2761",
"question": "Donner la d\u00e9finition d'un oxydant, puis d'un r\u00e9ducteur",
"answer": "Oxydant : esp\u00e8ce chimique capable de capter un ou plusieurs \u00e9lectrons.\nR\u00e9ducteur : esp\u00e8ce chimique capable de c\u00e9der un ou plusieurs \u00e9lectrons. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2763",
"position": 7,
"duration": 30,
"question": {
"id": "2763",
"question": "Ecrire la demi-\u00e9quation d'oxydor\u00e9duction du couple $MnO_4^-\/Mn^{2+}$. Justifier que $MnO_4^-$ est l'oxydant.",
"answer": "$MnO_4^{-} + 8H^+ + 5 e^- = Mn^{2+} + 4 H_2O$.\n$MnO_4^-$ est l'esp\u00e8ce qui capte 5 \u00e9lectrons, il s'agit donc bien de l'oxydant. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2764",
"position": 8,
"duration": 30,
"question": {
"id": "2764",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $MnO_4^-\/Mn^{2+}$. Justifier que $MnO_4^-$ est l'oxydant.",
"answer": "Pour $MnO_4^-$, $n.o. (Mn) + 4 n.o. (O) = - I$, donc $n.o (Mn) = + VII$.\nPour $Mn^{2+}$, $n.o. (Mn) = + II$.\n\n$MnO_4^-$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2765",
"position": 9,
"duration": 30,
"question": {
"id": "2765",
"question": "Ecrire la demi-\u00e9quation d'oxydor\u00e9duction du couple $Cr_2O_7^{2-}\/Cr^{3+}$. Justifier que $Cr_2O_7^{2-}$ est l'oxydant.",
"answer": "$Cr_2O_7^{2-} + 14 H^+ + 6 e^- = 2 Cr^{3+} + 7 H_2O$\n$Cr_2O_7^{2-}$ est bien l'oxydant car c'est l'esp\u00e8ce qui capte 6 \u00e9lectrons.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "839-2766",
"position": 10,
"duration": 30,
"question": {
"id": "2766",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $Cr_2O_7^{2-}\/Cr^{3+}$. Justifier que $Cr_2O_7^{2-}$ est l'oxydant.",
"answer": "Pour $Cr_2O_7^{2-}$, $2 n.o. (Cr) + 7 n.o. (O) = - II$, donc $n.o (Cr) = + VI$.\nPour $Cr^{3+}$, $n.o. (cr) = + III$.\n\n$Cr_2O_7^{2-}$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"840": {
"id": "840",
"name": "Quizz 27 : Oxydor\u00e9duction",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/840\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-03-27",
"questions": [{
"id": "840-2760",
"position": 0,
"duration": 30,
"question": {
"id": "2760",
"question": "D\u00e9terminer le pH d\u2019un m\u00e9lange de $V_1 = 100$ mL de solution d\u2019ammoniac $NH_3$ de concentration $c = 1, 0.10^{\u22123}$ mol\/L ($pK_a(NH^+_4 \/NH_3) = 9, 2$) et de $V_2 = 50$ mL de solution d\u2019acide formique de concentration $c = 0, 01$ mol\/L ($pKa(HCOOH\/HCOO^\u2212) = 3, 8$).",
"answer": "La r\u00e9action qui va se produire est la r\u00e9action acido-basique $NH_3 + HCOOH = HCOO^-+NH_4^+$, de constante de r\u00e9action $K = \\frac{K_a (HCOOH\/HCOO^-)}{K_a(NH_4^+\/NH_3)} = 10^{5,4}$, que l'on peut donc consid\u00e9rer comme totale.\nOn remplit alors un tableau d'avancement. \n\nOn voit alors que le r\u00e9catif en exc\u00e8s est $HCOOH$, et on utilise alors la relation $pH = pK_a(HCOOH\/HCOO^-) + \\log_{10} \\left( \\frac{[HCOO^-]}{[HCOOH]} \\right) = 3,2.$",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/26e375e0-a2e3-11e8-b309-23003c675c76",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "840-2761",
"position": 1,
"duration": 30,
"question": {
"id": "2761",
"question": "Donner la d\u00e9finition d'un oxydant, puis d'un r\u00e9ducteur",
"answer": "Oxydant : esp\u00e8ce chimique capable de capter un ou plusieurs \u00e9lectrons.\nR\u00e9ducteur : esp\u00e8ce chimique capable de c\u00e9der un ou plusieurs \u00e9lectrons. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2763",
"position": 2,
"duration": 30,
"question": {
"id": "2763",
"question": "Ecrire la demi-\u00e9quation d'oxydor\u00e9duction du couple $MnO_4^-\/Mn^{2+}$. Justifier que $MnO_4^-$ est l'oxydant.",
"answer": "$MnO_4^{-} + 8H^+ + 5 e^- = Mn^{2+} + 4 H_2O$.\n$MnO_4^-$ est l'esp\u00e8ce qui capte 5 \u00e9lectrons, il s'agit donc bien de l'oxydant. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2764",
"position": 3,
"duration": 30,
"question": {
"id": "2764",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $MnO_4^-\/Mn^{2+}$. Justifier que $MnO_4^-$ est l'oxydant.",
"answer": "Pour $MnO_4^-$, $n.o. (Mn) + 4 n.o. (O) = - I$, donc $n.o (Mn) = + VII$.\nPour $Mn^{2+}$, $n.o. (Mn) = + II$.\n\n$MnO_4^-$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2765",
"position": 4,
"duration": 30,
"question": {
"id": "2765",
"question": "Ecrire la demi-\u00e9quation d'oxydor\u00e9duction du couple $Cr_2O_7^{2-}\/Cr^{3+}$. Justifier que $Cr_2O_7^{2-}$ est l'oxydant.",
"answer": "$Cr_2O_7^{2-} + 14 H^+ + 6 e^- = 2 Cr^{3+} + 7 H_2O$\n$Cr_2O_7^{2-}$ est bien l'oxydant car c'est l'esp\u00e8ce qui capte 6 \u00e9lectrons.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2766",
"position": 5,
"duration": 30,
"question": {
"id": "2766",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $Cr_2O_7^{2-}\/Cr^{3+}$. Justifier que $Cr_2O_7^{2-}$ est l'oxydant.",
"answer": "Pour $Cr_2O_7^{2-}$, $2 n.o. (Cr) + 7 n.o. (O) = - II$, donc $n.o (Cr) = + VI$.\nPour $Cr^{3+}$, $n.o. (cr) = + III$.\n\n$Cr_2O_7^{2-}$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2767",
"position": 6,
"duration": 30,
"question": {
"id": "2767",
"question": "Les ions permanganate $MnO_4^-$ forment un couple avec $Mn^{2+}$. Ecrire la r\u00e9action des ions permangante et des ions fer II $Fe^{2+}$.",
"answer": "On \u00e9crit les demi-r\u00e9actions d'oxydor\u00e9duction :\n$MnO_4^- + 8 H^+ + 5 e^- = Mn^{2+} + 4 H_2O$\n$Fe^{2+} + 2 e^- = Fe$\n$Fe^{2+} = Fe^{3+} + e^-$\n\nOn voit que les ions permanganate sont oxydants, ils doivent donc r\u00e9agir avec $Fe^{2+}$ pour former l'esp\u00e8ce avec laquelle $Fe^{2+}$ forment un couple dont ils sont r\u00e9ducteurs : le couple $Fe^{3+}\/Fe^{2+}$.\n\nOn trouve alors en \u00e9quilibrant les 2 demi-r\u00e9actions afin de ne plus faire apparaitre d'\u00e9lectrons :\n$MnO_4^- + 8 H^+ + 5 Fe^{2+} = Mn^{2+} + 4 H_2O + 5 Fe^{3+}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "840-2770",
"position": 7,
"duration": 30,
"question": {
"id": "2770",
"question": "Dire quelle r\u00e9action se produit \u00e0 chaque \u00e9lectrode d'une pile \u00e9lectrochimique.",
"answer": "Oxydation \u00e0 l'anode, r\u00e9duction \u00e0 la cathode.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2776",
"position": 8,
"duration": 30,
"question": {
"id": "2776",
"question": "Ecrire la relation de Nernst pour une \u00e9lectrode $Cu_{(aq)}^{2+}\/Cu_{(s)}$.",
"answer": "La demi-\u00e9quation de r\u00e9action est $Cu_{(aq)}^{2+} + 2 e^- = Cu_{(s)}$.\nOn en d\u00e9duit donc la formule donnant le potentiel en volt de cette \u00e9lectrode :\n$E = E^0_{Cu^{2+}\/Cu} + 0,03 \\log_{10} \\left( \\frac{[Cu^{2+}]}{c^0} \\right)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "840-2777",
"position": 9,
"duration": 30,
"question": {
"id": "2777",
"question": "Calculer la constante de la r\u00e9action entre $Fe^{3+}$ et $S_2O_3^{2-}$ des couples $Fe^{3+}\/Fe^{2+}$ ($E^0_1 = 0, 77$ V) et $S_4O^{2\u2212}_6 \/S_2O^{2\u2212}_3$ ($E^0_2 = 0, 08$ V).",
"answer": "Les demi-\u00e9quations de r\u00e9action sont :\n$Fe^{3+} + e^- = Fe^{2+}$\n$2 S_2O_3^{2-} = S_4O_6^{2-} +2 e^-$\n\nOn en d\u00e9duit la r\u00e9action \u00e9tudi\u00e9e :\n$2 Fe^{3+} + 2 S_2O_3^{2-} = S_4O_6^{2-} + 2 Fe^{2+}$\n\nA l'\u00e9quilbre, le quotient de r\u00e9action est \u00e9gal \u00e0 la constante d'\u00e9quilibre, donc si on regarde les concentrations \u00e0 l'\u00e9quilibre :\n$K = \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2}$.\n\nOn peut exprimer le potentiel de la solution en appliquant la formule de Nernst aux deux couples :\n$E = E^0_1 + 0,06 \\log_{10} \\left( \\frac{[Fe^{3+}]}{[Fe^{2+}]} \\right)$\n$E = E^0_2 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}]c^0}{[S_2O_3^{2-}]^2} \\right)$\n\nOn retranche alors la premi\u00e8re ligne \u00e0 la deuxi\u00e8me et on obtient :\n$0 = E^0_2 - E^0_1 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2} \\right)$\net on reconnait l'expression de $K$.\nOn inverse donc la relation et on trouve $K = 10^{\\frac{E^0_1-E^0_2}{0,03}} = 10^{23}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"841": {
"id": "841",
"name": "Quizz 28 : Oxydor\u00e9duction. Thermodynamique",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/841\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 480,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.53125,
"shared_at": "2025-03-27",
"questions": [{
"id": "841-2764",
"position": 0,
"duration": 30,
"question": {
"id": "2764",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $MnO_4^-\/Mn^{2+}$. Justifier que $MnO_4^-$ est l'oxydant.",
"answer": "Pour $MnO_4^-$, $n.o. (Mn) + 4 n.o. (O) = - I$, donc $n.o (Mn) = + VII$.\nPour $Mn^{2+}$, $n.o. (Mn) = + II$.\n\n$MnO_4^-$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2766",
"position": 1,
"duration": 30,
"question": {
"id": "2766",
"question": "Donner les nombres d'oxydation des deux esp\u00e8ces du couple $Cr_2O_7^{2-}\/Cr^{3+}$. Justifier que $Cr_2O_7^{2-}$ est l'oxydant.",
"answer": "Pour $Cr_2O_7^{2-}$, $2 n.o. (Cr) + 7 n.o. (O) = - II$, donc $n.o (Cr) = + VI$.\nPour $Cr^{3+}$, $n.o. (cr) = + III$.\n\n$Cr_2O_7^{2-}$ est bien l'oxydant car il a le nombre d'oxydation le plus \u00e9lev\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2767",
"position": 2,
"duration": 30,
"question": {
"id": "2767",
"question": "Les ions permanganate $MnO_4^-$ forment un couple avec $Mn^{2+}$. Ecrire la r\u00e9action des ions permangante et des ions fer II $Fe^{2+}$.",
"answer": "On \u00e9crit les demi-r\u00e9actions d'oxydor\u00e9duction :\n$MnO_4^- + 8 H^+ + 5 e^- = Mn^{2+} + 4 H_2O$\n$Fe^{2+} + 2 e^- = Fe$\n$Fe^{2+} = Fe^{3+} + e^-$\n\nOn voit que les ions permanganate sont oxydants, ils doivent donc r\u00e9agir avec $Fe^{2+}$ pour former l'esp\u00e8ce avec laquelle $Fe^{2+}$ forment un couple dont ils sont r\u00e9ducteurs : le couple $Fe^{3+}\/Fe^{2+}$.\n\nOn trouve alors en \u00e9quilibrant les 2 demi-r\u00e9actions afin de ne plus faire apparaitre d'\u00e9lectrons :\n$MnO_4^- + 8 H^+ + 5 Fe^{2+} = Mn^{2+} + 4 H_2O + 5 Fe^{3+}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "841-2770",
"position": 3,
"duration": 30,
"question": {
"id": "2770",
"question": "Dire quelle r\u00e9action se produit \u00e0 chaque \u00e9lectrode d'une pile \u00e9lectrochimique.",
"answer": "Oxydation \u00e0 l'anode, r\u00e9duction \u00e0 la cathode.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2776",
"position": 4,
"duration": 30,
"question": {
"id": "2776",
"question": "Ecrire la relation de Nernst pour une \u00e9lectrode $Cu_{(aq)}^{2+}\/Cu_{(s)}$.",
"answer": "La demi-\u00e9quation de r\u00e9action est $Cu_{(aq)}^{2+} + 2 e^- = Cu_{(s)}$.\nOn en d\u00e9duit donc la formule donnant le potentiel en volt de cette \u00e9lectrode :\n$E = E^0_{Cu^{2+}\/Cu} + 0,03 \\log_{10} \\left( \\frac{[Cu^{2+}]}{c^0} \\right)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2777",
"position": 5,
"duration": 30,
"question": {
"id": "2777",
"question": "Calculer la constante de la r\u00e9action entre $Fe^{3+}$ et $S_2O_3^{2-}$ des couples $Fe^{3+}\/Fe^{2+}$ ($E^0_1 = 0, 77$ V) et $S_4O^{2\u2212}_6 \/S_2O^{2\u2212}_3$ ($E^0_2 = 0, 08$ V).",
"answer": "Les demi-\u00e9quations de r\u00e9action sont :\n$Fe^{3+} + e^- = Fe^{2+}$\n$2 S_2O_3^{2-} = S_4O_6^{2-} +2 e^-$\n\nOn en d\u00e9duit la r\u00e9action \u00e9tudi\u00e9e :\n$2 Fe^{3+} + 2 S_2O_3^{2-} = S_4O_6^{2-} + 2 Fe^{2+}$\n\nA l'\u00e9quilbre, le quotient de r\u00e9action est \u00e9gal \u00e0 la constante d'\u00e9quilibre, donc si on regarde les concentrations \u00e0 l'\u00e9quilibre :\n$K = \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2}$.\n\nOn peut exprimer le potentiel de la solution en appliquant la formule de Nernst aux deux couples :\n$E = E^0_1 + 0,06 \\log_{10} \\left( \\frac{[Fe^{3+}]}{[Fe^{2+}]} \\right)$\n$E = E^0_2 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}]c^0}{[S_2O_3^{2-}]^2} \\right)$\n\nOn retranche alors la premi\u00e8re ligne \u00e0 la deuxi\u00e8me et on obtient :\n$0 = E^0_2 - E^0_1 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2} \\right)$\net on reconnait l'expression de $K$.\nOn inverse donc la relation et on trouve $K = 10^{\\frac{E^0_1-E^0_2}{0,03}} = 10^{23}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "841-2778",
"position": 6,
"duration": 30,
"question": {
"id": "2778",
"question": "A quelle condition sur les potentiels standards des deux couples consid\u00e8re t'on g\u00e9n\u00e9ralement que la r\u00e9action d'oxydor\u00e9duction entre un oxydant $A$ et un r\u00e9ducteur $B$ est totale ?",
"answer": "Il faut que le potentiel standard du couple dont $A$ est l'oxydant soit sup\u00e9rieur d'au moins 0,3 V \u00e0 celui dont $B$ est le r\u00e9ducteur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "841-2779",
"position": 7,
"duration": 30,
"question": {
"id": "2779",
"question": "Qu'est-ce qu'une dismutation ?",
"answer": "Une dismutation est une r\u00e9action chimique d'une esp\u00e8ce avec elle-m\u00eame.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2780",
"position": 8,
"duration": 30,
"question": {
"id": "2780",
"question": "On donne $E^0(S_4O^{2\u2212}_6 \/S_2O^{2\u2212}_4) = 0, 08$ V et $E^0(S_2O^{2\u2212}_3 \/S) = 0, 50$ V.\nEcrire la r\u00e9action de dismutation des ions thiosulfates $S_2O_3^{2-}$, et dire si elle est totale.\nEst-il possible de stocker des ions thiosulfates en solution aqueuse ?",
"answer": "Les deux demi-\u00e9quations d er\u00e9actions sont :\n$2 S_2O_3^{2-} = S_4O_6^{2-} + 2 e^-$\n$S_2O_3^{2-} + 6 H^+ + 4e^-= 2 S + 3 H_2O$\n\ndonc la r\u00e9action de dismutation sera :\n$ 5 S_2O_3^{2-} + 6 H^+ = 2 S_4O_6^{2-} + 2 S + 3 H_2O $\nCette r\u00e9action est totale car la diff\u00e9rence entre les potentiels standards est sup\u00e9rieure \u00e0 0,3 V.\n\nIl est toutefois possible de stocker des ions thiosulfates si la solution n'est pas acide (car la r\u00e9action de dismutation n\u00e9cessite des ions $H^+$ pour se produire).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "841-2787",
"position": 9,
"duration": 30,
"question": {
"id": "2787",
"question": "Quelles sont les diff\u00e9rentes \u00e9chelles de longueur auxquelles on peut \u00e9tudier un syst\u00e8me physique ? Donner un ordre de grandeur pour chaque.",
"answer": "Il y a l'\u00e9chelle macroscopique, o\u00f9 la mati\u00e8re apparait comme continue, et le syst\u00e8me a un tr\u00e8s grand nombre de particules. OdG : 1 m\n\nIl y a l'\u00e9chelle microscopique o\u00f9 l'on voit la mati\u00e8re comme dicopntinue, form\u00e9e de particules. OdG : 1 nm\n\nIl y a l'\u00e9chelle m\u00e9soscopique, situ\u00e9e entre les deux, o\u00f9 le syst\u00e8me pr\u00e9sente un assez grand nombre de particules pour d\u00e9finir des moyennes, mais le syst\u00e8me est suffisamment petit pour que les grandeurs thermodynamiques soient constantes \u00e0 l'\u00e9chelle du syst\u00e8me. OdG 1 \u00b5m.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2788",
"position": 10,
"duration": 30,
"question": {
"id": "2788",
"question": "Qu'est-ce qu'un syst\u00e8me thermodynamique ?",
"answer": "C'est un syst\u00e8me comprenant suffisamment de particules pour pouvoir effectuer des moyennes : c'est donc un syst\u00e8me de taille m\u00e9soscopique ou macroscopique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2789",
"position": 11,
"duration": 30,
"question": {
"id": "2789",
"question": "Quelle est la diff\u00e9rence entre un syst\u00e8me ferm\u00e9 et un syst\u00e8me isol\u00e9 ?",
"answer": "Un syst\u00e8me ferm\u00e9 n'\u00e9change pas de mati\u00e8re avec l'ext\u00e9rieur alors qu'un syst\u00e8me isol\u00e9 n'\u00e9change ni mati\u00e8re ni \u00e9nergie avec l'ext\u00e9rieur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2790",
"position": 12,
"duration": 30,
"question": {
"id": "2790",
"question": "Quelle est l'origine microscopique de la pression cin\u00e9tique exerc\u00e9e par un fluide sur une paroi ?",
"answer": "La pression cin\u00e9tique est due aux collisions des particules de fluide sur la paroi.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2792",
"position": 13,
"duration": 30,
"question": {
"id": "2792",
"question": "Quelle est la force exerc\u00e9e par l'atmosph\u00e8re sur une vitre de surface 1 m$^2$ ? Au poids de quelle masse cette force correspond ?",
"answer": "La pression atmosph\u00e9rique est de l'ordre de 10$^5$ Pa, donc la force exerc\u00e9e est $F = P S = 10^5$ N.\nCette force correspond \u00e0 une masse approximative de 10 tonnes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2794",
"position": 14,
"duration": 30,
"question": {
"id": "2794",
"question": "Comment d\u00e9finit-on une grandeur extensive ? Donner un exemple.",
"answer": "Une grandeur extensive est une grandeur telle que sa valeur pour un syst\u00e8me est la somme de sa valeur pour chaque sous-syst\u00e8me le composant.\n\nOn peut citer la masse, le volume, la quantit\u00e9 de mati\u00e8re, etc.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "841-2795",
"position": 15,
"duration": 30,
"question": {
"id": "2795",
"question": "Comment d\u00e9finit-on une grandeur intensive ? Donner un exemple.",
"answer": "Une grandeur intensive est une grandeur qui peut \u00eatre d\u00e9finie localement, elle est ind\u00e9pendante de la taille du syst\u00e8me.\n\nExemples : temp\u00e9rature, pression, concentration molaire, volume massique, etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"845": {
"id": "845",
"name": "Quizz 29 : Oxydor\u00e9duction.Thermodynamique.",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/845\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 540,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-04-01",
"questions": [{
"id": "845-2770",
"position": 0,
"duration": 30,
"question": {
"id": "2770",
"question": "Dire quelle r\u00e9action se produit \u00e0 chaque \u00e9lectrode d'une pile \u00e9lectrochimique.",
"answer": "Oxydation \u00e0 l'anode, r\u00e9duction \u00e0 la cathode.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2777",
"position": 1,
"duration": 30,
"question": {
"id": "2777",
"question": "Calculer la constante de la r\u00e9action entre $Fe^{3+}$ et $S_2O_3^{2-}$ des couples $Fe^{3+}\/Fe^{2+}$ ($E^0_1 = 0, 77$ V) et $S_4O^{2\u2212}_6 \/S_2O^{2\u2212}_3$ ($E^0_2 = 0, 08$ V).",
"answer": "Les demi-\u00e9quations de r\u00e9action sont :\n$Fe^{3+} + e^- = Fe^{2+}$\n$2 S_2O_3^{2-} = S_4O_6^{2-} +2 e^-$\n\nOn en d\u00e9duit la r\u00e9action \u00e9tudi\u00e9e :\n$2 Fe^{3+} + 2 S_2O_3^{2-} = S_4O_6^{2-} + 2 Fe^{2+}$\n\nA l'\u00e9quilbre, le quotient de r\u00e9action est \u00e9gal \u00e0 la constante d'\u00e9quilibre, donc si on regarde les concentrations \u00e0 l'\u00e9quilibre :\n$K = \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2}$.\n\nOn peut exprimer le potentiel de la solution en appliquant la formule de Nernst aux deux couples :\n$E = E^0_1 + 0,06 \\log_{10} \\left( \\frac{[Fe^{3+}]}{[Fe^{2+}]} \\right)$\n$E = E^0_2 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}]c^0}{[S_2O_3^{2-}]^2} \\right)$\n\nOn retranche alors la premi\u00e8re ligne \u00e0 la deuxi\u00e8me et on obtient :\n$0 = E^0_2 - E^0_1 + 0,03 \\log_{10} \\left( \\frac{[S_4O_6^{2-}][Fe^{2+}]^2c^0}{[S_2O_3^{2-}]^2[Fe^{3+}]^2} \\right)$\net on reconnait l'expression de $K$.\nOn inverse donc la relation et on trouve $K = 10^{\\frac{E^0_1-E^0_2}{0,03}} = 10^{23}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "845-2778",
"position": 2,
"duration": 30,
"question": {
"id": "2778",
"question": "A quelle condition sur les potentiels standards des deux couples consid\u00e8re t'on g\u00e9n\u00e9ralement que la r\u00e9action d'oxydor\u00e9duction entre un oxydant $A$ et un r\u00e9ducteur $B$ est totale ?",
"answer": "Il faut que le potentiel standard du couple dont $A$ est l'oxydant soit sup\u00e9rieur d'au moins 0,3 V \u00e0 celui dont $B$ est le r\u00e9ducteur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "845-2779",
"position": 3,
"duration": 30,
"question": {
"id": "2779",
"question": "Qu'est-ce qu'une dismutation ?",
"answer": "Une dismutation est une r\u00e9action chimique d'une esp\u00e8ce avec elle-m\u00eame.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2780",
"position": 4,
"duration": 30,
"question": {
"id": "2780",
"question": "On donne $E^0(S_4O^{2\u2212}_6 \/S_2O^{2\u2212}_4) = 0, 08$ V et $E^0(S_2O^{2\u2212}_3 \/S) = 0, 50$ V.\nEcrire la r\u00e9action de dismutation des ions thiosulfates $S_2O_3^{2-}$, et dire si elle est totale.\nEst-il possible de stocker des ions thiosulfates en solution aqueuse ?",
"answer": "Les deux demi-\u00e9quations d er\u00e9actions sont :\n$2 S_2O_3^{2-} = S_4O_6^{2-} + 2 e^-$\n$S_2O_3^{2-} + 6 H^+ + 4e^-= 2 S + 3 H_2O$\n\ndonc la r\u00e9action de dismutation sera :\n$ 5 S_2O_3^{2-} + 6 H^+ = 2 S_4O_6^{2-} + 2 S + 3 H_2O $\nCette r\u00e9action est totale car la diff\u00e9rence entre les potentiels standards est sup\u00e9rieure \u00e0 0,3 V.\n\nIl est toutefois possible de stocker des ions thiosulfates si la solution n'est pas acide (car la r\u00e9action de dismutation n\u00e9cessite des ions $H^+$ pour se produire).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "845-2787",
"position": 5,
"duration": 30,
"question": {
"id": "2787",
"question": "Quelles sont les diff\u00e9rentes \u00e9chelles de longueur auxquelles on peut \u00e9tudier un syst\u00e8me physique ? Donner un ordre de grandeur pour chaque.",
"answer": "Il y a l'\u00e9chelle macroscopique, o\u00f9 la mati\u00e8re apparait comme continue, et le syst\u00e8me a un tr\u00e8s grand nombre de particules. OdG : 1 m\n\nIl y a l'\u00e9chelle microscopique o\u00f9 l'on voit la mati\u00e8re comme dicopntinue, form\u00e9e de particules. OdG : 1 nm\n\nIl y a l'\u00e9chelle m\u00e9soscopique, situ\u00e9e entre les deux, o\u00f9 le syst\u00e8me pr\u00e9sente un assez grand nombre de particules pour d\u00e9finir des moyennes, mais le syst\u00e8me est suffisamment petit pour que les grandeurs thermodynamiques soient constantes \u00e0 l'\u00e9chelle du syst\u00e8me. OdG 1 \u00b5m.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2788",
"position": 6,
"duration": 30,
"question": {
"id": "2788",
"question": "Qu'est-ce qu'un syst\u00e8me thermodynamique ?",
"answer": "C'est un syst\u00e8me comprenant suffisamment de particules pour pouvoir effectuer des moyennes : c'est donc un syst\u00e8me de taille m\u00e9soscopique ou macroscopique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2789",
"position": 7,
"duration": 30,
"question": {
"id": "2789",
"question": "Quelle est la diff\u00e9rence entre un syst\u00e8me ferm\u00e9 et un syst\u00e8me isol\u00e9 ?",
"answer": "Un syst\u00e8me ferm\u00e9 n'\u00e9change pas de mati\u00e8re avec l'ext\u00e9rieur alors qu'un syst\u00e8me isol\u00e9 n'\u00e9change ni mati\u00e8re ni \u00e9nergie avec l'ext\u00e9rieur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2790",
"position": 8,
"duration": 30,
"question": {
"id": "2790",
"question": "Quelle est l'origine microscopique de la pression cin\u00e9tique exerc\u00e9e par un fluide sur une paroi ?",
"answer": "La pression cin\u00e9tique est due aux collisions des particules de fluide sur la paroi.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2791",
"position": 9,
"duration": 30,
"question": {
"id": "2791",
"question": "Quelle est l'interpr\u00e9tation microscopique de la temp\u00e9rature cin\u00e9tique ? Que vaut-elle pour un gaz parfait monoatomique ?",
"answer": "La temp\u00e9rature cin\u00e9tique est une mesure de l'agitation des particules.\nPour un gaz parfait monoatomique, on d\u00e9finit la temp\u00e9rature $T$ telle que :\n$<E_c> = < \\frac12 mv^2> = \\frac32 k_B T.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2792",
"position": 10,
"duration": 30,
"question": {
"id": "2792",
"question": "Quelle est la force exerc\u00e9e par l'atmosph\u00e8re sur une vitre de surface 1 m$^2$ ? Au poids de quelle masse cette force correspond ?",
"answer": "La pression atmosph\u00e9rique est de l'ordre de 10$^5$ Pa, donc la force exerc\u00e9e est $F = P S = 10^5$ N.\nCette force correspond \u00e0 une masse approximative de 10 tonnes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2793",
"position": 11,
"duration": 30,
"question": {
"id": "2793",
"question": "Quelles sont les hypoth\u00e8ses du gaz parfait ?",
"answer": "Un gaz parfait est constitu\u00e9 de particules ponctuelles sans interactions \u00e0 distance, et soumises uniquement \u00e0 des chocs \u00e9lastiques entre lles et avec les parois.\nOn suppose de plus aucun mouvement d'ensemble $<\\vec{v}> = \\vec{0}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2794",
"position": 12,
"duration": 30,
"question": {
"id": "2794",
"question": "Comment d\u00e9finit-on une grandeur extensive ? Donner un exemple.",
"answer": "Une grandeur extensive est une grandeur telle que sa valeur pour un syst\u00e8me est la somme de sa valeur pour chaque sous-syst\u00e8me le composant.\n\nOn peut citer la masse, le volume, la quantit\u00e9 de mati\u00e8re, etc.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2795",
"position": 13,
"duration": 30,
"question": {
"id": "2795",
"question": "Comment d\u00e9finit-on une grandeur intensive ? Donner un exemple.",
"answer": "Une grandeur intensive est une grandeur qui peut \u00eatre d\u00e9finie localement, elle est ind\u00e9pendante de la taille du syst\u00e8me.\n\nExemples : temp\u00e9rature, pression, concentration molaire, volume massique, etc",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2796",
"position": 14,
"duration": 30,
"question": {
"id": "2796",
"question": "Donner l'\u00e9quation d'\u00e9tat du gaz parfait en pr\u00e9cisant l'unit\u00e9 et la signification de chaque grandeur.",
"answer": "$PV = n RT$\n$P$ : pression du gaz, en Pa\n$V$ : volume, en m$^3$\n$N$ : quantit\u00e9 de mati\u00e8re, en mol\n$R$ : constante de gaz parfaits, $R = 8,314$ J.mol$^{-1}$.K$^{-1}$\n$T$ : temp\u00e9rature en K",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2797",
"position": 15,
"duration": 30,
"question": {
"id": "2797",
"question": "Comment est d\u00e9finie l'\u00e9nergie cin\u00e9tique interne d'un gaz ? \nEt son \u00e9nergie interne ? Que vaut-elle pour un gaz parfait monoatomique ?",
"answer": "L'\u00e9nergie cin\u00e9tique interne est l'\u00e9nergie cin\u00e9tique de toutes les particules lorsque l'on se place dans le r\u00e9f\u00e9rentiel de centre de masse du gaz, tel que $<\\vec{v}> = \\vec{0}$.\n\nL'\u00e9nergie interne d'un gaz est la somme de son \u00e9nergie cin\u00e9tique interne et de son \u00e9nergie potentielle interne.\nPour un gaz parfait monoatomique, il n'y a pas d'interactions \u00e0 distance entre particules donc l'\u00e9nergie potentielle interne est nulle.\nOn a alors $U= E_{cin,i} = N <\\frac12 m v^2> = N \\frac32 k_B T = \\frac32 n R T$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "845-2798",
"position": 16,
"duration": 30,
"question": {
"id": "2798",
"question": "Comment est d\u00e9finie la capacit\u00e9 calorifique \u00e0 volume constant d'un corps ?\nQue vaut-elle pour un gaz parfait monoatomique ?",
"answer": "C'est la d\u00e9riv\u00e9e de l'\u00e9nergie interne par rapport \u00e0 la temp\u00e9rature, ou encore la quantit\u00e9 d'\u00e9nergie \u00e0 fournir pour \u00e9lever sa temp\u00e9rature de 1K.\nPour un GPM, $U = \\frac32 n RT$, donc $C_V = \\frac32 nR$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "845-2799",
"position": 17,
"duration": 30,
"question": {
"id": "2799",
"question": "Comment s'appellent les deux points remarquables d'un diagramme de phase d'un corps pur ? Que repr\u00e9sentent-ils ?",
"answer": "Il y a le point triple, qui correspond \u00e0 la temp\u00e9rature et \u00e0 la pression auxquelles les trois phases (solide, liquide et gaz) coexistent \u00e0 l'\u00e9quilibre, et le point critique, qui correspond \u00e0 la temp\u00e9rature et \u00e0 la pression \u00e0 partir desquelles la transition liquide-gaz n'est plus perceptible (on est alors dans l'\u00e9tat de fluide supercritique).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"847": {
"id": "847",
"name": "Quizz 30 : Thermodynamique, introduction",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/847\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-04-03",
"questions": [{
"id": "847-2790",
"position": 0,
"duration": 30,
"question": {
"id": "2790",
"question": "Quelle est l'origine microscopique de la pression cin\u00e9tique exerc\u00e9e par un fluide sur une paroi ?",
"answer": "La pression cin\u00e9tique est due aux collisions des particules de fluide sur la paroi.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2791",
"position": 1,
"duration": 30,
"question": {
"id": "2791",
"question": "Quelle est l'interpr\u00e9tation microscopique de la temp\u00e9rature cin\u00e9tique ? Que vaut-elle pour un gaz parfait monoatomique ?",
"answer": "La temp\u00e9rature cin\u00e9tique est une mesure de l'agitation des particules.\nPour un gaz parfait monoatomique, on d\u00e9finit la temp\u00e9rature $T$ telle que :\n$<E_c> = < \\frac12 mv^2> = \\frac32 k_B T.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2796",
"position": 2,
"duration": 30,
"question": {
"id": "2796",
"question": "Donner l'\u00e9quation d'\u00e9tat du gaz parfait en pr\u00e9cisant l'unit\u00e9 et la signification de chaque grandeur.",
"answer": "$PV = n RT$\n$P$ : pression du gaz, en Pa\n$V$ : volume, en m$^3$\n$N$ : quantit\u00e9 de mati\u00e8re, en mol\n$R$ : constante de gaz parfaits, $R = 8,314$ J.mol$^{-1}$.K$^{-1}$\n$T$ : temp\u00e9rature en K",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2797",
"position": 3,
"duration": 30,
"question": {
"id": "2797",
"question": "Comment est d\u00e9finie l'\u00e9nergie cin\u00e9tique interne d'un gaz ? \nEt son \u00e9nergie interne ? Que vaut-elle pour un gaz parfait monoatomique ?",
"answer": "L'\u00e9nergie cin\u00e9tique interne est l'\u00e9nergie cin\u00e9tique de toutes les particules lorsque l'on se place dans le r\u00e9f\u00e9rentiel de centre de masse du gaz, tel que $<\\vec{v}> = \\vec{0}$.\n\nL'\u00e9nergie interne d'un gaz est la somme de son \u00e9nergie cin\u00e9tique interne et de son \u00e9nergie potentielle interne.\nPour un gaz parfait monoatomique, il n'y a pas d'interactions \u00e0 distance entre particules donc l'\u00e9nergie potentielle interne est nulle.\nOn a alors $U= E_{cin,i} = N <\\frac12 m v^2> = N \\frac32 k_B T = \\frac32 n R T$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "847-2798",
"position": 4,
"duration": 30,
"question": {
"id": "2798",
"question": "Comment est d\u00e9finie la capacit\u00e9 calorifique \u00e0 volume constant d'un corps ?\nQue vaut-elle pour un gaz parfait monoatomique ?",
"answer": "C'est la d\u00e9riv\u00e9e de l'\u00e9nergie interne par rapport \u00e0 la temp\u00e9rature, ou encore la quantit\u00e9 d'\u00e9nergie \u00e0 fournir pour \u00e9lever sa temp\u00e9rature de 1K.\nPour un GPM, $U = \\frac32 n RT$, donc $C_V = \\frac32 nR$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2799",
"position": 5,
"duration": 30,
"question": {
"id": "2799",
"question": "Comment s'appellent les deux points remarquables d'un diagramme de phase d'un corps pur ? Que repr\u00e9sentent-ils ?",
"answer": "Il y a le point triple, qui correspond \u00e0 la temp\u00e9rature et \u00e0 la pression auxquelles les trois phases (solide, liquide et gaz) coexistent \u00e0 l'\u00e9quilibre, et le point critique, qui correspond \u00e0 la temp\u00e9rature et \u00e0 la pression \u00e0 partir desquelles la transition liquide-gaz n'est plus perceptible (on est alors dans l'\u00e9tat de fluide supercritique).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2802",
"position": 6,
"duration": 30,
"question": {
"id": "2802",
"question": "Quelle est la composition d'un autocuiseur de 25,0 L contenant $m=2,000$ kg d'eau \u00e0 la temp\u00e9rature de 130\u00b0C, sachant qu'\u00e0 cette temp\u00e9rature l'eau liquide a une masse volumique de 1,000 kg\/L et la vapeur saturante de 2,000 g\/L.",
"answer": "On va utiliser la loi des moments comme vue dans le diagramme de Clapeyron.\nOn a besoin de $v$ le volume massique de l'eau l'autocuiseur, $v_l$ celui de l'eau liquide \u00e0 130\u00b0C et $v_g$ celui de la vapeur saturante \u00e0 130\u00b0C.\n\nSi on appelle $m_l$ la masse d'eau liquide et $m_g$ la masse de la vapeur on a d'apr\u00e8s la loi des moments :\n$$\\frac{m_l}{m} = \\frac{v_g-v}{v_g-v_l};$$\n$$\\frac{m_g}{m} = \\frac{v-v_l}{v_g-v_l}.$$\n\nPour les applications num\u00e9riques, $v = 12,5$ L\/kg, $v_l = 1,000$ L\/kg et $v_g = 500,0$ L\/kg.\nOn trouve donc $m_l = 1,95$ kg et $m_g = 50$ g.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "847-2805",
"position": 7,
"duration": 30,
"question": {
"id": "2805",
"question": "Quel est le travail infinit\u00e9simal $\\delta W$ des forces de pression re\u00e7u par un syst\u00e8me \u00e0 la pression $P$ lors d'une \u00e9volution infinit\u00e9simale faisant varier son volume de $dV$.\nQue vaut le travail des forces de pression re\u00e7u par un syst\u00e8me \u00e9voluant de mani\u00e8re monobare d'un volume $V_1$ \u00e0 un volume $V_2$ ?",
"answer": "$\\delta W = - P dV$\n$W = P_{ext} (V_1 -V_2)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2806",
"position": 8,
"duration": 30,
"question": {
"id": "2806",
"question": "Qu'est-ce qu'une paroi adiabiatique ?",
"answer": "C'est une paroi emp\u00eachant les \u00e9changes de chaleur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "847-2807",
"position": 9,
"duration": 30,
"question": {
"id": "2807",
"question": "Quel est le travail des forces de pression re\u00e7u par un gaz parfait monoatomique passant de l'\u00e9tat $(P_0,T_0,V_0)$ \u00e0 un \u00e9tat $(P_1=3P_0,T_1,V_1)$ en suivant une transformation isotherme ?",
"answer": "Puisque l'\u00e9volution est isotherme, $T_1=T_0$.\n\nOn applique la relation d'\u00e9tat du GP dans l'\u00e9tat initial et dans l'\u00e9tat final et on a $P_0 V_0 = n R T_0 = n R T_1 = P_1 V_1$\nOn a donc $V_1 = \\frac{P_0V_0}{P_1} = V_0\/3$.\n\nLe travail des forces de pression est alors :\n$$W = \\int_{V_0}^{V_0\/3} - P dV$$\nor le long de l'\u00e9volution $PV = n R T_0 = P_0 V_0$ donc $P = \\frac{P_0 V_0}{V}$, on a donc :\n$$W = \\int_{V0}^{V_0\/3} - \\frac{P_0V_0dV}{V} = \\left[ P_0 V_0 \\ln (V) \\right]_{V_0\/3}^{V_0} = P_0 V_0 \\ln 3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "847-2809",
"position": 10,
"duration": 30,
"question": {
"id": "2809",
"question": "Qu'est-ce qu'une fonction d'\u00e9tat ? Donner un exemple et un contre-exemple.",
"answer": "Une fonction d'\u00e9tat est une grandeur dont la valeur ne d\u00e9pend que de l'\u00e9tat du syst\u00e8me thermodynamique, par exemple l'\u00e9nergie interne, l'enthalpie, l'entropie etc.\nLa chaleur ou le travail re\u00e7us par un syst\u00e8me thermodynamique ne sont pas des fonctions d'\u00e9tat.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"848": {
"id": "848",
"name": "Quizz 31 : Principe de la thermodynamique",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/848\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 510,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-04-10",
"questions": [{
"id": "848-2804",
"position": 0,
"duration": 30,
"question": {
"id": "2804",
"question": "Quelle est la diff\u00e9rence entre une \u00e9volution isobare et une \u00e9volution monobare ?",
"answer": "Lors d'une \u00e9volution isobare, la pression du syst\u00e8me reste constante. Lors d'une \u00e9volution monobare, c'est la pression ext\u00e9rieure qui reste constante.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2805",
"position": 1,
"duration": 30,
"question": {
"id": "2805",
"question": "Quel est le travail infinit\u00e9simal $\\delta W$ des forces de pression re\u00e7u par un syst\u00e8me \u00e0 la pression $P$ lors d'une \u00e9volution infinit\u00e9simale faisant varier son volume de $dV$.\nQue vaut le travail des forces de pression re\u00e7u par un syst\u00e8me \u00e9voluant de mani\u00e8re monobare d'un volume $V_1$ \u00e0 un volume $V_2$ ?",
"answer": "$\\delta W = - P dV$\n$W = P_{ext} (V_1 -V_2)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2806",
"position": 2,
"duration": 30,
"question": {
"id": "2806",
"question": "Qu'est-ce qu'une paroi adiabiatique ?",
"answer": "C'est une paroi emp\u00eachant les \u00e9changes de chaleur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2807",
"position": 3,
"duration": 30,
"question": {
"id": "2807",
"question": "Quel est le travail des forces de pression re\u00e7u par un gaz parfait monoatomique passant de l'\u00e9tat $(P_0,T_0,V_0)$ \u00e0 un \u00e9tat $(P_1=3P_0,T_1,V_1)$ en suivant une transformation isotherme ?",
"answer": "Puisque l'\u00e9volution est isotherme, $T_1=T_0$.\n\nOn applique la relation d'\u00e9tat du GP dans l'\u00e9tat initial et dans l'\u00e9tat final et on a $P_0 V_0 = n R T_0 = n R T_1 = P_1 V_1$\nOn a donc $V_1 = \\frac{P_0V_0}{P_1} = V_0\/3$.\n\nLe travail des forces de pression est alors :\n$$W = \\int_{V_0}^{V_0\/3} - P dV$$\nor le long de l'\u00e9volution $PV = n R T_0 = P_0 V_0$ donc $P = \\frac{P_0 V_0}{V}$, on a donc :\n$$W = \\int_{V0}^{V_0\/3} - \\frac{P_0V_0dV}{V} = \\left[ P_0 V_0 \\ln (V) \\right]_{V_0\/3}^{V_0} = P_0 V_0 \\ln 3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "848-2808",
"position": 4,
"duration": 30,
"question": {
"id": "2808",
"question": "Exprimer le premier principe de la thermodynamique en utilisant l'\u00e9nergie interne.",
"answer": "Le premier principe de la thermodynamique dit que l'\u00e9nergie est une grandeur extensive conservative, ce qui signifie que pour un syst\u00e8me thermodynamique la variation d'\u00e9nergie interne et d'\u00e9nergie cin\u00e9tique est \u00e9gale \u00e0 la somme du travail et de la chaleur re\u00e7us : $\\Delta U + \\Delta E_c = Q + W$.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2809",
"position": 5,
"duration": 30,
"question": {
"id": "2809",
"question": "Qu'est-ce qu'une fonction d'\u00e9tat ? Donner un exemple et un contre-exemple.",
"answer": "Une fonction d'\u00e9tat est une grandeur dont la valeur ne d\u00e9pend que de l'\u00e9tat du syst\u00e8me thermodynamique, par exemple l'\u00e9nergie interne, l'enthalpie, l'entropie etc.\nLa chaleur ou le travail re\u00e7us par un syst\u00e8me thermodynamique ne sont pas des fonctions d'\u00e9tat.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2814",
"position": 6,
"duration": 30,
"question": {
"id": "2814",
"question": "Comment est d\u00e9finie l'enthalpie d'un syst\u00e8me ?",
"answer": "L'enthalpie $H$ d'un syst\u00e8me d'\u00e9nergie interne $U$, de pression $P$ et de volume $V$ est $H = U + PV$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2815",
"position": 7,
"duration": 30,
"question": {
"id": "2815",
"question": "Exprimer le premier principe de la thermodynamique en utilisant l'enthalpie.",
"answer": "La variation d'enthalpie et d'\u00e9nergie cin\u00e9tique d'un syst\u00e8me thermodynamique au cours d'une transformation isobare est \u00e9gale \u00e0 la somme de la chaleur et des travaux re\u00e7us, \u00e0 l'exception des travaux des forces de pression : $\\Delta H + \\Delta E_c = Q + W'$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2816",
"position": 8,
"duration": 30,
"question": {
"id": "2816",
"question": "Comment est d\u00e9finie la capacit\u00e9 calorifique \u00e0 pression constante ?",
"answer": "C'est la d\u00e9rive de l'enthalpie par rapport \u00e0 la temp\u00e9rature : $C_p = \\frac{dH}{dT}$, ou bien l'\u00e9nergie \u00e0 fournir \u00e0 un corps pour \u00e9lever sa temp\u00e9rature de 1K, en maintenant la pression constante.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2817",
"position": 9,
"duration": 30,
"question": {
"id": "2817",
"question": "Quel est le lien entre capacit\u00e9 calorifique \u00e0 volume constant et capacit\u00e9 calorifique \u00e0 pression constante :\n- pour un gaz parfait ?\n- pour une phase condens\u00e9e ?",
"answer": "Pour un gaz parfait, $C_P = C_V + n R$.\nPour une phase condens\u00e9e, $C_p \\simeq C_V$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2818",
"position": 10,
"duration": 30,
"question": {
"id": "2818",
"question": "Qu'est-ce que l'enthalpie massique de fusion de la glace ?",
"answer": "C'est l'\u00e9nergie n\u00e9cessaire pour faire passer un kilogramme d'eau \u00e0 l'\u00e9tat solide \u00e0 l'\u00e9tat liquide, en restant \u00e0 la temp\u00e9rature de transition de phase.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2820",
"position": 11,
"duration": 30,
"question": {
"id": "2820",
"question": "Enoncer le deuxi\u00e8me principe de la thermodynamique.\nQue traduit-il ?",
"answer": "Le deuxi\u00e8me principe de la thermodynamique stipule qu'il existe une grandeur extensive appel\u00e9e entropie qui ne peut \u00eatre d\u00e9truite.\nIl traduit l'irr\u00e9versibilit\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2821",
"position": 12,
"duration": 30,
"question": {
"id": "2821",
"question": "Comment doit-on faire pour d\u00e9terminer si une \u00e9volution est r\u00e9versible ou non ?",
"answer": "Il faut r\u00e9ussir \u00e0 d\u00e9terminer le terme de cr\u00e9ation d'entropie $S_{cr}$. Si ce terme est nul, alors l'\u00e9volution est r\u00e9versible, si il est strictement positif, l'\u00e9volution est irr\u00e9versible.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2822",
"position": 13,
"duration": 30,
"question": {
"id": "2822",
"question": "Donner deux exemples de sources d'irr\u00e9versiblit\u00e9.",
"answer": "On peut citer les inhomog\u00e9n\u00e9it\u00e9s de temp\u00e9ratures, de concentration, de pression, les frottements, la viscosit\u00e9, l'effet Joule...",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2823",
"position": 14,
"duration": 30,
"question": {
"id": "2823",
"question": "Que vaut l'entropie re\u00e7ue par un syst\u00e8me au cours d'une \u00e9volution monotherme pendant laquelle il re\u00e7oit une chaleur $Q$ ?",
"answer": "Si on appelle $T_0$ la temp\u00e9rature de l'ext\u00e9rieur, $S_{ech} = \\frac{Q}{T_0}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "848-2824",
"position": 15,
"duration": 30,
"question": {
"id": "2824",
"question": "Montrer que l'\u00e9volution d'un bloc de m\u00e9tal \u00e0 la temp\u00e9rature $T_1\\neq 0\u00b0C$ plong\u00e9 dans de l'eau glac\u00e9e est irr\u00e9versible.",
"answer": "Prenons comme syst\u00e8me le bloc de m\u00e9tal, et appelons $C$ sa capacit\u00e9 thermique, et $T = 273,15$ la temp\u00e9rature finale du syst\u00e8me, \u00e9gale \u00e0 celle du bain de glace.\n\nSi on effectue un bilan d'enthalpie, on a $\\Delta H = C (T-T_1) = Q$.\nSi on calcule la variation d'entropie on a $\\Delta S = C \\ln \\left( \\frac{T}{T_1} \\right)$.\n\nOn peut alors calculer l'entropie cr\u00e9e $S_{cr} = \\Delta S - S_{ech} = \\Delta S - \\frac{Q}{T}$ car l'\u00e9volution est monotherme.\n\nOn a donc :\n$$S_{cr} = C \\left[ \\ln \\left( \\frac{T}{T_1} \\right) - \\frac{T-T_1}{T} \\right] > 0.$$ \n\nL'entropie cr\u00e9e est strictement positive, on en d\u00e9duit donc que l'\u00e9volution est irr\u00e9versible.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "848-2825",
"position": 16,
"duration": 30,
"question": {
"id": "2825",
"question": "Enoncer les lois de Laplace pour un gaz parfait, en pr\u00e9cisant dans quel cadre on peut les utiliser.",
"answer": "Au cours de l'\u00e9volution adiabatique r\u00e9versible (donc isentropique) d'un gaz parfait, on a :\n$$TV^{\\gamma-1} =cte \\qquad PV^\\gamma =cte  \\qquad T^{\\gamma}P^{1-\\gamma} =cte $$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"744": {
"id": "744",
"name": "Quizz 06 : Signaux p\u00e9riodiques, interf\u00e9rences",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/744\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "115",
"value": "Signaux",
"field_id": "23",
"created_at": "2017-08-21 12:25:59",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 285,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-03",
"questions": [{
"id": "744-2577",
"position": 0,
"duration": 30,
"question": {
"id": "2577",
"question": "Quel est le lien entre p\u00e9riode $T$, fr\u00e9quence $f$ et pulsation $\\omega$ d'un signal sinuso\u00efdal ?",
"answer": "$f = \\frac{1}{T} = \\frac{\\omega}{2 \\pi}$\n$T = \\frac{1}{f} = \\frac{2 \\pi}{\\omega}$\n$\\omega = 2 \\pi f = \\frac{2 \\pi}{T}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "744-2580",
"position": 1,
"duration": 45,
"question": {
"id": "2580",
"question": "Pour un signal se propageant \u00e0 la c\u00e9l\u00e9rit\u00e9 c dans le sens des x croissant dont on connait l'\u00e9volution temporelle en une position $x_0$ : $g(t)=s(x_0,t)$, d\u00e9terminer la forme du signal \u00e0 l'instant $t_0$ : $f(x)=s(x,t_0)$.",
"answer": "Le signal mesur\u00e9 en $x$ \u00e0 l'instant $t_0$ est le m\u00eame que celui mesur\u00e9 \u00e0 la position $x_0$ \u00e0 l'instant $t$ tel que $t - t_0 = (x_0\u2212x)\/c$, donc $t=t_0\u2212(x\u2212x_0)\/c$ et on peut alors \u00e9crire :\n$f(x) = s(x,t_0) = s(x_0, t_0 - (x-x_0)\/c) = g(t_0 - (x-x_0)\/c)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "744-2581",
"position": 2,
"duration": 30,
"question": {
"id": "2581",
"question": "Ecrire la formule g\u00e9n\u00e9rale d'une onde progressive sinuso\u00efdale.\nDonner le lien entre fr\u00e9quence et longueur d'onde.",
"answer": "Une onde progressive sinuso\u00efdale \u00e0 la c\u00e9l\u00e9rit\u00e9 $c$, de p\u00e9riode $T$ et de longueur d'onde $\\lambda$ s'\u00e9crit g\u00e9n\u00e9ralement :\n$s(x,t) = A \\cos ( 2 \\pi (\\frac{t}{T} - \\frac{x}{\\lambda}) + \\phi)$.\n\nOn a alors $ \\lambda f = c$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "744-2582",
"position": 3,
"duration": 60,
"question": {
"id": "2582",
"question": "On envoie une onde progressive sinuso\u00efdale monodimensionnelle en direction de deux \u00e9metteurs s\u00e9par\u00e9s de la distance $d$. A quelle condition sur $d$ et la longueur d'onde les deux signaux re\u00e7us sont en phase ? En opposition de phase ?\n\nComment rep\u00e9rer ces situations \u00e0 l'oscilloscope ?",
"answer": "Les deux signaux sont en phase lorsque les deux \u00e9metteurs sont s\u00e9par\u00e9s d'un nombre entier de longueur d'onde : $d = n \\lambda$, $n \\in \\mathbb{N}$.\n\nIls sont en opposition de phase lorsqu'i y a un nombre impair de demi-longueur d'onde entre eux : $d = \\frac{2 p + 1}{2} \\lambda$, $p \\in \\mathbb{N}$. \n\nPour rep\u00e9rer ces situations \u00e0 l'oscilloscope, on utilise le mode XY o\u00f9 on trace le second signal en fonction du premier. Dans le cas d'un d\u00e9phasage quelconque, on observe une ellipse, qui s'aplatit en un segment de droite lorsque le signaux sont en phase ou en opposition de phase.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "744-2583",
"position": 4,
"duration": 60,
"question": {
"id": "2583",
"question": "Ecrire la formule des interf\u00e9rences pour la somme de deux ondes progressives sinuso\u00efdales $s_1(x,t) = A_1 \\cos (\\omega t + \\phi_1)$ et $s_2 (x,t) = A_2 \\cos (\\omega t + \\phi_2)$.\nA quelle condition sur $\\phi_1$ et $\\phi_2$ observe t'on des interf\u00e9rences constructives ? destructives ?",
"answer": "$s(x,t) = s_1(x,t) + s_2(x,t) = A \\cos (\\omega t + \\phi)$ avec\n$A = \\sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \\cos (\\phi_1 - \\phi_2)}$\n\nD\u00e9monstration : \n$s(x,t) = A_1 \\cos (\\omega t+ \\phi_1) + A_2 \\cos (\\omega t +\\phi_2)$\n$= A_1 [ \\cos \\omega t \\cos \\phi_1 - \\sin \\omega t \\sin \\phi_1 ] + A_2 [ \\cos \\omega t \\cos \\phi_2 - \\sin \\omega t \\sin \\phi_2 ] $\n$ = ( A_1 \\cos \\phi_1 + A_2 \\cos \\phi_2) \\cos \\omega t - (A_1 \\sin \\phi_1 + A_2 \\sin \\phi_2) \\sin \\omega t$\non reconnait alors une des formes d'un signal sinuso\u00efdal $A \\cos (\\omega t + \\phi) = A [ \\cos \\omega t \\cos \\phi - \\sin \\omega t \\sin \\phi ]$, et on doit alors r\u00e9soudre le syst\u00e8me de deux \u00e9quations \u00e0 deux inconnues ($A$ et $\\phi$) suivant :\n$A \\cos \\phi = ( A_1 \\cos \\phi_1 + A_2 \\cos \\phi_2)$\n$A \\sin \\phi = ( A_1 \\sin \\phi_1 + A_2 \\sin \\phi_2)$\n\nEn prenant la somme des carr\u00e9s des deux \u00e9quations on trouve :\n$A^2 = ( A_1 \\cos \\phi_1 + A_2 \\cos \\phi_2)^2 + ( A_1 \\sin \\phi_1 + A_2 \\sin \\phi_2)^2 = A_1^2 + A_2^2 + 2 A_1A_2 (\\cos \\phi_1 \\cos \\phi_2 + \\sin \\phi_1 \\sin \\phi_2)$ d'o\u00f9 la formule des interf\u00e9rences.\n\nOn obtient des interf\u00e9rences constructives quand $A$ est maximal donc quand $\\cos (\\phi_1 - \\phi_2) = 1$, c'est-\u00e0-dire quand $\\phi_1 - \\phi_2 = 2 k \\pi$, $k \\in \\mathbb{N}$ : les deux signaux sont alors en phase.\n\nOn obtient des interf\u00e9rences destructives quand $A$ est minimal donc quand $\\cos (\\phi_1 - \\phi_2) = - 1$, c'est-\u00e0-dire quand $\\phi_1 - \\phi_2 = (2 k + 1) \\pi$, $k \\in \\mathbb{N}$ : les deux signaux sont alors en opposition de phase.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "744-2696",
"position": 5,
"duration": 30,
"question": {
"id": "2696",
"question": "Quel est l'int\u00e9r\u00eat de l'\u00e9tude des signaux sinuso\u00efdaux pour l'\u00e9tude des signaux p\u00e9riodiques ?",
"answer": "On peut d\u00e9composer tout signal p\u00e9riodique comme une somme de signaux sinuso\u00efdaux.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "744-2697",
"position": 6,
"duration": 30,
"question": {
"id": "2697",
"question": "Ecrire la s\u00e9rie de Fourier pour la d\u00e9composition d'un signal p\u00e9riodique $s(t)$ de p\u00e9riode $T$.",
"answer": "On peut \u00e9crire $s(t) = a_0 + \\sum_n \\left[a_n \\cos \\left(2 \\pi n \\frac{t}{T} \\right) + b_n \\sin \\left(2 \\pi n \\frac{t}{T} \\right) \\right]$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1263": {
"id": "1263",
"name": "Fonctions usuelles",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1263\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-14",
"questions": [{
"id": "1263-2994",
"position": 0,
"duration": 30,
"question": {
"id": "2994",
"question": "Compl\u00e9ter : $\\ln(x\\square{}y)=\\ln(x)\\square{}\\ln(y)$",
"answer": "$\\ln(x\\times y)=\\ln(x)+\\ln(y)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-2993",
"position": 1,
"duration": 30,
"question": {
"id": "2993",
"question": "Compl\u00e9ter : $\\exp(x\\square y)=\\exp(x)\\square\\exp(y)$",
"answer": "$\\exp(x+y)=\\exp(x)\\times\\exp(y)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3003",
"position": 2,
"duration": 30,
"question": {
"id": "3003",
"question": "Compl\u00e9ter : $\\forall x\\in\\square{}\\ e^{\\ln x}=\\square$.",
"answer": "$\\forall x\\in\\mathbf{R}_+^\\star\\ e^{\\ln x}=x$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3004",
"position": 3,
"duration": 30,
"question": {
"id": "3004",
"question": "Compl\u00e9ter : $\\forall x\\in\\square{}\\ \\ln (e^x)=\\square$.",
"answer": "$\\forall x\\in\\mathbf{R}\\ \\ln (e^x)=x$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3006",
"position": 4,
"duration": 30,
"question": {
"id": "3006",
"question": "D\u00e9finition de la fonction puissance d'exposant $a$.",
"answer": "\\[\\mathbf{R}_+^\\star\\to\\mathbf{R}\\\\x\\mapsto e^{a\\ln x}\\]\n\n(on d\u00e9finit donc $x^a$ par $e^{a\\ln x}$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3009",
"position": 5,
"duration": 30,
"question": {
"id": "3009",
"question": "D\u00e9riv\u00e9e de $x^a$",
"answer": "$ax^{a-1}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3029",
"position": 6,
"duration": 30,
"question": {
"id": "3029",
"question": "D\u00e9finition de la fonction arcsinus.",
"answer": "Pour tout $x\\in[-1;1]$, $\\arcsin(x)$ est l'unique angle $\\theta\\in[-\\frac{\\pi}{2};\\frac{\\pi}{2}]$ tel que $\\sin \\theta=x$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3030",
"position": 7,
"duration": 30,
"question": {
"id": "3030",
"question": "D\u00e9finition de la fonction arccosinus.",
"answer": "Pour tout $x\\in[-1;1]$, $\\arccos(x)$ est l'unique angle $\\theta\\in[0;\\pi]$ tel que $\\cos\\theta=x$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3031",
"position": 8,
"duration": 30,
"question": {
"id": "3031",
"question": "D\u00e9finition de la fonction arctangente.",
"answer": "Pour tout $x\\in\\mathbf{R}$, $\\arctan(x)$ est l'unique angle $\\theta\\in]-\\frac{\\pi}{2};\\frac{\\pi}{2}[$ tel que $\\tan\\theta = x$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3032",
"position": 9,
"duration": 30,
"question": {
"id": "3032",
"question": "Ensemble de d\u00e9rivabilit\u00e9 et d\u00e9riv\u00e9e de la fonction $\\arcsin$.",
"answer": "$\\arcsin$ est d\u00e9rivable sur $]-1;1[$.\nPour tout $x\\in]-1;1[$, $\\arcsin^\\prime(x)=\\dfrac{1}{\\sqrt{1-x^2}}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3033",
"position": 10,
"duration": 30,
"question": {
"id": "3033",
"question": "Ensemble de d\u00e9rivabilit\u00e9 et d\u00e9riv\u00e9e de la fonction $\\arccos$.",
"answer": "$\\arccos$ est d\u00e9rivable sur $]-1;1[$.\nPour tout $x\\in]-1;1[$, $\\arccos^\\prime(x)=-\\dfrac{1}{\\sqrt{1-x^2}}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3034",
"position": 11,
"duration": 30,
"question": {
"id": "3034",
"question": "Ensemble de d\u00e9rivabilit\u00e9 et d\u00e9riv\u00e9e de la fonction $\\arctan$.",
"answer": "$\\arctan$ est d\u00e9rivable sur $\\mathbf{R}$.\nPour tout $x\\in\\mathbf{R}$, $\\arctan^\\prime(x)=\\dfrac{1}{1+x^2}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1263-3038",
"position": 12,
"duration": 30,
"question": {
"id": "3038",
"question": "Variations et limites de la fonction $\\arctan$.",
"answer": "Strictement croissante sur $\\mathbf{R}$.\n$\\displaystyle\\lim_{x\\to-\\infty}\\arctan x=-\\frac{\\pi}{2};\\quad\\lim_{x\\to+\\infty}\\arctan x=\\frac{\\pi}{2}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1232": {
"id": "1232",
"name": "Quizz 32 : Machines thermiques",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1232\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "109",
"value": "Thermodynamique",
"field_id": "23",
"created_at": "2017-08-21 12:12:43",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 90,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-05-15",
"questions": [{
"id": "1232-2832",
"position": 0,
"duration": 30,
"question": {
"id": "2832",
"question": "Effectuer le bilan d'\u00e9nergie et d'entropie pour un moteur ditherme.\nEn d\u00e9duire le sens effectif des transferts d'\u00e9nergie. En d\u00e9duire le rendement maximal de ce moteur. ",
"answer": "Appelons $W$ le travail fourni par l'ext\u00e9rieur au fluide sur un cycle, $Q_c$ la chaleur fournie par la source chaude \u00e0 la temp\u00e9rature $T_c$ et $Q_f$ celle fournie par la source froide \u00e0 $T_f$. \nBilan d'\u00e9nergie sur un cycle de fluide : $\\Delta U = W + Q_f + Q_c = 0$ car $U$ est une fonction d'\u00e9tat.\nBilan d'entropie sur un cycle de fluide : $\\Delta S = S_{ech} + S_{cr} = \\frac{Q_f}{T_f} + \\frac{Q_c}{T_c} + S_{cr} = 0$ car $S$ est une fonction d'\u00e9tat.\n\nOn a donc $\\frac{Q_f}{T_f} + \\frac{Q_c}{T_c} = -  S_{cr} \\leq 0$. \nDe plus, pour un moteur, $W < 0$ car le fluide fournit effectivement du travail \u00e0 l'ext\u00e9rieur, donc $Q_f+Q_c = - W > 0$.\n\nOn en d\u00e9duit donc, puisque $T_c > T_f$ que $Q_c >0$ et $Q_f<0$.\n\nL'\u00e9nergie fournie au moteur est donc la chaleur re\u00e7ue de la source chaude $Q_c$, et l'\u00e9nergie utile est le travail $-W$.\nLe rendement est donc $\\eta = \\frac{-W}{Q_c} = 1 + \\frac{Q_f}{Q_c} \\leq 1 - \\frac{T_f}{T_c}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1232-2833",
"position": 1,
"duration": 30,
"question": {
"id": "2833",
"question": "Effectuer le bilan d'\u00e9nergie et d'entropie pour un r\u00e9firg\u00e9rateur.\nEn d\u00e9duire le sens effectif des transferts d'\u00e9nergie. \nEn d\u00e9duire l'efficacit\u00e9 de cette machine dans le cas r\u00e9versible en fonction des temp\u00e9ratures des deux thermostats. Faire l'application num\u00e9rique pour $T_f$ =4\u00b0C et $T_c$ = 25\u00b0C.",
"answer": "Appelons $W$ le travail fourni par l'ext\u00e9rieur au fluide sur un cycle, $Q_c$ la chaleur fournie par la source chaude \u00e0 la temp\u00e9rature $T_c$ et $Q_f$ celle fournie par la source froide \u00e0 $T_f$. \nBilan d'\u00e9nergie sur un cycle de fluide : $\\Delta U = W + Q_f + Q_c = 0$ car $U$ est une fonction d'\u00e9tat.\nBilan d'entropie sur un cycle de fluide : $\\Delta S = S_{ech} + S_{cr} = \\frac{Q_f}{T_f} + \\frac{Q_c}{T_c} + S_{cr} = 0$ car $S$ est une fonction d'\u00e9tat.\n\nOn a donc $\\frac{Q_f}{T_f} + \\frac{Q_c}{T_c} = -  S_{cr} \\leq 0$. \nDe plus, pour un r\u00e9frig\u00e9rateur, $Q_f > 0$ car le fluide absorbe effectivement de l'\u00e9nergie de la source froide qui est l'int\u00e9rieur du r\u00e9frig\u00e9rateur.\n\nOn en d\u00e9duit donc, puisque $T_c > T_f$ que $Q_c < 0$, et qu'en valeur absolue, $-Q_c \\geq Q_f$.\nFinalement, il faut aussi fournir du travail au r\u00e9frig\u00e9rateur, $W >0$.\n\nAinsi, l'efficacit\u00e9 d'un r\u00e9frig\u00e9rateur est $e = \\frac{Q_f}{W} = \\frac{Q_f}{-Q_f - Q_c}$. Dans le cas r\u00e9versible, il n'y a pas d'entropie cr\u00e9\u00e9e, donc $\\frac{Q_f}{T_f} + \\frac{Q_c}{T_c} = 0$, d'o\u00f9 $\\frac{Q_c}{Q_f} = \\frac{-T_c}{T_f}$.\nOn en d\u00e9duit l'efficacit\u00e9 de la machine $e= \\frac{1}{-1+T_c\/T_f} = \\frac{T_f}{T_c - T_f}\\simeq 13.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1232-2834",
"position": 2,
"duration": 30,
"question": {
"id": "2834",
"question": "Quelle est la diff\u00e9rence entre rendement et efficacit\u00e9 \u00e9nerg\u00e9tique ?",
"answer": "Les deux mesurent le rapport entre \u00e9nergie utile et \u00e9nergie payante, toutefois, alors qu'un rendement est tout le temps inf\u00e9rieur \u00e0 1, une efficacit\u00e9 \u00e9nerg\u00e9tique peut-\u00eatre plus grande.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "109",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1233": {
"id": "1233",
"name": "Quizz 33 : Pr\u00e9cipitation, solubilit\u00e9",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1233\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "117",
"value": "Chimie",
"field_id": "23",
"created_at": "2017-08-21 12:28:53",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 150,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-05-15",
"questions": [{
"id": "1233-2835",
"position": 0,
"duration": 30,
"question": {
"id": "2835",
"question": "Comment est d\u00e9finie la solubilit\u00e9 d'un compos\u00e9 ? Quelle est son unit\u00e9 ?",
"answer": "C'est la quantit\u00e9 maximale de compos\u00e9 que l'on peut dissoudre par unit\u00e9 de volume de solvant. Elle s'exprime donc en mol\/L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1233-2836",
"position": 1,
"duration": 30,
"question": {
"id": "2836",
"question": "Comment sont d\u00e9finis le $K_s$ et le $pK_s$ d'un solut\u00e9 ?",
"answer": "$K_s$ est la constante d'\u00e9quilibre de la r\u00e9action de dissolution, par exemple $NaCl_{(s)} = Na^+_{(aq)} + Cl^-_{(aq)}$.\n$pK_s = - \\log_{10} K_s$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1233-2837",
"position": 2,
"duration": 30,
"question": {
"id": "2837",
"question": "Calculer la solubilit\u00e9 de $PbI_2$ de $pK_s=8,1$.",
"answer": "La r\u00e9action de dissolution est $PbI_2 = Pb^{2+} + 2I^-$, donc pour une solution satur\u00e9e, on a $[Pb^{2+}] = s$ et $[I^-] = 2 s$.\nA l'\u00e9quilibre, le quotient de r\u00e9action est \u00e9gal \u00e0 la constante d'\u00e9quilibre donc :\n$\\frac{[Pb^{2+}][I^-]^2}{(c^0)^3} = K_s$\n$\\frac{4s^3}{(c^0)^3} = K_s$\ndonc $s = c_0 \\left(\\frac{K_s}{4}\\right)^{1\/3} \\simeq 1,3$ mmol\/L. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1233-2838",
"position": 3,
"duration": 30,
"question": {
"id": "2838",
"question": "Montrer que lorsqu'on verse une goutte ( $V_g\u22435. 10^{\u22122}$ mL) de\nnitrate d'argent ( $c_1=10^{\u22121}$ mol\/L) dans $V_0=50$ mL d'acide\nchlorhydrique ($c_0=10^{\u22121}$ mol\/L), il y a pr\u00e9cipitation de nitrate d'argent $AgCl_{(s)}$, $pK_s=9,8$.",
"answer": "Calculons le quotient de r\u00e9action de la r\u00e9action $AgCl = Ag^+ + Cl^-$ juste apr\u00e8s l'introduction de la goutte. On a \n$Q_r = \\frac{[Ag^+][Cl^-]}{(c^0)^2}$ avec\n$[Cl^-] = c_0$\n$[Ag^+] = c_1 \\frac{V_g}{V_0}$\nOn a donc $Q_r = \\frac{c_0 c_1 V_0}{(c^0)^2 V_g} \\simeq 10^{-5} \\geq K_s= 10^{-9,8}$, donc puisque $Q_r > K_s$ la r\u00e9action va se produire dans le sens indirect : il va y avoir formation du pr\u00e9cipit\u00e9.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1233-5424",
"position": 4,
"duration": 30,
"question": {
"id": "5424",
"question": "Citer 3 param\u00e8tres qui influent sur la solubilit\u00e9 d'un compos\u00e9 chimique. Quel sont leurs effets ?",
"answer": "On peut citer la temp\u00e9rature, le pH ou l'effet d'ion commun.\nOn ne peut pas pr\u00e9voir l'effet d ela temp\u00e9rature sur la solubilit\u00e9 a priori (elle augment pour du sel $NaCl$, mais diminue pour du \"tartre\" $CaCO_3$).\nL'effet d'ion commun diminue la solubilit\u00e9 d'un compos\u00e9 lorsqu'un des ions form\u00e9s par la dissolution est d\u00e9j\u00e0 pr\u00e9sent en solution.\nUn bas pH (solution acide) augmente la solubilit\u00e9 des compos\u00e9s formant des ions hydroxyde $HO^-$ qui sont alors d\u00e9truits lors de la r\u00e9action $HO^- + H_3O^+ -> 2 H_2O$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "117",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"769": {
"id": "769",
"name": "Quizz 04 : Lentilles minces, aspect corpusculaire de la lumi\u00e8re",
"user_id": "550",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/769\/entrainement",
"fields": [{
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "118",
"value": "Optique",
"field_id": "23",
"created_at": "2017-08-21 12:30:19",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 420,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-26",
"questions": [{
"id": "769-2593",
"position": 0,
"duration": 30,
"question": {
"id": "2593",
"question": "Quelle est la d\u00e9finition d'un syst\u00e8me optique stigmatique ? Aplan\u00e9tique ?",
"answer": "L'image d'un point par un syst\u00e8me optique stigmatique est un point.\nL'image d'un objet perpendiculaire \u00e0 l'axe optique par un syst\u00e8me aplan\u00e9tique est perpendiculaire \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "769-2594",
"position": 1,
"duration": 30,
"question": {
"id": "2594",
"question": "Enoncer les conditions de Gauss.\nQuel est leur int\u00e9r\u00eat pour les lentilles minces ?",
"answer": "Pour \u00eatre dans les conditions de Gauss, on ne consid\u00e8re que des rayons lumineux proches de l'axe optique et faiblement inclin\u00e9s par rapport \u00e0 l'axe optique.\n\nDans les conditions de Gauss, une lentille mince est stigmatique et aplan\u00e9tique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2595",
"position": 2,
"duration": 30,
"question": {
"id": "2595",
"question": "Donner la d\u00e9finition du foyer objet et du foyer image d'une lentille mince.",
"answer": "Le foyer objet est le point par lequel passent tous les rayons incidents qui sortent parall\u00e8les \u00e0 l'axe optique.\nLe foyer image est le point par lequel passent tous les rayons (apr\u00e8s travers\u00e9e de la lentille) qui arrivaient parall\u00e8les \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2596",
"position": 3,
"duration": 30,
"question": {
"id": "2596",
"question": "O\u00f9 est situ\u00e9 l'image \u00e0 travers une lentille mince d'un objet ponctuel situ\u00e9 \u00e0 l'infini ?",
"answer": "Elle est situ\u00e9e dans le plan focal image.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2597",
"position": 4,
"duration": 30,
"question": {
"id": "2597",
"question": "O\u00f9 est situ\u00e9e l'image d'un objet ponctuel situ\u00e9 dans le plan focal objet ?",
"answer": "Elle est situ\u00e9e \u00e0 l'infini.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2598",
"position": 5,
"duration": 30,
"question": {
"id": "2598",
"question": "On appelle $A'$ l'image du point $A$ par une lentille mince de centre $O$. Comment s'appelle $\\gamma = \\frac{\\overline{OA'}}{\\overline{OA}}$ ?\nQue peut-on dire si $\\gamma <0 $ ?\net si $\\vert \\gamma \\vert > 1$ ?",
"answer": "$\\gamma$ s'appelle le grandissement.\nSi $\\gamma < 0$, l'image est renvers\u00e9e par rapport \u00e0 l'objet.\nSi $\\vert \\gamma \\vert > 1$, l'image est plus grande que l'objet.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2599",
"position": 6,
"duration": 30,
"question": {
"id": "2599",
"question": "Comment peut-on mod\u00e9liser un \u0153il humain  ?\nA quelle distance doit \u00eatre situ\u00e9 un objet pour qu'un \u0153il humain normal le voie sans effort ? Et quelle est la distance minimale pour que l'objet soit vu en accommodant ?",
"answer": "Un \u0153il peut \u00eatre mod\u00e9lis\u00e9 par une lentille mince (le cristallin) et un \u00e9cran (la r\u00e9tine) situ\u00e9 \u00e0 une distance variable de la lentille.\n\nUn \u0153il humain normal voit \u00e0 l'infini sans effort, et peut voir un objet jusuq'\u00e0 une distance minimale de 25 cm environ.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2603",
"position": 7,
"duration": 30,
"question": {
"id": "2603",
"question": "Quelle est l'\u00e9nergie d'un photon de fr\u00e9quence $\\nu$ ?",
"answer": "$E = h \\nu$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2604",
"position": 8,
"duration": 30,
"question": {
"id": "2604",
"question": "Quelle est la longueur d'onde dans le vide d'un photon d'\u00e9nergie $E$ ?",
"answer": "$\\lambda = \\frac{h c}{E}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "769-2605",
"position": 9,
"duration": 30,
"question": {
"id": "2605",
"question": "Les diff\u00e9rents \u00e9tats de l'atome d'hydrog\u00e8ne ont pour \u00e9nergie $E_n = \\frac{-13,6 \\textrm{ eV}}{n^2}$. Quel est la longueur d'onde d'un photon \u00e9mis lors de la d\u00e9sexcitation de l'atome d'hydrog\u00e8ne de son \u00e9tat $n=5$ vers son \u00e9tat $n=2$ ?\n1 eV = 1,6 .10$^{-19}$ J",
"answer": "On aura $\\lambda = \\frac{h c}{E_5 - E_2} = 4,3 . 10^{-7}$ m, soit environ 430 nm : il s'agit d'une radiation dans le domaine du visible.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "769-2606",
"position": 10,
"duration": 30,
"question": {
"id": "2606",
"question": "Combien de photons sont \u00e9mis en une heure par un laser h\u00e9lium-n\u00e9on de puissance 1 mW \u00e9mettant \u00e0 la longueur d'onde 633 nm ?",
"answer": "Le nombre de photons est d\u00e9termin\u00e9 en divisant l'\u00e9nergie totale \u00e9mise par le laser en une heure $E_{tot}$ par l'\u00e9nergie d'un seul photon $E_{ph}$.\n\nOn a $E_{tot} = P \\Delta t = 3,6$ J.\n$E_{ph} = \\frac{hc}{\\lambda} = 3,0 . 10^{-19}$ J\n\nLe nombre de photons \u00e9mis par ce laser en une heure est donc $N = \\frac{E_{tot}}{E_{ph}} \\simeq 1,2.10^{19}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "769-2986",
"position": 11,
"duration": 30,
"question": {
"id": "2986",
"question": "Que peut-on dire du rayon \u00e9mergent d'une lentille mince correspondant \u00e0 un rayon incident passant par son centre optique ?",
"answer": "Il n'est pas d\u00e9vi\u00e9 en traversant la lentille.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2987",
"position": 12,
"duration": 30,
"question": {
"id": "2987",
"question": "Que peut-on dire du rayon incident d'une lentille mince correspondant \u00e0 un rayon \u00e9mergent passant par son foyer image ?",
"answer": "Il arrive parall\u00e8le \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "769-2988",
"position": 13,
"duration": 30,
"question": {
"id": "2988",
"question": "Que peut-on dire du rayon \u00e9mergent d'une lentille mince correspondant \u00e0 un rayon incident passant par son foyer objet ?",
"answer": "Il ressort parall\u00e8le \u00e0 l'axe optique.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "118",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "90",
"name": "TSI1",
"schoolyear": "2018-2019"
}, {
"id": "96",
"name": "TSI1",
"schoolyear": "2019-2020"
}, {
"id": "117",
"name": "TSI1",
"schoolyear": "2020-2021"
}, {
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1265": {
"id": "1265",
"name": "G\u00e9om\u00e9trie plane",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1265\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 480,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2024-11-19",
"questions": [{
"id": "1265-3013",
"position": 0,
"duration": 30,
"question": {
"id": "3013",
"question": "D\u00e9finition d'une base du plan.\nD\u00e9finition des coordonn\u00e9es d'un vecteur $\\vec{u}$ dans une base.",
"answer": "Une base est un couple de vecteurs $(\\vec{\\imath},\\vec{\\jmath})$ non colin\u00e9aires.\nDans la base $(\\vec{\\imath},\\vec{\\jmath})$, $\\vec{u}\\binom{x}{y}\\iff \\vec{u}=x\\vec{\\imath}+y\\vec{\\jmath}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3014",
"position": 1,
"duration": 30,
"question": {
"id": "3014",
"question": "D\u00e9finition d'un rep\u00e8re du plan.\nD\u00e9finition des coordonn\u00e9es d'un point $M$ dans un rep\u00e8re.",
"answer": "Un rep\u00e8re est un triplet $(O;\\vec{\\imath};\\vec{\\jmath})$ o\u00f9 $O$ est un point du plan (l'origine) et $(\\vec{\\imath};\\vec{\\jmath})$ une base du plan.\nDans le rep\u00e8re $(O;\\vec{\\imath};\\vec{\\jmath})$, $M(x;y)\\iff \\overrightarrow{OM}=x\\vec{\\imath}+y\\vec{\\jmath}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3017",
"position": 2,
"duration": 30,
"question": {
"id": "3017",
"question": "Quelle est la diff\u00e9rence entre base et rep\u00e8re du plan ?",
"answer": "Une base est compos\u00e9e de deux vecteurs, elle sert \u00e0 rep\u00e9rer des vecteurs.\nUn rep\u00e8re est compos\u00e9 d'une base et un point. Il sert \u00e0 rep\u00e9rer des points (mais on peut utiliser sa base associ\u00e9e pour rep\u00e9rer aussi des vecteurs).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3018",
"position": 3,
"duration": 30,
"question": {
"id": "3018",
"question": "D\u00e9finition d'une base orthogonale, orthonorm\u00e9e, orthonorm\u00e9e directe.",
"answer": "orthogonale : les vecteurs de base sont orthogonaux.\northonorm\u00e9e : les vecteurs de base sont orthogonaux et de norme 1.\northonorm\u00e9e directe : c'est une base orthonorm\u00e9e o\u00f9 le deuxi\u00e8me vecteur est l'image du premier par la rotation vectorielle d'angle $\\frac{\\pi}{2}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3019",
"position": 4,
"duration": 30,
"question": {
"id": "3019",
"question": "D\u00e9finition du produit scalaire.",
"answer": "$\\vec{u}.\\vec{v}=\\|\\vec{u}\\|\\cdot\\|\\vec{v}\\|\\cdot\\cos(\\vec{u},\\vec{v})$, ou $0$ si l'un des vecteurs $\\vec{u}$, $\\vec{v}$ est nul.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3020",
"position": 5,
"duration": 30,
"question": {
"id": "3020",
"question": "D\u00e9finition du d\u00e9terminant.",
"answer": "$\\det (\\vec{u},\\vec{v}) =\\|\\vec{u}\\|\\cdot\\|\\vec{v}\\|\\cdot\\sin(\\vec{u},\\vec{v})$, ou $0$ si l'un des vecteurs $\\vec{u}$, $\\vec{v}$ est nul.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3021",
"position": 6,
"duration": 30,
"question": {
"id": "3021",
"question": "Que dire des vecteurs $\\vec{u}$ et $\\vec{v}$ dans ce cas :\n$\\vec{u}.\\vec{v}=0\\iff\\ldots$",
"answer": "$\\vec{u}$ et $\\vec{v}$ sont orthogonaux.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3022",
"position": 7,
"duration": 30,
"question": {
"id": "3022",
"question": "Que dire des vecteurs $\\vec{u}$ et $\\vec{v}$ dans ce cas :\n$\\det(\\vec{u},\\vec{v})=0\\iff\\ldots$",
"answer": "$\\vec{u}$ et $\\vec{v}$ sont colin\u00e9aires.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3024",
"position": 8,
"duration": 30,
"question": {
"id": "3024",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique du d\u00e9terminant ?",
"answer": "C'est (au signe pr\u00e8s) l'aire du parall\u00e9logramme form\u00e9 par les deux vecteurs.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3025",
"position": 9,
"duration": 30,
"question": {
"id": "3025",
"question": "Donner une formule permettant de calculer le produit scalaire de deux vecteurs \u00e0 partir de leurs coordonn\u00e9es. Sous quelles conditions cette formule est-elle valable ?",
"answer": "$\\left(\\begin{array}{c}x_1\\\\y_1\\end{array}\\right).\\left(\\begin{array}{c}x_2\\\\y_2\\end{array}\\right)=x_1x_2+y_1y_2$,\n\u00e0 condition que la base soit orthonorm\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3026",
"position": 10,
"duration": 30,
"question": {
"id": "3026",
"question": "Donner une formule permettant de calculer le d\u00e9terminant de deux vecteurs \u00e0 partir de leurs coordonn\u00e9es. Sous quelles conditions cette formule est-elle valable ?",
"answer": "$\\left|\\begin{array}{cc}x_1 & x_2\\\\y_1 & y_2\\end{array}\\right|= x_1 y_2-y_1x_2$,  \n\nC'est vrai \u00e0 condition que la base soit orthonorm\u00e9e directe.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-3023",
"position": 11,
"duration": 30,
"question": {
"id": "3023",
"question": "Relation entre $\\vec{u}.\\vec{v}$ et $\\vec{v}.\\vec{u}$ ?\nRelation entre $\\det(\\vec{u},\\vec{v})$ et $\\det(\\vec{v},\\vec{u})$ ?",
"answer": "$\\vec{u}.\\vec{v}=\\vec{v}.\\vec{u}$ (le produit scalaire est sym\u00e9trique)\n$\\det(\\vec{u},\\vec{v})=-\\det(\\vec{v},\\vec{u})$ (le d\u00e9terminant est antisym\u00e9trique)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-5253",
"position": 12,
"duration": 30,
"question": {
"id": "5253",
"question": "Soit $d$ la droite d'\u00e9quation $ax+by+c=0$. Donner les coordonn\u00e9es d'un vecteur directeur de $d$.",
"answer": "$\\vec{u} \\binom{-b}{a}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-5254",
"position": 13,
"duration": 30,
"question": {
"id": "5254",
"question": "Soit $d$ la droite d'\u00e9quation $ax+by+c=0$. Donner les coordonn\u00e9es d'un vecteur normal \u00e0 d.",
"answer": "$\\vec{n} \\binom{a}{b}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-5252",
"position": 14,
"duration": 30,
"question": {
"id": "5252",
"question": "Quelle est la forme g\u00e9n\u00e9rale d'une \u00e9quation cart\u00e9sienne de droite ?",
"answer": "$ax+by+c=0$ o\u00f9 a,b,c sont 3 r\u00e9els, a et b non nuls en m\u00eame temps.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1265-5366",
"position": 15,
"duration": 30,
"question": {
"id": "5366",
"question": "Indiquer deux fa\u00e7ons de calculer le produit scalaire de deux vecteurs $\\vec{u} \\binom{x}{y}$ et $\\vec{v}\\binom{x'}{y'}$ dont on connait les coordonn\u00e9es dans un rep\u00e8re orthonorm\u00e9.",
"answer": "$xx'+yy'$\n ou \n$\\vec{u}.\\vec{v}=\\|\\vec{u}\\|\\cdot\\|\\vec{v}\\|\\cdot\\cos(\\vec{u},\\vec{v})$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1321": {
"id": "1321",
"name": "Limites et continuit\u00e9",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1321\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "498",
"value": "Analyse",
"field_id": "19",
"created_at": "2020-02-07 08:54:39",
"updated_at": "2020-02-07 08:54:39",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 420,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-03-18",
"questions": [{
"id": "1321-3156",
"position": 0,
"duration": 30,
"question": {
"id": "3156",
"question": "D\u00e9finition de la continuit\u00e9 en un point.",
"answer": "Une fonction $f$ est continue en $a\\in D_f$ si elle admet $f(a)$ comme limite en $a$; ou, de fa\u00e7on \u00e9quivalente, si elle admet une limite finie \u00e0 gauche et \u00e0 droite en $a$ et que ces limites sont \u00e9gales \u00e0 $f(a)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3157",
"position": 1,
"duration": 30,
"question": {
"id": "3157",
"question": "D\u00e9finition de la continuit\u00e9 sur un intervalle.",
"answer": "$f$ est continue sur $I$ si elle est continue en a pour tout $a\\in I$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3158",
"position": 2,
"duration": 30,
"question": {
"id": "3158",
"question": "Citer le th\u00e9or\u00e8me des valeurs interm\u00e9diaires .",
"answer": "Soit $f$ une fonction continue sur un intervalle $[a;b]$. Alors, pour tout $y\\in [f(a);f(b)]$ (ou $[f(b);f(a)]$), il existe $x\\in[a;b]$ tel que $f(x)=y$.\nAutre formulation : l'image d'un intervalle par une fonction continue est un intervalle.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3160",
"position": 3,
"duration": 30,
"question": {
"id": "3160",
"question": "Qu'est-ce qu'une fonction prolongeable par continuit\u00e9 ?",
"answer": "Une fonction $f$ d\u00e9finie au voisinage de $a$ mais pas en $a$ est prolongeable par continuit\u00e9 en $a$ si elle admet une limite \u00e0 gauche et une limite \u00e0 droite en $a$, toutes deux finies et \u00e9gales entre elles.\nDans ce cas, on peut d\u00e9finir une fonction $\\tilde{f}$ au voisinage de $a$, par $\\tilde{f}(x)=f(x)$ si $x\\neq a$ et $\\tilde{f}(a)=\\ell$, $\\ell$ \u00e9tant la valeur commune aux deux limites. La fonction $\\tilde{f}$ est alors continue en $a$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3162",
"position": 4,
"duration": 30,
"question": {
"id": "3162",
"question": "Comment montrer qu'une fonction $f$ n'a pas de limite en un point $a\\in\\mathbf{R}\\cup\\{\\pm\\infty\\}$ ?",
"answer": "Construire deux suites $(u_n)_{n\\in\\mathbf{N}}$ et $(v_n)_{n\\in\\mathbf{N}}$ qui convergent vers $a$, mais telles que les suites $(f(u_n))_{n\\in\\mathbf{N}}$ et $(f(v_n))_{n\\in\\mathbf{N}}$ convergent vers des limites diff\u00e9rentes (ou n'admettent pas de limite).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5413",
"position": 5,
"duration": 30,
"question": {
"id": "5413",
"question": "Peut-on prolonger par continuit\u00e9 en 0 la fonction $f$ d\u00e9finie sur $\\mathbb{R}^\\star$ par $f(x)=\\dfrac{e^x-1}{x}$ ?",
"answer": "Oui en posant f(0)=1 qui correspond \u00e0 $\\lim\\limits_{x\\to 0} \\dfrac{e^x-1}{x}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5690",
"position": 6,
"duration": 30,
"question": {
"id": "5690",
"question": "Citer le th\u00e9or\u00e8me d'encadrement (cas o\u00f9 les limites sont finies).",
"answer": "On consid\u00e8re trois fonctions $f,g,h\\colon I\\to\\mathbb{R}$ d\u00e9finies au voisinage de $a\\in\\mathbb{R}\\cup\\{\\pm\\infty\\}$.\nsi $f(x)\\leq g(x)\\leq h(x)$ pour tout $x\\in I$ et $\\displaystyle\\lim_{x\\to a}f(x)=\\lim_{x\\to a}h(x)=\\ell\\in\\mathbb{R}$, alors $\\displaystyle\\lim_{x\\to a}g(x)=\\ell$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5691",
"position": 7,
"duration": 30,
"question": {
"id": "5691",
"question": "Soit $f$ une fonction d\u00e9finie au voisinage de $+\\infty$, d\u00e9croissante et non minor\u00e9e. Alors...",
"answer": "$ \\displaystyle{\\lim_{x \\to +\\infty} f(x)=-\\infty}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5409",
"position": 8,
"duration": 30,
"question": {
"id": "5409",
"question": "Quelle est la bonne relation : $x \\underset{0}{=} o (x^2)$ ou $x^2 \\underset{0}{=} o (x)$ ?",
"answer": "$x^2 \\underset{0}{=} o (x)$ car $\\dfrac{x^2}{x}=x$ tend vers 0 en 0.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5408",
"position": 9,
"duration": 30,
"question": {
"id": "5408",
"question": "Que vaut $\\displaystyle{ \\lim_{x \\to 0\\\\x<0} \\dfrac{x-1}{x}}$ ?",
"answer": "$+ \\infty$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5689",
"position": 10,
"duration": 30,
"question": {
"id": "5689",
"question": "Donner un \u00e9quivalent simple de $f(x)=\\dfrac{3x-2}{x^2+1}$ au voisinage de $-\\infty$",
"answer": "$f(x)\\sim \\dfrac{3}{x}$ lorsque $x \\to -\\infty$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-5410",
"position": 11,
"duration": 30,
"question": {
"id": "5410",
"question": "Donner un \u00e9quivalent simple de $e^x-1$ en 0.",
"answer": "$x$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3159",
"position": 12,
"duration": 30,
"question": {
"id": "3159",
"question": "Citer le th\u00e9or\u00e8me des bornes (de Weierstrass).",
"answer": "Une fonction continue sur un segment (c-\u00e0-d un intervalle ferm\u00e9 et born\u00e9) est born\u00e9e et atteint ses bornes, autrement dit poss\u00e8de un maximum et un minimum.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1321-3161",
"position": 13,
"duration": 30,
"question": {
"id": "3161",
"question": "Comment montrer qu'une fonction est continue ?",
"answer": "On utilise le th\u00e9or\u00e8me de composition sur tous les intervalles o\u00f9 la fonction est d\u00e9finie par une formule ne faisant intervenir que des fonctions continues (\u00ab $f$ est continue sur $I$ par somme, produit, compos\u00e9e...de fonctions qui le sont \u00bb).\nPour tous les points du domaine de d\u00e9finition restants, on \u00e9tudie la limite \u00e0 droite et la limite \u00e0 gauche : on v\u00e9rifie que ces limites existent, sont \u00e9gales entre elles, et sont \u00e9gales \u00e0 la valeur de la fonction au point.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1326": {
"id": "1326",
"name": "Polyn\u00f4mes",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1326\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "53",
"value": "Alg\u00e8bre",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-03-25",
"questions": [{
"id": "1326-5697",
"position": 0,
"duration": 30,
"question": {
"id": "5697",
"question": "P et Q sont deux polyn\u00f4mes. Quel lien y a-t-il entre le degr\u00e9 de $P\\times Q$, celui de $P$ et celui de $Q$ ?",
"answer": "$\\deg(PQ)=\\deg(P)+\\deg(Q)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5698",
"position": 1,
"duration": 30,
"question": {
"id": "5698",
"question": "Vrai ou faux : Si $\\deg(P)=\\deg(Q)=n$, alors $\\deg(P+Q)=n$ ?",
"answer": "C'est faux, par exemple $X^3+X$ et $-X^3$ sont de degr\u00e9 3, mais leur somme est de degr\u00e9 1 (elle vaut $X$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5699",
"position": 2,
"duration": 30,
"question": {
"id": "5699",
"question": "Soit $P(X)$ un polyn\u00f4me de degr\u00e9 $n$. Quel est le degr\u00e9 de $X.P(X^2)$ ?",
"answer": "$2n+1$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5700",
"position": 3,
"duration": 30,
"question": {
"id": "5700",
"question": "Soit $P$ un polyn\u00f4me. Que signifie que $a$ est racine de $P$ de multiplicit\u00e9 $k$ (en parlant de factorisation) ?",
"answer": "Cela signifie que $P$ est divisible (ou factorisable) par $(X-a)^k$ , mais pas par  $(X-a)^{k+1}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5701",
"position": 4,
"duration": 30,
"question": {
"id": "5701",
"question": "Soit $P$ un polyn\u00f4me. Que signifie que $a$ est racine de $P$ de multiplicit\u00e9 $k$ (en parlant de d\u00e9riv\u00e9es) ?",
"answer": "Cela signifie que $P(a)=P'(a)=...=P^{(k-1)}(a)=0$ et $P^{(k)}(a) \\neq 0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5702",
"position": 5,
"duration": 30,
"question": {
"id": "5702",
"question": "Citer le th\u00e9or\u00e8me fondamental de l'alg\u00e8bre.",
"answer": "Tout polyn\u00f4me non constant \u00e0 coefficient complexe poss\u00e8de au moins une racine complexe.\n\n(remarque : il en poss\u00e8de donc exactement autant que son degr\u00e9)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5704",
"position": 6,
"duration": 30,
"question": {
"id": "5704",
"question": "Quels sont les polyn\u00f4mes irr\u00e9ductibles de $\\mathbb{C}[X]$ ?",
"answer": "Tous les polyn\u00f4mes de degr\u00e9 1.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5703",
"position": 7,
"duration": 30,
"question": {
"id": "5703",
"question": "Quels sont les polyn\u00f4mes irr\u00e9ductibles de $\\mathbb{R}[X]$ ?",
"answer": "Ce sont les polyn\u00f4mes de degr\u00e9 1, ainsi que ceux de degr\u00e9 2 dont le discriminant est strictement n\u00e9gatif.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5705",
"position": 8,
"duration": 30,
"question": {
"id": "5705",
"question": "Factoriser $P(X)=X^3-1$ en produit de facteurs irr\u00e9ductibles de $\\mathbb{R}[X]$.",
"answer": "$P(X)=(X-1)(X^2+X+1)$.\n\nOn remarque que 1 est racine \u00e9vidente et on factorise par $X-1$.\n$X^2+X+1$ est irr\u00e9ductible dans $\\mathbb{R}[X]$ car sans racine r\u00e9elle.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5706",
"position": 9,
"duration": 30,
"question": {
"id": "5706",
"question": "Quelles sont les racines complexes de $X^n-1$ ?",
"answer": "L'ensemble des racines n-i\u00e8mes de l'unit\u00e9, c'est-\u00e0-dire les $e^{i \\frac{2k\\pi}{n}}$ o\u00f9 $k$ est un entier.\n\n (il suffit de se limiter aux entiers entre 0 et $n-1$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5922",
"position": 10,
"duration": 30,
"question": {
"id": "5922",
"question": "Citer la formule de Taylor en 0 pour un polyn\u00f4me de degr\u00e9 $n$.",
"answer": "$P(X)=P(0)+XP'(0)+X^2\\dfrac{P''(0)}{2!}+...+X^n\\dfrac{P^{(n)}(0)}{n!}=\\displaystyle{\\sum_{k=0}^n\\dfrac{P^{(k)}(0)}{k!}X^k}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5923",
"position": 11,
"duration": 30,
"question": {
"id": "5923",
"question": "Citer la formule de Leibniz pour les polyn\u00f4mes.",
"answer": "$(PQ)^{(n)}=\\displaystyle{\\sum_{k=0}^n\\binom{n}{k}P^{(k)}Q^{(n-k)}}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1326-5924",
"position": 12,
"duration": 30,
"question": {
"id": "5924",
"question": "Quelles sont les racines complexes de $X^n+1$ ?",
"answer": "L'ensemble des racines n-i\u00e8mes de $-1$, c'est-\u00e0-dire les $e^{i \\left(\\frac{\\pi}{n}+\\frac{2k\\pi}{n}\\right)}$ o\u00f9 $k$ est un entier.\n\n (il suffit de se limiter aux entiers entre 0 et $n-1$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "130",
"name": "TSI1",
"schoolyear": "2021-2022"
}, {
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1355": {
"id": "1355",
"name": "DC1 Quizz 2 ",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1355\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "18",
"value": "Cin\u00e9matique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "24",
"value": "Mod\u00e9lisation des liaisons",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 5,
"duration": 780,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-15",
"questions": [{
"id": "1355-681",
"position": 0,
"duration": 30,
"question": {
"id": "681",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Sph\u00e8re Cylindre d'axe (O, $\\vec{x})$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/97b65020-93e3-11e7-b035-171168d9d4e8",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-692",
"position": 1,
"duration": 30,
"question": {
"id": "692",
"question": "Quels sont les degr\u00e9s de libert\u00e9 d'une liaison Appui Plan de normale $ \\vec{y}$ ",
"answer": "Une liaison Appui Plan de normale $ \\vec{y}$  poss\u00e8de 3 degr\u00e9s de libert\u00e9 : 1 rotation $(R_y)$ et deux translations ( $T_x $et $T_z$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-671",
"position": 2,
"duration": 30,
"question": {
"id": "671",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Sph\u00e8re-Plan (ponctuelle) de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f36eed70-93c4-11e7-ab05-9752d16c3428",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-679",
"position": 3,
"duration": 30,
"question": {
"id": "679",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Sph\u00e8re Sph\u00e8re (rotule) de centre A.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/779647d0-93e3-11e7-bfd3-e36de8c088b7",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-836",
"position": 4,
"duration": 30,
"question": {
"id": "836",
"question": "Quelle liaison poss\u00e8de comme degr\u00e9s de libert\u00e9 : 1 rotation $(R_x)$ et deux translations ( $T_y $ et $T_z$)",
"answer": "Une liaison Appui Plan de normale $ \\vec{x}$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1355-691",
"position": 5,
"duration": 30,
"question": {
"id": "691",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Appui Plan de normale $\\vec{x}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0e3d8690-93e8-11e7-9bdc-9b11dc1a48f8",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1355-660",
"position": 6,
"duration": 30,
"question": {
"id": "660",
"question": "Combien de classes d'\u00e9quivalence ?",
"answer": "4 classes d'\u00e9quivalence",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/99012100-93b1-11e7-8d83-a31dbefabf65",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a4811e20-93b1-11e7-9eaa-db9210ecbad0",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1355-682",
"position": 7,
"duration": 30,
"question": {
"id": "682",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot d'axe $ (A, \\vec{x})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/83df62e0-93e5-11e7-b72c-698d635723d7",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1355-686",
"position": 8,
"duration": 30,
"question": {
"id": "686",
"question": "Quelles sont les 4 hypoth\u00e8ses des liaisons parfaites ?",
"answer": "Solides ind\u00e9formables \nG\u00e9om\u00e9trie parfaite\nLiaisons sans jeu \nLiaisons sans frottement \n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-674",
"position": 9,
"duration": 30,
"question": {
"id": "674",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": " liaison cylindre plan d'axe $(A, \\vec{x})$ et de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/92acae20-93e4-11e7-81c7-d78e9f1ae196",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-687",
"position": 10,
"duration": 30,
"question": {
"id": "687",
"question": "Quels sont les degr\u00e9s de libert\u00e9 d\u2019une liaison h\u00e9lico\u00efdale?",
"answer": "une liaison h\u00e9lico\u00efdale comporte un seul degr\u00e9 de libert\u00e9 : une rotation ou  une translation ( les deux mouvements \u00e9tant li\u00e9s).",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0b57fd80-99fc-11e7-85ff-bffa9cf1c14d",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-688",
"position": 11,
"duration": 30,
"question": {
"id": "688",
"question": "Quels sont les degr\u00e9s de libert\u00e9 d'une liaison Cylindre Plan (lin\u00e9aire rectiligne) d'axe $ (0, \\vec{x})$ et de normale $ \\vec{z}$ ",
"answer": "une liaison cylindre plan d'axe $ (0, \\vec{x})$ et de normale $ \\vec{z}$  comporte 2 rotations $(R_x , R_z)$ et deux translations $(T_x, T_y )$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 5
}
}, {
"id": "1355-689",
"position": 12,
"duration": 30,
"question": {
"id": "689",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Sph\u00e8re-Cylindre (lin\u00e9aire annulaire) d'axe $(C, \\vec{x})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e7bcd970-93e3-11e7-9671-9d1da3cba263",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-670",
"position": 13,
"duration": 30,
"question": {
"id": "670",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ?",
"answer": " liaison Sph\u00e8re Cylindre (lin\u00e9aire annulaire) d'axe $ (C, \\vec{x})$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/029e8fc0-93e5-11e7-bf36-5fec0afaa748",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-661",
"position": 14,
"duration": 30,
"question": {
"id": "661",
"question": "Combien de classes d'\u00e9quivalence ?",
"answer": "3 classes d'\u00e9quivalence",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d023e1f0-93b1-11e7-9c9c-1fb2cfcf10d7",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e239d600-93b1-11e7-a37c-25e2e8414f2a",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-683",
"position": 15,
"duration": 30,
"question": {
"id": "683",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot Glissant d'axe $ (0, \\vec{x})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8c9a7cc0-93e5-11e7-8240-63575ae7e05a",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1355-673",
"position": 16,
"duration": 30,
"question": {
"id": "673",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Pivot Glissant d'axe $(A, \\vec{x})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b3245800-93e6-11e7-aa4a-efc05e0ddce7",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-685",
"position": 17,
"duration": 30,
"question": {
"id": "685",
"question": "Quels sont les degr\u00e9s de libert\u00e9 d\u2019une liaison ponctuelle  de normale $\\vec{z}$?",
"answer": "Liaison ponctuelle :  2 translations $(T_x, T_y)$ et 3 rotations",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ec78cba0-995a-11e7-90f7-fbb30059700f",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-730",
"position": 18,
"duration": 30,
"question": {
"id": "730",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison h\u00e9lico\u00efdale d'axe $ (0, \\vec{y})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/48568330-0a9c-11e8-b7a9-a10b7103137f",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-731",
"position": 19,
"duration": 30,
"question": {
"id": "731",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": " liaison cylindre plan (lin\u00e9aire rectiligne) d'arete $(A, \\vec{y})$ et de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a04d2890-0a9c-11e8-86e5-f59a780b47a9",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-732",
"position": 20,
"duration": 30,
"question": {
"id": "732",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot Glissant d'axe $ (0, \\vec{y})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/abdfbea0-0a9c-11e8-88f9-67ed615f78b5",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-779",
"position": 21,
"duration": 30,
"question": {
"id": "779",
"question": "\nQuels sont les degr\u00e9s de libert\u00e9 d'une liaison Cylindre Plan (lin\u00e9aire rectiligne) d'axe $ (0, \\vec{y})$ et de normale $ \\vec{x}$ \n\n",
"answer": "une liaison cylindre plan d'axe $ (0, \\vec{y})$ et de normale $ \\vec{x}$  comporte 2 rotations $(R_x , R_y)$ et deux translations $(T_y, T_z )$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1355-729",
"position": 22,
"duration": 30,
"question": {
"id": "729",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Appui Plan de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/41191730-0a9c-11e8-929d-b91a333a5de6",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1355-750",
"position": 23,
"duration": 30,
"question": {
"id": "750",
"question": "D\u00e9terminer la liaison cin\u00e9matiquement \u00e9quivalente  et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Pivot d'axe $(B,\\overrightarrow{z})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/475338f0-9b8e-11e7-8f43-1fa7e44640e3",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1355-812",
"position": 24,
"duration": 30,
"question": {
"id": "812",
"question": "D\u00e9terminer la liaison cin\u00e9matiquement \u00e9quivalente  et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot d'axe $ (0, \\vec{y})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/eac925b0-a27a-11e7-b89a-ff0d567f0ee5",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 5
}
}, {
"id": "1355-811",
"position": 25,
"duration": 30,
"question": {
"id": "811",
"question": "D\u00e9terminer la liaison cin\u00e9matiquement \u00e9quivalente  et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot d'axe ($A, \\vec{x_2}$)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/67f6bd60-a27a-11e7-86a0-6739e29d88df",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 5
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1354": {
"id": "1354",
"name": "DC1 Quizz 1",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1354\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "24",
"value": "Mod\u00e9lisation des liaisons",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 660,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-05",
"questions": [{
"id": "1354-694",
"position": 0,
"duration": 30,
"question": {
"id": "694",
"question": "Quelle fonction de la cha\u00eene d'information est assur\u00e9e par ce composant ?",
"answer": "fonction ACQUERIR",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d60cde70-9654-11e7-8c12-93868838d388",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-695",
"position": 1,
"duration": 30,
"question": {
"id": "695",
"question": "Quelle fonction de la cha\u00eene d'information est assur\u00e9e par ce composant ?",
"answer": "fonction TRAITER",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/4a94f760-9655-11e7-ac19-ef81803991ee",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-641",
"position": 2,
"duration": 30,
"question": {
"id": "641",
"question": "Quelle fonction de la cha\u00eene d'\u00e9nergie est assur\u00e9e par ce composant ?",
"answer": "fonction \"ALIMENTER\"",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0881b530-8c0e-11e7-bf40-ef570d95a31f",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-632",
"position": 3,
"duration": 30,
"question": {
"id": "632",
"question": "Quelle fonction de la cha\u00eene d'\u00e9nergie est assur\u00e9e par ce composant ?",
"answer": "unit\u00e9 FRL   Filtrage\/R\u00e9gulation\/LubrificationFonction \"ALIMENTER\" ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a7cb71e0-8c09-11e7-be4b-fde6cfae7fec",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-698",
"position": 4,
"duration": 30,
"question": {
"id": "698",
"question": "Quelle fonction de la cha\u00eene d'information est assur\u00e9e par ce composant ?",
"answer": "fonction RESTITUER",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/30940c20-9655-11e7-beda-b92111dfa822",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-666",
"position": 5,
"duration": 30,
"question": {
"id": "666",
"question": "Quelle est la d\u00e9signation de ce distributeur ?",
"answer": "Distributeur 5\/2 avec s\u00e9lecteur ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/3a7a52f0-93bf-11e7-b405-a3fe9b7ac51d",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-639",
"position": 6,
"duration": 30,
"question": {
"id": "639",
"question": "Quelle fonction de la cha\u00eene d'\u00e9nergie est assur\u00e9e par ce composant ?",
"answer": "fonction \"MODULER\"",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/92574290-8c0d-11e7-a45b-875292f00725",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-2860",
"position": 7,
"duration": 30,
"question": {
"id": "2860",
"question": "Comment calculer la puissance m\u00e9canique en sortie d'un actionneur de type machine \u00e9lectrique ?",
"answer": "$P=C\u00b7\\Omega$\navec $C$ moment du couple en $Nm$ et $\\Omega$ vitesse angulaire en $rad{\/s}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-2861",
"position": 8,
"duration": 30,
"question": {
"id": "2861",
"question": "Comment calculer la puissance \u00e9lectrique en entr\u00e9e d'un actionneur de type machine \u00e9lectrique ?",
"answer": "$P=U.I$\n $U$ : la tension aux bornes ($V$)\n $I$ : l'intensit\u00e9 du courant ($A$ )\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-5896",
"position": 9,
"duration": 30,
"question": {
"id": "5896",
"question": "par quelles grandeurs est caract\u00e9ris\u00e9e la puissance pneumatique ou hydraulique ?",
"answer": "le D\u00e9bit $q_{(t)}$ en   $m^3\/s$ et la Pression $p_ r{(t)}$ en $Pa$,",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-5897",
"position": 10,
"duration": 30,
"question": {
"id": "5897",
"question": "par quelles grandeurs est caract\u00e9ris\u00e9e la puissance m\u00e9canique en rotation ?",
"answer": "La vitesse angulaire $\\omega_{(t)}$ en $rad\/s$ et le moment du couple $c_{(t)}$ en $Nm$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-5898",
"position": 11,
"duration": 30,
"question": {
"id": "5898",
"question": "par quelles grandeurs est caract\u00e9ris\u00e9e la puissance m\u00e9canique en translation ?",
"answer": "La vitesse $v_{(t)}$ en $m\/s$ et la force $f_{(t)}$ en $N$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-2857",
"position": 12,
"duration": 30,
"question": {
"id": "2857",
"question": "par quelles grandeurs est caract\u00e9ris\u00e9e l'\u00e9nergie \u00e9lectrique ?",
"answer": "La tension $v_{(t)}$ en $V$ et l'intensit\u00e9 du courant \u00e9lectrique $i_{(t)}$ en $A$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-2858",
"position": 13,
"duration": 30,
"question": {
"id": "2858",
"question": "Comment calculer la puissance m\u00e9canique en sortie d'un actionneur de type v\u00e9rin ?",
"answer": "$P=F\u00b7V$\navec $F$ action m\u00e9canique en $N$ et $V$ vitesse  en $m{\/s}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-2859",
"position": 14,
"duration": 30,
"question": {
"id": "2859",
"question": "Comment calculer la puissance hydraulique en entr\u00e9e d'un actionneur de type v\u00e9rin ?",
"answer": "$P=P_r.Q$\navec $Q$ le d\u00e9bit en $m^3\/s$ et $P_r$ la Pression  en $Pa$,",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-640",
"position": 15,
"duration": 30,
"question": {
"id": "640",
"question": "Quelle fonction de la cha\u00eene d'\u00e9nergie est assur\u00e9e par ce composant ?",
"answer": "fonction \"TRANSMETTRE\"",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a8fa3260-8c0d-11e7-b328-355edc64d442",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-663",
"position": 16,
"duration": 30,
"question": {
"id": "663",
"question": "Quelle est la d\u00e9signation de ce distributeur ?",
"answer": "Distributeur 3\/2 avec bouton-poussoir, ferm\u00e9 au repos",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/25532680-93bf-11e7-a6e0-3f8dccae6393",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-674",
"position": 17,
"duration": 30,
"question": {
"id": "674",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": " liaison cylindre plan d'axe $(A, \\vec{x})$ et de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/92acae20-93e4-11e7-81c7-d78e9f1ae196",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-687",
"position": 18,
"duration": 30,
"question": {
"id": "687",
"question": "Quels sont les degr\u00e9s de libert\u00e9 d\u2019une liaison h\u00e9lico\u00efdale?",
"answer": "une liaison h\u00e9lico\u00efdale comporte un seul degr\u00e9 de libert\u00e9 : une rotation ou  une translation ( les deux mouvements \u00e9tant li\u00e9s).",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0b57fd80-99fc-11e7-85ff-bffa9cf1c14d",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1354-679",
"position": 19,
"duration": 30,
"question": {
"id": "679",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "Liaison Sph\u00e8re Sph\u00e8re (rotule) de centre A.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/779647d0-93e3-11e7-bfd3-e36de8c088b7",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1354-683",
"position": 20,
"duration": 30,
"question": {
"id": "683",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": "liaison Pivot Glissant d'axe $ (0, \\vec{x})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8c9a7cc0-93e5-11e7-8240-63575ae7e05a",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1354-731",
"position": 21,
"duration": 30,
"question": {
"id": "731",
"question": "Caract\u00e9riser la liaison et citer ses param\u00e8tres g\u00e9om\u00e9triques ",
"answer": " liaison cylindre plan (lin\u00e9aire rectiligne) d'arete $(A, \\vec{y})$ et de normale $\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a04d2890-0a9c-11e8-86e5-f59a780b47a9",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1357": {
"id": "1357",
"name": "DC2 Quizz 1",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1357\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}, {
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}, {
"id": "60",
"value": "EE",
"created_at": "2017-10-03 14:15:25",
"updated_at": "2017-10-03 14:15:25",
"deleted_at": "null",
"color": "duck",
"icon": "book"
}],
"courses": [{
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "243",
"value": "Distribution d'\u00e9nergie",
"field_id": "60",
"created_at": "2017-10-23 14:06:51",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "10"
}, {
"id": "147",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-09-14 10:20:37",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "50",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "21",
"value": "Energ\u00e9tique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "151",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-14 10:22:40",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "306",
"value": "Stockage d'\u00e9nergie",
"field_id": "60",
"created_at": "2017-11-30 08:17:15",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "10"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}, {
"id": "7",
"value": "Spe",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 150
}, {
"id": "10",
"value": "Term Sti2d",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-12-28 11:51:58",
"deleted_at": "null",
"level_group_id": "3",
"order": 120
}],
"difficulty": 4,
"duration": 720,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-21",
"questions": [{
"id": "1357-1881",
"position": 0,
"duration": 30,
"question": {
"id": "1881",
"question": "D\u00e9finir l'\u00e9nergie finale et citer trois exemples.",
"answer": "On utilise le terme d'\u00e9nergie finale au stade de son utilisation par le consommateur final.\nCharbon, Gaz, \u00e9lectricit\u00e9, gazole...",
"image_question_url": "",
"image_answer_url": "",
"field_id": "60",
"course_id": "243",
"level_id": "10",
"difficulty": 2
}
}, {
"id": "1357-1628",
"position": 1,
"duration": 30,
"question": {
"id": "1628",
"question": "Quelle est la capacit\u00e9 d'une batterie $12 \\, V$ compos\u00e9e de 8 \u00e9l\u00e9ments en s\u00e9rie ($U_e=1,6 \\, V$, capacit\u00e9 $C_e=4000 \\, mAh $) ?",
"answer": "La capacit\u00e9 de la batterie est de  $4000 \\, mAh $, c'est la tension qui augmente !\nEnergie stock\u00e9e par un \u00e9l\u00e9ment : $W_e=C_e\u00b7U_e=4\u00b71,6=6,4 \\, Wh$\nEnergie stock\u00e9e par la batterie : $W_b=C_b\u00b7U_b=4\u00b7(1,6\u00b78)=44,8 \\, Wh$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5ba17400-df79-11e7-8779-37b0a81d8ba3",
"image_answer_url": "",
"field_id": "60",
"course_id": "306",
"level_id": "10",
"difficulty": 4
}
}, {
"id": "1357-545",
"position": 2,
"duration": 30,
"question": {
"id": "545",
"question": "Le r\u00e9seau de distribution \u00e9lectrique a un comportement de source  (statique ou dynamique) de (tension ou de courant) ?",
"answer": "Le r\u00e9seau de distribution \u00e9lectrique a un comportement de source  statique de tension.",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/2d39cbb0-3484-11e7-a9d6-db1a2a6b0811",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-81",
"position": 3,
"duration": 30,
"question": {
"id": "81",
"question": "Quelle est l'expression de l'\u00e9nergie cin\u00e9tique stock\u00e9e dans un syst\u00e8me m\u00e9canique en rotation ?",
"answer": "$W=\\frac{1}{2}\u00b7J\u00b7 \\Omega^2$ \n$J$ : moment d'inertie ($kg.m^2$)\n$\\Omega$ : vitesse angulaire du solide ($rad\/s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-97",
"position": 4,
"duration": 30,
"question": {
"id": "97",
"question": "Comment calculer le rendement d'une cha\u00eene d'\u00e9nergie ?",
"answer": "Le rendement est d\u00e9fini par $\\eta=\\frac{P_u}{P_{ab}}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-98",
"position": 5,
"duration": 30,
"question": {
"id": "98",
"question": "Quelle est la relation en la puissance $P$ et l'\u00e9nergie $W$",
"answer": "$W=P\u00b7t$ \n $W$ : l'\u00e9nergie (en $J$)\n $P$ : la puissance (en $W$ )\n$t$ : le temps (en $s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-1578",
"position": 6,
"duration": 30,
"question": {
"id": "1578",
"question": "Une batterie de capacit\u00e9 100 Ah d\u00e9livre un courant de 20 A, quelle est son autonomie ?",
"answer": "20 A correspond \u00e0 $\\frac{C}{5}=0,2\u00b7C$\nL'autonomie est de  4 heures mais la tension sera inf\u00e9rieure \u00e0 12 volts au bout de deux heures !",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/52517170-db55-11e7-b5ac-e766bd6ab2fb",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1357-1232",
"position": 7,
"duration": 30,
"question": {
"id": "1232",
"question": "Exprimer la r\u00e9sistance \u00e9quivalente $R_{eq}$ de trois r\u00e9sistances en s\u00e9rie not\u00e9es $R_1, R_2 ,R_3$. ",
"answer": "$$R_{eq}=R_1+R_2+R_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1357-1233",
"position": 8,
"duration": 30,
"question": {
"id": "1233",
"question": "Exprimer le condensateur \u00e9quivalente $C_{eq}$ de trois condensateurs en parall\u00e8le not\u00e9es $C_1, C_2 ,C_3$.",
"answer": "$$C_{eq}=C_1+C_2+C_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1357-1477",
"position": 9,
"duration": 30,
"question": {
"id": "1477",
"question": "Quelle relation existe-t-il entre la valeur maximale d'une tension alternative sinuso\u00efdale $V_{max}$ et la tension efficace du m\u00eame signal $V_{eff}$?",
"answer": "$V_{max}=V_{eff}.\\sqrt 2$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "50",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1357-711",
"position": 10,
"duration": 30,
"question": {
"id": "711",
"question": "Question 2 :\nQu'appelle-t-on tensions simples et tensions compos\u00e9es dans une distribution triphas\u00e9e ?\nUtiliser les rep\u00e8res des fils (question 1) pour les d\u00e9finir \u00e0 partir d'un sch\u00e9ma",
"answer": "R\u00e9ponse 2 :\nTensions simples $V_1, V_2 , V_3$ entre phase et neutre\nTensions compos\u00e9es $U_{12}, U_{23}, U_{31}$ entre phases prises deux \u00e0 deux\n",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8c487f60-987b-11e7-996a-61e332ec0f0d",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1357-656",
"position": 11,
"duration": 30,
"question": {
"id": "656",
"question": "Question 4 :\nExprimer et d\u00e9terminer la puissance active dans une r\u00e9sistance $R = 10\\Omega $ sous $U = 230V$\nD\u00e9duire le courant $I$ et son d\u00e9phasage $\\phi$ ",
"answer": "R\u00e9ponse 4 :\n$P =  \\frac{U^2}{R} = \\frac{230}{10}  = 5290 W$\n$I = \\frac{U}{R} = 23A$ et $\\phi  = 0$ la r\u00e9sistance a une imp\u00e9dance purement r\u00e9elle",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1357-5489",
"position": 12,
"duration": 30,
"question": {
"id": "5489",
"question": "Puissance active dissip\u00e9e par un r\u00e9sistor dont la tension aux bornes prend la valeur $u(t)=U$?",
"answer": "$P=\\frac{U^2}{R}$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ac0d3ad0-191d-11ec-bc26-6146e817e646",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-1456",
"position": 13,
"duration": 30,
"question": {
"id": "1456",
"question": "Quelle tension peut-on mesurer en les points A et B si $U=10 \\;V$, $R_1=10\\;k\\Omega$ et $R_2=10\\;k\\Omega$",
"answer": "$U_{AB}=5\\;V$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d9122d40-ce2b-11e7-acb6-f921e6e0dc75",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-4917",
"position": 14,
"duration": 30,
"question": {
"id": "4917",
"question": "Qu'indique les amp\u00e8rem\u00e8tres dans le cas suivant:",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/742a18b0-f986-11ea-9847-575213be793f",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8f6d06a0-f986-11ea-8f15-4174a81ecc21",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-5490",
"position": 15,
"duration": 30,
"question": {
"id": "5490",
"question": "Puissance active dissip\u00e9 par une inductance L ?",
"answer": "nulle",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b6879e00-191d-11ec-aa25-1f4a75a91037",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-5492",
"position": 16,
"duration": 30,
"question": {
"id": "5492",
"question": "Expression de la puissance instantan\u00e9e $p(t)$ dans un circuit \u00e9lectrique ?",
"answer": "$p(t)=u(t)\u00b7i(t)$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-5494",
"position": 17,
"duration": 30,
"question": {
"id": "5494",
"question": "Energie stock\u00e9e dans un condensateur  quand la tension  \u00e9lectrique prend la valeur $u(t)=U$ ?",
"answer": "$W=\\frac{1}{2}\u00b7C\u00b7 U^2$ \n$C$ : capacit\u00e9 (F)\n$U$ : tension \u00e9lectrique (V)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b1ae56e0-191e-11ec-93d2-3bf6c66228ef",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1357-5495",
"position": 18,
"duration": 30,
"question": {
"id": "5495",
"question": "Unit\u00e9 de la capacit\u00e9 d'un condensateur (symbole C) ?",
"answer": "Le farad (symbole F) \nOn utilise couramment le microfarad, plus rarement le millifarad.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-5497",
"position": 19,
"duration": 30,
"question": {
"id": "5497",
"question": "Que signifie DC ?",
"answer": "Direct Current \nCircuits aliment\u00e9s par une source de courant continu (on devrait dire constant)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-5498",
"position": 20,
"duration": 30,
"question": {
"id": "5498",
"question": "Que signifie AC ",
"answer": "Alternative Current\nCircuits aliment\u00e9s par une source de tension alternative (souvent sinuso\u00efdale).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-1303",
"position": 21,
"duration": 30,
"question": {
"id": "1303",
"question": "D\u00e9terminer I en fonction de E et de R.",
"answer": "La r\u00e9sistance \u00e9quivalente est $R_{\u00e9q} = \\frac {6 R^2}{2R + 3R} = \\frac 6 5 R$.\nOn utilise ensuite la loi d'Ohm : $I \\frac {E}{R_{\u00e9q}} = \\frac {5 E}{6 R}$.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a0e4feb0-c7c5-11e7-b8da-ed672e2c1f16",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1357-2623",
"position": 22,
"duration": 30,
"question": {
"id": "2623",
"question": "Quand deux dip\u00f4les sont ils mont\u00e9s en s\u00e9rie ?",
"answer": "Ils sont en s\u00e9rie quand ils sont travers\u00e9s par le m\u00eame courant.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1357-2773",
"position": 23,
"duration": 30,
"question": {
"id": "2773",
"question": "relation courant-tension d'une bobine :",
"answer": "$$U_l(t)=L\\frac{di}{dt}$$ (courant continu \u00e0 travers une bobine)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1358": {
"id": "1358",
"name": "DC2 Quizz 2",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1358\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}, {
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}, {
"id": "60",
"value": "EE",
"created_at": "2017-10-03 14:15:25",
"updated_at": "2017-10-03 14:15:25",
"deleted_at": "null",
"color": "duck",
"icon": "book"
}],
"courses": [{
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "147",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-09-14 10:20:37",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "50",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "21",
"value": "Energ\u00e9tique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "151",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-14 10:22:40",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "306",
"value": "Stockage d'\u00e9nergie",
"field_id": "60",
"created_at": "2017-11-30 08:17:15",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "10"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}, {
"id": "7",
"value": "Spe",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 150
}, {
"id": "10",
"value": "Term Sti2d",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-12-28 11:51:58",
"deleted_at": "null",
"level_group_id": "3",
"order": 120
}],
"difficulty": 3,
"duration": 780,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-28",
"questions": [{
"id": "1358-1534",
"position": 0,
"duration": 30,
"question": {
"id": "1534",
"question": "Quelle est la densit\u00e9 massique d'\u00e9nergie (en kWh\/kg) d'un batterie Lithium-ion Tesla ?\n5750 mAh  3,7 V  55 grammes\nformfactor 21700 diam\u00e8tre 21 mm hauteur 700 mm",
"answer": "Densit\u00e9 massique d'\u00e9nergie $\\frac{5,750\u00b73,7}{0.055}=386,8 \\; Wh\/kg=0,386 \\, kWh\/kg$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a3ca8920-d5ab-11e7-bca1-5d7e2cff16e7",
"image_answer_url": "",
"field_id": "60",
"course_id": "306",
"level_id": "10",
"difficulty": 2
}
}, {
"id": "1358-544",
"position": 1,
"duration": 30,
"question": {
"id": "544",
"question": "Une batterie a un comportement de source (statique ou dynamique) de (tension ou de courant) ?",
"answer": "Une batterie a un comportement de source  statique de tension.",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/27129a10-3484-11e7-978b-df5c1e0e759b",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1358-82",
"position": 2,
"duration": 30,
"question": {
"id": "82",
"question": "Quelle est l'expression de l'\u00e9nergie cin\u00e9tique stock\u00e9e dans un syst\u00e8me m\u00e9canique en translation?",
"answer": "$W=\\frac{1}{2}\u00b7m\u00b7 V^2$ \n$m$ : la masse en $kg$ \n$V$ : la vitesse en $m\/s$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1358-76",
"position": 3,
"duration": 30,
"question": {
"id": "76",
"question": "Quelle est l'expression de la puissance active pour un syst\u00e8me m\u00e9canique en translation ?",
"answer": "$P=F\u00b7V$\navec $F$ action m\u00e9canique en $N$ et $V$ vitesse  en $m{\/s}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-1577",
"position": 4,
"duration": 30,
"question": {
"id": "1577",
"question": "Une batterie de capacit\u00e9 60 Ah d\u00e9livre un courant de 20 A, quelle est son autonomie ?",
"answer": "autonomie environ 2h.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f57f2910-db54-11e7-82c6-41e641ab79a0",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1358-95",
"position": 5,
"duration": 30,
"question": {
"id": "95",
"question": "Quels sont les deux crit\u00e8res de choix d'une batterie ?",
"answer": "La Capacit\u00e9 en $Ah$ (Amp\u00e8res-heures) et la tension nominale en $Volts$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1358-1494",
"position": 6,
"duration": 30,
"question": {
"id": "1494",
"question": "Quelle est la capacit\u00e9 $C$ d'une batterie  en $Ah$ si l'\u00e9nergie stock\u00e9e est $W=2,4 \\, kWh$ et la tension nominale $12 \\,V$?",
"answer": "$C=\\frac{W\u00b71000}{U_{bat}}=\\frac{2,4\u00b7 1000}{12}=200 \\, Ah$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1358-1232",
"position": 7,
"duration": 30,
"question": {
"id": "1232",
"question": "Exprimer la r\u00e9sistance \u00e9quivalente $R_{eq}$ de trois r\u00e9sistances en s\u00e9rie not\u00e9es $R_1, R_2 ,R_3$. ",
"answer": "$$R_{eq}=R_1+R_2+R_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-1233",
"position": 8,
"duration": 30,
"question": {
"id": "1233",
"question": "Exprimer le condensateur \u00e9quivalente $C_{eq}$ de trois condensateurs en parall\u00e8le not\u00e9es $C_1, C_2 ,C_3$.",
"answer": "$$C_{eq}=C_1+C_2+C_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-1234",
"position": 9,
"duration": 30,
"question": {
"id": "1234",
"question": "Exprimer l'inductance \u00e9quivalente $R_{eq}$ de trois inductances en s\u00e9rie not\u00e9es $L_1, L_2 ,L_3$. ",
"answer": "$$L_{eq}=L_1+L_2+L_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-1476",
"position": 10,
"duration": 30,
"question": {
"id": "1476",
"question": "Quelle relation existe-t-il entre la tension simple efficace $V_{eff}$ et la tension compos\u00e9e efficace $U_{eff}$ ?",
"answer": "$U_{eff}=V_{eff.\\sqrt 3}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "50",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-1477",
"position": 11,
"duration": 30,
"question": {
"id": "1477",
"question": "Quelle relation existe-t-il entre la valeur maximale d'une tension alternative sinuso\u00efdale $V_{max}$ et la tension efficace du m\u00eame signal $V_{eff}$?",
"answer": "$V_{max}=V_{eff}.\\sqrt 2$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "50",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-1015",
"position": 12,
"duration": 30,
"question": {
"id": "1015",
"question": "Exprimer la puissance active $P$ dans une distribution \u00e9lectrique triphas\u00e9e.",
"answer": "$P=\\sqrt{3} \\,  U.I. \\cos \\phi$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "50",
"level_id": "7",
"difficulty": 3
}
}, {
"id": "1358-710",
"position": 13,
"duration": 30,
"question": {
"id": "710",
"question": "Question 1:\nComment rep\u00e8re-t-on les fils de phase et le fil de neutre dans une distribution triphas\u00e9e ? \nA quoi correspond le rep\u00e8re $P_E$",
"answer": "R\u00e9ponse 1 :\n- 3 Phases $L_1, L_2, L_3$\n- Neutre $N$\n- $P_E$ Conducteur de protection \u00e9quipotentiel (vert\/jaune)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-711",
"position": 14,
"duration": 30,
"question": {
"id": "711",
"question": "Question 2 :\nQu'appelle-t-on tensions simples et tensions compos\u00e9es dans une distribution triphas\u00e9e ?\nUtiliser les rep\u00e8res des fils (question 1) pour les d\u00e9finir \u00e0 partir d'un sch\u00e9ma",
"answer": "R\u00e9ponse 2 :\nTensions simples $V_1, V_2 , V_3$ entre phase et neutre\nTensions compos\u00e9es $U_{12}, U_{23}, U_{31}$ entre phases prises deux \u00e0 deux\n",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8c487f60-987b-11e7-996a-61e332ec0f0d",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1358-5489",
"position": 15,
"duration": 30,
"question": {
"id": "5489",
"question": "Puissance active dissip\u00e9e par un r\u00e9sistor dont la tension aux bornes prend la valeur $u(t)=U$?",
"answer": "$P=\\frac{U^2}{R}$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ac0d3ad0-191d-11ec-bc26-6146e817e646",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-1312",
"position": 16,
"duration": 30,
"question": {
"id": "1312",
"question": "Exprimer le mod\u00e8le  de Th\u00e9venin \u00e9quivalent  ($E_{TH}$  $R_{TH})$  en fonction de $U$, $R_1$, $R_2$, $R_3$ et $R_4$.",
"answer": " $E_{TH}=U_{AB0}=V_A-V_B=\\frac{R_1}{R_1+R_2}\u00b7U-\\frac{R_4}{R_3+R_4}\u00b7U$\n $R_{TH}=\\frac{R_1\u00b7R_2}{R_1+R_2}+\\frac{R_3\u00b7R_4}{R_3+R_4}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e5686dd0-c87b-11e7-848f-21c2de80e6b8",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/848c1c90-c87c-11e7-b783-31c91ce77b59",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1358-1457",
"position": 17,
"duration": 30,
"question": {
"id": "1457",
"question": "Quelle tension peut-on mesurer en les points A et B si $U=30\\;V$, $R_1=11\\;k\\Omega$ et $R_2=22\\;k\\Omega$",
"answer": "$U_{AB}=10\\;V$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a4a12200-ce2c-11e7-ab12-47f45165c08a",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1358-4918",
"position": 18,
"duration": 30,
"question": {
"id": "4918",
"question": "Question...",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e40eff60-f986-11ea-aebd-77ec6b05fa5a",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/01f02150-f987-11ea-bb1a-035b5fbe840c",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-5490",
"position": 19,
"duration": 30,
"question": {
"id": "5490",
"question": "Puissance active dissip\u00e9 par une inductance L ?",
"answer": "nulle",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b6879e00-191d-11ec-aa25-1f4a75a91037",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-5491",
"position": 20,
"duration": 30,
"question": {
"id": "5491",
"question": "puissance active dissip\u00e9e par un condensateur ?",
"answer": "nulle",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/bc3b0c60-191d-11ec-9d7c-8de31808c54b",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-5492",
"position": 21,
"duration": 30,
"question": {
"id": "5492",
"question": "Expression de la puissance instantan\u00e9e $p(t)$ dans un circuit \u00e9lectrique ?",
"answer": "$p(t)=u(t)\u00b7i(t)$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-5493",
"position": 22,
"duration": 30,
"question": {
"id": "5493",
"question": "Energie stock\u00e9e dans une inductance  quand l'intensit\u00e9 du courant \u00e9lectrique prend la valeur $i(t)=I$ ?",
"answer": "$W=\\frac{1}{2}\u00b7L\u00b7 I^2$ \n$L$ : inductance (H)\n$I$ : intensit\u00e9 du courant \u00e9lectrique (A)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5f0c7970-191e-11ec-a9ad-b7f137d15435",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-5494",
"position": 23,
"duration": 30,
"question": {
"id": "5494",
"question": "Energie stock\u00e9e dans un condensateur  quand la tension  \u00e9lectrique prend la valeur $u(t)=U$ ?",
"answer": "$W=\\frac{1}{2}\u00b7C\u00b7 U^2$ \n$C$ : capacit\u00e9 (F)\n$U$ : tension \u00e9lectrique (V)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b1ae56e0-191e-11ec-93d2-3bf6c66228ef",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1358-2772",
"position": 24,
"duration": 30,
"question": {
"id": "2772",
"question": "relation courant-tension d'un condensateur :",
"answer": "$$i(t)=C\\frac{dU_c}{dt}$$ (tension continue aux bornes d'un condensateur)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1358-2773",
"position": 25,
"duration": 30,
"question": {
"id": "2773",
"question": "relation courant-tension d'une bobine :",
"answer": "$$U_l(t)=L\\frac{di}{dt}$$ (courant continu \u00e0 travers une bobine)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1359": {
"id": "1359",
"name": "DC2 Quizz 3",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1359\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}, {
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}],
"courses": [{
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "147",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-09-14 10:20:37",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "50",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "21",
"value": "Energ\u00e9tique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "151",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-14 10:22:40",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "7"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}, {
"id": "7",
"value": "Spe",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 150
}],
"difficulty": 2,
"duration": 600,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.55,
"shared_at": "2024-10-03",
"questions": [{
"id": "1359-5489",
"position": 0,
"duration": 30,
"question": {
"id": "5489",
"question": "Puissance active dissip\u00e9e par un r\u00e9sistor dont la tension aux bornes prend la valeur $u(t)=U$?",
"answer": "$P=\\frac{U^2}{R}$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ac0d3ad0-191d-11ec-bc26-6146e817e646",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-1312",
"position": 1,
"duration": 30,
"question": {
"id": "1312",
"question": "Exprimer le mod\u00e8le  de Th\u00e9venin \u00e9quivalent  ($E_{TH}$  $R_{TH})$  en fonction de $U$, $R_1$, $R_2$, $R_3$ et $R_4$.",
"answer": " $E_{TH}=U_{AB0}=V_A-V_B=\\frac{R_1}{R_1+R_2}\u00b7U-\\frac{R_4}{R_3+R_4}\u00b7U$\n $R_{TH}=\\frac{R_1\u00b7R_2}{R_1+R_2}+\\frac{R_3\u00b7R_4}{R_3+R_4}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e5686dd0-c87b-11e7-848f-21c2de80e6b8",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/848c1c90-c87c-11e7-b783-31c91ce77b59",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-1458",
"position": 2,
"duration": 30,
"question": {
"id": "1458",
"question": "Quelle tension peut-on mesurer en les points A et B si $U=10 \\;V$, $R_1=100\\;k\\Omega$ et $R_2=100\\;k\\Omega$",
"answer": "$U_{AB}=5\\;V$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/19b37ec0-ce2d-11e7-a0c4-295a77b97383",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-4919",
"position": 3,
"duration": 30,
"question": {
"id": "4919",
"question": "Question...",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/65a09d80-f987-11ea-b554-25acfa52e83b",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-5492",
"position": 4,
"duration": 30,
"question": {
"id": "5492",
"question": "Expression de la puissance instantan\u00e9e $p(t)$ dans un circuit \u00e9lectrique ?",
"answer": "$p(t)=u(t)\u00b7i(t)$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-5493",
"position": 5,
"duration": 30,
"question": {
"id": "5493",
"question": "Energie stock\u00e9e dans une inductance  quand l'intensit\u00e9 du courant \u00e9lectrique prend la valeur $i(t)=I$ ?",
"answer": "$W=\\frac{1}{2}\u00b7L\u00b7 I^2$ \n$L$ : inductance (H)\n$I$ : intensit\u00e9 du courant \u00e9lectrique (A)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5f0c7970-191e-11ec-a9ad-b7f137d15435",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-5495",
"position": 6,
"duration": 30,
"question": {
"id": "5495",
"question": "Unit\u00e9 de la capacit\u00e9 d'un condensateur (symbole C) ?",
"answer": "Le farad (symbole F) \nOn utilise couramment le microfarad, plus rarement le millifarad.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-5496",
"position": 7,
"duration": 30,
"question": {
"id": "5496",
"question": "Quelle est l'unit\u00e9 de l'inductance (symbole L) ?",
"answer": "Le henry (symbole H).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-5498",
"position": 8,
"duration": 30,
"question": {
"id": "5498",
"question": "Que signifie AC ",
"answer": "Alternative Current\nCircuits aliment\u00e9s par une source de tension alternative (souvent sinuso\u00efdale).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-5488",
"position": 9,
"duration": 30,
"question": {
"id": "5488",
"question": "Puissance active dissip\u00e9e par un r\u00e9sistor travers\u00e9 par un courant \u00e9lectrique d'intensit\u00e9 $i(t)=I$?",
"answer": "$P=R\u00b7I^2$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/cc7a3850-191e-11ec-a7ed-31646fc90e5e",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-1303",
"position": 10,
"duration": 30,
"question": {
"id": "1303",
"question": "D\u00e9terminer I en fonction de E et de R.",
"answer": "La r\u00e9sistance \u00e9quivalente est $R_{\u00e9q} = \\frac {6 R^2}{2R + 3R} = \\frac 6 5 R$.\nOn utilise ensuite la loi d'Ohm : $I \\frac {E}{R_{\u00e9q}} = \\frac {5 E}{6 R}$.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a0e4feb0-c7c5-11e7-b8da-ed672e2c1f16",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-2631",
"position": 11,
"duration": 30,
"question": {
"id": "2631",
"question": "Qu'est-ce que le mod\u00e8le de Th\u00e9venin pour un g\u00e9n\u00e9rateur ?",
"answer": "Un g\u00e9n\u00e9rateur r\u00e9el peut \u00eatre mod\u00e9lis\u00e9 par un g\u00e9n\u00e9rateur de Th\u00e9venin, qui est l'association en s\u00e9rie d'une source de tension id\u00e9ale et d'une r\u00e9sistance interne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-2772",
"position": 12,
"duration": 30,
"question": {
"id": "2772",
"question": "relation courant-tension d'un condensateur :",
"answer": "$$i(t)=C\\frac{dU_c}{dt}$$ (tension continue aux bornes d'un condensateur)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-2773",
"position": 13,
"duration": 30,
"question": {
"id": "2773",
"question": "relation courant-tension d'une bobine :",
"answer": "$$U_l(t)=L\\frac{di}{dt}$$ (courant continu \u00e0 travers une bobine)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1359-97",
"position": 14,
"duration": 30,
"question": {
"id": "97",
"question": "Comment calculer le rendement d'une cha\u00eene d'\u00e9nergie ?",
"answer": "Le rendement est d\u00e9fini par $\\eta=\\frac{P_u}{P_{ab}}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-95",
"position": 15,
"duration": 30,
"question": {
"id": "95",
"question": "Quels sont les deux crit\u00e8res de choix d'une batterie ?",
"answer": "La Capacit\u00e9 en $Ah$ (Amp\u00e8res-heures) et la tension nominale en $Volts$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1359-1234",
"position": 16,
"duration": 30,
"question": {
"id": "1234",
"question": "Exprimer l'inductance \u00e9quivalente $R_{eq}$ de trois inductances en s\u00e9rie not\u00e9es $L_1, L_2 ,L_3$. ",
"answer": "$$L_{eq}=L_1+L_2+L_3$$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1359-1477",
"position": 17,
"duration": 30,
"question": {
"id": "1477",
"question": "Quelle relation existe-t-il entre la valeur maximale d'une tension alternative sinuso\u00efdale $V_{max}$ et la tension efficace du m\u00eame signal $V_{eff}$?",
"answer": "$V_{max}=V_{eff}.\\sqrt 2$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "50",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1359-712",
"position": 18,
"duration": 30,
"question": {
"id": "712",
"question": "Question 3 :\nDans un r\u00e9seau triphas\u00e9 + neutre basse tension $BT$ $230\/400 V$ de fr\u00e9quence $f =50 Hz$ que valent :\n- les tensions simples $V$ ?\n- les tensions compos\u00e9es $U$ ?\nS'agit-il de valeurs maximales ?\nEtablir les relations entre tensions efficaces et tensions maximales pour V et U et faire les applications num\u00e9riques.",
"answer": "R\u00e9ponse 3 :\n- $V$ tensions simples $230V$ efficace\n- $U$ tensions compos\u00e9es $400 V$ efficace\nLes tensions maximales sont $\\sqrt{2}$ fois plus \u00e9lev\u00e9es en r\u00e9gime sinuso\u00efdal.\nOn obtient $Vmax = \\sqrt{2}.230 = 325 V$ et  $Umax = \\sqrt{2}.400 = 565 V$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1359-1629",
"position": 19,
"duration": 30,
"question": {
"id": "1629",
"question": "Comment convertir $360\\, 000 \\; J$ en $kWh$ ?",
"answer": "$W=360\\; 000 \\, J=360\\, 000 \\; Ws=\\frac{360\\, 000}{3600}=100 \\,Wh=0,1 \\,kWh$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1383": {
"id": "1383",
"name": "DC4 Quizz 1",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1383\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}, {
"id": "129",
"value": "electricit\u00e9",
"created_at": "2019-10-13 13:52:21",
"updated_at": "2019-10-13 13:52:21",
"deleted_at": "null",
"color": "duck",
"icon": "1"
}],
"courses": [{
"id": "23",
"value": "Hacheur",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "48",
"value": "Machines",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "435",
"value": "machines",
"field_id": "129",
"created_at": "2019-10-13 14:54:06",
"updated_at": "2019-10-13 14:54:06",
"deleted_at": "null",
"level_id": "28"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}, {
"id": "28",
"value": "Estp",
"created_at": "2017-12-11 04:07:11",
"updated_at": "2019-11-16 08:07:51",
"deleted_at": "null",
"level_group_id": "1",
"order": 180
}],
"difficulty": 4,
"duration": 630,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-09",
"questions": [{
"id": "1383-1485",
"position": 0,
"duration": 30,
"question": {
"id": "1485",
"question": "Quelle est la relation entre la fem $E$ et la vitesse angulaire $\\Omega$ du rotor par rapport au stator ?",
"answer": "$E=k\u00b7\\Omega$\n$k$ : constante de couplage ($V\/rad\/s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5936",
"position": 1,
"duration": 30,
"question": {
"id": "5936",
"question": "Quelle est la relation entre l'intensit\u00e9 du courant dans l'induit $I_a$ et le moment du couple m\u00e9canique dans l'entrefer $C_{em}$ ?",
"answer": "$C_{em}=k\u00b7I_a$\n$k$ : constante de couplage ($N\u00b7m\/A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5938",
"position": 2,
"duration": 30,
"question": {
"id": "5938",
"question": "Comp\u00e9ter le bilan de puissance de la machine \u00e0 courant continu en n\u00e9gligeant les pertes ferromagn\u00e9tiques.",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/093ac230-d12b-11e7-9f5d-37c81c1f4496",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0c61a0b0-d12b-11e7-9245-ab01d5d4a531",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5937",
"position": 3,
"duration": 30,
"question": {
"id": "5937",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu ",
"answer": "Equation \u00e9lectrique   :  $u_{(t)} =  R\u00b7i_{(t)} +L\u00b7\\frac{d{i}}{dt} + E$   \nEquation m\u00e9canique :  $J\u00b7 \\frac{d\\Omega}{dt}=  C_{m(t)} - C_{r(t)}$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}$\nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5939",
"position": 4,
"duration": 30,
"question": {
"id": "5939",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu en r\u00e9gime permanent",
"answer": "Equation \u00e9lectrique   :  $U =  R\u00b7I + E$   \nEquation m\u00e9canique :  $C_{em} = C_{r}$  + $C_{p}$\nEquation de couplage :  $C_{em}=k\u00b7I$\nEquation de couplage :  $E=k\u00b7\\Omega$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-1490",
"position": 5,
"duration": 30,
"question": {
"id": "1490",
"question": "Dessiner le mod\u00e8le \u00e9lectrique d'une machine \u00e0 courant continu en convention g\u00e9n\u00e9rateur et \u00e9tablir la loi des mailles.",
"answer": "$u_{(t)}+R\u00b7i_{(t)}+L\u00b7\\frac{di}{dt}-E=0$\n$R$ : r\u00e9sistance de l'enroulement d'induit ($\\Omega$)\n$L$ : inductance de l'enroulement d'induit ($H$)\n$E$ : fem ($V$)",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0fe701b0-d1bd-11e7-b4b4-f3487aa8c22a",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1383-1480",
"position": 6,
"duration": 30,
"question": {
"id": "1480",
"question": "Comment s'exprime la puissance \u00e9lectromagn\u00e9tique $P_{em}$ d'une machine \u00e0 courant continu du point de vue \u00e9lectrique ?",
"answer": "$P_{em}=E\u00b7I_a$\n$E$ : fem de la machine ($V$)\n$I_a$ : intensit\u00e9 du courant dans l'induit ($A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5940",
"position": 7,
"duration": 30,
"question": {
"id": "5940",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu dans le cas d'un essai \u00e0 vide.",
"answer": "Essai \u00e0 vide : $C_{u(t)}=0$\nEquation \u00e9lectrique   :  $u_{(t)} =  R\u00b7i_{(t)} +L\u00b7\\frac{d{i}}{dt} + E$   \nEquation m\u00e9canique :  $J\u00b7 \\frac{d\\Omega}{dt}=  C_{m(t)} - C_{r(t)}=  -C_{r(t)}+C_{em(t)}- C_p$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}$ \nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-83",
"position": 8,
"duration": 30,
"question": {
"id": "83",
"question": "Citer les 4 r\u00e8gles \u00e0 respecter pour les sources de tension et de courant.",
"answer": "R\u00e8gle n\u00b01 : On ne doit pas  interconnecter deux sources de tension  diff\u00e9rentes. \nR\u00e8gle n\u00b02 : il ne faut jamais court-circuiter une source de tension.\nR\u00e8gle n\u00b03 : On ne doit pas  interconnecter deux sources de courant diff\u00e9rentes. \nR\u00e8gle n\u00b04 : Il ne faut jamais laisser une source de courant en circuit ouvert.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-1481",
"position": 9,
"duration": 30,
"question": {
"id": "1481",
"question": "Comment s'exprime la puissance utile $P_u$ d'une machine \u00e0 courant continu ?",
"answer": " $P_u=C_u\u00b7\\Omega$\n$C_u$ : Moment du couple utile  ($N\u00b7m$)\n$\\Omega$ : vitesse angulaire du rotor par rapport au stator ($rad\/s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-3076",
"position": 10,
"duration": 30,
"question": {
"id": "3076",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu dans le cas d'un essai \u00e0 rotor bloqu\u00e9.",
"answer": "$\\Omega_{(t)}=0$\nEquation \u00e9lectrique   :  $u_{(t)} =  R\u00b7i_{(t)} +L\u00b7\\frac{d{i}}{dt}$   \nEquation m\u00e9canique :  $ C_{em(t)} =C_{blocage}$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}$\nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}=0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-5941",
"position": 11,
"duration": 30,
"question": {
"id": "5941",
"question": "Comment s'exprime la puissance absorb\u00e9e $P_{ab}$ d'une machine \u00e0 courant continu \u00e0 aimants ?",
"answer": " $P_{ab}=U_a\u00b7I_a$\n$U_a$ : tension d'alimentation de l'induit  ($V$)\n$I_a$ : intensit\u00e9 du courant dans l'induit ($A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-5942",
"position": 12,
"duration": 30,
"question": {
"id": "5942",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu dans le cas d'un essai de ralentissement.",
"answer": "$i_{(t)}=0$\nEquation \u00e9lectrique   :  $u_{(t)} =  E$   \nEquation m\u00e9canique :  $J\u00b7 \\frac{d\\Omega}{dt}=  C_{m(t)} - C_{r(t)}=- C_{r(t)}$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}=0$\nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-1484",
"position": 13,
"duration": 30,
"question": {
"id": "1484",
"question": "Que repr\u00e9sente $R_a$, $L_a$ et $E$ dans le sch\u00e9ma \u00e9lectrique  de la machine \u00e0 courant continu ?",
"answer": "$R_a$ : r\u00e9sistance de l'enroulement d'induit (effet thermique : pertes joules)\n$L_a$ : inductance de l'enroulement d'induit (effet \u00e9lectromagn\u00e9tique : cr\u00e9ation du champ magn\u00e9tique de l'induit)\n$E$ : fem force \u00e9lectromotrice (tension induite dans l'enroulement d'induit par le balayage du champ magn\u00e9tique)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ff3aae20-d128-11e7-882d-83a0979f16d2",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-1489",
"position": 14,
"duration": 30,
"question": {
"id": "1489",
"question": "Comment s'exprime la puissance \u00e9lectromagn\u00e9tique $P_{em}$ d'une machine \u00e0 courant continu du point de vue m\u00e9canique ?",
"answer": "$P_{em}=T_{em}\u00b7\\Omega$\n$T_{em}$ : moment du couple m\u00e9canique dans l'entrefer  ($N\u00b7m$)\n$\\Omega$ : vitesse angulaire du rotor par rapport au stator ($rad\/s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-1491",
"position": 15,
"duration": 30,
"question": {
"id": "1491",
"question": "Dessiner le mod\u00e8le \u00e9lectrique d'une machine \u00e0 courant continu en convention r\u00e9cepteur et \u00e9tablir la loi des mailles.",
"answer": "$u_{a(t)}-R_a\u00b7i_{a(t)}-L_a\u00b7\\frac{di_a}{dt}-E=0$\n$R$ : r\u00e9sistance de l'enroulement d'induit ($\\Omega$)\n$L$ : inductance de l'enroulement d'induit ($H$)\n$E$ : fem ($V$)",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ac7325b0-d1bd-11e7-b7ec-cfadf363a3dd",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1383-1483",
"position": 16,
"duration": 30,
"question": {
"id": "1483",
"question": "Comment s'expriment les pertes joules $P_j$ d'une machine \u00e0 courant continu ?",
"answer": "$P_j=R_a\u00b7I_a^2$ pour une machine \u00e0 aimants permanents\n $P_j=R_a\u00b7I_a^2+R_e\u00b7I_e^2$ pour une machine \u00e0 inducteur bobin\u00e9\n$R_a$ : r\u00e9sistance de l'induit ($\\Omega$)\n$I_a$  : intensit\u00e9 du courant dans l'induit ($A$)\n$R_e$  : r\u00e9sistance de l'inducteur ($\\Omega$)\n$I_e$  : intensit\u00e9 du courant dans l'inducteur ($A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1383-3791",
"position": 17,
"duration": 30,
"question": {
"id": "3791",
"question": "\u00e0 quoi sert le collecteur dans une machine \u00e0 courant continu ?",
"answer": "\u00e0 modifier le sens du courant dans les enroulements de l'induit (au rotor)",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f3559ca0-00c5-11ea-bc23-57ca1b43a287",
"field_id": "129",
"course_id": "435",
"level_id": "28",
"difficulty": 3
}
}, {
"id": "1383-3870",
"position": 18,
"duration": 30,
"question": {
"id": "3870",
"question": "Dans une machine \u00e0 courant continu, pourquoi l'induit est un assemblage de t\u00f4les alors que le stator est coul\u00e9 et massif ?",
"answer": "Seul le rotor est le si\u00e8ge d'un champ magn\u00e9tique variable, donc de pertes par courants de Foucault ; le feuilletage du rotor et l'ajout de silicium \u00e0 la coul\u00e9e augmente la r\u00e9sistance donc limite les pertes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "129",
"course_id": "435",
"level_id": "28",
"difficulty": 3
}
}, {
"id": "1383-4009",
"position": 19,
"duration": 30,
"question": {
"id": "4009",
"question": "Que repr\u00e9sente $L_a$ dans le sch\u00e9ma \u00e9lectrique  de la machine \u00e0 courant continu ?",
"answer": "$L_a$ : inductance de l'enroulement d'induit (effet \u00e9lectromagn\u00e9tique : cr\u00e9ation du champ magn\u00e9tique de l'induit)\n",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/2445a1a0-0dc0-11ea-b07a-f570a2f39509",
"image_answer_url": "",
"field_id": "129",
"course_id": "435",
"level_id": "28",
"difficulty": 2
}
}, {
"id": "1383-4008",
"position": 20,
"duration": 30,
"question": {
"id": "4008",
"question": "Que repr\u00e9sente $R_a$ dans le mod\u00e8le  de la machine \u00e0 courant continu ?",
"answer": "$R_a$ : r\u00e9sistance de l'enroulement d'induit (effet thermique : pertes joules)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d5b70270-0dbf-11ea-8cfa-81bce4083685",
"image_answer_url": "",
"field_id": "129",
"course_id": "435",
"level_id": "28",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1384": {
"id": "1384",
"name": "DC4 Quizz 2",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1384\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "23",
"value": "Hacheur",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "48",
"value": "Machines",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-15",
"questions": [{
"id": "1384-1595",
"position": 0,
"duration": 30,
"question": {
"id": "1595",
"question": "D\u00e9finition d'un hacheur parall\u00e8le (ou hacheur \u00e9l\u00e9vateur) ?",
"answer": "C'est un convertisseur d'\u00e9lectronique de puissance Continu - Continu qui r\u00e9alise le transfert direct d'une source de courant vers une source de tension.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b1c0e910-dc1a-11e7-9ddc-63c4cc07e0af",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1384-1596",
"position": 1,
"duration": 30,
"question": {
"id": "1596",
"question": "Quels sont les quadrants utilis\u00e9s par ce hacheur ?",
"answer": "Cette structure accepte une r\u00e9versibilit\u00e9 du courant dans la charge mais pas de la tension aux bornes de la charge. C'est donc une structure 2 quadrants.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/fd13f100-dc1a-11e7-878a-ff54077f53b5",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1384-5936",
"position": 2,
"duration": 30,
"question": {
"id": "5936",
"question": "Quelle est la relation entre l'intensit\u00e9 du courant dans l'induit $I_a$ et le moment du couple m\u00e9canique dans l'entrefer $C_{em}$ ?",
"answer": "$C_{em}=k\u00b7I_a$\n$k$ : constante de couplage ($N\u00b7m\/A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1384-1673",
"position": 3,
"duration": 30,
"question": {
"id": "1673",
"question": "Quel est le composant passant lorsque $H_2$ est command\u00e9 et $i_s>0$ ?",
"answer": "C'est la diode $D_2$ qui conduit",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9c7c9000-f576-11e7-875b-e1f0e71e652d",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1384-1598",
"position": 4,
"duration": 30,
"question": {
"id": "1598",
"question": "Quels sont les quadrants utilis\u00e9s par ce hacheur ?",
"answer": "Cette structure accepte une r\u00e9versibilit\u00e9 du courant dans la charge et de la tension aux bornes de la charge. C'est donc une structure 4 quadrants.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/dbc84f20-dc1a-11e7-9f14-059ab3c08af8",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1384-5938",
"position": 5,
"duration": 30,
"question": {
"id": "5938",
"question": "Comp\u00e9ter le bilan de puissance de la machine \u00e0 courant continu en n\u00e9gligeant les pertes ferromagn\u00e9tiques.",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/093ac230-d12b-11e7-9f5d-37c81c1f4496",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0c61a0b0-d12b-11e7-9245-ab01d5d4a531",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1384-5937",
"position": 6,
"duration": 30,
"question": {
"id": "5937",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu ",
"answer": "Equation \u00e9lectrique   :  $u_{(t)} =  R\u00b7i_{(t)} +L\u00b7\\frac{d{i}}{dt} + E$   \nEquation m\u00e9canique :  $J\u00b7 \\frac{d\\Omega}{dt}=  C_{m(t)} - C_{r(t)}$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}$\nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1384-1675",
"position": 7,
"duration": 30,
"question": {
"id": "1675",
"question": "Quels sont les composants passants lorsque $H_1$ et $H_4$  sont command\u00e9s et $i_s<0$ ?",
"answer": "les composants passants sont  $D_1$  et  $D_4$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9b2e5f60-f577-11e7-bc0f-71bcd37836e5",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1384-1677",
"position": 8,
"duration": 30,
"question": {
"id": "1677",
"question": "Calculer la valeur moyenne  $<U_{m(t)}>$",
"answer": " $<U_{m(t)}>=12 \\frac{30}{60}=6 V$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c3446090-f579-11e7-8764-dde2baa927a3",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1384-535",
"position": 9,
"duration": 30,
"question": {
"id": "535",
"question": "Montrer que pour une machine \u00e0 courant continu, la vitesse $\u03a9_{(t)}$ est proportionnelle \u00e0 $<U_{(t)}>$ si on n\u00e9glige la chute de tension dans la r\u00e9sistance de l'enroulement d'induit.",
"answer": "L'\u00e9quation \u00e9lectrique est obtenue par la loi des mailles :   \n$U_{(t)}-L \\cdot \\frac{di_s}{dt}-E=0 $\t\nen l\u2019exprimant en valeur moyenne : $<U_{(t)} -L \\cdot \\frac{di_s}{dt}-E>=0 $ \n$\\Leftrightarrow$   $<U_{(t)}>-<L \\cdot \\frac{di_s}{dt}>-E=0 $ \n\tLe terme $<L \\cdot \\frac{di_s}{dt}>$ est toujours nul dans un r\u00e9gime p\u00e9riodique de courant. alors$<U_{(t)}>=E $  \n  d\u2019autre part par la relation de couplage  $E=k\u00b7\\Omega _{(t)}$  alors  $<U_{(t)}>=k\u00b7\\Omega _{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1384-1490",
"position": 10,
"duration": 30,
"question": {
"id": "1490",
"question": "Dessiner le mod\u00e8le \u00e9lectrique d'une machine \u00e0 courant continu en convention g\u00e9n\u00e9rateur et \u00e9tablir la loi des mailles.",
"answer": "$u_{(t)}+R\u00b7i_{(t)}+L\u00b7\\frac{di}{dt}-E=0$\n$R$ : r\u00e9sistance de l'enroulement d'induit ($\\Omega$)\n$L$ : inductance de l'enroulement d'induit ($H$)\n$E$ : fem ($V$)",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0fe701b0-d1bd-11e7-b4b4-f3487aa8c22a",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1384-1593",
"position": 11,
"duration": 30,
"question": {
"id": "1593",
"question": "Quelles sont les deux familles de hacheur ?",
"answer": "Les hacheurs \u00e0 liaison continu et les alimentations \u00e0 d\u00e9coupage.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1384-1594",
"position": 12,
"duration": 30,
"question": {
"id": "1594",
"question": "D\u00e9finition du hacheur s\u00e9rie (ou hacheur abaisseur) ?",
"answer": "C'est un convertisseur d'\u00e9lectronique de puissance Continu - Continu qui r\u00e9alise le transfert direct d'une source de tension vers une source de courant.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1385": {
"id": "1385",
"name": "DC4 Quizz3",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1385\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "23",
"value": "Hacheur",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "48",
"value": "Machines",
"field_id": "11",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 450,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-15",
"questions": [{
"id": "1385-1595",
"position": 0,
"duration": 30,
"question": {
"id": "1595",
"question": "D\u00e9finition d'un hacheur parall\u00e8le (ou hacheur \u00e9l\u00e9vateur) ?",
"answer": "C'est un convertisseur d'\u00e9lectronique de puissance Continu - Continu qui r\u00e9alise le transfert direct d'une source de courant vers une source de tension.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b1c0e910-dc1a-11e7-9ddc-63c4cc07e0af",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1385-1596",
"position": 1,
"duration": 30,
"question": {
"id": "1596",
"question": "Quels sont les quadrants utilis\u00e9s par ce hacheur ?",
"answer": "Cette structure accepte une r\u00e9versibilit\u00e9 du courant dans la charge mais pas de la tension aux bornes de la charge. C'est donc une structure 2 quadrants.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/fd13f100-dc1a-11e7-878a-ff54077f53b5",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1673",
"position": 2,
"duration": 30,
"question": {
"id": "1673",
"question": "Quel est le composant passant lorsque $H_2$ est command\u00e9 et $i_s>0$ ?",
"answer": "C'est la diode $D_2$ qui conduit",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9c7c9000-f576-11e7-875b-e1f0e71e652d",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1487",
"position": 3,
"duration": 30,
"question": {
"id": "1487",
"question": "Comment s'exprime la constante de temps \u00e9lectrom\u00e9canique  $\\tau_{em}$ d'une machine \u00e0 courant continu ?",
"answer": "$\\tau_{em}=\\frac{R_a\u00b7J}{k^2}$ (s)\n$R_a$ : R\u00e9sistance du bobinage de l\u2019induit ($\\Omega$)\n$J$ : Inertie \u00e9quivalente du rotor et de la charge m\u00e9canique ($kg\u00b7m^2$)\n$k$ : constante de couplage ($Nm\/A$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-1598",
"position": 4,
"duration": 30,
"question": {
"id": "1598",
"question": "Quels sont les quadrants utilis\u00e9s par ce hacheur ?",
"answer": "Cette structure accepte une r\u00e9versibilit\u00e9 du courant dans la charge et de la tension aux bornes de la charge. C'est donc une structure 4 quadrants.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/dbc84f20-dc1a-11e7-9f14-059ab3c08af8",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1675",
"position": 5,
"duration": 30,
"question": {
"id": "1675",
"question": "Quels sont les composants passants lorsque $H_1$ et $H_4$  sont command\u00e9s et $i_s<0$ ?",
"answer": "les composants passants sont  $D_1$  et  $D_4$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9b2e5f60-f577-11e7-bc0f-71bcd37836e5",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1677",
"position": 6,
"duration": 30,
"question": {
"id": "1677",
"question": "Calculer la valeur moyenne  $<U_{m(t)}>$",
"answer": " $<U_{m(t)}>=12 \\frac{30}{60}=6 V$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c3446090-f579-11e7-8764-dde2baa927a3",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-540",
"position": 7,
"duration": 30,
"question": {
"id": "540",
"question": "Calculer l'expression du courant  $i_{s(t)}$   si   $i_{(0)}=I_{min}$",
"answer": "Loi des mailles  $U_{e}-L \\cdot \\frac{di_s}{dt}-E=0 $\n$\\Leftrightarrow di_s=\\frac{U_{e}-E}{L}\\cdot \\mathrm{d}t $\n$ \\Leftrightarrow i_{s(t)}=\\frac{U_{e}-E}{L}\\cdot t+cst$ \n$i_{s(0)}=\\frac{U_{e}-E}{L}\\cdot 0+cst=I_{min}$\nalors $i_{s(t)}=\\frac{U_{e}-E}{L}\\cdot t+I_{min}$ ",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/91b2ead0-3483-11e7-8331-2f2f6cf0bf77",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-541",
"position": 8,
"duration": 30,
"question": {
"id": "541",
"question": "Calculer l'expression du courant  $i_{(t)}$ pour $t>\\frac{T}{2}$   si$i_{(\\frac{T}{2})}=I_{max}$",
"answer": "Loi des mailles $-L \\cdot \\frac{di_s}{dt}-E=0 $\n$\\Leftrightarrow di_s=\\frac{-E}{L}\\cdot \\mathrm{d}t $\n$ \\Leftrightarrow i_{s(t)}=\\frac{-E}{L}\\cdot t+cst$ \n$i_{s(\\frac{T}{2})}=\\frac{-E}{L}\\cdot \\frac{T}{2}+cst=I_{max}$\n$cst=I_{max}+\\frac{E}{L}\\cdot \\frac{T}{2}$\nalors $i_{s(t)}=\\frac{-E}{L}\\cdot t+I_{max}+\\frac{E}{L}\\cdot \\frac{T}{2}= \\frac{-E}{L}\\cdot (t-\\frac{T}{2})+I_{max}$ ",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/c1e2d9a0-3483-11e7-81af-cbe050722cf5",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-535",
"position": 9,
"duration": 30,
"question": {
"id": "535",
"question": "Montrer que pour une machine \u00e0 courant continu, la vitesse $\u03a9_{(t)}$ est proportionnelle \u00e0 $<U_{(t)}>$ si on n\u00e9glige la chute de tension dans la r\u00e9sistance de l'enroulement d'induit.",
"answer": "L'\u00e9quation \u00e9lectrique est obtenue par la loi des mailles :   \n$U_{(t)}-L \\cdot \\frac{di_s}{dt}-E=0 $\t\nen l\u2019exprimant en valeur moyenne : $<U_{(t)} -L \\cdot \\frac{di_s}{dt}-E>=0 $ \n$\\Leftrightarrow$   $<U_{(t)}>-<L \\cdot \\frac{di_s}{dt}>-E=0 $ \n\tLe terme $<L \\cdot \\frac{di_s}{dt}>$ est toujours nul dans un r\u00e9gime p\u00e9riodique de courant. alors$<U_{(t)}>=E $  \n  d\u2019autre part par la relation de couplage  $E=k\u00b7\\Omega _{(t)}$  alors  $<U_{(t)}>=k\u00b7\\Omega _{(t)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-537",
"position": 10,
"duration": 30,
"question": {
"id": "537",
"question": "Calculer l'expression de la valeur moyenne de $u_{3(t)}$ not\u00e9e $<u_{3(t)}>$",
"answer": " $<u_{1(t)}>=\\frac{1}{T}((\\alpha \\cdot T-0)\\cdot (-U) + (T- \\alpha \\cdot T)\\cdot U)=(1-2 \\alpha) \\cdot U$\n $<f_{(t)}>=\\frac{1}{T}(intervalle)(valeur)$ pour une fonction $f_{(t)}$  constante par morceaux.",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/da15a290-3483-11e7-8186-ed394f82898d",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1490",
"position": 11,
"duration": 30,
"question": {
"id": "1490",
"question": "Dessiner le mod\u00e8le \u00e9lectrique d'une machine \u00e0 courant continu en convention g\u00e9n\u00e9rateur et \u00e9tablir la loi des mailles.",
"answer": "$u_{(t)}+R\u00b7i_{(t)}+L\u00b7\\frac{di}{dt}-E=0$\n$R$ : r\u00e9sistance de l'enroulement d'induit ($\\Omega$)\n$L$ : inductance de l'enroulement d'induit ($H$)\n$E$ : fem ($V$)",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0fe701b0-d1bd-11e7-b4b4-f3487aa8c22a",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1385-3076",
"position": 12,
"duration": 30,
"question": {
"id": "3076",
"question": "Citer les quatre \u00e9quations d'une machine \u00e0 courant continu dans le cas d'un essai \u00e0 rotor bloqu\u00e9.",
"answer": "$\\Omega_{(t)}=0$\nEquation \u00e9lectrique   :  $u_{(t)} =  R\u00b7i_{(t)} +L\u00b7\\frac{d{i}}{dt}$   \nEquation m\u00e9canique :  $ C_{em(t)} =C_{blocage}$\nEquation de couplage :  $C_{em(t)}=k\u00b7i_{(t)}$\nEquation de couplage :  $E=k\u00b7\\Omega_{(t)}=0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1385-1594",
"position": 13,
"duration": 30,
"question": {
"id": "1594",
"question": "D\u00e9finition du hacheur s\u00e9rie (ou hacheur abaisseur) ?",
"answer": "C'est un convertisseur d'\u00e9lectronique de puissance Continu - Continu qui r\u00e9alise le transfert direct d'une source de tension vers une source de courant.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "23",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1385-1489",
"position": 14,
"duration": 30,
"question": {
"id": "1489",
"question": "Comment s'exprime la puissance \u00e9lectromagn\u00e9tique $P_{em}$ d'une machine \u00e0 courant continu du point de vue m\u00e9canique ?",
"answer": "$P_{em}=T_{em}\u00b7\\Omega$\n$T_{em}$ : moment du couple m\u00e9canique dans l'entrefer  ($N\u00b7m$)\n$\\Omega$ : vitesse angulaire du rotor par rapport au stator ($rad\/s$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "48",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1386": {
"id": "1386",
"name": "D\u00e9nombrement",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1386\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-07",
"questions": [{
"id": "1386-2904",
"position": 0,
"duration": 30,
"question": {
"id": "2904",
"question": "\\[(x+y)^n=\\,?\\]",
"answer": "Bin\u00f4me de Newton:\n\\[(x+y)^n=\\sum_{k=0}^n\\binom{n}{k}x^ky^{n-k}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3097",
"position": 1,
"duration": 30,
"question": {
"id": "3097",
"question": "Nombre de parties \u00e0 $k$ \u00e9l\u00e9ments d'un ensemble de cardinal $n$ .",
"answer": "$\\displaystyle\\binom{n}{k}=\\frac{n(n-1)\\cdots(n-k+1)}{k!}=\\frac{n!}{k!(n-k)!}$\n\nil s'agit des combinaisons.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3099",
"position": 2,
"duration": 30,
"question": {
"id": "3099",
"question": "Nombre d'\u00e9l\u00e9ments du produit cart\u00e9sien $E\\times F$ (o\u00f9 $E$, $F$ sont finis de cardinaux respectifs $m$ et $n$).",
"answer": "$m\\times n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3101",
"position": 3,
"duration": 30,
"question": {
"id": "3101",
"question": "Compl\u00e9ter avec un autre coefficient binomial : $\\displaystyle \\binom{n}{n-k}=\\ldots\\,?$",
"answer": "$\\displaystyle \\binom{n}{k}$ (\u00ab choisir, c'est renoncer \u00bb)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3103",
"position": 4,
"duration": 30,
"question": {
"id": "3103",
"question": "Nombre de permutations d'un ensemble \u00e0 $n$ \u00e9l\u00e9ments.",
"answer": "$n!$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-5381",
"position": 5,
"duration": 30,
"question": {
"id": "5381",
"question": "Nombre de $p$-listes de E (E \u00e9tant fini de cardinal $n$)\u00a0?",
"answer": "$n^p$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-5874",
"position": 6,
"duration": 30,
"question": {
"id": "5874",
"question": "Une urne contient 15 jetons num\u00e9rot\u00e9s de 1 \u00e0 15. On tire successivement et sans remise 4 jetons de cette urne. Nombre de tirages possibles ?",
"answer": "15x14x13x12 (il s'agit d'arrangements)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-5875",
"position": 7,
"duration": 30,
"question": {
"id": "5875",
"question": "Une urne contient 15 jetons num\u00e9rot\u00e9s de 1 \u00e0 15. On tire simultan\u00e9ment 4 jetons de cette urne. Nombre de tirages possibles ?",
"answer": "$\\displaystyle{\\binom{15}{4}=\\dfrac{15!}{4!(15-4)!}=\\dfrac{15 \\times 14 \\times 13 \\times 12}{4 \\times 3 \\times 2}}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-5382",
"position": 8,
"duration": 30,
"question": {
"id": "5382",
"question": "Nombre d'arrangements de $p$ \u00e9l\u00e9ments de E (E fini, de cardinal $n$)",
"answer": "$n(n-1)...(n-p+1)=\\dfrac{n!}{(n-p)!}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3096",
"position": 9,
"duration": 30,
"question": {
"id": "3096",
"question": "Nombre de parties (ou de sous-ensembles) d'un ensemble fini de cardinal $n$ ?",
"answer": "$2^n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-5907",
"position": 10,
"duration": 30,
"question": {
"id": "5907",
"question": "Une urne contient 15 jetons num\u00e9rot\u00e9s de 1 \u00e0 15. On tire successivement et avec remise 4 jetons de cette urne. Nombre de tirages possibles ?",
"answer": "$15^4$ (il s'agit de 4-listes).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1386-3100",
"position": 11,
"duration": 30,
"question": {
"id": "3100",
"question": "$\\displaystyle\\sum_{k=0}^n \\binom{n}{k}=\\ldots\\,?$",
"answer": "$2^n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1387": {
"id": "1387",
"name": "syst\u00e8mes et familles de vecteurs",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1387\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-21",
"questions": [{
"id": "1387-5373",
"position": 0,
"duration": 30,
"question": {
"id": "5373",
"question": "La matrice suivante est -elle \u00e9chelonn\u00e9e en lignes ? \u00e9chelonn\u00e9e r\u00e9duite en lignes ?\n$M=\\begin{pmatrix} 1&2&0&3\\\\0&1&1&2\\\\0&0&0&1 \\end{pmatrix}$",
"answer": "\u00e9chelonn\u00e9e : oui\n\u00e9chelonn\u00e9e r\u00e9duite : non, le 2e pivot n'est pas le seul \u00e9l\u00e9ment non nul de sa colonne.\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5375",
"position": 1,
"duration": 30,
"question": {
"id": "5375",
"question": "Qu'appelle-t-on rang d'un syst\u00e8me lin\u00e9aire ?",
"answer": "Le nombre de pivots de la matrice \u00e9chelonn\u00e9e r\u00e9duite en ligne associ\u00e9e.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5628",
"position": 2,
"duration": 30,
"question": {
"id": "5628",
"question": "Quelle op\u00e9ration faut-il effectuer pour rendre la matrice suivante \u00e9chelonn\u00e9e r\u00e9duite en lignes ?\n$M=\\begin{pmatrix} 1&-1&0&3\\\\0&0&1&0\\\\0&0&0&1 \\end{pmatrix}$",
"answer": "$L_1 \\leftarrow L_1-3L_3$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5378",
"position": 3,
"duration": 30,
"question": {
"id": "5378",
"question": "On consid\u00e8re un syst\u00e8me $\\textit{compatible}$ \u00e0 $p$ inconnues et de rang $r$ avec $p>r$. Que dire du nombre de solutions du syst\u00e8me ?",
"answer": "il y en a une infinit\u00e9, elles sont param\u00e9tr\u00e9es par les p-r inconnues secondaires.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5377",
"position": 4,
"duration": 30,
"question": {
"id": "5377",
"question": "On consid\u00e8re un syst\u00e8me \u00e0 $p$ inconnues et de rang $r$ avec $p=r$. Ce syst\u00e8me admet-il une unique solution ?",
"answer": "Pas forc\u00e9ment:\noui s'il est compatible, non dans le cas contraire. Le syst\u00e8me peut \u00eatre incompatible notamment s'il y a plus d'\u00e9quations que d'inconnues.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5655",
"position": 5,
"duration": 30,
"question": {
"id": "5655",
"question": "D\u00e9finition de $\\mathrm{Vect}(u_1,\\dots,u_p)$ o\u00f9 $u_1,\\dots, u_p$ sont des vecteurs de $\\mathbb{R}^n$ ?",
"answer": "C'est l'ensemble des combinaisons lin\u00e9aires de ces $p$ vecteurs, autrement dit l'ensemble des vecteurs qui s'\u00e9crivent $\\lambda_1u_1+\\cdots+\\lambda_pu_p,\\quad$ avec $ \\lambda_1,\\dots,\\lambda_p$ r\u00e9els.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5656",
"position": 6,
"duration": 30,
"question": {
"id": "5656",
"question": "D\u00e9finition de $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$ est g\u00e9n\u00e9ratrice de $\\mathbb{R}^n$ ?",
"answer": "Tout vecteur $\\vec{X}$ de $\\mathbb{R}^n$ peut s'\u00e9crire comme combiniaison lin\u00e9aire des vecteurs $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$, autrement dit il existe $p$ r\u00e9els  $\\lambda_1,\\dots,\\lambda_p$ tels que $\\vec{X}=\\lambda_1 \\vec{u_1}+\\lambda_2 \\vec{u_2}+...+\\lambda_p \\vec{u_p}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5657",
"position": 7,
"duration": 30,
"question": {
"id": "5657",
"question": "D\u00e9finition de $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$ est libre dans $\\mathbb{R}^n$ ?",
"answer": "$(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$ est libre si :\n$(\\lambda_1 \\vec{u_1}+\\lambda_2 \\vec{u_2}+...+\\lambda_p \\vec{u_p}=\\vec{0})$ impose $(\\lambda_1=\\lambda_2=...=\\lambda_p=0)$\n\nvariante : Une famille de vecteurs de $\\mathbb{R}^n$ est dite libre si aucun de ses vecteurs ne peut s'\u00e9crire comme combinaison lin\u00e9aire des autres.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5372",
"position": 8,
"duration": 30,
"question": {
"id": "5372",
"question": "Quelles sont les op\u00e9rations \u00e9l\u00e9mentaires sur les lignes d'un syst\u00e8me lin\u00e9aire ?",
"answer": "1) Echange de 2 lignes.  ($L_i \\leftrightarrow L_j$)\n2) Multiplication d'une ligne par un r\u00e9el $k$ non nul.   ($L_i \\leftarrow k.L_i$)\n3) Ajout \u00e0 une ligne de k fois une autre ligne. ($L_i \\leftarrow L_i+k.L_j$ avec $j\\neq i$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5374",
"position": 9,
"duration": 30,
"question": {
"id": "5374",
"question": "Qu'est-ce qui explique que les op\u00e9rations \u00e9l\u00e9mentaires sur les lignes ne modifient pas les solutions d'un syst\u00e8me ?",
"answer": "Elles sont bijectives, chaque op\u00e9ration \u00e9l\u00e9mentaire admet une r\u00e9ciproque qui permet de revenir au syst\u00e8me de d\u00e9part.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1387-5630",
"position": 10,
"duration": 30,
"question": {
"id": "5630",
"question": "Qu'appelle-t-on pivot d'une ligne dans la matrice associ\u00e9e \u00e0 un syst\u00e8me lin\u00e9aire ?",
"answer": "Le premier \u00e9l\u00e9ment non nul de la ligne.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1389": {
"id": "1389",
"name": "DC2 Alternatif",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1389\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}, {
"id": "23",
"value": "Physique",
"created_at": "2017-07-07 10:44:53",
"updated_at": "2018-01-21 18:42:49",
"deleted_at": "null",
"color": "donny",
"icon": "flask"
}, {
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}, {
"id": "129",
"value": "electricit\u00e9",
"created_at": "2019-10-13 13:52:21",
"updated_at": "2019-10-13 13:52:21",
"deleted_at": "null",
"color": "duck",
"icon": "1"
}],
"courses": [{
"id": "53",
"value": "Alg\u00e8bre",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "115",
"value": "Signaux",
"field_id": "23",
"created_at": "2017-08-21 12:25:59",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "112",
"value": "Electricit\u00e9",
"field_id": "23",
"created_at": "2017-08-21 12:21:44",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "147",
"value": "Electricit\u00e9",
"field_id": "11",
"created_at": "2017-09-14 10:20:37",
"updated_at": "2018-01-21 18:39:30",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "21",
"value": "Energ\u00e9tique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "151",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-14 10:22:40",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "7"
}, {
"id": "438",
"value": "Sinuso\u00efdal",
"field_id": "129",
"created_at": "2019-10-13 14:54:51",
"updated_at": "2019-10-13 14:54:51",
"deleted_at": "null",
"level_id": "28"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}, {
"id": "7",
"value": "Spe",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 150
}, {
"id": "28",
"value": "Estp",
"created_at": "2017-12-11 04:07:11",
"updated_at": "2019-11-16 08:07:51",
"deleted_at": "null",
"level_group_id": "1",
"order": 180
}],
"difficulty": 3,
"duration": 690,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-29",
"questions": [{
"id": "1389-5508",
"position": 0,
"duration": 30,
"question": {
"id": "5508",
"question": "Soit une imp\u00e9dance $\\underline Z$ . Que signifie $\\vert \\underline Z \\vert$ ?",
"answer": "$\\vert \\underline Z \\vert$ repr\u00e9sente le module du nombre complexe $\\underline Z$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1389-5509",
"position": 1,
"duration": 30,
"question": {
"id": "5509",
"question": "Soit une imp\u00e9dance $\\underline Z$ . Que signifie $Arg(\\underline Z )$ ? ",
"answer": "$Arg(\\underline Z )$ repr\u00e9sente l'argument du nombre complexe $\\underline Z$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "147",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1389-1643",
"position": 2,
"duration": 30,
"question": {
"id": "1643",
"question": "Exprimer la puissance r\u00e9active consomm\u00e9e par une inductance $L$ \u00e0 une pulsation $\\omega$ lorsqu'elle est soumise \u00e0 une tension efficace $U$ et parcourue par un courant efficace $I$.",
"answer": "$Q_L=L\\omega.I^2$\nCette puissance est positive, elle est donc consomm\u00e9e par L.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1389-1639",
"position": 3,
"duration": 30,
"question": {
"id": "1639",
"question": "D'apr\u00e8s le th\u00e9or\u00e8me de Boucherot, dans une installation \u00e9lectrique, pour quelle raison peut-on ajouter alg\u00e9briquement les puissances actives entre elles, les puissances r\u00e9actives entre elle et pas les puissances apparentes entrs elles ? ",
"answer": "la repr\u00e9sentation vectorielle des puissances montrent que les puissances actives sont colin\u00e9aires, il est donc possible de sommer leurs normes. Idem pour les puissances r\u00e9actives. En revanche, les puissances apparentes ne sont pas colin\u00e9aires, on ne peut donc pas sommer leurs normes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-1640",
"position": 4,
"duration": 30,
"question": {
"id": "1640",
"question": "1. Exprimer la puissance instantan\u00e9e $p(t)$ pour le dip\u00f4le ci-contre.\n2. Exprimer l'\u00e9nergie consomm\u00e9e par ce dip\u00f4le sur l'intervalle de temps $[t_0,t_1]$.\n3. Quel est l'autre nom de la puissance active ?\n4. En supposant que $u(t)$ et $i(t)$ soient des fonctions T-p\u00e9riodiques, exprimer la puissance active de ce dip\u00f4le.",
"answer": "1. $p(t)=u(t).i(t)$\n\n\n2. $\\omega=\\int_{t_0}^{t_1}p(t)dt$\n\n\n3. c'est la valeur moyenne de la puissance instantan\u00e9e not\u00e9 $<p(t)>$ ou encore la puissance moyenne P.\n\n\n4. $P=<p(t)>=\\frac{1}{T}\\int_{t_0}^{t_0+T}p(t)dt$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/7bb8cb40-e16f-11e7-9719-e5e45427492c",
"image_answer_url": "",
"field_id": "11",
"course_id": "21",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1389-658",
"position": 5,
"duration": 30,
"question": {
"id": "658",
"question": "Question 6 :\nPour un circuit $R C$ parall\u00e8le sous une tension $U = 230V$ de fr\u00e9quence $f = 50Hz$  avec $R = 5 \\Omega$ et $C= 200\u00b5F$ :\n- Exprimer et calculer le courant $I_1$ dans $R$ puis $I_2$ dans $C$ sous forme complexe\n- Exprimer et d\u00e9terminer la puissance active $P$ et r\u00e9active $Q$ pour ce circuit\n- Exprimer et d\u00e9terminer la puissance apparente $S$ puis le courant $I_{total}$ et le facteur de puissance global $F_p$",
"answer": "R\u00e9ponse 6 :\n$I_1 = \\frac{U}{R} = \\frac{230}{5}= 46A$ purement actif d\u00e9phasage nul\n$I_2 = \\frac{U}{jC\\omega}= U.j C\\omega$ en avance de $\\pi\/2$ sur $U$ et de valeur $I_2 = 230.200.10^{-6}.2.\\pi.50 = 14,44 A$\n\n$P$ dans $R$ : $P = R.I_1^2 = 5 .46^2 = 10580W$ et $Q$ dans $C$ : $Q = I_2^2.(-\\frac{1}{C\\omega}) = 14,44\u00b2 . \\frac{1}{200 .10^{-6} .2.\\pi.50} = 3320VAR$\n\nde $S^2 = P^2 + Q^2= 10580^2 + 3320^2$ on d\u00e9duit $S = 11090 VA$\nde $S = U.I_{total}$ on d\u00e9duit $I_{total} = \\frac{11090}{230} = 48,2A$\nOn peut aussi remarquer que $I_{total}^2 = I_1^2 + I_2^2$ car les 2 courants sont en quadrature (d\u00e9phas\u00e9s de $\\frac{\\pi}{2}$ entre eux)\nOn trouve alors le m\u00eame r\u00e9sultat $I_{total} = 48,2 A$\nFacteur de puissance $F_p =\\frac{P}{S} =\\frac{10580}{11090 } = 0,95$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1389-654",
"position": 6,
"duration": 30,
"question": {
"id": "654",
"question": "Question 2 :\nExprimer l'imp\u00e9dance d'une inductance $L$ sous une pulsation $\\omega$",
"answer": "R\u00e9ponse 2 :\n$Z_L = jL\\omega$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1389-657",
"position": 7,
"duration": 30,
"question": {
"id": "657",
"question": "Question 5 :\nExprimer puis d\u00e9terminer num\u00e9riquement la puissance active $P$ et la puissance r\u00e9active $Q$ dans une inductance $L = 10\u00b5H$ parcourue par un courant $I = 10A$ \u00e0 une fr\u00e9quence $f = 10kHz$",
"answer": "R\u00e9ponse 6 :\n$P = 0 W$ car $Z_L$ est une r\u00e9actance pure \n$Q = L{\\omega}I^2 = L.2.\\pi.f.I^2= 10^{-5} . 2.\\pi.10^{4}.10^{2} = 62,8 VAR $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1389-653",
"position": 8,
"duration": 30,
"question": {
"id": "653",
"question": "Question 1 :\nExprimer l'imp\u00e9dance d'une capacit\u00e9 $C$ sous une pulsation $\\omega$",
"answer": "R\u00e9ponse 1 :\n$Z_c = \\frac{1}{jC \\omega} $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "106",
"level_id": "7",
"difficulty": 1
}
}, {
"id": "1389-2067",
"position": 9,
"duration": 30,
"question": {
"id": "2067",
"question": "Soit trois  imp\u00e9dances $\\underline {Z}_1$, $\\underline {Z}_2$  et $\\underline {Z}_3$. D\u00e9terminer l'imp\u00e9dance \u00e9quivalente $\\underline {Z}_{eq,P}$ pour une association parall\u00e8le des trois  imp\u00e9dances.",
"answer": "$\\frac{1}{\\underline {Z}_{eq,P}}=\\frac{1}{\\underline {Z}_1}+\\frac{1}{\\underline {Z}_2}+\\frac{1}{\\underline {Z}_3}$ \n\n$\\underline {Z}_{eq,P}=\\frac{\\underline {Z}_1 \\cdot \\underline {Z}_2 \\cdot \\underline {Z}_3}{\\underline {Z}_1 \\cdot \\underline {Z}_2 + \\underline {Z}_2 \\cdot \\underline {Z}_3 +\\underline {Z}_1 \\cdot \\underline {Z}_3}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/b38ce900-0f0d-11e8-ba1b-67d513a14ba3",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 3
}
}, {
"id": "1389-2068",
"position": 10,
"duration": 30,
"question": {
"id": "2068",
"question": "Soit deux imp\u00e9dances $\\underline {Z}_1$ et $\\underline {Z}_2$. D\u00e9terminer l'imp\u00e9dance \u00e9quivalente $\\underline {Z}_{eq,P}$ pour une association parall\u00e8le des deux imp\u00e9dances.",
"answer": "$\\frac{1}{\\underline {Z}_{eq,P}}=\\frac{1}{\\underline {Z}_1}+\\frac{1}{\\underline {Z}_2}$ \n  \n$\\underline {Z_{eq,P}}=\\frac{\\underline {Z_1}.\\underline {Z_2}}{\\underline {Z_1}+\\underline {Z_2}}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/113083e0-0f0e-11e8-ab4f-a18c7b328fd3",
"image_answer_url": "",
"field_id": "11",
"course_id": "151",
"level_id": "7",
"difficulty": 3
}
}, {
"id": "1389-2661",
"position": 11,
"duration": 30,
"question": {
"id": "2661",
"question": "Etablir l'expression de la tension aux bornes d'un condensateur de capacit\u00e9 $C$, pr\u00e9alablement charg\u00e9 \u00e0 la tension $E$ lors de sa d\u00e9charge dans une r\u00e9sistance $R$.",
"answer": "On appelle $i$ le courant traversant le circuit, $u$ la tension aux bornes du condensateur recherch\u00e9e (en convention g\u00e9n\u00e9rateur), $u_R$ la tension aux bornes de la r\u00e9sistance.\nOn applique alors les lois \u00e0 notre disposition :\n- loi des mailles $u = u_R$ ;\n- loi d'Ohm $u_R = R i$ ;\n- caract\u00e9ristique du condensateur $i = - C\\frac{du}{dt}$\n\nEn combinant ces trois \u00e9quations on trouve l'\u00e9quation diff\u00e9rentielle suivie par $u$ :\n$$ u + RC \\frac{du}{dt} = 0 $$\nque l'on r\u00e9\u00e9crit sous forme canonique en posant $\\tau = RC$ :\n$$ \\frac{du}{dt} + \\frac{u}{\\tau} = 0$$\nOn peut donc r\u00e9soudre, et on trouve comme solution g\u00e9n\u00e9rale :\n$$ u(t) = \\lambda e^{-t\/\\tau} $$\n\nLa condition initiale $u(t=0) = E$, d\u00e9termin\u00e9e gr\u00e2ce \u00e0 la continuit\u00e9 de la tension aux bornes du condensateur, fixe $\\lambda = E$ et on trouve finalement :\n$$ u(t) = E  e^{-t\/\\tau} .$$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "112",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1389-2696",
"position": 12,
"duration": 30,
"question": {
"id": "2696",
"question": "Quel est l'int\u00e9r\u00eat de l'\u00e9tude des signaux sinuso\u00efdaux pour l'\u00e9tude des signaux p\u00e9riodiques ?",
"answer": "On peut d\u00e9composer tout signal p\u00e9riodique comme une somme de signaux sinuso\u00efdaux.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-2578",
"position": 13,
"duration": 30,
"question": {
"id": "2578",
"question": "Donner la valeur de la fr\u00e9quence, de l'amplitude et de la phase initiale du signal suivant.",
"answer": "L'amplitude est de 3 A ; la fr\u00e9quence est de 0,4 Hz et la phase initiale vaut $- \\pi\/2$.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/63eca450-96e5-11e8-9bff-91800420ea59",
"image_answer_url": "",
"field_id": "23",
"course_id": "115",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-3788",
"position": 14,
"duration": 30,
"question": {
"id": "3788",
"question": "Quelle est l'imp\u00e9dance complexe $\\underline {Z_L}$ d'une inductance pour une pulsation $\\omega$ ? Exprimer cette imp\u00e9dance sous forme exponentielle.",
"answer": "$\\underline {Z}_L=L \\cdot \\omega  \\cdot {e^j}^\\frac{\\pi}{2}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "129",
"course_id": "438",
"level_id": "28",
"difficulty": 2
}
}, {
"id": "1389-3787",
"position": 15,
"duration": 30,
"question": {
"id": "3787",
"question": "Quelle est l'imp\u00e9dance complexe $\\underline {Z_c}$ d'un condensateur pour une pulsation $\\omega$ ? Exprimer cette imp\u00e9dance sous forme exponentielle.",
"answer": "$$\\underline {Z_c}=\\frac{1}{C\u00b7\\omega} \u00b7 {{e^-}^j}^\\frac{\\pi}{2}$$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "129",
"course_id": "438",
"level_id": "28",
"difficulty": 1
}
}, {
"id": "1389-452",
"position": 16,
"duration": 30,
"question": {
"id": "452",
"question": "Donner l'\u00e9criture alg\u00e9brique de $z=\\frac{1}{2+3i}$",
"answer": " $z=\\frac{1}{2+3i}= \\frac{2-3i}{(2+3i)(2-3i)}= \\frac{2-3i}{13}=\\frac{2}{13}- \\frac{3}{13}i$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1389-453",
"position": 17,
"duration": 30,
"question": {
"id": "453",
"question": "Donner l'\u00e9criture alg\u00e9brique de $z=\\frac{1-i}{1+i}$",
"answer": "$z=\\frac{1-i}{1+i}=\\frac{(1-i)^2}{(1+i)(1-i)}=\\frac{1-2i+1}{1-i^2}=\\frac{2-2i}{2}=1-i$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1389-2908",
"position": 18,
"duration": 30,
"question": {
"id": "2908",
"question": "Vrai ou faux ? (corriger si faux)\n\\[|z_1||z_2|=|z_1z_2|\\]",
"answer": "Vrai",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-2915",
"position": 19,
"duration": 30,
"question": {
"id": "2915",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $\\overline{z}$.",
"answer": "Sym\u00e9trique du point d'affixe $z$ par rapport \u00e0 l'axe r\u00e9el (axe des abscisses).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-2910",
"position": 20,
"duration": 30,
"question": {
"id": "2910",
"question": "Vrai ou faux ? (corriger si faux)\n\\[\\left|\\frac{z_1}{z_2}\\right|=\\frac{|z_1|}{|z_2|}\\]",
"answer": "Vrai",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-2961",
"position": 21,
"duration": 30,
"question": {
"id": "2961",
"question": "\\[\\arg(-z)=\\,?\\]",
"answer": "$\\pi+\\arg(z)  \\hspace{1cm}$  (\u00e0 un multiple de $2\\pi$ pr\u00e8s)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1389-2965",
"position": 22,
"duration": 30,
"question": {
"id": "2965",
"question": "D\u00e9finition de $e^z$.",
"answer": "\\[e^z=e^x\\times e^{iy}=e^x(\\cos y+i\\sin y)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1391": {
"id": "1391",
"name": "Matrices",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1391\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 270,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-18",
"questions": [{
"id": "1391-5397",
"position": 0,
"duration": 30,
"question": {
"id": "5397",
"question": "Soit $A$ une matrice de taille $3 \\times 4$. A quelle condition sur la taille de $B$ le produit $A \\times B$ est-il possible ?",
"answer": "Si B a 4 lignes. B doit \u00eatre de taille $4 \\times n$ o\u00f9 $n \\in \\mathbb{N}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5398",
"position": 1,
"duration": 30,
"question": {
"id": "5398",
"question": "Soit $A$ une matrice de taille $3\\times 4$. A quelle condition sur la taille de $B$ le produit $B \\times A$ est-il possible ?",
"answer": "Si B a 3 colonnes. B doit \u00eatre de taille $m \\times 3$ o\u00f9 $m \\in \\mathbb{N}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5399",
"position": 2,
"duration": 30,
"question": {
"id": "5399",
"question": "Dans l'op\u00e9ration matricielle $A \\times B = C$, $A$ est une matrice de dimension $3 \\times 2$ et $C$ une matrice de dimension $3 \\times 4$ . Quelle est la dimension de $B$ ?",
"answer": "$2 \\times 4$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5400",
"position": 3,
"duration": 30,
"question": {
"id": "5400",
"question": "Quand une matrice carr\u00e9e $A \\in \\mathcal{M}_n(\\mathbb{R})$ est-elle inversible ? ",
"answer": "S'il existe une matrice $B \\in \\mathcal{M}_n(\\mathbb{R})$ telle que $AB=BA=I_n$.\n(Notons que l'une des \u00e9galit\u00e9s $AB=I_n$ ou $BA=I_n$ suffit.)\nOn peut aussi dire que A est inversible si A est de rang $n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5401",
"position": 4,
"duration": 30,
"question": {
"id": "5401",
"question": "Citer la formule du bin\u00f4me de Newton pour d\u00e9velopper $(A+B)^n$ lorsque A et B sont des matrices carr\u00e9es d'ordre $n$.",
"answer": "D'abord, il est n\u00e9cessaire que AB=BA, sinon point de formule !\nDans ce cas, $(A+B)^n=\\displaystyle{\\sum_{k=0}^n \\binom{n}{k}A^k B^{n-k} }$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5402",
"position": 5,
"duration": 30,
"question": {
"id": "5402",
"question": "Soit A une matrice carr\u00e9e d'ordre n telle que $A^2+4A=I_n$. Que vaut $A^{-1}$ ?",
"answer": "$A^{-1}=A+4I_n \\quad$  car  $\\quad A^2+4A=A(A+4I_n)=I_n$ ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5877",
"position": 6,
"duration": 30,
"question": {
"id": "5877",
"question": "Soient $A$, $B$, $P$ des matrices carr\u00e9es d'ordre $n$, telles que $B=P^{-1}AP$. Alors $A= ...$",
"answer": "$PBP^{-1}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5878",
"position": 7,
"duration": 30,
"question": {
"id": "5878",
"question": "Soient A et B deux matrices carr\u00e9es d'ordre $n$, inversibles.\n Vrai ou faux : $(AB)^{-1}=A^{-1}B^{-1} ?$",
"answer": "Faux en g\u00e9n\u00e9ral. \nEn revanche, on a toujours  $(AB)^{-1}=B^{-1}A^{-1}$. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1391-5910",
"position": 8,
"duration": 30,
"question": {
"id": "5910",
"question": "On effectue le calcul $A \\times B=C$ o\u00f9 $A$, $B$ et $C$ sont toutes des matrices de taille $3 \\times 3$. Comment se calcule le coefficient $c_{2,3}$ de la matrice C ?",
"answer": "$c_{2,3}=\\displaystyle{\\sum_{k=1}^3 a_{2,k}b_{k,3}}$.\n$\\textit{on multiplie la ligne 2 de A par la colonne 3 de B}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1393": {
"id": "1393",
"name": "DC7 chaine info",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1393\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "17",
"value": "Capteurs",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "25",
"value": "Num\u00e9rique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "406",
"value": "Analogique",
"field_id": "11",
"created_at": "2018-02-04 15:16:07",
"updated_at": "2018-02-04 15:16:07",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 600,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2025-05-03",
"questions": [{
"id": "1393-2244",
"position": 0,
"duration": 30,
"question": {
"id": "2244",
"question": "A quelles conditions pourra-ton consid\u00e9rer que le r\u00e9gime de fonctionnement d'un ALI  dans un circuit est non lin\u00e9aire ?",
"answer": "S'il n'y a pas de contre r\u00e9action n\u00e9gative.\nS'il y a une contre r\u00e9action positive.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1393-2245",
"position": 1,
"duration": 30,
"question": {
"id": "2245",
"question": "Que peut valoir la tension de sortie de l'ALI qui fonctionne en r\u00e9gime non lin\u00e9aire ?",
"answer": "La tension de sortie vaut +Vsat ou -Vsat",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1393-1960",
"position": 2,
"duration": 30,
"question": {
"id": "1960",
"question": "Exprimer la relation ${V_s}=f({V_{e1}}, {V_{e2}})$ par superposition",
"answer": "${V_s}=({\\frac{V_s}{V_{e_1}}})_{V_{e_2}=0}+({\\frac{V_s}{V_{e_2}}})_{V_{e_1}=0}$\n\n${V_s}=-(\\frac{R}{R_1})\u00b7V_{e1}-(\\frac{R}{R_2})\u00b7V_{e2}$\nMontage \"sommateur inverseur\"",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/a0f93820-09be-11e8-9209-a17493659482",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1393-2258",
"position": 3,
"duration": 30,
"question": {
"id": "2258",
"question": "Tracer la caract\u00e9ristique $V_s=f(V_e)$.",
"answer": "absence de liaison entre la sortie et l'entr\u00e9e -, alors r\u00e9gime non lin\u00e9aire\nsi $\\epsilon >0$ alors $V_s=+V_{sat}$\nsi $\\epsilon <0$ alors $V_s=-V_{sat}$\n\n\u00e9tude du signe de $\\epsilon$\n$V^+=V_e$\n$V^-=e$\n$\\epsilon =V^+-V^-=V_e-e$\n$V_s=+V_{sat}$ vrai tant que $\\epsilon >0$ soit $V_e-e >0$soit $V_e>e$\n$V_s=-V_{sat}$ vrai tant que $\\epsilon <0$ soit $V_e-e <0$ soit $V_e<e$\n\n$V_s=+V_{sat}$ vrai tant que $V_e>e$\n$V_s=-V_{sat}$ vrai tant que  $V_e<e$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/aa982000-241d-11e8-8543-9dbe98f57dd7",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/854dd4a0-241d-11e8-af14-d3ed40ad0207",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1393-2051",
"position": 4,
"duration": 30,
"question": {
"id": "2051",
"question": "A quelle condition pourra-t-on conclure que le circuit qui comporte un amplificateur lin\u00e9aire int\u00e9gr\u00e9 fonctionne en r\u00e9gime lin\u00e9aire ? quelle est l'incidence de ce r\u00e9gime de fonctionnement ?",
"answer": "L'ALI fonctionne en r\u00e9gime lin\u00e9aire \u00e0 condition d'observer une r\u00e9action n\u00e9gative.\nOn consid\u00e9rera  alors que $V^+=V^-$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2077",
"position": 5,
"duration": 30,
"question": {
"id": "2077",
"question": "Exprimer la relation $\\frac{V_s}{V_e}$",
"answer": "sortie r\u00e9tro-actionn\u00e9e sur entr\u00e9e - alors r\u00e9gime de fonctionnement lin\u00e9aire\nsi le r\u00e9gime de fonctionnement de l'ALI est  lin\u00e9aire, $V^+=V^-$\n$V^+=0$\nCalcul de $V^-$ : \nEn appliquant la loi de courant sur l'entr\u00e9e -\n$\\frac{V_e-V^{-}}{R_1} + \\frac{V_{S}-V^{-}}{R_2}+0=0$\non obtient $\\frac{V_s}{V_e}=-\\frac{R_2}{R_1}$\nMontage amplificateur inverseur\n",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/781da980-0f14-11e8-b85c-594cc4d6ea64",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2266",
"position": 6,
"duration": 30,
"question": {
"id": "2266",
"question": "Citer deux technologies utilis\u00e9es dans les capteurs de vitesse.",
"answer": " - dynamo tachym\u00e9trique (capteur analogique - conversion vitesse angulaire\/tension),\n- codeur incr\u00e9mental (mesure de la fr\u00e9quence des impulsions).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2256",
"position": 7,
"duration": 30,
"question": {
"id": "2256",
"question": "A quelles conditions pourra-ton consid\u00e9rer que le r\u00e9gime de fonctionnement d'un ALI  dans un circuit est non lin\u00e9aire ?",
"answer": " le r\u00e9gime de fonctionnement d'un ALI  dans un circuit est non lin\u00e9aire si la sortie n'est pas reli\u00e9e sur l'entr\u00e9e -.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1393-2267",
"position": 8,
"duration": 30,
"question": {
"id": "2267",
"question": "Calculer le quantum d'un CAN 8 bits avec une plage de tension d'entr\u00e9e  $V_e $ de 10 Volts.",
"answer": "$q=\\frac{V_e}{2^8-1}=\\frac{10}{255}=0,0392=39,2 \\; mV$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-1885",
"position": 9,
"duration": 30,
"question": {
"id": "1885",
"question": "1. D\u00e9terminer l'expression de $V_S=f(V_E, R_1, R_2)$.\n2. On souhaite obtenir une amplification $A=\\frac{V_S}{V_E}=-5$, sachant que $R_2=10 k\\Omega$, calculer la valeur de $R_1$.\n3. La fonction $V_E(t)$ est repr\u00e9sent\u00e9e en bleu sur l'oscillogramme. En d\u00e9duire l'allure de $V_S(t)$ sur la voie 2.\n",
"answer": "1. $\\frac{V_S}{V_E}=- \\frac{R_2}{R_1}$\n2. $A=\\frac{V_S}{V_E}=-5=- \\frac{R_2}{R_1}=> R_1=\\frac{R_2}{5}=2k\\Omega$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e553eae0-03fc-11e8-9a2b-d397f782d313",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/47859a10-03ff-11e8-a353-6f61ebfb74ba",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-112",
"position": 10,
"duration": 30,
"question": {
"id": "112",
"question": "Citer deux technologies utilis\u00e9es dans les capteurs d'effort.",
"answer": "Piezo\u00e9lectricit\u00e9\njauges de contrainte",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 0
}
}, {
"id": "1393-113",
"position": 11,
"duration": 30,
"question": {
"id": "113",
"question": "Citer 4 technologies utilis\u00e9es dans les capteurs de temp\u00e9rature.",
"answer": "Thermistance\nThermocouple\nPT100\nThermographie infra-rouge",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 0
}
}, {
"id": "1393-115",
"position": 12,
"duration": 30,
"question": {
"id": "115",
"question": "D\u00e9crire la structure fonctionnelle d'un capteur",
"answer": "\u00a0",
"image_question_url": "",
"image_answer_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/5557afb7-992b-4585-88c4-aa1f5ee795b1",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1393-114",
"position": 13,
"duration": 30,
"question": {
"id": "114",
"question": "Quelle est la valeur num\u00e9rique (en binaire) de la position 45\u00b0 d'un codeur absolu binaire sur 10 bits ?",
"answer": "0010000000",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 0
}
}, {
"id": "1393-2081",
"position": 14,
"duration": 30,
"question": {
"id": "2081",
"question": "Quelle est la nature (incr\u00e9mental ou absolu) de ce codeur ?",
"answer": "Codeur absolu (en code Gray)",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0d0e0440-0f22-11e8-ab21-17f106eedc7c",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2080",
"position": 15,
"duration": 30,
"question": {
"id": "2080",
"question": "Quelle est la nature (incr\u00e9mental ou absolu) de ce codeur ?",
"answer": "codeur incr\u00e9mental",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/fafe0790-0f21-11e8-affc-4d9d6c857bfa",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2054",
"position": 16,
"duration": 30,
"question": {
"id": "2054",
"question": "Dans une cha\u00eene d'acquisition, quelle est la fonction assur\u00e9e par un transducteur ?",
"answer": "Un transducteur transforme la grandeur physique mesurable en un signal image exploitable.\nexemple : Capteur de force, un jauge de contrainte va transformer la d\u00e9formation du corps d'\u00e9preuve en une variation de r\u00e9sistance \u00e9lectrique.\n",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9dff1c00-0e8d-11e8-8d5e-bbb0718fdec6",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1393-2055",
"position": 17,
"duration": 30,
"question": {
"id": "2055",
"question": "Dans une cha\u00eene d'acquisition, quelle est la fonction assur\u00e9e par le corps d'\u00e9preuve ?",
"answer": "Le corps d'\u00e9preuve  a pour fonction de d\u00e9tecter la grandeur physique que l'on souhaite mesurer.\nexemple : Capteur de force : La force \u00e0 mesurer va d\u00e9former le corps d'\u00e9preuve.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/528a3390-0e8d-11e8-b5e8-f1d9cf4ecc22",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1393-768",
"position": 18,
"duration": 30,
"question": {
"id": "768",
"question": "Quelle est la valeur d\u00e9cimale cod\u00e9e par $9A_{(hex)}$  dans un registre 8 Bits sign\u00e9 (1 bit de signe -MSB- et 7 bit pour la valeur absolue)?",
"answer": "$9A_{(hex)}={1001 1010}_{(2)} = {-26}_{(dec)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "25",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1393-764",
"position": 19,
"duration": 30,
"question": {
"id": "764",
"question": "Quelle est la valeur d\u00e9cimale cod\u00e9e par $4C_{(hex)}$  dans un registre 8 bits non sign\u00e9 ?",
"answer": "$4C_{(hex)}={0100 1100}_{(2)} = {76}_{(dec)}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "25",
"level_id": "6",
"difficulty": 4
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1394": {
"id": "1394",
"name": "DC7 quizz 2",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1394\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "17",
"value": "Capteurs",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "406",
"value": "Analogique",
"field_id": "11",
"created_at": "2018-02-04 15:16:07",
"updated_at": "2018-02-04 15:16:07",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 5,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-05-12",
"questions": [{
"id": "1394-2244",
"position": 0,
"duration": 30,
"question": {
"id": "2244",
"question": "A quelles conditions pourra-ton consid\u00e9rer que le r\u00e9gime de fonctionnement d'un ALI  dans un circuit est non lin\u00e9aire ?",
"answer": "S'il n'y a pas de contre r\u00e9action n\u00e9gative.\nS'il y a une contre r\u00e9action positive.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-2255",
"position": 1,
"duration": 30,
"question": {
"id": "2255",
"question": "Exprimer la relation ${V_s}=f({V_{e1}}, {V_{e2}})$ par la loi de courant,",
"answer": "sortie r\u00e9tro-actionn\u00e9e sur entr\u00e9e - alors r\u00e9gime de fonctionnement lin\u00e9aire\nsi le r\u00e9gime de fonctionnement de l'ALI est  lin\u00e9aire, $V^+=V^-$\n$V^+=0$\nCalcul de $V^-$ : En appliquant la loi de courant sur l'entr\u00e9e -\n$\\frac{V_{e1}-V^{-}}{R_1} + \\frac{V_{e2}-V^{-}}{R_2} +\\frac{V_{S}-V^{-}}{R}+i^-=0$\n$\\frac{V_{e1}}{R_1} + \\frac{V_{e2}}{R_2} +\\frac{V_{S}}{R}+0=0$\n${R \\cdot R_2} \\cdot  {V_{e1}} + {R  \\cdot R_1} \\cdot  {V_{e2}}+{  R_1  \\cdot R_2 } \\cdot  {V_{S}}=0$\n${  R_1  \\cdot R_2 } \\cdot  {V_{S}}=-{R \\cdot R_2} \\cdot  {V_{e1}} - {R  \\cdot R_1} \\cdot  {V_{e2}}$\n\non obtient  ${V_{S}}=- \\frac {R}{R_1}  \\cdot   {V_{e1}} - \\frac {R }{R_2} \\cdot  {V_{e2}}$\n\nMontage amplificateur sommateur inverseur",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/79be4b50-2411-11e8-bc4a-f997edb1f2f0",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1394-2245",
"position": 2,
"duration": 30,
"question": {
"id": "2245",
"question": "Que peut valoir la tension de sortie de l'ALI qui fonctionne en r\u00e9gime non lin\u00e9aire ?",
"answer": "La tension de sortie vaut +Vsat ou -Vsat",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-2246",
"position": 3,
"duration": 30,
"question": {
"id": "2246",
"question": "A quelle condition la tension de sortie d'un ALI fonctionnant en r\u00e9gime non lin\u00e9aire peut valoir +Vsat ?",
"answer": "Si $\\epsilon > 0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-2247",
"position": 4,
"duration": 30,
"question": {
"id": "2247",
"question": "Tracer la caract\u00e9ristique $V_s=f(V_e)$.",
"answer": "R\u00e9ponse...",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c1f03480-237e-11e8-8442-7ffd2577117e",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/abec7670-237e-11e8-916a-d77372213076",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1394-2259",
"position": 5,
"duration": 30,
"question": {
"id": "2259",
"question": "Tracer la caract\u00e9ristique $V_s=f(V_e)$.",
"answer": "absence de liaison entre la sortie et l'entr\u00e9e -, alors r\u00e9gime non lin\u00e9aire\nsi $\\epsilon >0$ alors $V_s=+V_{sat}$\nsi $\\epsilon <0$ alors $V_s=-V_{sat}$\n\n\u00e9tude du signe de $\\epsilon$\n$V^-=V_e$\n$V^+=e$\n$\\epsilon =V^+-V^-=e-V_e$\n$V_s=+V_{sat}$ vrai tant que $\\epsilon >0$ soit $e-V_e >0$soit $V_e<e$\n$V_s=-V_{sat}$ vrai tant que $\\epsilon <0$ soit $e-V_e <0$ soit $V_e>e$\n\n$V_s=+V_{sat}$ vrai tant que $V_e<e$\n$V_s=-V_{sat}$ vrai tant que  $V_e>e$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ca191510-241d-11e8-8582-53bcaa8a981e",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d39b5300-241d-11e8-8f1f-39e643800f45",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1394-1962",
"position": 6,
"duration": 30,
"question": {
"id": "1962",
"question": "rappeler les hypoth\u00e8ses d'un ALI id\u00e9al.",
"answer": "\u2022 une imp\u00e9dance d'entr\u00e9e infinie donc des courants d'entr\u00e9e (i+ et i-) nuls,\n\u2022 une imp\u00e9dance de sortie nulle,\n\u2022 un gain diff\u00e9rentiel  infini, donc en fonctionnement lin\u00e9aire \u03b5 = v+ - v- = 0\n\u2022 une tension de sortie nulle en l'absence de signal d'entr\u00e9e,\n",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f5413f40-09be-11e8-a3cf-8fefb2c031dd",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-2260",
"position": 7,
"duration": 30,
"question": {
"id": "2260",
"question": "Tracer la caract\u00e9ristique $V_s=f(V_e)$.",
"answer": "absence de liaison entre la sortie et l'entr\u00e9e -, alors r\u00e9gime non lin\u00e9aire\nsi $\\epsilon >0$ alors $V_s=+V_{sat}$\nsi $\\epsilon <0$ alors $V_s=-V_{sat}$\n\n\u00e9tude du signe de $\\epsilon$\n$V^-=V_e$\ncalcul de $V^+$\n$V_+$ s'exprime par un pont diviseur de $V_s$\n$V_+=\\frac{R_1}{R_1+R_2} \\cdot V_s $\n\n$\\epsilon =V^+-V^-=\\frac{R_1}{R_1+R_2} \\cdot V_s-V_e$\n$V_s=+V_{sat}$ vrai tant que $\\epsilon >0$ soit $\\frac{R_1}{R_1+R_2} \\cdot V_{sat}-V_e >0$soit $V_e<\\frac{R_1}{R_1+R_2} \\cdot V_{sat}$\navec $\\beta = \\frac{R_1}{R_1+R_2} $\n$V_s=+V_{sat}$ vrai tant que $V_e<\\beta \\cdot V_{sat}$\n\n$V_s=-V_{sat}$ vrai tant que $\\epsilon <0$ soit $\\frac{R_1}{R_1+R_2} \\cdot (-V_{sat})-V_e <0$ soit $V_e>\\frac{R_1}{R_1+R_2} \\cdot V_{sat}$\n\n$V_s=+V_{sat}$ vrai tant que $V_e<\\beta \\cdot V_{sat}$\n$V_s=-V_{sat}$ vrai tant que  $V_e>-\\beta \\cdot V_{sat}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/3d690fc0-2421-11e8-af91-8f510218110e",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/cf36c900-2422-11e8-86fe-7914b61d23db",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 5
}
}, {
"id": "1394-2051",
"position": 8,
"duration": 30,
"question": {
"id": "2051",
"question": "A quelle condition pourra-t-on conclure que le circuit qui comporte un amplificateur lin\u00e9aire int\u00e9gr\u00e9 fonctionne en r\u00e9gime lin\u00e9aire ? quelle est l'incidence de ce r\u00e9gime de fonctionnement ?",
"answer": "L'ALI fonctionne en r\u00e9gime lin\u00e9aire \u00e0 condition d'observer une r\u00e9action n\u00e9gative.\nOn consid\u00e9rera  alors que $V^+=V^-$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1394-2075",
"position": 9,
"duration": 30,
"question": {
"id": "2075",
"question": "D\u00e9terminer l'expression $V_S=f(V_{e1}, V_{e2}, V_{e3}, R_1, R_2, R_3, R_4)$.\nQuel est le nom donn\u00e9 \u00e0 ce montage ALI ?",
"answer": "En appliquant la loi de courant sur l'entr\u00e9e -\n$\\frac{V_{e1}-V_{-}}{R_1} + \\frac{V_{e2}-V_{-}}{R_2} + \\frac{V_{e3}-V_{-}}{R_3} + \\frac{V_{s}-V_{-}}{R_4} =0$\non obtient \n$V_S=-R_4(\\frac{V_{e1}}{R_1}+\\frac{V_{e2}}{R_2}+\\frac{V_{e3}}{R_3})$\nLe montage est un sommateur inverseur.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9dfcf780-0f27-11e8-8f14-af9b135f62a0",
"image_answer_url": "",
"field_id": "11",
"course_id": "406",
"level_id": "6",
"difficulty": 5
}
}, {
"id": "1394-1883",
"position": 10,
"duration": 30,
"question": {
"id": "1883",
"question": "Dans un circuit, si l'on suppose que l'amplificateur lin\u00e9aire int\u00e9gr\u00e9 est id\u00e9al, quelle est la cons\u00e9quence sur les courants $i^+$ et $ i^-$ ? pourquoi?",
"answer": "$i^+ = i^- = 0$ car les imp\u00e9dances des bornes d'entr\u00e9e sont consid\u00e9r\u00e9s comme infinies.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5a727280-03fc-11e8-ace2-370f22c2cc4c",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-1884",
"position": 11,
"duration": 30,
"question": {
"id": "1884",
"question": "A quelle condition pourra t'on conclure que le circuit qui comporte un amplificateur lin\u00e9aire int\u00e9gr\u00e9 fonctionne en r\u00e9gime lin\u00e9aire ? quelle est l'incidence de ce r\u00e9gime de fonctionnement ?",
"answer": "A condition d'observer une contre r\u00e9action n\u00e9gative.\nOn consid\u00e9rera que $\\epsilon=0$ donc que $V^+=V^-$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/650e6440-03fc-11e8-bc76-bbe4f36d910f",
"image_answer_url": "",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1394-1885",
"position": 12,
"duration": 30,
"question": {
"id": "1885",
"question": "1. D\u00e9terminer l'expression de $V_S=f(V_E, R_1, R_2)$.\n2. On souhaite obtenir une amplification $A=\\frac{V_S}{V_E}=-5$, sachant que $R_2=10 k\\Omega$, calculer la valeur de $R_1$.\n3. La fonction $V_E(t)$ est repr\u00e9sent\u00e9e en bleu sur l'oscillogramme. En d\u00e9duire l'allure de $V_S(t)$ sur la voie 2.\n",
"answer": "1. $\\frac{V_S}{V_E}=- \\frac{R_2}{R_1}$\n2. $A=\\frac{V_S}{V_E}=-5=- \\frac{R_2}{R_1}=> R_1=\\frac{R_2}{5}=2k\\Omega$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e553eae0-03fc-11e8-9a2b-d397f782d313",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/47859a10-03ff-11e8-a353-6f61ebfb74ba",
"field_id": "11",
"course_id": "17",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1398": {
"id": "1398",
"name": "Espaces vectoriels",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1398\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "53",
"value": "Alg\u00e8bre",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 420,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-04-08",
"questions": [{
"id": "1398-3165",
"position": 0,
"duration": 30,
"question": {
"id": "3165",
"question": "D\u00e9finition de la somme de deux sous-espaces vectoriels.",
"answer": "$F+G=\\{u+v\\mid u\\in F,\\ v\\in G\\}$.\n\nC'est le plus petit sous-espace vectoriel contenant $F\\cup G$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3163",
"position": 1,
"duration": 30,
"question": {
"id": "3163",
"question": "D\u00e9finition d'un sous-espace vectoriel de E.",
"answer": "C'est une partie $F$ d'un $\\mathbf{R}$-espace vectoriel $E$ telle que :\n-- $0_E\\in F$;\n-- pour tous $u,v\\in F$ et pour tout $\\lambda \\in\\mathbf{R}$, $\\lambda u + v\\in F$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3166",
"position": 2,
"duration": 30,
"question": {
"id": "3166",
"question": "D\u00e9finition et caract\u00e9risation de deux sous-espaces vectoriels en somme directe.",
"answer": "D\u00e9finition : Les espaces $F$ et $G$ sont en somme directe si, pour tout $w\\in F+G$, il existe un unique couple $(f,g)\\in F\\times G$ tel que $w=f+g$.\n\nCaract\u00e9risation : $F$ et $G$ sont en somme directe si et seulement si $F\\cap G =\\{0\\}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3167",
"position": 3,
"duration": 30,
"question": {
"id": "3167",
"question": "D\u00e9finition de deux sous-espaces vectoriels suppl\u00e9mentaires.",
"answer": "$F$ et $G$ sont suppl\u00e9mentaires dans $E$ si $F\\oplus G= E$. Autrement dit, si $F$ et $G$ sont en somme directe et $F+G=E$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-5708",
"position": 4,
"duration": 30,
"question": {
"id": "5708",
"question": "Soit F un sev de E (en dimension finie). Comment construire un suppl\u00e9mentaire de F dans E ?",
"answer": "On compl\u00e8te une base de F en une base de E (th\u00e9or\u00e8me de la base incompl\u00e8te). L'espace engendr\u00e9 par les vecteurs ajout\u00e9s \u00e0 la base de F est un suppl\u00e9mentaire de F dans E.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-5709",
"position": 5,
"duration": 30,
"question": {
"id": "5709",
"question": "Soit F un sev de E : on a $F \\subset E$. Comment montrer que F=E ?",
"answer": "Soit on montre l'inclusion inverse , \u00e0 savoir $E \\subset F$\nSoit on prouve que $\\dim F=\\dim E$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3171",
"position": 6,
"duration": 30,
"question": {
"id": "3171",
"question": "D\u00e9finition d'une base d'un espace vectoriel $E$.",
"answer": "C'est une famille libre et g\u00e9n\u00e9ratrice de $E$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3168",
"position": 7,
"duration": 30,
"question": {
"id": "3168",
"question": "D\u00e9finition de l'espace vectoriel engendr\u00e9 par une famille de vecteurs.",
"answer": "$\\mathrm{Vect}(u_1,\\dots,u_n)=\\{\\lambda_1u_1+\\cdots+\\lambda_nu_n,\\quad \\lambda_1,\\dots,\\lambda_n\\in\\mathbf{R}\\}$.\n\nC'est le plus petit sous-espace vectoriel contenant les vecteurs $u_1,\\dots,u_n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-5380",
"position": 8,
"duration": 30,
"question": {
"id": "5380",
"question": "D\u00e9finition d'une famille libre d'un espace vectoriel E",
"answer": " $(\\vec{v_1}, \\vec{v_2},...,\\vec{v_p})$ est libre si :\n$(\\lambda_1 \\vec{v_1}+\\lambda_2 \\vec{v_2}+...+\\lambda_p \\vec{v_p}=\\vec{0})$ impose $(\\lambda_1=\\lambda_2=...=\\lambda_p=0)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3172",
"position": 9,
"duration": 30,
"question": {
"id": "3172",
"question": "Soit $E$ un espace vectoriel. Que dire du cardinal des bases de $E$ ?",
"answer": "Si elles existent (autrement dit, si $E$ est de dimension finie), alors toutes les bases de $E$ ont le m\u00eame cardinal, qui est par d\u00e9finition \u00e9gal \u00e0 la dimension de $E$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3170",
"position": 10,
"duration": 30,
"question": {
"id": "3170",
"question": "Soit $(u_1,\\dots,u_n)$ une famille de vecteurs d'un $\\mathbf{K}$-espace vectoriel $E$. Exprimer de deux fa\u00e7ons diff\u00e9rentes le fait que $(u_1,\\dots,u_n)$ est li\u00e9e.",
"answer": "Il existe $\\lambda_1,\\dots,\\lambda_n\\in\\mathbf{K}$ non tous nuls tels que $\\lambda_1u_1+\\cdots+\\lambda_nu_n=0$.\n\nAlternativement, un des vecteurs $u_k$ s'\u00e9crit comme combinaison lin\u00e9aire des autres.\n\nOn rappelle qu'une famille qui n'est pas li\u00e9e est dite libre.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-3169",
"position": 11,
"duration": 30,
"question": {
"id": "3169",
"question": "D\u00e9finition de $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$ est g\u00e9n\u00e9ratrice de E ?",
"answer": "Tout vecteur $\\vec{X}$ de E peut s'\u00e9crire comme combiniaison lin\u00e9aire des vecteurs $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$, autrement dit il existe $p$ r\u00e9els  $\\lambda_1,\\dots,\\lambda_p$ tels que $\\vec{X}=\\lambda_1 \\vec{u_1}+\\lambda_2 \\vec{u_2}+...+\\lambda_p \\vec{u_p}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-5925",
"position": 12,
"duration": 30,
"question": {
"id": "5925",
"question": "Une famille libre d'un ev E de dimension finie est-elle g\u00e9n\u00e9ratrice de E ?",
"answer": "En g\u00e9n\u00e9ral non ! Mais si le cardinal de la famille libre correspond \u00e0 la dimension de l'espace E, alors dans ce cas la famille constitue une base de E.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1398-5926",
"position": 13,
"duration": 30,
"question": {
"id": "5926",
"question": "Soit $n \\in \\mathbb{N}$. Donner la dimension et la base canonique de $\\mathbb{R}_n[X]$",
"answer": "la base canonique de $\\mathbb{R}_n[X]$ est $(1,X,X^2,...,X^n)$, $\\mathbb{R}_n[X]$ est donc de dimension $n+1$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1399": {
"id": "1399",
"name": "DC7 Quizz1",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1399\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "16",
"value": "Automatique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 360,
"already_tried": "false",
"already_passed": "false",
"best_score": 0,
"shared_at": "2025-05-25",
"questions": [{
"id": "1399-2248",
"position": 0,
"duration": 30,
"question": {
"id": "2248",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)$.\n1. Donner l'expression du gain $G$ en $dB$.\n2. Donner l'expression g\u00e9n\u00e9rale de son argument.",
"answer": "1. $G=20 log(\\vert\\underline T(j\\omega)\\vert)$\n2. $\\phi =Arg (\\underline T(j\\omega))$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-1324",
"position": 1,
"duration": 30,
"question": {
"id": "1324",
"question": "Soit $H(p)$ la fonction de transfert d'un SLCI. Comment calcule-t-on le gain $G(\\omega)$, pour une r\u00e9ponse harmonique de pulsation $\\omega$ ?",
"answer": "\\[G(\\omega) = \\left|H(j\\omega)\\right|\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-2249",
"position": 2,
"duration": 30,
"question": {
"id": "2249",
"question": "Donner les expressions des 4 formes canoniques des fonctions de transfert du 1 er ordre. Pr\u00e9ciser leurs noms.",
"answer": "$\\underline {T_1}(j\\omega)=j\\frac{\\omega}{\\omega_c}$  d\u00e9rivateur\n\n$\\underline {T_2}(j\\omega)=\\frac{1}{\\frac{j\\omega}{\\omega_c}}$  int\u00e9grateur\n\n$\\underline {T_3}(j\\omega)=1+j\\frac{\\omega}{\\omega_c}$  \"amplificateur hautes fr\u00e9quences\"\n\n$\\underline {T_4}(j\\omega)=\\frac{1}{1+j\\frac{\\omega}{\\omega_c}}$  passe bas",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-1326",
"position": 3,
"duration": 30,
"question": {
"id": "1326",
"question": "Soit $H(p)$ la fonction de transfert d'un SLCI. Comment calcule-t-on le d\u00e9phasage $\\phi(\\omega)$ pour une r\u00e9ponse harmonique de pulsation $\\omega$ ?",
"answer": "\\[\\phi(\\omega)=\\arg\\left(H(j\\omega)\\right)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-575",
"position": 4,
"duration": 30,
"question": {
"id": "575",
"question": "Tracer l'allure du diagramme asymptotique de Bode de la fonction $H_ {(j \\omega)}=\\frac{10}{1+j \\frac{\\omega}{\\omega_1}}$",
"answer": "$H_ {(j \\omega)}=\\frac{10}{1+j \\frac{\\omega}{\\omega_1}}$\npour $\\omega<<\\omega_1$   $H_ {(j \\omega)}=\\frac{10}{1}$\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0Gain  $  20 \\cdot log (K)$ \u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 Phase $\\phi=0$\npour $\\omega>>\\omega_1$   $H_ {(j \\omega)}=\\frac{10}{j\\frac{\\omega}{\\omega_1}}$\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0Gain  $  20 \\cdot  log(K)-20   \\cdot log(\\frac{\\omega}{\\omega_1})$\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0le gain tends vers $-\\infty$ \u00e0 la vitesse de $20 \\; dB\/dc$\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0Phase $\\phi=\\frac{-\\pi }{2}$",
"image_question_url": "",
"image_answer_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/613b2570-37d9-11e7-b753-79bc1ce90a6e",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1399-576",
"position": 5,
"duration": 30,
"question": {
"id": "576",
"question": "Tracer l'allure du diagramme asymptotique de Bode de la fonction $H_{(j \\omega)}=\\frac{1}{j \\frac{\\omega}{\\omega_3}}$",
"answer": "\u00a0",
"image_question_url": "",
"image_answer_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/76541df0-37d9-11e7-80a7-23335fa80793",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1399-2390",
"position": 6,
"duration": 30,
"question": {
"id": "2390",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=\\frac{K}{1+j\\frac{\\omega}{\\omega_c}}$.\n1. Comment appelle-t-on $K$ ?\n2. Comment appelle-t-on $\\omega_c$ ?",
"answer": "1. K est le gain statique de la fonction de transfert. (Gain de la fonction de transfert \u00e0 la pulsation nulle).\n2. $\\omega_c$ est la pulsation de cassure.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-2250",
"position": 7,
"duration": 30,
"question": {
"id": "2250",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=\\frac{K}{1+j\\frac{\\omega}{\\omega_c}}$.\n1. Comment appelle-t-on $K$ ?\n2. Comment appelle-t-on $\\omega_c$ ?",
"answer": "1. K est le gain statique de la fonction de transfert. (Gain de la fonction de transfert \u00e0 la pulsation nulle).\n2. $\\omega_c$ est la pulsation de cassure.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1399-2251",
"position": 8,
"duration": 30,
"question": {
"id": "2251",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=\\frac{20}{1+4j\\omega}$.\n1. Quelle est la forme canonique de cet fonction de transfert ?\n2. D\u00e9terminer $K$ et $\\omega_c$.\n3. Faire l'\u00e9tude de la fonction et tracer le diagramme de Bode asymptotique de cette fonction.",
"answer": "1. La forme canonique associ\u00e9e est celle d'un passe bas du 1er ordre soit $\\underline T(j\\omega)=\\frac{K}{1+j\\frac{\\omega}{\\omega_c}}$\n2. On en d\u00e9duit que $K=20$ et $\\omega_c=\\frac{1}{4}$",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c28d1b50-2383-11e8-8c13-c718148b4a79",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1399-2252",
"position": 9,
"duration": 30,
"question": {
"id": "2252",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=\\frac{1}{2+j\\omega}$.\n1. Mettre la fonction sous forme canonique.\n2. Faire l'\u00e9tude de la fonction et tracer le diagramme de Bode asymptotique de cette fonction.",
"answer": "1.  $\\underline T(j\\omega)=\\frac{1}{2+j\\omega}=\\frac{1}{2 (1+j\\frac{\\omega}{2})}$\n\nOn observe une fonction de transfert de la forme $\\frac{K}{(1+j\\frac{\\omega}{\\omega_c})}$\navec $K = \\frac{1}{2}$ et $\\omega_c=2$\n\n\n",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8b336660-2387-11e8-81aa-e7ed6526b726",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1399-2253",
"position": 10,
"duration": 30,
"question": {
"id": "2253",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=2+j\\omega$.\n1. Mettre la fonction sous forme canonique.\n2. Faire l'\u00e9tude de la fonction et tracer le diagramme de gain asymptotique de cette fonction.",
"answer": "1.  $\\underline T(j\\omega)=2+j\\omega=2 (1+j\\frac{\\omega}{2})$\n\nOn observe une fonction de transfert de la forme $K.(1+j\\frac{\\omega}{\\omega_c})$\navec $\\omega_c = 2$ et $K=2$",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/81dc3270-239a-11e8-8a53-f9daa4c6ad4e",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1399-2254",
"position": 11,
"duration": 30,
"question": {
"id": "2254",
"question": "Soit la fonction de transfert $\\underline T(j\\omega)=4+j\\omega$.\n1. Mettre la fonction sous forme canonique.\n2. Faire l'\u00e9tude de la fonction et tracer le diagramme de phase asymptotique de cette fonction.",
"answer": "1.  $\\underline T(j\\omega)=2+j\\omega=4 (1+j\\frac{\\omega}{4})$\n\nOn observe une fonction de transfert de la forme $K.(1+j\\frac{\\omega}{\\omega_c})$\navec $\\omega_c = 4$ et $K=4$",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/79fddfa0-239b-11e8-a88f-cb4a9ff27abd",
"field_id": "11",
"course_id": "16",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1404": {
"id": "1404",
"name": "dc5 statique",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1404\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "31",
"value": "Statique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "24",
"value": "Mod\u00e9lisation des liaisons",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 600,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-03-23",
"questions": [{
"id": "1404-709",
"position": 0,
"duration": 30,
"question": {
"id": "709",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}=\\begin{Bmatrix}   0 & 0\\\\ \\omega_{y,2\/1} & 0\\\\0 & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/27d888d0-9880-11e7-a0b7-9fd6de081d87",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-721",
"position": 1,
"duration": 30,
"question": {
"id": "721",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$).",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}  0 & V_{O_x,{2\/1}}\\\\ \\omega_{y,2\/1} & V_{O_y,{2\/1}}  \\\\ \\omega_{z,2\/1} & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/1854d950-9896-11e7-bbc7-91142743c545",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-716",
"position": 2,
"duration": 30,
"question": {
"id": "716",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}  0 & 0\\\\ 0 & V_{O_y,{2\/1}}  \\\\ 0 & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/63c42500-9882-11e7-a7ad-f3aa59941c6b",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-88",
"position": 3,
"duration": 30,
"question": {
"id": "88",
"question": "Donner la forme g\u00e9n\u00e9rale d'un torseur d'actions m\u00e9caniques de type glisseur  entre deux pi\u00e8ces (1 et 2)   au centre de la liaison (K), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{T_{1\\rightarrow2} \\} =\\begin{Bmatrix}\\overrightarrow { R_{1\\rightarrow2}}\\\\\\overrightarrow{0}\\end{Bmatrix}_K=\\begin{Bmatrix}X_{12} & 0\\\\ Y_{12} & 0  \\\\ Z_{12} & 0\\end{Bmatrix}_{K,  (\\vec{x} , \\vec{y}, \\vec{z})}$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1404-89",
"position": 4,
"duration": 30,
"question": {
"id": "89",
"question": "Exprimer le torseur d'actions m\u00e9caniques au centre de la liaison (A), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.\n",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & 0 \\\\ Y_{12} & M_{12}  \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{A , (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/05e63a00-01b6-11e8-9237-e38706465c96",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1404-1761",
"position": 5,
"duration": 30,
"question": {
"id": "1761",
"question": "Quelle sont les propri\u00e9t\u00e9s d'un solide soumis \u00e0 deux actions m\u00e9caniques de type Force ?",
"answer": "\u2022 les r\u00e9sultantes ont comme droite support la droite reliant les points d'application des 2 forces,\n\u2022 les r\u00e9sultantes ont m\u00eame intensit\u00e9 mais un sens oppos\u00e9. ",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5396dea0-fdba-11e7-b1c9-2730a56ee7b7",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-1850",
"position": 6,
"duration": 30,
"question": {
"id": "1850",
"question": "D\u00e9finir le $TMS$",
"answer": "Th\u00e9or\u00e8me du Moment Statique \nIl consiste \u00e0 faire la somme des composantes des moments qui agissent sur l'isolement.   $\\sum \\overrightarrow{M_{K , \\overline S \\rightarrow S}}=\\overrightarrow  {0}$\n Il est n\u00e9cessaire de d\u00e9placer les torseurs en un m\u00eame point pour l'appliquer.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1950",
"position": 7,
"duration": 30,
"question": {
"id": "1950",
"question": "Combien d'inconnues statiques $N_s$ ?",
"answer": "$N_s=2$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/1482e710-09b5-11e8-bc3b-05f2f27cf45c",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1404-1851",
"position": 8,
"duration": 30,
"question": {
"id": "1851",
"question": "D\u00e9finir le $PFS$",
"answer": "Principe Fondamental de la Statique\nIl consiste \u00e0 appliquer le TRS et le TMS \u00e0 un isolement. On obtient 6 \u00e9quations scalaires.\n$\\sum \\overrightarrow{R_{ \\overline S \\rightarrow S}}=\\overrightarrow  {0}$\n$\\sum \\overrightarrow{M_{K , \\overline S \\rightarrow S}}=\\overrightarrow  {0}$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1753",
"position": 9,
"duration": 30,
"question": {
"id": "1753",
"question": "Citer les 6 \u00e9tapes de la r\u00e9solution d'un probl\u00e8me de statique ?",
"answer": "1 Etablir le graphe d'analyse \n2 Choisir un isolement\n3 Etablir le BAME\n4 Mod\u00e9liser chacune des actions m\u00e9caniques\n5 choisir une strat\u00e9gie de calcul (TRS, TMS, PFS)\n6 r\u00e9soudre\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1764",
"position": 10,
"duration": 30,
"question": {
"id": "1764",
"question": "Quel est le th\u00e9or\u00e8me des actions mutuelles ?",
"answer": "On montre que les actions r\u00e9ciproques entre deux solides {\ud835\udc7a\ud835\udfcf} et {\ud835\udc7a\ud835\udfd0} sont oppos\u00e9es. $ \\{T_{1\\rightarrow2} \\} =- \\{T_{2\\rightarrow1} \\} $\n\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-1953",
"position": 11,
"duration": 30,
"question": {
"id": "1953",
"question": "Combien d'inconnues statiques $N_s$ ?",
"answer": " $N_s=2$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/84547bb0-09b5-11e8-bcfb-d9a7982f4931",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1404-1854",
"position": 12,
"duration": 30,
"question": {
"id": "1854",
"question": "Exprimer le torseur d'actions m\u00e9caniques au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}0 & 0\\\\ Y_{12} & M_{12}  \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{O, (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5dac5b60-01b6-11e8-bed0-9f10b401f34d",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1404-1955",
"position": 13,
"duration": 30,
"question": {
"id": "1955",
"question": "Exprimer le torseur d'actions m\u00e9caniques de la liaison au point O, dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$. \nO\u00f9 peut se trouver le point O pour que l'allure du torseur (les \"z\u00e9ros\" au m\u00eame endroit) reste la m\u00eame ? \nQuel est le nom complet de cette liaison ? \nDonner le nombre d\u2019inconnues statique de la liaison : ns= ?",
"answer": "$ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix} 0 &0 \\\\ 0 &  M_{12}\\\\ Z_{12} &0 \\end{Bmatrix}_{O , (\\vec{x} , \\vec{y}, \\vec{z})} $ \nLe point O peut se trouver en tout point du plan (O,$ \\vec{x}$,$ \\vec{z}$).\n La liaison est une lin\u00e9aire rectiligne de normale (O,$ \\vec{z}$) et d'ar\u00eate (O,$ \\vec{x}$) .\n ns =2",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/89bc07a0-09ba-11e8-81d5-7dc247377eea",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1404-1757",
"position": 14,
"duration": 30,
"question": {
"id": "1757",
"question": "D\u00e9finition d'une $r\u00e9sultante$,",
"answer": "On la note $\\overrightarrow { R_{1\\rightarrow2}}$\nLa r\u00e9sultante d\u2019une action m\u00e9canique d\u2019un solide 2 sur un solide 1 traduit la capacit\u00e9 de l\u2019action m\u00e9canique \u00e0 d\u00e9placer, stopper ou d\u00e9former le solide 2 par translation.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1717",
"position": 15,
"duration": 30,
"question": {
"id": "1717",
"question": "\u00e0 quelle action m\u00e9canique correspond un couple  (en Nm) ?",
"answer": "un couple est le nom donn\u00e9 au moment d'une action m\u00e9canique repr\u00e9sent\u00e9e par un torseur couple (o\u00f9 la r\u00e9sultante est nulle).\n$ \\{T_{1\\rightarrow2} \\} =\\begin{Bmatrix}\\overrightarrow { 0}\\\\\\overrightarrow{M_{K , 1\\rightarrow2}}\\end{Bmatrix}_K=\\begin{Bmatrix}0 & L_{12}\\\\ 0 & M_{12}  \\\\0 & N_{12}\\end{Bmatrix}_{K,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1849",
"position": 16,
"duration": 30,
"question": {
"id": "1849",
"question": "D\u00e9finir le $TRS$.",
"answer": "Th\u00e9or\u00e8me de la R\u00e9sultante Statique \nIl consiste \u00e0 faire la somme des composantes des r\u00e9sultantes qui agissent sur l'isolement. $\\sum \\overrightarrow{R_{, \\overline S \\rightarrow S}}=\\overrightarrow  {0}$\nIl n'est pas n\u00e9cessaire de d\u00e9placer les torseurs en un m\u00eame point pour l'appliquer.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1404-1927",
"position": 17,
"duration": 30,
"question": {
"id": "1927",
"question": "Combien d'inconnues statiques $N_s$ dans un probl\u00e8me plan ($\\vec {x}$, $\\vec {z}$)",
"answer": "$N_s=2$\n $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}0 & -\\\\ - &   M12  \\\\ Z12 & -\\end{Bmatrix}_{C, (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/368a5770-081a-11e8-b5dd-fb42d0e7d2d9",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1404-108",
"position": 18,
"duration": 30,
"question": {
"id": "108",
"question": "Compl\u00e9ter le torseur d'actions m\u00e9caniques au centre de la liaison (A), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$).\n $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & L_{12}\\\\   & M_{12}  \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{A,  (\\vec{x} , \\vec{y}, \\vec{z})}  $",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & L_{12}\\\\  \\frac{M_{12}.2.\\pi }{p}  & M_{12}  \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{A,  (\\vec{x} , \\vec{y}, \\vec{z})}  $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/59526650-9956-11e7-8bf5-b73019616091",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1404-714",
"position": 19,
"duration": 30,
"question": {
"id": "714",
"question": "Indiquer le torseur cin\u00e9matique en O, entre deux pi\u00e8ces (1 et 2) sans liaison,  dans une base$(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}   \\omega_{x,2\/1} & V_{O_x,{2\/1}}\\\\ \\omega_{y,2\/1} & V_{O_y,{2\/1}}  \\\\ \\omega_{z,2\/1} &V_{O_z,{2\/1}}\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "141",
"name": "TSI1 ",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1408": {
"id": "1408",
"name": "R\u00e9visions calcul (1)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1408\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-09",
"questions": [{
"id": "1408-2879",
"position": 0,
"duration": 30,
"question": {
"id": "2879",
"question": "Citer l'in\u00e9galit\u00e9 triangulaire.",
"answer": "$\\forall (x,y)\\in\\mathbf{R}^2\\ |x+y|\\leq |x|+|y|$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-2880",
"position": 1,
"duration": 30,
"question": {
"id": "2880",
"question": "R\u00e9soudre l'\u00e9quation $|x-5|=2$.",
"answer": "$x=3$ ou $x=7$. (interpr\u00e9tez en termes de distance : la distance de x \u00e0 5 vaut 2 donc...)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1408-2881",
"position": 2,
"duration": 30,
"question": {
"id": "2881",
"question": "Soient $(a,b,c)\\in\\mathbf{R}^3$. On suppose $a\\neq 0$. Sous quelle condition l'\u00e9quation $ax^2+bx+c=0$ admet-elle une unique solution ? Factoriser le trin\u00f4me $ax^2+bx+c$ dans ce cas.",
"answer": "L'\u00e9quation admet une unique solution si et seulement si $b^2-4ac=0$.\nDans ce cas, on a $ax^2+bx+c=a(x+\\frac{b}{2a})^2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3253",
"position": 3,
"duration": 30,
"question": {
"id": "3253",
"question": "D\u00e9finition de la valeur absolue d'un r\u00e9el $x$.",
"answer": "$|x|=x$ si $x\\geq0$, et $|x|=-x$ si $x<0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-2896",
"position": 4,
"duration": 30,
"question": {
"id": "2896",
"question": "Soit $x\\in\\mathbf{R}$. Interpr\u00e9ter en termes de distance le nombre $|x+1|$.",
"answer": "C'est la distance entre $x$ et $-1$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1408-5895",
"position": 5,
"duration": 30,
"question": {
"id": "5895",
"question": "On consid\u00e8re un trin\u00f4me du second degr\u00e9 sous forme canonique : $a(x-\\alpha)^2+ \\beta$. Quelle information concernant la courbe repr\u00e9sentative du trin\u00f4me lit-on dans cette forme canonique ?\n\nExemple avec le trin\u00f4me $2(x+1)^2-3$ ?",
"answer": "Les coordonn\u00e9es du sommet S de la parabole qui sont S$(\\alpha,\\beta)$\nExemple : la courbe de la fonction $x\\mapsto 2(x+1)^2-3$ a pour sommet $S(-1;-3)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3255",
"position": 6,
"duration": 30,
"question": {
"id": "3255",
"question": "Soient $x$ et $y$ deux r\u00e9els. Exprimer la distance entre $x$ et $y$ \u00e0 l'aide d'une valeur absolue.",
"answer": "$|x-y|$ ou $|y-x|$ , cela revient au m\u00eame !",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3258",
"position": 7,
"duration": 30,
"question": {
"id": "3258",
"question": "Exprimer la propri\u00e9t\u00e9 de compatibilit\u00e9 avec la multiplication de la relation d'ordre $\\leq$.",
"answer": "SI $x\\leq y$ et $z\\geq 0$, alors $x\\times z\\leq y\\times z$.\nSi $x\\leq y$ et $z\\leq 0$, alors $x\\times z\\geq y\\times z$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-2894",
"position": 8,
"duration": 30,
"question": {
"id": "2894",
"question": "R\u00e9soudre l'in\u00e9quation $|x-2|\\leq 3$.",
"answer": "$\\mathcal{S}=[-1;5]$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1408-2883",
"position": 9,
"duration": 30,
"question": {
"id": "2883",
"question": "Soient $(a,b,c)\\in\\mathbf{R}^3$. On suppose $a\\neq 0$. Sous quelle condition l'\u00e9quation $ax^2+bx+c=0$ admet-elle deux solutions r\u00e9elles distinctes ? Factoriser le trin\u00f4me $ax^2+bx+c$ dans ce cas.",
"answer": "L'\u00e9quation admet deux solutions r\u00e9elles distinctes si et seulement si $b^2-4ac>0$.\nDans ce cas, $ax^2+bx+c=a(x-\\frac{-b+\\sqrt{\\Delta}}{2a})(x-\\frac{-b-\\sqrt{\\Delta}}{2a})$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3261",
"position": 10,
"duration": 30,
"question": {
"id": "3261",
"question": "D\u00e9riv\u00e9e de $x^n$ pour $n$ entier.",
"answer": "\\[nx^{n-1}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3265",
"position": 11,
"duration": 30,
"question": {
"id": "3265",
"question": "D\u00e9riv\u00e9e de $\\cos x$",
"answer": "\\[-\\sin x\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1408-3266",
"position": 12,
"duration": 30,
"question": {
"id": "3266",
"question": "D\u00e9riv\u00e9e de $\\sin x$",
"answer": "\\[\\cos x\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1410": {
"id": "1410",
"name": "R\u00e9visions calcul (d\u00e9riv\u00e9es)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1410\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 450,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-16",
"questions": [{
"id": "1410-3261",
"position": 0,
"duration": 30,
"question": {
"id": "3261",
"question": "D\u00e9riv\u00e9e de $x^n$ pour $n$ entier.",
"answer": "\\[nx^{n-1}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3262",
"position": 1,
"duration": 30,
"question": {
"id": "3262",
"question": "D\u00e9riv\u00e9e de $\\sqrt{x}$",
"answer": "\\[\\frac{1}{2\\sqrt{x}}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3264",
"position": 2,
"duration": 30,
"question": {
"id": "3264",
"question": "D\u00e9riv\u00e9e de $\\ln x$",
"answer": "\\[\\frac{1}{x}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3265",
"position": 3,
"duration": 30,
"question": {
"id": "3265",
"question": "D\u00e9riv\u00e9e de $\\cos x$",
"answer": "\\[-\\sin x\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3266",
"position": 4,
"duration": 30,
"question": {
"id": "3266",
"question": "D\u00e9riv\u00e9e de $\\sin x$",
"answer": "\\[\\cos x\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3267",
"position": 5,
"duration": 30,
"question": {
"id": "3267",
"question": "D\u00e9riv\u00e9e de $\\tan x$ (deux formules)",
"answer": "\\[\\frac{1}{\\cos^2x}=1+\\tan^2 x\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3271",
"position": 6,
"duration": 30,
"question": {
"id": "3271",
"question": "D\u00e9riv\u00e9e de $\\frac{u(x)}{v(x)}$.",
"answer": "\\[\\frac{u^\\prime(x)v(x)-u(x)v^\\prime(x)}{v^2(x)}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3272",
"position": 7,
"duration": 30,
"question": {
"id": "3272",
"question": "D\u00e9riv\u00e9e de $v\\big(u(x)\\big)$",
"answer": "\\[u^\\prime(x)\\times v^\\prime\\big(u(x)\\big)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3273",
"position": 8,
"duration": 30,
"question": {
"id": "3273",
"question": "D\u00e9riv\u00e9e de $u^n(x)$",
"answer": "\\[nu^\\prime(x)u^{n-1}(x)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3274",
"position": 9,
"duration": 30,
"question": {
"id": "3274",
"question": "D\u00e9riv\u00e9e de $\\sqrt{u(x)}$.",
"answer": "\\[\\frac{u^\\prime(x)}{2\\sqrt{u(x)}}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3275",
"position": 10,
"duration": 30,
"question": {
"id": "3275",
"question": "D\u00e9riv\u00e9e de $\\ln(u(x))$.",
"answer": "\\[\\frac{u^\\prime(x)}{u(x)}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3276",
"position": 11,
"duration": 30,
"question": {
"id": "3276",
"question": "D\u00e9riv\u00e9e de $e^{u(x)}$.",
"answer": "\\[u^\\prime(x)e^{u(x)}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3269",
"position": 12,
"duration": 30,
"question": {
"id": "3269",
"question": "D\u00e9riv\u00e9e de $u(x)\\times v(x)$",
"answer": "\\[u^\\prime(x)v(x)+u(x)v^\\prime(x)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-3270",
"position": 13,
"duration": 30,
"question": {
"id": "3270",
"question": "D\u00e9riv\u00e9e de $\\frac{1}{u(x)}$.",
"answer": "\\[-\\frac{u^\\prime(x)}{u^2(x)}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1410-5930",
"position": 14,
"duration": 30,
"question": {
"id": "5930",
"question": "Mettre sous forme canonique le trin\u00f4me $x^2+6x+1$",
"answer": "$x^2+6x+1=(x+3)^2-8$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1411": {
"id": "1411",
"name": "R\u00e9visions (primitives et limites)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1411\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 450,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-09-24",
"questions": [{
"id": "1411-5361",
"position": 0,
"duration": 30,
"question": {
"id": "5361",
"question": "Donner une primitive de $f$ d\u00e9finie par $f(x)=e^{-2x}$",
"answer": "$F(x)=-\\dfrac{1}{2} e^{-2x}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5362",
"position": 1,
"duration": 30,
"question": {
"id": "5362",
"question": "Donner une primitive de $f$ d\u00e9finie sur un intervalle ne contenant par 0 par $f(x)=\\cos x+\\dfrac{2}{x}$",
"answer": "$F(x)=\\sin x + 2 \\ln|x|$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5364",
"position": 2,
"duration": 30,
"question": {
"id": "5364",
"question": "$u$ \u00e9tant une fonction d\u00e9rivable sur $\\mathbb{R}$, donner une primitive de $u' u^n$ lorsque $n \\neq -1$",
"answer": "$\\dfrac{1}{n+1} u^{n+1}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5835",
"position": 3,
"duration": 30,
"question": {
"id": "5835",
"question": "Soit $u$ une fonction d\u00e9rivable et qui ne s'annule pas sur un intervalle I. Donner une primitive de la fonction $\\dfrac{u'}{u}$",
"answer": "$\\ln |u|$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5365",
"position": 4,
"duration": 30,
"question": {
"id": "5365",
"question": "Donner une primitive de $f$ d\u00e9finie par $f(x)=\\dfrac{x}{x^2+1}$",
"answer": "$F(x)=\\dfrac{1}{2} \\ln|x^2+1|=\\dfrac{1}{2} \\ln(x^2+1)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5899",
"position": 5,
"duration": 30,
"question": {
"id": "5899",
"question": "$\\lim\\limits_{x \\to +\\infty} \\dfrac{-3}{1-x}= $ ?",
"answer": "0",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5900",
"position": 6,
"duration": 30,
"question": {
"id": "5900",
"question": "$\\lim\\limits_{x \\to 0^+} \\dfrac{3}{x}= $ ?",
"answer": "$+ \\infty$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5901",
"position": 7,
"duration": 30,
"question": {
"id": "5901",
"question": "$\\lim\\limits_{x \\to 2\\\\x>2} \\dfrac{x-3}{x-2}= $ ?",
"answer": "$- \\infty$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-2888",
"position": 8,
"duration": 30,
"question": {
"id": "2888",
"question": "\\[\\lim_{x\\to +\\infty}\\frac{e^x}{x}=?\\]",
"answer": "$+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-2887",
"position": 9,
"duration": 30,
"question": {
"id": "2887",
"question": "\\[\\lim_{x\\to 0}x\\ln x=?\\]",
"answer": "$0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-2890",
"position": 10,
"duration": 30,
"question": {
"id": "2890",
"question": "\\[\\lim_{x\\to+\\infty}\\frac{x}{\\ln x}=?\\]",
"answer": "$+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-2889",
"position": 11,
"duration": 30,
"question": {
"id": "2889",
"question": "\\[\\lim_{x\\to-\\infty}xe^x=?\\]",
"answer": "$0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-2882",
"position": 12,
"duration": 30,
"question": {
"id": "2882",
"question": "Si $\\lim\\limits_{x\\to+\\infty} u(x)=\\lim\\limits_{x\\to+\\infty}v(x)=+\\infty$, que peut-on dire des limites en $+\\infty$ de $u+v$, $u-v$, $uv$, $\\frac{u}{v}$ ?",
"answer": "$\\lim\\limits_{x\\to+\\infty}(u(x)+v(x))=\\lim\\limits_{x\\to+\\infty}(u(x)\\times v(x))=+\\infty$. Les limites de $u-v$ et $\\frac{u}{v}$ sont ind\u00e9termin\u00e9es.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-4915",
"position": 13,
"duration": 30,
"question": {
"id": "4915",
"question": "Soit $a$ un r\u00e9el. Si $\\lim\\limits_{x\\to a} u(x) =+\\infty$ et $\\lim\\limits_{x\\to a} v(x) =-\\infty$, que dire des limites en $a$ de $u+v , \\quad u \\times v , \\quad \\frac{u}{v}$ ?",
"answer": "le produit a pour limite $-\\infty$, les 2 autres limites sont ind\u00e9termin\u00e9es.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1411-5836",
"position": 14,
"duration": 30,
"question": {
"id": "5836",
"question": "Soit $a$ un r\u00e9el. Si $\\lim\\limits_{x\\to a} u(x) =0^{-}$ et $\\lim\\limits_{x\\to a} v(x) =-\\infty$, que dire des limites en $a$ de $\\dfrac{v}{u} , \\quad  \\dfrac{u}{v} $ ?",
"answer": "$\\lim\\limits_{x\\to a} \\dfrac{v(x)}{u(x)} = +\\infty$ et $\\lim\\limits_{x\\to a} \\dfrac{u(x)}{v(x)} = 0$  ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1415": {
"id": "1415",
"name": "DC3_0",
"user_id": "1160",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1415\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "155",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-15 10:21:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 5,
"duration": 420,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-04",
"questions": [{
"id": "1415-608",
"position": 0,
"duration": 30,
"question": {
"id": "608",
"question": "projeter $\\vec{X}_1$ dans la base  $(\\vec{X}  ; \\vec{Y}  ;  \\vec{Z})$",
"answer": "$\\overrightarrow{X_1} =  \\cos (\\alpha_1).\\overrightarrow{X}+\\sin (\\alpha_1).\\overrightarrow{Z} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5222c100-57dd-11e7-b4c5-e1b92121d1d8",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 5
}
}, {
"id": "1415-609",
"position": 1,
"duration": 30,
"question": {
"id": "609",
"question": "projeter $\\vec{X_{12}}$ dans la base $(\\vec{X}  ; \\vec{Y}  ;  \\vec{Z})$",
"answer": "$\\overrightarrow{X_{12}} =  \\cos (\\beta).\\overrightarrow{X}+\\sin (\\beta).\\overrightarrow{Z} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/68f59e20-57f0-11e7-89e7-2ddcda6461df",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1415-58",
"position": 2,
"duration": 30,
"question": {
"id": "58",
"question": "$\\vec{V_2}  . \\vec{V_1} = $",
"answer": "$\\vec{V_2}  . \\vec{V_1} =V_2.V_1. \\cos(\\theta) =V_1.V_2. \\cos(\\theta) $",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/1be2dfc8-fd36-4c0c-a69e-52d4809d8478",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1415-1460",
"position": 3,
"duration": 30,
"question": {
"id": "1460",
"question": "projeter $\\vec{y}_2$ dans la base B1",
"answer": "$\\vec{y}_2 = -\\sin (\\theta).\\vec{x}_1 +  \\cos(\\theta). \\vec{y}_1$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/09f81350-cec8-11e7-82d2-f7e04eb982af",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1415-1067",
"position": 4,
"duration": 30,
"question": {
"id": "1067",
"question": "Calculer $\\vec {x} \\wedge \\vec {y}$",
"answer": " $\\vec {x} \\wedge \\vec {y}=\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ce9d8630-b42a-11e7-a53a-337a36f243fd",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1415-1068",
"position": 5,
"duration": 30,
"question": {
"id": "1068",
"question": "Calculer $\\vec {x}_1 \\wedge \\vec {y}_1$",
"answer": " $\\vec {x}_1 \\wedge \\vec {y}_1= \\vec{z}_1$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e9a9e2e0-b42a-11e7-a118-39564fe59404",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1415-59",
"position": 6,
"duration": 30,
"question": {
"id": "59",
"question": "$\\vec{x_0}  \\wedge \\vec{y_0} = $",
"answer": "$\\vec{x_0}  \\wedge \\vec{y_0} = \\vec{z_0}$",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/75a01b1a-0da7-42aa-bdaa-e450927dae06",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1415-1070",
"position": 7,
"duration": 30,
"question": {
"id": "1070",
"question": "Calculer $\\vec {x}_1 \\wedge \\vec {y}_0$",
"answer": "$\\vec {x}_1 \\wedge \\vec {y}_0=\\sin(\\frac{\\pi}{2}-\\beta) . \\vec{z}_0=\\cos(\\beta). \\vec{z}_0$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/339a05d0-b42b-11e7-82e4-9f3d6e163956",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1415-1072",
"position": 8,
"duration": 30,
"question": {
"id": "1072",
"question": "Calculer $\\vec {y}_1 \\wedge \\vec {x}_1$",
"answer": "$\\vec {y}_1 \\wedge \\vec {x}_1=-  \\vec {z}_1$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c51a9440-b42b-11e7-89fe-8d1dd144f909",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1415-2241",
"position": 9,
"duration": 30,
"question": {
"id": "2241",
"question": "$\\vec{z_2} \\land \\vec{z_0} = $ ?\nR\u00e9ponse dans la base $R_2$",
"answer": "$\\vec{z_2} \\land \\vec{z_0} = \\vec{z_2} \\land (cos\\varphi\\,\\vec{z_1} - sin\\varphi\\,\\vec{x_1}) $\n$\\vec{z_2} \\land \\vec{z_0} = - cos\\theta\\,cos\\varphi\\,\\vec{x_2} - sin\\varphi\\,\\vec{y_2}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9bf7b850-1c98-11e8-95a5-f3144048d561",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1415-63",
"position": 10,
"duration": 30,
"question": {
"id": "63",
"question": "$\\vec{x_2}  \\wedge \\vec{y_1} =$",
"answer": "$\\vec{x_2}  \\wedge \\vec{y_1} = \\sin(\\frac{\\pi}{2} - \\alpha) .\\vec{z_1}=\\cos(\\alpha) .\\vec{z_1}$",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/78ad414b-2f01-4ca6-80f5-8e54403ea03c",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1415-1076",
"position": 11,
"duration": 30,
"question": {
"id": "1076",
"question": "Calculer $\\vec {z}_2 \\wedge \\vec {x}_2$",
"answer": "$\\vec {z}_2 \\wedge \\vec {x}_2= \\vec {y}_2$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/57f198d0-b42c-11e7-a6b1-b7792bcadbb2",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1415-53",
"position": 12,
"duration": 30,
"question": {
"id": "53",
"question": "projeter $\\overrightarrow{x_1}$ dans la base B0",
"answer": "$\\overrightarrow{x_1} = \\cos (\\alpha).\\overrightarrow{x_0} +  \\sin (\\alpha).\\overrightarrow{y_0}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e6695210-a431-11e7-b8c5-73324bd37f5f",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8bddde20-a431-11e7-b8af-eb61c39e05a9",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1415-1066",
"position": 13,
"duration": 30,
"question": {
"id": "1066",
"question": "Calculer $\\vec {x} \\wedge \\vec {x}_1$",
"answer": " $\\vec {x} \\wedge \\vec {x}_1=\\sin(\\alpha) . \\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/43650e40-b42a-11e7-847d-d16121e8ddc6",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1416": {
"id": "1416",
"name": "Nbes compexes (1)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1416\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-05",
"questions": [{
"id": "1416-2907",
"position": 0,
"duration": 30,
"question": {
"id": "2907",
"question": "Si $z=x+iy$ avec $x$ et $y$ r\u00e9els, $|z|=\\,?$",
"answer": "\\[|z|=\\sqrt{x^2+y^2}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2908",
"position": 1,
"duration": 30,
"question": {
"id": "2908",
"question": "Vrai ou faux ? (corriger si faux)\n\\[|z_1||z_2|=|z_1z_2|\\]",
"answer": "Vrai",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2909",
"position": 2,
"duration": 30,
"question": {
"id": "2909",
"question": "Vrai ou faux ? (corriger si faux)\n\\[|z_1+z_2|=|z_1|+|z_2|\\]",
"answer": "Faux\n\\[|z_1+z_2|\\leq |z_1|+|z_2|\\]\n(in\u00e9galit\u00e9 triangulaire)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2910",
"position": 3,
"duration": 30,
"question": {
"id": "2910",
"question": "Vrai ou faux ? (corriger si faux)\n\\[\\left|\\frac{z_1}{z_2}\\right|=\\frac{|z_1|}{|z_2|}\\]",
"answer": "Vrai",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2914",
"position": 4,
"duration": 30,
"question": {
"id": "2914",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $|z|$.",
"answer": "Distance entre l'origine et le point d'affixe $z$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2915",
"position": 5,
"duration": 30,
"question": {
"id": "2915",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $\\overline{z}$.",
"answer": "Sym\u00e9trique du point d'affixe $z$ par rapport \u00e0 l'axe r\u00e9el (axe des abscisses).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2952",
"position": 6,
"duration": 30,
"question": {
"id": "2952",
"question": "D\u00e9finition de $e^{i\\theta}$",
"answer": "\\[e^{i\\theta}=\\cos\\theta+i\\sin\\theta\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2949",
"position": 7,
"duration": 30,
"question": {
"id": "2949",
"question": "Formule d'Euler pour $\\cos\\theta$",
"answer": "\\[\\frac{e^{i\\theta}+e^{-i\\theta}}{2}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2950",
"position": 8,
"duration": 30,
"question": {
"id": "2950",
"question": "Formule d'Euler pour $\\sin\\theta$",
"answer": "\\[\\frac{e^{i\\theta}-e^{-i\\theta}}{2i}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2964",
"position": 9,
"duration": 30,
"question": {
"id": "2964",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $\\displaystyle z=\\rho e^{i\\theta}$ (avec sch\u00e9ma)",
"answer": "Le point $M$ d'affixe $z$ est situ\u00e9 \u00e0 une distance $\\rho$ de l'origine et le vecteur $\\overrightarrow{OM}$ forme un angle de mesure $\\theta$ avec l'axe des abscisses (autrement dit, $(\\rho,\\theta)$ sont les coordonn\u00e9es polaires du point $M$ dans le plan complexe).",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/34e41380-c622-11e8-abbf-c3edb88b4c7e",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2966",
"position": 10,
"duration": 30,
"question": {
"id": "2966",
"question": "Solutions de l'\u00e9quation $z^n=1$?",
"answer": "$n$ solutions distinctes:\n\\[z_k=e^{i\\frac{2k\\pi}{n}},\\quad k\\in\\{0; 1; \\dots;n-1\\}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-2970",
"position": 11,
"duration": 30,
"question": {
"id": "2970",
"question": "Solutions de $az^2+bz+c=0$, avec $a,b,c\\in\\mathbf{C}$ et $a\\neq 0$?",
"answer": "Si $b^2-4ac=0$, une seule solution: $\\displaystyle z=-\\frac{b}{2a}$\nSi $b^2-4ac\\neq 0$, soit $\\delta$ une racine carr\u00e9e complexe de $b^2-4ac$. Alors les deux solutions sont $\\displaystyle z=\\frac{-b\\pm\\delta}{2a}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1416-5931",
"position": 12,
"duration": 30,
"question": {
"id": "5931",
"question": "Forme trigonom\u00e9trique de $1+i$ et $-1+i$ ?",
"answer": "On s'aide d'un dessin pour les arguments, les modules sont \u00e9gaux \u00e0 $\\sqrt2$. On trouve :\n\n$1+i=\\sqrt2 e^{i\\frac{\\pi}{4}}$\n$-1+i=\\sqrt2 e^{i\\frac{3\\pi}{4}}$\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1418": {
"id": "1418",
"name": "DC3_1_2023",
"user_id": "1160",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1418\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "155",
"value": "Maths ing\u00e9.",
"field_id": "11",
"created_at": "2017-09-15 10:21:41",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "18",
"value": "Cin\u00e9matique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 510,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-17",
"questions": [{
"id": "1418-1059",
"position": 0,
"duration": 30,
"question": {
"id": "1059",
"question": "Quelle est la trajectoire $T_{B\\, \\in \\,3\/2}$ ?",
"answer": "$T_{B\\, \\in \\,3\/2}$ est un segment de droite d'axe $(C, \\vec{x_3})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/749c83c0-b351-11e7-8012-c3e1db79de44",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1418-851",
"position": 1,
"duration": 30,
"question": {
"id": "851",
"question": "Compl\u00e9ter la figure de changement de base",
"answer": "Figure :",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0a611630-a807-11e7-983f-a1c0b03a4431",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8937b140-a807-11e7-8999-d357a9249610",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-983",
"position": 2,
"duration": 30,
"question": {
"id": "983",
"question": "Exprimer la d\u00e9finition du vecteur position d\u2019un point O appartenant \u00e0 un solide S dans un rep\u00e8re de r\u00e9f\u00e9rence $\ud835\udc45_1 $ $(I,\\vec {\ud835\udc65_1}, \\vec {y_1}, \\vec {z_1}) $",
"answer": " $\\overrightarrow {IO}$ est le vecteur position d\u2019un point O appartenant \u00e0 un solide S dans un rep\u00e8re de r\u00e9f\u00e9rence $\ud835\udc45_1 $ $(I,\\vec {\ud835\udc65_1}, \\vec {y_1}, \\vec {z_1}) $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-852",
"position": 3,
"duration": 30,
"question": {
"id": "852",
"question": "Exprimer la fermeture g\u00e9om\u00e9trique du syst\u00e8me.",
"answer": " $\\overrightarrow {OO}=\\overrightarrow {OA}+\\overrightarrow {AB}+\\overrightarrow {BO}=\\vec 0$ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/829e88f0-a809-11e7-9f73-9f8da9f76b0a",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-845",
"position": 4,
"duration": 30,
"question": {
"id": "845",
"question": "Compl\u00e9ter la figure de changement de base",
"answer": "Figure :",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/6231ca70-a7e7-11e7-bf54-d1b4611e08dd",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/65f629e0-a7e7-11e7-bc03-1f6068fb86c3",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-989",
"position": 5,
"duration": 30,
"question": {
"id": "989",
"question": "Quelle est la trajectoire $T_{B\\, \\in \\,2\/3}$ ?",
"answer": " $T_{B\\, \\in \\,2\/3}$ est un segment de droite d'axe $(C, \\vec {x_3})$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/57876680-af13-11e7-8490-01aa1a6384fb",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-1132",
"position": 6,
"duration": 30,
"question": {
"id": "1132",
"question": "Le solide (1) et en mouvement de rotation d'axe $(0,\\vec{x_0})$ par rapport au solide (0). On note $(\\vec{z_0},\\vec{z_1})=\\beta$.\nR\u00e9aliser la figure plane de calcul illustrant le param\u00e8tre $\\beta$.",
"answer": "Figure",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/72cda800-b6f6-11e7-809f-f7de5c42ba7d",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/98d7d3b0-b6f6-11e7-ac71-1b11f0a48d52",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1418-11",
"position": 7,
"duration": 30,
"question": {
"id": "11",
"question": "D\u00e9finition du calcul direct pour le vecteur vitesse  $\\overrightarrow{V_{C \\in 2\/0}}$  \nrep\u00e8re de r\u00e9f\u00e9rence $\ud835\udc45_0 $ $(\ud835\udc42,\\vec {\ud835\udc65_0}, \\vec {y_0}, \\vec {z_0}) $",
"answer": "$\\overrightarrow{V_{C \\in 2\/0}} = \\left[ \\frac{d\\overrightarrow{{OC}}} {dt} \\right]_{\/R_0}$ si C est un point du solide 2 et 0 un point du solide de r\u00e9f\u00e9rence 0.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-16",
"position": 8,
"duration": 30,
"question": {
"id": "16",
"question": "D\u00e9finition du vecteur acceleration $\\overrightarrow{\\Gamma_{K \\in 2\/1}} $",
"answer": "$\\overrightarrow{\\Gamma_{K \\in 2\/1}} = \\left[ \\frac{d\\overrightarrow{V_{K \\in 2\/1}}} {dt} \\right]_{\/R_1}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-1067",
"position": 9,
"duration": 30,
"question": {
"id": "1067",
"question": "Calculer $\\vec {x} \\wedge \\vec {y}$",
"answer": " $\\vec {x} \\wedge \\vec {y}=\\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ce9d8630-b42a-11e7-a53a-337a36f243fd",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-1068",
"position": 10,
"duration": 30,
"question": {
"id": "1068",
"question": "Calculer $\\vec {x}_1 \\wedge \\vec {y}_1$",
"answer": " $\\vec {x}_1 \\wedge \\vec {y}_1= \\vec{z}_1$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e9a9e2e0-b42a-11e7-a118-39564fe59404",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1418-59",
"position": 11,
"duration": 30,
"question": {
"id": "59",
"question": "$\\vec{x_0}  \\wedge \\vec{y_0} = $",
"answer": "$\\vec{x_0}  \\wedge \\vec{y_0} = \\vec{z_0}$",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/75a01b1a-0da7-42aa-bdaa-e450927dae06",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1418-1070",
"position": 12,
"duration": 30,
"question": {
"id": "1070",
"question": "Calculer $\\vec {x}_1 \\wedge \\vec {y}_0$",
"answer": "$\\vec {x}_1 \\wedge \\vec {y}_0=\\sin(\\frac{\\pi}{2}-\\beta) . \\vec{z}_0=\\cos(\\beta). \\vec{z}_0$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/339a05d0-b42b-11e7-82e4-9f3d6e163956",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1418-1072",
"position": 13,
"duration": 30,
"question": {
"id": "1072",
"question": "Calculer $\\vec {y}_1 \\wedge \\vec {x}_1$",
"answer": "$\\vec {y}_1 \\wedge \\vec {x}_1=-  \\vec {z}_1$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/c51a9440-b42b-11e7-89fe-8d1dd144f909",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1418-63",
"position": 14,
"duration": 30,
"question": {
"id": "63",
"question": "$\\vec{x_2}  \\wedge \\vec{y_1} =$",
"answer": "$\\vec{x_2}  \\wedge \\vec{y_1} = \\sin(\\frac{\\pi}{2} - \\alpha) .\\vec{z_1}=\\cos(\\alpha) .\\vec{z_1}$",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/78ad414b-2f01-4ca6-80f5-8e54403ea03c",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1418-1076",
"position": 15,
"duration": 30,
"question": {
"id": "1076",
"question": "Calculer $\\vec {z}_2 \\wedge \\vec {x}_2$",
"answer": "$\\vec {z}_2 \\wedge \\vec {x}_2= \\vec {y}_2$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/57f198d0-b42c-11e7-a6b1-b7792bcadbb2",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1418-1066",
"position": 16,
"duration": 30,
"question": {
"id": "1066",
"question": "Calculer $\\vec {x} \\wedge \\vec {x}_1$",
"answer": " $\\vec {x} \\wedge \\vec {x}_1=\\sin(\\alpha) . \\vec{z}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/43650e40-b42a-11e7-847d-d16121e8ddc6",
"image_answer_url": "",
"field_id": "11",
"course_id": "155",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1419": {
"id": "1419",
"name": "G\u00e9om\u00e9trie plane (2)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1419\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "256",
"value": "Autre",
"field_id": "19",
"created_at": "2017-11-17 08:51:21",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2024-11-26",
"questions": [{
"id": "1419-5253",
"position": 0,
"duration": 30,
"question": {
"id": "5253",
"question": "Soit $d$ la droite d'\u00e9quation $ax+by+c=0$. Donner les coordonn\u00e9es d'un vecteur directeur de $d$.",
"answer": "$\\vec{u} \\binom{-b}{a}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5254",
"position": 1,
"duration": 30,
"question": {
"id": "5254",
"question": "Soit $d$ la droite d'\u00e9quation $ax+by+c=0$. Donner les coordonn\u00e9es d'un vecteur normal \u00e0 d.",
"answer": "$\\vec{n} \\binom{a}{b}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "256",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5367",
"position": 2,
"duration": 30,
"question": {
"id": "5367",
"question": "Dans un rep\u00e8re orthonorm\u00e9, caract\u00e9riser l'ensemble des points $M(x;y)$ v\u00e9rifiant $(x+1)^2+(y-2)^2=4$.",
"answer": "Il s'agit du cercle de centre $I(-1;2)$ et de rayon 2.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5837",
"position": 3,
"duration": 30,
"question": {
"id": "5837",
"question": "Donner un param\u00e9trage de la droite (AB) lorsque A(1;-1) et B(3;4).",
"answer": "$\\left\\{\\begin{array}{l} x=1+2t\\\\y= -1+5t \\end{array} \\right.$ , $t \\in \\mathbb{R}$ .\n\nCeci n'est qu'un exemple, il existe une infinit\u00e9 de param\u00e9trages de cette m\u00eame droite.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5838",
"position": 4,
"duration": 30,
"question": {
"id": "5838",
"question": "Doner un param\u00e9trage du cercle de centre I(2;3) et de rayon 4.",
"answer": "$\\left\\{ \\begin{array}{l} x=2+4\\cos t \\\\ y=3+4\\sin t \\end{array} \\right.$ ,  $t \\in \\mathbb{R}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5839",
"position": 5,
"duration": 30,
"question": {
"id": "5839",
"question": "D\u00e9crire pr\u00e9cis\u00e9ment l'ensemble des points de coordonn\u00e9es (x,y) v\u00e9rifiant :\n\n$\\left\\{\\begin{array}{l} x=2t\\\\y= 3-t \\end{array} \\right.$ , $t \\in \\mathbb{R}$  ?\n",
"answer": "Il s'agit de la droite passant par A(0;3) et dirig\u00e9e par le vecteur $\\vec{u} \\left| \\begin{array}{l} 2\\\\-1 \\end{array} \\right.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5840",
"position": 6,
"duration": 30,
"question": {
"id": "5840",
"question": "Le point B(-4;6) est-il sur la droite param\u00e9tr\u00e9e par $\\left\\{\\begin{array}{l} x=2+2t\\\\y= 3-t \\end{array} \\right.$ , $t \\in \\mathbb{R}$  ?\n",
"answer": "oui, il est atteint avec le param\u00e8tre $t=-3$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5841",
"position": 7,
"duration": 30,
"question": {
"id": "5841",
"question": "De mani\u00e8re g\u00e9n\u00e9rale, comment cherche-t-on l'intersection de deux ensembles d\u00e9finis par des \u00e9quations ?",
"answer": "On r\u00e9sout le syst\u00e8me form\u00e9 par les \u00e9quations d\u00e9finissant les deux ensembles.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5842",
"position": 8,
"duration": 30,
"question": {
"id": "5842",
"question": "Quel est l'ensemble des points M du plan tels que $\\overrightarrow{AM} \\cdot \\overrightarrow {AB}=0$ ?",
"answer": "Il s'agit de la perpendiculaire \u00e0 (AB) passant par A.\n(le produit scalaire nul traduit l'orthogonalit\u00e9 des vecteurs)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5903",
"position": 9,
"duration": 30,
"question": {
"id": "5903",
"question": "Quel est l'ensemble des points M du plan tels que $\\overrightarrow{MA} \\cdot \\overrightarrow {MB}=0$ ?",
"answer": "Il s'agit du cercle de diam\u00e8tre [AB].",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5904",
"position": 10,
"duration": 30,
"question": {
"id": "5904",
"question": "Donner une \u00e9quation cart\u00e9sienne de la droite param\u00e9tr\u00e9e par $\\left\\{\\begin{array}{l} x=2+2t\\\\y= 3-t \\end{array} \\right.$ , $t \\in \\mathbb{R}$  ?\n",
"answer": "$x+2y-8=0$ par exemple.\n\n$\\textit{Il suffit d'\u00e9liminer $t$ , soit par substitution, soit plus rapidement en effectuant $L_1$ + $2L_2$ o\u00f9 $L_1$ et $L_2$ sont les 2 lignes du syst\u00e8me}.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1419-5905",
"position": 11,
"duration": 30,
"question": {
"id": "5905",
"question": "Le vecteur $\\vec{v} \\left| \\begin{array}{l} -2\\\\-4 \\end{array} \\right.$ est-il un vecteur directeur de la droite d'\u00e9quation $2x-y+4=0$ ?",
"answer": "Oui, et c'est le cas de tout multiple du vecteur $\\vec{u} \\left| \\begin{array}{l} 1\\\\2 \\end{array} \\right.$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1420": {
"id": "1420",
"name": "Equations diff\u00e9rentielles \u00e0 coeff. constants",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1420\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "69",
"value": "Autre",
"field_id": "19",
"created_at": "2017-07-19 18:22:20",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-02",
"questions": [{
"id": "1420-3039",
"position": 0,
"duration": 30,
"question": {
"id": "3039",
"question": "M\u00e9thode de r\u00e9solution de l'\u00e9quation $y'+ay=b(t)$ o\u00f9 $a \\in \\mathbb{R}$ et $b$ fonction continue sur $\\mathbb{R}$.",
"answer": "1. R\u00e9solution de l'\u00e9quation homog\u00e8ne $y'+ay=0$ : on note $y_H$ les solutions.\n2. Recherche d'une solution partilculi\u00e8re, not\u00e9e $y_P$, de l'\u00e9quation compl\u00e8te.\n3. Conclusion : toutes les solutions de l'\u00e9quation initiale s'\u00e9crivent $y=y_P+y_H$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-5519",
"position": 1,
"duration": 30,
"question": {
"id": "5519",
"question": "Expression des solutions de l'\u00e9quation $y'+ay=0$ o\u00f9 $a \\in \\mathbb{R}$",
"answer": "$y(x)=Ke^{-ax}$ o\u00f9 $K$ parcourt l'ensemble des r\u00e9els.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-5520",
"position": 2,
"duration": 30,
"question": {
"id": "5520",
"question": "Solution particuli\u00e8re de l'\u00e9quation $2y'+5y=3$ ?",
"answer": "$y(x)=\\dfrac{3}{5}$ bien s\u00fbr ! \n(on cherche une fonction constante, donc de d\u00e9riv\u00e9e nulle, qui v\u00e9rifie simplement 5y=3...)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-5521",
"position": 3,
"duration": 30,
"question": {
"id": "5521",
"question": "Sous quelle forme chercher une solution particuli\u00e8re de l'\u00e9quation $y'+3y=\\cos(2x)$ ?",
"answer": "Sous la forme $y_P=A\\cos(2x)+B\\sin(2x)$, $A$ et $B$ sont des r\u00e9els \u00e0 d\u00e9terminer. ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-5522",
"position": 4,
"duration": 30,
"question": {
"id": "5522",
"question": "Sous quelle forme chercher une solution particuli\u00e8re de l'\u00e9quation $y'+2y=3e^{2x}$ ?",
"answer": "Sous la forme $y_P=Ae^{2x}$, $A$ \u00e9tant un r\u00e9el \u00e0 d\u00e9terminer.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-5523",
"position": 5,
"duration": 30,
"question": {
"id": "5523",
"question": "Sous quelle forme chercher une solution particuli\u00e8re de l'\u00e9quation $y'+2y=3e^{-2x}$ ?",
"answer": "Attention pi\u00e8ge ! \nOn la cherche sous la forme $y_P=Axe^{-2x}$ , A r\u00e9el \u00e0 d\u00e9terminer.\n\n (en effet, toutes les fonctions $x\\mapsto Ae^{-2x}$ sont solutions de l'\u00e9quation homog\u00e8ne).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-3047",
"position": 6,
"duration": 30,
"question": {
"id": "3047",
"question": "Solutions $\\textbf{\u00e0 valeurs r\u00e9elles}$ de l'\u00e9quation diff\u00e9rentielle $ay^{\\prime\\prime}+by^\\prime+cy=0$, avec $a,b,c\\in\\mathbf{R}$, $a\\neq 0$.",
"answer": "On r\u00e9sout l'\u00e9quation $ar^2+br+c=0$.\nSi deux solutions r\u00e9elles $r_1$ et $r_2$, les solutions sont les fonctions $y(t)=\\lambda e^{r_1 t}+\\mu e^{r_2 t}$.\nSi une seule solution $r_0$, les solutions sont les fonctions $y(t)=(\\lambda + \\mu t)e^{r_0t}$.\nSi deux solutions complexes conjugu\u00e9es $\\gamma\\pm i\\omega$, les solutions sont les fonctions $y(t)=\\big(\\lambda \\cos(\\omega t)+\\mu\\sin(\\omega t)\\big)e^{\\gamma t}$.\n\n$\\lambda$ et $\\mu$ d\u00e9signent \u00e0 chaque fois des r\u00e9els.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1420-3050",
"position": 7,
"duration": 30,
"question": {
"id": "3050",
"question": "Quel type de solution particuli\u00e8re d'une \u00e9qua. diff du second ordre faut-il chercher pour un second membre de la forme $e^{\\alpha t}$ ?",
"answer": "Chercher sous la forme $y(t)=Ae^{\\alpha t}, A \\in \\mathbb{R}$, si $\\alpha$ n'est pas racine de l'\u00e9quation caract\u00e9ristique.\n\nChercher sous la forme $y(t)=Ate^{\\alpha t}$ si $\\alpha$ est racine simple de l'\u00e9quation caract\u00e9ristique, et sous la forme $y(t)=At^2e^{\\alpha t}$ si $\\alpha$ est racine double de l'\u00e9quation caract\u00e9ristique,  .",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1420-3052",
"position": 8,
"duration": 30,
"question": {
"id": "3052",
"question": "Quelle solution particuli\u00e8re pour un second membre de la forme $\\cos (\\alpha  t)$ ou $\\sin(\\alpha t)$ dans une \u00e9quation diff\u00e9rentielle d'ordre 2 ?",
"answer": "Chercher sous la forme $A\\cos(\\alpha t)+B\\sin(\\alpha t)$ dans la plupart des cas, sauf si $A\\cos(\\alpha t)+B\\sin(\\alpha t)$ est solution de l'\u00e9quation homog\u00e8ne.\nDans ce dernier cas chercher sous la forme $At\\cos(\\alpha t)+Bt\\sin(\\alpha t)$\n(A et B r\u00e9els)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1420-3053",
"position": 9,
"duration": 30,
"question": {
"id": "3053",
"question": "Quelle solution particuli\u00e8re pour un second membre de la forme $f(t)+g(t)$, avec $f$ et $g$ deux fonctions diff\u00e9rentes ?",
"answer": "Chercher une solution particuli\u00e8re pour le second membre $f(t)$ et une autre solution particuli\u00e8re pour le second membre $g(t)$, puis additionner les deux (principe de superposition).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1420-5524",
"position": 10,
"duration": 30,
"question": {
"id": "5524",
"question": "Sous quelle forme chercher une solution particuli\u00e8re de l'\u00e9quation $y^{\\prime \\prime}-3y'+2y=3e^x$",
"answer": "sous la forme $y_P=Ax e^x, A \\in \\mathbb{R}$ car la fonction $x \\mapsto e^x$ est solution de l'\u00e9quation homog\u00e8ne",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1421": {
"id": "1421",
"name": "G\u00e9om\u00e9trie espace (1)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1421\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "69",
"value": "Autre",
"field_id": "19",
"created_at": "2017-07-19 18:22:20",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 390,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-10",
"questions": [{
"id": "1421-5851",
"position": 0,
"duration": 30,
"question": {
"id": "5851",
"question": "Positions relatives de deux plans dans l'espace ?",
"answer": "Parall\u00e8les ou s\u00e9cants.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5852",
"position": 1,
"duration": 30,
"question": {
"id": "5852",
"question": "Positions relatives de deux droites dans l'espace ?",
"answer": "Elles sont s\u00e9cantes, parall\u00e8les ou non coplanaires.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5854",
"position": 2,
"duration": 30,
"question": {
"id": "5854",
"question": "Quelle est la nature de l'intersection de deux droites ?",
"answer": "Trois possibilit\u00e9s :\n* Un point (droites s\u00e9cantes)\n* l'ensemble vide (droites strictement parall\u00e8les ou non coplanaires)\n* une droite (droites confondues)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5855",
"position": 3,
"duration": 30,
"question": {
"id": "5855",
"question": "Quelle est la nature de l'intersection d'une droite et d'un plan ?",
"answer": "Trois possibilit\u00e9s :\n* Un point (droite et plans s\u00e9cants)\n* l'ensemble vide (droite strictement parall\u00e8le au plan)\n* la droite elle-m\u00eame (droite incluse dans le plan).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-3056",
"position": 4,
"duration": 30,
"question": {
"id": "3056",
"question": "D\u00e9finition du produit vectoriel.",
"answer": "$\\vec{u}\\wedge\\vec{v}$ est l'unique vecteur :\n- orthogonal \u00e0 $\\vec{u}$ et $\\vec{v}$\n- de norme $\\|u\\|\\times\\|\\vec{v}\\|\\times\\sin(\\widehat{\\vec{u},\\vec{v}})$\n- orient\u00e9 tel que $(\\vec{u},\\vec{v},\\vec{u}\\wedge\\vec{v})$ soit dans le sens direct (r\u00e8gle des 3 doigts de la main droite par exemple)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-3059",
"position": 5,
"duration": 30,
"question": {
"id": "3059",
"question": "Que signifie $\\det(\\vec{u},\\vec{v},\\vec{w})=0$ pour les vecteurs $\\vec{u},\\vec{v},\\vec{w}$ ?",
"answer": "$\\vec{u}$, $\\vec{v}$ et $\\vec{w}$ sont coplanaires.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-3066",
"position": 6,
"duration": 30,
"question": {
"id": "3066",
"question": "Forme g\u00e9n\u00e9rale d'une \u00e9quation cart\u00e9sienne d'un plan ?",
"answer": "$ax+by+cz+d=0$, avec $(a,b,c)\\neq(0,0,0)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-3068",
"position": 7,
"duration": 30,
"question": {
"id": "3068",
"question": "Forme g\u00e9n\u00e9rale d'un param\u00e9trage d'une droite de l'espace ?",
"answer": "$\\left\\lbrace\\begin{array}{l} {x=x_A+tx_u \\phantom{uv}} \\\\y=y_A+ty_u\\\\z=z_A+tz_u\\end{array}\\right.$, $\\quad t\\in\\mathbf{R}$,\no\u00f9 $A(x_A;y_A;z_A)$ est un point de la droite et $\\vec{u}\\left(\\begin{array}{c}x_u\\phantom{u}\\\\y_u \\phantom{a}\\\\z_u\\phantom{a} \\end{array}\\right)$ un vecteur directeur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5533",
"position": 8,
"duration": 30,
"question": {
"id": "5533",
"question": "M\u00e9thode pour calculer la distance d'un point M (coordonn\u00e9es connues) \u00e0 un plan P (\u00e9quation cart\u00e9sienne connue) ?",
"answer": "1. On calcule les coordonn\u00e9es de H, projet\u00e9 orthogonal de M sur P.\n2. On calcule MH",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5534",
"position": 9,
"duration": 30,
"question": {
"id": "5534",
"question": "Vrai ou faux : Deux droites de l'espace qui n'ont pas de point en commun sont non coplanaires.",
"answer": "Faux, elles peuvent \u00eatre strictement parall\u00e8les (et dans ce cas elles sont coplanaires).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5535",
"position": 10,
"duration": 30,
"question": {
"id": "5535",
"question": "Soit P un plan de vecteur normal $\\vec{n}$ et $d$ une droite de vecteur directeur $\\vec{u}$. Que dire de la position relative de $d$ et P lorsque $\\vec{u}$ et $\\vec{n}$ sont colin\u00e9aires ?",
"answer": "$d$ est perpendiculaire \u00e0 P.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5906",
"position": 11,
"duration": 30,
"question": {
"id": "5906",
"question": "Soit P un plan de vecteur normal $\\vec{n}$ et $d$ une droite de vecteur directeur $\\vec{u}$. Que dire de la position relative de $d$ et P lorsque $\\vec{u}$ et $\\vec{n}$ sont  orthogonaux ?",
"answer": "$d$ est parall\u00e8le \u00e0 P.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1421-5853",
"position": 12,
"duration": 30,
"question": {
"id": "5853",
"question": "Quelle est la nature de l'intersection de deux plans ?",
"answer": "Trois possibilit\u00e9s :\n* une droite (plans s\u00e9cants)\n* un plan (plans confondus)\n* l'ensemble vide (plans strctement parall\u00e8les)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1422": {
"id": "1422",
"name": "G\u00e9om\u00e9trie dans l'espace (2)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1422\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "69",
"value": "Autre",
"field_id": "19",
"created_at": "2017-07-19 18:22:20",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-12-17",
"questions": [{
"id": "1422-5629",
"position": 0,
"duration": 30,
"question": {
"id": "5629",
"question": "Forme g\u00e9n\u00e9rale d'une \u00e9quation cart\u00e9sienne de sph\u00e8re dont on conna\u00eet centre et rayon ?",
"answer": "$(x-x_\\Omega)^2+(y-y_\\Omega)^2+(z-z_\\Omega)^2=R^2$ \no\u00f9 R est le rayon  et   $\\Omega (x_\\Omega,y_\\Omega,z_\\Omega)$ le centre.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5631",
"position": 1,
"duration": 30,
"question": {
"id": "5631",
"question": "Quelle peut \u00eatre l'intersection d'une droite et d'une sph\u00e8re ?",
"answer": "Deux points, 1 point ou l'ensemble vide.  (tout d\u00e9pend de la distance entre le centre de la sph\u00e8re et la droite).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5853",
"position": 2,
"duration": 30,
"question": {
"id": "5853",
"question": "Quelle est la nature de l'intersection de deux plans ?",
"answer": "Trois possibilit\u00e9s :\n* une droite (plans s\u00e9cants)\n* un plan (plans confondus)\n* l'ensemble vide (plans strctement parall\u00e8les)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5854",
"position": 3,
"duration": 30,
"question": {
"id": "5854",
"question": "Quelle est la nature de l'intersection de deux droites ?",
"answer": "Trois possibilit\u00e9s :\n* Un point (droites s\u00e9cantes)\n* l'ensemble vide (droites strictement parall\u00e8les ou non coplanaires)\n* une droite (droites confondues)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5855",
"position": 4,
"duration": 30,
"question": {
"id": "5855",
"question": "Quelle est la nature de l'intersection d'une droite et d'un plan ?",
"answer": "Trois possibilit\u00e9s :\n* Un point (droite et plans s\u00e9cants)\n* l'ensemble vide (droite strictement parall\u00e8le au plan)\n* la droite elle-m\u00eame (droite incluse dans le plan).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-3060",
"position": 5,
"duration": 30,
"question": {
"id": "3060",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $\\det(\\vec{u},\\vec{v},\\vec{w})$.",
"answer": "Au signe pr\u00e8s, c'est le volume du parall\u00e9l\u00e9pip\u00e8de form\u00e9 par les vecteurs $\\vec{u}$, $\\vec{v}$ et $\\vec{w}$\n(c'est aussi 6 fois le volume du t\u00e9tra\u00e8dre form\u00e9 par les 3 vecteurs...)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-3064",
"position": 6,
"duration": 30,
"question": {
"id": "3064",
"question": "Calcul du produit vectoriel dans une base orthonorm\u00e9e directe.",
"answer": "$\\left(\\begin{array}{l}x_1 \\phantom{w}\\\\y_1\\\\z_1\\end{array}\\right)\\wedge\\left(\\begin{array}{l}x_2 \\phantom{w}\\\\y_2\\\\z_2\\end{array}\\right)=\\left(\\begin{array}{c}y_1z_2-y_2z_1 \\phantom{w}\\\\z_1x_2-z_2x_1\\\\x_1y_2-y_2x_1\\end{array}\\right)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-3063",
"position": 7,
"duration": 30,
"question": {
"id": "3063",
"question": "Calcul du produit scalaire dans une base orthonorm\u00e9e.",
"answer": "$\\left(\\begin{array}{c}x_1 \\phantom{i}\\\\y_1 \\\\z_1\\end{array}\\right)\\cdot\\left(\\begin{array}{c}x_2 \\phantom{w}\\\\y_2\\\\z_2\\end{array}\\right)=x_1x_2+y_1y_2+z_1z_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-3066",
"position": 8,
"duration": 30,
"question": {
"id": "3066",
"question": "Forme g\u00e9n\u00e9rale d'une \u00e9quation cart\u00e9sienne d'un plan ?",
"answer": "$ax+by+cz+d=0$, avec $(a,b,c)\\neq(0,0,0)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-3068",
"position": 9,
"duration": 30,
"question": {
"id": "3068",
"question": "Forme g\u00e9n\u00e9rale d'un param\u00e9trage d'une droite de l'espace ?",
"answer": "$\\left\\lbrace\\begin{array}{l} {x=x_A+tx_u \\phantom{uv}} \\\\y=y_A+ty_u\\\\z=z_A+tz_u\\end{array}\\right.$, $\\quad t\\in\\mathbf{R}$,\no\u00f9 $A(x_A;y_A;z_A)$ est un point de la droite et $\\vec{u}\\left(\\begin{array}{c}x_u\\phantom{u}\\\\y_u \\phantom{a}\\\\z_u\\phantom{a} \\end{array}\\right)$ un vecteur directeur.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5906",
"position": 10,
"duration": 30,
"question": {
"id": "5906",
"question": "Soit P un plan de vecteur normal $\\vec{n}$ et $d$ une droite de vecteur directeur $\\vec{u}$. Que dire de la position relative de $d$ et P lorsque $\\vec{u}$ et $\\vec{n}$ sont  orthogonaux ?",
"answer": "$d$ est parall\u00e8le \u00e0 P.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1422-5535",
"position": 11,
"duration": 30,
"question": {
"id": "5535",
"question": "Soit P un plan de vecteur normal $\\vec{n}$ et $d$ une droite de vecteur directeur $\\vec{u}$. Que dire de la position relative de $d$ et P lorsque $\\vec{u}$ et $\\vec{n}$ sont colin\u00e9aires ?",
"answer": "$d$ est perpendiculaire \u00e0 P.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "69",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1423": {
"id": "1423",
"name": "Suites num\u00e9riques (1)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1423\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-01-28",
"questions": [{
"id": "1423-3106",
"position": 0,
"duration": 30,
"question": {
"id": "3106",
"question": "D\u00e9finition par r\u00e9currence d'une suite arithm\u00e9tique :\n $(u_n)_{n\\in\\mathbf{N}}$ est arithm\u00e9tique si...",
"answer": "... il existe $r\\in\\mathbb{R}$ tel que, pour tout $n\\in\\mathbb{N}$, $u_{n+1}=u_n+r$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3107",
"position": 1,
"duration": 30,
"question": {
"id": "3107",
"question": "D\u00e9finition par r\u00e9currence d'une suite g\u00e9om\u00e9trique :\n$(u_n)_{n\\in\\mathbf{N}}$ est g\u00e9om\u00e9trique si...",
"answer": "... il existe $q\\in\\mathbb{R}$ tel que, pour tout $n\\in\\mathbb{N}$, $u_{n+1}=q\\times u_n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3112",
"position": 2,
"duration": 30,
"question": {
"id": "3112",
"question": "Soit $(u_n)_{n\\in\\mathbb{N}}$ une suite arithm\u00e9tique de raison $r$. Soit $n\\in\\mathbb{N}$. Exprimer $u_n$ en fonction de $u_0$, $n$ et $r$.",
"answer": "$u_n=u_0+nr$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3113",
"position": 3,
"duration": 30,
"question": {
"id": "3113",
"question": "Soit $(u_n)_{n\\in\\mathbb{N}}$ une suite g\u00e9om\u00e9trique de raison $q$. Soit $n\\in\\mathbb{N}$. Exprimer $u_n$ en fonction de $u_0$, $n$ et $q$.",
"answer": "$u_n=u_0 .q^n $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3114",
"position": 4,
"duration": 30,
"question": {
"id": "3114",
"question": "Une suite $(u_n)_{n\\in\\mathbf{N}}$ est croissante si...",
"answer": "$\\forall n\\in\\mathbb{N}$, $u_{n+1}\\geq u_n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3115",
"position": 5,
"duration": 30,
"question": {
"id": "3115",
"question": "Une suite $(u_n)_{n\\in\\mathbf{N}}$ est strictement d\u00e9croissante si...",
"answer": "$\\forall n\\in\\mathbb{N}$, $u_{n+1}<u_n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3116",
"position": 6,
"duration": 30,
"question": {
"id": "3116",
"question": "Une suite $(u_n)_{n\\in\\mathbf{N}}$ est major\u00e9e si...",
"answer": "$\\exists M\\in\\mathbb{R} \\quad$ $\\forall n\\in\\mathbb{N} \\quad$ $u_n\\leq M$.\n(M est alors un majorant de la suite.)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3117",
"position": 7,
"duration": 30,
"question": {
"id": "3117",
"question": "Une suite $(u_n)_{n\\in\\mathbf{N}}$ est minor\u00e9e si...",
"answer": "$\\exists m\\in\\mathbb{R} \\quad$ $\\forall n\\in\\mathbb{N} \\quad$ $u_n\\geq m$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3118",
"position": 8,
"duration": 30,
"question": {
"id": "3118",
"question": "Une suite $(u_n)_{n\\in\\mathbf{N}}$ est born\u00e9e si...",
"answer": "... elle est major\u00e9e et minor\u00e9e. Autrement dit, \n\n$\\exists (m,M)\\in\\mathbf{R}^2 \\quad \\forall n\\in\\mathbf{N} \\quad m\\leq u_n\\leq M$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3108",
"position": 9,
"duration": 30,
"question": {
"id": "3108",
"question": "Comment reconna\u00eetre une suite arithm\u00e9tique ?",
"answer": "Fixer $n\\in\\mathbf{N}$, calculer $u_{n+1}-u_n$ et v\u00e9rifier que le r\u00e9sultat est ind\u00e9pendant de $n$, ou alors reconna\u00eetre la d\u00e9finition explicite $u_n=u_0+nr$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1423-3109",
"position": 10,
"duration": 30,
"question": {
"id": "3109",
"question": "Comment reconna\u00eetre une suite g\u00e9om\u00e9trique ?",
"answer": "Fixer $n\\in\\mathbf{N}$, calculer $\\frac{u_{n+1}}{u_n}$ et v\u00e9rifier que le r\u00e9sultat est ind\u00e9pendant de $n$, ou alors reconnaitre la d\u00e9finition explicite $u_n=u_0\\times q^n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1424": {
"id": "1424",
"name": "Suites num\u00e9riques (2)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1424\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-04",
"questions": [{
"id": "1424-3121",
"position": 0,
"duration": 30,
"question": {
"id": "3121",
"question": "Quelle est la d\u00e9finition de \" $(u_n)_{n\\in\\mathbf{N}}$ converge vers $\\ell\\in\\mathbf{R}$ \" ?",
"answer": " pour tout $\\varepsilon>0$, il existe $N\\in\\mathbb{N}$ tel que, pour tout $n\\geq N$, $|u_n-\\ell|\\leq \\varepsilon$.\nou encore $\\forall \\varepsilon>0 \\quad  \\exists N \\in \\mathbb{N} \\quad\\forall n\\geq N \\quad|u_n-\\ell| \\leq \\varepsilon$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3122",
"position": 1,
"duration": 30,
"question": {
"id": "3122",
"question": "Quelle est la d\u00e9finition de \" $(u_n)_{n\\in\\mathbf{N}}$ diverge vers $+\\infty$ \" ?",
"answer": " pour tout $M\\in\\mathbb{R}$, il existe $N\\in\\mathbb{N}$ tel que, pour tout $n\\geq N$, $u_n\\geq M$.\nou encore  $\\forall M \\in \\mathbb{R} \\quad  \\exists N \\in \\mathbb{N} \\quad\\forall n\\geq N \\quad u_n \\geq M$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3123",
"position": 2,
"duration": 30,
"question": {
"id": "3123",
"question": "Que peut-on dire des suites extraites d'une suite convergente ?",
"answer": "Toutes les suites extraites d'une suite convergente sont convergentes, de m\u00eame limite que la suite de d\u00e9part.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3124",
"position": 3,
"duration": 30,
"question": {
"id": "3124",
"question": "Comment montrer qu'une suite n'a pas de limite ?",
"answer": "Extraire deux sous-suites qui convergent vers deux limites diff\u00e9rentes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3125",
"position": 4,
"duration": 30,
"question": {
"id": "3125",
"question": "Compl\u00e9ter avec $\\Leftarrow$, $\\Rightarrow$ ou $\\iff$:\n$(u_n)_{n\\in\\mathbf{N}}$ born\u00e9e $\\dots$ $(u_n)_{n\\in\\mathbf{N}}$ convergente.",
"answer": "$(u_n)_{n\\in\\mathbf{N}}$ born\u00e9e $\\Leftarrow$ $(u_n)_{n\\in\\mathbf{N}}$ convergente.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3126",
"position": 5,
"duration": 30,
"question": {
"id": "3126",
"question": "Consid\u00e9rons deux suites $(u_n)_{n\\in\\mathbf{N}}$ et $(v_n)_{n\\in\\mathbf{N}}$ qui convergent respectivement vers $\\ell_1$ et $\\ell_2$. On suppose que, pour tout $n\\in\\mathbf{N}$, $u_n<v_n$. Que dire de $\\ell_1$ et $\\ell_2$ ?",
"answer": "On peut dire que $\\ell_1\\leq\\ell_2$ (mais on n'a pas n\u00e9cessairement $\\ell_1<\\ell_2$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3128",
"position": 6,
"duration": 30,
"question": {
"id": "3128",
"question": "Que dire de la convergence d'une suite  $(u_n)_{n\\in\\mathbf{N}}$ g\u00e9om\u00e9trique de raison $q$ ?",
"answer": "La suite $(u_n)_{n\\in\\mathbf{N}}$ converge vers $0$ si et seulement si $|q|<1$, elle est constante (donc convergente vers $u_0$) si et seulement si $q=1$, elle est divergente pour toutes les autres valeurs de $q$ (sauf si $u_0=0$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3129",
"position": 7,
"duration": 30,
"question": {
"id": "3129",
"question": "Soit $(u_n)_{n\\in\\mathbf{N}}$ une suite de r\u00e9els non nuls. \u00c0 quelles conditions la suite $(1\/u_n)_{n\\in\\mathbf{N}}$ diverge-t-elle vers $+\\infty$ ?",
"answer": "La suite $(1\/u_n)_{n\\in\\mathbf{N}}$ diverge vers $+\\infty$ si $(u_n)_{n\\in\\mathbf{N}}$ converge vers $0$ et que $u_n>0$ \u00e0 partir d'un certain rang $N$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3130",
"position": 8,
"duration": 30,
"question": {
"id": "3130",
"question": "Qu'est-ce qu'une suite divergente ? Quels sont les diff\u00e9rents comportements possibles d'une suite divergente ?",
"answer": "C'est une suite qui ne converge pas, autrement dit qui ne poss\u00e8de pas de limite finie. Elle peut poss\u00e9der une limite infinie ($+\\infty$ ou $-\\infty$), ou pas de limite du tout.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3133",
"position": 9,
"duration": 30,
"question": {
"id": "3133",
"question": "Citer le th\u00e9or\u00e8me de convergence monotone.",
"answer": "Si une suite est croissante et major\u00e9e, alors elle converge.\nSi une suite est d\u00e9croissante et minor\u00e9e, alors elle converge.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-5386",
"position": 10,
"duration": 30,
"question": {
"id": "5386",
"question": "Que dire d'une suite croissante non major\u00e9e ?",
"answer": "Elle diverge vers $+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1424-3131",
"position": 11,
"duration": 30,
"question": {
"id": "3131",
"question": "Citer le th\u00e9or\u00e8me d'encadrement (cas d'une limite finie).",
"answer": "Soient $(u_n)_{n\\in\\mathbf{N}}$, $(v_n)_{n\\in\\mathbf{N}}$ et $(w_n)_{n\\in\\mathbf{N}}$ trois suites r\u00e9elles.\nOn suppose que $(u_n)_{n\\in\\mathbf{N}}$ et $(w_n)_{n\\in\\mathbf{N}}$ convergent une m\u00eame limite $\\ell\\in\\mathbf{R}$.\nOn suppose de plus que, pour tout $n\\in\\mathbf{N}$, $u_n\\leq v_n\\leq w_n$.\nAlors la suite $(v_n)_{n\\in\\mathbf{N}}$ est convergente, de limite $\\ell$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1425": {
"id": "1425",
"name": "suites num\u00e9riques (bilan)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1425\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "496",
"value": "Alg\u00e8bre lin\u00e9aire",
"field_id": "19",
"created_at": "2020-02-07 08:54:02",
"updated_at": "2020-02-07 08:54:02",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 510,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2025-02-11",
"questions": [{
"id": "1425-3123",
"position": 0,
"duration": 30,
"question": {
"id": "3123",
"question": "Que peut-on dire des suites extraites d'une suite convergente ?",
"answer": "Toutes les suites extraites d'une suite convergente sont convergentes, de m\u00eame limite que la suite de d\u00e9part.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3124",
"position": 1,
"duration": 30,
"question": {
"id": "3124",
"question": "Comment montrer qu'une suite n'a pas de limite ?",
"answer": "Extraire deux sous-suites qui convergent vers deux limites diff\u00e9rentes.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3128",
"position": 2,
"duration": 30,
"question": {
"id": "3128",
"question": "Que dire de la convergence d'une suite  $(u_n)_{n\\in\\mathbf{N}}$ g\u00e9om\u00e9trique de raison $q$ ?",
"answer": "La suite $(u_n)_{n\\in\\mathbf{N}}$ converge vers $0$ si et seulement si $|q|<1$, elle est constante (donc convergente vers $u_0$) si et seulement si $q=1$, elle est divergente pour toutes les autres valeurs de $q$ (sauf si $u_0=0$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3129",
"position": 3,
"duration": 30,
"question": {
"id": "3129",
"question": "Soit $(u_n)_{n\\in\\mathbf{N}}$ une suite de r\u00e9els non nuls. \u00c0 quelles conditions la suite $(1\/u_n)_{n\\in\\mathbf{N}}$ diverge-t-elle vers $+\\infty$ ?",
"answer": "La suite $(1\/u_n)_{n\\in\\mathbf{N}}$ diverge vers $+\\infty$ si $(u_n)_{n\\in\\mathbf{N}}$ converge vers $0$ et que $u_n>0$ \u00e0 partir d'un certain rang $N$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3130",
"position": 4,
"duration": 30,
"question": {
"id": "3130",
"question": "Qu'est-ce qu'une suite divergente ? Quels sont les diff\u00e9rents comportements possibles d'une suite divergente ?",
"answer": "C'est une suite qui ne converge pas, autrement dit qui ne poss\u00e8de pas de limite finie. Elle peut poss\u00e9der une limite infinie ($+\\infty$ ou $-\\infty$), ou pas de limite du tout.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-5403",
"position": 5,
"duration": 30,
"question": {
"id": "5403",
"question": "Que signifie math\u00e9matiquement $u_n=o(v_n)$ ?",
"answer": "Cela revient \u00e0 dire (si $v_n$ ne s'annule pas) que $\\dfrac{u_n}{v_n} \\underset{n \\to \\infty}{\\longrightarrow } 0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-5404",
"position": 6,
"duration": 30,
"question": {
"id": "5404",
"question": "Que signifie math\u00e9matiquement $u_n \\sim v_n$ ?",
"answer": "Cela revient \u00e0 dire (si $v_n$ ne s'annule pas) que $\\dfrac{u_n}{v_n} \\underset{n \\to \\infty}{\\longrightarrow } 1$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "496",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-5876",
"position": 7,
"duration": 30,
"question": {
"id": "5876",
"question": "Donner un \u00e9quivalent de $u_n= \\dfrac{1}{\\ln n}+\\dfrac{2}{3^n}+\\dfrac{1}{n^4}$ lorsque $n \\to +\\infty$.",
"answer": "$\\dfrac{1}{\\ln n}$.\nEn effet, on peut v\u00e9rifier par croissance compar\u00e9e que les 2 autres termes de la somme sont n\u00e9gligeables devant celui-ci.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3134",
"position": 8,
"duration": 30,
"question": {
"id": "3134",
"question": "Deux suites $(u_n)_{n\\in\\mathbf{N}}$ et $(v_n)_{n\\in\\mathbf{N}}$ sont dites adjacentes si...",
"answer": "... $(u_n)_{n\\in\\mathbf{N}}$ est croissante, $(v_n)_{n\\in\\mathbf{N}}$ est d\u00e9croissante, et $\\displaystyle\\lim_{n\\to+\\infty}(u_n-v_n)=0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-5386",
"position": 9,
"duration": 30,
"question": {
"id": "5386",
"question": "Que dire d'une suite croissante non major\u00e9e ?",
"answer": "Elle diverge vers $+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3133",
"position": 10,
"duration": 30,
"question": {
"id": "3133",
"question": "Citer le th\u00e9or\u00e8me de convergence monotone.",
"answer": "Si une suite est croissante et major\u00e9e, alors elle converge.\nSi une suite est d\u00e9croissante et minor\u00e9e, alors elle converge.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3126",
"position": 11,
"duration": 30,
"question": {
"id": "3126",
"question": "Consid\u00e9rons deux suites $(u_n)_{n\\in\\mathbf{N}}$ et $(v_n)_{n\\in\\mathbf{N}}$ qui convergent respectivement vers $\\ell_1$ et $\\ell_2$. On suppose que, pour tout $n\\in\\mathbf{N}$, $u_n<v_n$. Que dire de $\\ell_1$ et $\\ell_2$ ?",
"answer": "On peut dire que $\\ell_1\\leq\\ell_2$ (mais on n'a pas n\u00e9cessairement $\\ell_1<\\ell_2$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3135",
"position": 12,
"duration": 30,
"question": {
"id": "3135",
"question": "Si deux suites sont adjacentes, que peut-on dire de leur convergence ?",
"answer": "Deux suites adjacentes sont convergentes et poss\u00e8dent la m\u00eame limite.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3111",
"position": 13,
"duration": 30,
"question": {
"id": "3111",
"question": "Somme des termes d'une suite g\u00e9om\u00e9trique $(u_n)_{n\\in\\mathbf{N}}$.",
"answer": "Notons $q$ la raison de la suite. Alors\n$\\displaystyle\\sum_{k=0}^n u_k=\\left\\{\\begin{array}{ll} u_0 \\times \\dfrac{1-q^{n+1}}{1-q} & \\text{si }q\\neq1 \\\\ \\phantom{\\dfrac{aa}{aa}} (n+1)u_0 \\phantom{aaa}& \\text{si } q=1  \\end{array}\\right.$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3110",
"position": 14,
"duration": 30,
"question": {
"id": "3110",
"question": "Somme des termes d'une suite arithm\u00e9tique $(u_n)_{n\\in\\mathbf{N}}$.",
"answer": "$\\displaystyle\\sum_{k=0}^n u_k=(n+1)\\frac{u_0+u_n}{2}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3131",
"position": 15,
"duration": 30,
"question": {
"id": "3131",
"question": "Citer le th\u00e9or\u00e8me d'encadrement (cas d'une limite finie).",
"answer": "Soient $(u_n)_{n\\in\\mathbf{N}}$, $(v_n)_{n\\in\\mathbf{N}}$ et $(w_n)_{n\\in\\mathbf{N}}$ trois suites r\u00e9elles.\nOn suppose que $(u_n)_{n\\in\\mathbf{N}}$ et $(w_n)_{n\\in\\mathbf{N}}$ convergent une m\u00eame limite $\\ell\\in\\mathbf{R}$.\nOn suppose de plus que, pour tout $n\\in\\mathbf{N}$, $u_n\\leq v_n\\leq w_n$.\nAlors la suite $(v_n)_{n\\in\\mathbf{N}}$ est convergente, de limite $\\ell$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1425-3132",
"position": 16,
"duration": 30,
"question": {
"id": "3132",
"question": "Citer le th\u00e9or\u00e8me d'encadrement (cas o\u00f9 la limite est $+\\infty$).",
"answer": "Soient $(u_n)_{n\\in\\mathbf{N}}$ et $(v_n)_{n\\in\\mathbf{N}}$ deux suites r\u00e9elles.\nOn suppose que $(u_n)_{n\\in\\mathbf{N}}$ diverge vers $+\\infty$.\nOn suppose de plus que, pour tout $n\\in\\mathbf{N}$, $u_n\\leq v_n$.\nAlors la suite $(v_n)_{n\\in\\mathbf{N}}$ diverge vers $+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1392": {
"id": "1392",
"name": "DC6_2",
"user_id": "1160",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1392\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "18",
"value": "Cin\u00e9matique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2025-03-09",
"questions": [{
"id": "1392-5879",
"position": 0,
"duration": 30,
"question": {
"id": "5879",
"question": "Indiquer le nom des \u00e9l\u00e9ments de ce train d'engrenages \u00e9picyclo\u00efdal.",
"answer": "3 : couronne ou grand plan\u00e9taire ou plan\u00e9taire ext\u00e9rieur\n2a et 2b : satellite\n4 : porte-satellites\n1 : plan\u00e9taire int\u00e9rieur ou petit plan\u00e9taire",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/11edc2e0-bcc4-11ed-a0aa-f95e968ceca9",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5880",
"position": 1,
"duration": 30,
"question": {
"id": "5880",
"question": "Indiquer le nom des \u00e9l\u00e9ments de ce train d'engrenages \u00e9picyclo\u00efdal.",
"answer": "1 : couronne ou grand plan\u00e9taire ou plan\u00e9taire ext\u00e9rieur\n4 : satellite\n3 : porte-satellites\n2 : plan\u00e9taire int\u00e9rieur ou petit plan\u00e9taire",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/00b133f0-bcc5-11ed-9181-b1b700979fd6",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5881",
"position": 2,
"duration": 30,
"question": {
"id": "5881",
"question": "Indiquer la relation existant entre les vitesses des \u00e9l\u00e9ments par rapport au b\u00e2ti not\u00e9 0.",
"answer": "\n${\\omega_{30}-\\omega_{40} \\over \\omega_{10}-\\omega_{40}}=-{Z_1\\over Z_3}$\n\n",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/6ff874b0-bcc5-11ed-8b4a-035b811a289a",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5911",
"position": 3,
"duration": 30,
"question": {
"id": "5911",
"question": "exprimer le rapport de vitesse entr\u00e9e\/sortie $\\frac{\\omega_{1\/0}}{\\omega_{3\/0}}$ si le mouvement du porte-satellite 4 est bloqu\u00e9.",
"answer": "Satellite 2\nPorte satellite 4\nPlan\u00e9taire2 3\nPlan\u00e9taire1 1\n\n $\\frac{\\omega_{1\/0}}{\\omega_{3\/0}}=-\\frac{Z_3}{Z_1}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/fad19a50-3354-11e8-a63c-af5417ba9720",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1392-5912",
"position": 4,
"duration": 30,
"question": {
"id": "5912",
"question": "exprimer le rapport de vitesse entr\u00e9e\/sortie $\\frac{\\omega_{4\/0}}{\\omega_{1\/0}}$ si le mouvement de la couronne 3 est bloqu\u00e9e.",
"answer": "Satellite 2\nPorte satellite 4\nPlan\u00e9taire2 3\nPlan\u00e9taire1 1\n\n $\\frac{\\omega_{4\/0}}{\\omega_{1\/0}}=\\frac{Z_1}{Z_1+Z_3}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f86412e0-df1a-11ee-b595-87d49ed1fbc5",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1392-5914",
"position": 5,
"duration": 30,
"question": {
"id": "5914",
"question": "Indiquer le nom des composants sur le sch\u00e9ma. Quelle est la particularit\u00e9 du satellite ?",
"answer": "bleu : plan\u00e9taire 1\nrouge : satellite, il s'agit d'un pignon double\njaune : porte satellite\nvert : plan\u00e9taire 2",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/48e80030-df1c-11ee-ba5b-3db0290fe28d",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5915",
"position": 6,
"duration": 30,
"question": {
"id": "5915",
"question": "exprimer le rapport de vitesse entr\u00e9e\/sortie $\\frac{\\omega_{3\/0}}{\\omega_{1\/0}}$ si le mouvement du porte-satellite 4 est bloqu\u00e9.",
"answer": "Satellite 2a et 2b\nPorte satellite 4\nPlan\u00e9taire2 3\nPlan\u00e9taire1 1\n\n $\\frac{\\omega_{3\/0}}{\\omega_{1\/0}}=\\frac{Z_1.Z_2b}{Z_3.Z_2a}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/65d70140-df1d-11ee-a1e9-33ee393de47e",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5916",
"position": 7,
"duration": 30,
"question": {
"id": "5916",
"question": "exprimer le rapport de vitesse entr\u00e9e\/sortie $\\frac{\\omega_{3\/0}}{\\omega_{1\/0}}$ si le mouvement du porte-satellite 4 est bloqu\u00e9.",
"answer": "Satellite 2a et 2b\nPorte satellite 4\nPlan\u00e9taire2 3\nPlan\u00e9taire1 1\n\n $\\frac{\\omega_{3\/0}}{\\omega_{1\/0}}=\\frac{Z_1.Z_2b}{Z_3.Z_2a}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/e49cd0e0-df1d-11ee-803f-e3151c7530ba",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5917",
"position": 8,
"duration": 30,
"question": {
"id": "5917",
"question": "Dans une automobile, \u00e0 quoi sert un diff\u00e9rentiel ?",
"answer": "Un diff\u00e9rentiel est un train \u00e9picyclo\u00efdal permettant de transmettre la puissance de l'arbre moteur aux deux roues de l'essieu moteur. La structure autorise des vitesses de roues droite et gauche diff\u00e9rente.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/907b92e0-df1e-11ee-ab3a-d7c0fc48d2f1",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1392-5918",
"position": 9,
"duration": 30,
"question": {
"id": "5918",
"question": "Indiquer dans les carr\u00e9s le nom des composants de ce diff\u00e9rentiel automobile. Indiquer \u00e9galement \u00e0 quelle pi\u00e8ce est reli\u00e9 chaque \u00e9l\u00e9ment.",
"answer": "rouge : porte-satellite (li\u00e9 \u00e0 l'arbre moteur)\nvert : plan\u00e9taire 1 (li\u00e9 \u00e0 la roue droite)\nbleu : plan\u00e9taire 2 (li\u00e9 \u00e0 la roue gauche)\norange : satellites (libres) \n",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/17fd0d90-df1f-11ee-b385-a7b0c9916fa4",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "147",
"name": "TSI1",
"schoolyear": "2022-2023"
}, {
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1427": {
"id": "1427",
"name": "Espaces vectoriels (d\u00e9but)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1427\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "53",
"value": "Alg\u00e8bre",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 3,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-04-01",
"questions": [{
"id": "1427-3163",
"position": 0,
"duration": 30,
"question": {
"id": "3163",
"question": "D\u00e9finition d'un sous-espace vectoriel de E.",
"answer": "C'est une partie $F$ d'un $\\mathbf{R}$-espace vectoriel $E$ telle que :\n-- $0_E\\in F$;\n-- pour tous $u,v\\in F$ et pour tout $\\lambda \\in\\mathbf{R}$, $\\lambda u + v\\in F$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-3164",
"position": 1,
"duration": 30,
"question": {
"id": "3164",
"question": "L'intersection (resp. l'union) de deux sous-espaces vectoriels est-elle un sous-espace vectoriel ?",
"answer": "Oui pour l'intersection, non en g\u00e9n\u00e9ral pour l'union.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-3165",
"position": 2,
"duration": 30,
"question": {
"id": "3165",
"question": "D\u00e9finition de la somme de deux sous-espaces vectoriels.",
"answer": "$F+G=\\{u+v\\mid u\\in F,\\ v\\in G\\}$.\n\nC'est le plus petit sous-espace vectoriel contenant $F\\cup G$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-3166",
"position": 3,
"duration": 30,
"question": {
"id": "3166",
"question": "D\u00e9finition et caract\u00e9risation de deux sous-espaces vectoriels en somme directe.",
"answer": "D\u00e9finition : Les espaces $F$ et $G$ sont en somme directe si, pour tout $w\\in F+G$, il existe un unique couple $(f,g)\\in F\\times G$ tel que $w=f+g$.\n\nCaract\u00e9risation : $F$ et $G$ sont en somme directe si et seulement si $F\\cap G =\\{0\\}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-3167",
"position": 4,
"duration": 30,
"question": {
"id": "3167",
"question": "D\u00e9finition de deux sous-espaces vectoriels suppl\u00e9mentaires.",
"answer": "$F$ et $G$ sont suppl\u00e9mentaires dans $E$ si $F\\oplus G= E$. Autrement dit, si $F$ et $G$ sont en somme directe et $F+G=E$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-5706",
"position": 5,
"duration": 30,
"question": {
"id": "5706",
"question": "Quelles sont les racines complexes de $X^n-1$ ?",
"answer": "L'ensemble des racines n-i\u00e8mes de l'unit\u00e9, c'est-\u00e0-dire les $e^{i \\frac{2k\\pi}{n}}$ o\u00f9 $k$ est un entier.\n\n (il suffit de se limiter aux entiers entre 0 et $n-1$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-5924",
"position": 6,
"duration": 30,
"question": {
"id": "5924",
"question": "Quelles sont les racines complexes de $X^n+1$ ?",
"answer": "L'ensemble des racines n-i\u00e8mes de $-1$, c'est-\u00e0-dire les $e^{i \\left(\\frac{\\pi}{n}+\\frac{2k\\pi}{n}\\right)}$ o\u00f9 $k$ est un entier.\n\n (il suffit de se limiter aux entiers entre 0 et $n-1$)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1427-3168",
"position": 7,
"duration": 30,
"question": {
"id": "3168",
"question": "D\u00e9finition de l'espace vectoriel engendr\u00e9 par une famille de vecteurs.",
"answer": "$\\mathrm{Vect}(u_1,\\dots,u_n)=\\{\\lambda_1u_1+\\cdots+\\lambda_nu_n,\\quad \\lambda_1,\\dots,\\lambda_n\\in\\mathbf{R}\\}$.\n\nC'est le plus petit sous-espace vectoriel contenant les vecteurs $u_1,\\dots,u_n$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-3169",
"position": 8,
"duration": 30,
"question": {
"id": "3169",
"question": "D\u00e9finition de $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$ est g\u00e9n\u00e9ratrice de E ?",
"answer": "Tout vecteur $\\vec{X}$ de E peut s'\u00e9crire comme combiniaison lin\u00e9aire des vecteurs $(\\vec{u_1}, \\vec{u_2},...,\\vec{u_p})$, autrement dit il existe $p$ r\u00e9els  $\\lambda_1,\\dots,\\lambda_p$ tels que $\\vec{X}=\\lambda_1 \\vec{u_1}+\\lambda_2 \\vec{u_2}+...+\\lambda_p \\vec{u_p}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1427-5380",
"position": 9,
"duration": 30,
"question": {
"id": "5380",
"question": "D\u00e9finition d'une famille libre d'un espace vectoriel E",
"answer": " $(\\vec{v_1}, \\vec{v_2},...,\\vec{v_p})$ est libre si :\n$(\\lambda_1 \\vec{v_1}+\\lambda_2 \\vec{v_2}+...+\\lambda_p \\vec{v_p}=\\vec{0})$ impose $(\\lambda_1=\\lambda_2=...=\\lambda_p=0)$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "53",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "150",
"name": "TSI1",
"schoolyear": "2023-2024"
}, {
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1428": {
"id": "1428",
"name": "Techniques de calcul",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1428\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-01",
"questions": [{
"id": "1428-2899",
"position": 0,
"duration": 30,
"question": {
"id": "2899",
"question": "\\[\\sum_{k=0}^n k=\\,?\\]",
"answer": "\\[\\frac{n(n+1)}{2}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2900",
"position": 1,
"duration": 30,
"question": {
"id": "2900",
"question": "\\[\\sum_{k=0}^nq^k=\\,?\\]",
"answer": "\\[\\frac{1-q^{n+1}}{1-q}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2901",
"position": 2,
"duration": 30,
"question": {
"id": "2901",
"question": "D\u00e9finition de $n!$.",
"answer": "\\[n!=1\\times2\\times\\cdots\\times n=\\prod_{k=1}^n k\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-5835",
"position": 3,
"duration": 30,
"question": {
"id": "5835",
"question": "Soit $u$ une fonction d\u00e9rivable et qui ne s'annule pas sur un intervalle I. Donner une primitive de la fonction $\\dfrac{u'}{u}$",
"answer": "$\\ln |u|$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-5364",
"position": 4,
"duration": 30,
"question": {
"id": "5364",
"question": "$u$ \u00e9tant une fonction d\u00e9rivable sur $\\mathbb{R}$, donner une primitive de $u' u^n$ lorsque $n \\neq -1$",
"answer": "$\\dfrac{1}{n+1} u^{n+1}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2882",
"position": 5,
"duration": 30,
"question": {
"id": "2882",
"question": "Si $\\lim\\limits_{x\\to+\\infty} u(x)=\\lim\\limits_{x\\to+\\infty}v(x)=+\\infty$, que peut-on dire des limites en $+\\infty$ de $u+v$, $u-v$, $uv$, $\\frac{u}{v}$ ?",
"answer": "$\\lim\\limits_{x\\to+\\infty}(u(x)+v(x))=\\lim\\limits_{x\\to+\\infty}(u(x)\\times v(x))=+\\infty$. Les limites de $u-v$ et $\\frac{u}{v}$ sont ind\u00e9termin\u00e9es.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-4915",
"position": 6,
"duration": 30,
"question": {
"id": "4915",
"question": "Soit $a$ un r\u00e9el. Si $\\lim\\limits_{x\\to a} u(x) =+\\infty$ et $\\lim\\limits_{x\\to a} v(x) =-\\infty$, que dire des limites en $a$ de $u+v , \\quad u \\times v , \\quad \\frac{u}{v}$ ?",
"answer": "le produit a pour limite $-\\infty$, les 2 autres limites sont ind\u00e9termin\u00e9es.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-5836",
"position": 7,
"duration": 30,
"question": {
"id": "5836",
"question": "Soit $a$ un r\u00e9el. Si $\\lim\\limits_{x\\to a} u(x) =0^{-}$ et $\\lim\\limits_{x\\to a} v(x) =-\\infty$, que dire des limites en $a$ de $\\dfrac{v}{u} , \\quad  \\dfrac{u}{v} $ ?",
"answer": "$\\lim\\limits_{x\\to a} \\dfrac{v(x)}{u(x)} = +\\infty$ et $\\lim\\limits_{x\\to a} \\dfrac{u(x)}{v(x)} = 0$  ",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2890",
"position": 8,
"duration": 30,
"question": {
"id": "2890",
"question": "\\[\\lim_{x\\to+\\infty}\\frac{x}{\\ln x}=?\\]",
"answer": "$+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2887",
"position": 9,
"duration": 30,
"question": {
"id": "2887",
"question": "\\[\\lim_{x\\to 0}x\\ln x=?\\]",
"answer": "$0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2888",
"position": 10,
"duration": 30,
"question": {
"id": "2888",
"question": "\\[\\lim_{x\\to +\\infty}\\frac{e^x}{x}=?\\]",
"answer": "$+\\infty$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1428-2889",
"position": 11,
"duration": 30,
"question": {
"id": "2889",
"question": "\\[\\lim_{x\\to-\\infty}xe^x=?\\]",
"answer": "$0$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1431": {
"id": "1431",
"name": "G\u00e9n\u00e9ralit\u00e9s sur les fonctions",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1431\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-10-08",
"questions": [{
"id": "1431-2972",
"position": 0,
"duration": 30,
"question": {
"id": "2972",
"question": "\u00c0 quelle condition une fonction $f\\colon I\\to J$ poss\u00e8de-t-elle une r\u00e9ciproque ?",
"answer": "Si et seulement si tout \u00e9l\u00e9ment de $J$ poss\u00e8de un unique ant\u00e9c\u00e9dent par $f$ (on dit alors que $f$ est bijective de $I$ sur $J$).",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1431-2973",
"position": 1,
"duration": 30,
"question": {
"id": "2973",
"question": "$f\\colon I\\to\\mathbf{R}$ major\u00e9e $\\iff \\dots$",
"answer": "il existe $M \\in\\mathbb{R}$ tel que $\\forall x\\in I\\  f(x)\\leq M$, qui s'\u00e9crit aussi\n\n$\\exists M \\in \\mathbb{R}, \\forall x\\in I,\\  f(x)\\leq M$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2974",
"position": 2,
"duration": 30,
"question": {
"id": "2974",
"question": "$f\\colon I\\to\\mathbf{R}$ minor\u00e9e $\\iff\\dots$",
"answer": "$\\exists m\\in\\mathbf{R},\\ \\forall x\\in I,\\ f(x)\\geq m$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2975",
"position": 3,
"duration": 30,
"question": {
"id": "2975",
"question": "$f\\colon I\\to\\mathbf{R}$ croissante sur $I$ $\\iff\\dots$",
"answer": "$\\forall (x,y)\\in I^2 ,\\, x\\leq y\\implies f(x)\\leq f(y)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2976",
"position": 4,
"duration": 30,
"question": {
"id": "2976",
"question": "$f\\colon I\\to\\mathbf{R}$ d\u00e9croissante sur $I$ $\\iff\\dots$",
"answer": "$\\forall (x,y)\\in I^2, \\ x\\leq y\\implies f(x)\\geq f(y)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2977",
"position": 5,
"duration": 30,
"question": {
"id": "2977",
"question": "$f\\colon I\\to\\mathbf{R}$ strictement croissante sur $I$ $\\iff\\dots$",
"answer": "$\\forall (x,y)\\in I^2 ,\\ x<y\\implies f(x)<f(y)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2978",
"position": 6,
"duration": 30,
"question": {
"id": "2978",
"question": "$f\\colon I\\to\\mathbf{R}$ strictement d\u00e9croissante sur $I$  $\\iff\\dots$",
"answer": "$\\forall (x,y)\\in I^2, \\ x<y\\implies f(x)>f(y)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2983",
"position": 7,
"duration": 30,
"question": {
"id": "2983",
"question": "$f\\colon\\mathbf{R}\\to\\mathbf{R}$ impaire $\\iff\\dots$",
"answer": "$\\forall x\\in\\mathbf{R}\\ f(-x)=-f(x)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2984",
"position": 8,
"duration": 30,
"question": {
"id": "2984",
"question": "$f\\colon\\mathbf{R}\\to\\mathbf{R}$ paire $\\iff\\colon$",
"answer": "$\\forall x\\in\\mathbf{R}\\ f(-x)=f(x)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1431-2985",
"position": 9,
"duration": 30,
"question": {
"id": "2985",
"question": "$f\\colon\\mathbf{R}\\to\\mathbf{R}$ p\u00e9riodique de p\u00e9riode $T$ $\\iff\\dots$",
"answer": "$\\forall x\\in\\mathbf{R}\\ f(x+T)=f(x)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1432": {
"id": "1432",
"name": "Nbes complexes (2)",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1432\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 330,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2024-11-11",
"questions": [{
"id": "1432-2905",
"position": 0,
"duration": 30,
"question": {
"id": "2905",
"question": "\\[z\\overline{z}=\\,?\\]",
"answer": "\\[z\\overline{z}=|z|^2\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2916",
"position": 1,
"duration": 30,
"question": {
"id": "2916",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $|z_1-z_2|$.",
"answer": "Distance entre les points d'affixe $z_1$ et $z_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2917",
"position": 2,
"duration": 30,
"question": {
"id": "2917",
"question": "Interpr\u00e9tation g\u00e9om\u00e9trique de $|z_1+z_2|$.",
"answer": "Distance entre les points d'affixe $z_1$ et $-z_2$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2952",
"position": 3,
"duration": 30,
"question": {
"id": "2952",
"question": "D\u00e9finition de $e^{i\\theta}$",
"answer": "\\[e^{i\\theta}=\\cos\\theta+i\\sin\\theta\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2959",
"position": 4,
"duration": 30,
"question": {
"id": "2959",
"question": "L'\u00e9criture trigonom\u00e9trique d'un nombre complexe est-elle unique ?",
"answer": "Le module est unique, l'argument est unique \u00e0 $2\\pi$ pr\u00e8s.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2966",
"position": 5,
"duration": 30,
"question": {
"id": "2966",
"question": "Solutions de l'\u00e9quation $z^n=1$?",
"answer": "$n$ solutions distinctes:\n\\[z_k=e^{i\\frac{2k\\pi}{n}},\\quad k\\in\\{0; 1; \\dots;n-1\\}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2970",
"position": 6,
"duration": 30,
"question": {
"id": "2970",
"question": "Solutions de $az^2+bz+c=0$, avec $a,b,c\\in\\mathbf{C}$ et $a\\neq 0$?",
"answer": "Si $b^2-4ac=0$, une seule solution: $\\displaystyle z=-\\frac{b}{2a}$\nSi $b^2-4ac\\neq 0$, soit $\\delta$ une racine carr\u00e9e complexe de $b^2-4ac$. Alors les deux solutions sont $\\displaystyle z=\\frac{-b\\pm\\delta}{2a}$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2971",
"position": 7,
"duration": 30,
"question": {
"id": "2971",
"question": "\u00c9crire trois \u00e9quations permettant de trouver les solutions de $(x+iy)^2=a+ib$.\n(x,y,a,b,r\u00e9els, x et y inconnus)\n",
"answer": "\\[\\left\\{\\begin{array}{l} x^2+y^2=\\sqrt{a^2+b^2} \\\\ x^2-y^2=a \\phantom{x^2+y^2+z^2} \\\\2xy=b \\phantom{x^2+y^2+z^2}\\end{array}\\right.\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1432-2951",
"position": 8,
"duration": 30,
"question": {
"id": "2951",
"question": "Formule de Moivre",
"answer": "\\[(cos\\theta+i\\sin\\theta)^n=\\cos(n\\theta)+i\\sin(n\\theta)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2958",
"position": 9,
"duration": 30,
"question": {
"id": "2958",
"question": "\\[\\arg\\left(\\frac{z_1}{z_2}\\right)\\]",
"answer": "$\\arg(z_1)-\\arg(z_2) \\hspace{1cm} $   (\u00e0 un multiple de $2\\pi$ pr\u00e8s)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1432-2961",
"position": 10,
"duration": 30,
"question": {
"id": "2961",
"question": "\\[\\arg(-z)=\\,?\\]",
"answer": "$\\pi+\\arg(z)  \\hspace{1cm}$  (\u00e0 un multiple de $2\\pi$ pr\u00e8s)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1433": {
"id": "1433",
"name": "DC61",
"user_id": "1160",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1433\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "33",
"value": "Technologie",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "18",
"value": "Cin\u00e9matique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 2,
"duration": 300,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-02-11",
"questions": [{
"id": "1433-142",
"position": 0,
"duration": 30,
"question": {
"id": "142",
"question": "Citer 1 avantage et 1 inconv\u00e9nient pour ce type de r\u00e9ducteur ",
"answer": "AV : grand rapport de r\u00e9duction possible, engr\u00e8nement \u00ab doux \u00bb et silencieux, d\u00e9calage 90\u00b0 entre les axes  vis et roue, possibilit\u00e9 d\u2019irr\u00e9versibilit\u00e9.\nINC : glissement (frottement) important entre la vis et la roue, rendement m\u00e9diocre.\n",
"image_question_url": "https:\/\/s3.eu-central-1.amazonaws.com\/project555-prod\/user_uploads\/08af42ec-7bd7-42d3-886e-8b803b9e1fb1",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-1554",
"position": 1,
"duration": 30,
"question": {
"id": "1554",
"question": "D\u00e9terminer la loi entr\u00e9e-sortie $\\frac{\\Omega_{2\/0}} { \\Omega_{1\/0}}$ de l'engrenage suivant, en fonction de Z1 et Z2 (nombre de dents).",
"answer": "$\\frac{ \\Omega_{2\/0}} { \\Omega_{1\/0}}=-\\frac{Z_1}{Z_2}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ecbdde10-da83-11e7-9e63-896c1ad5f851",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1433-1556",
"position": 2,
"duration": 30,
"question": {
"id": "1556",
"question": "D\u00e9terminer la loi entr\u00e9e-sortie entre ${V_{1\/0}}$  et ${\\Omega_{1\/0}}$ du m\u00e9canisme suivant, en fonction du pas p dans le cas d'une vis avec filet \u00e0 droite.",
"answer": " ${V_{1\/0}}=\\frac{p}{2\\pi}{\\Omega_{1\/0}}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/7ea67750-da88-11e7-a80a-e9d99fed9b96",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1433-1555",
"position": 3,
"duration": 30,
"question": {
"id": "1555",
"question": "D\u00e9terminer la loi entr\u00e9e-sortie $\\frac{\\Omega_{3\/0}} {\\Omega_{1\/0}}$ du train d'engrenage suivant, en fonction de Z1, Z2a, Z2b et Z3 (nombre de dents).",
"answer": "$\\frac{\\Omega_{3\/0}} {\\Omega_{1\/0}}=\\frac{Z_1*Z_{2b}}{Z_{2a}*Z_3}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8d937ec0-da85-11e7-943b-e373c44141f7",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1433-138",
"position": 4,
"duration": 30,
"question": {
"id": "138",
"question": "Pour un r\u00e9ducteur compos\u00e9 de trains simples d\u2019engrenages, donner la relation permettant de d\u00e9terminer le rapport de transmission r.",
"answer": "$ \\frac {\\omega_{sortie}}  {\\omega_{entr\u00e9e}} =(-1)^p.\\frac {produit ~des ~Z_{roues ~menantes}}  {produit~des ~Z_{roues~ men\u00e9es}}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "18",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-633",
"position": 5,
"duration": 30,
"question": {
"id": "633",
"question": "Quelle fonction de la cha\u00eene d'\u00e9nergie est assur\u00e9e par ce composant ?\n",
"answer": "fonction \"TRANSMETTRE\"",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0d4994b0-8c0d-11e7-ad7e-31f0c5569b87",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-5883",
"position": 6,
"duration": 30,
"question": {
"id": "5883",
"question": "Calculer le rapport de r\u00e9duction de ce train d'engrenages simples : $r={\\omega_1 \\over \\omega_7}$.\nLes nombres de dents sont les suivants :\n$Z_7=30$ , $Z_6=42$ , $Z_{5'}=54$ , $Z_5=26$ , $Z_4=38$ , $Z_{4'}=82$ , $Z_{3'}=48$\n$Z_{3}=24$ , $Z_{2}=32$ , $Z_{1}=65$",
"answer": "$r={\\omega_1 \\over \\omega_7}=(-1)^6.{ Z_7.Z_5.Z_4.Z_3 \\over Z_{5'}.Z_{4'}.Z_{3'}.Z_1}$\n\nApplication num\u00e9rique :\n$r=0.0514$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/6a3ac8a0-bcd2-11ed-a359-dd3ef0f1b478",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-5882",
"position": 7,
"duration": 30,
"question": {
"id": "5882",
"question": "Calculer le rapport de r\u00e9duction de ce train d'engrenages simples.\nZ1=31 , Z2a=52, Z2b=17 , Z3=79",
"answer": "${\\omega_{30} \\over \\omega_{10}}=(-1)^1.{ Z_{1}. Z_{2b} \\over Z_{2a}. Z_{3} }=-0.128$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/7b8f47a0-bcd1-11ed-bf88-11ade8e4c5d9",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-5908",
"position": 8,
"duration": 30,
"question": {
"id": "5908",
"question": "D\u00e9terminer le rapport de r\u00e9duction du train d'engrenage suivant. L'entr\u00e9e est l'arbre 4 et la sortie est l'arbre 1. Les nombres de dents sont not\u00e9s $Z_1, Z_2, Z_3, Z_4$.",
"answer": "$r=(-1)^2. {Z_4.Z_2 \\over Z_3.Z_1}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/da70c780-d971-11ee-825d-a9f25eeceea3",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1433-5909",
"position": 9,
"duration": 30,
"question": {
"id": "5909",
"question": "D\u00e9terminer le rapport de transmission $r={N_{16} \\over N_{moteur}}$ du syst\u00e8me suivant en fonction des nombres de dents $Z_i$ des roues dent\u00e9es.",
"answer": "$r={Z_{27}.Z_5 \\over Z_{35}.Z_{16}}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/0c788340-d973-11ee-85ab-3f6adbf749c4",
"image_answer_url": "",
"field_id": "11",
"course_id": "33",
"level_id": "6",
"difficulty": 2
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1435": {
"id": "1435",
"name": "DC5 STaTIC 3",
"user_id": "1272",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1435\/entrainement",
"fields": [{
"id": "11",
"value": "SI",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:41:32",
"deleted_at": "null",
"color": "cerise",
"icon": "gears"
}],
"courses": [{
"id": "31",
"value": "Statique",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "24",
"value": "Mod\u00e9lisation des liaisons",
"field_id": "11",
"created_at": "2017-04-16 06:56:53",
"updated_at": "2018-01-21 18:39:31",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 4,
"duration": 840,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 0.5,
"shared_at": "2025-04-03",
"questions": [{
"id": "1435-5944",
"position": 0,
"duration": 30,
"question": {
"id": "5944",
"question": "Combien d'inconnues statiques $N_s$ ?",
"answer": " $N_s=5$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/59c8a660-09b5-11e8-b781-49a6a904feec",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-87",
"position": 1,
"duration": 30,
"question": {
"id": "87",
"question": "Donner la forme g\u00e9n\u00e9rale d'un torseur d'actions m\u00e9caniques de type couple  entre deux pi\u00e8ces (1 et 2)  au centre de la liaison (K), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.\n",
"answer": "$ \\{T_{1\\rightarrow2} \\} =\\begin{Bmatrix}\\overrightarrow { 0}\\\\\\overrightarrow{M_{K , 1\\rightarrow2}}\\end{Bmatrix}_K=\\begin{Bmatrix}0 & L_{12}\\\\ 0 & M_{12}  \\\\0 & N_{12}\\end{Bmatrix}_{K,  (\\vec{x} , \\vec{y}, \\vec{z})} $\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1435-1914",
"position": 2,
"duration": 30,
"question": {
"id": "1914",
"question": "Exprimer le torseur d'actions m\u00e9caniques de la liaison au point A, dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$. \nO\u00f9 peut se trouver le point A pour que l'allure du torseur (les \"z\u00e9ros\" au m\u00eame endroit) reste la m\u00eame ? \nQuel est le nom complet de cette liaison ? \nQuel est le nombre d'inconnues statiques : ns=  ?",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix} 0 & 0\\\\ Y_{12} & M_{12} \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{A, (\\vec{x} , \\vec{y}, \\vec{z})} $ \nLe point A peut se trouver en tout point de l'axe (A,$ \\vec{x}$). \nLa liaison est un pivot glissant d'axe (A,$ \\vec{x}$). \nns=4",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/6b274310-075f-11e8-80e7-2500b2d79298",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1435-1718",
"position": 3,
"duration": 30,
"question": {
"id": "1718",
"question": "\u00e0 quelle action m\u00e9canique correspond une force  (en N) ?",
"answer": "une force est le nom donn\u00e9 \u00e0 la r\u00e9sultante d'une action m\u00e9canique repr\u00e9sent\u00e9e par un torseur glisseur -ou torseur force- (o\u00f9 le moment  est nul).\n$ \\{T_{1\\rightarrow2} \\} =\\begin{Bmatrix}\\overrightarrow { R_{1\\rightarrow2}}\\\\\\overrightarrow{0}\\end{Bmatrix}_K=\\begin{Bmatrix}X_{12} & 0\\\\ Y_{12} & 0  \\\\ Z_{12} & 0\\end{Bmatrix}_{K,  (\\vec{x} , \\vec{y}, \\vec{z})}$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1435-1929",
"position": 4,
"duration": 30,
"question": {
"id": "1929",
"question": "Combien d'inconnues statiques $N_s$ dans un probl\u00e8me plan ($\\vec {y}$, $\\vec {z}$)",
"answer": " $N_s=0$\n $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix} - & 0\\\\ 0 & - \\\\ 0 & -\\end{Bmatrix}_{A, (\\vec{x} , \\vec{y}, \\vec{z})} $ ",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/8afbf610-081d-11e8-9702-15c2d84c99fc",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1435-1930",
"position": 5,
"duration": 30,
"question": {
"id": "1930",
"question": "Combien d'inconnues statiques $N_s$ dans un probl\u00e8me plan ($\\vec {x}$, $\\vec {z}$)",
"answer": "$N_s=1$\n$ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix} 0 & -\\\\ - & 0 \\\\ Z_{12} & -\\end{Bmatrix}_{C, (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/04969ef0-081c-11e8-8609-65f367fee4e9",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1435-1890",
"position": 6,
"duration": 30,
"question": {
"id": "1890",
"question": "Exprimer le torseur d'actions m\u00e9caniques au centre de la liaison (C), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}0 & 0\\\\ Y_{12} & 0  \\\\ Z_{12} & 0\\end{Bmatrix}_{C, (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/93f2b2b0-05f0-11e8-aa5d-89b343645f8b",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-1928",
"position": 7,
"duration": 30,
"question": {
"id": "1928",
"question": "Combien d'inconnues statiques $N_s$ dans un probl\u00e8me plan ($\\vec {x}$, $\\vec {z}$)",
"answer": " $N_s=2$ \n $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}0 & -\\\\ - & M_{12}  \\\\ Z_{12} &-\\end{Bmatrix}_{O, (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9c46f540-081b-11e8-ab4a-cf6aa50ecc35",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1435-2242",
"position": 8,
"duration": 30,
"question": {
"id": "2242",
"question": "Quelle est la relation qui donne le barycentre d'un ensemble de n solides {$S_i$} de masses $M_i$ et de centres de gravit\u00e9 $G_i$ ?",
"answer": "$M \\cdot  \\overrightarrow{OG}=\\sum_{i=1}^n {(M_i \\cdot  \\overrightarrow{OG_i})}$\n\nexemple : $(m_1+m_2) \\cdot  \\overrightarrow{OG}=m_1 \\cdot  \\overrightarrow{OG}_1+m_2 \\cdot  \\overrightarrow{OG}_2$\n",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9d5a4520-1d25-11e8-9e1b-b9ec0bb671c4",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 2
}
}, {
"id": "1435-93",
"position": 9,
"duration": 30,
"question": {
"id": "93",
"question": "Exprimer la forme g\u00e9n\u00e9rale d'un torseur d'actions m\u00e9caniques au centre de la liaison (K), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & L_{12}\\\\ Y_{12} & M_{12}  \\\\ Z_{12} & N_{12}\\end{Bmatrix}_{ K, ( \\vec{x} , \\vec{y}, \\vec{z})}  $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-109",
"position": 10,
"duration": 30,
"question": {
"id": "109",
"question": "Compl\u00e9ter le torseur d'actions m\u00e9caniques d'un liaison h\u00e9lico\u00efdale d'axe $(D,\\vec{z})$ \n $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & L_{12}\\\\  Y_{12} &  M_{12} \\\\ Z_{12} &  \\end{Bmatrix}_{D,  (\\vec{x} , \\vec{y}, \\vec{z})}  $",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}X_{12} & L_{12}\\\\ Y_{12}  & M_{12}  \\\\ Z_{12} & \\frac{Z_{12}.p}{2.\\pi} \\end{Bmatrix}_{D,  (\\vec{x} , \\vec{y}, \\vec{z})}  $",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 4
}
}, {
"id": "1435-92",
"position": 11,
"duration": 30,
"question": {
"id": "92",
"question": "Exprimer le torseur d'actions m\u00e9caniques au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}0& 0\\\\ Y_{12} & 0  \\\\ Z_{12} & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/d9940ee0-9952-11e7-b6ee-ad11ec71b380",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-91",
"position": 12,
"duration": 30,
"question": {
"id": "91",
"question": "Exprimer le torseur d'actions m\u00e9caniques au centre de la liaison (K), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": " $ \\{T_{1\\rightarrow2} \\} = \\begin{Bmatrix}   X_{12} & 0\\\\ 0 & M_{12}  \\\\ 0 & N_{12}\\end{Bmatrix}_{K , (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/1976d830-9952-11e7-9bf7-71e2782d8e01",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-717",
"position": 13,
"duration": 30,
"question": {
"id": "717",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}  0 & 0\\\\ \\omega_{y,2\/1} & V_{O_y,{2\/1}}  \\\\ 0 & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $\nAvec  $V_{O_y,{2\/1}}=\\frac{p}{2.\\pi}.\\omega_{y,2\/1}$ pour un filet \u00e0 droite.",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/373de540-9892-11e7-bb09-5b71593a469c",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-716",
"position": 14,
"duration": 30,
"question": {
"id": "716",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}  0 & 0\\\\ 0 & V_{O_y,{2\/1}}  \\\\ 0 & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/63c42500-9882-11e7-a7ad-f3aa59941c6b",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-744",
"position": 15,
"duration": 30,
"question": {
"id": "744",
"question": "D\u00e9terminer la liaison cin\u00e9matiquement \u00e9quivalente aux deux liaisons propos\u00e9es.",
"answer": "Liaison glissi\u00e8re de direction $\\overrightarrow{y}$",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ffada090-9b89-11e7-80f4-7786eb885df1",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-722",
"position": 16,
"duration": 30,
"question": {
"id": "722",
"question": "Exprimer le torseur cin\u00e9matique au centre de la liaison (O), dans la base $(\\vec{x} , \\vec{y}, \\vec{z})$.",
"answer": "$ \\{V_{2\/1}\\}= \\begin{Bmatrix}  \\omega_{x,2\/1} & 0\\\\ \\omega_{y,2\/1} & V_{O_y,{2\/1}}  \\\\ \\omega_{z,2\/1} & 0\\end{Bmatrix}_{O,  (\\vec{x} , \\vec{y}, \\vec{z})} $",
"image_question_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/9869f670-9896-11e7-a971-c5c7b3c8d2da",
"image_answer_url": "",
"field_id": "11",
"course_id": "24",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-1753",
"position": 17,
"duration": 30,
"question": {
"id": "1753",
"question": "Citer les 6 \u00e9tapes de la r\u00e9solution d'un probl\u00e8me de statique ?",
"answer": "1 Etablir le graphe d'analyse \n2 Choisir un isolement\n3 Etablir le BAME\n4 Mod\u00e9liser chacune des actions m\u00e9caniques\n5 choisir une strat\u00e9gie de calcul (TRS, TMS, PFS)\n6 r\u00e9soudre\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1435-1764",
"position": 18,
"duration": 30,
"question": {
"id": "1764",
"question": "Quel est le th\u00e9or\u00e8me des actions mutuelles ?",
"answer": "On montre que les actions r\u00e9ciproques entre deux solides {\ud835\udc7a\ud835\udfcf} et {\ud835\udc7a\ud835\udfd0} sont oppos\u00e9es. $ \\{T_{1\\rightarrow2} \\} =- \\{T_{2\\rightarrow1} \\} $\n\n",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5945",
"position": 19,
"duration": 30,
"question": {
"id": "5945",
"question": "Lors d'un contact avec frottement, dans quel sens a lieu l'effort tangentiel ?",
"answer": "Toujours dans le sens oppos\u00e9 au mouvement.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5946",
"position": 20,
"duration": 30,
"question": {
"id": "5946",
"question": "Quel type de frottement peut-on mod\u00e9liser avec la loi de Coulomb ?",
"answer": "Uniquement le frottement sec, ind\u00e9pendant de la vitesse.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5947",
"position": 21,
"duration": 30,
"question": {
"id": "5947",
"question": "Donner la formule du coefficient de frottement f (loi de Coulomb).",
"answer": "R\u00e9ponse...",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/896bd2a0-0d83-11f0-9ff0-a5b6f971ecb8",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-1761",
"position": 22,
"duration": 30,
"question": {
"id": "1761",
"question": "Quelle sont les propri\u00e9t\u00e9s d'un solide soumis \u00e0 deux actions m\u00e9caniques de type Force ?",
"answer": "\u2022 les r\u00e9sultantes ont comme droite support la droite reliant les points d'application des 2 forces,\n\u2022 les r\u00e9sultantes ont m\u00eame intensit\u00e9 mais un sens oppos\u00e9. ",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/5396dea0-fdba-11e7-b1c9-2730a56ee7b7",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5943",
"position": 23,
"duration": 30,
"question": {
"id": "5943",
"question": "Dans un contact ponctuel avec frottement, comment se nomment les 2 composantes  de la r\u00e9sultante ?",
"answer": "La composante normale N et la composante tangentielle T.",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/bd7e3a60-0d82-11f0-a473-f15e57d6cba9",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5948",
"position": 24,
"duration": 30,
"question": {
"id": "5948",
"question": "Quel est le mod\u00e8le local de la pesanteur en un point M d'un solide ?",
"answer": "R\u00e9ponse...",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/ca4dd3c0-0d84-11f0-b193-c3caa1a8c8db",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5949",
"position": 25,
"duration": 30,
"question": {
"id": "5949",
"question": "Quelle est la forme globale du torseur de la pesanteur en un point A ?",
"answer": "R\u00e9ponse...",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/f2560050-0d84-11f0-9eb9-0f435fe8d9f4",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5950",
"position": 26,
"duration": 30,
"question": {
"id": "5950",
"question": "Quel est le mod\u00e8le local de l'action surfacique de contact d'un fluide 1 sur une surface \u00e9l\u00e9mentaire dS centr\u00e9e en M d'un solide 2 ? ",
"answer": "R\u00e9ponse...",
"image_question_url": "",
"image_answer_url": "https:\/\/project555-prod.s3.eu-central-1.amazonaws.com\/user_uploads\/788f9f60-0d85-11f0-8d4e-4d0c1e27b25e",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}, {
"id": "1435-5951",
"position": 27,
"duration": 30,
"question": {
"id": "5951",
"question": "Quel est le centre de pouss\u00e9e de l'action d'un fluide ?",
"answer": "C'est le point o\u00f9 le moment de l'action du fluide est nul.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "11",
"course_id": "31",
"level_id": "6",
"difficulty": 3
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
},
"1436": {
"id": "1436",
"name": "D\u00e9rivabilit\u00e9 et applications",
"user_id": "619",
"private": "false",
"url": "https:\/\/www.sophieand.me\/quizzs\/1436\/entrainement",
"fields": [{
"id": "19",
"value": "Math\u00e9matiques",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-25 08:14:39",
"deleted_at": "null",
"color": "duck",
"icon": "superscript"
}],
"courses": [{
"id": "54",
"value": "Analyse",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "55",
"value": "Calculs",
"field_id": "19",
"created_at": "2017-07-07 10:27:51",
"updated_at": "2018-01-21 18:39:28",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "49",
"value": "Maths",
"field_id": "19",
"created_at": "2017-04-20 11:09:25",
"updated_at": "2018-01-21 18:39:29",
"deleted_at": "null",
"level_id": "6"
}, {
"id": "498",
"value": "Analyse",
"field_id": "19",
"created_at": "2020-02-07 08:54:39",
"updated_at": "2020-02-07 08:54:39",
"deleted_at": "null",
"level_id": "6"
}],
"levels": [{
"id": "6",
"value": "Sup",
"created_at": "2017-04-16 06:56:52",
"updated_at": "2017-04-18 16:10:30",
"deleted_at": "null",
"level_group_id": "2",
"order": 140
}],
"difficulty": 1,
"duration": 360,
"already_tried": "true",
"already_passed": "true",
"best_score": 1,
"last_score": 1,
"shared_at": "2025-05-05",
"questions": [{
"id": "1436-3275",
"position": 0,
"duration": 30,
"question": {
"id": "3275",
"question": "D\u00e9riv\u00e9e de $\\ln(u(x))$.",
"answer": "\\[\\frac{u^\\prime(x)}{u(x)}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-3273",
"position": 1,
"duration": 30,
"question": {
"id": "3273",
"question": "D\u00e9riv\u00e9e de $u^n(x)$",
"answer": "\\[nu^\\prime(x)u^{n-1}(x)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-3272",
"position": 2,
"duration": 30,
"question": {
"id": "3272",
"question": "D\u00e9riv\u00e9e de $v\\big(u(x)\\big)$",
"answer": "\\[u^\\prime(x)\\times v^\\prime\\big(u(x)\\big)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-2997",
"position": 3,
"duration": 30,
"question": {
"id": "2997",
"question": "D\u00e9finition de $f^\\prime(a)$.",
"answer": "\\[f^\\prime(a)=\\lim_{x\\to a}\\frac{f(x)-f(a)}{x-a}\\] ou ce qui revient au m\u00eame  \\[f^\\prime(a)= \\lim_{h\\to 0}\\frac{f(a+h)-f(a)}{h}\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-2998",
"position": 4,
"duration": 30,
"question": {
"id": "2998",
"question": "Si $f$ admet une r\u00e9ciproque, $\\left(f^{-1}\\right)^\\prime(x)=\\dots$ ?",
"answer": "\\[\\left(f^{-1}\\right)^\\prime(x)=\\frac{1}{f^{\\prime}\\big(f^{-1}(x)\\big)}\\]\u00e0 condition que $f$ soit d\u00e9rivable en $f^{-1}(x)$ et que $f^\\prime$ ne s'annule pas en ce point.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "54",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-4795",
"position": 5,
"duration": 30,
"question": {
"id": "4795",
"question": "Si $\\frac{f(a+h)-f(a)}{h}$ admet une limite quand h tend vers 0, alors $f$ est d\u00e9rivable en $a$. Vrai ou faux ?",
"answer": "C'est faux, il faut que cette limite soit r\u00e9elle (pas un infini...)",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-4798",
"position": 6,
"duration": 30,
"question": {
"id": "4798",
"question": "Citer le th\u00e9or\u00e8me des accroissements finis.",
"answer": "Soit $f \\colon [a,b] \\to \\mathbb{R}$. Si $f$ est continue sur [a,b], d\u00e9rivable sur ]a,b[, alors il existe $c \\in ]a,b[$ tel que $\\frac{f(b)-f(a)}{b-a}=f'(c)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-4797",
"position": 7,
"duration": 30,
"question": {
"id": "4797",
"question": "Citer le th\u00e9or\u00e8me de Rolle (hypoth\u00e8ses et r\u00e9sultat !)",
"answer": "Soit $f \\colon [a,b] \\to \\mathbb{R}$. Si $f$ est continue sur [a,b], d\u00e9rivable sur ]a,b[, et telle que $f(a)=f(b)$, alors il existe $c \\in ]a,b[$ tel que $f'(c)=0$",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-5769",
"position": 8,
"duration": 30,
"question": {
"id": "5769",
"question": "Citer l'in\u00e9galit\u00e9 des accroissements finis",
"answer": "Soit $f \\colon [a,b] \\to \\mathbb{R}$. Si $f$ est continue sur [a,b], d\u00e9rivable sur ]a,b[, et si $f'$ est minor\u00e9e par $m$ et major\u00e9e par $M$ sur $]a,b[$, alors $m(b-a) \\leq f(b)-f(a) \\leq M(b-a)$.",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "49",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-4796",
"position": 9,
"duration": 30,
"question": {
"id": "4796",
"question": "Pour d\u00e9montrer que $f$ est d\u00e9rivable en $a$, comment peut-on s'y prendre ? (2 m\u00e9thodes...)",
"answer": "1\/ Etudier la limite du taux d'accroissement de f en a.\n2\/ Utiliser les op\u00e9rations sur les fonctions d\u00e9rivables",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "498",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-5886",
"position": 10,
"duration": 30,
"question": {
"id": "5886",
"question": "DL \u00e0 l'ordre 5 de $\\cos x $ en 0 ?",
"answer": "\\[\\cos x=1-\\frac{x^2}{2!}+\\frac{x^4}{4!}+o(x^5)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}, {
"id": "1436-5887",
"position": 11,
"duration": 30,
"question": {
"id": "5887",
"question": "DL \u00e0 l'ordre 5 de $\\sin x$ en 0 ?",
"answer": "\\[\\sin x=x-\\frac{x^3}{3!}+\\frac{x^5}{5!}+o(x^5)\\]",
"image_question_url": "",
"image_answer_url": "",
"field_id": "19",
"course_id": "55",
"level_id": "6",
"difficulty": 1
}
}],
"classesSharedWith": [{
"id": "154",
"name": "TSI1",
"schoolyear": "2024-2025"
}]
}
}
}

idtot: list = []



dico = L["fields"]
try :
    for i in dico.keys():
        print(dico[i]["value"])
        command = "CREATE TABLE " + str(dico[i]["value"]) + " (id VARCHAR(255), name VARCHAR(255), question VARCHAR(255), reponse VARCHAR(255), image_question_url VARCHAR(255), image_answer_url VARCHAR(255) , difficulty VARCHAR(255))"
        cur_i.execute(command)
except :
    print("Deja existant")

######################################## Permet d'avoir toute les questions d'un quizz

dico = L["quizzs"]
for i in dico.keys():
    idtot.append(i)


rep = 0
anciename = ""
val = {}
matierebyname = {}



for k in idtot:
    matlist = []
    name = dico[k]["name"]
    val = dico[k]["questions"]
    dico2 = {index: value for index, value in enumerate(val)}
    value = dico2.keys()
    for i in value:
        matiere = util.name(dico2[i]["question"]["field_id"])
        if matiere not in matlist:
            matlist.append(matiere)
    matierebyname.update({name: matlist})

for k in idtot:
    name = dico[k]["name"]
    val = dico[k]["questions"]
    dico2 = {index: value for index, value in enumerate(val)}
    value = dico2.keys()
    matiere = matierebyname[name]
    for y in matiere:
        rep = 0
        verifpresence = 'SELECT COUNT(*) from ' + y + ' WHERE name = "' + str(name) + '"'
        print(verifpresence)
        exist = cur_i.execute(verifpresence)
        count = str(exist.fetchall()).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "")
        if int(count) == 0:
          for i in value:
            question = dico2[i]["question"]["question"].encode('utf-8', 'replace').decode()
            answer = dico2[i]["question"]["answer"].encode('utf-8', 'replace').decode()
            image_question = dico2[i]["question"]["image_question_url"]
            image_answer = dico2[i]["question"]["image_answer_url"]
            difficulty = dico2[i]["question"]["difficulty"]
            if anciename == "":
                anciename = name
            if anciename == name:
                rep += 1
            else :
                rep = 1
            # print(name)
            # print(rep)
            # print(matiere)
            # print(question)
            # print("answer : ")
            # print(answer)
            # print("###########################################################################")
            anciename = name
            Command = "INSERT INTO " + y + " (id,name,question,reponse,image_question_url,image_answer_url,difficulty) VALUES (?,?,?,?,?,?,?)"
            val = (str(rep),name,question,answer,image_question,image_answer,difficulty)
            print(Command)
            print(val)
            cur_i.execute(Command,val)
            con_i.commit()
            print("1 record inserted, ID:", cur_i.lastrowid)
            print("###########################################################################")



##### Supprimer toute les donnée entourant la valeurs
####" Enlever la valeur ), document.getElementById('studentApp')); });
####### Supprimer les espaces entre les valeurs 
#####Remplacer tout les null par "null", tout les false par "false" et tout les tru par "true"
