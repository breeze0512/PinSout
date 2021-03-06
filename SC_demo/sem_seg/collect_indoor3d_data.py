import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
import indoor3d_util


# anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/test_anno_paths.txt'))]

# anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/anno_paths.txt'))]
anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/anno_paths.txt'))]
# anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/sc_test_anno_paths.txt'))]
# anno_paths = [line.rstrip() for line in open(os.path. join(BASE_DIR, 'meta/area_9_anno_paths.txt'))]
anno_paths = [os.path.join(indoor3d_util.DATA_PATH, p) for p in anno_paths]


output_folder = os.path.join(ROOT_DIR, '/root/pointnet/data/SCscan_data3')
# output_folder = os.path.join(ROOT_DIR, '/root/pointnet/sem_seg/npy_data')

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


for anno_path in anno_paths:
    print(anno_path)
    try:
        elements = anno_path.split('/')
        out_filename = elements[-3]+'_'+elements[-2]+'.npy'  # Area_1_hallway_1.npy
        print(out_filename)
        # indoor3d_util.collect_point_label2(anno_path, os.path.join(output_folder, out_filename), 'numpy')
        indoor3d_util.collect_point_label(anno_path, os.path.join(output_folder, out_filename), 'numpy')
    except:
        print(anno_path, 'ERROR!!')