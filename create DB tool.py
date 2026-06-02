import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from glob import glob

class App:
	# window
	def __init__(self, root):

		self.fields = []

		self.root = root
		# entry containing the db name
		
		self.l = tk.Label(self.root, text="Create a db [insert the name]")
		self.l.pack()

		self.db = tk.StringVar()
		self.e = tk.Entry(self.root, textvariable=self.db)
		self.e.pack()

		self.b = tk.Button(self.root, text="Create DB", command= lambda: self.mk_db())
		self.b.pack()

		self.lb = tk.Listbox(self.root)
		self.lb.pack()
		self.show_db()

		# label and Entry for Database name
		self.ldbname = tk.Label(self.root, text="Insert Database name")
		self.ldbname.pack()
		self.dbn = tk.StringVar()
		self.edb = tk.Entry(self.root, textvariable = self.dbn)
		self.edb.pack()
 
		self.ltbname = tk.Label(self.root, text="Insert Table name")
		self.ltbname.pack()
		self.tbn = tk.StringVar()
		self.etb = tk.Entry(self.root, textvariable = self.tbn)
		self.etb.pack()

		# FIELDS - vfl is the StringVar, efl is the Entry
		self.lflname = tk.Label(self.root, text="Insert Fields name and type\n followeb by a comma, one by one,\nclicking once for each field.")
		self.lflname.pack()
		self.vfl = tk.StringVar()
		self.efl = tk.Entry(self.root, textvariable = self.vfl)
		self.efl.pack()
		self.bfl = tk.Button(self.root, text="Create Field", command= lambda: self.mk_fl())
		self.bfl.pack()

		self.btb = tk.Button(self.root, text="Create Table", command= lambda: self.mk_tb(self.dbn, self.tbn))
		self.btb.pack()

	def show_db(self):
		for file in glob("*.db"):
			self.lb.insert(tk.END, file)

	def mk_db(self):
		db = self.e.get()
		if db.endswith(".db"):
			pass
		else:
			db = db + ".db"
		try:
			conn = lite.connect(db)
			if db in self.lb.get(0, tk.END):
				pass
			else:
				self.lb.insert(tk.END, db)
			return conn
		except Error as e:
			print(e)
		finally:
			self.db.set("")
			conn.close()

	def mk_tb(self, dbn, tbn):
		self.conn = lite.connect(dbn.get())
		self.cur = self.conn.cursor()
		self.fields = "".join(self.fields)
		self.cur.execute("""create table {} (
		{});""".format(tbn, self.fields))
		self.fields = []
		self.conn.close()

	def mk_fl(self):
		self.fields.append(self.efl.get())
		self.vfl.set("")

root = tk.Tk()	
win = App(root)
root.mainloop()
