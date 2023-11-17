# Arvore-B

Repositório destinado ao Trabalho 2 de Estrutura de Dados.



def mostra_arvore(self):
      self._mostra_arvore(self.raiz)
--> Chama a função _mostra_arvore (método privado) passando o parâmetro raíz da árvore b para a função.

def _mostra_arvore(self, nodo, nivel=0):
    if nodo:
            print(f"Nível {nivel}: {nodo.chaves}")
            if not nodo.folha:
                nivel += 1
                for filho in nodo.filhos:
                    self._mostra_arvore(filho, nivel)
--> Função privada que, recebe como parâmetro o nodo, nó atual, e define o nível como 0  (nodo raíz quando nível = 0 e pra cada nível de nó filho soma + 1 até o nó folha). Se tem um nodo, ele entra no bloco if nodo: e imprime o nível e todas as chaves do nodo. Se o nó tiver nó filhos ele entra no: if not nodo.folha:
                nivel += 1
                for filho in nodo.filhos:
                    self._mostra_arvore(filho, nivel)
Voltando ao contador de nível, como citado acima: Vai somar 1 no nível, e pra cada filho do nó, chama a função de novo e passa o nodo filho como parâmetro, junto do nível dele. Ele entra nesse looping, até que seja um nó folha. 