#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
1. Regardless of n size, always looping WHILE a + n^2 < n^3
2. a0 = 0
3. a1 = 0 + n^2 + n^2
4. a2 = 0 + n^2 + n^2
5. a3 = 0 + n^2 + n^2 + n^2
6. ai = i(n^2)
7. So, do while i(n^2) < n^3, or do until i(n^2) = n^3 => i = n
8. So, number of iterations is just n, so LINEAR = O(n)

b)
1. sum is irrelevant
2. Regardless of n size, always looping WHILE j < n
3. a0 = 1
4. a1 = 2
5. a2 = 4
6. a3 = 8
7. jk = 2^k
8. So, do while 2^k < n, or do until 2^k = n
9. If solve for k, then k = log(n)/log(2)
10. So, number of iteration of while loop is log of n
11. So for loop is just doing log(n) n times in a row, so it is LINEAR
12. CORRECT: O(nlogn)
c)
1. bunnies,	iterations
2. 0,	1
3. 1,	2
4. 2,	3
5. 3,   4
6. so LINEAR function of number of bunnies O(n)

## Exercise II

Use variation of binary search to find f while given n to minimize sum of number of eggs dropped and broken.

Two arguments
1. n: number of stories in the building
2. f: floor level at or above in which dropping egg breaks it

top floor = n

low floor = 1

sum = 0

Run while loop while top floor is greater than low floor

1. Find midpoint between top floor and low floor
2. If current floor is greater or equal to f then the dropped egg breaks. Respond by lowering current floor to mid floor and add 1 to sum
3. Otherwise, the dropped egg does not break. Respond by raising current floor to mid floor and add 1 to sum

print sum, which is number of eggs dropped and/or broken

print mid floor, which is estimate of f

ALTERNATIVE METHOD: start at bottom and keep dropping and stop when it breaks
