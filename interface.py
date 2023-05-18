from tkinter import ttk
import os
from tkinter import *

path = os.path.abspath("img")

def finish(l: list):
    display(lf=lup_loop(l), l=ldown(l), Table=createTable(ldown(l)))


def lup_loop(cources: list):
    lup = []
    for i in cources:
        lup.append([i.course_label, i.section, i.instructor, i.days, i.time_display])
    return lup


def ldown(cources: list):
    l = []
    k = 0
    for i in cources:
        l.append([2])
        time = i.time_display

        try:
            Hour1 = int(time[6:8])
        except:
            Hour1 = int(time[6])
        try:
            Hour2 = int(time[:2])
        except:
            Hour2 = int(time[0])

        sumHours = (Hour1 - Hour2)  # sumHours
        if sumHours < 0:
            sumHours += 12

        sumMin = (int(time[9:11]) - int(time[3:5]))  # sumMin
        if sumMin < 0:
            sumMin += 60
            sumHours -= 1
        while (sumHours > 0):
            sumHours -= 1
            sumMin += 60
        l[k].append(sumMin)
        l[k].append([int(time[0:2]), int(time[3:5])])

        if len(i.days) > 1:
            if i.days[0] == 'S':
                l[k].append(0)
                l[k].append(i.course_label)
                l[k].append(i)

            elif i.days[0] == 'M':
                l[k].append(2)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days[0] == 'T':
                l[k].append(3)
                l[k].append(i.course_label)
                l[k].append(i)

            else:
                raise Exception(f"Error we got unknown day ==> {i.days[0]}")
            if len(time) > 12:
                time = (time[13:])

            if i.days[2] == 'S':
                l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                k += 1
            elif i.days[2] == 'M':

                l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                k += 1
            elif i.days[2] == 'T':
                l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                k += 1
            elif i.days[2] == 'W':
                l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                k += 1
            elif i.days[2] == 'R':
                l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                k += 1

        elif (len(i.days) == 1):
            if i.days == 'S':
                l[k].append(0)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'M':
                l[k].append(2)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'T':
                l[k].append(3)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'W':
                l[k].append(4)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'R':
                l[k].append(5)
                l[k].append(i.course_label)
                l[k].append(i)
            else:
                raise Exception(f"Error we got unknown day ==> {i.days}")

        else:
            raise Exception(f"Error we got error with the size of the days ==> {i.days}")

        k += 1

    return l


def createTable(lfake: list):
    Table = [  # A #B #C #D #E
        [[], [], [], [], []],  # S
        [[], [], [], [], []],  # M
        [[], [], [], [], []],  # T
        [[], [], [], [], []],  # W
        [[], [], [], [], []]  # R
    ]

    for i in lfake:

        if True:
            if i[3] > 0:
                i[3] -= 1
            if i[2][0] >= 8 and i[2][
                0] < 10:  # A from 8:00 to 10:00       B from 10:00 to 11:25       C from 11:25 to 12:50       D from 12:50 to 2:15    E from 2 :15 to 3:30    Ep from 3:30 to 5:00
                k = 0
            elif i[2][0] == 10:
                k = 1
            elif i[2][0] == 11:
                k = 2
            elif i[2][0] >= 12:
                k = 3
            elif i[2][0] == 2:
                k = 4
            else:
                raise Exception(f"Error we got unknown time start ==> {i[2][0]}")

            Table[i[3]][k].append(i[5])
            if k < 4 and i[1] >= 100:
                Table[i[3]][k + 1].append(i[5])

    return Table


class display():
    def exit(self, event):
        self.window.attributes('-fullscreen', False)

    def button_Previous(self, lf):
        if self.point - 10 >= 0:
            end = self.point
            self.point -= 10
            self.dis_table_up(start=self.point, end=end, lf=lf)

    def button_Next(self, lf):
        if self.point + 10 < len(lf):
            self.point += 10
            if self.point + 10 <= len(lf):
                end = self.point + 10
            else:
                end = len(lf)
            self.dis_table_up(start=self.point, end=end, lf=lf)

    def dis_table_up(self, start, end, lf):
        for i in range(10):  # make sure to clean all the 10 Labels
            for partIndex in range(len(self.labels[i])):
                self.labels[i][partIndex].config(text='', bg='white')

        z = 0

        for i in range(start, end):
            i %= 10
            z += 1
            color = 'white'
            if z % 2 == 0:
                color = '#D9D9D9'

            for partIndex in range(5):
                self.labels[i][partIndex].config(text=lf[start + i][partIndex], bg=color)

    def show(self, l: list):

        length = ["1", "2", "3", "4", "5"]
        lst = [['Course Label', 'Section', 'Instructor', 'days', 'Time']]
        for i in l:
            lst.append(i)
        root = Tk()
        root.title('test')
        treev = ttk.Treeview(root, selectmode='browse')
        treev.pack(side='right')
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=treev.yview)
        verscrlbar.pack(side='right', fill='x')
        treev.configure(xscrollcommand=verscrlbar.set)

        treev["columns"] = length

        treev['show'] = 'headings'
        for i in range(1, len(length) + 1):
            treev.column(str(i), width=90, anchor='c')

        for i in range(len(lst[0])):  # 0 1 2 3 4
            treev.heading(str(i + 1), text=lst[0][i])

        for i in lst[1:]:
            treev.insert("", 'end', text="L1",
                         values=i)

        root.mainloop()

    def clicked(self, i, k):
        l = []
        for i in self.Table[i][k]:
            l.append([i.course_label, i.section, i.instructor, i.days, i.time_display])
        self.show(l=l)

    def create_Button(self, h, w, x, y, text, i, k):

        Button(master=self.window, command=lambda: self.clicked(i, k), relief="flat", bg="red", height=h, width=w,
               text=text, bd=0).place(x=x, y=y)

    def finalText(self, x, y, color, txt):
        return self.create_text(x=self.find_text_x(x), y=self.find_text_y(y), w=self.find_text_w(x), h=1, text=txt,
                                color=color, fg='black')

    def find_text_x(self, i):
        if i == 0:
            return 1439
        elif i == 1:
            return 1319
        elif i == 2:
            return 1069
        elif i == 3:
            return 841
        elif i == 4:
            return 707
        elif i == 5:
            return 546
        else:
            return 388

    def find_text_w(self, i):
        if i == 0:
            return 20
        elif i == 1:
            return 16
        elif i == 2:
            return 34
        elif i == 3:
            return 31
        elif i == 4:
            return 18
        elif i == 5:
            return 22
        else:
            return 21

    def find_text_y(self, h):
        y = 34
        while h > 0:
            y += 25
            h -= 1
        return y

    def create_text(self, x, y, w, h, text, color, fg):
        lab = Label(master=self.window, relief="flat", bg=color, height=h, width=w, text=text, bd=1.5, fg=fg)
        lab.place(x=x, y=y)
        return lab

    def create_label(self, h, w, x, y, text):
        lab = Label(master=self.window, relief="flat", bg="#787A6A", height=h, width=w, text=text, bd=1.5)
        lab.place(x=x, y=y)

    def find_w(self, min):
        return int(18 * min / 60)

    def find_x(self, hours, min):
        if hours == 2:
            hours = 14
        elif hours == 1:
            hours = 13
        elif hours == 3:
            hours = 15

        x = 145
        while hours > 7:
            hours -= 1
            x += 125
        if min > 0:
            x += int(125 * min / 60)
        return x

    def find_y(self, h):
        y = 351

        while h > 0:
            y += 53
            h -= 1
        return y

    def button_Exit(self, master):
        master.destroy()

    def __init__(self, l: list, lf, Table: list[list]):
        self.orginalList = l.copy()
        self.window = Toplevel()
        self.Table = Table
        self.labels = []
        self.point = 0  # using in Table up
        self.window.geometry("1600x853")
        self.window.configure(bg="#ffffff")
        self.window.overrideredirect(1)
        canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=900,
            width=1600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=path + r"\background.png")
        background = canvas.create_image(
            829.0, 386.0,
            image=background_img)
        # Label(relief="flat", bg="white", height=2, width=2, text=hours, bd=1.5, font=('Times', 16)).place(x=835, y=730)

        for i in range(len(Table)):
            for k in range(len(Table[i])):

                if len(Table[i][k]) > 1:
                    if k == 0:
                        sumMin = 110
                        hour = 8
                        min = 0
                    elif k == 1:
                        sumMin = 75
                        hour = 10
                        min = 0
                    elif k == 2:
                        sumMin = 75
                        hour = 11
                        min = 25
                    elif k == 3:
                        sumMin = 75
                        hour = 12
                        min = 50
                    elif k == 4:
                        hour = 2
                        sumMin = 180
                        min = 15
                    else:
                        raise Exception(f"Error we got unknown k ==> {k}")

                    if i > 0:
                        day = i + 1
                    else:
                        day = 0

                    # A from 8:00 to 9:50       B from 10:00 to 11:15       C from 11:25 to 12:40       D from 12:50 to 2:05    E from 2 :15 to 5:00    Ep from 3:30 to 5:00
                    self.create_Button(h=2, w=self.find_w(sumMin), x=self.find_x(hour, min),
                                       y=self.find_y(day), text=f'{len(Table[i][k])} sections', i=i, k=k)

                elif len(Table[i][k]) == 1:

                    for course in self.orginalList:
                        if (Table[i][k][0] == course[5] and (
                                (i == 0 and course[3] == 0) or (i > 0 and i == course[3] - 1))):
                            if (k == 0 and (course[2][0] == 8 or course[2][0] == 9)) or (
                                    k == 1 and course[2][0] == 10) or (k == 2 and course[2][0] == 11) or (
                                    k == 3 and course[2][0] == 12) or (k == 4 and course[2][0] == 2):
                                self.create_label(h=2, w=self.find_w(course[1]),
                                                  x=self.find_x(course[2][0], course[2][1]), y=self.find_y(course[3]),
                                                  text=course[4])
                                break
                                # A from 8:00 to 10:00       B from 10:00 to 11:25       C from 11:25 to 12:50       D from 12:50 to 2:15
                                # E from 2 :15 to 3:30    Ep from 3:30 to 5:00

        # Sharp Button Outline Dark Mode
        Exit = PhotoImage(file=path + r"\Sharp Button Outline Dark Mode.png")
        Button(
            master=self.window,
            image=Exit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Exit(master=self.window),
            relief="flat").place(x=10, y=10)
        for i in range(10):
            line_label = []
            for txt in range(5):
                line_label.append(self.finalText(x=txt, y=i, color='white', txt=''))
            self.labels.append(line_label)
        imgNext = PhotoImage(file=path + r"\Next.png")
        bNext = Button(
            master=self.window,
            image=imgNext,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Next(lf=lf),
            relief="flat")
        bNext.place(x=1178, y=293)
        imgPrevious = PhotoImage(file=path + r"\Previous.png")
        bPrevious = Button(
            master=self.window,
            image=imgPrevious,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Previous(lf=lf),
            relief="flat")
        bPrevious.place(x=1020, y=293)

        start = 0
        end = len(lf)
        if end > 10:
            end = 10
        self.dis_table_up(start=start, end=end, lf=lf)
        self.window.mainloop()



def ret(window, dec):  # from main(flag) to start
    window.destroy()
    start(dec=dec)


def showinstructor(dec, clicked):
    l = []
    for i in dec:
        if dec[i].instructor == clicked:
            l.append(dec[i])
    finish(l)


def showcourses(dec, clicked):
    if len(clicked) > 0:
        l = []
        for i in dec:
            if dec[i].course_label in clicked:
                l.append(dec[i])
        finish(l)


def confirm(clicked, l: list, options: list, drop, window, button, img):

    if len(options):
        for i in range(len(options)):
            if options[i] == clicked.get():
                l.append(options[i])
                options.pop(i)
                if len(options):
                    drop.place(x=100000, y=10000000)
                    drop = OptionMenu(window, clicked, *options)
                    drop.config(bg="black", fg="WHITE", font='Times 16 italic bold')
                    drop.place(x=165, y=318, width=232, height=45)
                if len(options) > 0:
                    clicked.set(options[0])
                else:
                    clicked.set('None')
                break
        if len(l) == 1:
            button = button.config(image=img)


def main(dec, flag):  # show(true) or to insert(false)
    # Change the label text

    window = Tk()
    window.overrideredirect(1)
    window.title('main')
    window.geometry("1600x900")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=900,
        width=1600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    options = []
    # Dropdown menu options
    if flag == 'i':
        for i in dec:
            if dec[i].instructor not in options:
                options.append(dec[i].instructor)
    elif flag == 'c':
        for i in dec:
            if dec[i].course_label not in options:
                options.append(dec[i].course_label)
    options = sorted(options)

    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    if len(options) != 0:
        clicked.set(options[0])
    else:
        clicked.set("None")
    # Create Dropdown menu
    drop = OptionMenu(window, clicked, *options)
    drop.config(bg="black", fg="WHITE", font='Times 16 italic bold')
    drop.place(x=165, y=318, width=232, height=45)

    # Create Label
    # label = Label(window, text="", bg='#94877F', font='Times 16 italic bold')
    # label.place(x=200, y=518)

    img0 = PhotoImage(file=path + r"\go_from_main.png")
    img1 = PhotoImage(file=path + r"\backvector.png")
    imgConfirm = PhotoImage(file=path + r"\confirm.png")
    lconfirm = []
    if flag == 'i':
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showinstructor(clicked=clicked.get(), dec=dec),
            relief="flat")
    elif flag == 'c':
        b0 = Button(
            bg='#675645',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showcourses(clicked=lconfirm, dec=dec),
            relief="flat")
        Button(
            image=imgConfirm,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: confirm(clicked=clicked, l=lconfirm, options=options, drop=drop, window=window, button=b0,
                                    img=img0),
            relief="flat").place(x=197, y=468)
    else:
        raise Exception(f"Error we got unknown flag  ==> ({flag})")
    # command=lambda: main3(clicked.get(),window),
    # else:raise Exception(f"Error we got unknown flag  ==> {flag}")

    b0.place(
        x=295, y=395)

    Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ret(window, dec=dec),
        relief="flat", bg='#FFF8F2').place(x=128, y=395, width=143, height=48)

    background_img = PhotoImage(file=path + r"\betweenbackground.png")
    background = canvas.create_image(
        800.0, 450.0,
        image=background_img)

    window.resizable(False, False)
    window.mainloop()


def convert_to_main(txt: str, dec, window):  # from start to main(flag)
    window.destroy()
    main(dec=dec, flag=txt)


def ext(window):
    window.destroy()


def start(dec):

    window = Tk()
    window.title('start')
    window.overrideredirect(1)
    window.geometry("1600x900")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=900,
        width=1600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=path + r"\background_dark.png")
    background = canvas.create_image(
        800.0, 450.0,
        image=background_img)

    img0 = PhotoImage(file=path + r"\search by courses.png")
    Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: convert_to_main(txt='c', dec=dec, window=window),
        relief="flat").place(x=365, y=466, width=966, height=56)

    img2 = PhotoImage(file=path + r"\search by instructor’s name.png")
    Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: convert_to_main(txt='i', dec=dec, window=window),
        relief="flat").place(x=365, y=569, width=966, height=56)

    exit_img = PhotoImage(file=path + r"\exit_img.png")
    b2 = Button(
        image=exit_img,
        borderwidth=0,
        bg='green',
        highlightthickness=0,
        command=lambda: ext(window),
        relief="flat")

    b2.place(
        x=18, y=21,
        width=65,
        height=82)
    window.resizable(False, False)
    window.mainloop()



class Course:
    def __init__(self, course_label, section, instructor, days, time_display):
        self.course_label = course_label
        self.time_display = time_display
        self.section = section  # 1,2,3,...
        self.instructor = instructor  # name
        self.days = days  # S,M,T,W,R

        # A from 8:00 to 10:00       B from 10:00 to 11:25       C from 11:25 to 12:50       D from 12:50 to 2:15
        # E from 2 :15 to 3:30    Ep from 3:30 to 5:00


# [2, 75, [10, 0], 2, "COMP333"],  # x,min,h:m,day,courseID
# [2, 75, [10, 0], 4, "COMP333"],
# 7:30 -> 10:00
def ldown(cources: list[Course]):
    l = []
    k = 0
    for i in cources:
        l.append([2])
        time = i.time_display

        try:
            Hour1 = int(time[6:8])
        except:
            Hour1 = int(time[6])
        try:
            Hour2 = int(time[:2])
        except:
            Hour2 = int(time[0])

        sumHours = (Hour1 - Hour2)  # sumHours
        if sumHours < 0:
            sumHours += 12

        if time[7]!=':':
            sumMin = (int(time[9:11]) - int(time[3:5]))  # sumMin

        else:
            sumMin = (int(time[8:10]) - int(time[3:5]))  # sumMin

        if sumMin < 0:
            sumMin += 60
            sumHours -= 1
        while (sumHours > 0):
            sumHours -= 1
            sumMin += 60
        l[k].append(sumMin)
        l[k].append([int(time[0:2]), int(time[3:5])])

        if len(i.days) > 1:
            if i.days[0] == 'S':
                l[k].append(0)
                l[k].append(i.course_label)
                l[k].append(i)
                if i.days[2] == 'M':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                    k += 1
                elif i.days[2] == 'W':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                    k += 1
                elif i.days[2] == 'T':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                    k += 1
                elif i.days[2] == 'R':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                    k += 1
                elif i.days[2] == 'S':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                    k += 1
                else:
                    raise Exception(f"Error we got unknown day with S ==> {i.days[2]}")
            elif i.days[0] == 'M':
                l[k].append(2)
                l[k].append(i.course_label)
                l[k].append(i)
                if i.days[2] == 'W':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                    k += 1
                elif i.days[2] == 'T':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                    k += 1
                elif i.days[2] == 'R':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                    k += 1
                elif i.days[2] == 'S':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                    k += 1
                elif i.days[2] == 'M':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                    k += 1
                else:
                    raise Exception(f"Error we got unknown day with M ==> {i.days[2]}")
            elif i.days[0] == 'W':
                l[k].append(4)
                l[k].append(i.course_label)
                l[k].append(i)
                if i.days[2] == 'M':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                    k += 1
                elif i.days[2] == 'T':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                    k += 1
                elif i.days[2] == 'R':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                    k += 1
                elif i.days[2] == 'S':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                    k += 1
                elif i.days[2] == 'W':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                    k += 1
                else:
                    raise Exception(f"Error we got unknown day with W ==> {i.days[2]}")
            elif i.days[0] == 'T':
                l[k].append(3)
                l[k].append(i.course_label)
                l[k].append(i)
                if i.days[2] == 'R':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                    k += 1
                elif i.days[2] == 'M':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                    k += 1
                elif i.days[2] == 'W':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                    k += 1
                elif i.days[2] == 'S':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                    k += 1
                elif i.days[2] == 'T':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                    k += 1
                else:
                    raise Exception(f"Error we got unknown day with T ==> {i.days[2]}")
            elif i.days[0] == 'R':
                l[k].append(5)
                l[k].append(i.course_label)
                l[k].append(i)
                if i.days[2] == 'T':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 3, i.course_label, i])
                    k += 1
                elif i.days[2] == 'M':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 2, i.course_label, i])
                    k += 1
                elif i.days[2] == 'W':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 4, i.course_label, i])
                    k += 1
                elif i.days[2] == 'S':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 0, i.course_label, i])
                    k += 1
                elif i.days[2] == 'R':
                    l.append([2, sumMin, [int(time[0:2]), int(time[3:5])], 5, i.course_label, i])
                    k += 1
                else:
                    raise Exception(f"Error we got unknown day with T ==> {i.days[2]}")
            else:
                raise Exception(f"Error we got unknown day ==> {i.days[0]}")

        elif (len(i.days) == 1):
            if i.days == 'S':
                l[k].append(0)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'M':
                l[k].append(2)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'T':
                l[k].append(3)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'W':
                l[k].append(4)
                l[k].append(i.course_label)
                l[k].append(i)
            elif i.days == 'R':
                l[k].append(5)
                l[k].append(i.course_label)
                l[k].append(i)
            else:
                raise Exception(f"Error we got unknown day ==> {i.days}")

        else:
            raise Exception(f"Error we got error with the size of the days ==> {i.days}")

        k += 1

    return l


# ['COMP333', '1', 'داتا', 'باسل', 'M,W', '10:00-11:15', 'masri202'],
def lup_loop(cources: list[Course]):
    lup = []
    for i in cources:
        lup.append([i.course_label, i.section, i.instructor, i.days, i.time_display])

    return lup


f = open("Table.txt", "r")
dec = {}
x = f.readline()

while x:

    if x == '\n':
        x = f.readline()
        continue
    else:
        courseName = (x[0:8])
        if courseName[len(courseName)-1]=='i':
            courseName=courseName[:len(courseName)-1]


        sec = (x[9])
        Dr = ''
        day = ''
        time = ''

        for i in range(12, len(x)):

            if x[i] == '-':
                Dr = (x[11:i])

                day = (x[i + 1:i + 4])
                if day == "Tue":
                    day = 'T'
                elif day == "Wen":
                    day = "W"
                elif day == "Mon":
                    day = "M"
                elif day == "Sat":
                    day = "S"
                elif day == "Thu":
                    day = "R"
                else:
                    raise Exception(f"Error in day at file input --> {day}")

                if (x[i + 6] == ':'):
                    time += '0'

                    time += x[i + 5:i + 18]

                else:

                    time += x[i + 5:i + 19]
                time = time[0:5] + '-' + time[9:]

                break

        if (courseName + "-" + sec) in dec:
            if courseName[5] == '1':
                raise Exception(f"we got two labs with same section -->{courseName}-{sec}")
            else:  # add the second day to dec[courseName+'-'+sec].days only if its a lecture
                d1 = dec[courseName + '-' + sec].days
                if time != dec[courseName + '-' + sec].time_display:
                    dec[courseName + '-' + sec].time_display += "//" + time

                if (d1 == 'M' and day == 'W') or (d1 == 'W' and day == 'M'):
                    dec[courseName + '-' + sec].days = 'M,W'
                elif (d1 == 'M' and day == 'T') or (d1 == 'T' and day == 'M'):
                    dec[courseName + '-' + sec].days = 'M,T'
                elif (d1 == 'M' and day == 'R') or (d1 == 'R' and day == 'M'):
                    dec[courseName + '-' + sec].days = 'M,R'

                elif (d1 == 'T' and day == 'R') or (d1 == 'R' and day == 'T'):
                    dec[courseName + '-' + sec].days = 'T,R'
                elif (d1 == 'T' and day == 'W') or (d1 == 'W' and day == 'T'):
                    dec[courseName + '-' + sec].days = 'T,W'
                elif (d1 == 'W' and day == 'R') or (d1 == 'R' and day == 'W'):
                    dec[courseName + '-' + sec].days = 'W,R'
                elif (d1 == 'S' and day == 'M') or (d1 == 'M' and day == 'S'):
                    dec[courseName + '-' + sec].days = 'S,M'
                elif (d1 == 'S' and day == 'W') or (d1 == 'W' and day == 'S'):
                    dec[courseName + '-' + sec].days = 'S,W'
                elif (d1 == 'S' and day == 'R') or (d1 == 'R' and day == 'S'):
                    dec[courseName + '-' + sec].days = 'S,R'
                elif (d1 == 'S' and day == 'T') or (d1 == 'T' and day == 'S'):
                    dec[courseName + '-' + sec].days = 'S,T'


                elif (d1 == 'S' and day == 'S'):
                    dec[courseName + '-' + sec].days = 'S,S'
                elif (d1 == 'M' and day == 'M'):
                    dec[courseName + '-' + sec].days = 'M,M'
                elif (d1 == 'T' and day == 'T'):
                    dec[courseName + '-' + sec].days = 'T,T'
                elif (d1 == 'W' and day == 'W'):
                    dec[courseName + '-' + sec].days = 'W,W'
                elif (d1 == 'R' and day == 'R'):
                    dec[courseName + '-' + sec].days = 'R,R'
                else:
                    raise Exception(
                        f"we got two unexpected days  -->{d1}-{day} in {dec[courseName + '-' + sec].course_label}-{sec}")


        else:  # if we got a course for a first time we will add it to the dec{}
            dec[courseName + "-" + sec] = Course(course_label=courseName, section=sec, instructor=Dr, days=day,
                                                 time_display=time)

        x = f.readline()

l = []

#############################################################################################################
# we need to break here adding the interface

start(dec)
# exit(1)
##########################################################################################################
