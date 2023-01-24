class Student:  # ---> class

    # We can use self within the class only to access current object
    # self is a reference variable which is always pointing to current object
    # self is not a keyword, we can use any name like delf/kelf etc, but self is recommended

    def __init__(self, name, rollno, marks):  # ---> Constructor

        # First argument to the constructor is always self
        # The below variables are instance variable
        # Inside constructor, we can use self to declare object related variables (Instance variable)
        
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):  # ---> Method (Instance method)

        # First argument to the instance method is always self
        # Inside instance method, we can use self to access the values of instance variables

        print('Hello, I am:', self.name)
        print('My Roll number is', self.rollno)
        print('My Marks are:', self.marks)


# We do not need to provide value for self variable, PVM itself will provide value

s1 = Student('Sunny', 101, 90)  # s1 = Reference variable, Student() is an object
s2 = Student('Bunny', 102, 95)  # s1 = Reference variable, Student() is an object
s1.talk()
s2.talk()
