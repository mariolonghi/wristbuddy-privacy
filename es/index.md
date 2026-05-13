---
layout: default
title: Wrist Buddy — Política de Privacidad
description: Política de privacidad de la app Wrist Buddy para iPhone y Apple Watch.
lang: es
permalink: /es/
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Política de Privacidad

**Fecha de entrada en vigor:** {{ page.effective_date }}
**Última actualización:** {{ page.last_updated }}

Wrist Buddy es una app utilitaria para iPhone y Apple Watch que muestra el estado de tu iPhone (batería, carga, red, movimiento, modo silencio / Concentración, distancia) en tu Apple Watch. Esta política explica qué datos maneja la app y por qué — es breve porque la respuesta es «casi ninguno».

El desarrollador de Wrist Buddy es **Mario Longhi**, un desarrollador independiente con sede en España (UE). En este documento, «nosotros» hace referencia a la app Wrist Buddy y a su desarrollador.

---

## Resumen

- Wrist Buddy **no recopila datos personales**.
- Wrist Buddy **no envía datos** a ningún servidor, nube ni tercero.
- Todos los datos intercambiados entre tu iPhone y tu Apple Watch permanecen en tus dispositivos, enviándose únicamente entre ambos a través del framework WatchConnectivity de Apple (Bluetooth o Wi-Fi local).
- Wrist Buddy no contiene analítica, publicidad, seguimiento ni SDK de terceros.
- Nuestra etiqueta de privacidad en App Store es **«Datos no recopilados»** — todas las categorías sin marcar.

---

## Información que no recopilamos

Queremos ser específicos sobre lo que *no* hacemos, porque la ausencia de recopilación de datos es la decisión central de diseño:

- **No** recopilamos tu nombre, dirección de correo, número de teléfono ni ningún otro dato identificativo.
- **No** te pedimos que crees una cuenta ni que inicies sesión.
- **No** recopilamos identificadores de dispositivo, identificadores de publicidad (IDFA) ni similares.
- **No** rastreamos tu ubicación.
- **No** rastreamos tu uso de la app, no almacenamos informes de fallos en nuestros servidores ni utilizamos ningún servicio de analítica.
- **No** compartimos, vendemos ni transmitimos datos a terceros — porque no tenemos datos que compartir.
- **No** almacenamos tus datos en iCloud, en nuestros servidores ni en los de nadie más.

---

## Cómo funciona la app (flujo de datos)

Wrist Buddy lee cierta información de tu iPhone y de tu Apple Watch a través de los frameworks estándar del sistema de Apple, y la muestra en la interfaz de la app. Nada de esta información sale de tus dispositivos:

| Información mostrada | Cómo se lee | Dónde permanece |
|---|---|---|
| Porcentaje de batería y estado de carga del iPhone | API de batería de iOS | En el iPhone; se envía a tu Apple Watch emparejado mediante WatchConnectivity |
| Estado de conectividad Wi-Fi y celular | Framework Network de Apple | Igual que arriba |
| Si el iPhone está en movimiento | Sensor de movimiento del iPhone (con tu permiso) | Igual que arriba |
| Si el iPhone está en silencio / en modo Concentración | API de audio y Concentración de iOS | Igual que arriba |
| Distancia entre el iPhone y el Apple Watch | Framework NearbyInteraction (UWB) de Apple — función Pro, requiere hardware compatible | Calculada localmente en cada dispositivo; nunca se transmite fuera del dispositivo |
| Porcentaje de batería y estado de carga del Apple Watch | API de batería de watchOS | En el Watch; se envía al iPhone mediante WatchConnectivity para la pantalla de estado «Apple Watch» (función Pro) |

**WatchConnectivity** es el framework integrado de Apple para la comunicación directa entre iPhone y Apple Watch. Usa Bluetooth o Wi-Fi local entre tus dos dispositivos. No enruta datos a través de ningún servidor.

**Un identificador generado aleatoriamente** se crea en tu dispositivo la primera vez que se inicia la app, se almacena solo en el UserDefaults local y se utiliza únicamente para etiquetar los correos salientes de «Sugerir una función» y poder correlacionar mensajes de la misma instalación si decides enviarnos seguimiento. Este identificador nunca sale de tu dispositivo a menos que toques explícitamente «Sugerir una función» y envíes el correo tú mismo.

---

## Permisos que Wrist Buddy puede solicitar

iOS exige que las apps pidan permiso antes de acceder a ciertas capacidades. Wrist Buddy solicita los siguientes, todos opcionales y usados solo para las funciones descritas:

| Permiso | Por qué lo pedimos |
|---|---|
| **Movimiento y estado físico** | Para detectar si tu iPhone está en movimiento (lectura del acelerómetro). Se usa solo para la fila de estado «Detección de movimiento». El acelerómetro se muestrea bajo demanda — solo brevemente cuando se actualiza la app del Watch — nunca de forma continua. |
| **Notificaciones** | Solo si activas la función Pro «Avisos de batería». Se usan para enviarte notificaciones locales cuando tu iPhone esté completamente cargado o caiga por debajo del 20 % de batería. Las notificaciones se generan íntegramente en tu dispositivo — sin intervención de servidor. |
| **Estado de Concentración** | Opcional, solo si activas la fila Pro «Modo Concentración». Permite que la app sepa si el modo Concentración de iOS está activo para que la fila correspondiente muestre Activado/Desactivado. Los datos permanecen en tus dispositivos. |
| **Micrófono** | Opcional, solo si activas la función Pro «Anillo localizador» en Más → Ajustes → Anillo localizador. iOS exige el permiso de micrófono para usar la categoría de audio que nos permite enrutar el sonido del anillo localizador hacia el altavoz integrado del iPhone, de modo que puedas oír el aviso incluso si tienes AirPods o auriculares con cable conectados. **El micrófono nunca se graba, no se escucha y no se utiliza para ninguna entrada de audio.** Si rechazas el permiso, el anillo localizador sigue funcionando — simplemente sonará por la salida que iOS enrute habitualmente (normalmente tus auriculares si están conectados). |

Puedes revocar cualquiera de estos permisos en cualquier momento en **Ajustes → Wrist Buddy** en tu iPhone. La función correspondiente simplemente dejará de funcionar; nada más en la app se verá afectado.

---

## Compras integradas

Wrist Buddy ofrece un desbloqueo **Pro** único a través del sistema estándar de compras integradas de Apple (StoreKit). Cuando realizas una compra:

- La transacción la gestiona íntegramente Apple. Nunca vemos tu nombre, datos de pago, ID de Apple ni ningún otro dato personal asociado a la compra.
- Apple puede enviarnos informes de ventas anónimos y agregados a través de App Store Connect (por ejemplo, «se vendieron X copias en el país Y este mes»). Estos informes no identifican a clientes individuales.
- El desbloqueo Pro se almacena localmente en tu dispositivo (en UserDefaults) y se verifica mediante el framework StoreKit de Apple. No hay cuenta ni inicio de sesión separado.

Puedes restaurar tu compra Pro en un dispositivo nuevo o reseteado tocando **Restaurar compras** en la app — Apple identifica el derecho a través de tu ID de Apple sin que nosotros conozcamos tu identidad.

---

## Privacidad de los menores

Wrist Buddy tiene una clasificación **4+** en App Store y es apta para todas las edades. La app no recopila a sabiendas información personal de nadie, incluidos los menores de 13 años.

---

## Servicios de terceros

Wrist Buddy **no utiliza servicios, SDK, frameworks ni redes de terceros**. Las dependencias de ejecución de la app se limitan a los frameworks del propio sistema de iOS y watchOS de Apple. No hay servicios de analítica, redes de publicidad ni servicios de informes de fallos más allá de los propios de Apple (que son anónimos y opcionales a nivel de iOS, no algo que Wrist Buddy active de forma independiente).

---

## Transferencias internacionales de datos

Como Wrist Buddy no recopila ni transmite datos, no hay transferencias internacionales de datos que comunicar. Todos los datos de la app permanecen en tus dispositivos personales.

---

## Tus derechos (UE / RGPD)

El diseño de la app implica que no hay tratamiento de datos personales sobre el que actuemos. Para ser explícitos:

- **Derecho de acceso**: no tenemos datos personales sobre ti.
- **Derecho de rectificación / supresión**: no hay datos que corregir o eliminar por nuestra parte. Para borrar todos los datos de la app de tu dispositivo, simplemente elimina Wrist Buddy — iOS retirará el UserDefaults local junto con ella.
- **Derecho a la portabilidad**: no aplicable, ya que no conservamos datos personales.
- **Derecho de oposición / limitación del tratamiento**: no aplicable, ya que no realizamos ningún tratamiento de datos personales.
- **Derecho a presentar una reclamación**: si aun así crees que hemos manejado mal los datos, puedes contactar con tu autoridad nacional de protección de datos. En España, es la **Agencia Española de Protección de Datos** (https://www.aepd.es).

---

## Cambios en esta política

Si alguna vez cambiamos cómo Wrist Buddy maneja los datos — por ejemplo, si añadimos una función que requiera un nuevo permiso — actualizaremos esta política y la fecha de «Última actualización» en la parte superior. Los cambios materiales también se reflejarán en la etiqueta de privacidad de App Store, que Apple muestra en la ficha de la app.

---

## Contacto

Para preguntas sobre privacidad, comentarios o para ejercer cualquiera de los derechos descritos arriba, contáctanos en:

**Mario Longhi** — wristbuddyapp+policy@gmail.com

Aspiramos a responder a las consultas de privacidad en un plazo de 14 días.
