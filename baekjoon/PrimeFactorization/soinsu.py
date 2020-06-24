# for (int i=2; i*i <= n; i++) { while (n%i == 0) {
#         printf("%d\n",i);
# n /= i; }
# }
# if (n > 1) {
#     printf("%d\n",n);
# }

import math
import sys


n = int(sys.stdin.readline())
for i in range(2, int(math.sqrt(n)), 1):
    while n%i == 0:
        print(i)
        n //= i
if n > 1:
    print(n)