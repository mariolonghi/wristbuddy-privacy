---
layout: default
title: Wrist Buddy — Datenschutzerklärung
description: Datenschutzerklärung der Wrist-Buddy-App für iPhone und Apple Watch.
lang: de
permalink: /de/
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Datenschutzerklärung

**Gültig ab:** {{ page.effective_date }}
**Zuletzt aktualisiert:** {{ page.last_updated }}

Wrist Buddy ist eine Dienstprogramm-App für iPhone und Apple Watch, die den Status deines iPhones (Akku, Laden, Netzwerk, Bewegung, Stumm-/Fokus-Modus, Entfernung) auf deiner Apple Watch anzeigt. Diese Erklärung beschreibt, welche Daten die App verarbeitet und warum — sie ist kurz, weil die Antwort lautet: „fast keine".

Entwickler von Wrist Buddy ist **Mario Longhi**, ein unabhängiger Entwickler mit Sitz in Spanien (EU). In diesem Dokument bezieht sich „wir" auf die App Wrist Buddy und ihren Entwickler.

---

## Kurzfassung

- Wrist Buddy erfasst **keine personenbezogenen Daten**.
- Wrist Buddy sendet **keine Daten** an Server, Cloud-Dienste oder Dritte.
- Alle Daten, die zwischen deinem iPhone und deiner Apple Watch ausgetauscht werden, bleiben auf deinen Geräten und werden ausschließlich über Apples WatchConnectivity-Framework (Bluetooth oder lokales WLAN) zwischen den beiden übertragen.
- Wrist Buddy enthält keine Analyse-Tools, keine Werbung, kein Tracking und keine Drittanbieter-SDKs.
- Unser Datenschutzlabel im App Store lautet **„Keine Daten erhoben"** — alle Kategorien sind leer.

---

## Informationen, die wir nicht erfassen

Wir möchten genau benennen, was wir *nicht* tun, denn der Verzicht auf Datenerfassung ist die zentrale Designentscheidung:

- Wir erfassen **nicht** deinen Namen, deine E-Mail-Adresse, deine Telefonnummer oder andere identifizierende Informationen.
- Wir verlangen **nicht**, dass du ein Konto erstellst oder dich anmeldest.
- Wir erfassen **keine** Gerätekennungen, Werbe-Identifikatoren (IDFA) oder Ähnliches.
- Wir verfolgen **nicht** deinen Standort.
- Wir verfolgen **nicht** deine Nutzung der App, speichern keine Absturzberichte auf unseren Servern und nutzen keinen Analyse-Dienst.
- Wir teilen, verkaufen oder übermitteln **keine** Daten an Dritte — weil wir keine Daten haben, die wir teilen könnten.
- Wir speichern deine Daten **nicht** in iCloud, auf unseren Servern oder auf Servern Dritter.

---

## So funktioniert die App (Datenfluss)

Wrist Buddy liest bestimmte Informationen von deinem iPhone und deiner Apple Watch über Apples Standard-System-Frameworks und zeigt sie in der App-Oberfläche an. Keine dieser Informationen verlässt deine Geräte:

| Angezeigte Information | Wie sie gelesen wird | Wo sie bleibt |
|---|---|---|
| iPhone-Akkustand und Ladezustand | iOS-Akku-APIs | Auf dem iPhone; per WatchConnectivity an deine gekoppelte Apple Watch gesendet |
| WLAN- und Mobilfunk-Verbindungsstatus | Apples Network-Framework | Wie oben |
| Ob das iPhone bewegt wird | Bewegungssensor des iPhones (mit deiner Erlaubnis) | Wie oben |
| Ob das iPhone stummgeschaltet ist / im Fokus-Modus ist | iOS-Audio- und Fokus-APIs | Wie oben |
| Entfernung zwischen iPhone und Apple Watch | Apples NearbyInteraction-Framework (UWB) — Pro-Funktion, kompatible Hardware erforderlich | Wird lokal auf jedem Gerät berechnet; verlässt das Gerät nie |
| Apple-Watch-Akkustand und Ladezustand | watchOS-Akku-APIs | Auf der Watch; per WatchConnectivity an das iPhone für den „Apple Watch"-Statusbildschirm gesendet (Pro-Funktion) |

**WatchConnectivity** ist Apples integriertes Framework für die direkte Kommunikation zwischen iPhone und Apple Watch. Es nutzt Bluetooth oder lokales WLAN zwischen deinen beiden Geräten. Es leitet keine Daten über einen Server.

**Eine zufällig generierte Kennung** wird beim ersten Start der App auf deinem Gerät erstellt, ausschließlich in den lokalen UserDefaults gespeichert und nur dazu verwendet, ausgehende „Funktion vorschlagen"-E-Mails zu kennzeichnen, damit wir Folgenachrichten derselben Installation zuordnen können, falls du uns welche schickst. Diese Kennung verlässt dein Gerät nie, es sei denn, du tippst ausdrücklich auf „Funktion vorschlagen" und schickst die E-Mail selbst.

---

## Berechtigungen, die Wrist Buddy anfordern kann

iOS verlangt von Apps, dass sie um Erlaubnis bitten, bevor sie auf bestimmte Funktionen zugreifen. Wrist Buddy fordert Folgendes an, alles optional und ausschließlich für die beschriebenen Funktionen verwendet:

| Berechtigung | Warum wir sie anfordern |
|---|---|
| **Bewegung & Fitness** | Um zu erkennen, ob dein iPhone gerade bewegt wird (Beschleunigungssensor-Messung). Wird ausschließlich für die Statuszeile „Bewegungserkennung" verwendet. Der Beschleunigungssensor wird auf Anforderung abgetastet — nur kurz beim Aktualisieren der Watch-App — niemals dauerhaft. |
| **Mitteilungen** | Nur wenn du die Pro-Funktion „Akku-Hinweise" aktivierst. Wird verwendet, um dir lokale Mitteilungen zu senden, wenn dein iPhone vollständig geladen ist oder unter 20 % Akku fällt. Die Mitteilungen werden vollständig auf deinem Gerät erzeugt — ohne Server-Beteiligung. |
| **Fokus-Status** | Optional, nur wenn du die Pro-Statuszeile „Fokus-Modus" aktivierst. Lässt die App wissen, ob der iOS-Fokus-Modus aktiv ist, damit die zugehörige Zeile Ein/Aus anzeigen kann. Die Daten bleiben auf deinen Geräten. |
| **Mikrofon** | Optional, nur wenn du die Pro-Funktion „Such-Klingelton" unter Mehr → Einstellungen → Such-Klingelton aktivierst. iOS verlangt die Mikrofon-Berechtigung, damit wir die Audio-Kategorie nutzen können, mit der wir den Such-Klingelton auf den eingebauten iPhone-Lautsprecher leiten — so hörst du den Klingelton auch dann, wenn AirPods oder kabelgebundene Kopfhörer angeschlossen sind. **Das Mikrofon wird nie aufgezeichnet, abgehört oder für irgendeine Audio-Eingabe verwendet.** Lehnst du die Berechtigung ab, funktioniert der Such-Klingelton trotzdem — er wird einfach über die Ausgabe wiedergegeben, die iOS normalerweise verwenden würde (üblicherweise deine Kopfhörer, falls verbunden). |

Du kannst alle diese Berechtigungen jederzeit unter **Einstellungen → Wrist Buddy** auf deinem iPhone widerrufen. Die zugehörige Funktion stellt dann einfach den Betrieb ein; sonst ist nichts in der App betroffen.

---

## In-App-Käufe

Wrist Buddy bietet eine einmalige **Pro**-Freischaltung über Apples Standard-In-App-Kaufsystem (StoreKit). Wenn du einen Kauf tätigst:

- Die Transaktion wird vollständig von Apple abgewickelt. Wir sehen nie deinen Namen, deine Zahlungsinformationen, deine Apple-ID oder andere mit dem Kauf verbundene personenbezogene Daten.
- Apple kann uns über App Store Connect anonyme, aggregierte Verkaufsberichte zusenden (z. B. „X Exemplare im Land Y in diesem Monat verkauft"). Diese Berichte identifizieren keine einzelnen Kund:innen.
- Die Pro-Freischaltung wird lokal auf deinem Gerät gespeichert (in UserDefaults) und über Apples StoreKit-Framework verifiziert. Es gibt kein separates Konto und keinen separaten Login.

Du kannst deinen Pro-Kauf auf einem neuen oder zurückgesetzten Gerät wiederherstellen, indem du in der App auf **Käufe wiederherstellen** tippst — Apple identifiziert die Berechtigung über deine Apple-ID, ohne dass wir deine Identität erfahren.

---

## Datenschutz von Kindern

Wrist Buddy ist im App Store mit **4+** klassifiziert und für alle Altersgruppen geeignet. Die App erfasst wissentlich keine personenbezogenen Daten von irgendjemandem, einschließlich Kindern unter 13 Jahren.

---

## Drittanbieter-Dienste

Wrist Buddy nutzt **keine Drittanbieter-Dienste, -SDKs, -Frameworks oder -Netzwerke**. Die Laufzeit-Abhängigkeiten der App beschränken sich auf Apples eigene iOS- und watchOS-System-Frameworks. Es gibt keine Analyse-Dienste, keine Werbenetzwerke und keine Absturzberichts-Dienste über Apples eigene hinaus (die anonym und auf iOS-Ebene optional sind und nicht etwas, das Wrist Buddy unabhängig aktivieren würde).

---

## Internationale Datenübermittlungen

Da Wrist Buddy keine Daten erfasst und überträgt, gibt es keine internationalen Datenübermittlungen offenzulegen. Alle App-Daten bleiben auf deinen persönlichen Geräten.

---

## Deine Rechte (EU / DSGVO)

Das Design der App bedeutet, dass es keine Verarbeitung personenbezogener Daten gibt, auf die wir reagieren könnten. Zur Klarstellung:

- **Auskunftsrecht**: Es gibt keine personenbezogenen Daten, die wir über dich speichern.
- **Recht auf Berichtigung / Löschung**: Bei uns gibt es keine Daten zu korrigieren oder zu löschen. Um alle App-Daten von deinem Gerät zu entfernen, lösche einfach die Wrist-Buddy-App — iOS entfernt die lokalen UserDefaults gleich mit.
- **Recht auf Datenübertragbarkeit**: Nicht anwendbar, da wir keine personenbezogenen Daten speichern.
- **Widerspruchsrecht / Recht auf Einschränkung der Verarbeitung**: Nicht anwendbar, da wir keine Verarbeitung personenbezogener Daten durchführen.
- **Beschwerderecht**: Solltest du dennoch der Ansicht sein, dass wir Daten falsch behandelt haben, kannst du dich an deine nationale Datenschutzbehörde wenden. In Deutschland ist das je nach Wohnsitz die zuständige Landesdatenschutzbehörde oder der **Bundesbeauftragte für den Datenschutz und die Informationsfreiheit** (https://www.bfdi.bund.de). In Spanien ist es die **Agencia Española de Protección de Datos** (https://www.aepd.es).

---

## Änderungen dieser Erklärung

Sollten wir jemals ändern, wie Wrist Buddy mit Daten umgeht — z. B. wenn wir eine Funktion hinzufügen, die eine neue Berechtigung erfordert — aktualisieren wir diese Erklärung sowie das Datum „Zuletzt aktualisiert" oben. Wesentliche Änderungen werden auch im App-Store-Datenschutzlabel widergespiegelt, das Apple auf der App-Detailseite anzeigt.

---

## Kontakt

Für Fragen zum Datenschutz, Feedback oder zur Ausübung der oben beschriebenen Rechte wende dich bitte an:

**Mario Longhi** — wristbuddyapp+policy@gmail.com

Wir bemühen uns, Datenschutz-Anfragen innerhalb von 14 Tagen zu beantworten.
