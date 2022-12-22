import view
import model

def run():
    b = True
    while b:
        view.menu()
        num = view.input_mode()
        if num == '1':
            view.print_base(model.read_file())
        elif num == '2':
            model.add_people(view.new_people())
        elif num == '3':
            people = view.find_people()
            result = model.find_people(people)
            view.print_find(people, result)
        elif num == '4':
            id = view.input_id()
            new_data = view.input_data()
            model.edit_people(id, new_data)
        else:
            b = False