# import os
# import pickle
#
# import pandas as pd
#
# # 定义存放CSV文件的文件夹路径
# folder_path = 'freebase'
#
# # 获取文件夹中所有的CSV文件
# csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
#
# # 存储表头的列表
# headers_list = []
#
# # 遍历每个CSV文件，读取表头并添加到列表中
# for csv_file in csv_files:
#     csv_path = os.path.join(folder_path, csv_file)
#     df = pd.read_csv(csv_path)
#     if not df.empty:
#         headers_list.append(df.columns.tolist())
#
# with open(file = 'candidate_attributes_list.pkl',mode = 'wb') as f:
#     pickle.dump(headers_list, f)
# # 打印生成的列表
# print(len(headers_list))
# print(headers_list)