class Student:
    stt = 1 
    def __init__(self, name, sex, age, math_score, physics_score, chemistry_score):
        pass
        self.id = self.stt
        Student.stt += 1
        self.name = name
        self.sex = sex
        self.age = int(age)
        self.math_score = float(math_score)
        self.physics_score = float(physics_score)
        self.chemistry = float(chemistry_score)
        self.medium_score = float(math_score + chemistry_score + physics_score)/3
        self.learning_ability = ''
    def student_display(self):
        print(self.id)
        print(self.name)
        print(self.sex)
        print(self.age)
        print(self.math_score)
        print(self.physics_score)
        print(self.chemistry)
        print(self.medium_score)
        print(self.learning_ability)
class StudentManager():
    list_student = []

    def add_student(self,student_id):
        # add student to list
        self.list_student.append(student_id)
        print('Add student succussfully!')

    def find_student_id(self, student_id):
        # find student per ID
        searchresult = None
        for st in self.list_student:
            if st.id == student_id:
                searchresult = st
                return searchresult
        print(f'Khong ton tai sinh vien co id = {student_id}')
        return False
    
    def update_student_id(self,id):
        # update student per ID
        st = self.find_student_id(id)
        if st != False:
            # update student infomation
            name = input('Name:')
            sex = input('sex:')
            age = int(input('age:'))
            math_score = float(input('Math_score:'))
            physics_score = float(input('Physics_score:'))
            chemistry_score = float(input('Chemistry_score:'))
            
            st.name = name
            st.sex = sex
            st.age = age
            st.math_score = math_score
            st.physics_score = physics_score
            st.chemistry_score = chemistry_score
            st.medium_score = (math_score + physics_score + chemistry_score)/3
            st.learning_ability = ''
            print('Update student is succussfully!')
            return True
        
    def remove_student_id(self, student_id):
        # remove student per ID
        st = self.find_student_id(student_id)
        if st != False:
            for sv in self.list_student:
                if sv.id == student_id:
                    self.list_student.remove(sv)
                    print('Remove student succussfully!')
                    return True
    def find_student_name(self, student_name):
        # find student per name
        stdname = None
        for st in self.list_student:
            if st.name == student_name:
                stdname = st
                return stdname
        print(f'Khong tim thay hoc sinh co ten : {student_name}')
        return False
    def sort_gpa(self):
        self.list_student.sort(reverse=True, key= lambda gpa: gpa.medium_score)
    def sort_name(self):
        self.list_student.sort(reverse= True, key= lambda name: name.name)
    def sort_id(self):
        self.list_student.sort(reverse= True, key= lambda id : id.id)
    def return_lis(self):
        return self.list_student







# student_long = Student(
#     name="Nguyen Van Long",
#     sex="Male",
#     age=24,
#     math_score=9.2,
#     physics_score=9.25,
#     chemistry_score=9.75
# )

# student_minh = Student(
#     name="Nguyen Van Minh",
#     sex="FeMale",
#     age=25,
#     math_score=9.2,
#     physics_score=9.25,
#    chemistry_score=9.75
# )
# manager = StudentManager()
# manager.add_student(student_long)
# manager.add_student(student_minh)
# # manager.update_student_id(1)
# print(manager.list_student)
