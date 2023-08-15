import os
import pandas as pd
import pickle
def read_scv_content(csv_path):
    df = pd.read_csv(csv_path)
    label_value_pairs = []
    for index, row in df.iterrows():
        key_value_pairs = {}  # 创建一个空字典用于存放键值对
        key = row[1]  # 第二列作为键
        # print(csv_path)
        value = 1.0 / row[2]  # 第三列作为值
        key_value_pairs[key] = value
        label_value_pairs.append(key_value_pairs)
    return label_value_pairs

# def label_weight_Set(key_value_pairs)
def set_lable_value(label_value_pairs, n ,m):

    #count计算实体集中有多少个实体，result_dit存放最终结果
    count = len(label_value_pairs)
    label_weight_dict = {}
    #将具有相同标签的实体，将其标签的权重相加在一起
    for my_set in label_value_pairs:
        for key, value in my_set.items():
            if key in label_weight_dict:
                label_weight_dict[key] += value
            else:
                label_weight_dict[key] = value

    #计算最终实体集的标签和标签的权重
    for key, value in label_weight_dict.items():
        mid_value = (value ** int(n)) / (count ** int(m))
        label_weight_dict[key] = mid_value

    # print(result_dict)
    # print(label_weight_dict)
    return label_weight_dict

def offine_processing(folder_path, m, n):
    # 遍历文件夹中的每个文件
    label_weight_set = []
    files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if file_path.endswith('.csv'):
            # print(file_path)
            # print(filename)
            files.append(filename)
            label_value_pairs = read_scv_content(file_path)
            label_weight_dict = set_lable_value(label_value_pairs, m, n)
            label_weight_set.append(label_weight_dict)
    # print(label_weight_set)
    # print(files)
    return label_weight_set, files

def read_folder_attributes(folder_path, fnames):
    # 存放所有表格的表头的二维列表
    attributes = []

    # 遍历文件夹中的所有文件
    for filename in fnames:
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)

            # 读取CSV文件，假设第一行是表头
            df = pd.read_csv(file_path)

            # 获取表头，并存放在一个列表中
            headers_list = df.columns.tolist()

            # 将表头列表添加到all_headers中
            attributes.append(headers_list)
    return attributes

def can_unique_label(can_label_folder_path, fnames):
    unique_labels = []
    # 遍历文件夹中的所有文件
    for filename in fnames:
        if filename.endswith('.csv'):
            file_path = os.path.join(can_label_folder_path, filename)

            # 读取CSV文件，假设第一行是表头
            df = pd.read_csv(file_path)

            # 获取第二列数据，不包含表头
            second_column_data = df.iloc[:, 1]

            # 将第一列数据转换为Python列表
            second_column_list = second_column_data.tolist()

            # 将列表转换为集合，自动去重
            unique_set = set(second_column_list)

            # 如果需要，将集合转换回列表
            unique_list = list(unique_set)
            print(unique_list)
            # 将表头列表添加到all_headers中
            unique_labels.append(unique_list)
    # print(len(fnames))
    # print(len(unique_labels))
    return unique_labels
#
p1 = r'freebaseResult'
p2 = r'freebase'
# p1 = r'test_free_result'
# p2 = r'test_free'
label_weight_set, files = offine_processing(p1, 2, 2)
attributes = read_folder_attributes(p2, files)
unique_label = can_unique_label(p1, files)
print(len(label_weight_set))
print(len(attributes))
print(len(unique_label))
with open(file = 'label.pkl',mode = 'wb') as f:
    pickle.dump(label_weight_set, f)
with open(file = 'file_names.pkl',mode = 'wb') as f:
    pickle.dump(files, f)
with open(file='candidate_attributes_list.pkl', mode='wb') as f:
    pickle.dump(attributes, f)
with open(file='unique_label.pkl',mode='wb') as f:
    pickle.dump(unique_label, f)