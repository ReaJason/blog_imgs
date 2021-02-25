#code=utf-8
import os
import random


jsdelivr = 'https://cdn.jsdelivr.net/gh/ReaJason/blog_imgs'
emoji = ['⚡', '🐶', '🦄', '🎨', '🐣', '🐬', '🐋', '💦', '🔰', '💤', '💫']

readme_text_list = ["""\
## [✨博客图片](https://reajason.top/) 

图床方案：[GitHub](https://github.com/) + [jsdelivr](https://www.jsdelivr.com/) + [docsmall](https://docsmall.com/)

后续可能会换方案，因此花一些时间整理一下图片，方便下次迁移

图片基本全来自于 [Awesome Wallpapers](https://wallhaven.cc/)

-----
## 🌈封面图
"""]
list_dir = os.listdir()
root_path = os.path.split(os.path.abspath(__file__))[0]
list_dir.remove('.git')
list_dir.remove('.github')
list_dir.remove('README.md')
list_dir.remove('update.py')
file_list = [file for file in list_dir if os.path.isfile(os.path.join(root_path, file))]
dir_list = [file for file in list_dir if file not in file_list]
readme_text_list.extend([f'[{jsdelivr}/{file}]({jsdelivr}/{file})' for file in file_list])
for dir in dir_list:
    readme_text_list.append(f'## {random.choice(emoji)}{dir}')
    file_list = os.listdir(os.path.join(root_path, dir))
    readme_text_list.extend([f'[{jsdelivr}/{dir}/{file}]({jsdelivr}/{dir}/{file})' for file in file_list])
with open('README.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(readme_text_list))

