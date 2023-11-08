import numpy as np 

def get_pos_emb_perm(th , ph):
    # th = 3  ph = 14
    new_perm = []
    t_num = th ** 2 
    p_num = ph ** 2 

    origin_perm = list(range(p_num))
    origin_perm = np.array(origin_perm)
    origin_perm = origin_perm.reshape((ph , ph))
    # print(origin_perm[0][0:4])
    min_tile_div = ph // th  #  4     
    res_tile_div = ph % th   #  2 
    
    col_list = [] 
    row_list = []
    div_num = 0 
    for idx in range(th):
        if idx < th - res_tile_div:  
            div_num += min_tile_div 
        else:
            div_num += min_tile_div + 1 
        col_list.append(div_num )
        row_list.append(div_num )
    # print(row_list)
        

    for id_r, col in enumerate(row_list):
        
        if id_r == 0: 
            start_r, end_r = 0, col 
        else:
            start_r, end_r = col_list[id_r - 1] , col   
                  
        for id_c, row in enumerate(col_list):
            if id_c == 0: 
                start_c, end_c = 0, row 
            else:
                start_c, end_c = col_list[id_c - 1] , row   
            
            
            # print([start_r, end_r , start_c, end_c])     

        
            for new_r in range(start_r, end_r):
                chosed = origin_perm[new_r][start_c: end_c]
                for kk in chosed:
                    new_perm.append(kk)
    return new_perm 

