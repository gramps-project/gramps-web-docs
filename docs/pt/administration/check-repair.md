# Verificar e validar dados

A seção **Processamento da Árvore Genealógica** nas [configurações de administração](settings.md) contém duas ferramentas que verificam a árvore genealógica: uma para problemas técnicos no banco de dados e outra para dados implausíveis.

## Verificar e Reparar Banco de Dados

Esta ferramenta verifica o banco de dados do Gramps em busca de inconsistências internas e corrige aquelas que pode – análoga à ferramenta [Verificar e Reparar Banco de Dados](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) no Gramps Desktop.

Clique em **Verificar e Reparar** e aguarde a conclusão do indicador de progresso. O resultado é exibido abaixo do botão:

- Se nenhum erro for encontrado, uma mensagem de confirmação é exibida.
- Se erros forem encontrados, um resumo das correções aplicadas é mostrado.

Execute esta ferramenta se você encontrar erros ou comportamentos inesperados que possam ser causados por inconsistências no banco de dados, como relacionamentos ausentes entre objetos.

## Validar os Dados

Enquanto a [Verificar e Reparar Banco de Dados](#check-and-repair-database) procura por inconsistências *técnicas*, esta ferramenta procura por dados *implausíveis* – análoga à ferramenta [Validar os Dados](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) no Gramps Desktop. Ela relata coisas que não são impossíveis, mas são improváveis o suficiente para merecer uma segunda olhada, como uma mãe com 12 anos ou uma pessoa que viveu até os 130 anos.

Sob **Opções**, você pode ajustar os limites que os testes utilizam – idade máxima, idade mínima e máxima para casar ou ter filhos, número máximo de filhos, e assim por diante – assim como se deseja estimar datas ausentes ou imprecisas e se deseja relatar datas inválidas, como 31 de fevereiro. As opções que você altera são lembradas em seu navegador para a próxima execução; **Redefinir** restaura os padrões.

Clique em **Validar os Dados** para começar. A verificação é executada como uma tarefa em segundo plano, e os resultados são listados sob **Resultados da Verificação de Dados**. Nada é alterado por esta ferramenta: ela apenas relata o que encontra.

!!! nota
    Um achado não é prova de um erro. Vidas longas e grandes diferenças de idade realmente ocorrem, então trate os resultados como uma lista de coisas a serem verificadas, em vez de uma lista de coisas a serem corrigidas.
