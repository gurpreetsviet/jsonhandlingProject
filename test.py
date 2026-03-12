def Save():
    print("save fun running")
def Update():
    pass
def Delete():
    pass
def Search():
    pass
def Cancel():
    pass
button_commands = {"Save":Save,
                   "Update":Update,
                   "Delete":Delete,
                   "Search":Search,
                   "Cancel":Cancel
                   }


for i,b_name in enumerate(button_commands):
    # print(i)
    # print(b_name)
    button_commands[b_name]()

