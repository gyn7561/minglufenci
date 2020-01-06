import pkuseg
import os

seg = pkuseg.pkuseg()  # 以默认配置加载模型


def process(file):
    filepath, tmpfilename = os.path.split(file)
    shotname, extension = os.path.splitext(tmpfilename)
    if os.path.exists(shotname + "-words" + extension):
        print("跳过" + file)
        return

    print("开始处理" + file)
    fp = open(file)
    content = fp.read()
    fp.close()
    text = seg.cut(content)
    word_set = set(text)

    with open(shotname + "-words" + extension, 'w') as file_obj:
        file_obj.write("\n".join(list(word_set)))

mainPath = "名录"
pathDir = os.listdir(mainPath)
for file in pathDir:
    process(mainPath + "/" + file)
