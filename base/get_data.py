import yaml
import os


def get_data(filename, case_name):
    file_path = r"E:\blackhorseappAutoTest\PO\case3\data" + os.sep + filename
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.load(f)[case_name]
        data_list = []
        for i in data.values():
            temp = []
            for j in i.values():
                temp.append(j)
            data_list.append(tuple(temp))
        return data_list

if __name__ == "__main__":
    data = get_data("add_contact.yaml", "test_add_contact")
    print(data)
