# Personalizando o frontend

O frontend do Gramps Web é uma aplicação Javascript que é implantada como um conjunto de arquivos estáticos HTML, CSS e Javascript. Normalmente, nenhuma configuração especial é necessária para o frontend. No entanto, alguns comportamentos podem ser alterados definindo opções apropriadas no arquivo `config.js` na raiz da distribuição.

O arquivo deve ter a seguinte estrutura:

```javascript
window.grampsjsConfig = {
    option: value
}
```

As seguintes chaves de opção existem.

Chave | Tipo | Descrição 
----|-----|-----------
`hideDNALink` | booleano | Se verdadeiro, oculta o link de DNA na barra de navegação.
`hideRegisterLink` | booleano | Se verdadeiro, oculta o link de registro na página de login. Isso deve ser usado para implantações de múltiplas árvores.
`loginRedirect` | string | URL para redirecionar quando não estiver logado e navegando para qualquer página que não seja "login" ou "register"
`mapBaseStyleLight` | string | URL de estilo MapLibre para o mapa base no tema claro (padrão: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL de estilo MapLibre para o mapa base no tema escuro (padrão: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL de estilo MapLibre para a sobreposição OpenHistoricalMap (padrão: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
