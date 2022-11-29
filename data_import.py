import os
import requests
from thoughtspot_tml import *
from thoughtspot import *
import re
import config

# Creating path for directory
working_dir = os.getcwd()
os.chdir('../src')  # changing current working directory to src
working_dir = os.getcwd()

# Sign-in to ThoughtSpot Server to use REST API
username = os.getenv('username')
password = os.getenv('password')
server = os.getenv('server')
ts: TSRestApiV1 = TSRestApiV1(server_url=config.server)  # referencing TSRestApiV1 class
try:
    ts.session_login(username=config.username, password=config.password)  # calling the session_login method from TSRESTApiV1 class
except requests.exceptions.HTTPError as e:
    print(e)
    print(e.response.content)

typ1 = "ONE_TO_ONE_LOGICAL"
typ2 = "WORKSHEET"
typ3 = "PINBOARD_ANSWER_BOOK"
typ4 = "QUESTION_ANSWER_BOOK"


def tags_tables():
    userques = input("Is there a tag name for tables: Y or N  \n")
    if (userques == "Y") or (userques == "y"):
        nametag = input("Please enter the tag name for tables: \n")
    if (userques == "N") or (userques == "n"):
        nametag = ""
    return(ts.metadata_listobjectheaders(object_type='LOGICAL_TABLE', subtypes=[typ1], tagname=[nametag]))  # declaring the object type

def tags_worksheets():
    userques = input("Is there a tag name for worksheets: Y or N  \n")
    if (userques == "Y") or (userques == "y"):
        nametag = input("Please enter the tag name for worksheets: \n")
    if (userques == "N") or (userques == "n"):
        nametag = ""
    return(ts.metadata_listobjectheaders(object_type='LOGICAL_TABLE', subtypes=[typ2], tagname=[nametag]))

def tags_liveboards():
    userques = input("Is there a tag name for liveboards: Y or N  \n")
    if (userques == "Y") or (userques == "y"):
        nametag = input("Please enter the tag name for liveboards: \n")
    if (userques == "N") or (userques == "n"):
        nametag = ""
    return(ts.metadata_listobjectheaders(object_type=typ3, tagname=[nametag]))  # declaring the object type

def tags_answers():
    userques = input("Is there a tag name for answers: Y or N  \n")
    if (userques == "Y") or (userques == "y"):
        nametag = input("Please enter the tag name for answers: \n")
    if (userques == "N") or (userques == "n"):
        nametag = ""
    return(ts.metadata_listobjectheaders(object_type=typ4))

def create_directory_tables():
    sub_dir1 = working_dir + "/tables"
    if not os.path.exists(sub_dir1):

        os.makedirs(sub_dir1)
    return(sub_dir1)

def create_directory_worksheets():

    sub_dir2 = working_dir + "/worksheets"
    if not os.path.exists(sub_dir2):
        os.makedirs(sub_dir2)
    return(sub_dir2)

def create_directory_liveboards():
    sub_dir3 = working_dir + "/liveboards"
    if not os.path.exists(sub_dir3):
        os.makedirs(sub_dir3)
    return(sub_dir3)

def create_directory_answers():
    sub_dir4 = working_dir + "/answers"
    if not os.path.exists(sub_dir4):
        os.makedirs(sub_dir4)
    return(sub_dir4)


def output_function(x):
    newFilePath = os.path.join(working_dir, x, file_path)
    with open(newFilePath, 'w') as new_file:
        new_file.write(str(modified_tml_string))

value = []
value = list(re.split(',| ', input("Please select an object or multiple objects: \nTables Enter 1\nWorksheets Enter 2\nLiveboards Enter 3\nAnswers Enter 4\n")))
for i in range(len(value)):
    if (value[i] == '1') or (value[i] == '2') or (value[i] == '3') or (value[i] == '4'):
        if value[i] == '1':
            sub_dir1 = create_directory_tables()
            output = tags_tables()

        if value[i] == '2':
            sub_dir2 = create_directory_worksheets()
            output = tags_worksheets()

        if value[i] == '3':
            sub_dir3 = create_directory_liveboards()
            output = tags_liveboards()

        if value[i] == '4':
            sub_dir4 = create_directory_answers()
            output = tags_answers()
            print("Running....")

        for x in output:
            try:
                file_path = x['name'] + '.tml'
                tml_yaml_str = ts.metadata_tml_export_string(guid=x['id'], formattype='YAML', export_associated=False)
                tml_yaml_ordereddict = YAMLTML.load_string(tml_yaml_str)
                tml_obj = Worksheet(tml_yaml_ordereddict)
                modified_tml_string = YAMLTML.dump_tml_object(tml_obj)
                if value[i] == '1':
                    output_function(sub_dir1)
                if value[i] == '2':
                    output_function(sub_dir2)
                if value[i] == '3':
                    output_function(sub_dir3)
                if value[i] == '4':
                    output_function(sub_dir4)
            except:
                print("Failed to export : " + file_path)
    else:
        print("Enter correct input")





