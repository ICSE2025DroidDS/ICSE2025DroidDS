import pandas as pd
from ast import literal_eval

# 尝试使用不同的编码读取文件
encoding = 'ISO-8859-1'

# 步骤 1: 读取CSV文件
input_file = './diffProgect-sap-recur_textblock-<name>.csv'
df = pd.read_csv(input_file, encoding=encoding)

# 转换字符串表示的列表和元组回到Python对象
df['merge_commitid'] = df['merge_commitid'].apply(literal_eval)
df['recurBlockSrc'] = df['recurBlockSrc'].apply(literal_eval)

# 步骤 2: 按照`file`和`recur_segment`字段分组
groups = df.groupby(['file', 'recur_segment'])

# 用于存储最终结果的列表
results = []

# 步骤 3: 循环处理每个分组
for (file, recur_segment), group in groups:
    # 合并`merge_commitid`列表并去除重复项
    merged_commitids = set()
    for commitids in group['merge_commitid']:
        merged_commitids.update(commitids)

    # 合并`recurBlockSrc`列表并去除重复项
    recurBlockSrcs = set()
    for recurBlockSrc in group['recurBlockSrc']:
        recurBlockSrcs.update(recurBlockSrc)
    
    # 添加到结果列表
    results.append({
        'file': file,
        'merge_commitid': list(merged_commitids),
        'recurBlockSrc': list(recurBlockSrcs),
        'recur_segment': recur_segment,
        'times': len(merged_commitids)
    })

# 转换结果列表为DataFrame
results_df = pd.DataFrame(results)

# 添加`id`列
results_df.reset_index(inplace=True, drop=True)
results_df.index += 1
results_df.reset_index(inplace=True)
results_df.rename(columns={'index': 'id'}, inplace=True)

# 步骤 4: 保存处理后的数据到新的CSV文件
output_file = './diffProgect-sap-recur_textblock-<name>_times.csv'
results_df.to_csv(output_file, index=False, encoding=encoding)

print(f'Processed data has been saved to {output_file}.')
