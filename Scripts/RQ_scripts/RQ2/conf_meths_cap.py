import pandas as pd

# 读取CSV文件
aospa_quartz_meths = pd.read_csv('./conf_meths/honor-u-meths.csv')
all_aff_files = pd.read_csv('all_aff_files-honor.csv')

# 筛选出AOSPA和quartz版本的条目
filtered_aff_files = all_aff_files[(all_aff_files['project'] == 'MagicOS') & (all_aff_files['version'] == 'UMagicOS')]

# 获取所有相关文件路径
aff_files_list = []
for files in filtered_aff_files['aff_files'].str.split(','):
    aff_files_list.extend(files)

# 检查aospa-quartz-meths中的文件路径是否存在于aff_files_list中
aospa_quartz_meths['is_in_aff_files'] = aospa_quartz_meths['Conf_details'].apply(lambda x: x in aff_files_list)

# 保留存在于aff_files_list中的条目
final_data = aospa_quartz_meths[aospa_quartz_meths['is_in_aff_files']]

# 可以选择打印或保存final_data
print(final_data)

# 如果需要保存处理后的数据到新的CSV文件
final_data.to_csv('./conf_meths_cap/honor-u-SAP-meths.csv', index=False)
