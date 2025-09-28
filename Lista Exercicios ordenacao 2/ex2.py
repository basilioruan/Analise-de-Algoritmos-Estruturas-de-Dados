def quickSort(v, esq, dir):
  i = esq
  j = dir
  pivo = v[(esq + dir) // 2] 

  while i <= j:
    while v[i] < pivo:
      i += 1
    while v[j] > pivo:
      j -= 1
    if i <= j:
      # O erro estava aqui, na versão do c++ do exercício estava fazendo v[i] = v[j] e depois v[j] = v[i]
      # ou seja, v[i] e v[j] eram iguais. Para resolver foi adicionado o aux (que por sinal já estava declarado no código c++)
      # para salvar o valor sem perder a referência
      aux = v[i]
      v[i] = v[j]
      v[j] = aux
      i += 1
      j -= 1

  for k in range (len(v)):
    print(v[k], end = " ")
  
  print()

  if esq < j:
    quickSort(v, esq, j)
  if i < dir:
    quickSort(v, i, dir)


def main():
  n = int(input())
  vetor = list(map(int, input().split())) 

  quickSort(vetor, 0, n-1)

if __name__ == "__main__":
  main()