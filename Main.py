class Node:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla.upper()
        self.nome_estado = nome_estado
        self.next = None


class HashTable:
    def __init__(self):
        self.tabela = [None] * 10          # Inicie 10 posições vazias/Initialize 10 empty buckets

    def funcao_hash(self, sigla):
        # Retorna posição baseada no cálculo da ASCII ou no caso especial do DF/Returns position based on ASCII calculation or special case for DF
        if sigla.upper() == "DF":
            return 7  # Caso especial para Distrito Federal/Special case for Distrito Federal
        else:
            return (ord(sigla[0].upper()) + ord(sigla[1].upper())) % 10

    def inserir(self, sigla, nome_estado):
        # Insere um node novo no começo da lista encadeada/Insert a new node at the beginning of the linked list
        index = self.funcao_hash(sigla)
        novo_nodo = Node(sigla, nome_estado)
        novo_nodo.next = self.tabela[index]
        self.tabela[index] = novo_nodo

    def imprimir_tabela(self):
        # Printa o estado atual da tabela hash/Print the current state of the hash table
        print("\n=== Situação Atual da Tabela Hash ===")
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            if not atual:
                print("Vazia")
            else:
                while atual:
                    print(f"[{atual.sigla} - {atual.nome_estado}]", end=" -> ")
                    atual = atual.next
                print("None")
        print("======================================\n")


def menu():
    tabela = HashTable()

    while True:
        print("1 - Mostrar tabela hash")
        print("2 - Inserir estado")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tabela.imprimir_tabela()
        elif opcao == "2":
            sigla = input("Digite a sigla do estado (2 letras): ").strip().upper()
            if len(sigla) != 2 or not sigla.isalpha():
                print("Sigla inválida! Digite exatamente 2 letras.\n")
                continue
            nome = input("Digite o nome completo do estado: ").strip()
            if not nome:
                print("Nome inválido! Tente novamente.\n")
                continue
            tabela.inserir(sigla, nome)
            print(f"Estado {sigla} inserido com sucesso!\n")
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Inicia o programa/Start the program
if __name__ == "__main__":
    menu()
