def print_vetor(vetor, n):
  for i in range(n):
    print(vetor[i], end=' ')
  print()

def insertion_sort(vetor, n):
  for i in range(n-2, -1, -1):
    key = vetor[i]
    j = i + 1

    while j < n and vetor[j] > key:
      vetor[j - 1] = vetor[j]
      j += 1
    vetor[j - 1] = key
    print_vetor(vetor, n)
  return vetor

def main():
  n = int(input())
  vetor = list(map(int, input().split())) 
  print()

  insertion_sort(vetor, n)

if __name__ == "__main__":
  main()