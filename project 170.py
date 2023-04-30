from tkinter import *
root = Tk()
root.title("PERCENTAGE CALCULATION")
root.geometry("500x500")

percentage_grade_3_label = Label(root)
percentage_grade_5_label = Label(root)
percentage_grade_10_label = Label(root)

class grade_3() :
    def __init__(self , language_arts , mathematic):
        self.language_arts = language_arts
        self.mathematic = mathematic
    def percentage (self) :
        total_marks = self.language_arts+ self.mathematic
        total_marks_with_100 = total * 100
        pa_g_3 = tm_with_100 / 200
        percentage_grade_3_label["text"] = pa_g_3
        
class grade_5():
    def __init__(self , language_arts , mathematic , sst):
        self.language_arts = language_arts
        self.mathematic = mathematic
        self.sst = sst
        
    def percentage (self) :
        total_marks = self.language_arts+ self.mathematic + self.sst
        total_marks_with_100 = total * 100
        pa_g_5 = tm_with_100 / 300
        percentage_grade_5_label["text"] = pa_g_5

class grade_10():
    def __init__(self , language_arts , mathematic , sst , foreign_language):
        self.language_arts = language_arts
        self.mathematic = mathematic
        self.sst = sst
        self.foreign_language = foreign_language
        
    def percentage ():   
        total_marks = self.language_arts+ self.mathematic + self.sst + self.foreign_language
        total_marks_with_100 = total * 100
        pa_g_10 = tm_with_100 / 400
        percentage_grade_10_label["text"] = pa_g_10
        
obj_grade_3 = grade_3(40 , 50)
grade_3_btn = Button(root , text = "Grade - 3" , command= obj_grade_3.percentage)
grade_3_btn.pack(padx = 20 , pady = 20)
percentage_grade_3_label.pack(padx = 20 , pady = 20)

obj_grade_5 = grade_3(40 , 50 , 70)
grade_5_btn = Button(root , text = "Grade - 5" , command= obj_grade_5.percentage)
grade_5_btn.pack(padx = 20 , pady = 20)
percentage_grade_5_label.pack(padx = 20 , pady = 20)

obj_grade_10 = grade_3(40 , 50 , 70 , 90)
grade_10_btn = Button(root , text = "Grade - 10" , command= obj_grade_10.percentage)
grade_10_btn.pack(padx = 20 , pady = 20)
percentage_grade_10_label.pack(padx = 20 , pady = 20)     


root.mainloop()

 