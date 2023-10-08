class A:
    def __init__(self, name, id, branch):
        self.name = name
        self.id = id
        self.branch = branch

    def show(self):
        print(f"name: {self.name}")
        print(f"id: {self.id}")
        print(f"branch: {self.branch}")


class B(A):
    def __init__(self, roll, id, branch):
        super().__init__(name="", id=id, branch=branch)
        self.roll = roll

    def show(self):
        super().show()
        print(f"Old University roll number: {self.roll}")


class C(A):
    def __init__(self, newbranch, id, branch):
        super().__init__(name="", id=id, branch=branch)
        self.newbranch = newbranch

    def show(self):
        super().show()
        print(f"Updated branch is: {self.newbranch}")


class D(B, C):
    def __init__(self, newroll, roll, id, branch):
        B.__init__(self, roll=roll, id=id, branch=branch)
        C.__init__(self, newbranch="", id=id, branch=branch)
        self.newroll = newroll

    def show(self):
        B.show(self)
        C.show(self)
        print(f"New University Roll No. is: {self.newroll}")


class E(D):
    def __init__(self, name, roll, newbranch, newroll, id, branch):
        super().__init__(newroll=newroll, roll=roll, id=id, branch=branch)
        self.name = name

    def show(self):
        D.show(self)
        print(f"Name: {self.name}")


obj = E(name="vipul", roll="2200270310189", newbranch="IT", newroll="220027011124", id="2231020", branch="ECE")
obj.show()
