def print_vetor(vetor, n):
  for i in range(n):
    print(vetor[i], end=' ')
  print()

def selection_sort(vetor, n):

  for i in range(n):
    max_idx = i

    for j in range(i + 1, n):
      if vetor[j] > vetor[max_idx]:
        max_idx = j

    vetor[i], vetor[max_idx] = vetor[max_idx], vetor[i]

    print_vetor(vetor, n)

  return vetor

def main():
  n = int(input())
  vetor = list(map(float, input().split())) 

  selection_sort(vetor, n)

if __name__ == "__main__":
  main()