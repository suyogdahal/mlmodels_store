
  test_dataloader /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_dataloader', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_dataloader 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/1d6b5e73b020f97a675f7a50f5d5814a804a8cd5', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/adata2/', 'repo': 'arita37/mlmodels', 'branch': 'adata2', 'sha': '1d6b5e73b020f97a675f7a50f5d5814a804a8cd5', 'workflow': 'test_dataloader'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_dataloader

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/adata2/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/1d6b5e73b020f97a675f7a50f5d5814a804a8cd5

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/1d6b5e73b020f97a675f7a50f5d5814a804a8cd5

 ************************************************************************************************************************

  ############Check model ################################ 





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py --do test  
['/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//keras_textcnn.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//namentity_crm_bilstm_new.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//resnet34_benchmark_mnist.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//matchzoo_models_new.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//charcnn.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//keras_reuters_charcnn.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//armdn_dataloader.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//resnet18_benchmark_mnist.json', '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor//torchhub_cnn_dataloader.json']





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/torchhub_cnn_dataloader.json 

#####  Load JSON data_pars
{'data_info': {'data_path': 'mlmodels/dataset/vision/MNIST', 'dataset': 'MNIST',
'data_type': 'tch_dataset', 'batch_size': 10, 'train': True}, 'preprocessors': [{'name':
'tch_dataset_start', 'uri': 'mlmodels.preprocess.generic::get_dataset_torch', 'args':
{'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri':
'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg':
{'fixed_size': 256, 'path': 'dataset/vision/MNIST/'}}, 'shuffle': True, 'download':
True}}]}

 #####  Load DataLoader 

 #####  compute DataLoader 

  URL:  mlmodels.preprocess.generic::get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {'fixed_size': 256, 'path': 'dataset/vision/MNIST/'}}, 'shuffle': True, 'download': True} 

###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f4641746e18>

 ######### postional parameteres :  ['data_info']

 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f4641746e18>

  function with postional parmater data_info <function get_dataset_torch at 0x7f4641746e18> , (data_info, **args) 

  #### If transformer URI is Provided 

  #### Loading dataloader URI 
0it [00:00, ?it/s]  0%|          | 0/9912422 [00:00<?, ?it/s] 31%|███       | 3096576/9912422 [00:00<00:00, 30403858.55it/s]9920512it [00:00, 32759809.85it/s]                             
0it [00:00, ?it/s]32768it [00:00, 530588.82it/s]
0it [00:00, ?it/s]  3%|▎         | 49152/1648877 [00:00<00:03, 460231.57it/s]1654784it [00:00, 11728636.84it/s]                         
0it [00:00, ?it/s]8192it [00:00, 188968.36it/s]dataset :  <class 'torchvision.datasets.mnist.MNIST'>
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Processing...
Done!

 #####  get_Data DataLoader 
((<torch.utils.data.dataloader.DataLoader object at 0x7f464027a080>, <torch.utils.data.dataloader.DataLoader object at 0x7f463fa85860>), {})





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_dataloader_new.json 

#####  Load JSON data_pars
Error /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_dataloader_new.json [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_dataloader_new.json'





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/model_list_CIFAR.json 

#####  Load JSON data_pars
Error /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/model_list_CIFAR.json [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/model_list_CIFAR.json'





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/resnet34_benchmark_mnist.json 

#####  Load JSON data_pars
{'data_info': {'data_path': 'mlmodels/dataset/vision/MNIST', 'dataset': 'MNIST',
'data_type': 'tch_dataset', 'batch_size': 10, 'train': True}, 'preprocessors': [{'name':
'tch_dataset_start', 'uri': 'mlmodels/preprocess/generic.py::get_dataset_torch', 'args':
{'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri':
'mlmodels.preprocess.image:torchvision_dataset_MNIST_load', 'pass_data_pars': False,
'arg': {'fixed_size': 256}}, 'shuffle': True, 'download': True}}]}

 #####  Load DataLoader 

 #####  compute DataLoader 

  URL:  mlmodels/preprocess/generic.py::get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torchvision_dataset_MNIST_load', 'pass_data_pars': False, 'arg': {'fixed_size': 256}}, 'shuffle': True, 'download': True} 

###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f4640292ea0>

 ######### postional parameteres :  ['data_info']

 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f4640292ea0>

  function with postional parmater data_info <function get_dataset_torch at 0x7f4640292ea0> , (data_info, **args) 

  #### If transformer URI is Provided 
transform torchvision_dataset_MNIST_load() missing 1 required positional argument: 'path'

  #### Loading dataloader URI 
dataset :  <class 'torchvision.datasets.mnist.MNIST'>

 #####  get_Data DataLoader 
((<torch.utils.data.dataloader.DataLoader object at 0x7f463faa19b0>, <torch.utils.data.dataloader.DataLoader object at 0x7f463faa1a20>), {})





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/keras_textcnn.json 

#####  Load JSON data_pars
{'data_info': {'dataset': 'mlmodels/dataset/text/imdb', 'pass_data_pars': False, 'train':
True, 'maxlen': 40, 'max_features': 5}, 'preprocessors': [{'name': 'loader', 'uri':
'mlmodels/preprocess/generic.py::NumpyDataset', 'args': {'numpy_loader_args':
{'allow_pickle': True}, 'encoding': "'ISO-8859-1'"}}]}

 #####  Load DataLoader 

 #####  compute DataLoader 

  URL:  mlmodels/preprocess/generic.py::NumpyDataset {'numpy_loader_args': {'allow_pickle': True}, 'encoding': "'ISO-8859-1'"} 

###### load_callable_from_uri LOADED <class 'mlmodels/preprocess/generic.NumpyDataset'>
cls_name : NumpyDataset
Dataset File path :  mlmodels/dataset/text/imdb.npz

 #####  get_Data DataLoader 
((array([list([10, 432, 2, 216, 11, 17, 233, 311, 100, 109, 27791, 5, 31, 3, 168, 366, 4, 1920, 634, 971, 12, 10, 13, 5523, 5, 64, 9, 85, 36, 48, 10, 694, 4, 13059, 15969, 26, 13, 61, 499, 5, 78, 209, 10, 13, 352, 15969, 253, 1, 106, 4, 3270, 14998, 52, 70, 2, 1839, 11762, 253, 1019, 7655, 16, 138, 12866, 1, 1910, 4, 3, 49, 17, 6, 12, 9, 67, 2885, 16, 260, 1435, 11, 28, 119, 615, 12, 1, 433, 747, 60, 13, 2959, 43, 13, 3080, 31, 2126, 312, 1, 83, 317, 4, 1, 17, 2, 68, 1678, 5, 1671, 312, 1, 330, 317, 134, 14200, 1, 747, 10, 21, 61, 216, 108, 369, 8, 1671, 18, 108, 365, 2068, 346, 14, 70, 266, 2721, 21, 5, 384, 256, 64, 95, 2575, 11, 17, 13, 84, 2, 10, 1464, 12, 22, 137, 64, 9, 156, 22, 1916]),
       list([281, 676, 164, 985, 5696, 1157, 53, 24, 2425, 2013, 1, 3357, 186, 11603, 16, 11, 220, 2572, 2252, 450, 41, 1, 21308, 1203, 587, 908, 118, 3, 182, 295, 47415, 5157, 36, 24, 4486, 975, 5, 294, 426, 24, 7117, 8, 48, 13, 2275, 14, 1, 830, 497, 123, 253, 143, 54, 334, 4, 8891, 2, 131, 10465, 9594, 2252, 1551, 23, 3, 9591, 3, 2517, 88, 1030, 221, 5, 1755, 959, 16, 4628, 2, 2376, 129, 18, 46, 86, 11, 19, 13, 8480, 29, 1, 169, 7, 7, 1, 19, 514, 16, 46, 1515, 633, 895, 835, 3, 51329, 307, 4, 1, 1122, 633, 895, 4, 27000, 49040, 2, 5544, 18, 35402, 364, 1361, 15, 91, 83, 31, 1, 1393, 531, 277, 1, 203, 1099, 5, 1, 1203, 587, 908, 180, 1258, 53, 52, 70, 5696, 124, 3, 324, 289, 2, 284, 3, 9408, 15, 1131, 3664, 15697, 10, 444, 1, 2514, 11836, 4223, 4, 1, 203, 20, 248, 104, 4, 1, 908, 12, 19323, 1, 111, 1034, 39, 760, 46, 2073, 1984, 1134, 5, 1, 3917, 222, 46, 1441, 106, 940, 51, 1, 695, 1332, 6, 2365, 31, 1215, 4, 1, 15171, 8, 325, 3672, 2, 347, 6085, 34, 2727, 24, 220, 17370, 14, 3, 503, 5, 94, 93, 15, 3, 8891, 262, 26, 79, 124, 3, 49, 289, 4, 2006, 5004, 48, 268, 20, 8, 1, 73329, 1825, 464, 5097, 8891, 3, 2146, 354, 4106, 6, 836, 6313, 1236, 130, 1106, 141, 79, 27, 345, 1, 267, 16132, 2, 2295, 2547, 15, 1852, 32, 1725, 807, 415, 838, 4, 1313, 2, 5788, 30, 1, 451, 4, 1, 10257, 1114, 7, 7, 22, 121, 86, 11, 6, 167, 5, 127, 21, 61, 85, 42, 445, 20, 3, 280, 62, 18, 79, 85, 105, 8, 11, 509, 791, 1, 169, 14212, 117, 2, 117, 18, 5696, 1454, 20, 3, 125, 71, 853, 120, 2, 379, 10442, 50, 673, 493, 1, 367, 71, 26, 123, 66, 8, 1008, 4, 9, 463, 1, 4374, 873, 11, 6, 3, 324, 2, 773, 19, 5, 3660, 15, 12, 1012, 5, 166, 32, 308]),
       list([14, 3, 32427, 48732, 16, 46, 1854, 4, 1, 45946, 476, 10, 13, 3518, 16, 4668, 8355, 5, 1, 1338, 4, 704, 8, 8891, 8, 1, 399, 10257, 1114, 1, 17, 2396, 70, 1, 1984, 3350, 12, 1332, 5103, 743, 306, 36, 24, 1545, 7417, 4, 109, 20936, 5, 24, 202, 5147, 5, 986, 12, 3059, 8553, 12, 10005, 87, 36, 109, 3208, 14, 32, 3212, 8, 628, 8891, 923, 4713, 1, 182, 268, 140, 24, 202, 704, 3044, 109, 3, 2688, 47450, 8, 1, 520, 4, 1, 3020, 16377, 1528, 34, 19884, 30, 24, 1024, 5, 2197, 749, 24, 2087, 7, 7, 48, 10, 444, 115, 187, 6, 86, 11, 753, 4, 704, 6, 16957, 8, 1, 102, 4, 843, 24, 333, 6, 3, 777, 704, 12527, 34, 1082, 1, 1104, 4, 251, 154, 18, 6, 22727, 31, 1, 3020, 704, 24, 449, 187, 12159, 38, 6253, 673, 2, 1759, 2, 9087, 87, 5, 6648, 24, 922, 4, 9887, 426, 145, 34, 101, 26, 6, 4551, 7, 7, 414, 1, 8891, 136, 23, 70, 3548, 258, 1, 262, 340, 8, 1, 17, 13, 21, 1, 776, 2135, 4, 1, 1376, 10822, 1, 114, 8863, 620, 31, 907, 78, 21, 6203, 36, 1, 933, 4, 1, 19, 222, 28, 114, 907, 558, 30, 1, 3070, 2699, 897, 1, 526, 124, 21, 63, 101, 907, 1, 274, 14, 8, 4628, 6, 21, 46, 907, 3562, 18, 28, 12, 61, 403, 476, 97, 25, 395]),
       ...,
       list([1, 1118, 509, 6, 3, 705, 14053, 16, 32, 3145, 31366, 3, 23322, 22816, 44, 802, 5, 94, 3, 173, 50, 43, 4, 11, 769, 1, 1835, 4, 1, 422, 8, 658, 5, 718, 41, 29, 1374, 4, 389, 1296, 10724, 2426, 5, 863, 1, 102, 50, 71, 1, 308, 7, 7, 42, 63, 244, 5919, 148, 22816, 149, 303, 925, 5264, 1, 705, 788, 8, 3, 1594, 12, 77, 398, 175, 2221, 9996, 244, 24, 1149, 6, 20, 1, 1512, 20469, 530, 7, 7, 1, 411, 6, 5559, 17993, 130, 20892, 47, 2, 16, 1, 1810, 863, 4, 1879, 13753, 31, 1, 2549, 1588, 148, 47, 6, 54, 117, 1, 1976, 35, 12, 1, 153, 67, 76, 20, 16, 7430, 8, 65, 831, 1, 2147, 600, 188, 984, 3, 1034, 4958, 2, 397, 492, 426, 1, 918, 7245, 4, 345, 267, 1325, 222, 79, 3, 52, 18911, 3325, 10, 132, 9, 695, 232, 5, 1, 1420, 10, 158, 178, 5, 64, 3, 6908, 4, 104, 1109, 652, 704, 81, 1056, 8, 32, 2799, 901, 10, 470, 5, 64, 46, 429, 4, 10282, 16531, 4, 1, 62, 7, 7, 414, 9, 6, 8, 189, 1, 62, 60, 1622, 1, 357, 177, 40, 14, 1, 788, 4, 833, 23, 244, 1032, 35, 1, 62, 6, 32, 3037, 4, 4760, 4, 272, 10523, 2, 15001, 9317, 14, 3, 2193, 15, 106, 5148, 36559, 2, 5105, 1422, 11, 23874, 11639, 16, 49, 351, 2, 305, 40745, 7695, 2179, 5, 36559, 6, 3, 2375, 7183, 15, 73, 4, 1, 7102, 7, 7, 143, 682, 21, 12, 42, 75, 18, 12, 9, 97, 25, 74, 73, 125, 339, 155]),
       list([686, 180, 3701, 69, 14, 5, 11, 19, 4630, 9, 378, 38277, 10300, 4, 1060, 2243, 34, 6, 207, 3, 1739, 5, 103, 9, 941, 527, 159, 9106, 521, 5179, 12748, 9, 6, 811, 8, 9055, 16, 1, 159, 9106, 19, 17147, 65041, 3, 461, 1175, 9, 5, 69, 187, 10, 13, 1251, 682, 1, 223, 766, 6, 1752, 2, 2729, 16, 52, 114, 3470, 113, 6, 475, 18, 5179, 6, 469, 464, 340, 1, 82, 153, 2, 1504, 23, 29, 861, 18, 10, 241, 7742, 16, 95, 29, 1209, 36, 1, 324, 26403, 60, 23, 20671, 466, 1, 17, 2, 10300, 2, 5179, 11, 19, 215, 52, 49, 35, 1, 1512, 4, 1, 62, 6, 89, 103, 9, 891, 22, 63, 178, 5]),
       list([625, 792, 4003, 23, 4840, 70, 395, 2, 7177, 14, 217, 132, 282, 10, 232, 41, 9287, 10159, 11, 2554, 618, 6, 35, 6735, 2, 117, 2651, 117, 1052, 2, 212, 25, 2161, 81794, 30, 5507, 8, 5493, 9, 2319, 5281, 1428, 2509, 12, 6, 328, 9120, 9287, 10159, 212, 25, 74, 33351, 36, 3, 2086, 2177, 12, 298, 1397, 72, 185, 12, 4995, 17441, 229, 2, 12, 478, 4, 225, 5583, 1622, 76, 11, 96, 2, 2672, 117, 3, 3682, 24375, 1, 956, 6, 3, 6759, 4, 14375, 84477, 317, 3, 47285, 46, 2726, 6580, 610, 2, 834, 1393, 4, 3, 402, 9645, 2, 58659, 35, 5453, 151, 3354, 14, 5, 27, 37, 618, 44883, 2, 20629, 21663, 16232, 1, 362, 6, 16326, 5464, 2874, 5, 647, 18, 1, 357, 1, 644, 880, 2803, 264, 15668, 3486, 457, 348, 1, 45365, 209, 2, 1, 14960, 354, 687, 11, 2090, 19, 80, 109, 2224, 10159, 6, 37, 3, 27315, 6300, 8107, 618, 16, 46, 5214, 1798, 5, 6708, 9, 53, 320, 623, 1, 288, 156, 1035, 8069, 2, 147, 6, 109, 414, 2522, 15, 1, 318, 19, 6, 2067, 6, 2, 3420, 269, 6459, 2697, 259, 8, 1, 233, 317, 531, 18, 10159, 6, 10218, 2, 13314, 45900, 2, 10, 261, 63, 553, 122, 1, 8107, 618, 18012, 4, 1, 3349, 2, 90, 3420, 165, 37, 10218, 171, 60, 10, 261, 13, 21, 10764, 3421, 5507, 212, 25, 14910, 43939, 51, 33, 216, 11, 2, 16, 157, 888, 1428, 19870, 8, 1274, 5281, 2, 1688, 1428, 8, 20, 3, 785, 248, 2, 2473, 1428, 8, 2562, 126, 10518, 33, 66, 3, 4115, 14120, 4, 15797, 8723, 16, 13816, 1428, 3143, 80, 467, 105, 16, 52, 8330, 21791, 276, 33, 141, 25, 1800, 81463, 7127, 15940, 36, 20, 3, 785, 248, 10159, 13, 52, 1060, 20, 5115, 83, 763, 8, 3872, 2, 2175, 8, 35532, 6151, 15, 1925, 18, 9, 1193, 277, 43, 8, 1, 16528, 2, 1, 3772, 2, 61, 123, 25474, 100, 12, 20, 28, 311, 1404, 16, 20, 3, 785, 248, 14, 3, 2707, 311, 1402, 1291, 555, 5507, 66, 65, 603, 87603, 419, 28, 1428, 2860, 19, 116, 62, 2, 12, 467, 1428, 2860, 2109, 11855, 1, 3515, 79, 1620, 5, 7733, 29, 1, 13816, 1428, 8, 40, 1, 372, 104, 150, 15, 40, 1045])],
      dtype=object), array([list([23022, 309, 6, 3, 1069, 209, 9, 2175, 30, 1, 169, 55, 14, 46, 82, 5869, 41, 393, 110, 138, 14, 5359, 58, 4477, 150, 8, 1, 5032, 5948, 482, 69, 5, 261, 12, 23022, 73935, 2003, 6, 73, 2436, 5, 632, 71, 6, 5359, 1, 25279, 5, 2004, 10471, 1, 5941, 1534, 34, 67, 64, 205, 140, 65, 1232, 63526, 21145, 1, 49265, 4, 1, 223, 901, 29, 3024, 69, 4, 1, 5863, 10, 694, 2, 65, 1534, 51, 10, 216, 1, 387, 8, 60, 3, 1472, 3724, 802, 5, 3521, 177, 1, 393, 10, 1238, 14030, 30, 309, 3, 353, 344, 2989, 143, 130, 5, 7804, 28, 4, 126, 5359, 1472, 2375, 5, 23022, 309, 10, 532, 12, 108, 1470, 4, 58, 556, 101, 12, 23022, 309, 6, 227, 4187, 48, 3, 2237, 12, 9, 215]),
       list([23777, 39, 81226, 14, 739, 20387, 3428, 44, 74, 32, 1831, 15, 150, 18, 112, 3, 1344, 5, 336, 145, 20, 1, 887, 12, 68, 277, 1189, 403, 34, 119, 282, 36, 167, 5, 393, 154, 39, 2299, 15, 1, 548, 88, 81, 101, 4, 1, 3273, 14, 40, 3, 413, 1200, 134, 8208, 41, 180, 138, 14, 3086, 1, 322, 20, 4930, 28948, 359, 5, 3112, 2128, 1, 20045, 19339, 39, 8208, 45, 3661, 27, 372, 5, 127, 53, 20, 1, 1983, 7, 7, 18, 48, 45, 22, 68, 345, 3, 2131, 5, 409, 20, 1, 1983, 15, 3, 3238, 206, 1, 31645, 22, 277, 66, 36, 3, 341, 1, 719, 729, 3, 3865, 1265, 20, 1, 1510, 3, 1219, 2, 282, 22, 277, 2525, 5, 64, 48, 42, 37, 5, 27, 3273, 12, 6, 23030, 75120, 2034, 7, 7, 3771, 3225, 34, 4186, 34, 378, 14, 12583, 296, 3, 1023, 129, 34, 44, 282, 8, 1, 179, 363, 7067, 5, 94, 3, 2131, 16, 3, 5211, 3005, 15913, 21720, 5, 64, 45, 26, 67, 409, 8, 1, 1983, 15, 3261, 501, 206, 1, 31645, 45, 12583, 2877, 26, 67, 78, 48, 26, 491, 16, 3, 702, 1184, 4, 228, 50, 4505, 1, 43259, 20, 118, 12583, 6, 1373, 20, 1, 887, 16, 3, 20447, 20, 24, 3964, 5, 10455, 24, 172, 844, 118, 26, 188, 1488, 122, 1, 6616, 237, 345, 1, 13891, 32804, 31, 3, 39870, 100, 42, 395, 20, 24, 12130, 118, 12583, 889, 82, 102, 584, 3, 252, 31, 1, 400, 4, 4787, 16974, 1962, 3861, 32, 1230, 3186, 34, 185, 4310, 156, 2325, 38, 341, 2, 38, 9048, 7355, 2231, 4846, 2, 32880, 8938, 2610, 34, 23, 457, 340, 5, 1, 1983, 504, 4355, 12583, 215, 237, 21, 340, 5, 4468, 5996, 34689, 37, 26, 277, 119, 51, 109, 1023, 118, 42, 545, 39, 2814, 513, 39, 27, 553, 7, 7, 134, 1, 116, 2022, 197, 4787, 2, 12583, 283, 1667, 5, 111, 10, 255, 110, 4382, 5, 27, 28, 4, 3771, 12267, 16617, 105, 118, 2597, 5, 109, 3, 209, 9, 284, 3, 4325, 496, 1076, 5, 24, 2761, 154, 138, 14, 7673, 11900, 182, 5276, 39, 20422, 15, 1, 548, 5, 120, 48, 42, 37, 257, 139, 4530, 156, 2325, 9, 1, 372, 248, 39, 20, 1, 82, 505, 228, 3, 376, 2131, 37, 29, 1023, 81, 78, 51, 33, 89, 121, 48, 5, 78, 16, 65, 275, 276, 33, 141, 199, 9, 5, 1, 3273, 302, 4, 769, 9, 37, 17648, 275, 7, 7, 39, 276, 11, 19, 77, 6018, 22, 5, 336, 406]),
       list([527, 117, 113, 31, 16974, 1962, 3861, 115, 902, 22590, 758, 10, 25, 123, 107, 2, 116, 136, 8, 1646, 7972, 23, 330, 5, 597, 1, 6244, 20, 390, 6, 3, 353, 14, 49, 14, 230, 8, 7673, 11900, 1, 190, 20, 9567, 6, 79, 894, 100, 109, 3609, 4, 109, 3, 36605, 3485, 43, 24, 1407, 2, 109, 12646, 1, 2405, 4, 32804, 12583, 26018, 39247, 143, 3, 2405, 26, 557, 286, 160, 712, 4122, 21720, 3, 511, 36, 1, 300, 2793, 7068, 120, 6, 774, 130, 96, 14, 3, 1165, 5285, 34, 491, 5, 4263, 1, 6788, 24, 106, 6, 50, 10557, 71, 641, 1, 1547, 133, 2, 1, 133, 118, 1, 3273, 18223, 3, 14364, 2135, 23, 29, 55, 2236, 165, 15, 1, 2974, 133, 2, 1, 104, 191, 16616, 994, 28, 26998, 11, 17, 211, 125, 254, 55, 10, 64, 9, 60, 6, 176, 397]),
       ...,
       list([10, 216, 77424, 233, 311, 30, 1, 21144, 19, 1410, 2, 9, 13, 28, 663, 1384, 1384, 85, 1, 766, 13, 4613, 973, 1, 10825, 4, 316, 7284, 3994, 8, 3, 4136, 4688, 17, 13, 1124, 2, 109, 3, 334, 931, 30037, 143, 21, 4, 45035, 49280, 1551, 4, 1, 1697, 10, 13, 2961, 5, 132, 52, 1994, 5, 805, 11, 17, 43, 58, 1171, 900, 1228, 5, 1, 2236, 419, 1, 766, 44, 983, 18, 1, 3230, 23, 1032, 1, 153, 2628, 57, 3994, 6, 1893, 46, 59, 132, 12, 42, 3, 205, 2820, 4, 1, 1167, 179, 8, 1, 175, 12, 1, 10732, 4, 1, 102, 2892, 3, 1285, 2, 29, 12, 3979, 18, 9, 40, 163, 1, 223, 17, 41077, 40, 37, 1, 133, 118, 3994, 211, 3537, 9, 612, 1500, 3030, 10, 283, 1014, 230, 63005, 402, 18, 128, 710, 72, 1405, 5, 232, 5051, 15, 38, 10, 158, 21, 15, 3, 783, 56, 13, 35, 832, 29, 1, 93, 2, 10, 329, 12, 1, 1378, 13, 1156, 70, 9, 6, 49, 846, 18, 161, 1562, 2241, 342, 10, 212, 971, 12, 1, 2821, 30, 1, 1410, 283, 35, 49, 35, 276, 10, 1046, 43, 139, 130, 18, 30, 1, 127, 4, 1, 17, 10, 423, 336, 533, 7159, 232, 37, 146, 16173, 69516, 171, 3999, 50, 612, 1, 83, 133, 8, 1, 1330, 6, 1290, 321, 2, 29, 18, 10, 66, 1, 2916, 8773, 4, 146, 3, 1204, 2, 50, 354, 307, 4, 1, 133, 8, 1, 6407, 1446, 748, 1, 295, 2277, 3620, 8, 7642, 42456, 8445, 965, 1132, 16, 15523, 1, 2622, 764, 2, 1333, 1521, 1, 1182, 9467, 225, 1, 828, 16846, 12600, 838, 54, 10, 40, 423, 76, 80, 11, 17, 96, 75]),
       list([46, 105, 12, 22, 1258, 53, 15, 3, 6564, 468, 43, 5, 27, 244, 49, 31940, 1114, 105, 623, 4190, 4, 3717, 1119, 2, 295, 17, 12, 68, 84, 18, 258, 35131, 623, 46, 4956, 105, 2920, 406, 1, 6134, 4, 65, 10561, 6, 592, 37, 1, 862, 6242, 7, 7, 1, 61, 1120, 152, 10, 67, 132, 41, 11, 19, 6, 12, 42, 1279, 748, 14, 613, 14, 1, 7222, 4, 2117, 82, 71, 12, 91, 3, 52, 4113, 6825, 19, 16, 1, 1756, 18424, 4, 3, 27058, 310, 2168, 31, 3, 60431, 7, 7, 42, 74, 3209, 3297, 18, 22, 63, 78, 25, 5, 3247, 41, 3, 19, 12, 17580, 5593, 4, 1, 203, 80, 91, 1106, 717, 35, 31, 1, 55, 9, 211, 5, 1, 862, 3031, 871, 107, 9, 29, 457, 7, 7, 75, 17, 448, 77, 25, 3, 1868, 146, 1, 3067, 1779, 2383, 2494, 2, 1, 9586, 113, 4, 1, 174, 259, 1, 11200, 34, 13, 35, 75, 26, 119, 94, 69, 459, 3, 224, 2, 3597, 5, 35131, 15, 394, 8, 5, 1, 1100, 4, 180, 31, 7015, 3, 2489, 35, 75, 9, 418, 37, 10, 13, 146, 46, 1556, 53, 341, 371, 4, 3, 7790, 1186, 7, 7, 370, 370, 535, 1999, 29, 90, 535, 37, 11, 51, 1999, 1837, 3, 1067, 4, 3, 367, 18, 1138, 278, 14824, 2, 131, 105, 38137, 8, 260, 51902, 1195, 795]),
       list([11, 6, 28, 4, 1, 7051, 105, 204, 123, 107, 9, 7244, 122, 751, 123, 549, 4, 705, 2, 1027, 5, 94, 3, 944, 4, 95, 29, 7, 7, 222, 21, 3, 683, 49, 344, 39, 106, 8, 1, 223, 944, 45, 47, 13, 3, 111, 9, 13, 32, 11620, 2, 14, 227, 14, 113, 268, 222, 161, 49, 5, 132, 35, 1812, 132, 161, 10, 1249, 2485, 388, 86, 11, 549, 4, 1832, 211, 1052, 2, 162, 623, 124, 1840, 1195, 21, 30, 46, 865, 101, 12919, 58, 555, 11, 63, 6, 3, 3814, 4, 62964, 2, 680, 9, 3, 248, 91, 592, 37, 11, 12, 44, 81, 17238, 20043, 1, 1469, 269, 37, 3, 337, 272, 19, 30, 219, 45, 22, 25, 10131, 9, 22, 771, 1050, 126, 55, 39, 275, 89, 434, 126, 55, 11, 6, 1347])],
      dtype=object), array([1, 1, 1, ..., 0, 0, 0]), array([1, 1, 1, ..., 0, 0, 0])), {})





 ####################################################################################################
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_new.json 

#####  Load JSON data_pars
{'data_info': {'data_path': 'dataset/text/', 'dataset': 'ner_dataset.csv',
'pass_data_pars': False, 'train': True}, 'preprocessors': [{'name': 'loader', 'uri':
'mlmodels/preprocess/generic.py::pandasDataset', 'args': {'read_csv_parm': {'encoding':
'ISO-8859-1'}, 'colX': [], 'coly': []}}, {'uri':
'mlmodels/preprocess/text_keras.py::Preprocess_namentity', 'args': {'max_len': 75},
'internal_states': ['word_count']}, {'name': 'split_xy', 'uri':
'mlmodels/dataloader.py::split_xy_from_dict', 'args': {'col_Xinput': ['X'], 'col_yinput':
['y']}}, {'name': 'split_train_test', 'uri': 'sklearn.model_selection::train_test_split',
'args': {'test_size': 0.5}}, {'name': 'saver', 'uri':
'mlmodels/dataloader.py::pickle_dump', 'args': {'path':
'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'}}], 'output': {'shape': [[75],
[75, 18]], 'max_len': 75}}

 #####  Load DataLoader 

 #####  compute DataLoader 

  URL:  mlmodels/preprocess/generic.py::pandasDataset {'read_csv_parm': {'encoding': 'ISO-8859-1'}, 'colX': [], 'coly': []} 

###### load_callable_from_uri LOADED <class 'mlmodels/preprocess/generic.pandasDataset'>
cls_name : pandasDataset
>>>> df:      Sentence #           Word  POS Tag
0  Sentence: 1      Thousands  NNS   O
1          NaN             of   IN   O
2          NaN  demonstrators  NNS   O
3          NaN           have  VBP   O
4          NaN        marched  VBN   O

  URL:  mlmodels/preprocess/text_keras.py::Preprocess_namentity {'max_len': 75} 

###### load_callable_from_uri LOADED <class 'mlmodels/preprocess/text_keras.Preprocess_namentity'>
cls_name : Preprocess_namentity

 Object Creation

 Object Compute

 Object get_data

  URL:  mlmodels/dataloader.py::split_xy_from_dict {'col_Xinput': ['X'], 'col_yinput': ['y']} 

###### load_callable_from_uri LOADED <function split_xy_from_dict at 0x7f462437d0d0>

 ######### postional parameteres :  ['out']

 ######### Execute : preprocessor_func <function split_xy_from_dict at 0x7f462437d0d0>

  URL:  sklearn.model_selection::train_test_split {'test_size': 0.5} 

###### load_callable_from_uri LOADED <function train_test_split at 0x7f4693ec8ae8>

 ######### postional parameteres :  []

 ######### Execute : preprocessor_func <function train_test_split at 0x7f4693ec8ae8>

  URL:  mlmodels/dataloader.py::pickle_dump {'path': 'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'} 

Using TensorFlow backend.

###### load_callable_from_uri LOADED <function pickle_dump at 0x7f463faa3268>

 ######### postional parameteres :  ['t']

 ######### Execute : preprocessor_func <function pickle_dump at 0x7f463faa3268>
Error /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_new.json [Errno 2] No such file or directory: 'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'
