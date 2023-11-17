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

    chave_busca = 91
    if arvore_b.busca(chave_busca):
        print(f'A chave {chave_busca} foi encontrada na árvore B.')
    else:
        print(f'A chave {chave_busca} não foi encontrada na árvore B.')

    print("\nÁrvore B:")
    arvore_b.mostra_arvore()
