import PySimpleGUI as sg
import csv

# Manually set the window style
def vcsv():
    filename = sg.PopupGetFile('Get required file', no_window=True, file_types=(("CSV Files", "*.csv"),))
    data = []

    # Read csv
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Get headings
        data = list(reader)    # Read everything else into a list of rows

    col_layout = [
        [sg.Text('Attendance Report', font='Helvetica 28', justification='center', pad=(0, 10))],
        [sg.Table(
            values=data, headings=header, col_widths=(5, 15, 10, 15, 15, 10, 10), auto_size_columns=False,
            max_col_width=30, size=(None, len(data)), font='Helvetica 14', justification='center',
            background_color='#303030', text_color='white', alternating_row_color='#505050'
        )],
        [sg.Button('Back', font=('Arial', 14, 'bold'), size=(15, 1), pad=(0, 25))]
    ]

    layout = [[sg.Column(col_layout, size=(1050, 500), scrollable=True, element_justification='center')]]

    # Create the window with manually set background color
    window = sg.Window('Attendance', layout, grab_anywhere=False, element_justification='c', location=(200, 150),
                       background_color='#303030')

    event, values = window.read()  # Use read() instead of Read()
    while True:
        if event == 'Back' or event == sg.WIN_CLOSED:
            window.close()
            break
5
