Projeto github-interface.
Desenvolvedor: Celoezra
GitHub Manager
GitHub Manager é um aplicativo de desktop simples que permite criar, excluir, alterar a visibilidade de repositórios no GitHub e fazer o upload de arquivos em um repositório recém-criado. Ele foi desenvolvido usando a linguagem de programação Python e a biblioteca Tkinter para a interface gráfica.

Requisitos
Antes de executar o aplicativo, certifique-se de que você atenda aos seguintes requisitos:

Python instalado: O aplicativo foi desenvolvido em Python, portanto, você precisa ter o Python instalado na sua máquina.

Bibliotecas Python: O aplicativo utiliza as seguintes bibliotecas Python, portanto, você precisa instalá-las se ainda não o fez:

tkinter: Para criar a interface gráfica.
github e pygithub: Para interagir com a API do GitHub.
Você pode instalar essas bibliotecas usando o comando pip install no seu terminal:

Copy code
pip install tk github pygithub
Funcionalidades
Autenticação no GitHub
Antes de usar o aplicativo, você será solicitado a inserir seu token do GitHub para autenticação. O token é usado para criar repositórios em sua conta e realizar outras operações.

Criar Repositório
Clique no botão "Criar Repositório" na interface principal.
Isso abrirá uma janela secundária onde você pode fornecer os detalhes do novo repositório, como nome, descrição, diretório local e visibilidade (público ou privado).
Após preencher as informações, clique no botão "Criar" para criar o repositório no GitHub.
O aplicativo também permite fazer o upload de um arquivo README.md para o novo repositório.
Excluir Repositório
Clique no botão "Excluir Repositório" na interface principal.
Isso abrirá uma janela secundária onde você pode fornecer o nome do repositório que deseja excluir.
O aplicativo verificará se o repositório existe e solicitará confirmação antes de excluí-lo.
Alterar Visibilidade do Repositório
Clique no botão "Alterar Visibilidade" na interface principal.
Isso abrirá uma janela secundária onde você pode fornecer o nome do repositório que deseja alterar a visibilidade.
Você pode escolher entre tornar o repositório público ou privado.
O aplicativo verificará se o repositório existe e atualizará a visibilidade de acordo com sua escolha.
Sair
Clique no botão "Sair" na interface principal para fechar o aplicativo.

Uso
Para usar o aplicativo, siga estas etapas:

Execute o programa e insira seu token do GitHub quando solicitado.

Use as opções na interface principal para criar, excluir ou alterar a visibilidade de repositórios no GitHub.

Siga as instruções fornecidas na interface para concluir as operações desejadas.

Feche o aplicativo clicando no botão "Sair" quando terminar.

Avisos
Certifique-se de não compartilhar seu token do GitHub com outras pessoas, pois ele concede acesso à sua conta no GitHub.

Tenha cuidado ao excluir repositórios, pois essa ação é irreversível e resultará na perda permanente de dados.

Contribuição
Se você deseja contribuir para o desenvolvimento deste aplicativo, sinta-se à vontade para fazer um fork do repositório, fazer as alterações desejadas e enviar um pull request. Serão bem-vindas contribuições para melhorar e expandir as funcionalidades do aplicativo.

Espero que esta documentação ajude a explicar como o seu aplicativo funciona e a facilitar o uso por outros usuários. Boa sorte com seu projeto no GitHub!
