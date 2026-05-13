---
layout: default
title: Wrist Buddy — Política de Privacidade
description: Política de Privacidade do app Wrist Buddy para iPhone e Apple Watch.
lang: pt-BR
permalink: /pt-br/
effective_date: 2026-05-13
last_updated: 2026-05-13
---

# Wrist Buddy — Política de Privacidade

**Data de vigência:** {{ page.effective_date }}
**Última atualização:** {{ page.last_updated }}

O Wrist Buddy é um app utilitário para iPhone e Apple Watch que mostra o estado do seu iPhone (bateria, carregamento, rede, movimento, modo silencioso / Foco, distância) no seu Apple Watch. Esta política explica quais dados o app manipula e por quê — é curta porque a resposta é "quase nenhum".

O desenvolvedor do Wrist Buddy é o **Mario Longhi**, um desenvolvedor independente sediado na Espanha (UE). Ao longo deste documento, "nós" se refere ao app Wrist Buddy e ao seu desenvolvedor.

---

## Resumo

- O Wrist Buddy não coleta **nenhum dado pessoal**.
- O Wrist Buddy não envia **nenhum dado** para servidores, nuvem ou terceiros.
- Todos os dados trocados entre o seu iPhone e o seu Apple Watch ficam nos seus dispositivos, sendo enviados apenas entre os dois pelo framework WatchConnectivity da Apple (Bluetooth ou Wi-Fi local).
- O Wrist Buddy não contém análises, anúncios, rastreamento nem SDKs de terceiros.
- O nosso rótulo de privacidade na App Store é **"Dados não coletados"** — todas as categorias desmarcadas.

---

## Informações que não coletamos

Queremos ser específicos sobre o que *não* fazemos, porque a ausência de coleta de dados é a decisão central de design:

- **Não** coletamos seu nome, endereço de e-mail, número de telefone ou qualquer outra informação identificadora.
- **Não** exigimos que você crie uma conta ou faça login.
- **Não** coletamos identificadores de dispositivo, identificadores de publicidade (IDFA) ou similares.
- **Não** rastreamos sua localização.
- **Não** rastreamos o seu uso do app, não armazenamos relatórios de falhas em nossos servidores nem usamos qualquer serviço de análise.
- **Não** compartilhamos, vendemos nem transmitimos dados a terceiros — porque não temos dados para compartilhar.
- **Não** armazenamos seus dados no iCloud, em nossos servidores nem nos de terceiros.

---

## Como o app funciona (fluxo de dados)

O Wrist Buddy lê certas informações do seu iPhone e do seu Apple Watch por meio dos frameworks padrão do sistema da Apple, e as exibe na interface do app. Nenhuma dessas informações sai dos seus dispositivos:

| Informação exibida | Como é lida | Onde permanece |
|---|---|---|
| Porcentagem de bateria e estado de carregamento do iPhone | APIs de bateria do iOS | No iPhone; enviada ao seu Apple Watch pareado via WatchConnectivity |
| Estado de conectividade Wi-Fi e celular | Framework Network da Apple | Mesma coisa que acima |
| Se o iPhone está em movimento | Sensor de movimento do iPhone (com sua permissão) | Mesma coisa que acima |
| Se o iPhone está no silencioso / em modo Foco | APIs de áudio e Foco do iOS | Mesma coisa que acima |
| Distância entre o iPhone e o Apple Watch | Framework NearbyInteraction (UWB) da Apple — recurso Pro, requer hardware compatível | Calculada localmente em cada dispositivo; nunca transmitida para fora do dispositivo |
| Porcentagem de bateria e estado de carregamento do Apple Watch | APIs de bateria do watchOS | No Watch; enviada ao iPhone via WatchConnectivity para a tela de estado "Apple Watch" (recurso Pro) |

**WatchConnectivity** é o framework integrado da Apple para comunicação direta entre iPhone e Apple Watch. Usa Bluetooth ou Wi-Fi local entre os seus dois dispositivos. Não roteia dados por nenhum servidor.

**Um identificador gerado aleatoriamente** é criado no seu dispositivo na primeira vez em que o app é aberto, armazenado apenas no UserDefaults local e usado exclusivamente para identificar e-mails de "Sugerir um recurso" enviados, para que possamos correlacionar e-mails da mesma instalação caso você decida nos enviar mensagens de acompanhamento. Esse identificador nunca sai do seu dispositivo a menos que você toque explicitamente em "Sugerir um recurso" e envie o e-mail você mesmo.

---

## Permissões que o Wrist Buddy pode solicitar

O iOS exige que os apps peçam permissão antes de acessar determinados recursos. O Wrist Buddy solicita as seguintes, todas opcionais e usadas apenas para os recursos descritos:

| Permissão | Por que pedimos |
|---|---|
| **Movimento e fitness** | Para detectar se o seu iPhone está atualmente em movimento (leitura do acelerômetro). Usado apenas para a linha de estado "Detecção de movimento". O acelerômetro é amostrado sob demanda — apenas brevemente quando o app do Watch é atualizado — nunca de forma contínua. |
| **Notificações** | Apenas se você ativar o recurso Pro "Alertas de bateria". Usado para enviar notificações locais quando o seu iPhone estiver totalmente carregado ou cair abaixo de 20% de bateria. As notificações são geradas inteiramente no seu dispositivo — sem envolvimento de servidor. |
| **Estado de Foco** | Opcional, apenas se você ativar a linha Pro "Modo Foco". Permite que o app saiba se o modo Foco do iOS está ativo para que a linha correspondente mostre Ativado/Desativado. Os dados ficam nos seus dispositivos. |
| **Microfone** | Opcional, apenas se você ativar o recurso Pro "Anel localizador" em Mais → Ajustes → Anel localizador. O iOS exige a permissão de microfone para usar a categoria de áudio que nos permite rotear o som do anel localizador para o alto-falante embutido do iPhone, de modo que você consiga ouvir o aviso mesmo quando AirPods ou fones com fio estiverem conectados. **O microfone nunca é gravado, ouvido nem usado para qualquer entrada de áudio.** Se você recusar a permissão, o anel localizador continua funcionando — apenas será reproduzido pela saída que o iOS rotearia normalmente (geralmente seus fones, se conectados). |

Você pode revogar qualquer uma dessas permissões a qualquer momento em **Ajustes → Wrist Buddy** no seu iPhone. O recurso correspondente simplesmente parará de funcionar; nada mais no app será afetado.

---

## Compras no aplicativo

O Wrist Buddy oferece um desbloqueio **Pro** único pelo sistema padrão de compras no aplicativo da Apple (StoreKit). Quando você faz uma compra:

- A transação é totalmente conduzida pela Apple. Nunca vemos seu nome, informações de pagamento, ID Apple nem qualquer outro dado pessoal associado à compra.
- A Apple pode nos enviar relatórios de vendas anônimos e agregados pelo App Store Connect (por exemplo, "X cópias vendidas no país Y neste mês"). Esses relatórios não identificam clientes individuais.
- O desbloqueio Pro é armazenado localmente no seu dispositivo (no UserDefaults) e verificado pelo framework StoreKit da Apple. Não há conta nem login separado.

Você pode restaurar sua compra Pro em um dispositivo novo ou redefinido tocando em **Restaurar compras** no app — a Apple identifica o direito por meio do seu ID Apple sem que conheçamos sua identidade.

---

## Privacidade de crianças

O Wrist Buddy é classificado como **4+** na App Store e é adequado para todas as idades. O app não coleta intencionalmente informações pessoais de ninguém, inclusive crianças menores de 13 anos.

---

## Serviços de terceiros

O Wrist Buddy **não usa serviços, SDKs, frameworks nem redes de terceiros**. As dependências de execução do app estão limitadas aos próprios frameworks de sistema do iOS e do watchOS da Apple. Não há serviços de análise, redes de publicidade nem serviços de relatório de falhas além dos da própria Apple (que são anônimos e opcionais no nível do iOS, e não algo que o Wrist Buddy ative de forma independente).

---

## Transferências internacionais de dados

Como o Wrist Buddy não coleta nem transmite dados, não há transferências internacionais de dados a divulgar. Todos os dados do app permanecem nos seus dispositivos pessoais.

---

## Seus direitos (UE / RGPD / LGPD)

O design do app significa que não há tratamento de dados pessoais sobre o qual possamos agir. Para deixar claro:

- **Direito de acesso**: não há dados pessoais sobre você em nosso poder.
- **Direito de retificação / eliminação**: não há dados a corrigir ou apagar do nosso lado. Para remover todos os dados do app do seu dispositivo, basta excluir o Wrist Buddy — o iOS removerá o UserDefaults local junto com ele.
- **Direito à portabilidade dos dados**: não aplicável, já que não retemos dados pessoais.
- **Direito de oposição / restrição do tratamento**: não aplicável, já que não realizamos tratamento de dados pessoais.
- **Direito de apresentar reclamação**: se ainda assim você acreditar que manipulamos dados de forma indevida, pode entrar em contato com a sua autoridade nacional de proteção de dados. No Brasil, é a **Autoridade Nacional de Proteção de Dados (ANPD)** (https://www.gov.br/anpd). Na Espanha, é a **Agencia Española de Protección de Datos** (https://www.aepd.es).

---

## Alterações nesta política

Se um dia mudarmos como o Wrist Buddy lida com dados — por exemplo, se adicionarmos um recurso que exija uma nova permissão — atualizaremos esta política e a data de "Última atualização" no topo. Mudanças relevantes também serão refletidas no rótulo de privacidade da App Store, que a Apple exibe na listagem do app.

---

## Contato

Para perguntas sobre privacidade, comentários ou para exercer qualquer um dos direitos descritos acima, entre em contato:

**Mario Longhi** — wristbuddyapp+policy@gmail.com

Buscamos responder a consultas sobre privacidade em até 14 dias.
