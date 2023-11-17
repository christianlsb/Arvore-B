class NodoB:
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []
        self.filhos = []

class ArvoreB:
    def __init__(self, ordem):
        self.raiz = NodoB()
        self.ordem = ordem

    def busca(self, chave, nodo=None):
        if nodo is None:
            nodo = self.raiz

        i = 0
        while i < len(nodo.chaves) and chave > nodo.chaves[i]:
            i += 1

        if i < len(nodo.chaves) and chave == nodo.chaves[i]:
            return True 
        elif nodo.folha:
            return False  
        else:
            return self.busca(chave, nodo.filhos[i])

    def insere(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.ordem) - 1:
            novo_nodo = NodoB(folha=False)
            novo_nodo.filhos.append(raiz)
            self.dividir_filho(novo_nodo, 0)
            self.raiz = novo_nodo
            self.insere_nao_cheio(novo_nodo, chave)
        else:
            self.insere_nao_cheio(raiz, chave)

    def insere_nao_cheio(self, x, chave):
        i = len(x.chaves) - 1
        if x.folha:
            x.chaves.append(0) 
            while i >= 0 and chave < x.chaves[i]:
                x.chaves[i + 1] = x.chaves[i]
                i -= 1
            x.chaves[i + 1] = chave
        else:
            while i >= 0 and chave < x.chaves[i]:
                i -= 1
            i += 1
            if len(x.filhos[i].chaves) == (2 * self.ordem) - 1:
                self.dividir_filho(x, i)
                if chave > x.chaves[i]:
                    i += 1
            self.insere_nao_cheio(x.filhos[i], chave)

    def dividir_filho(self, x, i):
        t = self.ordem
        y = x.filhos[i]
        z = NodoB(folha=y.folha)
        x.filhos.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t - 1])
        z.chaves = y.chaves[t:]
        y.chaves = y.chaves[:t - 1]
        if not y.folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t]

    def remove(self, chave):
        raiz = self.raiz
        if chave in raiz.chaves:
            if len(raiz.chaves) == 1 and len(raiz.filhos) > 1:
                predecessor = self.get_predecessor(raiz)
                raiz.chaves.remove(chave)
                raiz.chaves.append(predecessor)
                self.remove_predecessor(raiz, predecessor)
            else:
                self.remove_da_folha(raiz, chave)
        else:
            self.remove_recursivo(raiz, chave)

    def remove_recursivo(self, x, chave):
        i = 0
        while i < len(x.chaves) and chave > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and chave == x.chaves[i]:
            if x.folha:
                self.remove_da_folha(x, chave)
            else:
                self.remove_de_nao_folha(x, chave, i)
        else:
            if x.folha:
                print(f"A chave {chave} não está na árvore.")
            else:
                filho = x.filhos[i]
                if len(filho.chaves) == self.ordem - 1:
                    self.preencher(filho, i)
                self.remove_recursivo(filho, chave)

    def remove_da_folha(self, x, chave):
        x.chaves.remove(chave)

    def remove_de_nao_folha(self, x, chave, i):
        if len(x.filhos[i].chaves) >= self.ordem:
            predecessor = self.get_predecessor(x.filhos[i])
            x.chaves[i] = predecessor
            self.remove_predecessor(x.filhos[i], predecessor)
        elif len(x.filhos[i + 1].chaves) >= self.ordem:
            sucessor = self.get_sucessor(x.filhos[i + 1])
            x.chaves[i] = sucessor
            self.remove_sucessor(x.filhos[i + 1], sucessor)
        else:
            self.merge(x, i)

    def preencher(self, x, i):
        if i != 0 and len(x.filhos[i - 1].chaves) >= self.ordem:
            self.puxar_de_anterior(x, i)
        elif i != len(x.filhos) - 1 and len(x.filhos[i + 1].chaves) >= self.ordem:
            self.puxar_de_seguinte(x, i)
        else:
            if i != len(x.filhos) - 1:
                self.merge(x, i)
            else:
                self.merge(x, i - 1)

    def puxar_de_anterior(self, x, i):
        filho = x.filhos[i]
        irmao_anterior = x.filhos[i - 1]
        filho.chaves.insert(0, x.chaves[i - 1])
        x.chaves[i - 1] = irmao_anterior.chaves.pop()

        if not filho.folha:
            filho.filhos.insert(0, irmao_anterior.filhos.pop())

    def puxar_de_seguinte(self, x, i):
        filho = x.filhos[i]
        irmao_seguinte = x.filhos[i + 1]
        filho.chaves.append(x.chaves[i])
        x.chaves[i] = irmao_seguinte.chaves.pop(0)

        if not filho.folha:
            filho.filhos.append(irmao_seguinte.filhos.pop(0))

    def merge(self, x, i):
        filho = x.filhos[i]
        irmao_seguinte = x.filhos[i + 1]

        filho.chaves.append(x.chaves[i])
        filho.chaves.extend(irmao_seguinte.chaves)

        if not filho.folha:
            filho.filhos.extend(irmao_seguinte.filhos)

        x.chaves.pop(i)
        x.filhos.pop(i + 1)

    def get_predecessor(self, x):
        while not x.folha:
            x = x.filhos[-1]
        return x.chaves[-1]

    def remove_predecessor(self, x, chave):
        if x.folha:
            x.chaves.remove(chave)
        else:
            self.remove_recursivo(x.filhos[-1], chave)

    def get_sucessor(self, x):
        while not x.folha:
            x = x.filhos[0]
        return x.chaves[0]

    def remove_sucessor(self, x, chave):
        if x.folha:
            x.chaves.remove(chave)
        else:
            self.remove_recursivo(x.filhos[0], chave)

    def mostra_arvore(self):
        self._mostra_arvore(self.raiz)

    def _mostra_arvore(self, nodo, nivel=0):
        if nodo:
            print(f"Nível {nivel}: {nodo.chaves}")
            if not nodo.folha:
                nivel += 1
                for filho in nodo.filhos:
                    self._mostra_arvore(filho, nivel)

if __name__ == "__main__":
    arvore_b = ArvoreB(ordem=2)

    chaves = [3, 7, 1, 5, 9, 2, 8, 4, 6]

    for chave in chaves:
        arvore_b.insere(chave)

    chave_busca = 6
    if arvore_b.busca(chave_busca):
        print(f'A chave {chave_busca} foi encontrada na árvore B.')
    else:
        print(f'A chave {chave_busca} não foi encontrada na árvore B.')

    print("\nÁrvore B:")
    arvore_b.mostra_arvore()

    chave_remover = 6
    arvore_b.remove(chave_remover)

    print(f"\nÁrvore B após remover a chave {chave_remover}:")
    arvore_b.mostra_arvore()
