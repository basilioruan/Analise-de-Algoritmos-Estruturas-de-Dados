def intercala(vetor, inicio, meio, fim):
  i = inicio
  j = meio
  tamanho = fim - inicio + 1
  vetor_auxiliar = [0] * tamanho 
  k = 0

  while (i < meio):
    print(vetor[i], end=" ")
    i += 1
  
  print(" + ", end=" ")


  while (j <= fim):
    print(vetor[j], end=" ")
    j += 1

  i = inicio
  j = meio  

  while (i < meio) and (j <= fim):                
    if vetor[i] <= vetor[j]:
      vetor_auxiliar[k] = vetor[i]
      k += 1
      i += 1
    else:
      vetor_auxiliar[k] = vetor[j]
      k += 1
      j += 1
                         
  while i < meio:
    vetor_auxiliar[k] = vetor[i]
    k += 1
    i += 1
  
  while j <= fim:
    vetor_auxiliar[k] = vetor[j]
    k += 1
    j += 1
  
  print(" = ", end=" ")

  for posicao in range(tamanho):
    print(vetor_auxiliar[posicao], end=" ")
    vetor[inicio + posicao] = vetor_auxiliar[posicao]
  
  print()

def mergeSort(vetor, inicio, fim):
  if inicio < fim:
    meio = (inicio + fim) // 2
    mergeSort(vetor, inicio, meio)
    mergeSort(vetor, meio + 1, fim)
    intercala(vetor, inicio, meio + 1, fim)

def main():
  n = int(input())
  vetor = list(map(int, input().split())) 

  mergeSort(vetor, 0, n-1)
  

if __name__ == "__main__":
  main()