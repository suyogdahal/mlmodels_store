
  test_pullrequest /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_pullrequest', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_pullrequest 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/22f2b7c7253266907172fe15dac6b61745a76480', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '22f2b7c7253266907172fe15dac6b61745a76480', 'workflow': 'test_pullrequest'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_pullrequest

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/22f2b7c7253266907172fe15dac6b61745a76480

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/22f2b7c7253266907172fe15dac6b61745a76480

 ************************************************************************************************************************

  /home/runner/work/mlmodels/mlmodels/pullrequest/ 

  ############Check model ################################ 

  ['/home/runner/work/mlmodels/mlmodels/pullrequest/aa_mycode_test.py'] 

  Used ['/home/runner/work/mlmodels/mlmodels/pullrequest/aa_mycode_test.py'] 

  ########### Run Check ############################## 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/22f2b7c7253266907172fe15dac6b61745a76480', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '22f2b7c7253266907172fe15dac6b61745a76480', 'workflow': 'test_pullrequest'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_pullrequest

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/22f2b7c7253266907172fe15dac6b61745a76480

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/22f2b7c7253266907172fe15dac6b61745a76480

 ************************************************************************************************************************





 ************************************************************************************************************************

  test_import 
['model_tf.temporal_fusion_google', 'model_tf.util', 'model_tf.__init__', 'model_tf.1_lstm', 'model_dev.__init__', 'model_sklearn.model_lightgbm', 'model_sklearn.__init__', 'model_sklearn.model_sklearn', 'preprocess.generic_old', 'preprocess.image', 'preprocess.generic', 'preprocess.tabular', 'preprocess.ztemp', 'preprocess.__init__', 'preprocess.text_torch', 'preprocess.tabular_keras', 'preprocess.timeseries', 'preprocess.text_keras', 'preprocess.text', 'model_tch.util_data', 'model_tch.pplm', 'model_tch.transformer_sentence', 'model_tch.__init__', 'model_tch.nbeats', 'model_tch.textcnn', 'model_tch.mlp', 'model_tch.pytorch_vae', 'model_tch.03_nbeats_dataloader', 'model_tch.torchhub', 'model_tch.util_transformer', 'model_tch.transformer_classifier', 'model_tch.matchzoo_models', 'model_gluon.util_autogluon', 'model_gluon.util', 'model_gluon.gluonts_model', 'model_gluon.__init__', 'model_gluon.fb_prophet', 'model_gluon.gluon_automl', 'model_flow.__init__', 'example.vision_mnist', 'example.arun_model', 'example.lightgbm_glass', 'example.benchmark_timeseries_m4', 'example.arun_hyper', 'example.benchmark_timeseries_m5', 'template.00_template_keras', 'template.model_xxx', 'model_rank.__init__', 'model_keras.charcnn', 'model_keras.charcnn_zhang', 'model_keras.namentity_crm_bilstm_dataloader', 'model_keras.01_deepctr', 'model_keras.util', 'model_keras.__init__', 'model_keras.namentity_crm_bilstm', 'model_keras.nbeats', 'model_keras.textcnn', 'model_keras.keras_gan', 'model_keras.textcnn_dataloader', 'model_keras.02_cnn', 'model_keras.preprocess', 'model_keras.Autokeras', 'model_keras.armdn', 'model_keras.textvae', 'utils.ztest_structure', 'utils.test_dataloader', 'utils.parse']

  Error mlmodels.model_tf.temporal_fusion_google No module named 'mlmodels.mode_tf' 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
mlmodels.model_tf.util
mlmodels.model_tf.__init__
mlmodels.model_tf.1_lstm
mlmodels.model_dev.__init__
mlmodels.model_sklearn.model_lightgbm
mlmodels.model_sklearn.__init__
mlmodels.model_sklearn.model_sklearn
mlmodels.preprocess.generic_old
mlmodels.preprocess.image
mlmodels.preprocess.generic
mlmodels.preprocess.tabular

  Error mlmodels.preprocess.ztemp invalid character in identifier (ztemp.py, line 6) 
mlmodels.preprocess.__init__
mlmodels.preprocess.text_torch
mlmodels.preprocess.tabular_keras
mlmodels.preprocess.timeseries
mlmodels.preprocess.text_keras
mlmodels.preprocess.text

  Error mlmodels.model_tch.util_data [Errno 2] File b'./data/train.csv' does not exist: b'./data/train.csv' 
mlmodels.model_tch.pplm
mlmodels.model_tch.transformer_sentence
mlmodels.model_tch.__init__
mlmodels.model_tch.nbeats
mlmodels.model_tch.textcnn
mlmodels.model_tch.mlp

  Error mlmodels.model_tchtorch_vae No module named 'mlmodels.model_tchtorch_vae' 

  Error mlmodels.model_tch.03_nbeats_dataloader No module named 'dataloader' 
mlmodels.model_tch.torchhub
mlmodels.model_tch.util_transformer

  Error mlmodels.model_tch.transformer_classifier No module named 'util_transformer' 
mlmodels.model_tch.matchzoo_models
mlmodels.model_gluon.util_autogluon

  Error mlmodels.model_gluon.util create_model() takes exactly 1 positional argument (0 given) 

  Error mlmodels.model_gluon.gluonts_model create_model() takes exactly 1 positional argument (0 given) 
mlmodels.model_gluon.__init__
mlmodels.model_gluon.fb_prophet
mlmodels.model_gluon.gluon_automl
mlmodels.model_flow.__init__

  Error mlmodels.example.vision_mnist invalid syntax (vision_mnist.py, line 15) 
<module 'mlmodels' from '/home/runner/work/mlmodels/mlmodels/mlmodels/__init__.py'>
/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json

  Error mlmodels.example.arun_model [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json' 
Deprecaton set to False
/home/runner/work/mlmodels/mlmodels

  Error mlmodels.example.lightgbm_glass [Errno 2] No such file or directory: 'lightgbm_glass.json' 
mlmodels.example.benchmark_timeseries_m4

  Error mlmodels.example.arun_hyper name 'mlmodels' is not defined 

  Error mlmodels.example.benchmark_timeseries_m5 invalid syntax (benchmark_timeseries_m5.py, line 248) 

  Error mlmodels.template.00_template_keras expected an indented block (00_template_keras.py, line 68) 

  Error mlmodels.template.model_xxx name '__file___' is not defined 
mlmodels.model_rank.__init__
mlmodels.model_keras.charcnn
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset
mlmodels.model_keras.charcnn_zhang
mlmodels.model_keras.namentity_crm_bilstm_dataloader
mlmodels.model_keras.01_deepctr

  Error mlmodels.model_keras.util create_model() takes exactly 1 positional argument (0 given) 
mlmodels.model_keras.__init__
mlmodels.model_keras.namentity_crm_bilstm
mlmodels.model_keras.nbeats
mlmodels.model_keras.textcnn

  Error mlmodels.model_keras.keras_gan module 'mlmodels.model_keras.raw.keras_gan' has no attribute 'aae' 
mlmodels.model_keras.textcnn_dataloader
mlmodels.model_keras.02_cnn
mlmodels.model_keras.preprocess

  Error mlmodels.model_keras.Autokeras No module named 'autokeras' 
Deprecaton set to False

  {'model_uri': 'model_tf.1_lstm', 'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} {'engine': 'optuna', 'method': 'prune', 'ntrials': 5} {'engine_pars': {'engine': 'optuna', 'method': 'normal', 'ntrials': 2, 'metric_target': 'loss'}, 'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}, 'num_layers': {'type': 'int', 'init': 2, 'range': [2, 4]}, 'size': {'type': 'int', 'init': 6, 'range': [6, 6]}, 'output_size': {'type': 'int', 'init': 6, 'range': [6, 6]}, 'size_layer': {'type': 'categorical', 'value': [128, 256]}, 'timestep': {'type': 'categorical', 'value': [5]}, 'epoch': {'type': 'categorical', 'value': [2]}} 

  <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> 

  ###### Hyper-optimization through study   ################################## 

  check <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} 
[32m[I 2020-05-11 06:11:11,067][0m Finished trial#0 resulted in value: 7.4695985317230225. Current best value is 7.4695985317230225 with parameters: {'learning_rate': 0.053533819784658834, 'num_layers': 4, 'size': 6, 'output_size': 6, 'size_layer': 128, 'timestep': 5, 'epoch': 2}.[0m
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

  check <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} 
[32m[I 2020-05-11 06:11:13,014][0m Finished trial#1 resulted in value: 0.3267613723874092. Current best value is 0.3267613723874092 with parameters: {'learning_rate': 0.010829201279599259, 'num_layers': 4, 'size': 6, 'output_size': 6, 'size_layer': 128, 'timestep': 5, 'epoch': 2}.[0m
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

 ################################### Optim, finished ###################################

  ### Save Stats   ########################################################## 

  ### Run Model with best   ################################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

  #### Saving     ########################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/optim_1lstm/', 'model_type': 'model_tf', 'model_uri': 'model_tf-1_lstm'}
sh: 1: ml_mlmodels: not found
mlmodels.model_keras.armdn
mlmodels.model_keras.textvae
mlmodels.utils.ztest_structure
mlmodels.utils.test_dataloader
mlmodels.utils.parse





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/pullrequest/aa_mycode_test.py  2>&1 | tee -a  cd log_.txt 
os.getcwd /home/runner/work/mlmodels/mlmodels
############ Your custom code ################################



 python /home/runner/work/mlmodels/mlmodels/mlmodels/optim.py  
Deprecaton set to False

  {'model_uri': 'model_tf.1_lstm', 'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} {'engine': 'optuna', 'method': 'prune', 'ntrials': 5} {'engine_pars': {'engine': 'optuna', 'method': 'normal', 'ntrials': 2, 'metric_target': 'loss'}, 'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}, 'num_layers': {'type': 'int', 'init': 2, 'range': [2, 4]}, 'size': {'type': 'int', 'init': 6, 'range': [6, 6]}, 'output_size': {'type': 'int', 'init': 6, 'range': [6, 6]}, 'size_layer': {'type': 'categorical', 'value': [128, 256]}, 'timestep': {'type': 'categorical', 'value': [5]}, 'epoch': {'type': 'categorical', 'value': [2]}} 

  <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> 

  ###### Hyper-optimization through study   ################################## 

  check <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} 

  <mlmodels.model_tf.1_lstm.Model object at 0x7f408927f2e8> 
[32m[I 2020-05-11 06:11:19,967][0m Finished trial#0 resulted in value: 0.47443486750125885. Current best value is 0.47443486750125885 with parameters: {'learning_rate': 0.003648885071629544, 'num_layers': 2, 'size': 6, 'output_size': 6, 'size_layer': 256, 'timestep': 5, 'epoch': 2}.[0m
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

  check <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]} 

  <mlmodels.model_tf.1_lstm.Model object at 0x7f40a69b57f0> 
[32m[I 2020-05-11 06:11:21,628][0m Finished trial#1 resulted in value: 0.3299776613712311. Current best value is 0.3299776613712311 with parameters: {'learning_rate': 0.009577408427677455, 'num_layers': 3, 'size': 6, 'output_size': 6, 'size_layer': 256, 'timestep': 5, 'epoch': 2}.[0m
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

 ################################### Optim, finished ###################################

  ### Save Stats   ########################################################## 

  ### Run Model with best   ################################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year_small.csv
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

  #### Saving     ########################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/optim_1lstm/', 'model_type': 'model_tf', 'model_uri': 'model_tf-1_lstm'}



 python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.py    

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 2:17
   40960/17464789 [..............................] - ETA: 54s 
   90112/17464789 [..............................] - ETA: 37s
  196608/17464789 [..............................] - ETA: 22s
  401408/17464789 [..............................] - ETA: 13s
  630784/17464789 [>.............................] - ETA: 10s
  974848/17464789 [>.............................] - ETA: 7s 
 1032192/17464789 [>.............................] - ETA: 8s
 1294336/17464789 [=>............................] - ETA: 7s
 1376256/17464789 [=>............................] - ETA: 7s
 1572864/17464789 [=>............................] - ETA: 7s
 1744896/17464789 [=>............................] - ETA: 7s
 1933312/17464789 [==>...........................] - ETA: 6s
 2129920/17464789 [==>...........................] - ETA: 6s
 2318336/17464789 [==>...........................] - ETA: 6s
 2506752/17464789 [===>..........................] - ETA: 6s
 2768896/17464789 [===>..........................] - ETA: 5s
 2965504/17464789 [====>.........................] - ETA: 5s
 3227648/17464789 [====>.........................] - ETA: 5s
 3481600/17464789 [====>.........................] - ETA: 5s
 3743744/17464789 [=====>........................] - ETA: 4s
 3899392/17464789 [=====>........................] - ETA: 4s
 4161536/17464789 [======>.......................] - ETA: 4s
 4284416/17464789 [======>.......................] - ETA: 4s
 4456448/17464789 [======>.......................] - ETA: 4s
 4653056/17464789 [======>.......................] - ETA: 4s
 4915200/17464789 [=======>......................] - ETA: 4s
 5177344/17464789 [=======>......................] - ETA: 4s
 5431296/17464789 [========>.....................] - ETA: 4s
 5693440/17464789 [========>.....................] - ETA: 4s
 5955584/17464789 [=========>....................] - ETA: 3s
 6217728/17464789 [=========>....................] - ETA: 3s
 6479872/17464789 [==========>...................] - ETA: 3s
 6742016/17464789 [==========>...................] - ETA: 3s
 7004160/17464789 [===========>..................] - ETA: 3s
 7266304/17464789 [===========>..................] - ETA: 3s
 7503872/17464789 [===========>..................] - ETA: 3s
 7766016/17464789 [============>.................] - ETA: 3s
 8028160/17464789 [============>.................] - ETA: 2s
 8290304/17464789 [=============>................] - ETA: 2s
 8552448/17464789 [=============>................] - ETA: 2s
 8814592/17464789 [==============>...............] - ETA: 2s
 9076736/17464789 [==============>...............] - ETA: 2s
 9330688/17464789 [===============>..............] - ETA: 2s
 9592832/17464789 [===============>..............] - ETA: 2s
 9854976/17464789 [===============>..............] - ETA: 2s
10117120/17464789 [================>.............] - ETA: 2s
10379264/17464789 [================>.............] - ETA: 2s
10641408/17464789 [=================>............] - ETA: 2s
10903552/17464789 [=================>............] - ETA: 1s
11165696/17464789 [==================>...........] - ETA: 1s
11419648/17464789 [==================>...........] - ETA: 1s
11681792/17464789 [===================>..........] - ETA: 1s
11878400/17464789 [===================>..........] - ETA: 1s
12140544/17464789 [===================>..........] - ETA: 1s
12394496/17464789 [====================>.........] - ETA: 1s
12591104/17464789 [====================>.........] - ETA: 1s
12853248/17464789 [=====================>........] - ETA: 1s
13115392/17464789 [=====================>........] - ETA: 1s
13369344/17464789 [=====================>........] - ETA: 1s
13631488/17464789 [======================>.......] - ETA: 1s
13844480/17464789 [======================>.......] - ETA: 1s
14032896/17464789 [=======================>......] - ETA: 1s
14204928/17464789 [=======================>......] - ETA: 0s
14401536/17464789 [=======================>......] - ETA: 0s
14589952/17464789 [========================>.....] - ETA: 0s
14802944/17464789 [========================>.....] - ETA: 0s
14991360/17464789 [========================>.....] - ETA: 0s
15204352/17464789 [=========================>....] - ETA: 0s
15392768/17464789 [=========================>....] - ETA: 0s
15597568/17464789 [=========================>....] - ETA: 0s
15810560/17464789 [==========================>...] - ETA: 0s
16072704/17464789 [==========================>...] - ETA: 0s
16334848/17464789 [===========================>..] - ETA: 0s
16596992/17464789 [===========================>..] - ETA: 0s
16850944/17464789 [===========================>..] - ETA: 0s
17113088/17464789 [============================>.] - ETA: 0s
17375232/17464789 [============================>.] - ETA: 0s
17465344/17464789 [==============================] - 5s 0us/step
Pad sequences (samples x time)...

  #### Model init, fit   ############################################# 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 40, 50)       250         input_1[0][0]                    
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 38, 128)      19328       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 37, 128)      25728       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 36, 128)      32128       embedding_1[0][0]                
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
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 12s - loss: 7.9120 - accuracy: 0.4840
 2000/25000 [=>............................] - ETA: 8s - loss: 7.4136 - accuracy: 0.5165 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.4877 - accuracy: 0.5117
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.4558 - accuracy: 0.5138
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.5409 - accuracy: 0.5082
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.5465 - accuracy: 0.5078
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.5308 - accuracy: 0.5089
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.5420 - accuracy: 0.5081
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.5491 - accuracy: 0.5077
10000/25000 [===========>..................] - ETA: 3s - loss: 7.5608 - accuracy: 0.5069
11000/25000 [============>.................] - ETA: 3s - loss: 7.6262 - accuracy: 0.5026
12000/25000 [=============>................] - ETA: 3s - loss: 7.6360 - accuracy: 0.5020
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6513 - accuracy: 0.5010
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6666 - accuracy: 0.5000
15000/25000 [=================>............] - ETA: 2s - loss: 7.6646 - accuracy: 0.5001
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6714 - accuracy: 0.4997
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6504 - accuracy: 0.5011
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6411 - accuracy: 0.5017
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6521 - accuracy: 0.5009
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6513 - accuracy: 0.5010
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6498 - accuracy: 0.5011
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6624 - accuracy: 0.5003
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6626 - accuracy: 0.5003
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6622 - accuracy: 0.5003
25000/25000 [==============================] - 7s 282us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### save the trained model  ####################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}

  #### Predict   ##################################################### 
Loading data...

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/keras/initializers.py:119: calling RandomUniform.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}
(<mlmodels.util.Model_empty object at 0x7f20f2294748>, None)

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.textcnn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 
Model: "model_2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_2 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_2 (Embedding)         (None, 40, 50)       250         input_2[0][0]                    
__________________________________________________________________________________________________
conv1d_4 (Conv1D)               (None, 38, 128)      19328       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_5 (Conv1D)               (None, 37, 128)      25728       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_6 (Conv1D)               (None, 36, 128)      32128       embedding_2[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_4 (GlobalM (None, 128)          0           conv1d_4[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_5 (GlobalM (None, 128)          0           conv1d_5[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_6 (GlobalM (None, 128)          0           conv1d_6[0][0]                   
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 384)          0           global_max_pooling1d_4[0][0]     
                                                                 global_max_pooling1d_5[0][0]     
                                                                 global_max_pooling1d_6[0][0]     
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 1)            385         concatenate_2[0][0]              
==================================================================================================
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________

  <mlmodels.model_keras.textcnn.Model object at 0x7f20d4221278> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 10s - loss: 7.6360 - accuracy: 0.5020
 2000/25000 [=>............................] - ETA: 7s - loss: 7.6590 - accuracy: 0.5005 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.5746 - accuracy: 0.5060
 4000/25000 [===>..........................] - ETA: 5s - loss: 7.4750 - accuracy: 0.5125
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.6176 - accuracy: 0.5032
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.6590 - accuracy: 0.5005
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6338 - accuracy: 0.5021
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6436 - accuracy: 0.5015
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.6360 - accuracy: 0.5020
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6559 - accuracy: 0.5007
11000/25000 [============>.................] - ETA: 3s - loss: 7.7084 - accuracy: 0.4973
12000/25000 [=============>................] - ETA: 3s - loss: 7.6743 - accuracy: 0.4995
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6666 - accuracy: 0.5000
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6458 - accuracy: 0.5014
15000/25000 [=================>............] - ETA: 2s - loss: 7.6390 - accuracy: 0.5018
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6292 - accuracy: 0.5024
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6179 - accuracy: 0.5032
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6317 - accuracy: 0.5023
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6456 - accuracy: 0.5014
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6475 - accuracy: 0.5013
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6440 - accuracy: 0.5015
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6367 - accuracy: 0.5020
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6500 - accuracy: 0.5011
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6698 - accuracy: 0.4998
25000/25000 [==============================] - 7s 282us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### Predict   #################################################### 
Loading data...
(array([[1.],
       [1.],
       [1.],
       ...,
       [1.],
       [1.],
       [1.]], dtype=float32), None)

  #### Get  metrics   ################################################ 

  #### Save   ######################################################## 

  #### Load   ######################################################## 

  ############ Model preparation   ################################## 

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.textcnn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 
Model: "model_3"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_3 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_3 (Embedding)         (None, 40, 50)       250         input_3[0][0]                    
__________________________________________________________________________________________________
conv1d_7 (Conv1D)               (None, 38, 128)      19328       embedding_3[0][0]                
__________________________________________________________________________________________________
conv1d_8 (Conv1D)               (None, 37, 128)      25728       embedding_3[0][0]                
__________________________________________________________________________________________________
conv1d_9 (Conv1D)               (None, 36, 128)      32128       embedding_3[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_7 (GlobalM (None, 128)          0           conv1d_7[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_8 (GlobalM (None, 128)          0           conv1d_8[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_9 (GlobalM (None, 128)          0           conv1d_9[0][0]                   
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 384)          0           global_max_pooling1d_7[0][0]     
                                                                 global_max_pooling1d_8[0][0]     
                                                                 global_max_pooling1d_9[0][0]     
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            385         concatenate_3[0][0]              
==================================================================================================
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________

  ############ Model fit   ########################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 11s - loss: 7.6513 - accuracy: 0.5010
 2000/25000 [=>............................] - ETA: 8s - loss: 7.7050 - accuracy: 0.4975 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.7433 - accuracy: 0.4950
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.6896 - accuracy: 0.4985
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.6912 - accuracy: 0.4984
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.6998 - accuracy: 0.4978
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6732 - accuracy: 0.4996
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6494 - accuracy: 0.5011
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.6496 - accuracy: 0.5011
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6544 - accuracy: 0.5008
11000/25000 [============>.................] - ETA: 3s - loss: 7.6638 - accuracy: 0.5002
12000/25000 [=============>................] - ETA: 3s - loss: 7.6551 - accuracy: 0.5008
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6737 - accuracy: 0.4995
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6688 - accuracy: 0.4999
15000/25000 [=================>............] - ETA: 2s - loss: 7.6554 - accuracy: 0.5007
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6752 - accuracy: 0.4994
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6666 - accuracy: 0.5000
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6504 - accuracy: 0.5011
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6352 - accuracy: 0.5021
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6482 - accuracy: 0.5012
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6338 - accuracy: 0.5021
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6478 - accuracy: 0.5012
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6493 - accuracy: 0.5011
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6622 - accuracy: 0.5003
25000/25000 [==============================] - 7s 289us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
fit success None

  ############ Prediction############################################ 
Loading data...
(array([[1.],
       [1.],
       [1.],
       ...,
       [1.],
       [1.],
       [1.]], dtype=float32), None)

  ############ Save/ Load ############################################ 
Using TensorFlow backend.
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py:569: DeprecationWarning: invalid escape sequence \s
  """
/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/raw/char_cnn/data_utils.py:45: DeprecationWarning:

invalid escape sequence \s
