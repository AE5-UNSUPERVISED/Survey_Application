#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd

# Function to save survey data to the Excel file
def save_survey_data():
    # Get the values from the input fields
    surname = surname_entry.get()
    first_names = first_names_entry.get()
    contact_number = contact_number_entry.get()
    date = date_picker.get()
    age = age_entry.get()
    favourite_food = ", ".join(food_choices.get(0, tk.END))
    like_eat_out = rating_eat_out.get()  # Fixed variable name
    like_watch_movies = rating_watch_movies.get()
    like_watch_tv = rating_watch_tv.get()
    like_listen_radio = rating_listen_radio.get()

    # Validate the input fields
    if not surname or not first_names or not contact_number or not date or not age:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return

    if not age.isdigit() or int(age) < 5 or int(age) > 120:
        messagebox.showerror("Error", "Invalid age. Age must be a number between 5 and 120.")
        return

    if like_eat_out == 0 or like_watch_movies == 0 or like_watch_tv == 0 or like_listen_radio == 0:
        messagebox.showerror("Error", "Please select a rating for all the questions.")
        return

    if len(contact_number) > 10:
        messagebox.showerror("Error", "Contact number must not exceed 10 digits.")
        return

    # Prepare the data for saving
    data = {
        'Surname': [surname],
        'First Names': [first_names],
        'Contact Number': [contact_number],
        'Date': [date],
        'Age': [age],
        'Favourite Food': [favourite_food],
        'Like Eat Out': [like_eat_out],
        'Like Watch Movies': [like_watch_movies],
        'Like Watch TV': [like_watch_tv],
        'Like Listen to Radio': [like_listen_radio]
    }

    df = pd.DataFrame(data)

    # Check if the file exists
    try:
        existing_data = pd.read_excel("survey_data.xlsx")
        df = pd.concat([existing_data, df])
    except FileNotFoundError:
        pass

    # Save the data to Excel
    df.to_excel("survey_data.xlsx", index=False)

    # Clear the input fields
    surname_entry.delete(0, tk.END)
    first_names_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    food_choices.selection_clear(0, tk.END)
    rating_eat_out.set(0)
    rating_watch_movies.set(0)
    rating_watch_tv.set(0)
    rating_listen_radio.set(0)

    # Show a success message
    messagebox.showinfo("Success", "Survey data saved successfully.")

    # Return to the main menu
    show_main_menu()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd

# ...

# Function to calculate and display the survey results
def show_survey_results():
    try:
        df = pd.read_excel("survey_data.xlsx")

        total_surveys = len(df)
        average_age = df['Age'].mean()
        max_age = df['Age'].max()
        min_age = df['Age'].min()
        pizza_count = df[df['Favourite Food'].str.contains('Pizza', case=False)]['Favourite Food'].count()
        pizza_percentage = (pizza_count / total_surveys) * 100
        avg_rating_eat_out = df['Like Eat Out'].mean()
        avg_rating_watch_movies = df['Like Watch Movies'].mean()
        avg_rating_watch_tv = df['Like Watch TV'].mean()
        avg_rating_listen_radio = df['Like Listen to Radio'].mean()

        results_text = f"Total Surveys: {total_surveys}\n\n"
        results_text += f"Average Age: {average_age:.2f}\n"
        results_text += f"Oldest Participant Age: {max_age}\n"
        results_text += f"Youngest Participant Age: {min_age}\n\n"
        results_text += f"Pizza as Favourite Food: {pizza_percentage:.2f}%\n\n"
        results_text += f"Average Rating for 'Like Eat Out': {avg_rating_eat_out:.2f}\n"
        results_text += f"Average Rating for 'Like Watch Movies': {avg_rating_watch_movies:.2f}\n"
        results_text += f"Average Rating for 'Like Watch TV': {avg_rating_watch_tv:.2f}\n"
        results_text += f"Average Rating for 'Like Listen to Radio': {avg_rating_listen_radio:.2f}"

        # Create a text widget to display the results
        results_text_widget = tk.Text(results_frame, height=10, width=40)
        results_text_widget.insert(tk.END, results_text)
        results_text_widget.pack(pady=10)

        # Create a button to close the results screen
        close_button = ttk.Button(results_frame, text="OK", command=close_results_screen)
        close_button.pack(pady=10)

        # Show the results screen
        results_frame.pack(fill=tk.BOTH, expand=True)
    except FileNotFoundError:
        messagebox.showinfo("Survey Results", "No survey data found.")

# ...

# Function to show the survey screen
def show_survey_screen():
    main_menu_frame.pack_forget()
    results_frame.pack_forget()
    survey_frame.pack(fill=tk.BOTH, expand=True)

# Function to show the results screen
def show_results_screen():
    main_menu_frame.pack_forget()
    survey_frame.pack_forget()
    show_survey_results()
    results_frame.pack(fill=tk.BOTH, expand=True)

# Function to show the main menu screen
def show_main_menu():
    survey_frame.pack_forget()
    results_frame.pack_forget()
    main_menu_frame.pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Survey Application")

# Set the window size and position
window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create frames for each screen
main_menu_frame = tk.Frame(root)
survey_frame = tk.Frame(root)
results_frame = tk.Frame(root)

# Configure the main menu screen
fill_survey_button = ttk.Button(main_menu_frame, text="Fill Out Survey", command=show_survey_screen, style='Blue.TButton')
fill_survey_button.pack(pady=10)

view_results_button = ttk.Button(main_menu_frame, text="View Survey Results", command=show_results_screen, style='Blue.TButton')
view_results_button.pack(pady=10)


# Define custom style for blue buttons
root.style = ttk.Style()
root.style.configure('Blue.TButton', background='blue')


# Function to submit survey data
def submit_survey_data():
    # Get the values from the input fields
    surname = surname_entry.get()
    first_names = first_names_entry.get()
    contact_number = contact_number_entry.get()
    date = date_picker.get()
    age = age_entry.get()
    favourite_food = ", ".join(food_choices.get(0, tk.END))
    like_eat_out = rating_eat_out.get()
    like_watch_movies = rating_watch_movies.get()
    like_watch_tv = rating_watch_tv.get()
    like_listen_radio = rating_listen_radio.get()

    # Validate the input fields
    if not surname or not first_names or not contact_number or not date or not age:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return

    if not age.isdigit() or int(age) < 5 or int(age) > 120:
        messagebox.showerror("Error", "Invalid age. Age must be a number between 5 and 120.")
        return

    if like_eat_out == 0 or like_watch_movies == 0 or like_watch_tv == 0 or like_listen_radio == 0:
        messagebox.showerror("Error", "Please select a rating for all the questions.")
        return

    # Prepare the data for saving
    data = {
        'Surname': [surname],
        'First Names': [first_names],
        'Contact Number': [contact_number],
        'Date': [date],
        'Age': [age],
        'Favourite Food': [favourite_food],
        'Like Eat Out': [like_eat_out],
        'Like Watch Movies': [like_watch_movies],
        'Like Watch TV': [like_watch_tv],
        'Like Listen to Radio': [like_listen_radio]
    }

    df = pd.DataFrame(data)

    # Check if the file exists
    try:
        existing_data = pd.read_excel("survey_data.xlsx")
        df = pd.concat([existing_data, df])
    except FileNotFoundError:
        pass

    # Save the data to Excel
    df.to_excel("survey_data.xlsx", index=False)

    # Clear the input fields
    surname_entry.delete(0, tk.END)
    first_names_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    food_choices.selection_clear(0, tk.END)
    rating_eat_out.set(0)
    rating_watch_movies.set(0)
    rating_watch_tv.set(0)
    rating_listen_radio.set(0)

    # Show a success message
    messagebox.showinfo("Success", "Survey data saved successfully.")

    # Return to the main menu
    show_main_menu()

# Function to show the survey screen
def show_survey_screen():
    main_menu_frame.pack_forget()
    results_frame.pack_forget()
    survey_frame.pack(fill=tk.BOTH, expand=True)

    # Clear the input fields
    surname_entry.delete(0, tk.END)
    first_names_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    food_choices.selection_clear(0, tk.END)
    rating_eat_out.set(0)
    rating_watch_movies.set(0)
    rating_watch_tv.set(0)
    rating_listen_radio.set(0)

# Configure the survey screen
surname_label = ttk.Label(survey_frame, text="Surname:")
surname_label.grid(row=0, column=0, sticky="w")
surname_entry = ttk.Entry(survey_frame)
surname_entry.grid(row=0, column=1)

first_names_label = ttk.Label(survey_frame, text="First Names:")
first_names_label.grid(row=1, column=0, sticky="w")
first_names_entry = ttk.Entry(survey_frame)
first_names_entry.grid(row=1, column=1)

contact_number_label = ttk.Label(survey_frame, text="Contact Number:")
contact_number_label.grid(row=2, column=0, sticky="w")
contact_number_entry = ttk.Entry(survey_frame)
contact_number_entry.grid(row=2, column=1)

date_label = ttk.Label(survey_frame, text="Date:")
date_label.grid(row=3, column=0, sticky="w")
date_picker = DateEntry(survey_frame)
date_picker.grid(row=3, column=1)

age_label = ttk.Label(survey_frame, text="Age:")
age_label.grid(row=4, column=0, sticky="w")
age_entry = ttk.Entry(survey_frame)
age_entry.grid(row=4, column=1)

food_label = ttk.Label(survey_frame, text="What is your favourite food?")
food_label.grid(row=5, column=0, sticky="w")

food_choices = tk.Listbox(survey_frame, selectmode=tk.MULTIPLE)
food_choices.insert(tk.END, "Pizza")
food_choices.insert(tk.END, "Pasta")
food_choices.insert(tk.END, "Pap and Wors")
food_choices.insert(tk.END, "Chicken stir fry")
food_choices.insert(tk.END, "Beef stir fry")
food_choices.insert(tk.END, "Other")
food_choices.grid(row=5, column=1)

# Configure the survey screen
# ...

rating_label = ttk.Label(survey_frame, text="On a scale of 1 to 5, indicate your response:")
rating_label.grid(row=6, column=0, columnspan=2)

rating_eat_out = tk.IntVar()
rating_watch_movies = tk.IntVar()
rating_watch_tv = tk.IntVar()
rating_listen_radio = tk.IntVar()

questions = {
    "I like to eat out": rating_eat_out,
    "I like to watch movies": rating_watch_movies,
    "I like to watch TV": rating_watch_tv,
    "I like to listen to the radio": rating_listen_radio
}

# Create the rating options with corresponding values
rating_options = {
    "Strongly Agree (1)": 1,
    "Agree (2)": 2,
    "Neutral (3)": 3,
    "Disagree (4)": 4,
    "Strongly Disagree (5)": 5
}

rating_frames = {}

# Create the rating questions with radio buttons
row_num = 7
for question, rating_var in questions.items():
    rating_frame = ttk.Frame(survey_frame)
    rating_frame.grid(row=row_num, column=0, columnspan=2, pady=5)
    rating_label = ttk.Label(rating_frame, text=question)
    rating_label.pack(side=tk.LEFT)
    
    # Create radio buttons for each rating option
    for option, value in rating_options.items():
        ttk.Radiobutton(rating_frame, text=option, variable=rating_var, value=value).pack(side=tk.LEFT)
    
    rating_frames[question] = rating_frame
    row_num += 1

submit_button = ttk.Button(survey_frame, text="Submit", command=submit_survey_data)
submit_button.grid(row=row_num, column=0, columnspan=2, pady=10)


# Function to show the results screen
def show_results_screen():
    main_menu_frame.pack_forget()
    survey_frame.pack_forget()
    results_frame.pack(fill=tk.BOTH, expand=True)
    show_survey_results()

    # Create the OK button
    ok_button = ttk.Button(results_frame, text="OK", command=show_main_menu)
    ok_button.pack(pady=10)

# Function to show the survey screen
def show_survey_screen():
    main_menu_frame.pack_forget()
    results_frame.pack_forget()
    survey_frame.pack(fill=tk.BOTH, expand=True)

    # Clear the input fields
    surname_entry.delete(0, tk.END)
    first_names_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    food_choices.selection_clear(0, tk.END)
    rating_eat_out.set(0)
    rating_watch_movies.set(0)
    rating_watch_tv.set(0)
    rating_listen_radio.set(0)

# Configure the survey screen
# Function to show the results screen
def show_results_screen():
    main_menu_frame.pack_forget()
    survey_frame.pack_forget()
    show_survey_results()
    
def close_results_screen():
    results_frame.pack_forget()
    show_main_menu()
    
close_button = ttk.Button(results_frame, text="OK", command=show_main_menu)


# Show the main menu screen initially
show_main_menu()



# Start the main event loop
root.mainloop()


# In[ ]:





# In[ ]:




