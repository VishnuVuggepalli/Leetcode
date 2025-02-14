class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefixProd = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num != 0:
            if len(self.prefixProd) == 0:
                self.prefixProd.append(num)
            else:
                self.prefixProd.append(self.prefixProd[-1] * num)
        else:
            self.prefixProd = []


    def getProduct(self, k: int) -> int:
        N = len(self.prefixProd)
        if k > N:
            return 0
        elif k == N:
            return self.prefixProd[-1]
        else:
            prev = -1 * (k+1)
            return self.prefixProd[-1] // self.prefixProd[prev]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)