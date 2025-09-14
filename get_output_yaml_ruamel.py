import os
from dotenv import load_dotenv
from ruamel.yaml import YAML
from pathlib import Path

# 脚本作用，读取原yaml配置文件，用.env的配置替换yaml文件内容，保存到新yaml文件
# mihomo相关软件在订阅了新建本地订阅，然后指定该新yaml文件即可完成订阅

def load_config(input_path='config_input.yaml', output_path='config_output.yaml', env_path='.env'):
    # 加载自定义 .env
    load_dotenv(dotenv_path=env_path)
    print(f"已加载文件: {env_path}")
    
    # 用 ruamel.yaml 加载原 YAML（保留顺序和注释）
    yaml = YAML()
    yaml.preserve_quotes = True  # 保留引号（可选）
    yaml.indent(mapping=2, sequence=4, offset=2)  # 保持缩进（可选）
    print(f"已加载文件: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)  # data 是 CommentedMap，保持结构
    
    # 检查后替换
    if 'proxy-providers' in data and 'url' in data['proxy-providers']['Node']:
        data['proxy-providers']['Node']['url'] = os.getenv('LINK1')
    
    # 保存到新 YAML（保留原顺序、注释和格式）
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)
    
    print(f"配置已加载并保存到: {output_path}（保留了原顺序和注释）")
    return data

if __name__ == "__main__":
    config = load_config(input_path='singo的Mihomo单节点配置_base.yaml', output_path='singo的Mihomo单节点配置_output.yaml', env_path='mihomo.env')