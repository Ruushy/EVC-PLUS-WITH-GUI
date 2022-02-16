from tkinter import *
import tkinter.messagebox


class application:
    def __init__(self, master):
        self.master = master
        self.password = Label(master, text="fadlan gali pinkaga: ", font='arial 30 bold ')
        self.password.place(x=200, y=50)
        self.passentry = Entry(master, width=40)
        self.passentry.place(x=260, y=110)
        self.passbox = Button(master, text="OK", width=20, height=2, fg='black', bg='cyan', command=self.passcheck)
        self.passbox.place(x=290, y=165)

    def passcheck(self):
        with open("Password File.txt", "r") as self.File:
            self.file_Var = self.File.read()
            self.passwo = self.file_Var

        if self.passentry.get() == self.passwo:

            self.password.destroy()
            self.passentry.destroy()
            self.passentry.destroy()
            self.passbox.destroy()

            self.dooro = Label(self.master, fg='steelblue', text="fadlan dooro", font='arial 25 bold')
            self.dooro.place(x=250, y=40)

            self.haraaga = Label(self.master, text="1: Haragaaga: ", font='arial 15 bold')
            self.haraaga.place(x=260, y=90)

            self.kaarka = Label(self.master, text="2: kaarka ku hadalka : ", font='arial 15 bold')
            self.kaarka.place(x=260, y=120)

            self.bixi = Label(self.master, text="3: Bixi biil : ", font='arial 15 bold')
            self.bixi.place(x=260, y=150)

            self.evc = Label(self.master, text="4: EVCPlus : ", font='arial 15 bold')
            self.evc.place(x=260, y=180)

            self.warbixin = Label(self.master, text="5: Warbixin kjooban: ", font='arial 15 bold')
            self.warbixin.place(x=260, y=210)

            self.salaam = Label(self.master, text="6: Salaambank ", font='arial 15 bold')
            self.salaam.place(x=260, y=240)

            self.maaraynta = Label(self.master, text="7:maaraynta : ", font='arial 15 bold')
            self.maaraynta.place(x=260, y=270)


            self.second = Entry(self.master, width=20)
            self.second.place(x=280, y=370)

            self.evpox = Button(self.master, text="submit", bg='cyan', width=15, command=self.adeeg)
            self.evpox.place(x=290, y=400)




        elif self.passentry.get() == "":
            tkinter.messagebox.showinfo("", "fadlan gali pinka ")
        else:
            tkinter.messagebox.showinfo("ERROR", "pinkaga waa khalad")

    def destroying(self):
        self.dooro.destroy()
        self.haraaga.destroy()
        self.kaarka.destroy()
        self.bixi.destroy()
        self.evc.destroy()
        self.warbixin.destroy()
        self.salaam.destroy()
        self.maaraynta.destroy()
        self.second.destroy()
        self.evpox.destroy()

    def adeeg(self):
        self.b = self.second.get()
        self.b = int(self.b)

        if self.b == 1:
            self.destroying()
            Label(self.master, text="haraagagu waa 200", font='arial 40 bold', fg='steelblue').place(x=250, y=100)
        elif self.b == 2:
            self.destroying()
            self.kushubo = Label(self.master, text="ku shubo", font="arial 20 bold ")
            self.kushubo.place(x=260, y=100)
            self.ugushubo = Label(self.master, text="ugu shubo", font="arial 20 bold ")
            self.ugushubo.place(x=260, y=130)
            self.kaar = Entry(self.master, width=20)
            self.kaar.place(x=270, y=180)
            self.kaarpox = Button(self.master, text='submit', bg='cyan', fg='black', width=15, command=self.checkaar)
            self.kaarpox.place(x=270, y=210)
        elif self.b == 3:
            self.destroying()
            self.bixi = Label(self.master, text="1.Ku Iibso\n2.Kabax", font="arial 20 bold ").place(x=260, y=100)
            self.entryka = Entry(self.master, width=20)
            self.entryka.place(x=270, y=180)
            self.bixibtn = Button(self.master, text='submit', bg='cyan', fg='black', width=15,
                                  command=self.bixifunc).place(x=270, y=210)

        elif self.b == 4:
            self.destroying()
            self.num4 = Label(self.master, text="fadlan gali numberka aad u warejineyso", font='arial 15 bold').place(
                x=260, y=90)
            self.lacag4 = Entry(self.master, width=20)
            self.lacag4.place(x=270, y=130)
            self.num5 = Label(self.master, text="fadlan gali lacagta ", font='arial 15 bold').place(x=260, y=170)
            self.lacag5 = Entry(self.master, width=20)
            self.lacag5.place(x=270, y=200)
            self.lacagpox4 = Button(self.master, text="submit", bg='cyan', width=15, command=self.evcplus)
            self.lacagpox4.place(x=270, y=250)

        elif self.b == 5:
            self.destroying()
            self.warbixin = Label(self.master, text="Warbixin Kooban", font="arial 15 bold").place(x=260, y=90)
            self.optionswarbin = Label(self.master, text="1.Last Action\n2.All Action", font="arial 15 bold").place(
                x=260, y=120)
            self.optionEntry = Entry(self.master, width=20)
            self.optionEntry.place(x=270, y=200)
            self.optionButton = Button(self.master, text="submit", bg='cyan', width=15,
                                       command=self.warbixin_fun).place(x=270, y=250)
        elif self.b == 7:
            self.destroying()
            Label(self.master, text="1.Badal pinkaga\n2.Kabax", font="arial 15 bold").place(x=260, y=120)
            self.optionEntry = Entry(self.master, width=20)
            self.optionEntry.place(x=270, y=200)
            Button(self.master, text="submit", bg='cyan', width=15, command=self.mareyn_fun).place(x=270, y=250)


    # ==========================================start command Functions============================================================#

    def checkaar(self):
        self.kaar_hubi = self.kaar.get()
        self.kaar_hubi = int(self.kaar_hubi)

        if self.kaar_hubi == 1:
            self.kushubo.destroy()
            self.ugushubo.destroy()
            self.kaar.destroy()
            self.kaarpox.destroy()
            Label(self.master, text="fadlan gali lagta aad ku shubaneyso", font='arial 15 bold').place(x=260, y=90)
            self.lacag = Entry(self.master, width=20)
            self.lacag.place(x=270, y=130)
            self.lacagpox = Button(self.master, text="submit", bg='cyan', width=15, command=self.kushubasho)
            self.lacagpox.place(x=270, y=160)

        elif self.kaar_hubi == 2:
            self.kushubo.destroy()
            self.ugushubo.destroy()
            self.kaar.destroy()
            self.kaarpox.destroy()
            self.num1 = Label(self.master, text="fadlan gali numberka aad u warejineyso", font='arial 15 bold').place(
                x=260, y=90)
            self.lacag1 = Entry(self.master, width=20)
            self.lacag1.place(x=270, y=130)
            self.num2 = Label(self.master, text="fadlan gali lacagta ", font='arial 15 bold').place(x=260, y=170)
            self.lacag2 = Entry(self.master, width=20)
            self.lacag2.place(x=270, y=200)
            self.lacagpox1 = Button(self.master, text="submit", bg='cyan', width=15, command=self.tuurid)
            self.lacagpox1.place(x=270, y=250)


        elif self.kaar_hubi == "":
            tkinter.messagebox.showinfo(" ", "fadlan dooro number 1")
        else:
            tkinter.messagebox.showinfo(" ", "invalid number")
            root.destroy()

    def bixifunc(self):
        try:
            self.hubin = self.entryka.get()
            self.hubin = int(self.hubin)
            if self.hubin == 1:
                Label(self.master, text="", fg='cyan', font='arial 15 bold').place(x=260, y=90, width=400, height=200)
                Label(self.master, text="Fadlan Soo Gali Numberka Ganacsadaha", fg='cyan', font='arial 15 bold').place(
                    x=260, y=80, width=400, height=200)
                self.gn = Entry(self.master, width=30, font='15')
                self.gn.place(x=280, y=200)
                self.btn2 = Button(self.master, text="submit", bg='cyan', width=15).place(x=270, y=250)
            elif self.hubin == 2:
                self.xaqiijin = tkinter.messagebox.askquestion("ERROR", "ma hubtaa inaad kabaxayso")
                if self.xaqiijin == "yes":
                    root.destroy()
        except ValueError:
            tkinter.messagebox.showinfo("ERROR", "Fadlan Hasoo galin Xaraf\n\tiyo number jajab ah")

    def tuurid(self):
        self.tuurid = self.lacag1.get()
        self.tuurid1 = self.lacag2.get()

        if self.tuurid == "":
            tkinter.messagebox.showinfo(" ", "fadlan gali lacagta ama numberka ")
        elif self.tuurid1 == "":
            tkinter.messagebox.showinfo(" ", "fadlan gali lacagta ama numberka ")
        else:
            res = tkinter.messagebox.askquestion(" ma hubtaa", " in lactan warejiso")
            if res == "yes":
                tkinter.messagebox.showinfo("mahadsanid", "howshada waa laguu qabtay")
                root.destroy()
            else:
                root.destroy()

    def kushubasho(self):
        self.kush = self.lacag.get()
        self.kush = int(self.kush)

        if self.kush == "":
            tkinter.messagebox.showinfo(" ", "fadlan gali lacagta ")
        elif self.kush > 300:
            tkinter.messagebox.showinfo(" ", "lacagtas badan lama gudbin karo")

        else:
            rest = tkinter.messagebox.askquestion(" ma hubtaa", " in lacgtan ku shubato")
            if rest == "yes":
                tkinter.messagebox.showinfo("mahadsanid", "howshada waa laguu qabtay")
                root.destroy()
            else:
                root.destroy()

    def evcplus(self):
        self.tuurid4 = self.lacag4.get()
        self.tuurid5 = self.lacag5.get()

        if self.tuurid4 == "":
            tkinter.messagebox.showinfo(" ", "fadlan gali lacagta ama numberka ")
        elif self.tuurid5 == "":
            tkinter.messagebox.showinfo(" ", "fadlan gali lacagta ama numberka ")
        else:
            res = tkinter.messagebox.askquestion(" ma hubtaa", " in lacagtan warejiso")
            if res == "yes":
                with open("Wareejin.txt", "a") as self.Wareejin:
                    self.write1 = self.Wareejin.write("Waxaad $")
                    self.write2 = self.Wareejin.write(self.tuurid5)
                    self.write3 = self.Wareejin.write(" u wareejisay numberkan ")
                    self.write4 = self.Wareejin.write(self.tuurid4)
                    self.write5 = self.Wareejin.write("\n")

                tkinter.messagebox.showinfo("mahadsanid", "howshada waa laguu qabtay")
                root.destroy()
            else:
                root.destroy()

    def warbixin_fun(self):

        try:

            self.option1 = self.optionEntry.get()
            self.option1 = int(self.option1)
            if self.option1 == 1:
                with open("Wareejin.txt", "r") as self.action1:
                    for self.aqriye in self.action1:
                        self.aqriye1 = self.action1.readline()
                Label(self.master, text=self.aqriye1).place(x=260, y=80, width=900, height=200)
            elif self.option1 == 2:
                with open("Wareejin.txt", "r") as self.action1:
                    for self.aqriye in self.action1:
                        self.aqriye2 = self.action1.read()
                        self.aqr_soobandhig = self.aqriye2 + self.aqriye
                Label(self.master, text=self.aqr_soobandhig).place(x=260, y=80, width=900, height=200)
            elif self.option1 <= 0 or self.option1 >= 3:
                tkinter.messagebox.showinfo("ERROR", "Fadlan dooro number sax ah!")
        except ValueError:
            tkinter.messagebox.showinfo("ERROR", "Fadlan Hasoo galin Xaraf\n\tiyo number jajab ah")

    def mareyn_fun(self):
        try:
            self.var1 = self.optionEntry.get()
            self.var1 = int(self.var1)
            if self.var1 == 1:

                Label(self.master, text="soo gali pin ka cusub", font="arial 20 bold").place(x=210, y=90, width=400,
                                                                                             height=200)
                self.passw = Entry(self.master, font="20", width=20, bg="lightyellow")
                self.passw.place(x=270, y=210)
                self.passw_btn = Button(self.master, text="submit", bg='cyan', width=15, command=self.pass_func).place(
                    x=270, y=250)
            elif self.var1 == 2:
                root.destroy()
            else:
                tkinter.messagebox.showinfo("ERROR", "Fadlan dooro number sax ah!")


        except ValueError:
            tkinter.messagebox.showinfo("ERROR", "Fadlan Hasoo galin Xaraf\n\tiyo number jajab ah")

    def pass_func(self):
        try:
            self.varr = self.passw.get()
            self.varr = int(self.varr)

            if self.varr >= 1001 or self.varr < 10000:
                with open("Password File.txt", "w") as self.ff:
                    self.varr2 = self.passw.get()
                    self.pas = self.ff.write(self.varr2)
                    tkinter.messagebox.showinfo("mahadsanid", "Waad ku guulaysatay Badalidda pinka")
                    root.destroy()
            else:
                tkinter.messagebox.showinfo("ERROR", "Fadlan soo gali pin ka \n\tkooban 4 god")


        except ValueError:
            tkinter.messagebox.showinfo("ERROR", "Fadlan Hasoo galin Xaraf\n\tiyo number jajab ah")


root = Tk()
root.geometry("1350x750")
root.resizable(False, False)
b = application(root)

root.mainloop()
