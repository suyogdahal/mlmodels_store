
  test_jupyter /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_jupyter', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_jupyter 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/66c80276865deac85c18a6c92009a1b1c80dedef', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '66c80276865deac85c18a6c92009a1b1c80dedef', 'workflow': 'test_jupyter'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_jupyter

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/66c80276865deac85c18a6c92009a1b1c80dedef

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/66c80276865deac85c18a6c92009a1b1c80dedef

 ************************************************************************************************************************
/home/runner/work/mlmodels/mlmodels/mlmodels/example/
############ List of files ################################
['ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_titanic.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_svm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//keras_charcnn_reuters.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//keras-textcnn.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//fashion_MNIST_mlmodels.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//mnist_mlmodels_.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//tensorflow_1_lstm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_home_retail.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//gluon_automl.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//gluon_automl_titanic.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vison_fashion_MNIST.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//tensorflow__lstm_json.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//arun_model.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//benchmark_timeseries_m4.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//arun_hyper.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m4.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//benchmark_timeseries_m5.py']





 ************************************************************************************************************************
############ Running Jupyter files ################################





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_titanic.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_titanic.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0mdata_path[0m [0;34m=[0m [0;34m'hyper_lightgbm_titanic.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'hyper_lightgbm_titanic.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_svm.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     69[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 70[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     71[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     81[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 82[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     83[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_svm.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;34m[0m[0m
[1;32m      4[0m [0mmodel_uri[0m    [0;34m=[0m [0;34m"model_sklearn.sklearn.py"[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;34m[0m[0m
[1;32m      7[0m model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     85[0m [0;34m[0m[0m
[1;32m     86[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 87[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     88[0m [0;34m[0m[0m
[1;32m     89[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//keras_charcnn_reuters.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//keras_charcnn_reuters.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mmodel_pars[0m      [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'model_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      3[0m [0mdata_pars[0m       [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'data_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0mcompute_pars[0m    [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'compute_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0mout_pars[0m        [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'out_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'reuters_charcnn.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//keras-textcnn.ipynb 

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 400)          0                                            
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 400, 50)      500         input_1[0][0]                    
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 398, 128)     19328       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 397, 128)     25728       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 396, 128)     32128       embedding_1[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_1 (GlobalM (None, 128)          0           conv1d_1[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_2 (GlobalM (None, 128)          0           conv1d_2[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_3 (GlobalM (None, 128)          0           conv1d_3[0][0]                   
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 384)          0           global_max_pooling1d_1[0][0]     
                                                                 global_max_pooling1d_2[0][0]     
                                                                 global_max_pooling1d_3[0][0]     
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 1)            385         concatenate_1[0][0]              
==================================================================================================
Total params: 78,069
Trainable params: 78,069
Non-trainable params: 0
__________________________________________________________________________________________________
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 1499136/17464789 [=>............................] - ETA: 0s
 8028160/17464789 [============>.................] - ETA: 0s
16408576/17464789 [===========================>..] - ETA: 0s
17465344/17464789 [==============================] - 0s 0us/step
Pad sequences (samples x time)...
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-11 03:27:13.625441: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-11 03:27:13.629913: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-11 03:27:13.630042: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55e2d9c0db00 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-11 03:27:13.630056: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

2020-05-11 03:27:14.108626: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 17424000 exceeds 10% of system memory.
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

   32/25000 [..............................] - ETA: 4:40 - loss: 7.6666 - accuracy: 0.50002020-05-11 03:27:14.229798: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 17424000 exceeds 10% of system memory.

   64/25000 [..............................] - ETA: 3:07 - loss: 6.7083 - accuracy: 0.56252020-05-11 03:27:14.354738: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 17424000 exceeds 10% of system memory.

   96/25000 [..............................] - ETA: 2:36 - loss: 7.5069 - accuracy: 0.51042020-05-11 03:27:14.472771: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 17424000 exceeds 10% of system memory.

  128/25000 [..............................] - ETA: 2:20 - loss: 7.6666 - accuracy: 0.50002020-05-11 03:27:14.593643: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 17424000 exceeds 10% of system memory.

  160/25000 [..............................] - ETA: 2:12 - loss: 7.9541 - accuracy: 0.4812
  192/25000 [..............................] - ETA: 2:05 - loss: 8.4652 - accuracy: 0.4479
  224/25000 [..............................] - ETA: 2:01 - loss: 8.2827 - accuracy: 0.4598
  256/25000 [..............................] - ETA: 1:58 - loss: 8.3854 - accuracy: 0.4531
  288/25000 [..............................] - ETA: 1:55 - loss: 8.3055 - accuracy: 0.4583
  320/25000 [..............................] - ETA: 1:52 - loss: 8.1458 - accuracy: 0.4688
  352/25000 [..............................] - ETA: 1:50 - loss: 8.3200 - accuracy: 0.4574
  384/25000 [..............................] - ETA: 1:48 - loss: 8.3854 - accuracy: 0.4531
  416/25000 [..............................] - ETA: 1:46 - loss: 8.3669 - accuracy: 0.4543
  448/25000 [..............................] - ETA: 1:44 - loss: 8.3169 - accuracy: 0.4576
  480/25000 [..............................] - ETA: 1:43 - loss: 8.2097 - accuracy: 0.4646
  512/25000 [..............................] - ETA: 1:42 - loss: 8.1158 - accuracy: 0.4707
  544/25000 [..............................] - ETA: 1:41 - loss: 7.9767 - accuracy: 0.4798
  576/25000 [..............................] - ETA: 1:41 - loss: 7.9062 - accuracy: 0.4844
  608/25000 [..............................] - ETA: 1:40 - loss: 7.8179 - accuracy: 0.4901
  640/25000 [..............................] - ETA: 1:40 - loss: 7.9541 - accuracy: 0.4812
  672/25000 [..............................] - ETA: 1:39 - loss: 7.8720 - accuracy: 0.4866
  704/25000 [..............................] - ETA: 1:38 - loss: 7.7973 - accuracy: 0.4915
  736/25000 [..............................] - ETA: 1:39 - loss: 7.8125 - accuracy: 0.4905
  768/25000 [..............................] - ETA: 1:38 - loss: 7.8862 - accuracy: 0.4857
  800/25000 [..............................] - ETA: 1:38 - loss: 7.7816 - accuracy: 0.4925
  832/25000 [..............................] - ETA: 1:37 - loss: 7.7956 - accuracy: 0.4916
  864/25000 [>.............................] - ETA: 1:37 - loss: 7.7731 - accuracy: 0.4931
  896/25000 [>.............................] - ETA: 1:36 - loss: 7.7864 - accuracy: 0.4922
  928/25000 [>.............................] - ETA: 1:35 - loss: 7.7823 - accuracy: 0.4925
  960/25000 [>.............................] - ETA: 1:35 - loss: 7.7625 - accuracy: 0.4938
  992/25000 [>.............................] - ETA: 1:34 - loss: 7.6975 - accuracy: 0.4980
 1024/25000 [>.............................] - ETA: 1:34 - loss: 7.7265 - accuracy: 0.4961
 1056/25000 [>.............................] - ETA: 1:33 - loss: 7.7683 - accuracy: 0.4934
 1088/25000 [>.............................] - ETA: 1:33 - loss: 7.7653 - accuracy: 0.4936
 1120/25000 [>.............................] - ETA: 1:32 - loss: 7.7214 - accuracy: 0.4964
 1152/25000 [>.............................] - ETA: 1:32 - loss: 7.7598 - accuracy: 0.4939
 1184/25000 [>.............................] - ETA: 1:32 - loss: 7.7573 - accuracy: 0.4941
 1216/25000 [>.............................] - ETA: 1:31 - loss: 7.7675 - accuracy: 0.4934
 1248/25000 [>.............................] - ETA: 1:31 - loss: 7.8018 - accuracy: 0.4912
 1280/25000 [>.............................] - ETA: 1:30 - loss: 7.7984 - accuracy: 0.4914
 1312/25000 [>.............................] - ETA: 1:30 - loss: 7.8419 - accuracy: 0.4886
 1344/25000 [>.............................] - ETA: 1:30 - loss: 7.8492 - accuracy: 0.4881
 1376/25000 [>.............................] - ETA: 1:30 - loss: 7.8561 - accuracy: 0.4876
 1408/25000 [>.............................] - ETA: 1:29 - loss: 7.8409 - accuracy: 0.4886
 1440/25000 [>.............................] - ETA: 1:29 - loss: 7.8050 - accuracy: 0.4910
 1472/25000 [>.............................] - ETA: 1:29 - loss: 7.8125 - accuracy: 0.4905
 1504/25000 [>.............................] - ETA: 1:29 - loss: 7.8093 - accuracy: 0.4907
 1536/25000 [>.............................] - ETA: 1:28 - loss: 7.8463 - accuracy: 0.4883
 1568/25000 [>.............................] - ETA: 1:28 - loss: 7.8622 - accuracy: 0.4872
 1600/25000 [>.............................] - ETA: 1:28 - loss: 7.8295 - accuracy: 0.4894
 1632/25000 [>.............................] - ETA: 1:28 - loss: 7.8169 - accuracy: 0.4902
 1664/25000 [>.............................] - ETA: 1:28 - loss: 7.7864 - accuracy: 0.4922
 1696/25000 [=>............................] - ETA: 1:28 - loss: 7.7661 - accuracy: 0.4935
 1728/25000 [=>............................] - ETA: 1:27 - loss: 7.7642 - accuracy: 0.4936
 1760/25000 [=>............................] - ETA: 1:27 - loss: 7.7363 - accuracy: 0.4955
 1792/25000 [=>............................] - ETA: 1:27 - loss: 7.7436 - accuracy: 0.4950
 1824/25000 [=>............................] - ETA: 1:27 - loss: 7.7507 - accuracy: 0.4945
 1856/25000 [=>............................] - ETA: 1:27 - loss: 7.7327 - accuracy: 0.4957
 1888/25000 [=>............................] - ETA: 1:26 - loss: 7.7478 - accuracy: 0.4947
 1920/25000 [=>............................] - ETA: 1:26 - loss: 7.7545 - accuracy: 0.4943
 1952/25000 [=>............................] - ETA: 1:26 - loss: 7.7452 - accuracy: 0.4949
 1984/25000 [=>............................] - ETA: 1:26 - loss: 7.7516 - accuracy: 0.4945
 2016/25000 [=>............................] - ETA: 1:26 - loss: 7.7731 - accuracy: 0.4931
 2048/25000 [=>............................] - ETA: 1:26 - loss: 7.7789 - accuracy: 0.4927
 2080/25000 [=>............................] - ETA: 1:25 - loss: 7.7919 - accuracy: 0.4918
 2112/25000 [=>............................] - ETA: 1:25 - loss: 7.7392 - accuracy: 0.4953
 2144/25000 [=>............................] - ETA: 1:25 - loss: 7.7310 - accuracy: 0.4958
 2176/25000 [=>............................] - ETA: 1:25 - loss: 7.7230 - accuracy: 0.4963
 2208/25000 [=>............................] - ETA: 1:24 - loss: 7.7222 - accuracy: 0.4964
 2240/25000 [=>............................] - ETA: 1:24 - loss: 7.6940 - accuracy: 0.4982
 2272/25000 [=>............................] - ETA: 1:24 - loss: 7.7341 - accuracy: 0.4956
 2304/25000 [=>............................] - ETA: 1:24 - loss: 7.6932 - accuracy: 0.4983
 2336/25000 [=>............................] - ETA: 1:24 - loss: 7.6535 - accuracy: 0.5009
 2368/25000 [=>............................] - ETA: 1:24 - loss: 7.6990 - accuracy: 0.4979
 2400/25000 [=>............................] - ETA: 1:23 - loss: 7.6858 - accuracy: 0.4988
 2432/25000 [=>............................] - ETA: 1:23 - loss: 7.6981 - accuracy: 0.4979
 2464/25000 [=>............................] - ETA: 1:23 - loss: 7.7040 - accuracy: 0.4976
 2496/25000 [=>............................] - ETA: 1:23 - loss: 7.7281 - accuracy: 0.4960
 2528/25000 [==>...........................] - ETA: 1:23 - loss: 7.7576 - accuracy: 0.4941
 2560/25000 [==>...........................] - ETA: 1:23 - loss: 7.7505 - accuracy: 0.4945
 2592/25000 [==>...........................] - ETA: 1:22 - loss: 7.7376 - accuracy: 0.4954
 2624/25000 [==>...........................] - ETA: 1:22 - loss: 7.7367 - accuracy: 0.4954
 2656/25000 [==>...........................] - ETA: 1:22 - loss: 7.7186 - accuracy: 0.4966
 2688/25000 [==>...........................] - ETA: 1:22 - loss: 7.7008 - accuracy: 0.4978
 2720/25000 [==>...........................] - ETA: 1:22 - loss: 7.7174 - accuracy: 0.4967
 2752/25000 [==>...........................] - ETA: 1:22 - loss: 7.7000 - accuracy: 0.4978
 2784/25000 [==>...........................] - ETA: 1:21 - loss: 7.6776 - accuracy: 0.4993
 2816/25000 [==>...........................] - ETA: 1:21 - loss: 7.6721 - accuracy: 0.4996
 2848/25000 [==>...........................] - ETA: 1:21 - loss: 7.6505 - accuracy: 0.5011
 2880/25000 [==>...........................] - ETA: 1:21 - loss: 7.6506 - accuracy: 0.5010
 2912/25000 [==>...........................] - ETA: 1:21 - loss: 7.6508 - accuracy: 0.5010
 2944/25000 [==>...........................] - ETA: 1:21 - loss: 7.6510 - accuracy: 0.5010
 2976/25000 [==>...........................] - ETA: 1:20 - loss: 7.6151 - accuracy: 0.5034
 3008/25000 [==>...........................] - ETA: 1:20 - loss: 7.6054 - accuracy: 0.5040
 3040/25000 [==>...........................] - ETA: 1:20 - loss: 7.6263 - accuracy: 0.5026
 3072/25000 [==>...........................] - ETA: 1:20 - loss: 7.6317 - accuracy: 0.5023
 3104/25000 [==>...........................] - ETA: 1:20 - loss: 7.6320 - accuracy: 0.5023
 3136/25000 [==>...........................] - ETA: 1:20 - loss: 7.6373 - accuracy: 0.5019
 3168/25000 [==>...........................] - ETA: 1:20 - loss: 7.6231 - accuracy: 0.5028
 3200/25000 [==>...........................] - ETA: 1:19 - loss: 7.6427 - accuracy: 0.5016
 3232/25000 [==>...........................] - ETA: 1:19 - loss: 7.6619 - accuracy: 0.5003
 3264/25000 [==>...........................] - ETA: 1:19 - loss: 7.6619 - accuracy: 0.5003
 3296/25000 [==>...........................] - ETA: 1:19 - loss: 7.6480 - accuracy: 0.5012
 3328/25000 [==>...........................] - ETA: 1:19 - loss: 7.6620 - accuracy: 0.5003
 3360/25000 [===>..........................] - ETA: 1:19 - loss: 7.6712 - accuracy: 0.4997
 3392/25000 [===>..........................] - ETA: 1:19 - loss: 7.6983 - accuracy: 0.4979
 3424/25000 [===>..........................] - ETA: 1:18 - loss: 7.6845 - accuracy: 0.4988
 3456/25000 [===>..........................] - ETA: 1:18 - loss: 7.6844 - accuracy: 0.4988
 3488/25000 [===>..........................] - ETA: 1:18 - loss: 7.6754 - accuracy: 0.4994
 3520/25000 [===>..........................] - ETA: 1:18 - loss: 7.6884 - accuracy: 0.4986
 3552/25000 [===>..........................] - ETA: 1:18 - loss: 7.7012 - accuracy: 0.4977
 3584/25000 [===>..........................] - ETA: 1:18 - loss: 7.7008 - accuracy: 0.4978
 3616/25000 [===>..........................] - ETA: 1:18 - loss: 7.7133 - accuracy: 0.4970
 3648/25000 [===>..........................] - ETA: 1:18 - loss: 7.7171 - accuracy: 0.4967
 3680/25000 [===>..........................] - ETA: 1:17 - loss: 7.7208 - accuracy: 0.4965
 3712/25000 [===>..........................] - ETA: 1:17 - loss: 7.7162 - accuracy: 0.4968
 3744/25000 [===>..........................] - ETA: 1:17 - loss: 7.7117 - accuracy: 0.4971
 3776/25000 [===>..........................] - ETA: 1:17 - loss: 7.7072 - accuracy: 0.4974
 3808/25000 [===>..........................] - ETA: 1:17 - loss: 7.6988 - accuracy: 0.4979
 3840/25000 [===>..........................] - ETA: 1:17 - loss: 7.7065 - accuracy: 0.4974
 3872/25000 [===>..........................] - ETA: 1:17 - loss: 7.7023 - accuracy: 0.4977
 3904/25000 [===>..........................] - ETA: 1:16 - loss: 7.6980 - accuracy: 0.4980
 3936/25000 [===>..........................] - ETA: 1:16 - loss: 7.6939 - accuracy: 0.4982
 3968/25000 [===>..........................] - ETA: 1:16 - loss: 7.6898 - accuracy: 0.4985
 4000/25000 [===>..........................] - ETA: 1:16 - loss: 7.6820 - accuracy: 0.4990
 4032/25000 [===>..........................] - ETA: 1:16 - loss: 7.6704 - accuracy: 0.4998
 4064/25000 [===>..........................] - ETA: 1:16 - loss: 7.6666 - accuracy: 0.5000
 4096/25000 [===>..........................] - ETA: 1:16 - loss: 7.6591 - accuracy: 0.5005
 4128/25000 [===>..........................] - ETA: 1:15 - loss: 7.6480 - accuracy: 0.5012
 4160/25000 [===>..........................] - ETA: 1:15 - loss: 7.6334 - accuracy: 0.5022
 4192/25000 [====>.........................] - ETA: 1:15 - loss: 7.6374 - accuracy: 0.5019
 4224/25000 [====>.........................] - ETA: 1:15 - loss: 7.6085 - accuracy: 0.5038
 4256/25000 [====>.........................] - ETA: 1:15 - loss: 7.6018 - accuracy: 0.5042
 4288/25000 [====>.........................] - ETA: 1:15 - loss: 7.6094 - accuracy: 0.5037
 4320/25000 [====>.........................] - ETA: 1:15 - loss: 7.6240 - accuracy: 0.5028
 4352/25000 [====>.........................] - ETA: 1:15 - loss: 7.6349 - accuracy: 0.5021
 4384/25000 [====>.........................] - ETA: 1:14 - loss: 7.6316 - accuracy: 0.5023
 4416/25000 [====>.........................] - ETA: 1:14 - loss: 7.6458 - accuracy: 0.5014
 4448/25000 [====>.........................] - ETA: 1:14 - loss: 7.6632 - accuracy: 0.5002
 4480/25000 [====>.........................] - ETA: 1:14 - loss: 7.6769 - accuracy: 0.4993
 4512/25000 [====>.........................] - ETA: 1:14 - loss: 7.6598 - accuracy: 0.5004
 4544/25000 [====>.........................] - ETA: 1:14 - loss: 7.6700 - accuracy: 0.4998
 4576/25000 [====>.........................] - ETA: 1:14 - loss: 7.6800 - accuracy: 0.4991
 4608/25000 [====>.........................] - ETA: 1:14 - loss: 7.6899 - accuracy: 0.4985
 4640/25000 [====>.........................] - ETA: 1:13 - loss: 7.6964 - accuracy: 0.4981
 4672/25000 [====>.........................] - ETA: 1:13 - loss: 7.6994 - accuracy: 0.4979
 4704/25000 [====>.........................] - ETA: 1:13 - loss: 7.6764 - accuracy: 0.4994
 4736/25000 [====>.........................] - ETA: 1:13 - loss: 7.6763 - accuracy: 0.4994
 4768/25000 [====>.........................] - ETA: 1:13 - loss: 7.6666 - accuracy: 0.5000
 4800/25000 [====>.........................] - ETA: 1:13 - loss: 7.6698 - accuracy: 0.4998
 4832/25000 [====>.........................] - ETA: 1:13 - loss: 7.6698 - accuracy: 0.4998
 4864/25000 [====>.........................] - ETA: 1:12 - loss: 7.6761 - accuracy: 0.4994
 4896/25000 [====>.........................] - ETA: 1:12 - loss: 7.6917 - accuracy: 0.4984
 4928/25000 [====>.........................] - ETA: 1:12 - loss: 7.7071 - accuracy: 0.4974
 4960/25000 [====>.........................] - ETA: 1:12 - loss: 7.7068 - accuracy: 0.4974
 4992/25000 [====>.........................] - ETA: 1:12 - loss: 7.7158 - accuracy: 0.4968
 5024/25000 [=====>........................] - ETA: 1:12 - loss: 7.7216 - accuracy: 0.4964
 5056/25000 [=====>........................] - ETA: 1:12 - loss: 7.7182 - accuracy: 0.4966
 5088/25000 [=====>........................] - ETA: 1:12 - loss: 7.7148 - accuracy: 0.4969
 5120/25000 [=====>........................] - ETA: 1:11 - loss: 7.7205 - accuracy: 0.4965
 5152/25000 [=====>........................] - ETA: 1:11 - loss: 7.7261 - accuracy: 0.4961
 5184/25000 [=====>........................] - ETA: 1:11 - loss: 7.7139 - accuracy: 0.4969
 5216/25000 [=====>........................] - ETA: 1:11 - loss: 7.7137 - accuracy: 0.4969
 5248/25000 [=====>........................] - ETA: 1:11 - loss: 7.7192 - accuracy: 0.4966
 5280/25000 [=====>........................] - ETA: 1:11 - loss: 7.7015 - accuracy: 0.4977
 5312/25000 [=====>........................] - ETA: 1:11 - loss: 7.7186 - accuracy: 0.4966
 5344/25000 [=====>........................] - ETA: 1:11 - loss: 7.7125 - accuracy: 0.4970
 5376/25000 [=====>........................] - ETA: 1:10 - loss: 7.7180 - accuracy: 0.4967
 5408/25000 [=====>........................] - ETA: 1:10 - loss: 7.7063 - accuracy: 0.4974
 5440/25000 [=====>........................] - ETA: 1:10 - loss: 7.7089 - accuracy: 0.4972
 5472/25000 [=====>........................] - ETA: 1:10 - loss: 7.7115 - accuracy: 0.4971
 5504/25000 [=====>........................] - ETA: 1:10 - loss: 7.7140 - accuracy: 0.4969
 5536/25000 [=====>........................] - ETA: 1:10 - loss: 7.7192 - accuracy: 0.4966
 5568/25000 [=====>........................] - ETA: 1:10 - loss: 7.7217 - accuracy: 0.4964
 5600/25000 [=====>........................] - ETA: 1:10 - loss: 7.7241 - accuracy: 0.4963
 5632/25000 [=====>........................] - ETA: 1:09 - loss: 7.7265 - accuracy: 0.4961
 5664/25000 [=====>........................] - ETA: 1:09 - loss: 7.7262 - accuracy: 0.4961
 5696/25000 [=====>........................] - ETA: 1:09 - loss: 7.7151 - accuracy: 0.4968
 5728/25000 [=====>........................] - ETA: 1:09 - loss: 7.7068 - accuracy: 0.4974
 5760/25000 [=====>........................] - ETA: 1:09 - loss: 7.7119 - accuracy: 0.4970
 5792/25000 [=====>........................] - ETA: 1:09 - loss: 7.7169 - accuracy: 0.4967
 5824/25000 [=====>........................] - ETA: 1:09 - loss: 7.7272 - accuracy: 0.4961
 5856/25000 [======>.......................] - ETA: 1:09 - loss: 7.7268 - accuracy: 0.4961
 5888/25000 [======>.......................] - ETA: 1:08 - loss: 7.7239 - accuracy: 0.4963
 5920/25000 [======>.......................] - ETA: 1:08 - loss: 7.7184 - accuracy: 0.4966
 5952/25000 [======>.......................] - ETA: 1:08 - loss: 7.7078 - accuracy: 0.4973
 5984/25000 [======>.......................] - ETA: 1:08 - loss: 7.7179 - accuracy: 0.4967
 6016/25000 [======>.......................] - ETA: 1:08 - loss: 7.7150 - accuracy: 0.4968
 6048/25000 [======>.......................] - ETA: 1:08 - loss: 7.7173 - accuracy: 0.4967
 6080/25000 [======>.......................] - ETA: 1:08 - loss: 7.7246 - accuracy: 0.4962
 6112/25000 [======>.......................] - ETA: 1:08 - loss: 7.7218 - accuracy: 0.4964
 6144/25000 [======>.......................] - ETA: 1:07 - loss: 7.7290 - accuracy: 0.4959
 6176/25000 [======>.......................] - ETA: 1:07 - loss: 7.7188 - accuracy: 0.4966
 6208/25000 [======>.......................] - ETA: 1:07 - loss: 7.7185 - accuracy: 0.4966
 6240/25000 [======>.......................] - ETA: 1:07 - loss: 7.7133 - accuracy: 0.4970
 6272/25000 [======>.......................] - ETA: 1:07 - loss: 7.7106 - accuracy: 0.4971
 6304/25000 [======>.......................] - ETA: 1:07 - loss: 7.7104 - accuracy: 0.4971
 6336/25000 [======>.......................] - ETA: 1:07 - loss: 7.7126 - accuracy: 0.4970
 6368/25000 [======>.......................] - ETA: 1:07 - loss: 7.7051 - accuracy: 0.4975
 6400/25000 [======>.......................] - ETA: 1:06 - loss: 7.7097 - accuracy: 0.4972
 6432/25000 [======>.......................] - ETA: 1:06 - loss: 7.7095 - accuracy: 0.4972
 6464/25000 [======>.......................] - ETA: 1:06 - loss: 7.7069 - accuracy: 0.4974
 6496/25000 [======>.......................] - ETA: 1:06 - loss: 7.6997 - accuracy: 0.4978
 6528/25000 [======>.......................] - ETA: 1:06 - loss: 7.6948 - accuracy: 0.4982
 6560/25000 [======>.......................] - ETA: 1:06 - loss: 7.6993 - accuracy: 0.4979
 6592/25000 [======>.......................] - ETA: 1:06 - loss: 7.7038 - accuracy: 0.4976
 6624/25000 [======>.......................] - ETA: 1:06 - loss: 7.6990 - accuracy: 0.4979
 6656/25000 [======>.......................] - ETA: 1:06 - loss: 7.6943 - accuracy: 0.4982
 6688/25000 [=======>......................] - ETA: 1:05 - loss: 7.6941 - accuracy: 0.4982
 6720/25000 [=======>......................] - ETA: 1:05 - loss: 7.6986 - accuracy: 0.4979
 6752/25000 [=======>......................] - ETA: 1:05 - loss: 7.7098 - accuracy: 0.4972
 6784/25000 [=======>......................] - ETA: 1:05 - loss: 7.7050 - accuracy: 0.4975
 6816/25000 [=======>......................] - ETA: 1:05 - loss: 7.7049 - accuracy: 0.4975
 6848/25000 [=======>......................] - ETA: 1:05 - loss: 7.7092 - accuracy: 0.4972
 6880/25000 [=======>......................] - ETA: 1:05 - loss: 7.7134 - accuracy: 0.4969
 6912/25000 [=======>......................] - ETA: 1:05 - loss: 7.7154 - accuracy: 0.4968
 6944/25000 [=======>......................] - ETA: 1:04 - loss: 7.7130 - accuracy: 0.4970
 6976/25000 [=======>......................] - ETA: 1:04 - loss: 7.6974 - accuracy: 0.4980
 7008/25000 [=======>......................] - ETA: 1:04 - loss: 7.6994 - accuracy: 0.4979
 7040/25000 [=======>......................] - ETA: 1:04 - loss: 7.7015 - accuracy: 0.4977
 7072/25000 [=======>......................] - ETA: 1:04 - loss: 7.6840 - accuracy: 0.4989
 7104/25000 [=======>......................] - ETA: 1:04 - loss: 7.6882 - accuracy: 0.4986
 7136/25000 [=======>......................] - ETA: 1:04 - loss: 7.6881 - accuracy: 0.4986
 7168/25000 [=======>......................] - ETA: 1:04 - loss: 7.6859 - accuracy: 0.4987
 7200/25000 [=======>......................] - ETA: 1:03 - loss: 7.6922 - accuracy: 0.4983
 7232/25000 [=======>......................] - ETA: 1:03 - loss: 7.6942 - accuracy: 0.4982
 7264/25000 [=======>......................] - ETA: 1:03 - loss: 7.6898 - accuracy: 0.4985
 7296/25000 [=======>......................] - ETA: 1:03 - loss: 7.7002 - accuracy: 0.4978
 7328/25000 [=======>......................] - ETA: 1:03 - loss: 7.7064 - accuracy: 0.4974
 7360/25000 [=======>......................] - ETA: 1:03 - loss: 7.7083 - accuracy: 0.4973
 7392/25000 [=======>......................] - ETA: 1:03 - loss: 7.6977 - accuracy: 0.4980
 7424/25000 [=======>......................] - ETA: 1:03 - loss: 7.6997 - accuracy: 0.4978
 7456/25000 [=======>......................] - ETA: 1:02 - loss: 7.6934 - accuracy: 0.4983
 7488/25000 [=======>......................] - ETA: 1:02 - loss: 7.6850 - accuracy: 0.4988
 7520/25000 [========>.....................] - ETA: 1:02 - loss: 7.6789 - accuracy: 0.4992
 7552/25000 [========>.....................] - ETA: 1:02 - loss: 7.6829 - accuracy: 0.4989
 7584/25000 [========>.....................] - ETA: 1:02 - loss: 7.6808 - accuracy: 0.4991
 7616/25000 [========>.....................] - ETA: 1:02 - loss: 7.6807 - accuracy: 0.4991
 7648/25000 [========>.....................] - ETA: 1:02 - loss: 7.6847 - accuracy: 0.4988
 7680/25000 [========>.....................] - ETA: 1:02 - loss: 7.6826 - accuracy: 0.4990
 7712/25000 [========>.....................] - ETA: 1:02 - loss: 7.6845 - accuracy: 0.4988
 7744/25000 [========>.....................] - ETA: 1:01 - loss: 7.6785 - accuracy: 0.4992
 7776/25000 [========>.....................] - ETA: 1:01 - loss: 7.6844 - accuracy: 0.4988
 7808/25000 [========>.....................] - ETA: 1:01 - loss: 7.6804 - accuracy: 0.4991
 7840/25000 [========>.....................] - ETA: 1:01 - loss: 7.6862 - accuracy: 0.4987
 7872/25000 [========>.....................] - ETA: 1:01 - loss: 7.6880 - accuracy: 0.4986
 7904/25000 [========>.....................] - ETA: 1:01 - loss: 7.6880 - accuracy: 0.4986
 7936/25000 [========>.....................] - ETA: 1:01 - loss: 7.6898 - accuracy: 0.4985
 7968/25000 [========>.....................] - ETA: 1:01 - loss: 7.6859 - accuracy: 0.4987
 8000/25000 [========>.....................] - ETA: 1:00 - loss: 7.6839 - accuracy: 0.4989
 8032/25000 [========>.....................] - ETA: 1:00 - loss: 7.6800 - accuracy: 0.4991
 8064/25000 [========>.....................] - ETA: 1:00 - loss: 7.6875 - accuracy: 0.4986
 8096/25000 [========>.....................] - ETA: 1:00 - loss: 7.6875 - accuracy: 0.4986
 8128/25000 [========>.....................] - ETA: 1:00 - loss: 7.6893 - accuracy: 0.4985
 8160/25000 [========>.....................] - ETA: 1:00 - loss: 7.6854 - accuracy: 0.4988
 8192/25000 [========>.....................] - ETA: 1:00 - loss: 7.6853 - accuracy: 0.4988
 8224/25000 [========>.....................] - ETA: 1:00 - loss: 7.6946 - accuracy: 0.4982
 8256/25000 [========>.....................] - ETA: 1:00 - loss: 7.6945 - accuracy: 0.4982
 8288/25000 [========>.....................] - ETA: 59s - loss: 7.6962 - accuracy: 0.4981 
 8320/25000 [========>.....................] - ETA: 59s - loss: 7.6924 - accuracy: 0.4983
 8352/25000 [=========>....................] - ETA: 59s - loss: 7.6942 - accuracy: 0.4982
 8384/25000 [=========>....................] - ETA: 59s - loss: 7.6922 - accuracy: 0.4983
 8416/25000 [=========>....................] - ETA: 59s - loss: 7.6994 - accuracy: 0.4979
 8448/25000 [=========>....................] - ETA: 59s - loss: 7.7047 - accuracy: 0.4975
 8480/25000 [=========>....................] - ETA: 59s - loss: 7.7046 - accuracy: 0.4975
 8512/25000 [=========>....................] - ETA: 59s - loss: 7.7062 - accuracy: 0.4974
 8544/25000 [=========>....................] - ETA: 58s - loss: 7.7007 - accuracy: 0.4978
 8576/25000 [=========>....................] - ETA: 58s - loss: 7.6988 - accuracy: 0.4979
 8608/25000 [=========>....................] - ETA: 58s - loss: 7.7040 - accuracy: 0.4976
 8640/25000 [=========>....................] - ETA: 58s - loss: 7.7057 - accuracy: 0.4975
 8672/25000 [=========>....................] - ETA: 58s - loss: 7.7020 - accuracy: 0.4977
 8704/25000 [=========>....................] - ETA: 58s - loss: 7.7036 - accuracy: 0.4976
 8736/25000 [=========>....................] - ETA: 58s - loss: 7.7070 - accuracy: 0.4974
 8768/25000 [=========>....................] - ETA: 58s - loss: 7.7051 - accuracy: 0.4975
 8800/25000 [=========>....................] - ETA: 57s - loss: 7.7015 - accuracy: 0.4977
 8832/25000 [=========>....................] - ETA: 57s - loss: 7.7048 - accuracy: 0.4975
 8864/25000 [=========>....................] - ETA: 57s - loss: 7.6908 - accuracy: 0.4984
 8896/25000 [=========>....................] - ETA: 57s - loss: 7.6976 - accuracy: 0.4980
 8928/25000 [=========>....................] - ETA: 57s - loss: 7.6907 - accuracy: 0.4984
 8960/25000 [=========>....................] - ETA: 57s - loss: 7.6854 - accuracy: 0.4988
 8992/25000 [=========>....................] - ETA: 57s - loss: 7.6854 - accuracy: 0.4988
 9024/25000 [=========>....................] - ETA: 57s - loss: 7.6836 - accuracy: 0.4989
 9056/25000 [=========>....................] - ETA: 57s - loss: 7.6802 - accuracy: 0.4991
 9088/25000 [=========>....................] - ETA: 56s - loss: 7.6666 - accuracy: 0.5000
 9120/25000 [=========>....................] - ETA: 56s - loss: 7.6700 - accuracy: 0.4998
 9152/25000 [=========>....................] - ETA: 56s - loss: 7.6700 - accuracy: 0.4998
 9184/25000 [==========>...................] - ETA: 56s - loss: 7.6616 - accuracy: 0.5003
 9216/25000 [==========>...................] - ETA: 56s - loss: 7.6533 - accuracy: 0.5009
 9248/25000 [==========>...................] - ETA: 56s - loss: 7.6567 - accuracy: 0.5006
 9280/25000 [==========>...................] - ETA: 56s - loss: 7.6584 - accuracy: 0.5005
 9312/25000 [==========>...................] - ETA: 56s - loss: 7.6518 - accuracy: 0.5010
 9344/25000 [==========>...................] - ETA: 55s - loss: 7.6519 - accuracy: 0.5010
 9376/25000 [==========>...................] - ETA: 55s - loss: 7.6535 - accuracy: 0.5009
 9408/25000 [==========>...................] - ETA: 55s - loss: 7.6536 - accuracy: 0.5009
 9440/25000 [==========>...................] - ETA: 55s - loss: 7.6520 - accuracy: 0.5010
 9472/25000 [==========>...................] - ETA: 55s - loss: 7.6456 - accuracy: 0.5014
 9504/25000 [==========>...................] - ETA: 55s - loss: 7.6424 - accuracy: 0.5016
 9536/25000 [==========>...................] - ETA: 55s - loss: 7.6377 - accuracy: 0.5019
 9568/25000 [==========>...................] - ETA: 55s - loss: 7.6410 - accuracy: 0.5017
 9600/25000 [==========>...................] - ETA: 55s - loss: 7.6395 - accuracy: 0.5018
 9632/25000 [==========>...................] - ETA: 54s - loss: 7.6443 - accuracy: 0.5015
 9664/25000 [==========>...................] - ETA: 54s - loss: 7.6396 - accuracy: 0.5018
 9696/25000 [==========>...................] - ETA: 54s - loss: 7.6429 - accuracy: 0.5015
 9728/25000 [==========>...................] - ETA: 54s - loss: 7.6414 - accuracy: 0.5016
 9760/25000 [==========>...................] - ETA: 54s - loss: 7.6431 - accuracy: 0.5015
 9792/25000 [==========>...................] - ETA: 54s - loss: 7.6416 - accuracy: 0.5016
 9824/25000 [==========>...................] - ETA: 54s - loss: 7.6448 - accuracy: 0.5014
 9856/25000 [==========>...................] - ETA: 54s - loss: 7.6433 - accuracy: 0.5015
 9888/25000 [==========>...................] - ETA: 53s - loss: 7.6387 - accuracy: 0.5018
 9920/25000 [==========>...................] - ETA: 53s - loss: 7.6450 - accuracy: 0.5014
 9952/25000 [==========>...................] - ETA: 53s - loss: 7.6574 - accuracy: 0.5006
 9984/25000 [==========>...................] - ETA: 53s - loss: 7.6666 - accuracy: 0.5000
10016/25000 [===========>..................] - ETA: 53s - loss: 7.6651 - accuracy: 0.5001
10048/25000 [===========>..................] - ETA: 53s - loss: 7.6620 - accuracy: 0.5003
10080/25000 [===========>..................] - ETA: 53s - loss: 7.6605 - accuracy: 0.5004
10112/25000 [===========>..................] - ETA: 53s - loss: 7.6727 - accuracy: 0.4996
10144/25000 [===========>..................] - ETA: 53s - loss: 7.6712 - accuracy: 0.4997
10176/25000 [===========>..................] - ETA: 52s - loss: 7.6742 - accuracy: 0.4995
10208/25000 [===========>..................] - ETA: 52s - loss: 7.6726 - accuracy: 0.4996
10240/25000 [===========>..................] - ETA: 52s - loss: 7.6756 - accuracy: 0.4994
10272/25000 [===========>..................] - ETA: 52s - loss: 7.6681 - accuracy: 0.4999
10304/25000 [===========>..................] - ETA: 52s - loss: 7.6711 - accuracy: 0.4997
10336/25000 [===========>..................] - ETA: 52s - loss: 7.6711 - accuracy: 0.4997
10368/25000 [===========>..................] - ETA: 52s - loss: 7.6651 - accuracy: 0.5001
10400/25000 [===========>..................] - ETA: 52s - loss: 7.6637 - accuracy: 0.5002
10432/25000 [===========>..................] - ETA: 51s - loss: 7.6696 - accuracy: 0.4998
10464/25000 [===========>..................] - ETA: 51s - loss: 7.6783 - accuracy: 0.4992
10496/25000 [===========>..................] - ETA: 51s - loss: 7.6827 - accuracy: 0.4990
10528/25000 [===========>..................] - ETA: 51s - loss: 7.6856 - accuracy: 0.4988
10560/25000 [===========>..................] - ETA: 51s - loss: 7.6840 - accuracy: 0.4989
10592/25000 [===========>..................] - ETA: 51s - loss: 7.6941 - accuracy: 0.4982
10624/25000 [===========>..................] - ETA: 51s - loss: 7.6955 - accuracy: 0.4981
10656/25000 [===========>..................] - ETA: 51s - loss: 7.6983 - accuracy: 0.4979
10688/25000 [===========>..................] - ETA: 51s - loss: 7.6924 - accuracy: 0.4983
10720/25000 [===========>..................] - ETA: 50s - loss: 7.6967 - accuracy: 0.4980
10752/25000 [===========>..................] - ETA: 50s - loss: 7.6909 - accuracy: 0.4984
10784/25000 [===========>..................] - ETA: 50s - loss: 7.6851 - accuracy: 0.4988
10816/25000 [===========>..................] - ETA: 50s - loss: 7.6879 - accuracy: 0.4986
10848/25000 [============>.................] - ETA: 50s - loss: 7.6822 - accuracy: 0.4990
10880/25000 [============>.................] - ETA: 50s - loss: 7.6892 - accuracy: 0.4985
10912/25000 [============>.................] - ETA: 50s - loss: 7.6849 - accuracy: 0.4988
10944/25000 [============>.................] - ETA: 50s - loss: 7.6764 - accuracy: 0.4994
10976/25000 [============>.................] - ETA: 50s - loss: 7.6764 - accuracy: 0.4994
11008/25000 [============>.................] - ETA: 49s - loss: 7.6736 - accuracy: 0.4995
11040/25000 [============>.................] - ETA: 49s - loss: 7.6750 - accuracy: 0.4995
11072/25000 [============>.................] - ETA: 49s - loss: 7.6722 - accuracy: 0.4996
11104/25000 [============>.................] - ETA: 49s - loss: 7.6708 - accuracy: 0.4997
11136/25000 [============>.................] - ETA: 49s - loss: 7.6666 - accuracy: 0.5000
11168/25000 [============>.................] - ETA: 49s - loss: 7.6611 - accuracy: 0.5004
11200/25000 [============>.................] - ETA: 49s - loss: 7.6639 - accuracy: 0.5002
11232/25000 [============>.................] - ETA: 49s - loss: 7.6639 - accuracy: 0.5002
11264/25000 [============>.................] - ETA: 48s - loss: 7.6625 - accuracy: 0.5003
11296/25000 [============>.................] - ETA: 48s - loss: 7.6612 - accuracy: 0.5004
11328/25000 [============>.................] - ETA: 48s - loss: 7.6558 - accuracy: 0.5007
11360/25000 [============>.................] - ETA: 48s - loss: 7.6585 - accuracy: 0.5005
11392/25000 [============>.................] - ETA: 48s - loss: 7.6572 - accuracy: 0.5006
11424/25000 [============>.................] - ETA: 48s - loss: 7.6545 - accuracy: 0.5008
11456/25000 [============>.................] - ETA: 48s - loss: 7.6546 - accuracy: 0.5008
11488/25000 [============>.................] - ETA: 48s - loss: 7.6519 - accuracy: 0.5010
11520/25000 [============>.................] - ETA: 48s - loss: 7.6506 - accuracy: 0.5010
11552/25000 [============>.................] - ETA: 47s - loss: 7.6507 - accuracy: 0.5010
11584/25000 [============>.................] - ETA: 47s - loss: 7.6560 - accuracy: 0.5007
11616/25000 [============>.................] - ETA: 47s - loss: 7.6613 - accuracy: 0.5003
11648/25000 [============>.................] - ETA: 47s - loss: 7.6587 - accuracy: 0.5005
11680/25000 [=============>................] - ETA: 47s - loss: 7.6587 - accuracy: 0.5005
11712/25000 [=============>................] - ETA: 47s - loss: 7.6575 - accuracy: 0.5006
11744/25000 [=============>................] - ETA: 47s - loss: 7.6666 - accuracy: 0.5000
11776/25000 [=============>................] - ETA: 47s - loss: 7.6666 - accuracy: 0.5000
11808/25000 [=============>................] - ETA: 47s - loss: 7.6679 - accuracy: 0.4999
11840/25000 [=============>................] - ETA: 46s - loss: 7.6601 - accuracy: 0.5004
11872/25000 [=============>................] - ETA: 46s - loss: 7.6627 - accuracy: 0.5003
11904/25000 [=============>................] - ETA: 46s - loss: 7.6653 - accuracy: 0.5001
11936/25000 [=============>................] - ETA: 46s - loss: 7.6679 - accuracy: 0.4999
11968/25000 [=============>................] - ETA: 46s - loss: 7.6717 - accuracy: 0.4997
12000/25000 [=============>................] - ETA: 46s - loss: 7.6705 - accuracy: 0.4997
12032/25000 [=============>................] - ETA: 46s - loss: 7.6704 - accuracy: 0.4998
12064/25000 [=============>................] - ETA: 46s - loss: 7.6704 - accuracy: 0.4998
12096/25000 [=============>................] - ETA: 45s - loss: 7.6704 - accuracy: 0.4998
12128/25000 [=============>................] - ETA: 45s - loss: 7.6704 - accuracy: 0.4998
12160/25000 [=============>................] - ETA: 45s - loss: 7.6704 - accuracy: 0.4998
12192/25000 [=============>................] - ETA: 45s - loss: 7.6717 - accuracy: 0.4997
12224/25000 [=============>................] - ETA: 45s - loss: 7.6779 - accuracy: 0.4993
12256/25000 [=============>................] - ETA: 45s - loss: 7.6791 - accuracy: 0.4992
12288/25000 [=============>................] - ETA: 45s - loss: 7.6778 - accuracy: 0.4993
12320/25000 [=============>................] - ETA: 45s - loss: 7.6753 - accuracy: 0.4994
12352/25000 [=============>................] - ETA: 45s - loss: 7.6753 - accuracy: 0.4994
12384/25000 [=============>................] - ETA: 44s - loss: 7.6728 - accuracy: 0.4996
12416/25000 [=============>................] - ETA: 44s - loss: 7.6666 - accuracy: 0.5000
12448/25000 [=============>................] - ETA: 44s - loss: 7.6703 - accuracy: 0.4998
12480/25000 [=============>................] - ETA: 44s - loss: 7.6691 - accuracy: 0.4998
12512/25000 [==============>...............] - ETA: 44s - loss: 7.6691 - accuracy: 0.4998
12544/25000 [==============>...............] - ETA: 44s - loss: 7.6776 - accuracy: 0.4993
12576/25000 [==============>...............] - ETA: 44s - loss: 7.6752 - accuracy: 0.4994
12608/25000 [==============>...............] - ETA: 44s - loss: 7.6776 - accuracy: 0.4993
12640/25000 [==============>...............] - ETA: 43s - loss: 7.6763 - accuracy: 0.4994
12672/25000 [==============>...............] - ETA: 43s - loss: 7.6763 - accuracy: 0.4994
12704/25000 [==============>...............] - ETA: 43s - loss: 7.6739 - accuracy: 0.4995
12736/25000 [==============>...............] - ETA: 43s - loss: 7.6702 - accuracy: 0.4998
12768/25000 [==============>...............] - ETA: 43s - loss: 7.6726 - accuracy: 0.4996
12800/25000 [==============>...............] - ETA: 43s - loss: 7.6714 - accuracy: 0.4997
12832/25000 [==============>...............] - ETA: 43s - loss: 7.6642 - accuracy: 0.5002
12864/25000 [==============>...............] - ETA: 43s - loss: 7.6654 - accuracy: 0.5001
12896/25000 [==============>...............] - ETA: 43s - loss: 7.6714 - accuracy: 0.4997
12928/25000 [==============>...............] - ETA: 42s - loss: 7.6678 - accuracy: 0.4999
12960/25000 [==============>...............] - ETA: 42s - loss: 7.6654 - accuracy: 0.5001
12992/25000 [==============>...............] - ETA: 42s - loss: 7.6643 - accuracy: 0.5002
13024/25000 [==============>...............] - ETA: 42s - loss: 7.6654 - accuracy: 0.5001
13056/25000 [==============>...............] - ETA: 42s - loss: 7.6607 - accuracy: 0.5004
13088/25000 [==============>...............] - ETA: 42s - loss: 7.6584 - accuracy: 0.5005
13120/25000 [==============>...............] - ETA: 42s - loss: 7.6549 - accuracy: 0.5008
13152/25000 [==============>...............] - ETA: 42s - loss: 7.6526 - accuracy: 0.5009
13184/25000 [==============>...............] - ETA: 42s - loss: 7.6550 - accuracy: 0.5008
13216/25000 [==============>...............] - ETA: 41s - loss: 7.6597 - accuracy: 0.5005
13248/25000 [==============>...............] - ETA: 41s - loss: 7.6608 - accuracy: 0.5004
13280/25000 [==============>...............] - ETA: 41s - loss: 7.6562 - accuracy: 0.5007
13312/25000 [==============>...............] - ETA: 41s - loss: 7.6539 - accuracy: 0.5008
13344/25000 [===============>..............] - ETA: 41s - loss: 7.6528 - accuracy: 0.5009
13376/25000 [===============>..............] - ETA: 41s - loss: 7.6517 - accuracy: 0.5010
13408/25000 [===============>..............] - ETA: 41s - loss: 7.6529 - accuracy: 0.5009
13440/25000 [===============>..............] - ETA: 41s - loss: 7.6552 - accuracy: 0.5007
13472/25000 [===============>..............] - ETA: 41s - loss: 7.6530 - accuracy: 0.5009
13504/25000 [===============>..............] - ETA: 40s - loss: 7.6530 - accuracy: 0.5009
13536/25000 [===============>..............] - ETA: 40s - loss: 7.6485 - accuracy: 0.5012
13568/25000 [===============>..............] - ETA: 40s - loss: 7.6485 - accuracy: 0.5012
13600/25000 [===============>..............] - ETA: 40s - loss: 7.6486 - accuracy: 0.5012
13632/25000 [===============>..............] - ETA: 40s - loss: 7.6531 - accuracy: 0.5009
13664/25000 [===============>..............] - ETA: 40s - loss: 7.6543 - accuracy: 0.5008
13696/25000 [===============>..............] - ETA: 40s - loss: 7.6554 - accuracy: 0.5007
13728/25000 [===============>..............] - ETA: 40s - loss: 7.6532 - accuracy: 0.5009
13760/25000 [===============>..............] - ETA: 39s - loss: 7.6499 - accuracy: 0.5011
13792/25000 [===============>..............] - ETA: 39s - loss: 7.6511 - accuracy: 0.5010
13824/25000 [===============>..............] - ETA: 39s - loss: 7.6444 - accuracy: 0.5014
13856/25000 [===============>..............] - ETA: 39s - loss: 7.6456 - accuracy: 0.5014
13888/25000 [===============>..............] - ETA: 39s - loss: 7.6423 - accuracy: 0.5016
13920/25000 [===============>..............] - ETA: 39s - loss: 7.6424 - accuracy: 0.5016
13952/25000 [===============>..............] - ETA: 39s - loss: 7.6435 - accuracy: 0.5015
13984/25000 [===============>..............] - ETA: 39s - loss: 7.6425 - accuracy: 0.5016
14016/25000 [===============>..............] - ETA: 39s - loss: 7.6382 - accuracy: 0.5019
14048/25000 [===============>..............] - ETA: 38s - loss: 7.6339 - accuracy: 0.5021
14080/25000 [===============>..............] - ETA: 38s - loss: 7.6372 - accuracy: 0.5019
14112/25000 [===============>..............] - ETA: 38s - loss: 7.6405 - accuracy: 0.5017
14144/25000 [===============>..............] - ETA: 38s - loss: 7.6395 - accuracy: 0.5018
14176/25000 [================>.............] - ETA: 38s - loss: 7.6363 - accuracy: 0.5020
14208/25000 [================>.............] - ETA: 38s - loss: 7.6321 - accuracy: 0.5023
14240/25000 [================>.............] - ETA: 38s - loss: 7.6343 - accuracy: 0.5021
14272/25000 [================>.............] - ETA: 38s - loss: 7.6301 - accuracy: 0.5024
14304/25000 [================>.............] - ETA: 38s - loss: 7.6291 - accuracy: 0.5024
14336/25000 [================>.............] - ETA: 37s - loss: 7.6292 - accuracy: 0.5024
14368/25000 [================>.............] - ETA: 37s - loss: 7.6303 - accuracy: 0.5024
14400/25000 [================>.............] - ETA: 37s - loss: 7.6347 - accuracy: 0.5021
14432/25000 [================>.............] - ETA: 37s - loss: 7.6316 - accuracy: 0.5023
14464/25000 [================>.............] - ETA: 37s - loss: 7.6316 - accuracy: 0.5023
14496/25000 [================>.............] - ETA: 37s - loss: 7.6338 - accuracy: 0.5021
14528/25000 [================>.............] - ETA: 37s - loss: 7.6402 - accuracy: 0.5017
14560/25000 [================>.............] - ETA: 37s - loss: 7.6350 - accuracy: 0.5021
14592/25000 [================>.............] - ETA: 37s - loss: 7.6340 - accuracy: 0.5021
14624/25000 [================>.............] - ETA: 36s - loss: 7.6352 - accuracy: 0.5021
14656/25000 [================>.............] - ETA: 36s - loss: 7.6384 - accuracy: 0.5018
14688/25000 [================>.............] - ETA: 36s - loss: 7.6395 - accuracy: 0.5018
14720/25000 [================>.............] - ETA: 36s - loss: 7.6447 - accuracy: 0.5014
14752/25000 [================>.............] - ETA: 36s - loss: 7.6406 - accuracy: 0.5017
14784/25000 [================>.............] - ETA: 36s - loss: 7.6407 - accuracy: 0.5017
14816/25000 [================>.............] - ETA: 36s - loss: 7.6470 - accuracy: 0.5013
14848/25000 [================>.............] - ETA: 36s - loss: 7.6460 - accuracy: 0.5013
14880/25000 [================>.............] - ETA: 35s - loss: 7.6522 - accuracy: 0.5009
14912/25000 [================>.............] - ETA: 35s - loss: 7.6563 - accuracy: 0.5007
14944/25000 [================>.............] - ETA: 35s - loss: 7.6584 - accuracy: 0.5005
14976/25000 [================>.............] - ETA: 35s - loss: 7.6615 - accuracy: 0.5003
15008/25000 [=================>............] - ETA: 35s - loss: 7.6584 - accuracy: 0.5005
15040/25000 [=================>............] - ETA: 35s - loss: 7.6585 - accuracy: 0.5005
15072/25000 [=================>............] - ETA: 35s - loss: 7.6575 - accuracy: 0.5006
15104/25000 [=================>............] - ETA: 35s - loss: 7.6565 - accuracy: 0.5007
15136/25000 [=================>............] - ETA: 35s - loss: 7.6565 - accuracy: 0.5007
15168/25000 [=================>............] - ETA: 34s - loss: 7.6575 - accuracy: 0.5006
15200/25000 [=================>............] - ETA: 34s - loss: 7.6596 - accuracy: 0.5005
15232/25000 [=================>............] - ETA: 34s - loss: 7.6566 - accuracy: 0.5007
15264/25000 [=================>............] - ETA: 34s - loss: 7.6546 - accuracy: 0.5008
15296/25000 [=================>............] - ETA: 34s - loss: 7.6526 - accuracy: 0.5009
15328/25000 [=================>............] - ETA: 34s - loss: 7.6506 - accuracy: 0.5010
15360/25000 [=================>............] - ETA: 34s - loss: 7.6467 - accuracy: 0.5013
15392/25000 [=================>............] - ETA: 34s - loss: 7.6487 - accuracy: 0.5012
15424/25000 [=================>............] - ETA: 34s - loss: 7.6467 - accuracy: 0.5013
15456/25000 [=================>............] - ETA: 33s - loss: 7.6498 - accuracy: 0.5011
15488/25000 [=================>............] - ETA: 33s - loss: 7.6478 - accuracy: 0.5012
15520/25000 [=================>............] - ETA: 33s - loss: 7.6478 - accuracy: 0.5012
15552/25000 [=================>............] - ETA: 33s - loss: 7.6499 - accuracy: 0.5011
15584/25000 [=================>............] - ETA: 33s - loss: 7.6499 - accuracy: 0.5011
15616/25000 [=================>............] - ETA: 33s - loss: 7.6509 - accuracy: 0.5010
15648/25000 [=================>............] - ETA: 33s - loss: 7.6509 - accuracy: 0.5010
15680/25000 [=================>............] - ETA: 33s - loss: 7.6510 - accuracy: 0.5010
15712/25000 [=================>............] - ETA: 33s - loss: 7.6471 - accuracy: 0.5013
15744/25000 [=================>............] - ETA: 32s - loss: 7.6491 - accuracy: 0.5011
15776/25000 [=================>............] - ETA: 32s - loss: 7.6482 - accuracy: 0.5012
15808/25000 [=================>............] - ETA: 32s - loss: 7.6492 - accuracy: 0.5011
15840/25000 [==================>...........] - ETA: 32s - loss: 7.6521 - accuracy: 0.5009
15872/25000 [==================>...........] - ETA: 32s - loss: 7.6502 - accuracy: 0.5011
15904/25000 [==================>...........] - ETA: 32s - loss: 7.6483 - accuracy: 0.5012
15936/25000 [==================>...........] - ETA: 32s - loss: 7.6464 - accuracy: 0.5013
15968/25000 [==================>...........] - ETA: 32s - loss: 7.6465 - accuracy: 0.5013
16000/25000 [==================>...........] - ETA: 31s - loss: 7.6484 - accuracy: 0.5012
16032/25000 [==================>...........] - ETA: 31s - loss: 7.6504 - accuracy: 0.5011
16064/25000 [==================>...........] - ETA: 31s - loss: 7.6475 - accuracy: 0.5012
16096/25000 [==================>...........] - ETA: 31s - loss: 7.6542 - accuracy: 0.5008
16128/25000 [==================>...........] - ETA: 31s - loss: 7.6552 - accuracy: 0.5007
16160/25000 [==================>...........] - ETA: 31s - loss: 7.6600 - accuracy: 0.5004
16192/25000 [==================>...........] - ETA: 31s - loss: 7.6581 - accuracy: 0.5006
16224/25000 [==================>...........] - ETA: 31s - loss: 7.6609 - accuracy: 0.5004
16256/25000 [==================>...........] - ETA: 31s - loss: 7.6572 - accuracy: 0.5006
16288/25000 [==================>...........] - ETA: 30s - loss: 7.6600 - accuracy: 0.5004
16320/25000 [==================>...........] - ETA: 30s - loss: 7.6600 - accuracy: 0.5004
16352/25000 [==================>...........] - ETA: 30s - loss: 7.6619 - accuracy: 0.5003
16384/25000 [==================>...........] - ETA: 30s - loss: 7.6619 - accuracy: 0.5003
16416/25000 [==================>...........] - ETA: 30s - loss: 7.6591 - accuracy: 0.5005
16448/25000 [==================>...........] - ETA: 30s - loss: 7.6573 - accuracy: 0.5006
16480/25000 [==================>...........] - ETA: 30s - loss: 7.6555 - accuracy: 0.5007
16512/25000 [==================>...........] - ETA: 30s - loss: 7.6508 - accuracy: 0.5010
16544/25000 [==================>...........] - ETA: 30s - loss: 7.6481 - accuracy: 0.5012
16576/25000 [==================>...........] - ETA: 29s - loss: 7.6490 - accuracy: 0.5011
16608/25000 [==================>...........] - ETA: 29s - loss: 7.6482 - accuracy: 0.5012
16640/25000 [==================>...........] - ETA: 29s - loss: 7.6473 - accuracy: 0.5013
16672/25000 [===================>..........] - ETA: 29s - loss: 7.6445 - accuracy: 0.5014
16704/25000 [===================>..........] - ETA: 29s - loss: 7.6428 - accuracy: 0.5016
16736/25000 [===================>..........] - ETA: 29s - loss: 7.6446 - accuracy: 0.5014
16768/25000 [===================>..........] - ETA: 29s - loss: 7.6447 - accuracy: 0.5014
16800/25000 [===================>..........] - ETA: 29s - loss: 7.6411 - accuracy: 0.5017
16832/25000 [===================>..........] - ETA: 29s - loss: 7.6420 - accuracy: 0.5016
16864/25000 [===================>..........] - ETA: 28s - loss: 7.6366 - accuracy: 0.5020
16896/25000 [===================>..........] - ETA: 28s - loss: 7.6394 - accuracy: 0.5018
16928/25000 [===================>..........] - ETA: 28s - loss: 7.6422 - accuracy: 0.5016
16960/25000 [===================>..........] - ETA: 28s - loss: 7.6431 - accuracy: 0.5015
16992/25000 [===================>..........] - ETA: 28s - loss: 7.6459 - accuracy: 0.5014
17024/25000 [===================>..........] - ETA: 28s - loss: 7.6432 - accuracy: 0.5015
17056/25000 [===================>..........] - ETA: 28s - loss: 7.6477 - accuracy: 0.5012
17088/25000 [===================>..........] - ETA: 28s - loss: 7.6460 - accuracy: 0.5013
17120/25000 [===================>..........] - ETA: 27s - loss: 7.6460 - accuracy: 0.5013
17152/25000 [===================>..........] - ETA: 27s - loss: 7.6496 - accuracy: 0.5011
17184/25000 [===================>..........] - ETA: 27s - loss: 7.6506 - accuracy: 0.5010
17216/25000 [===================>..........] - ETA: 27s - loss: 7.6497 - accuracy: 0.5011
17248/25000 [===================>..........] - ETA: 27s - loss: 7.6471 - accuracy: 0.5013
17280/25000 [===================>..........] - ETA: 27s - loss: 7.6462 - accuracy: 0.5013
17312/25000 [===================>..........] - ETA: 27s - loss: 7.6462 - accuracy: 0.5013
17344/25000 [===================>..........] - ETA: 27s - loss: 7.6410 - accuracy: 0.5017
17376/25000 [===================>..........] - ETA: 27s - loss: 7.6393 - accuracy: 0.5018
17408/25000 [===================>..........] - ETA: 26s - loss: 7.6349 - accuracy: 0.5021
17440/25000 [===================>..........] - ETA: 26s - loss: 7.6341 - accuracy: 0.5021
17472/25000 [===================>..........] - ETA: 26s - loss: 7.6298 - accuracy: 0.5024
17504/25000 [====================>.........] - ETA: 26s - loss: 7.6298 - accuracy: 0.5024
17536/25000 [====================>.........] - ETA: 26s - loss: 7.6273 - accuracy: 0.5026
17568/25000 [====================>.........] - ETA: 26s - loss: 7.6256 - accuracy: 0.5027
17600/25000 [====================>.........] - ETA: 26s - loss: 7.6274 - accuracy: 0.5026
17632/25000 [====================>.........] - ETA: 26s - loss: 7.6275 - accuracy: 0.5026
17664/25000 [====================>.........] - ETA: 26s - loss: 7.6276 - accuracy: 0.5025
17696/25000 [====================>.........] - ETA: 25s - loss: 7.6259 - accuracy: 0.5027
17728/25000 [====================>.........] - ETA: 25s - loss: 7.6260 - accuracy: 0.5027
17760/25000 [====================>.........] - ETA: 25s - loss: 7.6260 - accuracy: 0.5026
17792/25000 [====================>.........] - ETA: 25s - loss: 7.6244 - accuracy: 0.5028
17824/25000 [====================>.........] - ETA: 25s - loss: 7.6210 - accuracy: 0.5030
17856/25000 [====================>.........] - ETA: 25s - loss: 7.6228 - accuracy: 0.5029
17888/25000 [====================>.........] - ETA: 25s - loss: 7.6195 - accuracy: 0.5031
17920/25000 [====================>.........] - ETA: 25s - loss: 7.6204 - accuracy: 0.5030
17952/25000 [====================>.........] - ETA: 25s - loss: 7.6196 - accuracy: 0.5031
17984/25000 [====================>.........] - ETA: 24s - loss: 7.6240 - accuracy: 0.5028
18016/25000 [====================>.........] - ETA: 24s - loss: 7.6275 - accuracy: 0.5026
18048/25000 [====================>.........] - ETA: 24s - loss: 7.6258 - accuracy: 0.5027
18080/25000 [====================>.........] - ETA: 24s - loss: 7.6276 - accuracy: 0.5025
18112/25000 [====================>.........] - ETA: 24s - loss: 7.6277 - accuracy: 0.5025
18144/25000 [====================>.........] - ETA: 24s - loss: 7.6235 - accuracy: 0.5028
18176/25000 [====================>.........] - ETA: 24s - loss: 7.6228 - accuracy: 0.5029
18208/25000 [====================>.........] - ETA: 24s - loss: 7.6228 - accuracy: 0.5029
18240/25000 [====================>.........] - ETA: 24s - loss: 7.6263 - accuracy: 0.5026
18272/25000 [====================>.........] - ETA: 23s - loss: 7.6247 - accuracy: 0.5027
18304/25000 [====================>.........] - ETA: 23s - loss: 7.6256 - accuracy: 0.5027
18336/25000 [=====================>........] - ETA: 23s - loss: 7.6256 - accuracy: 0.5027
18368/25000 [=====================>........] - ETA: 23s - loss: 7.6232 - accuracy: 0.5028
18400/25000 [=====================>........] - ETA: 23s - loss: 7.6250 - accuracy: 0.5027
18432/25000 [=====================>........] - ETA: 23s - loss: 7.6250 - accuracy: 0.5027
18464/25000 [=====================>........] - ETA: 23s - loss: 7.6243 - accuracy: 0.5028
18496/25000 [=====================>........] - ETA: 23s - loss: 7.6202 - accuracy: 0.5030
18528/25000 [=====================>........] - ETA: 22s - loss: 7.6170 - accuracy: 0.5032
18560/25000 [=====================>........] - ETA: 22s - loss: 7.6195 - accuracy: 0.5031
18592/25000 [=====================>........] - ETA: 22s - loss: 7.6221 - accuracy: 0.5029
18624/25000 [=====================>........] - ETA: 22s - loss: 7.6213 - accuracy: 0.5030
18656/25000 [=====================>........] - ETA: 22s - loss: 7.6214 - accuracy: 0.5029
18688/25000 [=====================>........] - ETA: 22s - loss: 7.6199 - accuracy: 0.5031
18720/25000 [=====================>........] - ETA: 22s - loss: 7.6199 - accuracy: 0.5030
18752/25000 [=====================>........] - ETA: 22s - loss: 7.6208 - accuracy: 0.5030
18784/25000 [=====================>........] - ETA: 22s - loss: 7.6242 - accuracy: 0.5028
18816/25000 [=====================>........] - ETA: 21s - loss: 7.6226 - accuracy: 0.5029
18848/25000 [=====================>........] - ETA: 21s - loss: 7.6211 - accuracy: 0.5030
18880/25000 [=====================>........] - ETA: 21s - loss: 7.6203 - accuracy: 0.5030
18912/25000 [=====================>........] - ETA: 21s - loss: 7.6196 - accuracy: 0.5031
18944/25000 [=====================>........] - ETA: 21s - loss: 7.6221 - accuracy: 0.5029
18976/25000 [=====================>........] - ETA: 21s - loss: 7.6254 - accuracy: 0.5027
19008/25000 [=====================>........] - ETA: 21s - loss: 7.6255 - accuracy: 0.5027
19040/25000 [=====================>........] - ETA: 21s - loss: 7.6280 - accuracy: 0.5025
19072/25000 [=====================>........] - ETA: 21s - loss: 7.6280 - accuracy: 0.5025
19104/25000 [=====================>........] - ETA: 20s - loss: 7.6273 - accuracy: 0.5026
19136/25000 [=====================>........] - ETA: 20s - loss: 7.6266 - accuracy: 0.5026
19168/25000 [======================>.......] - ETA: 20s - loss: 7.6266 - accuracy: 0.5026
19200/25000 [======================>.......] - ETA: 20s - loss: 7.6251 - accuracy: 0.5027
19232/25000 [======================>.......] - ETA: 20s - loss: 7.6284 - accuracy: 0.5025
19264/25000 [======================>.......] - ETA: 20s - loss: 7.6268 - accuracy: 0.5026
19296/25000 [======================>.......] - ETA: 20s - loss: 7.6301 - accuracy: 0.5024
19328/25000 [======================>.......] - ETA: 20s - loss: 7.6285 - accuracy: 0.5025
19360/25000 [======================>.......] - ETA: 20s - loss: 7.6278 - accuracy: 0.5025
19392/25000 [======================>.......] - ETA: 19s - loss: 7.6279 - accuracy: 0.5025
19424/25000 [======================>.......] - ETA: 19s - loss: 7.6240 - accuracy: 0.5028
19456/25000 [======================>.......] - ETA: 19s - loss: 7.6193 - accuracy: 0.5031
19488/25000 [======================>.......] - ETA: 19s - loss: 7.6186 - accuracy: 0.5031
19520/25000 [======================>.......] - ETA: 19s - loss: 7.6163 - accuracy: 0.5033
19552/25000 [======================>.......] - ETA: 19s - loss: 7.6164 - accuracy: 0.5033
19584/25000 [======================>.......] - ETA: 19s - loss: 7.6157 - accuracy: 0.5033
19616/25000 [======================>.......] - ETA: 19s - loss: 7.6174 - accuracy: 0.5032
19648/25000 [======================>.......] - ETA: 18s - loss: 7.6198 - accuracy: 0.5031
19680/25000 [======================>.......] - ETA: 18s - loss: 7.6214 - accuracy: 0.5029
19712/25000 [======================>.......] - ETA: 18s - loss: 7.6176 - accuracy: 0.5032
19744/25000 [======================>.......] - ETA: 18s - loss: 7.6154 - accuracy: 0.5033
19776/25000 [======================>.......] - ETA: 18s - loss: 7.6147 - accuracy: 0.5034
19808/25000 [======================>.......] - ETA: 18s - loss: 7.6140 - accuracy: 0.5034
19840/25000 [======================>.......] - ETA: 18s - loss: 7.6110 - accuracy: 0.5036
19872/25000 [======================>.......] - ETA: 18s - loss: 7.6157 - accuracy: 0.5033
19904/25000 [======================>.......] - ETA: 18s - loss: 7.6150 - accuracy: 0.5034
19936/25000 [======================>.......] - ETA: 17s - loss: 7.6166 - accuracy: 0.5033
19968/25000 [======================>.......] - ETA: 17s - loss: 7.6175 - accuracy: 0.5032
20000/25000 [=======================>......] - ETA: 17s - loss: 7.6206 - accuracy: 0.5030
20032/25000 [=======================>......] - ETA: 17s - loss: 7.6238 - accuracy: 0.5028
20064/25000 [=======================>......] - ETA: 17s - loss: 7.6231 - accuracy: 0.5028
20096/25000 [=======================>......] - ETA: 17s - loss: 7.6239 - accuracy: 0.5028
20128/25000 [=======================>......] - ETA: 17s - loss: 7.6262 - accuracy: 0.5026
20160/25000 [=======================>......] - ETA: 17s - loss: 7.6294 - accuracy: 0.5024
20192/25000 [=======================>......] - ETA: 17s - loss: 7.6324 - accuracy: 0.5022
20224/25000 [=======================>......] - ETA: 16s - loss: 7.6333 - accuracy: 0.5022
20256/25000 [=======================>......] - ETA: 16s - loss: 7.6341 - accuracy: 0.5021
20288/25000 [=======================>......] - ETA: 16s - loss: 7.6326 - accuracy: 0.5022
20320/25000 [=======================>......] - ETA: 16s - loss: 7.6327 - accuracy: 0.5022
20352/25000 [=======================>......] - ETA: 16s - loss: 7.6350 - accuracy: 0.5021
20384/25000 [=======================>......] - ETA: 16s - loss: 7.6365 - accuracy: 0.5020
20416/25000 [=======================>......] - ETA: 16s - loss: 7.6351 - accuracy: 0.5021
20448/25000 [=======================>......] - ETA: 16s - loss: 7.6389 - accuracy: 0.5018
20480/25000 [=======================>......] - ETA: 16s - loss: 7.6412 - accuracy: 0.5017
20512/25000 [=======================>......] - ETA: 15s - loss: 7.6427 - accuracy: 0.5016
20544/25000 [=======================>......] - ETA: 15s - loss: 7.6383 - accuracy: 0.5018
20576/25000 [=======================>......] - ETA: 15s - loss: 7.6398 - accuracy: 0.5017
20608/25000 [=======================>......] - ETA: 15s - loss: 7.6398 - accuracy: 0.5017
20640/25000 [=======================>......] - ETA: 15s - loss: 7.6376 - accuracy: 0.5019
20672/25000 [=======================>......] - ETA: 15s - loss: 7.6347 - accuracy: 0.5021
20704/25000 [=======================>......] - ETA: 15s - loss: 7.6355 - accuracy: 0.5020
20736/25000 [=======================>......] - ETA: 15s - loss: 7.6363 - accuracy: 0.5020
20768/25000 [=======================>......] - ETA: 15s - loss: 7.6341 - accuracy: 0.5021
20800/25000 [=======================>......] - ETA: 14s - loss: 7.6342 - accuracy: 0.5021
20832/25000 [=======================>......] - ETA: 14s - loss: 7.6350 - accuracy: 0.5021
20864/25000 [========================>.....] - ETA: 14s - loss: 7.6313 - accuracy: 0.5023
20896/25000 [========================>.....] - ETA: 14s - loss: 7.6307 - accuracy: 0.5023
20928/25000 [========================>.....] - ETA: 14s - loss: 7.6300 - accuracy: 0.5024
20960/25000 [========================>.....] - ETA: 14s - loss: 7.6308 - accuracy: 0.5023
20992/25000 [========================>.....] - ETA: 14s - loss: 7.6352 - accuracy: 0.5020
21024/25000 [========================>.....] - ETA: 14s - loss: 7.6323 - accuracy: 0.5022
21056/25000 [========================>.....] - ETA: 13s - loss: 7.6324 - accuracy: 0.5022
21088/25000 [========================>.....] - ETA: 13s - loss: 7.6346 - accuracy: 0.5021
21120/25000 [========================>.....] - ETA: 13s - loss: 7.6318 - accuracy: 0.5023
21152/25000 [========================>.....] - ETA: 13s - loss: 7.6325 - accuracy: 0.5022
21184/25000 [========================>.....] - ETA: 13s - loss: 7.6326 - accuracy: 0.5022
21216/25000 [========================>.....] - ETA: 13s - loss: 7.6334 - accuracy: 0.5022
21248/25000 [========================>.....] - ETA: 13s - loss: 7.6334 - accuracy: 0.5022
21280/25000 [========================>.....] - ETA: 13s - loss: 7.6320 - accuracy: 0.5023
21312/25000 [========================>.....] - ETA: 13s - loss: 7.6299 - accuracy: 0.5024
21344/25000 [========================>.....] - ETA: 12s - loss: 7.6285 - accuracy: 0.5025
21376/25000 [========================>.....] - ETA: 12s - loss: 7.6308 - accuracy: 0.5023
21408/25000 [========================>.....] - ETA: 12s - loss: 7.6337 - accuracy: 0.5021
21440/25000 [========================>.....] - ETA: 12s - loss: 7.6344 - accuracy: 0.5021
21472/25000 [========================>.....] - ETA: 12s - loss: 7.6331 - accuracy: 0.5022
21504/25000 [========================>.....] - ETA: 12s - loss: 7.6331 - accuracy: 0.5022
21536/25000 [========================>.....] - ETA: 12s - loss: 7.6353 - accuracy: 0.5020
21568/25000 [========================>.....] - ETA: 12s - loss: 7.6375 - accuracy: 0.5019
21600/25000 [========================>.....] - ETA: 12s - loss: 7.6361 - accuracy: 0.5020
21632/25000 [========================>.....] - ETA: 11s - loss: 7.6361 - accuracy: 0.5020
21664/25000 [========================>.....] - ETA: 11s - loss: 7.6369 - accuracy: 0.5019
21696/25000 [=========================>....] - ETA: 11s - loss: 7.6398 - accuracy: 0.5018
21728/25000 [=========================>....] - ETA: 11s - loss: 7.6433 - accuracy: 0.5015
21760/25000 [=========================>....] - ETA: 11s - loss: 7.6434 - accuracy: 0.5015
21792/25000 [=========================>....] - ETA: 11s - loss: 7.6434 - accuracy: 0.5015
21824/25000 [=========================>....] - ETA: 11s - loss: 7.6455 - accuracy: 0.5014
21856/25000 [=========================>....] - ETA: 11s - loss: 7.6456 - accuracy: 0.5014
21888/25000 [=========================>....] - ETA: 11s - loss: 7.6463 - accuracy: 0.5013
21920/25000 [=========================>....] - ETA: 10s - loss: 7.6463 - accuracy: 0.5013
21952/25000 [=========================>....] - ETA: 10s - loss: 7.6443 - accuracy: 0.5015
21984/25000 [=========================>....] - ETA: 10s - loss: 7.6429 - accuracy: 0.5015
22016/25000 [=========================>....] - ETA: 10s - loss: 7.6471 - accuracy: 0.5013
22048/25000 [=========================>....] - ETA: 10s - loss: 7.6485 - accuracy: 0.5012
22080/25000 [=========================>....] - ETA: 10s - loss: 7.6506 - accuracy: 0.5010
22112/25000 [=========================>....] - ETA: 10s - loss: 7.6521 - accuracy: 0.5009
22144/25000 [=========================>....] - ETA: 10s - loss: 7.6542 - accuracy: 0.5008
22176/25000 [=========================>....] - ETA: 10s - loss: 7.6562 - accuracy: 0.5007
22208/25000 [=========================>....] - ETA: 9s - loss: 7.6570 - accuracy: 0.5006 
22240/25000 [=========================>....] - ETA: 9s - loss: 7.6556 - accuracy: 0.5007
22272/25000 [=========================>....] - ETA: 9s - loss: 7.6549 - accuracy: 0.5008
22304/25000 [=========================>....] - ETA: 9s - loss: 7.6549 - accuracy: 0.5008
22336/25000 [=========================>....] - ETA: 9s - loss: 7.6522 - accuracy: 0.5009
22368/25000 [=========================>....] - ETA: 9s - loss: 7.6515 - accuracy: 0.5010
22400/25000 [=========================>....] - ETA: 9s - loss: 7.6516 - accuracy: 0.5010
22432/25000 [=========================>....] - ETA: 9s - loss: 7.6550 - accuracy: 0.5008
22464/25000 [=========================>....] - ETA: 8s - loss: 7.6523 - accuracy: 0.5009
22496/25000 [=========================>....] - ETA: 8s - loss: 7.6503 - accuracy: 0.5011
22528/25000 [==========================>...] - ETA: 8s - loss: 7.6550 - accuracy: 0.5008
22560/25000 [==========================>...] - ETA: 8s - loss: 7.6523 - accuracy: 0.5009
22592/25000 [==========================>...] - ETA: 8s - loss: 7.6524 - accuracy: 0.5009
22624/25000 [==========================>...] - ETA: 8s - loss: 7.6524 - accuracy: 0.5009
22656/25000 [==========================>...] - ETA: 8s - loss: 7.6531 - accuracy: 0.5009
22688/25000 [==========================>...] - ETA: 8s - loss: 7.6538 - accuracy: 0.5008
22720/25000 [==========================>...] - ETA: 8s - loss: 7.6545 - accuracy: 0.5008
22752/25000 [==========================>...] - ETA: 7s - loss: 7.6552 - accuracy: 0.5007
22784/25000 [==========================>...] - ETA: 7s - loss: 7.6592 - accuracy: 0.5005
22816/25000 [==========================>...] - ETA: 7s - loss: 7.6606 - accuracy: 0.5004
22848/25000 [==========================>...] - ETA: 7s - loss: 7.6626 - accuracy: 0.5003
22880/25000 [==========================>...] - ETA: 7s - loss: 7.6613 - accuracy: 0.5003
22912/25000 [==========================>...] - ETA: 7s - loss: 7.6626 - accuracy: 0.5003
22944/25000 [==========================>...] - ETA: 7s - loss: 7.6606 - accuracy: 0.5004
22976/25000 [==========================>...] - ETA: 7s - loss: 7.6613 - accuracy: 0.5003
23008/25000 [==========================>...] - ETA: 7s - loss: 7.6626 - accuracy: 0.5003
23040/25000 [==========================>...] - ETA: 6s - loss: 7.6640 - accuracy: 0.5002
23072/25000 [==========================>...] - ETA: 6s - loss: 7.6633 - accuracy: 0.5002
23104/25000 [==========================>...] - ETA: 6s - loss: 7.6633 - accuracy: 0.5002
23136/25000 [==========================>...] - ETA: 6s - loss: 7.6640 - accuracy: 0.5002
23168/25000 [==========================>...] - ETA: 6s - loss: 7.6646 - accuracy: 0.5001
23200/25000 [==========================>...] - ETA: 6s - loss: 7.6607 - accuracy: 0.5004
23232/25000 [==========================>...] - ETA: 6s - loss: 7.6607 - accuracy: 0.5004
23264/25000 [==========================>...] - ETA: 6s - loss: 7.6581 - accuracy: 0.5006
23296/25000 [==========================>...] - ETA: 6s - loss: 7.6620 - accuracy: 0.5003
23328/25000 [==========================>...] - ETA: 5s - loss: 7.6640 - accuracy: 0.5002
23360/25000 [===========================>..] - ETA: 5s - loss: 7.6640 - accuracy: 0.5002
23392/25000 [===========================>..] - ETA: 5s - loss: 7.6666 - accuracy: 0.5000
23424/25000 [===========================>..] - ETA: 5s - loss: 7.6679 - accuracy: 0.4999
23456/25000 [===========================>..] - ETA: 5s - loss: 7.6705 - accuracy: 0.4997
23488/25000 [===========================>..] - ETA: 5s - loss: 7.6660 - accuracy: 0.5000
23520/25000 [===========================>..] - ETA: 5s - loss: 7.6673 - accuracy: 0.5000
23552/25000 [===========================>..] - ETA: 5s - loss: 7.6673 - accuracy: 0.5000
23584/25000 [===========================>..] - ETA: 5s - loss: 7.6666 - accuracy: 0.5000
23616/25000 [===========================>..] - ETA: 4s - loss: 7.6647 - accuracy: 0.5001
23648/25000 [===========================>..] - ETA: 4s - loss: 7.6627 - accuracy: 0.5003
23680/25000 [===========================>..] - ETA: 4s - loss: 7.6660 - accuracy: 0.5000
23712/25000 [===========================>..] - ETA: 4s - loss: 7.6660 - accuracy: 0.5000
23744/25000 [===========================>..] - ETA: 4s - loss: 7.6673 - accuracy: 0.5000
23776/25000 [===========================>..] - ETA: 4s - loss: 7.6686 - accuracy: 0.4999
23808/25000 [===========================>..] - ETA: 4s - loss: 7.6673 - accuracy: 0.5000
23840/25000 [===========================>..] - ETA: 4s - loss: 7.6660 - accuracy: 0.5000
23872/25000 [===========================>..] - ETA: 3s - loss: 7.6647 - accuracy: 0.5001
23904/25000 [===========================>..] - ETA: 3s - loss: 7.6666 - accuracy: 0.5000
23936/25000 [===========================>..] - ETA: 3s - loss: 7.6653 - accuracy: 0.5001
23968/25000 [===========================>..] - ETA: 3s - loss: 7.6673 - accuracy: 0.5000
24000/25000 [===========================>..] - ETA: 3s - loss: 7.6660 - accuracy: 0.5000
24032/25000 [===========================>..] - ETA: 3s - loss: 7.6653 - accuracy: 0.5001
24064/25000 [===========================>..] - ETA: 3s - loss: 7.6666 - accuracy: 0.5000
24096/25000 [===========================>..] - ETA: 3s - loss: 7.6679 - accuracy: 0.4999
24128/25000 [===========================>..] - ETA: 3s - loss: 7.6679 - accuracy: 0.4999
24160/25000 [===========================>..] - ETA: 2s - loss: 7.6685 - accuracy: 0.4999
24192/25000 [============================>.] - ETA: 2s - loss: 7.6666 - accuracy: 0.5000
24224/25000 [============================>.] - ETA: 2s - loss: 7.6641 - accuracy: 0.5002
24256/25000 [============================>.] - ETA: 2s - loss: 7.6641 - accuracy: 0.5002
24288/25000 [============================>.] - ETA: 2s - loss: 7.6622 - accuracy: 0.5003
24320/25000 [============================>.] - ETA: 2s - loss: 7.6603 - accuracy: 0.5004
24352/25000 [============================>.] - ETA: 2s - loss: 7.6616 - accuracy: 0.5003
24384/25000 [============================>.] - ETA: 2s - loss: 7.6603 - accuracy: 0.5004
24416/25000 [============================>.] - ETA: 2s - loss: 7.6622 - accuracy: 0.5003
24448/25000 [============================>.] - ETA: 1s - loss: 7.6654 - accuracy: 0.5001
24480/25000 [============================>.] - ETA: 1s - loss: 7.6654 - accuracy: 0.5001
24512/25000 [============================>.] - ETA: 1s - loss: 7.6654 - accuracy: 0.5001
24544/25000 [============================>.] - ETA: 1s - loss: 7.6635 - accuracy: 0.5002
24576/25000 [============================>.] - ETA: 1s - loss: 7.6641 - accuracy: 0.5002
24608/25000 [============================>.] - ETA: 1s - loss: 7.6641 - accuracy: 0.5002
24640/25000 [============================>.] - ETA: 1s - loss: 7.6660 - accuracy: 0.5000
24672/25000 [============================>.] - ETA: 1s - loss: 7.6641 - accuracy: 0.5002
24704/25000 [============================>.] - ETA: 1s - loss: 7.6623 - accuracy: 0.5003
24736/25000 [============================>.] - ETA: 0s - loss: 7.6623 - accuracy: 0.5003
24768/25000 [============================>.] - ETA: 0s - loss: 7.6623 - accuracy: 0.5003
24800/25000 [============================>.] - ETA: 0s - loss: 7.6641 - accuracy: 0.5002
24832/25000 [============================>.] - ETA: 0s - loss: 7.6660 - accuracy: 0.5000
24864/25000 [============================>.] - ETA: 0s - loss: 7.6691 - accuracy: 0.4998
24896/25000 [============================>.] - ETA: 0s - loss: 7.6691 - accuracy: 0.4998
24928/25000 [============================>.] - ETA: 0s - loss: 7.6678 - accuracy: 0.4999
24960/25000 [============================>.] - ETA: 0s - loss: 7.6660 - accuracy: 0.5000
24992/25000 [============================>.] - ETA: 0s - loss: 7.6672 - accuracy: 0.5000
25000/25000 [==============================] - 106s 4ms/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
Loading data...
Using TensorFlow backend.





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//fashion_MNIST_mlmodels.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//fashion_MNIST_mlmodels.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//mnist_mlmodels_.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//mnist_mlmodels_.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//tensorflow_1_lstm.ipynb 

/home/runner/work/mlmodels/mlmodels
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384
test

  #### Module init   ############################################ 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term

  <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> 

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  #### Model init   ############################################ 

  <mlmodels.model_tf.1_lstm.Model object at 0x7f99eddeda90> 

  #### Fit   ######################################################## 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   #################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384
[[ 0.          0.          0.          0.          0.          0.        ]
 [-0.04437276  0.02047656 -0.01974449 -0.00566156 -0.04283222  0.02428636]
 [ 0.23904197  0.08327175 -0.0846252   0.05405093  0.29221821  0.07447617]
 [-0.03736224  0.00584727  0.01910893  0.18684588  0.22394739 -0.06116866]
 [ 0.12272096  0.18510891 -0.1095816   0.36950538 -0.41111565  0.05816888]
 [-0.02447533  0.1163331   0.165133   -0.09440306  0.18061087 -0.05087188]
 [-0.06807277 -0.32969788  0.19298668 -0.12622789  0.10290413 -0.2672025 ]
 [ 0.12046757 -0.10912419  0.2418295   0.31712765 -0.38628134  0.03282329]
 [ 0.28741607  0.51392967  0.23077856 -0.34774917  0.08326829  0.47139943]
 [ 0.          0.          0.          0.          0.          0.        ]]

  #### Get  metrics   ################################################ 

  #### Save   ######################################################## 

  #### Load   ######################################################## 
model_tf/1_lstm.py
model_tf.1_lstm.py
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  {'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'timestep': 4, 'epoch': 2, 'output_size': 6} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'} {} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'} 

  #### Loading dataset   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]

  #### Model init  ############################################# 

  #### Model fit   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   ##################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'train': 0}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384

  #### metrics   ##################################################### 
{'loss': 0.41018325090408325, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Failed [Errno 13] Permission denied: '/model/'
model_tf/1_lstm.py
model_tf.1_lstm.py
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  {'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'timestep': 4, 'epoch': 2, 'output_size': 6} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'} {} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'} 

  #### Loading dataset   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]

  #### Model init  ############################################# 

  #### Model fit   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   ##################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'train': 0}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384

  #### metrics   ##################################################### 
{'loss': 0.6021712571382523, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Failed [Errno 13] Permission denied: '/model/'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_home_retail.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_home_retail.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0mdata_path[0m [0;34m=[0m [0;34m'hyper_lightgbm_home_retail.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'hyper_lightgbm_home_retail.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//gluon_automl.ipynb 

/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv | Columns = 15 / 15 | Rows = 39073 -> 39073
Warning: `hyperparameter_tune=True` is currently experimental and may cause the process to hang. Setting `auto_stack=True` instead is recommended to achieve maximum quality models.
Beginning AutoGluon training ... Time limit = 120s
AutoGluon will save models to dataset/
Train Data Rows:    39073
Train Data Columns: 15
Preprocessing data ...
Here are the first 10 unique label values in your data:  [' Tech-support' ' Transport-moving' ' Other-service' ' ?'
 ' Handlers-cleaners' ' Sales' ' Craft-repair' ' Adm-clerical'
 ' Exec-managerial' ' Prof-specialty']
AutoGluon infers your prediction problem is: multiclass  (because dtype of label-column == object)
If this is wrong, please specify `problem_type` argument in fit() instead (You may specify problem_type as one of: ['binary', 'multiclass', 'regression'])

Feature Generator processed 39073 data points with 14 features
Original Features:
	int features: 6
	object features: 8
Generated Features:
	int features: 0
All Features:
	int features: 6
	object features: 8
	Data preprocessing and feature engineering runtime = 0.25s ...
AutoGluon will gauge predictive performance using evaluation metric: accuracy
To change this, specify the eval_metric argument of fit()
AutoGluon will early stop models using evaluation metric: accuracy
Saving dataset/learner.pkl
Beginning hyperparameter tuning for Gradient Boosting Model...
Hyperparameter search space for Gradient Boosting Model: 
num_leaves:   Int: lower=26, upper=30
learning_rate:   Real: lower=0.005, upper=0.2
feature_fraction:   Real: lower=0.75, upper=1.0
min_data_in_leaf:   Int: lower=2, upper=30
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/trainer/abstract_trainer.py", line 360, in train_single_full
    Y_train=y_train, Y_test=y_test, scheduler_options=(self.scheduler_func, self.scheduler_options), verbosity=self.verbosity)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/models/lgb/lgb_model.py", line 283, in hyperparameter_tune
    directory=directory, lgb_model=self, **params_copy)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 69, in register_args
    self.update(**kwvars)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 79, in update
    hp = v.get_hp(name=k)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/space.py", line 451, in get_hp
    default_value=self._default)
  File "ConfigSpace/hyperparameters.pyx", line 773, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.__init__
  File "ConfigSpace/hyperparameters.pyx", line 843, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.check_default
Warning: Exception caused LightGBMClassifier to fail during hyperparameter tuning... Skipping this model.
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/trainer/abstract_trainer.py", line 360, in train_single_full
    Y_train=y_train, Y_test=y_test, scheduler_options=(self.scheduler_func, self.scheduler_options), verbosity=self.verbosity)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/models/lgb/lgb_model.py", line 283, in hyperparameter_tune
    directory=directory, lgb_model=self, **params_copy)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 69, in register_args
    self.update(**kwvars)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 79, in update
    hp = v.get_hp(name=k)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/space.py", line 451, in get_hp
    default_value=self._default)
  File "ConfigSpace/hyperparameters.pyx", line 773, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.__init__
  File "ConfigSpace/hyperparameters.pyx", line 843, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.check_default
ValueError: Illegal default value 36
Saving dataset/models/trainer.pkl
Beginning hyperparameter tuning for Neural Network...
Hyperparameter search space for Neural Network: 
network_type:   Categorical['widedeep', 'feedforward']
layers:   Categorical[[100], [1000], [200, 100], [300, 200, 100]]
activation:   Categorical['relu', 'softrelu', 'tanh']
embedding_size_factor:   Real: lower=0.5, upper=1.5
use_batchnorm:   Categorical[True, False]
dropout_prob:   Real: lower=0.0, upper=0.5
learning_rate:   Real: lower=0.0001, upper=0.01
weight_decay:   Real: lower=1e-12, upper=0.1
AutoGluon Neural Network infers features are of the following types:
{
    "continuous": [
        "age",
        "education-num",
        "hours-per-week"
    ],
    "skewed": [
        "fnlwgt",
        "capital-gain",
        "capital-loss"
    ],
    "onehot": [
        "sex",
        "class"
    ],
    "embed": [
        "workclass",
        "education",
        "marital-status",
        "relationship",
        "race",
        "native-country"
    ],
    "language": []
}


Saving dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Starting Experiments
Num of Finished Tasks is 0
Num of Pending Tasks is 5

Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862

Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Finished Task with config: {'activation.choice': 2, 'dropout_prob': 0.38289765386527974, 'embedding_size_factor': 0.7180387152208412, 'layers.choice': 2, 'learning_rate': 0.0072320106661035305, 'network_type.choice': 1, 'use_batchnorm.choice': 1, 'weight_decay': 1.6307344745232966e-12} and reward: 0.3756
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xd8\x81e)DA\x9cX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe6\xfa,S\xe4T\xf4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?}\x9fP\x14\xb9KPX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=|\xb0,\xd8\x0f.\x87u.' and reward: 0.3756
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xd8\x81e)DA\x9cX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe6\xfa,S\xe4T\xf4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?}\x9fP\x14\xb9KPX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=|\xb0,\xd8\x0f.\x87u.' and reward: 0.3756

Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Finished Task with config: {'activation.choice': 1, 'dropout_prob': 0.37821708209280347, 'embedding_size_factor': 0.7231042194358328, 'layers.choice': 3, 'learning_rate': 0.001140319420145891, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1.9091856601522774e-12} and reward: 0.3774
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xd84\xb5k\x98#\x08X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe7#\xabu\xc2r\xc4X\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?R\xae\xd8\xa7u\x11\x80X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G=\x80\xcb\x1a\x9a\x18\xa0\xb6u.' and reward: 0.3774
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xd84\xb5k\x98#\x08X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe7#\xabu\xc2r\xc4X\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?R\xae\xd8\xa7u\x11\x80X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G=\x80\xcb\x1a\x9a\x18\xa0\xb6u.' and reward: 0.3774
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 170.30097126960754
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.75s of the -53.08s of remaining time.
Ensemble size: 29
Ensemble weights: 
[0.5862069  0.17241379 0.24137931]
	0.3924	 = Validation accuracy score
	1.06s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 174.18s ...
Loading: dataset/models/trainer.pkl
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
test

  #### Module init   ############################################ 

  <module 'mlmodels.model_gluon.gluon_automl' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py'> 

  #### Loading params   ############################################## 
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 506, in main
    test_cli(arg)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 436, in test_cli
    test_module(arg.model_uri, param_pars=param_pars)  # '1_lstm'
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 255, in test_module
    model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py", line 109, in get_params
    return model_pars, data_pars, compute_pars, out_pars
UnboundLocalError: local variable 'model_pars' referenced before assignment





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vision_mnist.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_glass.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      8[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      9[0m [0;34m[0m[0m
[0;32m---> 10[0;31m [0mprint[0m[0;34m([0m [0mos[0m[0;34m.[0m[0mgetcwd[0m[0;34m([0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m
[0;31mNameError[0m: name 'os' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//gluon_automl_titanic.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//gluon_automl_titanic.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      8[0m     [0mchoice[0m[0;34m=[0m[0;34m'json'[0m[0;34m,[0m[0;34m[0m[0;34m[0m[0m
[1;32m      9[0m     [0mconfig_mode[0m[0;34m=[0m [0;34m'test'[0m[0;34m,[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 10[0;31m     [0mdata_path[0m[0;34m=[0m [0;34m'../mlmodels/dataset/json/gluon_automl.json'[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     11[0m )

[0;32m~/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py[0m in [0;36mget_params[0;34m(choice, data_path, config_mode, **kw)[0m
[1;32m     80[0m             __file__)).parent.parent / "model_gluon/gluon_automl.json" if data_path == "dataset/" else data_path
[1;32m     81[0m [0;34m[0m[0m
[0;32m---> 82[0;31m         [0;32mwith[0m [0mopen[0m[0;34m([0m[0mdata_path[0m[0;34m,[0m [0mencoding[0m[0;34m=[0m[0;34m'utf-8'[0m[0;34m)[0m [0;32mas[0m [0mconfig_f[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     83[0m             [0mconfig[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mconfig_f[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     84[0m             [0mconfig[0m [0;34m=[0m [0mconfig[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '../mlmodels/dataset/json/gluon_automl.json'
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vison_fashion_MNIST.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//vison_fashion_MNIST.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//tensorflow__lstm_json.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//tensorflow__lstm_json.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      5[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      6[0m [0;34m[0m[0m
[0;32m----> 7[0;31m [0mprint[0m[0;34m([0m [0mos[0m[0;34m.[0m[0mgetcwd[0m[0;34m([0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m
[0;31mNameError[0m: name 'os' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      4[0m [0mdata_path[0m [0;34m=[0m [0;34m'lightgbm_titanic.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0;34m[0m[0m
[0;32m----> 6[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      7[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      8[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'lightgbm_titanic.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_randomForest.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     69[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 70[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     71[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     81[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 82[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     83[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      2[0m [0;34m[0m[0m
[1;32m      3[0m [0mmodel_uri[0m    [0;34m=[0m [0;34m"model_sklearn.sklearn.py"[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 4[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      5[0m [0;34m[0m[0m
[1;32m      6[0m model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     85[0m [0;34m[0m[0m
[1;32m     86[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 87[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     88[0m [0;34m[0m[0m
[1;32m     89[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     69[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 70[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     71[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     81[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 82[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     83[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mmodels[0m [0;32mimport[0m [0mmodule_load[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0mmodel[0m         [0;34m=[0m  [0mmodule[0m[0;34m.[0m[0mModel[0m[0;34m([0m[0mmodel_pars[0m[0;34m=[0m[0mmodel_pars[0m[0;34m,[0m [0mdata_pars[0m[0;34m=[0m[0mdata_pars[0m[0;34m,[0m [0mcompute_pars[0m[0;34m=[0m[0mcompute_pars[0m[0;34m)[0m             [0;31m# Create Model instance[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0mmodel[0m[0;34m,[0m [0msess[0m   [0;34m=[0m  [0mmodule[0m[0;34m.[0m[0mfit[0m[0;34m([0m[0mmodel[0m[0;34m,[0m [0mdata_pars[0m[0;34m=[0m[0mdata_pars[0m[0;34m,[0m [0mcompute_pars[0m[0;34m=[0m[0mcompute_pars[0m[0;34m,[0m [0mout_pars[0m[0;34m=[0m[0mout_pars[0m[0;34m)[0m          [0;31m# fit the model[0m[0;34m[0m[0;34m[0m[0m

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     85[0m [0;34m[0m[0m
[1;32m     86[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 87[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     88[0m [0;34m[0m[0m
[1;32m     89[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0mdata_path[0m [0;34m=[0m [0;34m'../mlmodels/dataset/json/hyper_titanic_randomForest.json'[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      7[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '../mlmodels/dataset/json/hyper_titanic_randomForest.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vision_mnist.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/vision_mnist.py"[0;36m, line [0;32m15[0m
[0;31m    !git clone https://github.com/ahmed3bbas/mlmodels.git[0m
[0m    ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//arun_model.py 

<module 'mlmodels' from '/home/runner/work/mlmodels/mlmodels/mlmodels/__init__.py'>
/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/arun_model.py[0m in [0;36m<module>[0;34m[0m
[1;32m     25[0m [0;31m# Model Parameters[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[1;32m     26[0m [0;31m# model_pars, data_pars, compute_pars, out_pars[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 27[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m[0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     28[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m     29[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpdict[0m   [0;34m)[0m   [0;31m###Normalize path[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_glass.py 

Deprecaton set to False
/home/runner/work/mlmodels/mlmodels
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/lightgbm_glass.py[0m in [0;36m<module>[0;34m[0m
[1;32m     20[0m [0;34m[0m[0m
[1;32m     21[0m [0;34m[0m[0m
[0;32m---> 22[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     23[0m [0mprint[0m[0;34m([0m[0mpars[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     24[0m [0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'lightgbm_glass.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//benchmark_timeseries_m4.py 






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//arun_hyper.py 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/arun_hyper.py[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mmodels[0m [0;32mimport[0m [0mmodule_load[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mutil[0m [0;32mimport[0m [0mpath_norm_dict[0m[0;34m,[0m [0mpath_norm[0m[0;34m,[0m [0mparams_json_load[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mprint[0m[0;34m([0m[0mmlmodels[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;34m[0m[0m
[1;32m      7[0m [0;34m[0m[0m

[0;31mNameError[0m: name 'mlmodels' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example/benchmark_timeseries_m4.py 






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example/benchmark_timeseries_m5.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py"[0;36m, line [0;32m248[0m
[0;31m    We then reshape the forecasts into the correct data shape for submission ...[0m
[0m          ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//benchmark_timeseries_m5.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py"[0;36m, line [0;32m248[0m
[0;31m    We then reshape the forecasts into the correct data shape for submission ...[0m
[0m          ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax
