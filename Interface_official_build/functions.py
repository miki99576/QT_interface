import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg
import shutil


def table(header,file_name):
   rows = []
   with open(file_name, encoding="utf8") as f:
      csv_reader = csv.DictReader(f,delimiter=",")
      for line in csv_reader:
         rows.append([line[header[0]],line[header[1]]])

   return rows


def display_csv(parent_directory,searched_folder):
    folder_list=[]
    full_path=os.path.join(parent_directory,searched_folder)
    if os.path.exists(full_path):
        for csv in os.listdir(full_path):
            if (csv.endswith(".csv")):
                return os.path.join(parent_directory,searched_folder,csv)

def display_image(parent_directory,searched_folder,searched_image):
    folder_list=[]
    full_path=os.path.join(parent_directory,searched_folder)
    if os.path.exists(full_path):
        for images in os.listdir(full_path):
            if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
                if searched_image in images:
                    return os.path.join(parent_directory,searched_folder,images)
                    #return os.path.join(parent_directory,searched_folder,images)
                #return os.path.join(parent_directory,searched_folder,images)
   

def show_graph(path_csv_file,col1,col2,title_graph,parent_directory,parent_folder):
    x = []
    y = []
    figure_name = title_graph +"_figure.png"
    with open(path_csv_file, encoding="utf8") as f:
        csv_reader = csv.DictReader(f,delimiter=",")
        for line in csv_reader:
            x.append(line[col1])
            y.append(int(line[col2]))
    plt.figure(figsize=(10,6))
    plt.plot(x, y)
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
  
    # giving a title to my graph
    plt.title(title_graph)
    full_path = os.path.join(parent_directory,parent_folder,figure_name)
    # function to show the plot
    plt.savefig(full_path)
    #plt.show()

#append new line to a csv file
def append_csv(file_name,col1,col2):
    with open(file_name, 'a', newline='') as file:
          writer = csv.writer(file,delimiter=",")
          writer.writerow([col1,col2])


#reads a csv file and updates the values of a specific window
def read_csv(file_name,col_name):
    file_list = []
    with open(file_name, encoding="utf8") as f:
        csv_reader = csv.DictReader(f,delimiter=',')
        for line in csv_reader:
            file_list.append(line[col_name])

        for i in file_list:    
            #window[key].update(file_list)
            return file_list
            #print(line[col_name])
# First the window layout in 2 columns

def getlines(file_name):
    with open(file_name, encoding="utf8") as f:
        results = pd.read_csv(f)
        return len(results)



# takes a dictionary as input searches for a value who's key is equal to index_val and gets the value of the other key
def search(file_name,main_col_name,index_val,alt_col_name): 
    with open(file_name, encoding="utf8") as f:
        csv_reader = csv.DictReader(f,delimiter=',')
        for line in csv_reader:
            if line[main_col_name] == index_val:
                return line[alt_col_name]




def create_student(folder_name,folder_path,col1,col2,col3,col4,image_origine):
    file_name = folder_name +'.csv'
    folder_directory = os.path.join(folder_path,folder_name)
    if os.path.exists(folder_directory):
        print("folder already exists")
        return
        
    else:   
        os.makedirs(folder_directory)

    file = os.path.join(folder_directory,file_name)
    with open(file, 'a', newline='') as file:
          writer = csv.writer(file,delimiter=",")
          writer.writerow([col1,col2,col3])
          print("Students addes")
    shutil.copy(image_origine,folder_directory)
    print("image inserted successfully")


def generate_buttons(question,state):
    true_key = "-TRUE"+question+"-"
    false_key = "-FALSE"+question+"-"
    row = [[sg.Text(question,key=question,visible=state),sg.Button("True",key=true_key,visible=state),sg.Button("False",key=false_key,visible=state)]]
    return [question,true_key,false_key,row]    