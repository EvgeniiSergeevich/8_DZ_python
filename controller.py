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
            people = view.new_people()
            model.add_people(people)
            view.add_ready(people)
        elif num == '3':
            people = view.find_people()
            result = model.find_people(people)
            view.print_find(people, result)
        elif num == '4':
            id = view.input_id()
            view.print_find(id, model.find_people(id))
            new_data = view.input_data()
            l = model.edit_people(id, new_data)
            view.change()
        else:
            b = False