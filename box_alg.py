import sys


def create_boxes_list():
    box_list = []

    for i in range(m):
        box_size = []
    
        for j in range(k):
            box_size.append(0)
    
        box_list.append(box_size)
    
    return box_list
    

def check_the_box(box_list , objects_size , flag , ones_list):
    index_of_num = 0
    
    for box in box_list:
        if flag == False:
            print(f'Finish the process -----------------------------------------------------------------------------------------------------> {box_list}')
            break
        
        for num in objects_size[index_of_num :]:
            zero_count = box.count(0)
            
            if num > len(box):
                continue
            
            if num < zero_count:
                    
                index_of_element = box.index(0)

                for i in range(num):
                    box[index_of_element + i] = 1

                print(f'Number: {num} is less than our box but we can use that -------------------> Box: {box_list}')
                one_count = box.count(1)
                ones_list.append(one_count)
                
                if objects_size.index(num) == len(objects_size) - 1:
                    print('We are out of numbers')
                    flag = False
                    break
    #             objects_size.remove(num)
                continue
            
            if num == zero_count:
                    
                index_of_element = box.index(0)

                for i in range(num):
                    box[index_of_element + i] = 1

                print(f'Number: {num} is equal to our box and we can use that -------------------> Box: {box_list}')
                one_count = box.count(1)
                ones_list.append(one_count)
                index_of_num = objects_size.index(num) + 1
                break
        
            elif num > zero_count:
                if zero_count == 0:
                    if objects_size.index(num) == len(objects_size) - 1:
                        print("the deadline")
                        one_count = box.count(1)
                        ones_list.append(one_count)
                        flag = False
                        break
                
                print(f'Number: {num} is The stop point -------------------------------------------> Box: {box_list}')
                one_count = box.count(1)
                ones_list.append(one_count)
                box_list = create_boxes_list()
                objects_size = objects_size[objects_size.index(num) :]
                check_the_box(box_list , objects_size , True , ones_list)
                sys.exit("The End")
        
    
n = int(input('Enter the number of the objects which you want to put into the box: '))
m = int(input('Enter the number of boxes which you want to use: '))
k = int(input('Enter the size of each box: '))
objects_size = list()

for i in range(n):
    size = int(input('Enter the size for your object: '))
    objects_size.append(size)

    
ones_list = list()
box_list = create_boxes_list()
check_the_box(box_list , objects_size , True , ones_list)

max_value = max(ones_list)
sum_value = 0

for i in range(len(objects_size)):

    sum_value = objects_size[i] + sum_value

    if sum_value > max_value:
        sum_value = objects_size[i]
        continue

    if sum_value < max_value:
        continue

    if sum_value == max_value:
        print(i+1)
        break

    
    