import datetime
import calendar

import tkinter as tk
data={}
l1,l2,l3,l4,l5=[],[],[],[],[]

class Calendar:
    def __init__(self, parent):
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.wid = []
        self.day_selected = datetime.date.today().day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''

        self.setup(self.year, self.month)

    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            # w.destroy()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        # self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1

        # self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)

    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name

        # data
        data['day_selected'] = l1
        data['month_selected'] = l2
        data['year_selected'] = l3
        data['day_name'] = l4
        data['month_name'] = l5
        l1.append(self.day_selected)
        l2.append(self.month_selected)
        l3.append(self.year_selected)
        l4.append(self.day_name)
        l5.append(self.month)

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):
        left = tk.Button(self.parent, text='<', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=1)

        header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)

        right = tk.Button(self.parent, text='>', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5)

        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    # print(calendar.day_name[day])
                    b = tk.Button(self.parent, width=1, text=day,
                                  command=lambda day=day: self.selection(day, calendar.day_name[(day - 1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d)

        sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)

        ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)

    def kill_and_save(self):
        self.parent.destroy()

class Control:
    def __init__(self, parent,column):
        self.parent = parent
        global data
        self.choose_btn = tk.Button(self.parent, text='Choose', command=lambda : self.popup(column))
        self.show_btn = tk.Button(self.parent, text='Show Selected', command=self.print_selected_date)
        self.choose_btn.grid(column=column)
        self.label = tk.Label(self.parent, text=self.data).grid(column=column)
        self.show_btn.grid()



    #def __init__(self,parent,column):
    def print_selected_date(self,column):
        global data
        self.label = tk.Label(self.parent, text=data).grid(column=column)
        print(data)


    def popup(self, column):
        child = tk.Toplevel()
        cal = Calendar(child)
        self.print_selected_date(column)



if __name__ == '__main__':
    root = tk.Tk()
    app = Control(root)
    root.mainloop()
