---
layout: default
title: Wrist Buddy — Politique de confidentialité
description: Politique de confidentialité de l'app Wrist Buddy pour iPhone et Apple Watch.
lang: fr
permalink: /fr/
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Politique de confidentialité

**Date d'entrée en vigueur :** {{ page.effective_date }}
**Dernière mise à jour :** {{ page.last_updated }}

Wrist Buddy est une app utilitaire pour iPhone et Apple Watch qui affiche l'état de ton iPhone (batterie, charge, réseau, mouvement, mode silencieux / Concentration, distance) sur ton Apple Watch. Cette politique explique quelles données l'app gère et pourquoi — elle reste courte parce que la réponse est « presque aucune ».

Le développeur de Wrist Buddy est **Mario Longhi**, un développeur indépendant basé en Espagne (UE). Dans tout ce document, « nous » désigne l'app Wrist Buddy et son développeur.

---

## En bref

- Wrist Buddy ne collecte **aucune donnée personnelle**.
- Wrist Buddy n'envoie **aucune donnée** à un serveur, à un cloud ou à un tiers.
- Toutes les données échangées entre ton iPhone et ton Apple Watch restent sur tes appareils, transmises uniquement entre les deux via le framework WatchConnectivity d'Apple (Bluetooth ou Wi-Fi local).
- Wrist Buddy ne contient ni analytique, ni publicité, ni traçage, ni SDK tiers.
- Notre étiquette de confidentialité sur l'App Store est **« Aucune donnée collectée »** — toutes les catégories décochées.

---

## Informations que nous ne collectons pas

Nous tenons à être précis sur ce que nous *ne faisons pas*, car l'absence de collecte est le choix de conception central :

- Nous **ne** collectons **pas** ton nom, ton adresse e-mail, ton numéro de téléphone ni aucune autre information identifiante.
- Nous **ne** te demandons **pas** de créer un compte ni de te connecter.
- Nous **ne** collectons **pas** d'identifiants d'appareil, d'identifiants publicitaires (IDFA) ou similaires.
- Nous **ne** suivons **pas** ta localisation.
- Nous **ne** suivons **pas** ton utilisation de l'app, ne stockons pas de rapports de crash sur nos serveurs et n'utilisons aucun service d'analytique.
- Nous **ne** partageons, vendons ou transmettons **pas** de données à des tiers — parce que nous n'avons aucune donnée à partager.
- Nous **ne** stockons **pas** tes données sur iCloud, sur nos serveurs ou sur ceux de qui que ce soit d'autre.

---

## Comment l'app fonctionne (flux de données)

Wrist Buddy lit certaines informations de ton iPhone et de ton Apple Watch via les frameworks système standard d'Apple, puis les affiche dans l'interface de l'app. Aucune de ces informations ne quitte tes appareils :

| Information affichée | Comment elle est lue | Où elle reste |
|---|---|---|
| Pourcentage de batterie et état de charge de l'iPhone | API de batterie d'iOS | Sur l'iPhone ; envoyée à ton Apple Watch jumelée via WatchConnectivity |
| État de connectivité Wi-Fi et cellulaire | Framework Network d'Apple | Idem ci-dessus |
| Si l'iPhone est en mouvement | Capteur de mouvement de l'iPhone (avec ton autorisation) | Idem ci-dessus |
| Si l'iPhone est en silencieux / en mode Concentration | API audio et Concentration d'iOS | Idem ci-dessus |
| Distance entre l'iPhone et l'Apple Watch | Framework NearbyInteraction (UWB) d'Apple — fonction Pro, nécessite un matériel compatible | Calculée localement sur chaque appareil ; jamais transmise hors de l'appareil |
| Pourcentage de batterie et état de charge de l'Apple Watch | API de batterie de watchOS | Sur la Watch ; envoyée à l'iPhone via WatchConnectivity pour l'écran d'état « Apple Watch » (fonction Pro) |

**WatchConnectivity** est le framework intégré d'Apple pour la communication directe entre l'iPhone et l'Apple Watch. Il utilise le Bluetooth ou le Wi-Fi local entre tes deux appareils. Il ne fait transiter aucune donnée par un serveur.

**Un identifiant généré aléatoirement** est créé sur ton appareil au premier lancement de l'app, stocké uniquement dans les UserDefaults locaux et utilisé exclusivement pour étiqueter les e-mails sortants de « Suggérer une fonctionnalité » afin que nous puissions corréler les messages d'une même installation si tu choisis de nous envoyer un suivi. Cet identifiant ne quitte jamais ton appareil à moins que tu ne touches explicitement « Suggérer une fonctionnalité » et que tu envoies l'e-mail toi-même.

---

## Autorisations que Wrist Buddy peut demander

iOS exige des apps qu'elles demandent l'autorisation avant d'accéder à certaines capacités. Wrist Buddy demande les suivantes, toutes optionnelles et utilisées uniquement pour les fonctions décrites :

| Autorisation | Pourquoi nous la demandons |
|---|---|
| **Mouvement et forme** | Pour détecter si ton iPhone est actuellement en mouvement (lecture de l'accéléromètre). Utilisé uniquement pour la ligne d'état « Détection de mouvement ». L'accéléromètre est échantillonné à la demande — seulement brièvement à chaque rafraîchissement de l'app Watch — jamais en continu. |
| **Notifications** | Uniquement si tu actives la fonction Pro « Alertes de batterie ». Utilisées pour t'envoyer des notifications locales lorsque ton iPhone est entièrement chargé ou descend sous 20 % de batterie. Les notifications sont générées entièrement sur ton appareil — sans intervention serveur. |
| **État de Concentration** | Optionnel, uniquement si tu actives la ligne Pro « Mode Concentration ». Permet à l'app de savoir si le mode Concentration d'iOS est actif afin que la ligne correspondante affiche Activé/Désactivé. Les données restent sur tes appareils. |
| **Microphone** | Optionnel, uniquement si tu actives la fonction Pro « Anneau localisateur » dans Plus → Réglages → Anneau localisateur. iOS exige l'autorisation du microphone pour utiliser la catégorie audio qui nous permet d'acheminer le son de l'anneau localisateur vers le haut-parleur intégré de l'iPhone, afin que tu puisses entendre l'alerte même quand des AirPods ou un casque filaire sont connectés. **Le microphone n'est jamais enregistré, écouté ou utilisé pour quelque entrée audio que ce soit.** Si tu refuses l'autorisation, l'anneau localisateur fonctionne quand même — il sera simplement diffusé sur la sortie qu'iOS utiliserait normalement (en général, tes écouteurs s'ils sont connectés). |

Tu peux révoquer ces autorisations à tout moment dans **Réglages → Wrist Buddy** sur ton iPhone. La fonction correspondante cessera simplement de marcher ; rien d'autre dans l'app n'en sera affecté.

---

## Achats intégrés

Wrist Buddy propose un déverrouillage **Pro** unique via le système standard d'achats intégrés d'Apple (StoreKit). Lorsque tu effectues un achat :

- La transaction est entièrement gérée par Apple. Nous ne voyons jamais ton nom, tes informations de paiement, ton identifiant Apple ni aucune autre donnée personnelle associée à l'achat.
- Apple peut nous envoyer des rapports de ventes anonymes et agrégés via App Store Connect (par exemple, « X exemplaires vendus dans le pays Y ce mois-ci »). Ces rapports n'identifient pas les clients individuels.
- Le déverrouillage Pro est stocké localement sur ton appareil (dans UserDefaults) et vérifié via le framework StoreKit d'Apple. Il n'y a ni compte ni connexion séparée.

Tu peux restaurer ton achat Pro sur un appareil neuf ou réinitialisé en touchant **Restaurer les achats** dans l'app — Apple identifie le droit via ton identifiant Apple sans que nous apprenions ton identité.

---

## Confidentialité des enfants

Wrist Buddy est classée **4+** sur l'App Store et convient à tous les âges. L'app ne collecte sciemment aucune information personnelle de qui que ce soit, y compris des enfants de moins de 13 ans.

---

## Services tiers

Wrist Buddy n'utilise **aucun service, SDK, framework ou réseau tiers**. Les dépendances d'exécution de l'app se limitent aux frameworks système d'iOS et de watchOS d'Apple. Il n'y a aucun service d'analytique, aucun réseau publicitaire ni aucun service de rapport de crash au-delà de ceux d'Apple (qui sont anonymes et optionnels au niveau d'iOS, et non quelque chose que Wrist Buddy active de manière indépendante).

---

## Transferts internationaux de données

Comme Wrist Buddy ne collecte ni ne transmet aucune donnée, il n'y a aucun transfert international de données à divulguer. Toutes les données de l'app restent sur tes appareils personnels.

---

## Tes droits (UE / RGPD)

La conception de l'app fait qu'il n'y a aucun traitement de données personnelles sur lequel agir de notre côté. Pour être explicite :

- **Droit d'accès** : nous ne détenons aucune donnée personnelle te concernant.
- **Droit de rectification / d'effacement** : il n'y a aucune donnée à corriger ou supprimer de notre côté. Pour retirer toutes les données de l'app de ton appareil, il suffit de supprimer Wrist Buddy — iOS supprimera les UserDefaults locaux en même temps.
- **Droit à la portabilité des données** : non applicable, puisque nous ne détenons aucune donnée personnelle.
- **Droit d'opposition / de limitation du traitement** : non applicable, puisque nous n'effectuons aucun traitement de données personnelles.
- **Droit d'introduire une réclamation** : si tu estimes néanmoins que nous avons mal géré tes données, tu peux contacter ton autorité nationale de protection des données. En France, il s'agit de la **CNIL** (https://www.cnil.fr).

---

## Modifications de cette politique

Si nous changeons un jour la manière dont Wrist Buddy gère les données — par exemple en ajoutant une fonctionnalité qui nécessite une nouvelle autorisation — nous mettrons à jour cette politique ainsi que la date de « Dernière mise à jour » en haut. Les changements importants seront également reflétés dans l'étiquette de confidentialité de l'App Store qu'Apple affiche sur la fiche de l'app.

---

## Contact

Pour toute question relative à la confidentialité, tout retour ou pour exercer l'un des droits décrits ci-dessus, contacte :

**Mario Longhi** — wristbuddyapp+policy@gmail.com

Nous nous efforçons de répondre aux demandes de confidentialité dans un délai de 14 jours.
