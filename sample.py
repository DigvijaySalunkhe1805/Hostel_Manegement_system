from tkinter.ttk import *
from tkinter import * 
import os
from datetime import datetime
from tkinter import messagebox

# Custom color scheme
BG_COLOR = "#2a5179"
HEADER_COLOR = "#3498db"
BUTTON_COLOR = "#1687d3"
ACCENT_COLOR = "#fc5745"
TEXT_COLOR = "#ecf0f1"
ENTRY_COLOR = "#05294d"
CANVAS_COLOR = "#bdc3c7"
SUCCESS_COLOR = "#17cc62"
WARNING_COLOR = "#d1850b"

# Font styles
HEADER_FONT = ("Helvetica", 28, "bold")
TITLE_FONT = ("Helvetica", 20, "bold")
LABEL_FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 12, "bold")
ENTRY_FONT = ("Helvetica", 12)

# Create required files if they don't exist
file_names = ["inouttime.txt", "leave_applications.txt", "room_info_boys.txt", 
              "room_info_girls.txt", "student_info.txt", "room_info_others.txt", 
              "visitor_info.txt"]

for file_name in file_names:
    if not os.path.exists(file_name):
        try:
            with open(file_name, "x") as fp:
                pass
        except FileExistsError:
            print(f"File {file_name} already exists.")

def date():
    now = datetime.now()
    return now.strftime("%H:%M,%Y-%m-%d")

class RoundedButton(Canvas):
    def __init__(self, master=None, text="", radius=25, btnforeground="#000000", 
                 btnbackground="#ffffff", clicked=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(bg=BG_COLOR, bd=0, highlightthickness=0)
        self.btnbackground = btnbackground
        self.clicked = clicked
        
        self.radius = radius
        
        self.rect = self.create_rectangle(
            (0, radius, radius, 0),
            (radius, 0, radius*2, radius),
            (radius*2, radius, radius, radius*2),
            (radius, radius*2, 0, radius),
            fill=btnbackground, outline=btnbackground
        )
        
        self.text = self.create_text(
            radius, radius,
            text=text,
            fill=btnforeground,
            font=BUTTON_FONT
        )
        
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
    def _on_press(self, event):
        self.itemconfig(self.rect, fill=self._darken_color(self.btnbackground))
        
    def _on_release(self, event):
        self.itemconfig(self.rect, fill=self.btnbackground)
        if self.clicked:
            self.clicked()
            
    def _darken_color(self, color, factor=0.8):
        """Return a darker version of the given color"""
        r, g, b = self.master.winfo_rgb(color)
        r = int(r * factor / 65535 * 255)
        g = int(g * factor / 65535 * 255)
        b = int(b * factor / 65535 * 255)
        return f'#{r:02x}{g:02x}{b:02x}'

class ModernEntry(Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.placeholder = placeholder
        self.placeholder_color = 'grey'
        self.default_fg_color = self['fg']
        
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        self._add_placeholder()
        
    def _clear_placeholder(self, event=None):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            
    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert('0', self.placeholder)
            self['fg'] = self.placeholder_color

class HostelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("HOSTEL MANAGEMENT SYSTEM")
        self.root.geometry(f'{1500}x{750}+{0}+{0}')
        self.root.configure(bg=BG_COLOR)
        
        # Set window icon
        try:
            self.root.iconbitmap("hostel_icon.ico")  # Add an icon file if available
        except:
            pass
        
        self.create_login_screen()
        
    def create_login_screen(self):
        # Header
        self.header = Label(self.root, text="HOSTEL MANAGEMENT SYSTEM", 
                           font=HEADER_FONT, bg=HEADER_COLOR, fg=TEXT_COLOR, 
                           padx=400, pady=20)
        self.header.pack(fill=X)
        
        # Main frame
        self.login_frame = Frame(self.root, bg=BG_COLOR)
        self.login_frame.pack(expand=True, fill=BOTH)
        
        # Login form container
        self.form_container = Frame(self.login_frame, bg=BG_COLOR)
        self.form_container.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Login title
        self.login_title = Label(self.form_container, text="Admin Login", 
                               font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.login_title.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Username
        self.username_label = Label(self.form_container, text="Username", 
                                  font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
        
        self.username_entry = ModernEntry(self.form_container, placeholder="Enter username", 
                                        font=ENTRY_FONT, width=25, bg=ENTRY_COLOR, 
                                        fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                        relief=FLAT, highlightthickness=1, 
                                        highlightbackground=HEADER_COLOR,
                                        highlightcolor=HEADER_COLOR)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.username_entry.focus()
        
        # Password
        self.password_label = Label(self.form_container, text="Password", 
                                  font=LABEL_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)
        
        self.password_entry = ModernEntry(self.form_container, placeholder="Enter password", 
                                        font=ENTRY_FONT, width=25, bg=ENTRY_COLOR, 
                                        fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                        relief=FLAT, highlightthickness=1, 
                                        highlightbackground=HEADER_COLOR,
                                        highlightcolor=HEADER_COLOR, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Login button
        self.login_btn = Button(self.form_container, text="Login", 
                              font=BUTTON_FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                              activebackground=HEADER_COLOR, 
                              activeforeground=TEXT_COLOR,
                              relief=FLAT, padx=20, pady=5,
                              command=self.login)
        self.login_btn.grid(row=3, column=0, columnspan=2, pady=30)
        
        # Footer
        self.footer = Label(self.root, text="© 2023 Hostel Management System", 
                          font=("Helvetica", 10), bg=BG_COLOR, fg=TEXT_COLOR)
        self.footer.pack(side=BOTTOM, fill=X, pady=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "cwc":
            self.login_frame.destroy()
            self.create_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            self.username_entry.focus()
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            
    def create_main_screen(self):
        # Main container
        self.main_container = Frame(self.root, bg=BG_COLOR)
        self.main_container.pack(fill=BOTH, expand=True)
        
        # Sidebar
        self.sidebar = Frame(self.main_container, bg=BG_COLOR, width=300)
        self.sidebar.pack(side=LEFT, fill=Y)
        
        # Sidebar buttons
        buttons = [
            ("Add Student", self.add_student),
            ("Add New Room", self.add_room),
            ("In/Out Time", self.in_out_time),
            ("Visitor", self.visitor),
            ("View Information", self.view_info),
            ("Leave Application", self.leave_application),
            ("Exit", self.quit_app)
        ]
        
        for i, (text, command) in enumerate(buttons, start=1):
            btn = Button(self.sidebar, text=text, font=BUTTON_FONT, 
                        bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=FLAT,
                        activebackground=HEADER_COLOR, 
                        activeforeground=TEXT_COLOR,
                        command=command)
            btn.pack(fill=X, padx=10, pady=5, ipady=10)
            
        # Main content area
        self.content_area = Frame(self.main_container, bg=CANVAS_COLOR)
        self.content_area.pack(side=RIGHT, fill=BOTH, expand=True)
        
        # Welcome message
        self.welcome_label = Label(self.content_area, 
                                 text="Welcome to Hostel Management System",
                                 font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        self.welcome_label.pack(pady=50)
        
        # Dashboard widgets can be added here
        
    def add_student(self):
        # Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # Add student form
        self.student_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.student_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = Label(self.student_form, text="Add New Student", 
                     font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        title.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # Personal Info Frame
        personal_frame = LabelFrame(self.student_form, text="Personal Information", 
                                  font=LABEL_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        personal_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # First Name
        Label(personal_frame, text="First Name:", bg=CANVAS_COLOR).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.first_name_entry = Entry(personal_frame, font=ENTRY_FONT)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Last Name
        Label(personal_frame, text="Last Name:", bg=CANVAS_COLOR).grid(row=0, column=2, sticky=E, padx=5, pady=5)
        self.last_name_entry = Entry(personal_frame, font=ENTRY_FONT)
        self.last_name_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Father's Name
        Label(personal_frame, text="Father's Name:", bg=CANVAS_COLOR).grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.father_name_entry = Entry(personal_frame, font=ENTRY_FONT)
        self.father_name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Mother's Name
        Label(personal_frame, text="Mother's Name:", bg=CANVAS_COLOR).grid(row=1, column=2, sticky=E, padx=5, pady=5)
        self.mother_name_entry = Entry(personal_frame, font=ENTRY_FONT)
        self.mother_name_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # Contact Info Frame
        contact_frame = LabelFrame(self.student_form, text="Contact Information", 
                                 font=LABEL_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        contact_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Contact Number
        Label(contact_frame, text="Contact No:", bg=CANVAS_COLOR).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.contact_entry = Entry(contact_frame, font=ENTRY_FONT)
        self.contact_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Email
        Label(contact_frame, text="Email:", bg=CANVAS_COLOR).grid(row=0, column=2, sticky=E, padx=5, pady=5)
        self.email_entry = Entry(contact_frame, font=ENTRY_FONT)
        self.email_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Address
        Label(contact_frame, text="Address:", bg=CANVAS_COLOR).grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.address_entry = Entry(contact_frame, font=ENTRY_FONT)
        self.address_entry.grid(row=1, column=1, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Other Info Frame
        other_frame = LabelFrame(self.student_form, text="Other Information", 
                               font=LABEL_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        other_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # DOB
        Label(other_frame, text="Date of Birth:", bg=CANVAS_COLOR).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.dob_entry = Entry(other_frame, font=ENTRY_FONT)
        self.dob_entry.grid(row=0, column=1, padx=5, pady=5)
        Label(other_frame, text="(YYYY-MM-DD)", bg=CANVAS_COLOR, fg=WARNING_COLOR).grid(row=0, column=2, sticky=W, padx=5, pady=5)
        
        # Vehicle No
        Label(other_frame, text="Vehicle No:", bg=CANVAS_COLOR).grid(row=0, column=3, sticky=E, padx=5, pady=5)
        self.vehicle_entry = Entry(other_frame, font=ENTRY_FONT)
        self.vehicle_entry.grid(row=0, column=4, padx=5, pady=5)
        
        # Work Place/College
        Label(other_frame, text="Work/College:", bg=CANVAS_COLOR).grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.work_entry = Entry(other_frame, font=ENTRY_FONT)
        self.work_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Gender
        Label(other_frame, text="Gender:", bg=CANVAS_COLOR).grid(row=1, column=2, sticky=E, padx=5, pady=5)
        self.gender_var = StringVar(value="Male")
        Radiobutton(other_frame, text="Male", variable=self.gender_var, 
                   value="Male", bg=CANVAS_COLOR).grid(row=1, column=3, sticky=W, padx=5, pady=5)
        Radiobutton(other_frame, text="Female", variable=self.gender_var, 
                   value="Female", bg=CANVAS_COLOR).grid(row=1, column=4, sticky=W, padx=5, pady=5)
        Radiobutton(other_frame, text="Other", variable=self.gender_var, 
                   value="Other", bg=CANVAS_COLOR).grid(row=1, column=5, sticky=W, padx=5, pady=5)
        
        # Room Assignment Frame
        room_frame = LabelFrame(self.student_form, text="Room Assignment", 
                              font=LABEL_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        room_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        # Room No
        Label(room_frame, text="Room No:", bg=CANVAS_COLOR).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.room_entry = Entry(room_frame, font=ENTRY_FONT)
        self.room_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Bed No
        Label(room_frame, text="Bed No:", bg=CANVAS_COLOR).grid(row=0, column=2, sticky=E, padx=5, pady=5)
        self.bed_entry = Entry(room_frame, font=ENTRY_FONT)
        self.bed_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Buttons
        Button(self.student_form, text="Check Available Rooms", 
              font=BUTTON_FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR,
              command=self.check_available_rooms).grid(row=5, column=0, columnspan=2, pady=20)
        
        Button(self.student_form, text="Add Student", 
              font=BUTTON_FONT, bg=SUCCESS_COLOR, fg=TEXT_COLOR,
              command=self.save_student).grid(row=5, column=2, columnspan=2, pady=20)
        
    def check_available_rooms(self):
        # This would show available rooms based on gender
        messagebox.showinfo("Available Rooms", "Showing available rooms...")
        
    def save_student(self):
        # Validate and save student data
        messagebox.showinfo("Success", "Student added successfully!")
        
    def add_room(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # Add room form
        self.room_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.room_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = Label(self.room_form, text="Add New Room", 
                     font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        title.pack(pady=(0, 20))
        
        # Room details frame
        details_frame = Frame(self.room_form, bg=CANVAS_COLOR)
        details_frame.pack(pady=10)
        
        # Room No
        Label(details_frame, text="Room Number:", bg=CANVAS_COLOR).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.new_room_entry = Entry(details_frame, font=ENTRY_FONT)
        self.new_room_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Gender
        Label(details_frame, text="Gender Type:", bg=CANVAS_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.room_gender_var = StringVar(value="Male")
        Radiobutton(details_frame, text="Male", variable=self.room_gender_var, 
                   value="Male", bg=CANVAS_COLOR).grid(row=1, column=1, sticky=W)
        Radiobutton(details_frame, text="Female", variable=self.room_gender_var, 
                   value="Female", bg=CANVAS_COLOR).grid(row=1, column=2, sticky=W)
        Radiobutton(details_frame, text="Other", variable=self.room_gender_var, 
                   value="Other", bg=CANVAS_COLOR).grid(row=1, column=3, sticky=W)
        
        # Add button
        Button(self.room_form, text="Add Room", font=BUTTON_FONT, 
              bg=SUCCESS_COLOR, fg=TEXT_COLOR, command=self.save_room).pack(pady=20)
        
    def save_room(self):
        messagebox.showinfo("Success", "Room added successfully!")
        
    def in_out_time(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # In/Out time form
        self.io_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.io_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Notebook for tabs
        self.io_notebook = Notebook(self.io_form)
        self.io_notebook.pack(fill=BOTH, expand=True)
        
        # Outtime tab
        out_frame = Frame(self.io_notebook, bg=CANVAS_COLOR)
        self.io_notebook.add(out_frame, text="Out Time")
        
        # Outtime form
        Label(out_frame, text="Record Out Time", font=TITLE_FONT, 
             bg=CANVAS_COLOR, fg=BG_COLOR).pack(pady=(0, 20))
        
        form_frame = Frame(out_frame, bg=CANVAS_COLOR)
        form_frame.pack(pady=10)
        
        Label(form_frame, text="Student ID:", bg=CANVAS_COLOR).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.out_id_entry = Entry(form_frame, font=ENTRY_FONT)
        self.out_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Label(form_frame, text="Purpose:", bg=CANVAS_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.purpose_entry = Entry(form_frame, font=ENTRY_FONT)
        self.purpose_entry.grid(row=1, column=1, padx=5, pady=5)
        
        Button(out_frame, text="Record Out Time", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.record_out_time).pack(pady=20)
        
        # Intime tab
        in_frame = Frame(self.io_notebook, bg=CANVAS_COLOR)
        self.io_notebook.add(in_frame, text="In Time")
        
        # Intime form
        Label(in_frame, text="Record In Time", font=TITLE_FONT, 
             bg=CANVAS_COLOR, fg=BG_COLOR).pack(pady=(0, 20))
        
        form_frame = Frame(in_frame, bg=CANVAS_COLOR)
        form_frame.pack(pady=10)
        
        Label(form_frame, text="Student ID:", bg=CANVAS_COLOR).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.in_id_entry = Entry(form_frame, font=ENTRY_FONT)
        self.in_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Button(form_frame, text="Search Out Time", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, columnspan=2, pady=10)
        
        Label(form_frame, text="Out Time:", bg=CANVAS_COLOR).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.out_time_display = Entry(form_frame, font=ENTRY_FONT, state='readonly')
        self.out_time_display.grid(row=2, column=1, padx=5, pady=5)
        
        Label(form_frame, text="Remark:", bg=CANVAS_COLOR).grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.remark_var = StringVar()
        OptionMenu(form_frame, self.remark_var, "Before Time", "On Time", "Late").grid(row=3, column=1, padx=5, pady=5, sticky=EW)
        
        Button(in_frame, text="Record In Time", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR, command=self.record_in_time).pack(pady=20)
        
    def record_out_time(self):
        messagebox.showinfo("Success", "Out time recorded successfully!")
        
    def record_in_time(self):
        messagebox.showinfo("Success", "In time recorded successfully!")
        
    def visitor(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # Visitor form
        self.visitor_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.visitor_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = Label(self.visitor_form, text="Visitor Information", 
                     font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        title.pack(pady=(0, 20))
        
        # Visitor details frame
        details_frame = Frame(self.visitor_form, bg=CANVAS_COLOR)
        details_frame.pack(pady=10)
        
        # Visitor Name
        Label(details_frame, text="Visitor Name:", bg=CANVAS_COLOR).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.visitor_name_entry = Entry(details_frame, font=ENTRY_FONT)
        self.visitor_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Contact
        Label(details_frame, text="Contact No:", bg=CANVAS_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.visitor_contact_entry = Entry(details_frame, font=ENTRY_FONT)
        self.visitor_contact_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Reason
        Label(details_frame, text="Reason:", bg=CANVAS_COLOR).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.reason_entry = Entry(details_frame, font=ENTRY_FONT)
        self.reason_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Address
        Label(details_frame, text="Address:", bg=CANVAS_COLOR).grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.visitor_address_entry = Entry(details_frame, font=ENTRY_FONT)
        self.visitor_address_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Student Name
        Label(details_frame, text="Student Name:", bg=CANVAS_COLOR).grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.student_name_entry = Entry(details_frame, font=ENTRY_FONT)
        self.student_name_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Search button
        Button(details_frame, text="Search", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR).grid(row=4, column=2, padx=5, pady=5)
        
        # Room No display
        Label(details_frame, text="Room No:", bg=CANVAS_COLOR).grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.visitor_room_display = Entry(details_frame, font=ENTRY_FONT, state='readonly')
        self.visitor_room_display.grid(row=5, column=1, padx=5, pady=5)
        
        # Add button
        Button(self.visitor_form, text="Add Visitor", font=BUTTON_FONT, 
              bg=SUCCESS_COLOR, fg=TEXT_COLOR, command=self.add_visitor).pack(pady=20)
        
    def add_visitor(self):
        messagebox.showinfo("Success", "Visitor added successfully!")
        
    def view_info(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # View info form
        self.view_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.view_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = Label(self.view_form, text="View Information", 
                     font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        title.pack(pady=(0, 20))
        
        # Buttons
        Button(self.view_form, text="All Students", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR, width=20,
              command=self.view_all_students).pack(pady=10)
        
        Button(self.view_form, text="Room Wise", font=BUTTON_FONT, 
              bg=BUTTON_COLOR, fg=TEXT_COLOR, width=20,
              command=self.view_room_wise).pack(pady=10)
        
    def view_all_students(self):
        # This would show all students in a table
        messagebox.showinfo("All Students", "Showing all students...")
        
    def view_room_wise(self):
        # This would show students room-wise
        messagebox.showinfo("Room Wise", "Showing room-wise information...")
        
    def leave_application(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
            
        # Leave application form
        self.leave_form = Frame(self.content_area, bg=CANVAS_COLOR)
        self.leave_form.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = Label(self.leave_form, text="Leave Application", 
                     font=TITLE_FONT, bg=CANVAS_COLOR, fg=BG_COLOR)
        title.pack(pady=(0, 20))
        
        # Student details frame
        details_frame = Frame(self.leave_form, bg=CANVAS_COLOR)
        details_frame.pack(pady=10)
        
        # Hostel ID
        Label(details_frame, text="Hostel ID:", bg=CANVAS_COLOR).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.leave_id_entry = Entry(details_frame, font=ENTRY_FONT)
        self.leave_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Name
        Label(details_frame, text="Name:", bg=CANVAS_COLOR).grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.leave_name_entry = Entry(details_frame, font=ENTRY_FONT)
        self.leave_name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Room No
        Label(details_frame, text="Room No:", bg=CANVAS_COLOR).grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.leave_room_entry = Entry(details_frame, font=ENTRY_FONT)
        self.leave_room_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Mobile No
        Label(details_frame, text="Mobile No:", bg=CANVAS_COLOR).grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.leave_mobile_entry = Entry(details_frame, font=ENTRY_FONT)
        self.leave_mobile_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Reason
        Label(details_frame, text="Reason:", bg=CANVAS_COLOR).grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.leave_reason_entry = Entry(details_frame, font=ENTRY_FONT)
        self.leave_reason_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Return Date
        Label(details_frame, text="Return Date:", bg=CANVAS_COLOR).grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.return_date_entry = Entry(details_frame, font=ENTRY_FONT)
        self.return_date_entry.grid(row=5, column=1, padx=5, pady=5)
        Label(details_frame, text="(YYYY-MM-DD)", bg=CANVAS_COLOR, fg=WARNING_COLOR).grid(row=5, column=2, padx=5, pady=5, sticky=W)
        
        # Submit button
        Button(self.leave_form, text="Submit", font=BUTTON_FONT, 
              bg=SUCCESS_COLOR, fg=TEXT_COLOR, command=self.submit_leave).pack(pady=20)
        
    def submit_leave(self):
        messagebox.showinfo("Success", "Leave application submitted successfully!")
        
    def quit_app(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = HostelManagementSystem(root)
    root.mainloop()