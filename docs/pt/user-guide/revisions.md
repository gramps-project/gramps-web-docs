# Histórico de Revisões

A visualização do histórico de revisões mostra todas as edições que foram feitas na árvore genealógica.

A visualização em lista mostra as edições agrupadas por "transações". Uma transação é um grupo de uma ou mais adições, exclusões ou alterações em objetos Gramps. Por exemplo, adicionar uma nova família com duas pessoas existentes como pai e mãe gera uma transação com um objeto de família adicionado e dois objetos de pessoa modificados (porque eles contêm o link para o novo objeto de família).

Clicar em uma transação abre a visualização de detalhes da transação. Ela contém a lista de adições, exclusões e atualizações individuais por objeto Gramps.

Selecionar uma alteração individual abre uma visualização da representação JSON bruta do objeto Gramps, com adições e exclusões destacadas em verde e vermelho, respectivamente.

## Desfazendo uma revisão

Na página de detalhes da transação, um botão **Desfazer** permite reverter essa transação. Clicar nele verifica se o desfazer pode ser realizado de forma limpa.

**Desfazer limpo** – se nenhum dos objetos afetados pela transação foi modificado desde então, o desfazer pode prosseguir sem risco. Um diálogo de confirmação é exibido e clicar em **Desfazer** reverte a transação.

**Forçar necessário** – se um ou mais objetos afetados foram modificados por uma transação posterior, um desfazer limpo não é possível. O diálogo avisa que forçar o desfazer pode resultar em inconsistências de dados, uma vez que alterações posteriores que dependem dos objetos em questão serão preservadas como estão, mesmo que os objetos subjacentes estejam sendo revertidos. Você pode então cancelar ou clicar em **Forçar desfazer** para prosseguir de qualquer maneira.

Em ambos os casos, o desfazer é executado como uma tarefa em segundo plano e um indicador de progresso é exibido.
