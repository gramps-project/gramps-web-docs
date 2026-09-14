# Histórico de Revisões

A visualização do histórico de revisões mostra todas as edições que foram feitas na árvore genealógica.

A visualização em lista mostra as edições agrupadas por "transações". Uma transação é um grupo de uma ou mais adições, exclusões ou alterações em objetos do Gramps. Por exemplo, adicionar uma nova família com duas pessoas existentes como pai e mãe gera uma transação com um objeto de família adicionado e dois objetos de pessoa modificados (porque eles contêm o link para o novo objeto de família).

Clicar em uma transação abre a visualização de detalhes da transação. Ela contém a lista de adições, exclusões e atualizações individuais por objeto do Gramps.

Selecionar uma alteração individual abre uma visualização da representação JSON bruta do objeto do Gramps, com adições e exclusões destacadas em verde e vermelho, respectivamente. Um botão acima do diff leva você diretamente à página do próprio objeto.

## Revisões de um único objeto

Para ver o histórico de uma pessoa, família, evento ou outro objeto em particular, abra sua página e mude para a aba **Revisões**. Ela lista cada alteração feita naquele objeto, da mais nova para a mais antiga, com o tipo de alteração (adicionada, atualizada ou excluída), o usuário que a fez e quando. Clicar em uma entrada abre a transação à qual pertence, onde você pode inspecionar o diff ou desfazê-lo.

Clique em **Mostrar mais** para carregar entradas mais antigas; para objetos com um histórico muito longo, apenas as revisões mais recentes são mostradas. Para objetos alterados pela última vez antes do histórico de revisões ser registrado, a aba mostra apenas o horário da última alteração.

!!! nota
    A aba Revisões é visível para membros e acima e requer a versão 3.22 ou posterior da API Web do Gramps.

## Desfazendo uma revisão

Na página de detalhes da transação, um botão **Desfazer** permite que você reverta essa transação. Clicar nele verifica se o desfazer pode ser realizado de forma limpa.

**Desfazer limpo** – se nenhum dos objetos afetados pela transação foi modificado desde então, o desfazer pode prosseguir sem risco. Um diálogo de confirmação é exibido e clicar em **Desfazer** reverte a transação.

**Forçar necessário** – se um ou mais objetos afetados foram modificados por uma transação posterior, um desfazer limpo não é possível. O diálogo avisa que forçar o desfazer pode resultar em inconsistências de dados, uma vez que alterações posteriores que dependem dos objetos em questão serão preservadas como estão, mesmo que os objetos subjacentes estejam sendo revertidos. Você pode então cancelar ou clicar em **Forçar desfazer** para prosseguir assim mesmo.

Em ambos os casos, o desfazer é executado como uma tarefa em segundo plano e um indicador de progresso é exibido.
