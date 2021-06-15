import os 

DATA_PATH = r'complete'

projects = ['528','671','672','673','674','675',
            '677','678','680','709','756','986','1024','1025',
            '1027','1029','1034','1035','1036',
            '1048','1058','1071','1072','1075','1079',
            '1084','1085','1098','1099','1102','1105',
            '1110','1117','1120','1145','1147',
            '1162','1167','1184','1189','1192','1207']

for i in range(1, 13):
    month = '{0:02d}'.format(i)
    for project in projects:
        folder_path = os.path.join(DATA_PATH, month, project)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print("{} created".format(folder_path))
        else:
            print("{} already existed".format(folder_path))

    

