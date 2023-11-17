# Arvore-B

Repositório destinado ao Trabalho 2 de Estrutura de Dados.

Classe NodoB:
Esta classe representa um nó na árvore B. Cada nó contém uma lista de chaves e uma lista de filhos. O atributo folha indica se o nó é uma folha da árvore.

Classe ArvoreB:
A classe principal que representa a árvore B. Aqui estão os métodos da classe:

**init**(self, ordem): O construtor inicializa a árvore B com uma ordem específica.

busca(self, chave, nodo=None): Realiza uma busca pela chave na árvore. Se a chave for encontrada, retorna True; caso contrário, retorna False.

insere(self, chave): Insere uma chave na árvore. Se a raiz estiver cheia, é criado um novo nó e a raiz é dividida.

insere_nao_cheio(self, x, chave): Realiza a inserção em um nó não cheio. Se o nó estiver cheio, ele é dividido antes da inserção.

dividir_filho(self, x, i): Divide um filho do nó x na posição i. Isso é necessário durante a inserção quando um nó atinge sua capacidade máxima.

remover(self, chave): Remove uma chave da árvore. Se a chave não estiver presente, uma mensagem é exibida. O método chama o método remover_nao_vazio para lidar com a remoção de uma chave de um nó não folha.

remover_nao_vazio(self, x, chave): Método auxiliar para remover uma chave de um nó não folha.

remover_chave_de_folha(self, x, i): Remove uma chave de um nó folha.

remover_de_subarvore(self, x, i, chave): Remove uma chave de um nó não folha.

encontrar_predecessor(self, x, i): Encontra o predecessor de uma chave em um nó.

encontrar_sucessor(self, x, i): Encontra o sucessor de uma chave em um nó.

fundir_filhos(self, x, i): Funde dois filhos de um nó durante a remoção.

mostrar(self, nodo=None, nivel=0): Exibe a árvore de forma mais visual, percorrendo os nós em ordem e exibindo suas chaves.

inserir_elemento(self, chave): Método auxiliar para simplificar a inserção de elementos e exibe uma mensagem indicando que a chave foi inserida.

Exemplo de Uso:
No bloco final, é fornecido um exemplo de uso da árvore B. Chaves são inseridas na árvore usando o método inserir_elemento. Após a inserção, a árvore é exibida usando o método mostrar. Em seguida, uma chave é removida usando o método remover, e a árvore é exibida novamente.

Espero que isso ajude a entender a estrutura do código! Se houver alguma parte específica que você gostaria de explorar mais, por favor, me avise.
