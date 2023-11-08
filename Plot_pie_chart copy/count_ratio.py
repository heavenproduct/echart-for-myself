# {value: 60, name: 'CCLSa', label:{normal:{rotate:60}}},

import os 


def geneData(rotate_val_list):
    # 生成一个环的数据
    # rotate_val_list = [
    #     [cls_name , cls_num],
    #     [cls_name , cls_num],
    #     [cls_name , cls_num],
    # ] 

    # sumAngle 累加label角度用 给label加rotate  初始为90 因为echart中 饼图开始位置和字体初始化角度有90度的夹角
    sumAngle = 90 
    # 先要计算总共的数据量, 才能按照比例来设定角度
    totalAmount = 0
    for rvl in rotate_val_list:
        totalAmount += rvl[1]
    
    for rvl in rotate_val_list:
        cls_name = rvl[0] 
        cls_angle = rvl[1] / totalAmount * 360
        cls_rotate = sumAngle - (0.5 * cls_angle) 
        sumAngle -= cls_angle
        if cls_rotate <= -90 :
            cls_rotate = cls_rotate + 180
        str_cls = "{value: "+str(cls_angle)+", name: '"+cls_name+"', label:{normal:{rotate:"+str(cls_rotate)+"}}},"
        print(str_cls)

# data1 = [
#     ['yidanA' , 30],
#     ['yidanB' , 50],
#     ['yidanC' , 60],
# ]

# data2 = [
#     ['subA1', 10],
#     ['subA2', 10],
#     ['subA3', 10],
#     ['subB1', 10],
#     ['subB2', 20],
#     ['subB3', 20],
#     ['subC1', 10],
#     ['subC2', 50],
# ]


# data3 = [
#     ['subA11', 5],
#     ['subA12', 5],
#     ['subA21', 2],
#     ['subA22', 8],
#     ['subA31', 3],
#     ['subA32', 7],
#     ['subB11', 4],
#     ['subB12', 6],
#     ['subB21', 11],
#     ['subB22', 9],
#     ['subB31', 10],
#     ['subB32', 5],
#     ['subB33', 5],
#     ['subC1', 10],
#     ['subC21', 33],
#     ['subC22', 17],
# ]


# geneData(data3)




        




