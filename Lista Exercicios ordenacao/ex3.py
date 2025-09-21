def print_vetor(vetor, n, i, j, trocou):
  for k in range(n):
    if (trocou and (k == i or k == j)):
      print(vetor[k], end='t  ')
    elif (not trocou and (k == i or k == j)):
      print(vetor[k], end='*  ')
    else:
      print(vetor[k], end='   ')
  print()

def bubble_sort(vetor, n):
  for i in range(n):
    for j in range(0, n - i - 1):
      trocou = False
      if vetor[j] > vetor[j + 1]:
        trocou = True
        print_vetor(vetor, n, j, j+1, trocou)
        aux = vetor[j]
        vetor[j] = vetor[j+1]
        vetor[j+1] = aux
      else:
        print_vetor(vetor, n, j, j+1, trocou)

  print_vetor(vetor, n, -1, -1, False)
  return vetor

def main():
  n = int(input())
  vetor = list(map(int, input().split())) 
  print()

  bubble_sort(vetor, n)

if __name__ == "__main__":
  main()