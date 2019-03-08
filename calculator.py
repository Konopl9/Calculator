# ------------------------------------------------------------------------------#
# Kalkulacka                                                                   #
# ------------------------------------------------------------------------------#

# lst.append(x)
# eval("5+5")
# s = "".join(lst) //// "separator Mezi Prvky Pole".join(lst) ///eg. ";".join(lst) -> output -> prvek1;prvek2;


from tkinter import *
from math import *
from tkinter.font import *


def callback(f, *a):
    """
    Vraci funkci f s nastavenym parametrem a.
    Tato funkce umi osetrit i vice nez jeden parametr.

    Pouziti:
        callback(funkce, arg1, arg2, ..., argn )
    """
    return lambda: f(*a)


class MyApp:

    def big(self):
        self.font.config(size=15)

    def normal(self):
        self.font.config(size=10)

    def insKey(self, znak):
        if znak is '=':
            if '+' in self.operator:
                numbers = self.operator.split('+')
                sum = float(numbers[0]) + float(numbers[1])
                self.operator = sum
                self.fo.set(sum)
                self.operator = ''
            if '-' in self.operator:
                numbers = self.operator.split('-')
                diff = float(numbers[0]) - float(numbers[1])
                self.operator = diff
                self.fo.set(diff)
                self.operator = ''
            if '*' in self.operator:
                numbers = self.operator.split('*')
                mult = float(numbers[0]) * float(numbers[1])
                self.operator = mult
                self.fo.set(mult)
                self.operator = ''
            if '/' in self.operator:
                numbers = self.operator.split('/')
                div = float(numbers[0]) + float(numbers[1])
                self.operator = div
                self.fo.set(div)
                self.operator = ''
        else:
            self.operator = self.operator + str(znak)
            self.fo.set(self.operator)
        if znak == 'Cls':
            self.operator = ""
            self.fo.set(self.operator)

    def __init__(self, root):
        self.fo = StringVar()
        self.operator = ""
        root.title("Calculator")

        self.font = Font(family='Helvetica', weight='bold', size=10)

        self.la = Label(root, textvariable=self.fo, background="#ffffff", anchor=E, relief=SUNKEN, height=2,
                        font=self.font)
        self.la.pack(fill=X, side=TOP, padx=8, pady=5)
    # Frame 1 radiobutton
        self.opts = Frame(root, relief=GROOVE)
        self.opts.pack()
        self.nor = Radiobutton(self.opts, text="Normal", value="normal", command=self.normal,
                               font=self.font)
        self.nor.pack(side=LEFT)
        self.big = Radiobutton(self.opts, text="Big", value='big', command=self.big, font=self.font)
        self.big.pack(side=RIGHT)

        # Frame 2 calc buttons
        self.numbts = Frame(root, relief=GROOVE)
        self.numbts.pack(fill=BOTH,expand=1, padx=4, pady=4)
        self.numbts.grid_columnconfigure(1, weight=1)
        self.cls = Button(self.numbts, text="Cls", width=5, height=2, font=self.font,
                          command=callback(self.insKey, "Cls"))
        self.division = Button(self.numbts, text="/", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "/"))
        self.multiplication = Button(self.numbts, text="*", width=5, height=2, font=self.font,
                                     command=callback(self.insKey, "*"))
        self.subtraction = Button(self.numbts, text="-", width=5, height=2, font=self.font,
                                  command=callback(self.insKey, "-"))
        self.addition = Button(self.numbts, text="+", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "+"))
        self.equal = Button(self.numbts, text="=", width=5, height=2, font=self.font,
                            command=callback(self.insKey, "="))
        self.comma = Button(self.numbts, text=",", width=5, height=2, font=self.font,
                            command=callback(self.insKey, "."))
        self.number_9 = Button(self.numbts, text="9", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "9"))
        self.number_8 = Button(self.numbts, text="8", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "8"))
        self.number_7 = Button(self.numbts, text="7", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "7"))
        self.number_6 = Button(self.numbts, text="6", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "6"))
        self.number_5 = Button(self.numbts, text="5", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "5"))
        self.number_4 = Button(self.numbts, text="4", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "4"))
        self.number_3 = Button(self.numbts, text="3", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "3"))
        self.number_2 = Button(self.numbts, text="2", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "2"))
        self.number_1 = Button(self.numbts, text="1", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "1"))
        self.number_0 = Button(self.numbts, text="0", width=5, height=2, font=self.font,
                               command=callback(self.insKey, "0"))
        # All buttons in list
        self.creator = Label(root, text='Cviceni 3 URO: mis0066', fg="blue", font=self.font)
        self.creator.pack(fill=X, side=BOTTOM, padx=8, pady=5)
        self.cls.grid(row=1, column=1, sticky=W + E + N + S, padx=2, pady=2)
        self.division.grid(row=1, column=2, sticky=W + E + N + S, padx=2, pady=2)
        self.multiplication.grid(row=1, column=3, sticky=W + E + N + S, padx=2, pady=2)
        self.subtraction.grid(row=1, column=4, sticky=W + E + N + S, padx=2, pady=2)
        self.addition.grid(row=2, column=4, rowspan=2, sticky=W + E + N + S, padx=2, pady=2)
        self.equal.grid(row=4, column=4, rowspan=2, sticky=W + E + N + S, padx=2, pady=2)
        self.comma.grid(row=5, column=3, sticky=W + E + N + S, padx=2, pady=2)
        self.number_9.grid(row=2, column=3, sticky=W + E + N + S, padx=2, pady=2)
        self.number_8.grid(row=2, column=2, sticky=W + E + N + S, padx=2, pady=2)
        self.number_7.grid(row=2, column=1, sticky=W + E + N + S, padx=2, pady=2)
        self.number_6.grid(row=3, column=3, sticky=W + E + N + S, padx=2, pady=2)
        self.number_5.grid(row=3, column=2, sticky=W + E + N + S, padx=2, pady=2)
        self.number_4.grid(row=3, column=1, sticky=W + E + N + S, padx=2, pady=2)
        self.number_3.grid(row=4, column=3, sticky=W + E + N + S, padx=2, pady=2)
        self.number_2.grid(row=4, column=2, sticky=W + E + N + S, padx=2, pady=2)
        self.number_1.grid(row=4, column=1, sticky=W + E + N + S, padx=2, pady=2)
        self.number_0.grid(row=5, column=1, columnspan=2, sticky=W + E + N + S, padx=2, pady=2)
        self.cls.config(state=NORMAL)
        self.division.config(state=NORMAL)
        self.multiplication.config(state=NORMAL)
        self.subtraction.config(state=NORMAL)
        self.addition.config(state=NORMAL)
        self.equal.config(state=NORMAL)
        self.comma.config(state=NORMAL)
        self.number_9.config(state=NORMAL)
        self.number_8.config(state=NORMAL)
        self.number_7.config(state=NORMAL)
        self.number_6.config(state=NORMAL)
        self.number_5.config(state=NORMAL)
        self.number_4.config(state=NORMAL)
        self.number_3.config(state=NORMAL)
        self.number_2.config(state=NORMAL)
        self.number_1.config(state=NORMAL)
        self.number_0.config(state=NORMAL)
        self.nor.select()
        self.numbts.rowconfigure(1, weight=1)
        self.numbts.rowconfigure(2, weight=1)
        self.numbts.rowconfigure(3, weight=1)
        self.numbts.rowconfigure(4, weight=1)
        self.numbts.rowconfigure(5, weight=1)
        self.numbts.columnconfigure(1, weight=1)
        self.numbts.columnconfigure(2, weight=1)
        self.numbts.columnconfigure(3, weight=1)
        self.numbts.columnconfigure(4, weight=1)



root = Tk()
app = MyApp(root)
root.mainloop()
root.destroy()

