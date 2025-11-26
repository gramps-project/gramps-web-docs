---
hide:
  - navigation
---

Se você encontrar problemas ou precisar de ajuda com o Gramps Web, por favor, escolha uma das opções a seguir.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Problemas de backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Problemas de frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Veja abaixo algumas orientações sobre onde começar.

## Fazendo perguntas

O fórum oficial do Gramps Discourse tem uma [categoria separada para o Gramps Web](https://gramps.discourse.group/c/gramps-web/). Por favor, use-a para fazer quaisquer perguntas que você possa ter sobre o Gramps Web, por exemplo:

- Perguntas sobre o uso do Gramps Web
- Perguntas sobre a configuração do Gramps Web
- Solução de problemas de uma implantação do Gramps Web
- Ideias sobre melhorias para o Gramps Web
- ...

## Reportando problemas

Se você encontrar um problema que acredita ser um bug no Gramps Web, por favor, relate-o via GitHub.

Existem dois repositórios GitHub separados para o código usado no Gramps Web, um para a interface do usuário (“frontend”) e um para o código do servidor (“backend”):

- [Problemas de frontend](https://github.com/gramps-project/gramps-web/issues)
- [Problemas de backend](https://github.com/gramps-project/gramps-web-api/issues)

Se você não tiver certeza de onde registrar um problema, não se preocupe e escolha qualquer um dos dois – os mantenedores poderão transferir o problema se necessário.

Em qualquer caso, por favor, inclua sempre as seguintes informações em seu relatório:

- Detalhes sobre sua configuração (por exemplo, um arquivo docker-compose com valores sensíveis ocultos, ou se você está usando uma versão hospedada, como o Grampshub, ou uma imagem pré-configurada, como a DigitalOcean)
- Informações sobre a versão. Para obtê-las, vá até a aba "Informações do sistema" na página de Configurações do Gramps Web e copie/cole os valores na caixa, que deve parecer algo assim:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Sugerindo melhorias

Para ideias gerais e discussões sobre melhorias futuras, sinta-se à vontade para abrir uma discussão no [fórum](https://gramps.discourse.group/c/gramps-web/). Você também pode querer verificar as páginas de problemas (veja os links acima) se uma funcionalidade específica já estiver planejada ou em desenvolvimento.

Para melhorias específicas com um escopo limitado, sinta-se à vontade para abrir diretamente um problema com um pedido de funcionalidade no repositório GitHub apropriado de frontend ou backend.
