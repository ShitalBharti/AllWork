class Intersection:
    def user_input(self):
        print("Enter list1 elements: ")
        self.lst1 = [int(x) for x in input().split(' ')]
        print("Enter list2 elements: ")
        self.lst2 = [int(x) for x in input().split(' ')]
        print(self.lst1)
        print(self.lst2)
        self.intersect()

    def intersect(self):
        len1 = len(self.lst1)
        len2 = len(self.lst2)
        if len1 < len2:
            self.check(self.lst1,self.lst2)
        else:
            self.check(self.lst2, self.lst1)

    def check(self,l1,l2):
        res = []
        for element in l1:
            count = l1.count(element)
            if element in l2:
                if l2.count(element) >= count:
                    res.append(element)
        print(res)

ins = Intersection()
ins.user_input()