# Arquitetura

## Componentes

O frontend é construído a partir de componentes web. Eles são definidos nos arquivos Javascript no diretório `src`.

Normalmente, cada arquivo define um componente, começando com
```javascript
class GrampsjsSomeElement extends LitElement
```
e terminando com
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
que define o novo elemento HTML `grampsjs-some-element` que pode ser usado em outros lugares.

O ponto de entrada principal, incluído em `index.html`, é o elemento `gramps-js` definido em `GrampsJs.js`. Isso contém a definição de todas as páginas individuais (que correspondem simplesmente a elementos que são mostrados ou ocultos com base na rota/URL), o menu e o roteamento.

Os componentes no diretório `src/views` geralmente correspondem a componentes de página inteira que buscam dados do backend (por exemplo, a visualização da lista de pessoas), enquanto os componentes em `src/components` são geralmente blocos de construção menores usados dentro das visualizações que obtêm seus dados de atributos fornecidos pelo seu elemento pai. No entanto, essa separação não é estrita.

## Fluxo de dados

Os dados são trocados com o Backend/API através dos métodos `apiGet`, `apiPut` e `apiPost` em `src/api.js`, que cuidam automaticamente da autenticação.

Os dados são passados de componentes pai para componentes filho através de propriedades (veja, por exemplo, a [documentação do Lit](https://lit.dev/docs/components/properties/)).

Quando os dados precisam ser enviados de volta de um componente filho para um componente pai, eventos personalizados são usados, que podem ser disparados com a função `fireEvent` em `src/api.js` e ouvidos usando a sintaxe `@` do Lit [(docs)](https://lit.dev/docs/components/events/).

## Autenticação

O token de atualização e o token de autenticação são armazenados no armazenamento local do navegador. Sempre que uma chamada de API é feita e o token está expirado, o token de atualização armazenado é usado para buscar um novo token de acesso e a chamada de API é repetida.

O escopo de autorização do usuário, que é armazenado nas reivindicações do token de acesso, é obtido com a função `getPermissions` e usado no elemento de nível superior `GrampsJs` para definir as propriedades booleanas `canAdd`, `canEdit`, `canManageUsers`, que são passadas para os elementos filhos para implementar funcionalidades específicas de autorização.
