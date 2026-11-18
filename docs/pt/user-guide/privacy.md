# Registros privados

Qualquer registro na árvore pode ser marcado como privado. Juntamente com os [papéis de usuário](../install_setup/users.md#user-roles), isso decide quem vê o quê.

## Quem pode ver o quê

O Gramps Web nunca está aberto ao público: apenas usuários com uma conta podem ver qualquer coisa. "Público" no Gramps simplesmente significa "não privado", ou seja, visível para todos os usuários logados na árvore.

| Papel | Registros públicos | Registros privados |
|---|---|---|
| Convidado | ver | – |
| Membro | ver | ver |
| Contribuidor | ver, adicionar | ver, adicionar |
| Editor, Proprietário, Administrador | ver, adicionar, editar, excluir | ver, adicionar, editar, excluir |

Para convidados, registros privados não existem: eles são excluídos de páginas, listas, resultados de busca, gráficos, relatórios, exportações e respostas do assistente de IA. Isso é aplicado onde o servidor lê o banco de dados, não escondendo coisas no aplicativo, de modo que um convidado não possa acessar dados privados de nenhuma outra maneira.

Contas que ainda não foram aprovadas (após [auto-registro](registration.md)) não podem fazer login de forma alguma.

Portanto, se parentes ou outras pessoas com uma conta de convidado não devem ver certas informações, marque-as como privadas. Se todos os usuários de uma árvore podem ver tudo, dê a eles o papel de membro (ou superior) e não há necessidade de marcar nada como privado.

## Pessoas vivas não são privadas automaticamente

Nada é tornado privado automaticamente – nem mesmo pessoas que ainda estão vivas. Dados de pessoas vivas são visíveis para convidados até que você os marque como privados. Isso também se aplica a árvores importadas.

Para tornar as pessoas que provavelmente estão vivas privadas no Gramps Web:

1. Na lista de pessoas, abra o [filtro avançado](lists.md#advanced-filter) e adicione a condição "Pessoas provavelmente vivas" (deixe a data vazia para hoje). Aplique o filtro.
2. Clique em **Selecionar**, marque a caixa de seleção no cabeçalho e escolha **Selecionar Tudo**.
3. Escolha a ação **Privacidade** e marque os registros como privados.

"Provavelmente vivas" é estimado a partir das datas da pessoa e de seus parentes. Pessoas sem datas utilizáveis são consideradas vivas. Verifique o resultado e tenha em mente que a estimativa pode mudar à medida que você adiciona dados.

Marcar uma pessoa como privada oculta a pessoa, mas não seus eventos, notas, mídias ou famílias – veja abaixo. O Gramps Desktop possui mais ferramentas para definir a privacidade de muitos registros relacionados de uma só vez, que você pode usar com o [addon Sync](../administration/sync.md).

Pessoas que morrem depois também não se tornam públicas automaticamente. Se você deseja isso, depende de você – muitos pesquisadores preferem manter as informações coletadas privadas por algum tempo.

## Lendo os ícones de bloqueio

Usuários que podem visualizar dados privados veem um cadeado ao lado de itens privados. Existem dois tipos:

- **Cadeado preenchido** – o registro em si é privado. Na página de uma pessoa, por exemplo, um cadeado preenchido ao lado de um evento significa que o evento é privado, e ao lado de uma criança que a criança é privada.
- **Cadeado contornado** – apenas o *link* é privado, não o registro ao qual ele leva. Por exemplo, o link de uma pessoa para um evento pode ser privado enquanto o evento em si é público. O evento é então ocultado da página daquela pessoa, mas ainda visível em outros lugares, como nas páginas de outros participantes ou na lista de eventos.

Se tanto o registro quanto seu link forem privados, o cadeado preenchido é exibido.

A mesma distinção se aplica a crianças (a criança ou o link da criança para a família), associações, links de repositório de uma fonte e mídias em uma galeria. Nomes, atributos, endereços e URLs pertencem ao seu registro e só têm o cadeado preenchido.

## Tornando algo privado

Você precisa de permissões de edição para alterar a privacidade.

- **Um registro inteiro**: abra sua página, entre no modo de edição e clique no botão de cadeado na barra de ferramentas.
- **Parte de um registro** – um nome alternativo, atributo, endereço, URL, associação, link de criança ou link de repositório: abra a caixa de diálogo de edição desse item e ative o interruptor **Privado**. O nome principal não tem interruptor, pois a pessoa apareceria como "Privada".
- **Um evento da página de uma pessoa ou família**: a caixa de diálogo de edição do evento tem um interruptor de privacidade para o evento em si. Se o evento for compartilhado com outras pessoas, ele só se torna editável após **Editar para todos**, já que é privado para todos eles.
- **O link de uma pessoa para um evento**: na página do evento, abra a linha do participante em modo de edição. O interruptor de privacidade lá se aplica apenas ao link daquele participante, de modo que o evento permaneça visível para os outros participantes.
- **Um objeto de mídia em uma galeria**: no modo de edição, clique no cadeado no canto do bloco.
- **Muitos registros de uma vez**: selecione-os em uma lista e use a ação **Privacidade**, veja [Listas](lists.md#tags-and-privacy).

Para verificar quais registros em uma lista são privados, ative a coluna **Privacidade** no seletor de colunas da lista.

## Coisas a ter em mente

- Tornar um registro privado não torna os registros aos quais ele está vinculado privados. Se uma pessoa é privada, seus eventos, as famílias a que pertencem e as notas anexadas a eles ainda são visíveis, a menos que sejam privadas também. Use o filtro avançado ou a coluna **Privacidade** para verificar registros relacionados.
- Tornar uma família ou evento privado o oculta, mas não as pessoas nele.
- [Combinações de DNA e dados de Y-DNA](dna-matches.md#private-matches) têm seu próprio interruptor **Privado** em suas caixas de diálogo.
- Exportações e arquivos de mídia feitos por um usuário que não pode visualizar dados privados não contêm registros ou arquivos privados.
- A privacidade é um recurso do Gramps, portanto, registros marcados como privados no Gramps Desktop são privados no Gramps Web também, e vice-versa.
