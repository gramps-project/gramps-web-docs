# Atualizar Gramps Web

Se você estiver usando um dos métodos de instalação baseados em Docker Compose, atualizar o Gramps Web para a versão mais recente é simples. Na pasta onde seu `docker-compose.yml` está localizado, execute os seguintes comandos

```bash
docker compose pull
docker compose up -d
```

Para saltos de versão menores da [API Gramps Web](https://github.com/gramps-project/gramps-web-api), isso é tudo que é necessário. No entanto, siga as [notas de lançamento da API Gramps Web](https://github.com/gramps-project/gramps-web-api/releases), pois pode haver alterações que quebram a compatibilidade que requerem atenção ou mudanças de configuração adicionais.

Observe que a imagem docker padrão `grampsweb:latest` sempre combina a versão mais recente da API com a versão mais recente do frontend. Se você quiser atualizar os dois componentes separadamente - o que é possível - uma configuração mais elaborada do que a descrita aqui é necessária.
