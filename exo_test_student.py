class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'
       
    def take_test(self, exam, res):
        if isinstance(self.tests_taken, str):
            self.tests_taken = ""
            self.tests_taken = {}
        score = int(round(len(set(exam.markscheme) & set(res))/len(exam.markscheme) * 100))
        strScore = "(" + str(score) + "%" +")"
        self.tests_taken[exam.subject] = "Passed! " + strScore if score >= int(exam.pass_mark[0:2]) else "Failed! " + strScore        
        return self.tests_taken
        








paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
paper4 = Testpaper('Physics', ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A'], '90%')
student1 = Student()
student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
# student1.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student1.tests_taken)
# print(paper1.subject)