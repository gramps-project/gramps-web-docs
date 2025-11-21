---
hide:
  - toc
---

# Desenvolvimento do Gramps Web: visão geral

Gramps Web é uma aplicação web que consiste em dois componentes que são desenvolvidos separadamente:

- **Gramps Web API** é uma API RESTful escrita em Python e baseada em Flask. O código-fonte está hospedado em [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Ela gerencia o acesso ao banco de dados e funções genealógicas aproveitando diretamente a biblioteca Gramps Python. Serve como o backend do Gramps Web. Para a documentação de desenvolvimento, veja [Backend](backend/index.md).
- **Gramps Web Frontend** é uma aplicação web em Javascript que serve como o frontend do Gramps Web. O código-fonte está hospedado em [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Para a documentação de desenvolvimento, veja [Frontend](frontend/index.md).

Uma nota sobre versionamento: Gramps Web API e o frontend do Gramps Web são versionados de forma independente. No momento, "Gramps Web" – a aplicação combinada – não possui um número de versão separado. Ambos os projetos aderem ao [SemVer](https://semver.org/).

Se você não é um desenvolvedor Python ou Javascript, mas ainda gostaria de contribuir para o Gramps Web, confira [Contribute](../contribute/contribute.md).
