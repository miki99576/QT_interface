import PySimpleGUI as sg

def create_row(row_counter, row_number_view):
    row =  [sg.pin(
        sg.Col([[
            sg.Button("X", border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key=('-DEL-', row_counter)),
            sg.Input(size=(20,1), key=('-DESC-', row_counter)),
            sg.Text(f'Row {row_number_view}', key=('-STATUS-', row_counter))]],
        key=('-ROW-', row_counter)
        ))]
    return row



layout = [  [sg.Text('Add and "Delete" Rows From a Window', font='15')],
            [sg.Column([create_row(0, 1)], k='-ROW_PANEL-')],
            [sg.Text("Exit", enable_events=True, key='-EXIT-', tooltip='Exit Application'),
            sg.Text("Refresh", enable_events=True, key='-REFRESH-', tooltip='Exit Application'),
            sg.Text('+', enable_events=True, k='-ADD_ITEM-', tooltip='Add Another Item')]]

window = sg.Window('Dynamically Adding Elements', 
    layout,  use_default_focus=False, font='15')

row_counter = 0
row_number_view = 1
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break
    if event == '-ADD_ITEM-':
        row_counter += 1
        row_number_view += 1
        print("Actual Row Number: ", row_counter)
        print("Displayed Row Number: ", row_number_view)
        # Allows you to add items to a layout
        # These items cannot be deleted, but can be made invisible
        window.extend_layout(window['-ROW_PANEL-'], [create_row(row_counter, row_number_view)])
    elif event[0] == '-DEL-':
        row_number_view -= 1
        window[('-ROW-', event[1])].update(visible=False)
window.close()