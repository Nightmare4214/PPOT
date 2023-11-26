# Prototypical Partial Optimal Transport for Universal Domain Adaptation

Code for paper "Yucheng Yang, Xiang Gu, Jian Sun, **Prototypical Partial Optimal Transport for Universal Domain Adaptation**, the 37th AAAI Conference on Artificial Intelligence, 2023".

## Prerequisites

python==3.9  
pytorch ==1.12.1  
torchvision ==0.13.1  
numpy==1.23.1  
POT==0.8.2

## Datasets

Download the datasets of  
[DomainNet](http://ai.bu.edu/M3SDA/)  
[Office-Home](https://www.hemanthdv.org/officeHomeDataset.html)  
[Office-31](https://www.cc.gatech.edu/~judy/domainadapt/)  
[VisDA-2017](http://ai.bu.edu/visda-2017/)  
and modify the path of images in each '.txt' under the folder './data/'.

## Training

Office-31:

```bash
python train.py --task office31 -s amazon -t dslr --lr 0.0002 --balanced --no-ssl
```

batch=60  
best H-score = 88.9  
best unknown accuracy = 94.7  
best known accuracy = 83.8

Office-Home:

```bash
python train.py --task officehome -s Art -t Clipart --lr 0.001 --balanced --mlp --aug-plus --cos --multiprocessing-distributed
```

VisDA-2017:

```bash
python train.py --task VisDA2017 -s train -t validation --lr 0.0005 --balanced --mlp --aug-plus --cos --multiprocessing-distributed
```

## Reference code

<https://github.com/facebookresearch/moco>

## Contact

If you have any problem, feel free to contect ycyang@stu.xjtu.edu.cn.
