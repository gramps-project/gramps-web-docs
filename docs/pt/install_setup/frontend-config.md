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
`leafletTileUrl` | string | URL de tile personalizada para mapas Leaflet
`leafletTileSize` | número | Tamanho de tile personalizado para mapas Leaflet
`leafletZoomOffset` | número | Deslocamento de zoom personalizado para mapas Leaflet
`leafletTileAttribution` | string | Atribuição personalizada para mapas Leaflet
