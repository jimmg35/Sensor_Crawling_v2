from src.Parser import Parser
import os 
from os import listdir
from colorama import init, Fore, Back, Style
init(convert=True)

DATA_PATH = r"data"
OUTPUT_PATH = r"complete"

if __name__ == "__main__":
    # get input data path
    project_name = []
    project_month = []
    for i in listdir(DATA_PATH):
        for j in listdir(os.path.join(DATA_PATH, i)):
            project_name.append(i)
            project_month.append(j)
    
    my_parser = Parser()

    print(project_name)
    print(project_month)
    for project, month in zip(project_name, project_month):
        project_data_path = os.path.join(DATA_PATH, project, month)
        project_output_path = os.path.join(OUTPUT_PATH, month, project)
        output_file_name = project + '_' + month
        check_file_name = project + '_' + month + '_' + "1" + ".csv"

        exist_status = os.path.exists(os.path.join(project_output_path, check_file_name))
        if exist_status:
            print(Style.RESET_ALL + Fore.YELLOW + "{} already existed".format(os.path.join(project_output_path, output_file_name)) + Style.RESET_ALL)
            continue
        else:
            try:
                my_parser.parseProjectMonthData(project, project_data_path, 
                                                project_output_path, output_file_name)
                print(Style.RESET_ALL + Fore.LIGHTGREEN_EX + "{} at {} complete!".format(project, month) + Style.RESET_ALL)
            except Exception as e: 
                print(Style.RESET_ALL + Fore.RED + "{} at {} falied!".format(project, month))
                print(e)

