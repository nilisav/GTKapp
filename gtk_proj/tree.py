import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import json


store = Gtk.TreeStore(str)

with open('example_2.json') as f:
    quiz = json.load(f)
    their_parent = store.append(None, [list(quiz.items())[0][0]])
    quiz2 = quiz['quiz']


def recursion(parent, quiz):
    if type(quiz) is dict:
        for i1, i2 in quiz.items():
            new_parent = store.append(parent, [str(i1)])
            recursion(new_parent, i2)
    elif type(quiz) is list:
        for i2 in quiz:
            store.append(parent, [str(i2)])
    elif type(quiz) is str:
        store.append(parent, [str(quiz)])


recursion(their_parent, quiz2)
view = Gtk.TreeView(model=store)
renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Квиз", renderer, text=0)
view.append_column(column)
