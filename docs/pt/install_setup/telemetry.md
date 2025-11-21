# Telemetria

A partir da versão 3.2.0 da Gramps Web API, o Gramps Web envia, por padrão, dados de telemetria totalmente anônimos a cada 24 horas para um endpoint de análise controlado pela equipe do Gramps Web. Esta página contém informações sobre os dados de telemetria coletados, como eles são usados e como desativá-los, se desejado.

## Quais dados são coletados?

Os dados de telemetria são um pequeno payload JSON da seguinte forma:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Como você pode verificar [no código-fonte](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), os identificadores do servidor e da árvore são únicos para o servidor e a árvore, mas não contêm nenhuma informação pessoal identificável. O `timestamp` é o horário atual como um timestamp Unix.

## Por que os dados são coletados?

O envio de um identificador único uma vez por dia permite que a equipe do Gramps Web acompanhe quantos servidores únicos estão executando o Gramps Web e quantas árvores únicas estão sendo usadas.

Isso é importante para entender o impacto em serviços externos que são utilizados pelo Gramps Web, como os tiles de mapa.

## Como os dados são coletados?

Quando uma solicitação é feita ao seu servidor Gramps Web API, ele verifica se a telemetria foi enviada nas últimas 24 horas (verificando uma chave no cache local). Se não, o payload acima é enviado para um endpoint que registra os dados.

O endpoint de registro está hospedado no Google Cloud Run e é diretamente implantado a partir de um [repositório de código aberto](https://github.com/DavidMStraub/cloud-run-telemetry), para que você possa inspecionar como os dados são processados.

## O que será feito com os dados?

Antes de mais nada, nenhum dado além do payload anônimo, que poderia hipoteticamente ser coletado (como o endereço IP do servidor), será usado pela equipe do Gramps Web.

Os IDs anônimos coletados e o timestamp serão agregados para produzir gráficos como:

- Número de instalações ativas do Gramps Web em função do tempo
- Número de árvores ativas do Gramps Web em função do tempo

Esses gráficos serão publicados no site de documentação do Gramps Web.

## Como desativar a telemetria?

Uma vez que os dados estatísticos são úteis para a equipe do Gramps Web e garantimos que nenhum dado pessoal identificável é enviado, **ficaríamos gratos se você não desativasse a telemetria!**

No entanto, o Gramps Web coloca os usuários em total controle, então, é claro, você pode escolher desativar o recurso se desejar.

Para fazer isso, basta definir a opção de configuração `DISABLE_TELEMETRY` como `True` (por exemplo, definindo a variável de ambiente `GRAMPSWEB_DISABLE_TELEMETRY` como `true` &ndash; consulte a [documentação de configuração](configuration.md) para mais detalhes).
