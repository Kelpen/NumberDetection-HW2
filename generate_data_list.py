DATA_ROOT = '/home/gpl/Dataset/HW2/'


with open('train_list.txt', 'w') as train_list:
    for i in range(30000):
        train_list.write(DATA_ROOT + '%d.png\n'%(i+1))


with open('val_list.txt', 'w') as val_list:
    for i in range(30000, 33403):
        val_list.write(DATA_ROOT + '%d.png\n'%(i+1))


with open('test_list.txt', 'w') as test_list:
    for i in range(13068):
        test_list.write(DATA_ROOT + '%d.png\n'%(i+1))
    

