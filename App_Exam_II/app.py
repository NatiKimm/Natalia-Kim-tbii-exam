import tkinter as tk
import openai #dowloading openAI for working with chat chatGBT
import os
from PIL import Image, ImageTk, ImageOps
from PIL.Image import Resampling
import deepl #dowloading deepL for word translation
import random 

#creating a GUI window with a title
root = tk.Tk()
root.geometry("850x700")
root.configure(bg = 'light blue')
root.title("RuGer")

DEEPL_KEY = ""  #INSERT DEEPL KEY HERE
GPT_KEY = ""    #INSERT GBT KEY HERE




#setting up an image background for the third page of application
def background_foto():
    img = Image.open("/Users/natikimm/PycharmProjects/pythonProject/tech1/App_Exam_II/images/background.png")
    img = img.resize((850, 700), Resampling.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(root, image=pic)
    Lab.place(x=0, y=0, relwidth=1, relheight=1)
    Lab.image = pic
    Lab.is_background = True 

#creating a dictinary with languages names and abbreviation(codes) for the deepl API
language_mapping = {
        "German": "DE",
        "English": "EN",
        "Spanish": "ES",
        "Russian": "RU",
        "Chinese": "ZH"
    }

#list of colours used in the app
COLORS = ["coral1", "cornsilk1", "darkolivegreen2", "darkseagreen", "darkslategray2", "lavenderblush2", "lavender", "lightpink"]


#list for saving entered words for translation
entered_words = []

#function to destroy all widgets
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()

#creating the first page of the app where the user selects the language he is learning, his native language and a topic of his choice 
def first_page():
    global selected_topic, selected_level, selected_level_topic_label
    clear_widgets(root)

    welcome_text = tk.Label(root, height=5, width=52,text="Hello 😊 Let's practise languages together 🥳",
                            bg='light pink', fg='black', font="georgia 25 bold")
    welcome_text.pack()

    #creating a label to select language which user want to practise. From this language the word will be translated.
    target_language_label=tk.Label(root, text="Select your target language: ", bd=3, fg="black", relief='flat', bg='light blue', font="georgia 20 bold")
    target_language_label.place(rely=0.21, relx=0.25, relwidth=0.5, 
                  relheight=0.1, anchor='n')
    
    #creating a label for the user to choose his level of his target language that he learns
    level_of_language = tk.Label(root, text="What is your level?", bd=3, relief='flat',fg='black', bg='light blue',font="georgia 20 bold")
    level_of_language.place(rely=0.31, relx=0.19, relwidth=0.5, relheight=0.1, anchor='n')
    
    #creating a label for the user to choose a topic in which sentences will be created with the word that the user writes
    topic_label = tk.Label(root, text="What topic would you like?", bd=3, relief='flat', fg='black', bg='light blue', font="georgia 20 bold")
    topic_label.place(rely=0.51, relx=0.23, relwidth=0.5, relheight=0.1, anchor='n')
    
    #creating a label to choose a native language. To this language the written word will be translated.
    native_language_label=tk.Label(root, text="Select your native language: ", bd=3, fg="black", relief='flat', bg='light blue', font="georgia 20 bold")
    native_language_label.place(rely=0.41, relx=0.245, relwidth=0.5, 
                  relheight=0.1, anchor='n')

    #creating a label which will show to the user what languages, level of a languages and topic the user have chosen.
    selected_level_topic_label = tk.Label(root, text= " ", bd=3, relief='flat', fg= 'black', bg='light blue', font="georgia 20 bold")
    selected_level_topic_label.place(rely=0.65, relx=0.2)
    
    # a button to go to the second page, the actual page of the app. 
    go_to_app = tk.Button(text='LETS GO 🚀', font='georgia 15 bold', fg='black', highlightbackground='light blue',
                          command=lambda: second_page(root))
    go_to_app.place(rely=0.79, relx=0.5, relwidth=0.2, relheight=0.1, anchor='n')

    option_topics()
    option_level()
    option_languages()


selected_level = " "


#function to handle the selection of a language level
def on_select1(event):
    global selected_level, selected_level_topic_label
    selected_level = var.get()
    update_level_label()
    print("Selected level:", selected_level)

#function to create a dropdown menu for selecting language levels.
def option_level():
    global var, selected_level_topic_label
    level = ["A1", "A2", "B1", "B2", "C1"]
    # Create a variable to hold the selected option
    var = tk.StringVar(root)
    var.set(level[0])  # Set the default option
    #Create the dropdown list
    dropdown = tk.OptionMenu(root, var, *level,command=on_select1)
    dropdown.place(rely=0.31, relx=0.75, anchor ='n')
    dropdown.config(width=15, height=3, bg='light blue', fg="black", font=('georgia', 15,), bd=0, relief="flat")


selected_topic = ""

#function to handle the selection of topic
def on_select(event):
    global selected_topic, selected_level_topic_label
    selected_topic = variable.get()
    update_level_label()
    print("Selected topic:", selected_topic)

#function to create a dropdown menu for selecting a topic
def option_topics():
    global variable, selected_level_topic_label
    topics = ["Medicine 💉", "Harry Potter 🧙🏻‍♂️ ", "Travelling 🌏 ", "Food 🍕 ", "Biology 🧬 ", "Politics 🧐 "]
    variable = tk.StringVar(root)
    variable.set(topics[0])  
    dropdown = tk.OptionMenu(root, variable, *topics, command=on_select)
    dropdown.place(rely = 0.51, relx = 0.75, anchor ='n')
    dropdown.config(width=15, height=3, bg='light blue', fg = "black", font=('georgia', 17,), bd=0, relief="flat")


selected_language_source = ""
selected_language_target = ""

#function to handle the selection of a language that the user want to practise
def on_select_language_source(event):
    global selected_language_source
    selected_language_source = language_mapping[var_source.get()]
    update_level_label()
    print("Selected language source:", selected_language_source)

#function to handle the selection of a native language a language into which the user want his words to be translated to
def on_select_language_target(event):
    global selected_language_target
    selected_language_target = language_mapping[var_target.get()]
    update_level_label()
    print("Selected language target:", selected_language_target)
    #statement which transform EN to EN-GB (brittish) for the DeepL
    if selected_language_target == "EN":
       selected_language_target = "EN-GB"

#function to create a dropdown menu for languages
def option_languages():
    global var_source, var_target, selected_language_source, selected_language_target

    languages = list(language_mapping.keys())

    var_source = tk.StringVar(root)
    var_source.set(languages[0])  # Set the default option

    var_target=tk.StringVar(root)
    var_target.set(languages[1])

    dropdown_source = tk.OptionMenu(root, var_source, *languages,command=on_select_language_source)
    dropdown_source.place(rely=0.21, relx=0.75, anchor ='n')
    dropdown_source.config(width=15, height=3, bg='light blue', fg="black", font=('georgia', 16,), borderwidth=5, relief="flat")

    dropdown_target = tk.OptionMenu(root, var_target, *languages,command=on_select_language_target)
    dropdown_target.place(rely=0.41, relx=0.75, anchor ='n')
    dropdown_target.config(width=15, height=3, bg='light blue', fg="black", font=('georgia', 16,), borderwidth=5, relief="flat")

#function which will update the selected_level_topic_label
def update_level_label():
    global selected_level_topic_label, selected_level, selected_topic, selected_language_target, selected_language_source
    selected_level_topic_label.config(text="You have selected: " + selected_level + " - " + selected_topic + " - " + selected_language_source + " - " + selected_language_target)

first_page()

#creating the second page where the user can translate the word, have an example with this word and save words in a list on his computer
def second_page(root):
    global word_entry, translated_word, listbox, example_box, level_label
    word_name = tk.StringVar()
    clear_widgets(root)

    # entry widget for entering a word user wants to translate
    word_entry = tk.Entry(root, textvar=word_name, fg='black', bg=random.choice(COLORS), font='georgia 25 bold')
    word_entry.place(rely=0.03, relx=0.2, relwidth=0.35, relheight=0.1, anchor='n')

    # a button widget for translatin the entered word by calling the tranlsate function
    translate_button = tk.Button(text='Translate me', font='georgia 15 bold', fg='black',highlightbackground='light blue', command=translate)
    translate_button.place(rely=0.04, relx=0.5, relwidth=0.2, relheight=0.07, anchor='n')

    # a label displaying the translated word
    translated_word = tk.Label(root, text=" ", bd=3, relief='solid', fg='black', bg='white', font="georgia 25 bold")
    translated_word.place(rely=0.03, relx=0.8, relwidth=0.35, relheight=0.1, anchor='n')

    # a save button to save all the entered words to the text file by calling the save_word_to_file funtion
    save = tk.Button(text='Save me', font='georgia 15 bold', fg='black', highlightbackground='light blue', command=save_word_to_file)
    save.place(rely=0.77, relx=0.5, relwidth=0.2, relheight=0.07, anchor='n')

    # example button that triggers the generate example_function
    example = tk.Button(text='Example', font='georgia 15 bold', fg='black', highlightbackground='light blue',
                        command=generate_example)
    example.place(rely=0.17, relx=0.5, relwidth=0.2, relheight=0.07, anchor='n')
    # label to display the chatGPT response for the sentence example
    example_box = tk.Label(root, text=" ", bd=3, relief='solid', fg='black', bg='white', font="georgia 20 bold ", wraplength=700)
    example_box.place(rely=0.3, relx=0.5, relwidth=0.9, relheight=0.45, anchor='n')
    
    #button which will lead to the first page
    first_page_button = tk.Button (text= "🏠", font='georgia 15 bold', fg='light blue', highlightbackground='light blue', command=first_page)
    first_page_button.place(rely=0.89, relx=0.5, relwidth=0.2, relheight=0.07, anchor='n')
    
    #button which will lead to the last page
    third_page_button = tk.Button(text="❌", command=lambda: third_page(root))
    third_page_button.place(rely=0.92, relx=0.95, relheight=0.07, anchor='n')

    # a listbox widget to display all entered words
    listbox = tk.Listbox(root, height = 15,
                  width = 30,
                  bg = 'lavenderblush2',
                  relief="solid",
                  activestyle = 'dotbox',
                  font = "georgia 15 bold",
                  fg = "black")
    listbox.insert(1, entered_words)
    listbox.place(rely = 0.89, relx = 0.31, relwidth=0.35, relheight=0.38, anchor ='se')
    
    listbox.place_forget()

    #listbox button to show or hide the listbox
    toggle_listbox_button = tk.Button(text="Words list🖊", font='georgia 15 bold', fg='black', highlightbackground='light blue', command=toggle_listbox_visibility)
    toggle_listbox_button.place(rely=0.92, relx=0.2, relwidth=0.2, relheight=0.05, anchor='ne')


# definition for updating the listbox
def update_listbox():
    listbox.delete(0, tk.END)  # Clear the listbox
    for word_name, translated_text in entered_words:
        listbox.insert(tk.END, f"{word_name} - {translated_text}")

# definition to show or hide the listbox
def toggle_listbox_visibility():
    if listbox.winfo_viewable():
        listbox.place_forget()
    else:
        listbox.place(rely=0.91, relx=0.31, relwidth=0.3, relheight=0.4, anchor='se')


def translate():
    word_name = word_entry.get()
    translator = deepl.Translator(DEEPL_KEY)
    result = translator.translate_text(word_name, formality='prefer_more', source_lang=selected_language_source,  target_lang=selected_language_target) #taking the word from the word_entry (word_name) and  translating from chosen language to the native language
    translated_text = result.text #assigning the translated text to the variable translated_text.
    display_translation(translated_text) #calling the display_translation function to pass the translated text as an argument.
    # This function updates the translated_word label with the translated text. See below
    entered_words.append((word_name, translated_text))
    # This list is used to keep track of words and their translations that the user has entered.
    update_listbox()# calling the update_listbox function, which updates the listbox widget with the latest entered words and translations.
    translated_word.configure(bg = random.choice(COLORS)) #This line changes the background color (bg) of the translated_word label to a randomly chosen color
    # from the COLORS list.

def display_translation(text): # function for updating the translated_word label with the word that the user wants to translate
    translated_word.config(text=text)

def save_word_to_file(): # This function saves the entered words and their translations to a file named "filename.txt".
        with open("filename.txt", "a") as file: #opening a text file in the append mode so all enetered words will be safed in a list and each time new word will be
            #appended to the existed list
            for word_name, translated_text in entered_words:
                file.write(f"{word_name} - {translated_text}\n")
                print("Words saved to the file successfully.")
                #listbox.configure(bg = random.choice(COLORS))

openai.api_key = GPT_KEY 

# This function is responsible for sending a prompt to the OpenAI and returning the generated response
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    print(prompt)
    return response.choices[0].message["content"]

#list containing promts for the openAI to achieve variety in the chatGPT responses.

prompts = [
    "Write one sentence in this language {} with the word {} in a level {} ! Make sure it is the level I asked you, try to use words suitable for this {} level! And write the sentence in the topic of {}. Make the sentence fun! Use the given word in the middle of a sentence. Show translation into this language {} afterwards.  Show the translation in braces like this (). Do not write anything else."
    "Give me one sentence in this language {} with the word {} in a level {} ! Make sure it is the level I asked you, try to use words suitable for this {} level! And do it in the topic of {}.Make the sentence interesting and useful for German learners! Try write a sentence as local would say.Show translation into this language {} afterwards.  Show the translation in braces like this (). Do not write anything else",
    "Create one sentence in this language {} with the word {} in a level {} ! Make sure it is the level I asked you, try to use words suitable for this {} level! And do it in the topic of {}. Make the sentence short but meaningful! Show translation into this language {} afterwards.  Show the translation in braces like this (). Do not write anything else",
    "Give me one sentence in this language {} with the word {} in a level {}! Make sure it is the level I asked you, try to use words suitable for this {} level! And do it in the topic of {}. Make the sentence not too long and try to use adjectives in the sentence! Show translation into into this language {}afterwards .  Show the translation in braces like this ().  Do not write anything else",
    "Write one interesting sentence in this language {} with the word {} in a level {} ! Make sure it is the level I asked you, try to use words suitable for this {} level! And do it in the topic of {}.Make the sentence not too long, try to use verbs in it! Show translation into into this language {} afterwards.  Show the translation in braces like this ().Do not write anything else",
    "Create one sentence in this kanguage {} with the word {} in a level {} ! Make sure it is the level I asked you, try to use words suitable for this {} level! And do it in the topic of {}.Make the sentence short but nice and unique, try to create a sentence which will be useful for learners in their everyday life! Show translation into into this language {} afterwards.  Do not write anything else",
    "Write one sentence in this language {} with the word {} in level {} ! Make sure it is the level I asked you for, and try to use words suitable for this {} level!  And write this sentence in the topic of {}. Use your creativity to create a nice kind sentence! Show translation into this language {} afterwards. Show the translation in braces like this ().  Do not write anything else."


]

# empty list is defined to keep track of the indices of prompts that haven't been used yet.
prompt_indices = []

# this function populates the prompt_indices list with the indices of prompts from the prompts list above. It's called in the
# beginning to fill up the promt_indices list
def setup():
    for i in range(len(prompts)):
        prompt_indices.append(i)

# function that is responsible for generating an example with the entered  word
def generate_example():
    global prompts, prompt_indices
    word_name = word_entry.get().upper()  #retrieve the content entered in the word entry and save it in the variable word_name

    if not prompt_indices:  # this line checks if the promt_indices list is empty, and if it is, it calls the setup function to reset the list
        setup()
    random_index = random.choice(prompt_indices)  # choosing a random index in the list prompt_indices
    prompt = prompts[
        random_index]  # choosing the prompt for  chatgpt from prompt_list using the randomly selected index
    print(prompts[random_index])

    prompt_indices.remove(
        random_index)  # remove the selected index from the list to ensure it will not be selected again

    if not prompt_indices:
        prompt_indices.extend(range(
            len(prompts)))  # checks if the promt_indices is empty again and if it is empty it reinitialize the list

    prompt_with_word = prompt.format(selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic, selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level,selected_level, selected_topic,selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level, selected_level,selected_topic,selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic,selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic,selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic,selected_language_target,
                                     selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic, selected_language_target
    )
    
    #statement that makes sure that when the chinese is selected, user will get a transription of a sentence in simplified chinese
    if selected_language_source == "ZH" or selected_language_target == "ZH":
        chinese_promts = ["Write one simple sentence in this language {} with the word {} in a level {}! Make sure it is a simple sentence, try to use words suitable for this {} level! And write the sentence in the topic of {}. Write the sentence in simplified Chinese (not traditional, use simplified chinese characters! Show the transcription of Chinese language in Pinyin after you write a chinese sentence. Show translation into this language {} afterwards. Do not write anything else.",
                         "Write one short beatiful sentence in this language {} with the word {} in a level {}! Make sure it is a simple sentence, try to use words suitable for this {} level! And write the sentence in the topic of {}. Write the sentence in simplified Chinese (not traditional, use simplified chinese characters! Show the transcription of Chinese language in Pinyin after you write a chinese sentence. Show translation into this language {} afterwards. Do not write anything else.",
                         "Write one sentence using adjectives in this language {} with the word {} in a level {}! Make sure it is a simple sentence, try to use words suitable for this {} level! And write the sentence in the topic of {}. Write the sentence in simplified Chinese (not traditional, use simplified chinese characters! Show the transcription of Chinese language in Pinyin after you write a chinese sentence. Show translation into this language {} afterwards. Do not write anything else."
]

        prompt = random.choice(chinese_promts)
        prompt_with_word = prompt.format(selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic, selected_language_target,
                                         selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic, selected_language_target,
                                         selected_language_source, word_name.upper(), selected_level, selected_level, selected_topic, selected_language_target)

    response = get_completion(prompt_with_word)  #send the formatted prompt to get_completion function to get a responce from the chatGPT API
    
    example_box.config(text=response) #updating the text content with a response from chatGPT in the example_box widget
    print(response) #shows the created sentence!!!
    bg_color = random.choice(COLORS) #choosing a random colour for the background
    example_box.configure( bg = bg_color, fg = 'black') #updating the background and foreground colour of the example_box widget


def third_page(root):
    clear_widgets(root)
    background_foto()

root.mainloop()

