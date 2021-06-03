from src.Parser import Parser



if __name__ == "__main__":
    data_path = r"data/528/03"
    output_path = r"complete/528/03"
    my_parser = Parser()



    my_parser.parseProjectMonthData(data_path, output_path)

