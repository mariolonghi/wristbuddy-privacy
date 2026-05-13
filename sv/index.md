---
layout: default
title: Wrist Buddy — Integritetspolicy
description: Integritetspolicy för Wrist Buddy-appen för iPhone och Apple Watch.
lang: sv
permalink: /sv/
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Integritetspolicy

**Gäller från:** {{ page.effective_date }}
**Senast uppdaterad:** {{ page.last_updated }}

Wrist Buddy är en hjälpapp för iPhone och Apple Watch som visar din iPhones status (batteri, laddning, nätverk, rörelse, tyst läge / Fokus, avstånd) på din Apple Watch. Den här policyn förklarar vilken data appen hanterar och varför — den är kort eftersom svaret är "nästan ingen".

Utvecklare av Wrist Buddy är **Mario Longhi**, en oberoende utvecklare baserad i Spanien (EU). I det här dokumentet syftar "vi" på Wrist Buddy-appen och dess utvecklare.

---

## Sammanfattning

- Wrist Buddy samlar **inte in några personuppgifter**.
- Wrist Buddy skickar **ingen data** till någon server, något moln eller någon tredje part.
- All data som utbyts mellan din iPhone och din Apple Watch stannar på dina enheter och skickas endast mellan de två via Apples WatchConnectivity-ramverk (Bluetooth eller lokalt Wi-Fi).
- Wrist Buddy innehåller ingen analys, ingen annonsering, ingen spårning och inga tredjeparts-SDK:er.
- Vår integritetsetikett på App Store är **"Ingen data samlas in"** — alla kategorier omarkerade.

---

## Information vi inte samlar in

Vi vill vara tydliga med vad vi *inte* gör, eftersom frånvaron av datainsamling är det centrala designvalet:

- Vi samlar **inte** in ditt namn, din e-postadress, ditt telefonnummer eller annan identifierande information.
- Vi kräver **inte** att du skapar ett konto eller loggar in.
- Vi samlar **inte** in enhets-ID, annons-ID (IDFA) eller liknande.
- Vi spårar **inte** din position.
- Vi spårar **inte** din användning av appen, lagrar inga kraschrapporter på våra servrar och använder ingen analystjänst.
- Vi delar, säljer eller överför **inte** data till någon tredje part — eftersom vi inte har någon data att dela.
- Vi lagrar **inte** dina data i iCloud, på våra servrar eller på någon annans servrar.

---

## Så fungerar appen (dataflöde)

Wrist Buddy läser viss information från din iPhone och din Apple Watch via Apples standard-systemramverk och visar den i appens gränssnitt. Ingen av denna information lämnar dina enheter:

| Information som visas | Hur den läses | Var den stannar |
|---|---|---|
| iPhones batteriprocent och laddningsstatus | iOS batteri-API:er | På iPhone; skickas till din parade Apple Watch via WatchConnectivity |
| Wi-Fi- och mobilanslutningsstatus | Apples Network-ramverk | Samma som ovan |
| Om iPhone rör sig | iPhones rörelsesensor (med ditt tillstånd) | Samma som ovan |
| Om iPhone är i tyst läge / i Fokus-läge | iOS ljud- och Fokus-API:er | Samma som ovan |
| Avståndet mellan iPhone och Apple Watch | Apples NearbyInteraction-ramverk (UWB) — Pro-funktion, kräver kompatibel hårdvara | Beräknas lokalt på varje enhet; överförs aldrig från enheten |
| Apple Watchs batteriprocent och laddningsstatus | watchOS batteri-API:er | På klockan; skickas till iPhone via WatchConnectivity för "Apple Watch"-statusskärmen (Pro-funktion) |

**WatchConnectivity** är Apples inbyggda ramverk för direktkommunikation mellan iPhone och Apple Watch. Det använder Bluetooth eller lokalt Wi-Fi mellan dina två enheter. Det skickar ingen data via någon server.

**En slumpmässigt genererad identifierare** skapas på din enhet första gången appen startas, lagras endast i lokala UserDefaults och används enbart för att märka utgående "Föreslå en funktion"-mejl så att vi kan koppla samman meddelanden från samma installation om du väljer att skicka oss uppföljningar. Den här identifieraren lämnar aldrig din enhet om du inte uttryckligen trycker på "Föreslå en funktion" och skickar mejlet själv.

---

## Behörigheter som Wrist Buddy kan begära

iOS kräver att appar ber om tillstånd innan de får åtkomst till vissa funktioner. Wrist Buddy begär följande, alla frivilliga och endast använda för de funktioner som beskrivs:

| Behörighet | Varför vi frågar |
|---|---|
| **Rörelse och kondition** | För att avgöra om din iPhone är i rörelse just nu (avläsning av accelerometern). Används endast för statusraden "Rörelsedetektering". Accelerometern samplas på begäran — bara kortvarigt när Watch-appen uppdateras — aldrig kontinuerligt. |
| **Notiser** | Endast om du aktiverar Pro-funktionen "Batterivarningar". Används för att skicka lokala notiser när din iPhone är fulladdad eller faller under 20 % batteri. Notiserna genereras helt på din enhet — utan inblandning av server. |
| **Fokus-status** | Frivilligt, endast om du aktiverar Pro-raden "Fokus-läge". Låter appen veta om iOS Fokus-läge är aktivt så att motsvarande rad kan visa På/Av. Datan stannar på dina enheter. |
| **Mikrofon** | Frivilligt, endast om du aktiverar Pro-funktionen "Lokaliseringssignal" under Mer → Inställningar → Lokaliseringssignal. iOS kräver mikrofonbehörighet för att vi ska kunna använda den ljudkategori som låter oss dirigera lokaliseringssignalens ljud till iPhones inbyggda högtalare, så att du kan höra signalen även när AirPods eller hörlurar med sladd är anslutna. **Mikrofonen spelas aldrig in, lyssnas aldrig på och används aldrig för någon ljudinmatning.** Om du nekar behörigheten fungerar lokaliseringssignalen ändå — den spelas bara via den utgång iOS normalt skulle dirigera till (vanligen dina hörlurar om de är anslutna). |

Du kan när som helst återkalla dessa behörigheter i **Inställningar → Wrist Buddy** på din iPhone. Den motsvarande funktionen slutar då helt enkelt fungera; inget annat i appen påverkas.

---

## Köp i appen

Wrist Buddy erbjuder en engångs **Pro**-upplåsning via Apples standardsystem för köp i appen (StoreKit). När du gör ett köp:

- Transaktionen hanteras helt av Apple. Vi ser aldrig ditt namn, dina betaluppgifter, ditt Apple-ID eller andra personuppgifter kopplade till köpet.
- Apple kan skicka oss anonyma, aggregerade försäljningsrapporter via App Store Connect (t.ex. "X exemplar sålda i land Y den här månaden"). Dessa rapporter identifierar inte enskilda kunder.
- Pro-upplåsningen lagras lokalt på din enhet (i UserDefaults) och verifieras via Apples StoreKit-ramverk. Det finns inget separat konto eller separat inloggning.

Du kan återställa ditt Pro-köp på en ny eller återställd enhet genom att trycka på **Återställ köp** i appen — Apple identifierar rättigheten via ditt Apple-ID utan att vi får veta din identitet.

---

## Barns integritet

Wrist Buddy har åldersgränsen **4+** på App Store och passar alla åldrar. Appen samlar inte medvetet in personuppgifter från någon, inklusive barn under 13 år.

---

## Tredjepartstjänster

Wrist Buddy använder **inga tredjepartstjänster, -SDK:er, -ramverk eller -nätverk**. Appens körtidsberoenden begränsar sig till Apples egna iOS- och watchOS-systemramverk. Det finns inga analystjänster, inga annonsnätverk och inga kraschrapporteringstjänster utöver Apples egna (som är anonyma och frivilliga på iOS-nivå, och inte något Wrist Buddy aktiverar på egen hand).

---

## Internationella dataöverföringar

Eftersom Wrist Buddy varken samlar in eller överför data finns det inga internationella dataöverföringar att redovisa. All appdata stannar på dina personliga enheter.

---

## Dina rättigheter (EU / GDPR)

Appens design innebär att det inte finns någon behandling av personuppgifter att agera på. För tydlighetens skull:

- **Rätt till tillgång**: vi har inga personuppgifter om dig.
- **Rätt till rättelse / radering**: det finns inga uppgifter att rätta eller ta bort hos oss. För att ta bort all appdata från din enhet räcker det att ta bort Wrist Buddy — iOS tar bort den lokala UserDefaults samtidigt.
- **Rätt till dataportabilitet**: ej tillämpligt, eftersom vi inte sparar några personuppgifter.
- **Rätt att invända / begränsa behandlingen**: ej tillämpligt, eftersom vi inte utför någon behandling av personuppgifter.
- **Rätt att lämna in klagomål**: om du ändå anser att vi har hanterat data felaktigt kan du kontakta din nationella dataskyddsmyndighet. I Sverige är det **Integritetsskyddsmyndigheten (IMY)** (https://www.imy.se). I Spanien är det **Agencia Española de Protección de Datos** (https://www.aepd.es).

---

## Ändringar i denna policy

Om vi någon gång ändrar hur Wrist Buddy hanterar data — till exempel om vi lägger till en funktion som kräver en ny behörighet — uppdaterar vi denna policy och datumet för "Senast uppdaterad" högst upp. Väsentliga ändringar speglas också i App Stores integritetsetikett, som Apple visar på appens sida.

---

## Kontakt

För integritetsfrågor, feedback eller för att utöva någon av rättigheterna ovan, kontakta:

**Mario Longhi** — wristbuddyapp+policy@gmail.com

Vi strävar efter att besvara integritetsfrågor inom 14 dagar.
