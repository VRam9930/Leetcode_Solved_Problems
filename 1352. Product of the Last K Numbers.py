class ProductOfNumbers(object):

    def __init__(self):
        self.nums=[]

    def add(self, num):
        
        if self.nums:
            if num==0:
                self.nums.append((0, len(self.nums)))
            else:
                if self.nums[-1][0]!=0:
                   self.nums.append((num*self.nums[-1][0], self.nums[-1][1]))
                else:
                   self.nums.append((num, self.nums[-1][1]))
        else:
            if num==0:
              self.nums.append((0, 0))
            else:
              self.nums.append((num, -1))

    def getProduct(self, k):
        
        if self.nums[-1][1]==-1:
            if k==len(self.nums):
              return self.nums[-1][0]
            return self.nums[-1][0]//self.nums[-k-1][0]
        elif self.nums[-1][1] > len(self.nums)-k-1:
            return 0
        elif self.nums[-1][1] == len(self.nums)-k-1:
            return self.nums[-1][0]
        else:
            return self.nums[-1][0]//self.nums[-k-1][0]
