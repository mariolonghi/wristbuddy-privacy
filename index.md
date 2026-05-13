---
layout: default
title: Wrist Buddy — Privacy Policy
description: Privacy Policy for the Wrist Buddy iPhone + Apple Watch app.
lang: en
permalink: /
# Single source of truth for the policy date. Translations declare their
# own `last_updated` in front matter; CI fails the build if any translation
# drifts from the English value. Bump this when you publish a material
# change AND make the matching update in every other locale.
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Privacy Policy

**Effective date:** {{ page.effective_date }}
**Last updated:** {{ page.last_updated }}

Wrist Buddy is an iPhone and Apple Watch utility app that displays your iPhone's status (battery, charging, network, motion, silent / Focus mode, distance) on your Apple Watch. This policy explains what data the app handles and why — kept short because the answer is "almost nothing."

The developer of Wrist Buddy is **Mario Longhi**, an independent developer based in Spain (EU). Throughout this document, "we" refers to the Wrist Buddy app and its developer.

---

## TL;DR

- Wrist Buddy collects **no personal data**.
- Wrist Buddy sends **no data** to any server, cloud, or third party.
- All data exchanged between your iPhone and Apple Watch stays on your devices, sent only between the two via Apple's WatchConnectivity framework (Bluetooth or local Wi-Fi).
- Wrist Buddy contains no analytics, no advertising, no tracking, and no third-party SDKs.
- Our App Store privacy nutrition label is **"Data Not Collected"** — every category unchecked.

---

## Information we do not collect

We want to be specific about what we do *not* do, because the absence of data collection is the central design choice:

- We do **not** collect your name, email address, phone number, or any other identifying information.
- We do **not** require you to create an account or sign in.
- We do **not** collect device identifiers, advertising identifiers (IDFA), or similar.
- We do **not** track your location.
- We do **not** track your usage of the app, store crash reports on our servers, or use any analytics service.
- We do **not** share, sell, or transmit data to any third party — because we do not have any data to share.
- We do **not** store your data in iCloud, on our servers, or on anyone else's servers.

---

## How the app works (data flow)

Wrist Buddy reads certain information from your iPhone and Apple Watch through Apple's standard system frameworks, and displays it in the app interface. None of this information leaves your devices:

| Information shown | How it's read | Where it stays |
|---|---|---|
| iPhone battery percentage and charging state | iOS battery APIs | On the iPhone; sent to your paired Apple Watch via WatchConnectivity |
| Wi-Fi and cellular connectivity status | Apple's Network framework | Same as above |
| Whether the iPhone is moving | iPhone motion sensor (with your permission) | Same as above |
| Whether the iPhone is on silent / in Focus mode | iOS audio + Focus APIs | Same as above |
| Distance between iPhone and Apple Watch | Apple's NearbyInteraction (UWB) framework — Pro feature, requires compatible hardware | Computed locally on each device; never transmitted off-device |
| Apple Watch battery percentage and charging state | watchOS battery APIs | On the Watch; sent to your iPhone via WatchConnectivity for the "Apple Watch" status screen (Pro feature) |

**WatchConnectivity** is Apple's built-in framework for direct iPhone↔Apple Watch communication. It uses Bluetooth or local Wi-Fi between your two devices. It does not route data through any server.

**A randomly generated identifier** is created on your device the first time the app launches, stored only in the app's local UserDefaults, and used solely to label outgoing "Suggest a feature" feedback emails so we can correlate emails from the same install if you choose to send us follow-up messages. This identifier never leaves your device unless you explicitly tap "Suggest a feature" and send the email yourself.

---

## Permissions Wrist Buddy may request

iOS requires apps to ask for permission before accessing certain capabilities. Wrist Buddy requests the following, all opt-in, all only used for the features described:

| Permission | Why we ask |
|---|---|
| **Motion & Fitness** | To detect whether your iPhone is currently moving (accelerometer reading). Used only for the "Motion detection" status row. The accelerometer is sampled on-demand — only briefly when the Watch app is refreshed — never continuously. |
| **Notifications** | Only if you enable the Pro "Battery alerts" feature. Used to send you local notifications when your iPhone is fully charged or drops below 20% battery. Notifications are generated entirely on your device — no server involvement. |
| **Focus Status** | Optional, only if you enable the Pro "Focus mode" status row. Lets the app know whether iOS Focus mode is active so the corresponding row can show On/Off. The data stays on your devices. |
| **Microphone** | Optional, only if you enable the Pro "Locator Ring" feature in More → Settings → Locator Ring. iOS requires the microphone permission to use the audio category that lets us route the locator ring sound to the iPhone's built-in speaker, so you can hear the ring even when AirPods or wired headphones are connected. **The microphone is never recorded, listened to, or used for any audio input.** If you decline the permission, the locator ring still works — it just plays through whichever output iOS would normally route to (typically your headphones if connected). |

You can revoke any of these permissions at any time in **Settings → Wrist Buddy** on your iPhone. The corresponding feature will simply stop working; nothing else in the app is affected.

---

## In-App Purchases

Wrist Buddy offers a one-time **Pro** unlock through Apple's standard In-App Purchase system (StoreKit). When you make a purchase:

- The transaction is handled entirely by Apple. We never see your name, payment information, Apple ID, or any other personal data associated with the purchase.
- Apple may send us anonymous, aggregated sales reports through App Store Connect (e.g., "X copies sold in country Y this month"). These reports do not identify individual customers.
- The Pro unlock is stored locally on your device (in UserDefaults) and verified through Apple's StoreKit framework. There is no separate account or login.

You can restore your Pro purchase on a new or reset device by tapping **Restore Purchases** in the app — Apple identifies the entitlement through your Apple ID without us learning your identity.

---

## Children's privacy

Wrist Buddy is rated **4+** on the App Store and is suitable for all ages. The app does not knowingly collect personal information from anyone, including children under 13.

---

## Third-party services

Wrist Buddy uses **no third-party services, SDKs, frameworks, or networks**. The app's runtime dependencies are limited to Apple's own iOS and watchOS system frameworks. There are no analytics services, no advertising networks, no crash reporting services beyond Apple's own (which is anonymous and opt-in at the iOS level, not something Wrist Buddy enables independently).

---

## International data transfers

Because Wrist Buddy collects and transmits no data, there are no international data transfers to disclose. All app data stays on your personal devices.

---

## Your rights (EU / GDPR)

The app's design means there is no personal data processing for us to act on. To be explicit:

- **Right of access**: there is no personal data we hold about you.
- **Right to rectification / erasure**: there is no data to correct or delete on our end. To remove all app data from your device, simply delete the Wrist Buddy app — iOS will remove the local UserDefaults along with it.
- **Right to data portability**: not applicable, as we hold no personal data.
- **Right to object / restrict processing**: not applicable, as we conduct no processing of personal data.
- **Right to lodge a complaint**: if you nonetheless believe we have mishandled data, you may contact your national data protection authority. In Spain, that is the **Agencia Española de Protección de Datos** (https://www.aepd.es).

---

## Changes to this policy

If we ever change how Wrist Buddy handles data — for instance, if we add a feature that requires a new permission — we will update this policy and the "Last updated" date at the top. Material changes will also be reflected in the App Store privacy nutrition label, which Apple displays on the app's listing.

---

## Contact

For privacy questions, feedback, or to exercise any of your rights described above, please contact:

**Mario Longhi** — wristbuddyapp+policy@gmail.com

We aim to respond to privacy inquiries within 14 days.
