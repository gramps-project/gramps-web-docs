# Índice de pesquisa

A seção **Índice de pesquisa** das [Configurações de administração](settings.md) mostra o estado do índice de pesquisa de texto completo e permite que você o reconstrua.

## Gerenciar índice de pesquisa

O Gramps Web mantém um índice de pesquisa de texto completo que normalmente é atualizado automaticamente sempre que os dados mudam. O indicador de status mostra quantos objetos estão atualmente indexados em relação ao total de objetos.

Clique em **Atualizar índice de pesquisa** para acionar uma reconstrução completa. Um indicador de progresso é exibido enquanto a tarefa é executada em segundo plano. Isso raramente é necessário.

Se uma árvore ainda não tiver índice de pesquisa, por exemplo, após uma atualização do servidor que alterou o formato do índice, o Gramps Web o constrói em segundo plano na primeira vez que a árvore é aberta. Enquanto está sendo construído, a seção mostra "O índice de pesquisa está sendo construído." em vez das contagens, **Atualizar índice de pesquisa** está desativado, e os resultados da pesquisa podem estar incompletos. A construção aparece em [Notificações](../user-guide/notifications.md) como a tarefa "Atualizar índice de pesquisa".
