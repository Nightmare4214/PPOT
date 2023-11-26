import os
from glob import glob

if __name__ == '__main__':
    root = '/home/icml007/Nightmare4214/datasets/office31'
    # /home/icml007/Nightmare4214/datasets/office31/amazon/images
    # /home/icml007/Nightmare4214/datasets/office31/dslr/images/back_pack/xxx.jpg
    all_paths = [x for x in glob(os.path.join(root, '*')) if os.path.isdir(x)]
    all_classes = list({os.path.basename(x) for x in glob(os.path.join(root, '*', '*', '*'))})
    all_classes.sort()
    all_classes = {cur_class:idx for idx, cur_class in enumerate(all_classes)}

    for path in all_paths:
        target = path + '.txt'
        with open(target, 'w') as f:
            for cur in glob(os.path.join(path, '*', '*', '*.jpg')):
                cur_class = os.path.basename(os.path.dirname(cur))
                f.write(f'{cur} {all_classes[cur_class]}\n')
        