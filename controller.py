import view
import model

def run():
    view.menu()
    num = view.input_mode()
    func(num)



def func(num):
    if num == 1:
        view.print_base(model.read_file())
    elif num == 2:
        model.add_people(view.new_people())
    elif num == 3:
        people = model.find_people(view.find_people())
        view.print_find(people)
    elif num == 4:
        id = view.input_id()
        new_data = view.input_data()
        model.edit_people(id, new_data)
