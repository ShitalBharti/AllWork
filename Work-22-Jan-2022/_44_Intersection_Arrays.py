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
        s1 = set(self.lst1)
        s2 = set(self.lst2)
        res = s1.intersection(s2)
        res = list(res)
        print(res)

ins = Intersection()
ins.user_input()