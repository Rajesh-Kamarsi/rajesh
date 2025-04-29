import os
import Capture_Image
import Train_Image
import Recognize
import view_attendance
import PySimpleGUI as sg

def mainMenu():
    # Set theme for the window
    sg.set_options(background_color='black', text_element_background_color='black', element_text_color='white')

    menu_def = [['&File', ['&Open Attendance Folder', '&Open Student Records', '---', 'E&xit', ]]]
    
    # Layout for the main menu window
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('Attendance Capture System Using Face Recognition ', font='Helvetica 30', justification='center')],
        [sg.Image(r'Images/Facial_Recognition_logo.png', size=(650, 450))],
        [sg.Button("Mark Attendance", size=(82, 2), font='Helvetica 14', button_color=('white', '#303030'))],
        [sg.Button("Add Person", size=(40, 2), font='Helvetica 14', button_color=('white', '#303030')),
         sg.Button("Train Images", size=(40, 2), font='Helvetica 14', button_color=('white', '#303030'))],
        [sg.Button("View Attendance", size=(40, 2), font='Helvetica 14', button_color=('white', '#303030')),
         sg.Button("Quit", size=(40, 2), font='Helvetica 14', button_color=('white', 'red'))]
    ]

    window = sg.Window('Face Attendance Recognition Program', layout, auto_size_buttons=False, element_justification='c')

    while True:
        event, values = window.read(timeout=0.1)
        
        # Exit condition
        if event == "Quit" or event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break
        
        # Open Attendance Folder
        elif event == "Open Attendance Folder":
            path = "Attendance"
            path = os.path.realpath(path)
            os.startfile(path)
        
        # Open Student Records
        elif event == "Open Student Records":
            path = "StudentDetails"
            path = os.path.realpath(path)
            os.startfile(path)
        
        # Add Person (opens the Capture Image window)
        elif event == "Add Person":
            window.close()
            Capture_Image.takeImages()
            mainMenu()
            break
        
        # Train Images (opens the Train Image window)
        elif event == "Train Images":
            window.close()
            Train_Image.TrainImages()
            mainMenu()
            break
        
        # Mark Attendance (opens the Recognize window)
        elif event == "Mark Attendance":
            window.close()
            Recognize.recognize_attendence()
            mainMenu()
            break
        
        # View Attendance (opens the View Attendance window)
        elif event == "View Attendance":
            window.close()
            view_attendance.vcsv()
            mainMenu()
            break

    window.close()  # Close the window after the loop ends

# Run the main menu
mainMenu()
