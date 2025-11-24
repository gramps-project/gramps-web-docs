Para experimentar o Gramps Web em seu computador local (Linux, Mac ou Windows) sem interferir na sua instalação do Gramps Desktop, você pode usar o Docker com o seguinte comando:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Isso tornará uma nova instância vazia do Gramps Web acessível em [http://localhost:5055](http://localhost:5055), onde você pode criar um usuário administrador e importar um arquivo XML do Gramps.

!!! info
    Como essa configuração simples não permite executar tarefas longas em um processo separado, a importação de um grande arquivo XML do Gramps pode falhar devido a um tempo limite no assistente de primeira execução.


Para usar arquivos de mídia do seu computador, você pode montar a pasta de mídia do Gramps no contêiner com

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Observe que isso não persistirá as alterações que você faz no banco de dados quando você reiniciar o contêiner. Para configurar corretamente o Gramps Web, continue lendo sobre [Implantação](deployment.md).
