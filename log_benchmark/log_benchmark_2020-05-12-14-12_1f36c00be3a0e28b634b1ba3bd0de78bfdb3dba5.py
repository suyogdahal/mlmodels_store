
  test_benchmark /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_benchmark', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_benchmark 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5', 'workflow': 'test_benchmark'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_benchmark

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5

 ************************************************************************************************************************

  ############Check model ################################ 





 ************************************************************************************************************************

  timeseries 

  json_path /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/benchmark_timeseries/test02/model_list.json 

  Model List [{'model_pars': {'model_uri': 'model_gluon/fb_prophet.py'}, 'data_pars': {'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60, 'date_col': 'Date', 'freq': 'D', 'col_Xinput': 'Close'}, 'compute_pars': {'dummy': 'dummy'}, 'out_pars': {'outpath': 'ztest/model_fb/fb_prophet/'}}, {'model_pars': {'model_uri': 'model_keras.armdn.py', 'lstm_h_list': [300, 200, 24], 'last_lstm_neuron': 12, 'timesteps': 60, 'dropout_rate': 0.1, 'n_mixes': 3, 'dense_neuron': 10}, 'data_pars': {'train': True, 'col_Xinput': ['Close'], 'col_ytarget': 'Close', 'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60}, 'compute_pars': {'batch_size': 32, 'epochs': 10, 'learning_rate': 0.05, 'patience': 50}, 'out_pars': {'outpath': 'ztest/model_keras/armdn/'}}, {'hypermodel_pars': {}, 'data_pars': {'forecast_length': 60, 'backcast_length': 100, 'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'col_Xinput': ['Close'], 'col_ytarget': 'Close'}, 'model_pars': {'model_uri': 'model_tch.nbeats.py', 'forecast_length': 60, 'backcast_length': 100, 'stack_types': ['NBeatsNet.GENERIC_BLOCK', 'NBeatsNet.GENERIC_BLOCK'], 'device': 'cpu', 'nb_blocks_per_stack': 3, 'thetas_dims': [7, 8], 'share_weights_in_stack': 0, 'hidden_layer_units': 256}, 'compute_pars': {'batch_size': 100, 'disable_plot': 1, 'norm_constant': 1.0, 'result_path': 'ztest/model_tch/nbeats/n_beats_{}test.png', 'model_path': 'ztest/mycheckpoint'}, 'out_pars': {'out_path': 'mlmodels/ztest/model_tch/nbeats/', 'model_checkpoint': 'ztest/model_tch/nbeats/model_checkpoint/'}}, {'model_pars': {'model_name': 'deepar', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'use_feat_static_real': False, 'scaling': True, 'num_parallel_samples': 100}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepar/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_name': 'deepfactor', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_hidden_global': 50, 'num_layers_global': 1, 'num_factors': 10, 'num_hidden_local': 5, 'num_layers_local': 1, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'embedding_dimension': 10}, '_comment': {'distr_output': 'StudentTOutput()', 'cardinality': 'List[int] = list([1])', 'context_length': 'None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepfactor/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_name': 'wavenet', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'num_parallel_samples': 100, 'num_bins': 1024, 'hybridize_prediction_net': False, 'n_residue': 24, 'n_skip': 32, 'n_stacks': 1, 'temperature': 1.0, 'act_type': 'elu'}, '_comment': {'cardinality': 'List[int] = [1]', 'context_length': 'None', 'seasonality': 'Optional[int] = None', 'dilation_depth': 'Optional[int] = None', 'train_window_length': 'Optional[int] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_wavenet/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_name': 'transformer', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'dropout_rate': 0.1, 'model_dim': 32, 'inner_ff_dim_scale': 4, 'pre_seq': 'dn', 'post_seq': 'drn', 'act_type': 'softrelu', 'num_heads': 8, 'scaling': True, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False}, '_comment': {'cardinality': 'List[int] = list([1])', 'context_length': 'None', 'distr_output': 'DistributionOutput = StudentTOutput()', 'lags_seq': 'Optional[List[int]] = None', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_transformer/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_name': 'deepstate', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': [1], 'add_trend': False, 'num_periods_to_train': 4, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'scaling': True}, '_comment': {'past_length': 'Optional[int] = None', 'time_features': 'Optional[List[TimeFeature]] = None', 'noise_std_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'prior_cov_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'innovation_bounds': 'ParameterBounds = ParameterBounds(1e-6, 0.01)', 'embedding_dimension': 'Optional[List[int]] = None', 'issm: Optional[ISSM]': 'None', 'cardinality': 'List[int]'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepstate/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'gp_forecaster', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': 2, 'max_iter_jitter': 10, 'jitter_method': 'iter', 'sample_noise': True, 'num_parallel_samples': 100}, '_comment': {'context_length': 'Optional[int] = None', 'kernel_output': 'KernelOutput = RBFKernelOutput()', 'dtype': 'DType = np.float64', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_gpforecaster/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'feedforward', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'batch_normalization': False, 'mean_scaling': True, 'num_parallel_samples': 100}, '_comment': {'num_hidden_dimensions': 'Optional[List[int]] = None', 'context_length': 'Optional[int] = None', 'distr_output': 'DistributionOutput = StudentTOutput()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_feedforward/', 'plot_prob': True, 'quantiles': [0.5]}}, {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'seq2seq', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_parallel_samples': 100, 'cardinality': [2], 'embedding_dimension': 10, 'decoder_mlp_layer': [5, 10, 5], 'decoder_mlp_static_dim': 10, 'quantiles': [0.1, 0.5, 0.9]}, '_comment': {'encoder': 'Seq2SeqEncoder', 'context_length': 'Optional[int] = None', 'scaler': 'Scaler = NOPScaler()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_seq2seq/', 'plot_prob': True, 'quantiles': [0.5]}}] 

  


### Running {'model_pars': {'model_uri': 'model_gluon/fb_prophet.py'}, 'data_pars': {'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60, 'date_col': 'Date', 'freq': 'D', 'col_Xinput': 'Close'}, 'compute_pars': {'dummy': 'dummy'}, 'out_pars': {'outpath': 'ztest/model_fb/fb_prophet/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60, 'date_col': 'Date', 'freq': 'D', 'col_Xinput': 'Close'} {'outpath': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_fb/fb_prophet/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
INFO:numexpr.utils:NumExpr defaulting to 2 threads.
INFO:fbprophet:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
Initial log joint probability = -192.039
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
      99       9186.38     0.0272386        1207.2           1           1      123   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     199       10269.2     0.0242289       2566.31        0.89        0.89      233   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     299       10621.2     0.0237499       3262.95           1           1      343   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     399       10886.5     0.0339822       1343.14           1           1      459   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     499       11288.1    0.00255943       1266.79           1           1      580   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     599       11498.7     0.0166167       2146.51           1           1      698   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     699       11555.9     0.0104637       2039.91           1           1      812   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     799       11575.2    0.00955805       570.757           1           1      922   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     899       11630.7     0.0178715       1643.41      0.3435      0.3435     1036   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
     999       11700.1      0.034504       2394.16           1           1     1146   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1099       11744.7   0.000237394       144.685           1           1     1258   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1199       11753.1    0.00188838       552.132      0.4814           1     1372   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1299         11758    0.00101299       262.652      0.7415      0.7415     1490   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1399         11761   0.000712302       157.258           1           1     1606   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1499       11781.3     0.0243264       931.457           1           1     1717   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1599       11791.1     0.0025484       550.483      0.7644      0.7644     1834   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1699       11797.7    0.00732868       810.153           1           1     1952   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1799       11802.5   0.000319611       98.1955     0.04871           1     2077   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1818       11803.2   5.97419e-05       246.505   3.588e-07       0.001     2142  LS failed, Hessian reset 
    1855       11803.6   0.000110613       144.447   1.529e-06       0.001     2225  LS failed, Hessian reset 
    1899       11804.3   0.000976631       305.295           1           1     2275   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    1999       11805.4   4.67236e-05       72.2243      0.9487      0.9487     2391   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2033       11806.1   1.47341e-05       111.754   8.766e-08       0.001     2480  LS failed, Hessian reset 
    2099       11806.6   9.53816e-05       108.311      0.9684      0.9684     2563   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2151       11806.8   3.32394e-05       152.834   3.931e-07       0.001     2668  LS failed, Hessian reset 
    2199         11807    0.00273479       216.444           1           1     2723   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2299       11810.9    0.00793685       550.165           1           1     2837   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2399       11818.9     0.0134452       377.542           1           1     2952   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2499       11824.9     0.0041384       130.511           1           1     3060   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2525       11826.5   2.36518e-05       102.803   6.403e-08       0.001     3158  LS failed, Hessian reset 
    2599       11827.9   0.000370724       186.394      0.4637      0.4637     3242   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2606         11828   1.70497e-05       123.589     7.9e-08       0.001     3292  LS failed, Hessian reset 
    2699       11829.1    0.00168243       332.201           1           1     3407   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2709       11829.2   1.92694e-05       146.345   1.034e-07       0.001     3461  LS failed, Hessian reset 
    2746       11829.4   1.61976e-05       125.824   9.572e-08       0.001     3551  LS failed, Hessian reset 
    2799       11829.5    0.00491161       122.515           1           1     3615   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2899       11830.6   0.000250007       100.524           1           1     3742   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    2999       11830.9    0.00236328       193.309           1           1     3889   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3099       11831.3   0.000309242       194.211      0.7059      0.7059     4015   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3199       11831.4    1.3396e-05       91.8042      0.9217      0.9217     4136   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3299       11831.6   0.000373334       77.3538      0.3184           1     4256   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3399       11831.8   0.000125272       64.7127           1           1     4379   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3499         11832     0.0010491       69.8273           1           1     4503   
    Iter      log prob        ||dx||      ||grad||       alpha      alpha0  # evals  Notes 
    3553       11832.1   1.09422e-05       89.3197   8.979e-08       0.001     4612  LS failed, Hessian reset 
    3584       11832.1   8.65844e-07       55.9367      0.4252      0.4252     4658   
Optimization terminated normally: 
  Convergence detected: relative gradient magnitude is below tolerance
>>>model:  <mlmodels.model_gluon.fb_prophet.Model object at 0x7f1602ac3fd0> <class 'mlmodels.model_gluon.fb_prophet.Model'>

  #### Inference Need return ypred, ytrue ######################### 

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-12 14:12:47.356855
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   14.3339
metric_name                                  mean_absolute_error
Name: 0, dtype: object 

  date_run                              2020-05-12 14:12:47.360366
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   215.367
metric_name                                   mean_squared_error
Name: 1, dtype: object 

  date_run                              2020-05-12 14:12:47.363268
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   14.4309
metric_name                                median_absolute_error
Name: 2, dtype: object 

  date_run                              2020-05-12 14:12:47.366253
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  -18.2877
metric_name                                             r2_score
Name: 3, dtype: object 

  


### Running {'model_pars': {'model_uri': 'model_keras.armdn.py', 'lstm_h_list': [300, 200, 24], 'last_lstm_neuron': 12, 'timesteps': 60, 'dropout_rate': 0.1, 'n_mixes': 3, 'dense_neuron': 10}, 'data_pars': {'train': True, 'col_Xinput': ['Close'], 'col_ytarget': 'Close', 'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60}, 'compute_pars': {'batch_size': 32, 'epochs': 10, 'learning_rate': 0.05, 'patience': 50}, 'out_pars': {'outpath': 'ztest/model_keras/armdn/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'col_Xinput': ['Close'], 'col_ytarget': 'Close', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_test.csv', 'prediction_length': 60} {'outpath': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/armdn/'} 

  #### Setup Model   ############################################## 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_probability/python/distributions/mixture.py:154: Categorical.event_size (from tensorflow_probability.python.distributions.categorical) is deprecated and will be removed after 2019-05-19.
Instructions for updating:
The `event_size` property is deprecated.  Use `num_categories` instead.  They have the same value, but `event_size` is misnamed.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_ops.py:2509: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
LSTM_1 (LSTM)                (None, 60, 300)           362400    
_________________________________________________________________
LSTM_2 (LSTM)                (None, 60, 200)           400800    
_________________________________________________________________
LSTM_3 (LSTM)                (None, 60, 24)            21600     
_________________________________________________________________
LSTM_4 (LSTM)                (None, 12)                1776      
_________________________________________________________________
dense_1 (Dense)              (None, 10)                130       
_________________________________________________________________
mdn_1 (MDN)                  (None, 363)               3993      
=================================================================
Total params: 790,699
Trainable params: 790,699
Non-trainable params: 0
_________________________________________________________________

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_keras.armdn.Model object at 0x7f1602d17b00> <class 'mlmodels.model_keras.armdn.Model'>

  #### Loading dataset   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Epoch 1/10

1/1 [==============================] - 1s 1s/step - loss: 354634.1562
Epoch 2/10

1/1 [==============================] - 0s 97ms/step - loss: 258913.2500
Epoch 3/10

1/1 [==============================] - 0s 94ms/step - loss: 164818.1250
Epoch 4/10

1/1 [==============================] - 0s 95ms/step - loss: 95761.0938
Epoch 5/10

1/1 [==============================] - 0s 101ms/step - loss: 55267.9727
Epoch 6/10

1/1 [==============================] - 0s 94ms/step - loss: 32864.4922
Epoch 7/10

1/1 [==============================] - 0s 101ms/step - loss: 20184.3398
Epoch 8/10

1/1 [==============================] - 0s 96ms/step - loss: 12821.3682
Epoch 9/10

1/1 [==============================] - 0s 96ms/step - loss: 8874.6494
Epoch 10/10

1/1 [==============================] - 0s 112ms/step - loss: 6639.3896

  #### Inference Need return ypred, ytrue ######################### 
[[ 8.8203883e-01  6.2975806e-01 -2.3103573e+00  5.5065274e-01
   4.8847663e-01  8.8690341e-01 -1.2213969e+00 -1.5688196e+00
  -9.7554100e-01  2.4673371e-02  1.4419186e-01  1.1641312e-01
  -8.1231689e-01 -1.1100936e-01 -5.9698725e-01 -1.0561032e+00
   1.0634094e+00 -6.9682568e-02 -2.8715360e-01 -3.4623903e-01
   5.6256872e-01 -9.3240196e-01 -1.3890932e+00 -9.4462043e-01
   1.2576549e+00 -6.5322852e-01  2.8274876e-01 -1.5270730e+00
  -1.4639597e+00  2.0305850e-01 -8.2324600e-01  2.0026288e+00
  -8.4673440e-01 -2.3367832e+00  3.2526612e-01 -1.6008964e+00
   1.2740991e+00 -7.2713268e-01  1.4587691e+00  5.3938997e-01
   6.8583894e-01 -1.1007802e+00 -4.7383904e-01 -5.5148333e-01
   1.9773063e-01 -9.0439725e-01  9.2036188e-02 -2.2614837e+00
   9.1957396e-01  1.2724739e-01  1.5324211e+00  1.1232661e+00
  -1.2584329e-03  5.5471981e-01  1.0600902e+00 -7.7733505e-01
   1.6423086e+00 -9.7092152e-02 -4.5743972e-01  7.7822244e-01
   3.8729069e-01  7.8177299e+00  7.8431616e+00  7.2352419e+00
   9.2187967e+00  7.1253457e+00  9.6350822e+00  8.4554739e+00
   8.1585245e+00  8.2477341e+00  8.8899908e+00  8.2295933e+00
   7.9283838e+00  7.4158764e+00  8.5783825e+00  8.3007412e+00
   7.4853616e+00  9.4852343e+00  8.2995329e+00  8.4497356e+00
   9.0049152e+00  8.1633358e+00  9.0245094e+00  8.4657660e+00
   7.2264414e+00  7.1525116e+00  8.1466789e+00  8.2241106e+00
   8.0110455e+00  8.3072920e+00  8.3776388e+00  7.3635921e+00
   8.2258959e+00  9.4311361e+00  8.9110928e+00  1.0358416e+01
   6.9249911e+00  6.9293332e+00  7.4662266e+00  9.6913824e+00
   6.9266386e+00  8.6851664e+00  7.9638295e+00  8.1128616e+00
   8.3190203e+00  7.4720039e+00  7.2998195e+00  6.6196990e+00
   7.3980145e+00  6.6666064e+00  8.9289465e+00  7.8366508e+00
   8.1907692e+00  8.5839138e+00  9.1354847e+00  8.0802126e+00
   9.3793755e+00  8.7720966e+00  7.5999017e+00  9.8462887e+00
   3.9647076e-01  4.2942065e-01 -6.0899907e-01 -9.5768732e-01
   6.2696511e-01 -1.4614344e-01 -4.4839126e-01 -2.1356148e-01
   6.1883405e-03 -2.4933636e-02 -7.0766157e-01 -1.9094042e+00
   3.9365733e-01 -1.1992176e+00  1.4599878e+00  6.3757443e-01
  -1.5461528e-01  2.1135228e+00 -7.9050362e-01  1.3791070e+00
   1.2554240e+00  9.4409448e-01  9.5883548e-02 -8.8421381e-01
   6.9279885e-01  7.5320947e-01 -1.4387215e+00 -1.1057189e+00
   9.5119518e-01 -1.2532051e+00  9.9923676e-01 -1.2497197e-01
  -3.9979360e-01  1.3008660e+00 -6.4690202e-01  1.5868735e-01
   1.2735054e+00  1.3332453e+00  1.6411242e+00 -9.7974885e-01
   2.0381346e-01  1.8351171e+00 -3.1317770e-03 -8.1172287e-03
  -8.6170053e-01  5.5302465e-01 -7.3786533e-01  3.1303585e-02
  -1.4470148e+00  1.1200622e-01  1.4766066e+00 -1.6233169e+00
   5.7358545e-01  1.7740332e+00  5.7101834e-01  1.9137269e-01
   3.8771829e-01 -1.1185049e+00 -1.0733749e+00  6.6778445e-01
   5.4675567e-01  2.2576694e+00  7.5552976e-01  1.2964541e-01
   9.4005924e-01  7.3452127e-01  1.4771667e+00  2.5181575e+00
   2.0661201e+00  4.6586263e-01  2.9363209e-01  4.1483963e-01
   1.0343277e+00  2.0141888e-01  2.9678380e-01  2.1481092e+00
   1.2607784e+00  2.5103980e-01  4.2573196e-01  1.3238220e+00
   7.1879709e-01  1.5908488e+00  2.5683188e+00  1.9167731e+00
   1.7419189e-01  6.1618054e-01  1.5605510e+00  1.2491270e+00
   2.4736643e+00  2.6243477e+00  2.7444780e-01  1.5275280e+00
   3.6395586e-01  6.9796491e-01  1.4346957e+00  3.1823969e+00
   1.5016272e+00  1.8824965e+00  1.8897475e+00  9.2520899e-01
   2.3784661e+00  6.2093186e-01  6.2393838e-01  5.1234859e-01
   1.3990413e+00  1.5286180e+00  1.3314018e+00  2.7760181e+00
   2.0542870e+00  1.8166630e+00  9.8380852e-01  2.3705864e+00
   2.1060534e+00  2.0711348e+00  5.9260523e-01  2.5774662e+00
   2.0225329e+00  4.1242683e-01  2.3927002e+00  1.1023171e+00
   7.6753855e-02  7.3262868e+00  7.3752408e+00  8.7361765e+00
   9.2839584e+00  8.8606806e+00  8.2842312e+00  9.7125492e+00
   7.6151776e+00  8.4088354e+00  6.5961709e+00  1.0594096e+01
   9.3645840e+00  8.5119238e+00  9.1081028e+00  9.9964638e+00
   8.2605877e+00  7.2914243e+00  9.9203558e+00  8.2125053e+00
   8.3998747e+00  9.1978731e+00  8.7729330e+00  7.0442376e+00
   8.5506582e+00  7.0889893e+00  9.3432245e+00  6.7661710e+00
   8.9564571e+00  8.4409533e+00  9.7141972e+00  8.7799826e+00
   9.8085737e+00  9.0323057e+00  8.3125429e+00  9.3787413e+00
   9.9795046e+00  8.9431524e+00  7.9185033e+00  7.1593800e+00
   9.3355560e+00  7.6410394e+00  9.1321554e+00  7.6753612e+00
   6.7600789e+00  8.8151693e+00  8.3062487e+00  8.7251873e+00
   9.0237150e+00  6.8406215e+00  7.6059914e+00  8.2065811e+00
   8.3051424e+00  8.8394995e+00  8.4171305e+00  8.0406084e+00
   8.1394596e+00  7.6575108e+00  8.8719254e+00  1.0444375e+01
   1.2221937e+00  7.7258110e-02  2.1572328e+00  1.2444334e+00
   3.2899714e-01  2.0051618e+00  1.3406484e+00  5.8728766e-01
   8.6793989e-01  2.4685252e-01  1.6902413e+00  9.4563389e-01
   1.3460805e+00  1.6422534e-01  4.0362477e-01  2.0127082e+00
   2.1576309e+00  1.6969113e+00  2.1438866e+00  5.8563572e-01
   1.1142837e+00  2.2027931e+00  1.7452247e+00  1.9760621e-01
   2.7442141e+00  7.3749202e-01  1.9805760e+00  7.4921352e-01
   1.2472661e+00  1.3198808e+00  7.4631751e-01  2.0744190e+00
   3.2341685e+00  1.7213533e+00  2.1313190e-01  2.1369100e+00
   2.4066944e+00  6.8823463e-01  1.3459744e+00  1.3304477e+00
   4.6045446e-01  6.6616011e-01  5.4626721e-01  2.0327766e+00
   1.7900805e+00  1.2520063e-01  8.2247686e-01  7.8203082e-01
   1.9178098e-01  1.7604164e+00  1.4707863e-01  1.1212969e+00
   1.5408113e+00  9.5381355e-01  6.8309516e-01  8.6858582e-01
   2.8951383e-01  2.0388856e+00  3.2955754e-01  1.1639814e+00
  -6.0337415e+00  3.6999891e+00 -1.1530747e+01]]

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-12 14:12:57.570477
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   93.9331
metric_name                                  mean_absolute_error
Name: 4, dtype: object 

  date_run                              2020-05-12 14:12:57.575029
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   8843.98
metric_name                                   mean_squared_error
Name: 5, dtype: object 

  date_run                              2020-05-12 14:12:57.579226
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   93.8101
metric_name                                median_absolute_error
Name: 6, dtype: object 

  date_run                              2020-05-12 14:12:57.582713
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  -791.041
metric_name                                             r2_score
Name: 7, dtype: object 

  


### Running {'hypermodel_pars': {}, 'data_pars': {'forecast_length': 60, 'backcast_length': 100, 'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'col_Xinput': ['Close'], 'col_ytarget': 'Close'}, 'model_pars': {'model_uri': 'model_tch.nbeats.py', 'forecast_length': 60, 'backcast_length': 100, 'stack_types': ['NBeatsNet.GENERIC_BLOCK', 'NBeatsNet.GENERIC_BLOCK'], 'device': 'cpu', 'nb_blocks_per_stack': 3, 'thetas_dims': [7, 8], 'share_weights_in_stack': 0, 'hidden_layer_units': 256}, 'compute_pars': {'batch_size': 100, 'disable_plot': 1, 'norm_constant': 1.0, 'result_path': 'ztest/model_tch/nbeats/n_beats_{}test.png', 'model_path': 'ztest/mycheckpoint'}, 'out_pars': {'out_path': 'mlmodels/ztest/model_tch/nbeats/', 'model_checkpoint': 'ztest/model_tch/nbeats/model_checkpoint/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'forecast_length': 60, 'backcast_length': 100, 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_test.csv', 'col_Xinput': ['Close'], 'col_ytarget': 'Close'} {'out_path': 'mlmodels/ztest/model_tch/nbeats/', 'model_checkpoint': 'ztest/model_tch/nbeats/model_checkpoint/'} 

  #### Setup Model   ############################################## 
| N-Beats
| --  Stack Nbeatsnet.Generic_Block (#0) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @139732154107048
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @139731078529264
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @139731078529768
| --  Stack Nbeatsnet.Generic_Block (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @139731078530272
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @139731078530776
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @139731078531280

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.nbeats.Model object at 0x7f15ee6f0fd0> <class 'mlmodels.model_tch.nbeats.Model'>
[[0.40504701]
 [0.40695405]
 [0.39710839]
 ...
 [0.93587014]
 [0.95086039]
 [0.95547277]]
--- fiting ---
grad_step = 000000, loss = 0.506372
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.465721
grad_step = 000002, loss = 0.440218
grad_step = 000003, loss = 0.416616
grad_step = 000004, loss = 0.392269
grad_step = 000005, loss = 0.369587
grad_step = 000006, loss = 0.355948
grad_step = 000007, loss = 0.347058
grad_step = 000008, loss = 0.334583
grad_step = 000009, loss = 0.323108
grad_step = 000010, loss = 0.313273
grad_step = 000011, loss = 0.303773
grad_step = 000012, loss = 0.295264
grad_step = 000013, loss = 0.287664
grad_step = 000014, loss = 0.280145
grad_step = 000015, loss = 0.272090
grad_step = 000016, loss = 0.263284
grad_step = 000017, loss = 0.253810
grad_step = 000018, loss = 0.244269
grad_step = 000019, loss = 0.235693
grad_step = 000020, loss = 0.228709
grad_step = 000021, loss = 0.222347
grad_step = 000022, loss = 0.214959
grad_step = 000023, loss = 0.206640
grad_step = 000024, loss = 0.198648
grad_step = 000025, loss = 0.191606
grad_step = 000026, loss = 0.185187
grad_step = 000027, loss = 0.178796
grad_step = 000028, loss = 0.172121
grad_step = 000029, loss = 0.165272
grad_step = 000030, loss = 0.158651
grad_step = 000031, loss = 0.152596
grad_step = 000032, loss = 0.146955
grad_step = 000033, loss = 0.141248
grad_step = 000034, loss = 0.135389
grad_step = 000035, loss = 0.129698
grad_step = 000036, loss = 0.124381
grad_step = 000037, loss = 0.119377
grad_step = 000038, loss = 0.114509
grad_step = 000039, loss = 0.109652
grad_step = 000040, loss = 0.104837
grad_step = 000041, loss = 0.100201
grad_step = 000042, loss = 0.095815
grad_step = 000043, loss = 0.091643
grad_step = 000044, loss = 0.087621
grad_step = 000045, loss = 0.083683
grad_step = 000046, loss = 0.079822
grad_step = 000047, loss = 0.076127
grad_step = 000048, loss = 0.072640
grad_step = 000049, loss = 0.069281
grad_step = 000050, loss = 0.065986
grad_step = 000051, loss = 0.062825
grad_step = 000052, loss = 0.059857
grad_step = 000053, loss = 0.057012
grad_step = 000054, loss = 0.054225
grad_step = 000055, loss = 0.051546
grad_step = 000056, loss = 0.049022
grad_step = 000057, loss = 0.046608
grad_step = 000058, loss = 0.044271
grad_step = 000059, loss = 0.042042
grad_step = 000060, loss = 0.039950
grad_step = 000061, loss = 0.037950
grad_step = 000062, loss = 0.036003
grad_step = 000063, loss = 0.034147
grad_step = 000064, loss = 0.032402
grad_step = 000065, loss = 0.030741
grad_step = 000066, loss = 0.029150
grad_step = 000067, loss = 0.027632
grad_step = 000068, loss = 0.026193
grad_step = 000069, loss = 0.024836
grad_step = 000070, loss = 0.023539
grad_step = 000071, loss = 0.022293
grad_step = 000072, loss = 0.021120
grad_step = 000073, loss = 0.020020
grad_step = 000074, loss = 0.018968
grad_step = 000075, loss = 0.017963
grad_step = 000076, loss = 0.017020
grad_step = 000077, loss = 0.016132
grad_step = 000078, loss = 0.015285
grad_step = 000079, loss = 0.014482
grad_step = 000080, loss = 0.013732
grad_step = 000081, loss = 0.013022
grad_step = 000082, loss = 0.012347
grad_step = 000083, loss = 0.011713
grad_step = 000084, loss = 0.011118
grad_step = 000085, loss = 0.010555
grad_step = 000086, loss = 0.010023
grad_step = 000087, loss = 0.009525
grad_step = 000088, loss = 0.009056
grad_step = 000089, loss = 0.008613
grad_step = 000090, loss = 0.008198
grad_step = 000091, loss = 0.007809
grad_step = 000092, loss = 0.007442
grad_step = 000093, loss = 0.007096
grad_step = 000094, loss = 0.006773
grad_step = 000095, loss = 0.006470
grad_step = 000096, loss = 0.006184
grad_step = 000097, loss = 0.005916
grad_step = 000098, loss = 0.005666
grad_step = 000099, loss = 0.005429
grad_step = 000100, loss = 0.005208
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.005001
grad_step = 000102, loss = 0.004805
grad_step = 000103, loss = 0.004623
grad_step = 000104, loss = 0.004452
grad_step = 000105, loss = 0.004291
grad_step = 000106, loss = 0.004140
grad_step = 000107, loss = 0.004000
grad_step = 000108, loss = 0.003867
grad_step = 000109, loss = 0.003743
grad_step = 000110, loss = 0.003628
grad_step = 000111, loss = 0.003519
grad_step = 000112, loss = 0.003417
grad_step = 000113, loss = 0.003322
grad_step = 000114, loss = 0.003233
grad_step = 000115, loss = 0.003149
grad_step = 000116, loss = 0.003071
grad_step = 000117, loss = 0.002999
grad_step = 000118, loss = 0.002930
grad_step = 000119, loss = 0.002867
grad_step = 000120, loss = 0.002807
grad_step = 000121, loss = 0.002752
grad_step = 000122, loss = 0.002700
grad_step = 000123, loss = 0.002651
grad_step = 000124, loss = 0.002606
grad_step = 000125, loss = 0.002563
grad_step = 000126, loss = 0.002524
grad_step = 000127, loss = 0.002487
grad_step = 000128, loss = 0.002452
grad_step = 000129, loss = 0.002421
grad_step = 000130, loss = 0.002393
grad_step = 000131, loss = 0.002370
grad_step = 000132, loss = 0.002346
grad_step = 000133, loss = 0.002317
grad_step = 000134, loss = 0.002288
grad_step = 000135, loss = 0.002269
grad_step = 000136, loss = 0.002256
grad_step = 000137, loss = 0.002240
grad_step = 000138, loss = 0.002221
grad_step = 000139, loss = 0.002199
grad_step = 000140, loss = 0.002181
grad_step = 000141, loss = 0.002168
grad_step = 000142, loss = 0.002160
grad_step = 000143, loss = 0.002155
grad_step = 000144, loss = 0.002153
grad_step = 000145, loss = 0.002154
grad_step = 000146, loss = 0.002143
grad_step = 000147, loss = 0.002124
grad_step = 000148, loss = 0.002101
grad_step = 000149, loss = 0.002086
grad_step = 000150, loss = 0.002082
grad_step = 000151, loss = 0.002086
grad_step = 000152, loss = 0.002094
grad_step = 000153, loss = 0.002091
grad_step = 000154, loss = 0.002083
grad_step = 000155, loss = 0.002059
grad_step = 000156, loss = 0.002045
grad_step = 000157, loss = 0.002042
grad_step = 000158, loss = 0.002048
grad_step = 000159, loss = 0.002057
grad_step = 000160, loss = 0.002044
grad_step = 000161, loss = 0.002031
grad_step = 000162, loss = 0.002021
grad_step = 000163, loss = 0.002020
grad_step = 000164, loss = 0.002026
grad_step = 000165, loss = 0.002030
grad_step = 000166, loss = 0.002036
grad_step = 000167, loss = 0.002026
grad_step = 000168, loss = 0.002018
grad_step = 000169, loss = 0.002007
grad_step = 000170, loss = 0.002000
grad_step = 000171, loss = 0.001998
grad_step = 000172, loss = 0.001999
grad_step = 000173, loss = 0.002004
grad_step = 000174, loss = 0.002004
grad_step = 000175, loss = 0.002006
grad_step = 000176, loss = 0.001999
grad_step = 000177, loss = 0.001994
grad_step = 000178, loss = 0.001986
grad_step = 000179, loss = 0.001982
grad_step = 000180, loss = 0.001980
grad_step = 000181, loss = 0.001979
grad_step = 000182, loss = 0.001980
grad_step = 000183, loss = 0.001983
grad_step = 000184, loss = 0.001994
grad_step = 000185, loss = 0.002001
grad_step = 000186, loss = 0.002025
grad_step = 000187, loss = 0.002015
grad_step = 000188, loss = 0.002010
grad_step = 000189, loss = 0.001973
grad_step = 000190, loss = 0.001970
grad_step = 000191, loss = 0.001994
grad_step = 000192, loss = 0.001983
grad_step = 000193, loss = 0.001964
grad_step = 000194, loss = 0.001960
grad_step = 000195, loss = 0.001974
grad_step = 000196, loss = 0.001995
grad_step = 000197, loss = 0.001986
grad_step = 000198, loss = 0.001976
grad_step = 000199, loss = 0.001954
grad_step = 000200, loss = 0.001947
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.001955
grad_step = 000202, loss = 0.001962
grad_step = 000203, loss = 0.001970
grad_step = 000204, loss = 0.001956
grad_step = 000205, loss = 0.001944
grad_step = 000206, loss = 0.001939
grad_step = 000207, loss = 0.001944
grad_step = 000208, loss = 0.001955
grad_step = 000209, loss = 0.001950
grad_step = 000210, loss = 0.001943
grad_step = 000211, loss = 0.001931
grad_step = 000212, loss = 0.001930
grad_step = 000213, loss = 0.001936
grad_step = 000214, loss = 0.001941
grad_step = 000215, loss = 0.001947
grad_step = 000216, loss = 0.001937
grad_step = 000217, loss = 0.001930
grad_step = 000218, loss = 0.001921
grad_step = 000219, loss = 0.001918
grad_step = 000220, loss = 0.001918
grad_step = 000221, loss = 0.001920
grad_step = 000222, loss = 0.001924
grad_step = 000223, loss = 0.001925
grad_step = 000224, loss = 0.001931
grad_step = 000225, loss = 0.001927
grad_step = 000226, loss = 0.001928
grad_step = 000227, loss = 0.001919
grad_step = 000228, loss = 0.001912
grad_step = 000229, loss = 0.001904
grad_step = 000230, loss = 0.001901
grad_step = 000231, loss = 0.001902
grad_step = 000232, loss = 0.001905
grad_step = 000233, loss = 0.001911
grad_step = 000234, loss = 0.001915
grad_step = 000235, loss = 0.001928
grad_step = 000236, loss = 0.001928
grad_step = 000237, loss = 0.001938
grad_step = 000238, loss = 0.001920
grad_step = 000239, loss = 0.001910
grad_step = 000240, loss = 0.001891
grad_step = 000241, loss = 0.001886
grad_step = 000242, loss = 0.001895
grad_step = 000243, loss = 0.001900
grad_step = 000244, loss = 0.001906
grad_step = 000245, loss = 0.001894
grad_step = 000246, loss = 0.001886
grad_step = 000247, loss = 0.001878
grad_step = 000248, loss = 0.001873
grad_step = 000249, loss = 0.001871
grad_step = 000250, loss = 0.001871
grad_step = 000251, loss = 0.001872
grad_step = 000252, loss = 0.001875
grad_step = 000253, loss = 0.001885
grad_step = 000254, loss = 0.001895
grad_step = 000255, loss = 0.001922
grad_step = 000256, loss = 0.001925
grad_step = 000257, loss = 0.001941
grad_step = 000258, loss = 0.001901
grad_step = 000259, loss = 0.001870
grad_step = 000260, loss = 0.001859
grad_step = 000261, loss = 0.001875
grad_step = 000262, loss = 0.001888
grad_step = 000263, loss = 0.001873
grad_step = 000264, loss = 0.001857
grad_step = 000265, loss = 0.001847
grad_step = 000266, loss = 0.001850
grad_step = 000267, loss = 0.001863
grad_step = 000268, loss = 0.001883
grad_step = 000269, loss = 0.001922
grad_step = 000270, loss = 0.001933
grad_step = 000271, loss = 0.001958
grad_step = 000272, loss = 0.001904
grad_step = 000273, loss = 0.001862
grad_step = 000274, loss = 0.001835
grad_step = 000275, loss = 0.001851
grad_step = 000276, loss = 0.001880
grad_step = 000277, loss = 0.001864
grad_step = 000278, loss = 0.001834
grad_step = 000279, loss = 0.001832
grad_step = 000280, loss = 0.001853
grad_step = 000281, loss = 0.001877
grad_step = 000282, loss = 0.001859
grad_step = 000283, loss = 0.001837
grad_step = 000284, loss = 0.001820
grad_step = 000285, loss = 0.001820
grad_step = 000286, loss = 0.001831
grad_step = 000287, loss = 0.001839
grad_step = 000288, loss = 0.001844
grad_step = 000289, loss = 0.001830
grad_step = 000290, loss = 0.001817
grad_step = 000291, loss = 0.001809
grad_step = 000292, loss = 0.001810
grad_step = 000293, loss = 0.001817
grad_step = 000294, loss = 0.001818
grad_step = 000295, loss = 0.001817
grad_step = 000296, loss = 0.001807
grad_step = 000297, loss = 0.001800
grad_step = 000298, loss = 0.001797
grad_step = 000299, loss = 0.001798
grad_step = 000300, loss = 0.001801
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.001804
grad_step = 000302, loss = 0.001808
grad_step = 000303, loss = 0.001809
grad_step = 000304, loss = 0.001812
grad_step = 000305, loss = 0.001806
grad_step = 000306, loss = 0.001802
grad_step = 000307, loss = 0.001792
grad_step = 000308, loss = 0.001784
grad_step = 000309, loss = 0.001780
grad_step = 000310, loss = 0.001780
grad_step = 000311, loss = 0.001783
grad_step = 000312, loss = 0.001785
grad_step = 000313, loss = 0.001791
grad_step = 000314, loss = 0.001793
grad_step = 000315, loss = 0.001800
grad_step = 000316, loss = 0.001800
grad_step = 000317, loss = 0.001807
grad_step = 000318, loss = 0.001800
grad_step = 000319, loss = 0.001797
grad_step = 000320, loss = 0.001782
grad_step = 000321, loss = 0.001770
grad_step = 000322, loss = 0.001761
grad_step = 000323, loss = 0.001759
grad_step = 000324, loss = 0.001764
grad_step = 000325, loss = 0.001770
grad_step = 000326, loss = 0.001782
grad_step = 000327, loss = 0.001792
grad_step = 000328, loss = 0.001820
grad_step = 000329, loss = 0.001836
grad_step = 000330, loss = 0.001877
grad_step = 000331, loss = 0.001857
grad_step = 000332, loss = 0.001839
grad_step = 000333, loss = 0.001781
grad_step = 000334, loss = 0.001746
grad_step = 000335, loss = 0.001755
grad_step = 000336, loss = 0.001784
grad_step = 000337, loss = 0.001802
grad_step = 000338, loss = 0.001783
grad_step = 000339, loss = 0.001767
grad_step = 000340, loss = 0.001743
grad_step = 000341, loss = 0.001731
grad_step = 000342, loss = 0.001728
grad_step = 000343, loss = 0.001732
grad_step = 000344, loss = 0.001744
grad_step = 000345, loss = 0.001757
grad_step = 000346, loss = 0.001782
grad_step = 000347, loss = 0.001794
grad_step = 000348, loss = 0.001819
grad_step = 000349, loss = 0.001800
grad_step = 000350, loss = 0.001781
grad_step = 000351, loss = 0.001740
grad_step = 000352, loss = 0.001716
grad_step = 000353, loss = 0.001721
grad_step = 000354, loss = 0.001741
grad_step = 000355, loss = 0.001756
grad_step = 000356, loss = 0.001751
grad_step = 000357, loss = 0.001740
grad_step = 000358, loss = 0.001722
grad_step = 000359, loss = 0.001710
grad_step = 000360, loss = 0.001702
grad_step = 000361, loss = 0.001698
grad_step = 000362, loss = 0.001696
grad_step = 000363, loss = 0.001695
grad_step = 000364, loss = 0.001695
grad_step = 000365, loss = 0.001698
grad_step = 000366, loss = 0.001705
grad_step = 000367, loss = 0.001716
grad_step = 000368, loss = 0.001743
grad_step = 000369, loss = 0.001776
grad_step = 000370, loss = 0.001846
grad_step = 000371, loss = 0.001872
grad_step = 000372, loss = 0.001916
grad_step = 000373, loss = 0.001837
grad_step = 000374, loss = 0.001737
grad_step = 000375, loss = 0.001683
grad_step = 000376, loss = 0.001714
grad_step = 000377, loss = 0.001777
grad_step = 000378, loss = 0.001791
grad_step = 000379, loss = 0.001770
grad_step = 000380, loss = 0.001709
grad_step = 000381, loss = 0.001673
grad_step = 000382, loss = 0.001666
grad_step = 000383, loss = 0.001683
grad_step = 000384, loss = 0.001722
grad_step = 000385, loss = 0.001757
grad_step = 000386, loss = 0.001805
grad_step = 000387, loss = 0.001802
grad_step = 000388, loss = 0.001796
grad_step = 000389, loss = 0.001728
grad_step = 000390, loss = 0.001673
grad_step = 000391, loss = 0.001653
grad_step = 000392, loss = 0.001674
grad_step = 000393, loss = 0.001704
grad_step = 000394, loss = 0.001703
grad_step = 000395, loss = 0.001678
grad_step = 000396, loss = 0.001650
grad_step = 000397, loss = 0.001643
grad_step = 000398, loss = 0.001655
grad_step = 000399, loss = 0.001675
grad_step = 000400, loss = 0.001702
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.001712
grad_step = 000402, loss = 0.001726
grad_step = 000403, loss = 0.001711
grad_step = 000404, loss = 0.001699
grad_step = 000405, loss = 0.001668
grad_step = 000406, loss = 0.001644
grad_step = 000407, loss = 0.001628
grad_step = 000408, loss = 0.001626
grad_step = 000409, loss = 0.001635
grad_step = 000410, loss = 0.001644
grad_step = 000411, loss = 0.001646
grad_step = 000412, loss = 0.001638
grad_step = 000413, loss = 0.001629
grad_step = 000414, loss = 0.001619
grad_step = 000415, loss = 0.001613
grad_step = 000416, loss = 0.001611
grad_step = 000417, loss = 0.001611
grad_step = 000418, loss = 0.001615
grad_step = 000419, loss = 0.001620
grad_step = 000420, loss = 0.001630
grad_step = 000421, loss = 0.001644
grad_step = 000422, loss = 0.001672
grad_step = 000423, loss = 0.001695
grad_step = 000424, loss = 0.001738
grad_step = 000425, loss = 0.001748
grad_step = 000426, loss = 0.001750
grad_step = 000427, loss = 0.001698
grad_step = 000428, loss = 0.001640
grad_step = 000429, loss = 0.001598
grad_step = 000430, loss = 0.001594
grad_step = 000431, loss = 0.001619
grad_step = 000432, loss = 0.001652
grad_step = 000433, loss = 0.001685
grad_step = 000434, loss = 0.001691
grad_step = 000435, loss = 0.001706
grad_step = 000436, loss = 0.001683
grad_step = 000437, loss = 0.001668
grad_step = 000438, loss = 0.001629
grad_step = 000439, loss = 0.001596
grad_step = 000440, loss = 0.001574
grad_step = 000441, loss = 0.001572
grad_step = 000442, loss = 0.001585
grad_step = 000443, loss = 0.001600
grad_step = 000444, loss = 0.001610
grad_step = 000445, loss = 0.001608
grad_step = 000446, loss = 0.001603
grad_step = 000447, loss = 0.001590
grad_step = 000448, loss = 0.001581
grad_step = 000449, loss = 0.001572
grad_step = 000450, loss = 0.001565
grad_step = 000451, loss = 0.001559
grad_step = 000452, loss = 0.001555
grad_step = 000453, loss = 0.001551
grad_step = 000454, loss = 0.001548
grad_step = 000455, loss = 0.001545
grad_step = 000456, loss = 0.001543
grad_step = 000457, loss = 0.001541
grad_step = 000458, loss = 0.001539
grad_step = 000459, loss = 0.001537
grad_step = 000460, loss = 0.001536
grad_step = 000461, loss = 0.001535
grad_step = 000462, loss = 0.001535
grad_step = 000463, loss = 0.001537
grad_step = 000464, loss = 0.001544
grad_step = 000465, loss = 0.001560
grad_step = 000466, loss = 0.001600
grad_step = 000467, loss = 0.001672
grad_step = 000468, loss = 0.001848
grad_step = 000469, loss = 0.002052
grad_step = 000470, loss = 0.002369
grad_step = 000471, loss = 0.002181
grad_step = 000472, loss = 0.001764
grad_step = 000473, loss = 0.001544
grad_step = 000474, loss = 0.001778
grad_step = 000475, loss = 0.002020
grad_step = 000476, loss = 0.001747
grad_step = 000477, loss = 0.001525
grad_step = 000478, loss = 0.001659
grad_step = 000479, loss = 0.001823
grad_step = 000480, loss = 0.001835
grad_step = 000481, loss = 0.001552
grad_step = 000482, loss = 0.001547
grad_step = 000483, loss = 0.001725
grad_step = 000484, loss = 0.001787
grad_step = 000485, loss = 0.001610
grad_step = 000486, loss = 0.001504
grad_step = 000487, loss = 0.001598
grad_step = 000488, loss = 0.001704
grad_step = 000489, loss = 0.001583
grad_step = 000490, loss = 0.001492
grad_step = 000491, loss = 0.001554
grad_step = 000492, loss = 0.001621
grad_step = 000493, loss = 0.001563
grad_step = 000494, loss = 0.001482
grad_step = 000495, loss = 0.001514
grad_step = 000496, loss = 0.001588
grad_step = 000497, loss = 0.001553
grad_step = 000498, loss = 0.001479
grad_step = 000499, loss = 0.001482
grad_step = 000500, loss = 0.001526
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.001530
Finished.

  #### Inference Need return ypred, ytrue ######################### 
[[0.40504701]
 [0.40695405]
 [0.39710839]
 ...
 [0.93587014]
 [0.95086039]
 [0.95547277]]

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-12 14:13:20.426116
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.248665
metric_name                                  mean_absolute_error
Name: 8, dtype: object 

  date_run                              2020-05-12 14:13:20.431436
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.147986
metric_name                                   mean_squared_error
Name: 9, dtype: object 

  date_run                              2020-05-12 14:13:20.438201
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.155936
metric_name                                median_absolute_error
Name: 10, dtype: object 

  date_run                              2020-05-12 14:13:20.444437
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  -1.24869
metric_name                                             r2_score
Name: 11, dtype: object 

  


### Running {'model_pars': {'model_name': 'deepar', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'use_feat_static_real': False, 'scaling': True, 'num_parallel_samples': 100}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepar/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepar/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_name': 'deepar', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'use_feat_static_real': False, 'scaling': True, 'num_parallel_samples': 100}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepar/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_name': 'deepfactor', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_hidden_global': 50, 'num_layers_global': 1, 'num_factors': 10, 'num_hidden_local': 5, 'num_layers_local': 1, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'embedding_dimension': 10}, '_comment': {'distr_output': 'StudentTOutput()', 'cardinality': 'List[int] = list([1])', 'context_length': 'None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepfactor/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepfactor/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_name': 'deepfactor', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_hidden_global': 50, 'num_layers_global': 1, 'num_factors': 10, 'num_hidden_local': 5, 'num_layers_local': 1, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'embedding_dimension': 10}, '_comment': {'distr_output': 'StudentTOutput()', 'cardinality': 'List[int] = list([1])', 'context_length': 'None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepfactor/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_name': 'wavenet', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'num_parallel_samples': 100, 'num_bins': 1024, 'hybridize_prediction_net': False, 'n_residue': 24, 'n_skip': 32, 'n_stacks': 1, 'temperature': 1.0, 'act_type': 'elu'}, '_comment': {'cardinality': 'List[int] = [1]', 'context_length': 'None', 'seasonality': 'Optional[int] = None', 'dilation_depth': 'Optional[int] = None', 'train_window_length': 'Optional[int] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_wavenet/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_wavenet/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

  {'model_pars': {'model_name': 'wavenet', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'num_parallel_samples': 100, 'num_bins': 1024, 'hybridize_prediction_net': False, 'n_residue': 24, 'n_skip': 32, 'n_stacks': 1, 'temperature': 1.0, 'act_type': 'elu'}, '_comment': {'cardinality': 'List[int] = [1]', 'context_length': 'None', 'seasonality': 'Optional[int] = None', 'dilation_depth': 'Optional[int] = None', 'train_window_length': 'Optional[int] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_wavenet/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_name': 'transformer', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'dropout_rate': 0.1, 'model_dim': 32, 'inner_ff_dim_scale': 4, 'pre_seq': 'dn', 'post_seq': 'drn', 'act_type': 'softrelu', 'num_heads': 8, 'scaling': True, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False}, '_comment': {'cardinality': 'List[int] = list([1])', 'context_length': 'None', 'distr_output': 'DistributionOutput = StudentTOutput()', 'lags_seq': 'Optional[List[int]] = None', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_transformer/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_transformer/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_name': 'transformer', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'dropout_rate': 0.1, 'model_dim': 32, 'inner_ff_dim_scale': 4, 'pre_seq': 'dn', 'post_seq': 'drn', 'act_type': 'softrelu', 'num_heads': 8, 'scaling': True, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False}, '_comment': {'cardinality': 'List[int] = list([1])', 'context_length': 'None', 'distr_output': 'DistributionOutput = StudentTOutput()', 'lags_seq': 'Optional[List[int]] = None', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_transformer/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_name': 'deepstate', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': [1], 'add_trend': False, 'num_periods_to_train': 4, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'scaling': True}, '_comment': {'past_length': 'Optional[int] = None', 'time_features': 'Optional[List[TimeFeature]] = None', 'noise_std_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'prior_cov_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'innovation_bounds': 'ParameterBounds = ParameterBounds(1e-6, 0.01)', 'embedding_dimension': 'Optional[List[int]] = None', 'issm: Optional[ISSM]': 'None', 'cardinality': 'List[int]'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_deepstate/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepstate/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_name': 'deepstate', 'model_uri': 'model_gluon.gluonts_model', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': [1], 'add_trend': False, 'num_periods_to_train': 4, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'scaling': True}, '_comment': {'past_length': 'Optional[int] = None', 'time_features': 'Optional[List[TimeFeature]] = None', 'noise_std_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'prior_cov_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'innovation_bounds': 'ParameterBounds = ParameterBounds(1e-6, 0.01)', 'embedding_dimension': 'Optional[List[int]] = None', 'issm: Optional[ISSM]': 'None', 'cardinality': 'List[int]'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_deepstate/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'gp_forecaster', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': 2, 'max_iter_jitter': 10, 'jitter_method': 'iter', 'sample_noise': True, 'num_parallel_samples': 100}, '_comment': {'context_length': 'Optional[int] = None', 'kernel_output': 'KernelOutput = RBFKernelOutput()', 'dtype': 'DType = np.float64', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_gpforecaster/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_gpforecaster/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,

  {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'gp_forecaster', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': 2, 'max_iter_jitter': 10, 'jitter_method': 'iter', 'sample_noise': True, 'num_parallel_samples': 100}, '_comment': {'context_length': 'Optional[int] = None', 'kernel_output': 'KernelOutput = RBFKernelOutput()', 'dtype': 'DType = np.float64', 'time_features': 'Optional[List[TimeFeature]] = None'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_gpforecaster/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'feedforward', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'batch_normalization': False, 'mean_scaling': True, 'num_parallel_samples': 100}, '_comment': {'num_hidden_dimensions': 'Optional[List[int]] = None', 'context_length': 'Optional[int] = None', 'distr_output': 'DistributionOutput = StudentTOutput()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_feedforward/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_feedforward/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'feedforward', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'batch_normalization': False, 'mean_scaling': True, 'num_parallel_samples': 100}, '_comment': {'num_hidden_dimensions': 'Optional[List[int]] = None', 'context_length': 'Optional[int] = None', 'distr_output': 'DistributionOutput = StudentTOutput()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_feedforward/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  


### Running {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'seq2seq', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_parallel_samples': 100, 'cardinality': [2], 'embedding_dimension': 10, 'decoder_mlp_layer': [5, 10, 5], 'decoder_mlp_static_dim': 10, 'quantiles': [0.1, 0.5, 0.9]}, '_comment': {'encoder': 'Seq2SeqEncoder', 'context_length': 'Optional[int] = None', 'scaler': 'Scaler = NOPScaler()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': 'ztest/model_gluon/gluonts_seq2seq/', 'plot_prob': True, 'quantiles': [0.5]}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_seq2seq/', 'plot_prob': True, 'quantiles': [0.5]} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_uri': 'model_gluon.gluonts_model', 'model_name': 'seq2seq', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_parallel_samples': 100, 'cardinality': [2], 'embedding_dimension': 10, 'decoder_mlp_layer': [5, 10, 5], 'decoder_mlp_static_dim': 10, 'quantiles': [0.1, 0.5, 0.9]}, '_comment': {'encoder': 'Seq2SeqEncoder', 'context_length': 'Optional[int] = None', 'scaler': 'Scaler = NOPScaler()'}}, 'data_pars': {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []}, 'compute_pars': {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_gluon/gluonts_seq2seq/', 'plot_prob': True, 'quantiles': [0.5]}} Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range 

  benchmark file saved at /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark/timeseries/test02/model_list.json 

                        date_run  ...            metric_name
0   2020-05-12 14:12:47.356855  ...    mean_absolute_error
1   2020-05-12 14:12:47.360366  ...     mean_squared_error
2   2020-05-12 14:12:47.363268  ...  median_absolute_error
3   2020-05-12 14:12:47.366253  ...               r2_score
4   2020-05-12 14:12:57.570477  ...    mean_absolute_error
5   2020-05-12 14:12:57.575029  ...     mean_squared_error
6   2020-05-12 14:12:57.579226  ...  median_absolute_error
7   2020-05-12 14:12:57.582713  ...               r2_score
8   2020-05-12 14:13:20.426116  ...    mean_absolute_error
9   2020-05-12 14:13:20.431436  ...     mean_squared_error
10  2020-05-12 14:13:20.438201  ...  median_absolute_error
11  2020-05-12 14:13:20.444437  ...               r2_score

[12 rows x 6 columns] 
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do timeseries 





 ************************************************************************************************************************

  vision_mnist 

  json_path /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/benchmark_cnn/mnist 

  Model List [{'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext101_32x8d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext101_32x8d/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnext101_32x8d/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet18', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet18/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet18/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet152', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet152/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet34', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet34/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x0_5', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/checkpoints/', 'path': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet50_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet50_2/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet101', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet101/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet50', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet50/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet101_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet101_2/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x1_0', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/checkpoints/', 'path': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/'}}, {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext50_32x4d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnext50_32x4d/'}}] 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext101_32x8d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext101_32x8d/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnext101_32x8d/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnext101_32x8d/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnext101_32x8d/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
Downloading: "https://github.com/pytorch/vision/archive/master.zip" to /home/runner/.cache/torch/hub/master.zip
0it [00:00, ?it/s]  0%|          | 16384/9912422 [00:00<01:19, 124762.12it/s] 81%|████████  | 7995392/9912422 [00:00<00:10, 178111.85it/s]9920512it [00:00, 40020123.88it/s]                           
0it [00:00, ?it/s]32768it [00:00, 607183.20it/s]
0it [00:00, ?it/s]  2%|▏         | 40960/1648877 [00:00<00:03, 408465.84it/s]1654784it [00:00, 11384992.53it/s]                         
0it [00:00, ?it/s]8192it [00:00, 160086.75it/s]>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4fb372fd0> <class 'mlmodels.model_tch.torchhub.Model'>
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Processing...
Done!

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext101_32x8d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext101_32x8d/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnext101_32x8d/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet18', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet18/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet18/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet18/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc498a8eef0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet18', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet18/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet152', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet152/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet152/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4fb2fdef0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet152', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet152/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet34', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet34/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet34/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4985660f0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet34', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet34/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x0_5', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/checkpoints/', 'path': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x0_5/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4fb372fd0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x0_5', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x0_5/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet50_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet50_2/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet50_2/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4adcf7e80> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet50_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet50_2/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet101', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet101/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet101/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4fb372fd0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet101', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet101/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet50', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet50/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet50/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4a21a9748> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet50', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet50/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet101_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet101_2/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet101_2/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4fb33acc0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet101_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet101_2/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x1_0', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/checkpoints/', 'path': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x1_0/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc4adcf7e80> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x1_0', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x1_0/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext50_32x4d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnext50_32x4d/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnext50_32x4d/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7fc498a8efd0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext50_32x4d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnext50_32x4d/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  benchmark file saved at /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark/cnn/mnist 

  Empty DataFrame
Columns: [date_run, model_uri, json, dataset_uri, metric, metric_name]
Index: [] 
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do vision_mnist 





 ************************************************************************************************************************

  fashion_vision_mnist 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 284, in <module>
    main()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 281, in main
    raise Exception("No options")
Exception: No options
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do fashion_vision_mnist 





 ************************************************************************************************************************

  text_classification 

  json_path /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/benchmark_text_classification/model_list_bench01.json 

  Model List [{'hypermodel_pars': {}, 'data_pars': {'data_path': 'dataset/recommender/IMDB_sample.txt', 'train_path': 'dataset/recommender/IMDB_train.csv', 'valid_path': 'dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}}, {'model_pars': {'model_uri': 'model_keras.textcnn.py', 'maxlen': 40, 'max_features': 5, 'embedding_dims': 50}, 'data_pars': {'path': 'dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5}, 'compute_pars': {'engine': 'adam', 'loss': 'binary_crossentropy', 'metrics': ['accuracy'], 'batch_size': 1000, 'epochs': 1}, 'out_pars': {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'}}] 

  


### Running {'hypermodel_pars': {}, 'data_pars': {'data_path': 'dataset/recommender/IMDB_sample.txt', 'train_path': 'dataset/recommender/IMDB_train.csv', 'valid_path': 'dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64} {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'} 

  #### Setup Model   ############################################## 
{'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.textcnn.Model object at 0x7f1d444451d0> <class 'mlmodels.model_tch.textcnn.Model'>
Spliting original file to train/valid set...

  Download en 
Collecting en_core_web_sm==2.2.5
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.5/en_core_web_sm-2.2.5.tar.gz (12.0 MB)
Requirement already satisfied: spacy>=2.2.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from en_core_web_sm==2.2.5) (2.2.4)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.0.3)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.23.0)
Requirement already satisfied: numpy>=1.15.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.18.4)
Requirement already satisfied: plac<1.2.0,>=0.9.6 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.1.3)
Requirement already satisfied: blis<0.5.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.4.1)
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (45.2.0)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (4.46.0)
Requirement already satisfied: thinc==7.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (7.4.0)
Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.6.0)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.2)
Requirement already satisfied: srsly<1.1.0,>=1.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: catalogue<1.1.0,>=0.0.7 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.0)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: idna<3,>=2.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2.9)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.25.9)
Requirement already satisfied: certifi>=2017.4.17 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2020.4.5.1)
Requirement already satisfied: chardet<4,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.4)
Requirement already satisfied: importlib-metadata>=0.20; python_version < "3.8" in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.6.0)
Requirement already satisfied: zipp>=0.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from importlib-metadata>=0.20; python_version < "3.8"->catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.1.0)
Building wheels for collected packages: en-core-web-sm
  Building wheel for en-core-web-sm (setup.py): started
  Building wheel for en-core-web-sm (setup.py): finished with status 'done'
  Created wheel for en-core-web-sm: filename=en_core_web_sm-2.2.5-py3-none-any.whl size=12011738 sha256=f487be55f9eabecb4880b50f5a9b4cfaecf6da6ab17d54fe1148b47095a2784c
  Stored in directory: /tmp/pip-ephem-wheel-cache-xval2cnd/wheels/b5/94/56/596daa677d7e91038cbddfcf32b591d0c915a1b3a3e3d3c79d
Successfully built en-core-web-sm
Installing collected packages: en-core-web-sm
Successfully installed en-core-web-sm-2.2.5
WARNING: You are using pip version 20.0.2; however, version 20.1 is available.
You should consider upgrading via the '/opt/hostedtoolcache/Python/3.6.10/x64/bin/python -m pip install --upgrade pip' command.
[38;5;2m✔ Download and installation successful[0m
You can now load the model via spacy.load('en_core_web_sm')
[38;5;2m✔ Linking successful[0m
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/en_core_web_sm
-->
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/data/en
You can now load the model via spacy.load('en')

  {'hypermodel_pars': {}, 'data_pars': {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64, 'train': True}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}} [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory. 

  


### Running {'model_pars': {'model_uri': 'model_keras.textcnn.py', 'maxlen': 40, 'max_features': 5, 'embedding_dims': 50}, 'data_pars': {'path': 'dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5}, 'compute_pars': {'engine': 'adam', 'loss': 'binary_crossentropy', 'metrics': ['accuracy'], 'batch_size': 1000, 'epochs': 1}, 'out_pars': {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5} {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'} 

  #### Setup Model   ############################################## 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 153, in create_tabular_dataset
    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
    return util.load_model(name, **overrides)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 291, in fit
    train_iter, valid_iter, vocab = get_dataset(data_pars, out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 334, in get_dataset
    trainset, validset, vocab = create_tabular_dataset( data_pars['train_path'], data_pars['valid_path'], lang, pretrained_emb)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 159, in create_tabular_dataset
    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
    return util.load_model(name, **overrides)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
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

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_keras.textcnn.Model object at 0x7f1cdc02d128> <class 'mlmodels.model_keras.textcnn.Model'>
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 4145152/17464789 [======>.......................] - ETA: 0s
11247616/17464789 [==================>...........] - ETA: 0s
16211968/17464789 [==========================>...] - ETA: 0s
17465344/17464789 [==============================] - 0s 0us/step
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-12 14:14:44.187185: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-12 14:14:44.191014: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-12 14:14:44.191190: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5585f169e110 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-12 14:14:44.191214: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 11s - loss: 7.2833 - accuracy: 0.5250
 2000/25000 [=>............................] - ETA: 8s - loss: 7.6666 - accuracy: 0.5000 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.7177 - accuracy: 0.4967
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.7050 - accuracy: 0.4975
 5000/25000 [=====>........................] - ETA: 6s - loss: 7.6850 - accuracy: 0.4988
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.7484 - accuracy: 0.4947
 7000/25000 [=======>......................] - ETA: 5s - loss: 7.7740 - accuracy: 0.4930
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.7912 - accuracy: 0.4919
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.7671 - accuracy: 0.4934
10000/25000 [===========>..................] - ETA: 4s - loss: 7.7556 - accuracy: 0.4942
11000/25000 [============>.................] - ETA: 4s - loss: 7.7307 - accuracy: 0.4958
12000/25000 [=============>................] - ETA: 3s - loss: 7.7228 - accuracy: 0.4963
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6926 - accuracy: 0.4983
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6579 - accuracy: 0.5006
15000/25000 [=================>............] - ETA: 2s - loss: 7.6554 - accuracy: 0.5007
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6570 - accuracy: 0.5006
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6477 - accuracy: 0.5012
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6590 - accuracy: 0.5005
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6279 - accuracy: 0.5025
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6528 - accuracy: 0.5009
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6403 - accuracy: 0.5017
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6534 - accuracy: 0.5009
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6586 - accuracy: 0.5005
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6647 - accuracy: 0.5001
25000/25000 [==============================] - 9s 342us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### Inference Need return ypred, ytrue ######################### 
Loading data...

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-12 14:14:59.290504
model_uri                                 model_keras.textcnn.py
json           [{'model_uri': 'model_keras.textcnn.py', 'maxl...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                       0.5
metric_name                                       accuracy_score
Name: 0, dtype: object 

  benchmark file saved at /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark/text_classification/ 

                       date_run               model_uri  ... metric     metric_name
0  2020-05-12 14:14:59.290504  model_keras.textcnn.py  ...    0.5  accuracy_score

[1 rows x 6 columns] 
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do text_classification 





 ************************************************************************************************************************

  nlp_reuters 

  json_path /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/benchmark_text/ 

  Model List [{'model_pars': {'model_uri': 'model_keras.textvae.py', 'MAX_NB_WORDS': 12000, 'EMBEDDING_DIM': 50, 'latent_dim': 32, 'intermediate_dim': 96, 'epsilon_std': 0.1, 'num_sampled': 500, 'optimizer': 'adam'}, 'data_pars': {'train': True, 'MAX_SEQUENCE_LENGTH': 15, 'train_data_path': 'dataset/text/quora/train.csv', 'glove_embedding': 'dataset/text/glove/glove.6B.50d.txt'}, 'compute_pars': {'epochs': 1, 'batch_size': 100, 'VALIDATION_SPLIT': 0.2}, 'out_pars': {'path': 'ztest/ml_keras/textvae/'}}, {'model_pars': {'model_uri': 'model_keras.namentity_crm_bilstm.py', 'embedding': 40, 'optimizer': 'rmsprop'}, 'data_pars': {'train': True, 'mode': 'test_repo', 'path': 'dataset/text/ner_dataset.csv', 'location_type': 'repo', 'data_type': 'text', 'data_loader': 'mlmodels.data:import_data_fromfile', 'data_loader_pars': {'size': 50}, 'data_processor': 'mlmodels.model_keras.prepocess:process', 'data_processor_pars': {'split': 0.5, 'max_len': 75}, 'max_len': 75, 'size': [0, 1, 2], 'output_size': [0, 6]}, 'compute_pars': {'epochs': 1, 'batch_size': 64}, 'out_pars': {'path': 'ztest/ml_keras/namentity_crm_bilstm/', 'data_type': 'pandas'}}, {'model_pars': {'model_uri': 'model_keras.Autokeras.py', 'max_trials': 1}, 'data_pars': {'dataset': 'IMDB', 'data_path': 'dataset/nlp/', 'num_words': 1000, 'validation_split': 0.15, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 1, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': 'ztest/model_tch/MATCHZOO/BERT/'}}, {'model_pars': {'model_uri': 'model_keras.textcnn.py', 'maxlen': 40, 'max_features': 5, 'embedding_dims': 50}, 'data_pars': {'path': 'dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5}, 'compute_pars': {'engine': 'adam', 'loss': 'binary_crossentropy', 'metrics': ['accuracy'], 'batch_size': 1000, 'epochs': 1}, 'out_pars': {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'}}, {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_classifier.py', 'task_name': 'binary', 'model_type': 'xlnet', 'model_name': 'xlnet-base-cased', 'learning_rate': 0.001, 'sequence_length': 56, 'num_classes': 2, 'drop_out': 0.5, 'l2_reg_lambda': 0.0, 'optimization': 'adam', 'embedding_size': 300, 'filter_sizes': [3, 4, 5], 'num_filters': 128, 'do_train': True, 'do_eval': True, 'fp16': False, 'fp16_opt_level': 'O1', 'max_seq_length': 128, 'output_mode': 'classification', 'cache_dir': 'mlmodels/ztest/'}, 'data_pars': {'data_dir': './mlmodels/dataset/text/yelp_reviews/', 'negative_data_file': './dataset/rt-polaritydata/rt-polarity.neg', 'DEV_SAMPLE_PERCENTAGE': 0.1, 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'train': 'True', 'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'cache_dir': 'mlmodels/ztest/'}, 'compute_pars': {'epochs': 10, 'batch_size': 128, 'return_pred': 'True', 'train_batch_size': 8, 'eval_batch_size': 8, 'gradient_accumulation_steps': 1, 'num_train_epochs': 1, 'weight_decay': 0, 'learning_rate': 4e-05, 'adam_epsilon': 1e-08, 'warmup_ratio': 0.06, 'warmup_steps': 0, 'max_grad_norm': 1.0, 'logging_steps': 50, 'evaluate_during_training': False, 'num_samples': 500, 'save_steps': 100, 'eval_all_checkpoints': True, 'overwrite_output_dir': True, 'reprocess_input_data': False}, 'out_pars': {'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'modelpath': './output/model/model.h5'}}, {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_sentence.py', 'embedding_model': 'BERT', 'embedding_model_name': 'bert-base-uncased'}, 'data_pars': {'data_path': 'dataset/text/', 'train_path': 'AllNLI', 'train_type': 'NLI', 'test_path': 'stsbenchmark', 'test_type': 'sts', 'train': 1}, 'compute_pars': {'loss': 'SoftmaxLoss', 'batch_size': 32, 'num_epochs': 1, 'evaluation_steps': 10, 'warmup_steps': 100}, 'out_pars': {'path': './output/transformer_sentence/', 'modelpath': './output/transformer_sentence/model.h5'}}, {'hypermodel_pars': {}, 'data_pars': {'data_path': 'dataset/recommender/IMDB_sample.txt', 'train_path': 'dataset/recommender/IMDB_train.csv', 'valid_path': 'dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}}, {'model_pars': {'model_uri': 'model_tch.matchzoo_models.py', 'model': 'BERT', 'pretrained': 0, 'embedding_output_dim': 100, 'mode': 'bert-base-uncased', 'dropout_rate': 0.2}, 'data_pars': {'dataset': 'WIKI_QA', 'data_path': 'dataset/nlp/', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 10, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': 'ztest/model_tch/MATCHZOO/BERT/'}}] 

  


### Running {'model_pars': {'model_uri': 'model_keras.textvae.py', 'MAX_NB_WORDS': 12000, 'EMBEDDING_DIM': 50, 'latent_dim': 32, 'intermediate_dim': 96, 'epsilon_std': 0.1, 'num_sampled': 500, 'optimizer': 'adam'}, 'data_pars': {'train': True, 'MAX_SEQUENCE_LENGTH': 15, 'train_data_path': 'dataset/text/quora/train.csv', 'glove_embedding': 'dataset/text/glove/glove.6B.50d.txt'}, 'compute_pars': {'epochs': 1, 'batch_size': 100, 'VALIDATION_SPLIT': 0.2}, 'out_pars': {'path': 'ztest/ml_keras/textvae/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'MAX_SEQUENCE_LENGTH': 15, 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv', 'glove_embedding': 'dataset/text/glove/glove.6B.50d.txt'} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/ml_keras/textvae/'} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_uri': 'model_keras.textvae.py', 'MAX_NB_WORDS': 12000, 'EMBEDDING_DIM': 50, 'latent_dim': 32, 'intermediate_dim': 96, 'epsilon_std': 0.1, 'num_sampled': 500, 'optimizer': 'adam'}, 'data_pars': {'train': True, 'MAX_SEQUENCE_LENGTH': 15, 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv', 'glove_embedding': 'dataset/text/glove/glove.6B.50d.txt'}, 'compute_pars': {'epochs': 1, 'batch_size': 100, 'VALIDATION_SPLIT': 0.2}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/ml_keras/textvae/'}} [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv' 

  


### Running {'model_pars': {'model_uri': 'model_keras.namentity_crm_bilstm.py', 'embedding': 40, 'optimizer': 'rmsprop'}, 'data_pars': {'train': True, 'mode': 'test_repo', 'path': 'dataset/text/ner_dataset.csv', 'location_type': 'repo', 'data_type': 'text', 'data_loader': 'mlmodels.data:import_data_fromfile', 'data_loader_pars': {'size': 50}, 'data_processor': 'mlmodels.model_keras.prepocess:process', 'data_processor_pars': {'split': 0.5, 'max_len': 75}, 'max_len': 75, 'size': [0, 1, 2], 'output_size': [0, 6]}, 'compute_pars': {'epochs': 1, 'batch_size': 64}, 'out_pars': {'path': 'ztest/ml_keras/namentity_crm_bilstm/', 'data_type': 'pandas'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'train': True, 'mode': 'test_repo', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ner_dataset.csv', 'location_type': 'repo', 'data_type': 'text', 'data_loader': 'mlmodels.data:import_data_fromfile', 'data_loader_pars': {'size': 50}, 'data_processor': 'mlmodels.model_keras.prepocess:process', 'data_processor_pars': {'split': 0.5, 'max_len': 75}, 'max_len': 75, 'size': [0, 1, 2], 'output_size': [0, 6]} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/ml_keras/namentity_crm_bilstm/', 'data_type': 'pandas'} 

  #### Setup Model   ############################################## 
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 120, in benchmark_run
    model     = module.Model(model_pars, data_pars, compute_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 51, in __init__
    texts, embeddings_index = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 269, in get_dataset
    with codecs.open(data_pars["train_data_path"], encoding='utf-8') as f:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/codecs.py", line 897, in open
    file = builtins.open(filename, mode, buffering)
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv'
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_ops.py:2509: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Model: "model_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 75)                0         
_________________________________________________________________
embedding_1 (Embedding)      (None, 75, 40)            1720      
_________________________________________________________________
bidirectional_1 (Bidirection (None, 75, 100)           36400     
_________________________________________________________________
time_distributed_1 (TimeDist (None, 75, 50)            5050      
_________________________________________________________________
crf_1 (CRF)                  (None, 75, 5)             290       
=================================================================
Total params: 43,460
Trainable params: 43,460
Non-trainable params: 0
_________________________________________________________________

  #### Fit  ####################################################### 
2020-05-12 14:15:05.113555: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-12 14:15:05.118651: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-12 14:15:05.118799: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5615d2d566d0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-12 14:15:05.118814: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

>>>model:  <mlmodels.model_keras.namentity_crm_bilstm.Model object at 0x7f9127b42be0> <class 'mlmodels.model_keras.namentity_crm_bilstm.Model'>
Train on 1 samples, validate on 1 samples
Epoch 1/1

1/1 [==============================] - 1s 948ms/step - loss: 1.6502 - crf_viterbi_accuracy: 0.3467 - val_loss: 1.5553 - val_crf_viterbi_accuracy: 0.3333

  #### Inference Need return ypred, ytrue ######################### 

  ### Calculate Metrics    ######################################## 

  {'model_pars': {'model_uri': 'model_keras.namentity_crm_bilstm.py', 'embedding': 40, 'optimizer': 'rmsprop'}, 'data_pars': {'train': False, 'mode': 'test_repo', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ner_dataset.csv', 'location_type': 'repo', 'data_type': 'text', 'data_loader': 'mlmodels.data:import_data_fromfile', 'data_loader_pars': {'size': 50}, 'data_processor': 'mlmodels.model_keras.prepocess:process', 'data_processor_pars': {'split': 0.5, 'max_len': 75}, 'max_len': 75, 'size': [0, 1, 2], 'output_size': [0, 6]}, 'compute_pars': {'epochs': 1, 'batch_size': 64}, 'out_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/ml_keras/namentity_crm_bilstm/', 'data_type': 'pandas'}} module 'sklearn.metrics' has no attribute 'accuracy, f1_score' 

  


### Running {'model_pars': {'model_uri': 'model_keras.Autokeras.py', 'max_trials': 1}, 'data_pars': {'dataset': 'IMDB', 'data_path': 'dataset/nlp/', 'num_words': 1000, 'validation_split': 0.15, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 1, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': 'ztest/model_tch/MATCHZOO/BERT/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'IMDB', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'num_words': 1000, 'validation_split': 0.15, 'train_batch_size': 4, 'test_batch_size': 1} {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_uri': 'model_keras.Autokeras.py', 'max_trials': 1}, 'data_pars': {'dataset': 'IMDB', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'num_words': 1000, 'validation_split': 0.15, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 1, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'}} Module model_keras.Autokeras notfound, No module named 'autokeras', tuple index out of range 

  


### Running {'model_pars': {'model_uri': 'model_keras.textcnn.py', 'maxlen': 40, 'max_features': 5, 'embedding_dims': 50}, 'data_pars': {'path': 'dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5}, 'compute_pars': {'engine': 'adam', 'loss': 'binary_crossentropy', 'metrics': ['accuracy'], 'batch_size': 1000, 'epochs': 1}, 'out_pars': {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/imdb.csv', 'train': 1, 'maxlen': 40, 'max_features': 5} {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'} 

  #### Setup Model   ############################################## 
Model: "model_2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_2 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_2 (Embedding)         (None, 40, 50)       250         input_2[0][0]                    
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 38, 128)      19328       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 37, 128)      25728       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 36, 128)      32128       embedding_2[0][0]                
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
dense_2 (Dense)                 (None, 1)            385         concatenate_1[0][0]              
==================================================================================================
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_keras.textcnn.Model object at 0x7f912f29f128> <class 'mlmodels.model_keras.textcnn.Model'>
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 13s - loss: 7.4520 - accuracy: 0.5140
 2000/25000 [=>............................] - ETA: 9s - loss: 7.3676 - accuracy: 0.5195 
 3000/25000 [==>...........................] - ETA: 8s - loss: 7.6155 - accuracy: 0.5033
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.6206 - accuracy: 0.5030
 5000/25000 [=====>........................] - ETA: 6s - loss: 7.6298 - accuracy: 0.5024
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.6181 - accuracy: 0.5032
 7000/25000 [=======>......................] - ETA: 5s - loss: 7.5571 - accuracy: 0.5071
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.5574 - accuracy: 0.5071
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.5746 - accuracy: 0.5060
10000/25000 [===========>..................] - ETA: 4s - loss: 7.5670 - accuracy: 0.5065
11000/25000 [============>.................] - ETA: 4s - loss: 7.5788 - accuracy: 0.5057
12000/25000 [=============>................] - ETA: 3s - loss: 7.6181 - accuracy: 0.5032
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6100 - accuracy: 0.5037
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6414 - accuracy: 0.5016
15000/25000 [=================>............] - ETA: 2s - loss: 7.6339 - accuracy: 0.5021
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6436 - accuracy: 0.5015
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6477 - accuracy: 0.5012
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6462 - accuracy: 0.5013
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6586 - accuracy: 0.5005
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6651 - accuracy: 0.5001
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6622 - accuracy: 0.5003
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6652 - accuracy: 0.5001
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6646 - accuracy: 0.5001
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6788 - accuracy: 0.4992
25000/25000 [==============================] - 9s 346us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### Inference Need return ypred, ytrue ######################### 
Loading data...

  ### Calculate Metrics    ######################################## 

  {'model_pars': {'model_uri': 'model_keras.textcnn.py', 'maxlen': 40, 'max_features': 5, 'embedding_dims': 50}, 'data_pars': {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/imdb.csv', 'train': False, 'maxlen': 40, 'max_features': 5}, 'compute_pars': {'engine': 'adam', 'loss': 'binary_crossentropy', 'metrics': ['accuracy'], 'batch_size': 1000, 'epochs': 1}, 'out_pars': {'path': './output/textcnn_keras//model.h5', 'model_path': './output/textcnn_keras/model.h5'}} module 'sklearn.metrics' has no attribute 'accuracy, f1_score' 

  


### Running {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_classifier.py', 'task_name': 'binary', 'model_type': 'xlnet', 'model_name': 'xlnet-base-cased', 'learning_rate': 0.001, 'sequence_length': 56, 'num_classes': 2, 'drop_out': 0.5, 'l2_reg_lambda': 0.0, 'optimization': 'adam', 'embedding_size': 300, 'filter_sizes': [3, 4, 5], 'num_filters': 128, 'do_train': True, 'do_eval': True, 'fp16': False, 'fp16_opt_level': 'O1', 'max_seq_length': 128, 'output_mode': 'classification', 'cache_dir': 'mlmodels/ztest/'}, 'data_pars': {'data_dir': './mlmodels/dataset/text/yelp_reviews/', 'negative_data_file': './dataset/rt-polaritydata/rt-polarity.neg', 'DEV_SAMPLE_PERCENTAGE': 0.1, 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'train': 'True', 'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'cache_dir': 'mlmodels/ztest/'}, 'compute_pars': {'epochs': 10, 'batch_size': 128, 'return_pred': 'True', 'train_batch_size': 8, 'eval_batch_size': 8, 'gradient_accumulation_steps': 1, 'num_train_epochs': 1, 'weight_decay': 0, 'learning_rate': 4e-05, 'adam_epsilon': 1e-08, 'warmup_ratio': 0.06, 'warmup_steps': 0, 'max_grad_norm': 1.0, 'logging_steps': 50, 'evaluate_during_training': False, 'num_samples': 500, 'save_steps': 100, 'eval_all_checkpoints': True, 'overwrite_output_dir': True, 'reprocess_input_data': False}, 'out_pars': {'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'modelpath': './output/model/model.h5'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'data_dir': './mlmodels/dataset/text/yelp_reviews/', 'negative_data_file': './dataset/rt-polaritydata/rt-polarity.neg', 'DEV_SAMPLE_PERCENTAGE': 0.1, 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'train': 'True', 'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'cache_dir': 'mlmodels/ztest/'} {'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'modelpath': './output/model/model.h5'} 

  #### Setup Model   ############################################## 

  {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_classifier.py', 'task_name': 'binary', 'model_type': 'xlnet', 'model_name': 'xlnet-base-cased', 'learning_rate': 0.001, 'sequence_length': 56, 'num_classes': 2, 'drop_out': 0.5, 'l2_reg_lambda': 0.0, 'optimization': 'adam', 'embedding_size': 300, 'filter_sizes': [3, 4, 5], 'num_filters': 128, 'do_train': True, 'do_eval': True, 'fp16': False, 'fp16_opt_level': 'O1', 'max_seq_length': 128, 'output_mode': 'classification', 'cache_dir': 'mlmodels/ztest/'}, 'data_pars': {'data_dir': './mlmodels/dataset/text/yelp_reviews/', 'negative_data_file': './dataset/rt-polaritydata/rt-polarity.neg', 'DEV_SAMPLE_PERCENTAGE': 0.1, 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'train': 'True', 'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'cache_dir': 'mlmodels/ztest/'}, 'compute_pars': {'epochs': 10, 'batch_size': 128, 'return_pred': 'True', 'train_batch_size': 8, 'eval_batch_size': 8, 'gradient_accumulation_steps': 1, 'num_train_epochs': 1, 'weight_decay': 0, 'learning_rate': 4e-05, 'adam_epsilon': 1e-08, 'warmup_ratio': 0.06, 'warmup_steps': 0, 'max_grad_norm': 1.0, 'logging_steps': 50, 'evaluate_during_training': False, 'num_samples': 500, 'save_steps': 100, 'eval_all_checkpoints': True, 'overwrite_output_dir': True, 'reprocess_input_data': False}, 'out_pars': {'output_dir': './mlmodels/dataset/text/yelp_reviews/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6], 'modelpath': './output/model/model.h5'}} Module model_tch.transformer_classifier notfound, No module named 'util_transformer', tuple index out of range 

  


### Running {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_sentence.py', 'embedding_model': 'BERT', 'embedding_model_name': 'bert-base-uncased'}, 'data_pars': {'data_path': 'dataset/text/', 'train_path': 'AllNLI', 'train_type': 'NLI', 'test_path': 'stsbenchmark', 'test_type': 'sts', 'train': 1}, 'compute_pars': {'loss': 'SoftmaxLoss', 'batch_size': 32, 'num_epochs': 1, 'evaluation_steps': 10, 'warmup_steps': 100}, 'out_pars': {'path': './output/transformer_sentence/', 'modelpath': './output/transformer_sentence/model.h5'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/', 'train_path': 'AllNLI', 'train_type': 'NLI', 'test_path': 'stsbenchmark', 'test_type': 'sts', 'train': 1} {'path': './output/transformer_sentence/', 'modelpath': './output/transformer_sentence/model.h5'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.transformer_sentence.Model object at 0x7f90be808c88> <class 'mlmodels.model_tch.transformer_sentence.Model'>

  {'notes': 'Using Yelp Reviews dataset', 'model_pars': {'model_uri': 'model_tch.transformer_sentence.py', 'embedding_model': 'BERT', 'embedding_model_name': 'bert-base-uncased'}, 'data_pars': {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/', 'train_path': 'AllNLI', 'train_type': 'NLI', 'test_path': 'stsbenchmark', 'test_type': 'sts', 'train': True}, 'compute_pars': {'loss': 'SoftmaxLoss', 'batch_size': 32, 'num_epochs': 1, 'evaluation_steps': 10, 'warmup_steps': 100}, 'out_pars': {'path': './output/transformer_sentence/', 'modelpath': './output/transformer_sentence/model.h5'}} 'model_path' 

  


### Running {'hypermodel_pars': {}, 'data_pars': {'data_path': 'dataset/recommender/IMDB_sample.txt', 'train_path': 'dataset/recommender/IMDB_train.csv', 'valid_path': 'dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64} {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'} 

  #### Setup Model   ############################################## 
{'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}

  #### Fit  ####################################################### 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 140, in benchmark_run
    metric_val = metric_eval(actual=ytrue, pred=ypred,  metric_name=metric)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 60, in metric_eval
    metric = getattr(importlib.import_module("sklearn.metrics"), metric_name)
AttributeError: module 'sklearn.metrics' has no attribute 'accuracy, f1_score'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/Autokeras.py", line 12, in <module>
    import autokeras as ak
ModuleNotFoundError: No module named 'autokeras'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_keras.Autokeras notfound, No module named 'autokeras', tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 140, in benchmark_run
    metric_val = metric_eval(actual=ytrue, pred=ypred,  metric_name=metric)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 60, in metric_eval
    metric = getattr(importlib.import_module("sklearn.metrics"), metric_name)
AttributeError: module 'sklearn.metrics' has no attribute 'accuracy, f1_score'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
    module = import_module(f"mlmodels.{model_name}")
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_classifier.py", line 39, in <module>
    from util_transformer import (convert_examples_to_features, output_modes,
ModuleNotFoundError: No module named 'util_transformer'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_tch.transformer_classifier notfound, No module named 'util_transformer', tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_sentence.py", line 164, in fit
    output_path      = out_pars["model_path"]
KeyError: 'model_path'
.vector_cache/glove.6B.zip: 0.00B [00:00, ?B/s].vector_cache/glove.6B.zip:   0%|          | 8.19k/862M [00:00<21:50:51, 11.0kB/s].vector_cache/glove.6B.zip:   0%|          | 49.2k/862M [00:00<15:31:34, 15.4kB/s].vector_cache/glove.6B.zip:   0%|          | 221k/862M [00:01<10:55:19, 21.9kB/s] .vector_cache/glove.6B.zip:   0%|          | 893k/862M [00:01<7:39:05, 31.3kB/s] .vector_cache/glove.6B.zip:   0%|          | 2.32M/862M [00:01<5:21:07, 44.6kB/s].vector_cache/glove.6B.zip:   1%|          | 6.65M/862M [00:01<3:43:45, 63.7kB/s].vector_cache/glove.6B.zip:   1%|          | 9.92M/862M [00:01<2:36:09, 91.0kB/s].vector_cache/glove.6B.zip:   2%|▏         | 15.2M/862M [00:01<1:48:42, 130kB/s] .vector_cache/glove.6B.zip:   2%|▏         | 18.4M/862M [00:01<1:15:57, 185kB/s].vector_cache/glove.6B.zip:   3%|▎         | 22.6M/862M [00:01<53:00, 264kB/s]  .vector_cache/glove.6B.zip:   3%|▎         | 26.9M/862M [00:01<37:00, 376kB/s].vector_cache/glove.6B.zip:   4%|▎         | 31.2M/862M [00:01<25:52, 535kB/s].vector_cache/glove.6B.zip:   4%|▍         | 35.5M/862M [00:02<18:07, 760kB/s].vector_cache/glove.6B.zip:   5%|▍         | 39.8M/862M [00:02<12:42, 1.08MB/s].vector_cache/glove.6B.zip:   5%|▌         | 44.1M/862M [00:02<08:57, 1.52MB/s].vector_cache/glove.6B.zip:   6%|▌         | 48.5M/862M [00:02<06:19, 2.14MB/s].vector_cache/glove.6B.zip:   6%|▌         | 52.5M/862M [00:03<05:06, 2.64MB/s].vector_cache/glove.6B.zip:   7%|▋         | 56.7M/862M [00:05<05:28, 2.45MB/s].vector_cache/glove.6B.zip:   7%|▋         | 56.9M/862M [00:05<06:10, 2.18MB/s].vector_cache/glove.6B.zip:   7%|▋         | 57.8M/862M [00:05<04:47, 2.80MB/s].vector_cache/glove.6B.zip:   7%|▋         | 60.2M/862M [00:05<03:30, 3.80MB/s].vector_cache/glove.6B.zip:   7%|▋         | 60.8M/862M [00:06<13:11, 1.01MB/s].vector_cache/glove.6B.zip:   7%|▋         | 61.1M/862M [00:07<10:40, 1.25MB/s].vector_cache/glove.6B.zip:   7%|▋         | 62.6M/862M [00:07<07:47, 1.71MB/s].vector_cache/glove.6B.zip:   8%|▊         | 64.9M/862M [00:08<08:22, 1.59MB/s].vector_cache/glove.6B.zip:   8%|▊         | 65.1M/862M [00:09<08:33, 1.55MB/s].vector_cache/glove.6B.zip:   8%|▊         | 65.9M/862M [00:09<06:32, 2.03MB/s].vector_cache/glove.6B.zip:   8%|▊         | 68.3M/862M [00:09<04:44, 2.79MB/s].vector_cache/glove.6B.zip:   8%|▊         | 69.1M/862M [00:10<11:23, 1.16MB/s].vector_cache/glove.6B.zip:   8%|▊         | 69.5M/862M [00:11<09:20, 1.41MB/s].vector_cache/glove.6B.zip:   8%|▊         | 71.0M/862M [00:11<06:52, 1.92MB/s].vector_cache/glove.6B.zip:   8%|▊         | 73.2M/862M [00:12<07:52, 1.67MB/s].vector_cache/glove.6B.zip:   9%|▊         | 73.4M/862M [00:13<08:11, 1.61MB/s].vector_cache/glove.6B.zip:   9%|▊         | 74.2M/862M [00:13<06:16, 2.09MB/s].vector_cache/glove.6B.zip:   9%|▉         | 76.1M/862M [00:13<04:35, 2.85MB/s].vector_cache/glove.6B.zip:   9%|▉         | 77.3M/862M [00:14<08:33, 1.53MB/s].vector_cache/glove.6B.zip:   9%|▉         | 77.7M/862M [00:14<07:18, 1.79MB/s].vector_cache/glove.6B.zip:   9%|▉         | 79.2M/862M [00:15<05:26, 2.40MB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.4M/862M [00:16<06:51, 1.90MB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.6M/862M [00:16<07:26, 1.75MB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.4M/862M [00:17<05:52, 2.21MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.5M/862M [00:18<06:11, 2.09MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.9M/862M [00:18<05:40, 2.28MB/s].vector_cache/glove.6B.zip:  10%|█         | 87.5M/862M [00:19<04:17, 3.01MB/s].vector_cache/glove.6B.zip:  10%|█         | 89.6M/862M [00:20<06:00, 2.14MB/s].vector_cache/glove.6B.zip:  10%|█         | 90.0M/862M [00:20<05:30, 2.34MB/s].vector_cache/glove.6B.zip:  11%|█         | 91.6M/862M [00:21<04:10, 3.08MB/s].vector_cache/glove.6B.zip:  11%|█         | 93.7M/862M [00:22<05:57, 2.15MB/s].vector_cache/glove.6B.zip:  11%|█         | 93.9M/862M [00:22<06:46, 1.89MB/s].vector_cache/glove.6B.zip:  11%|█         | 94.7M/862M [00:22<05:23, 2.37MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.9M/862M [00:24<05:49, 2.19MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 98.3M/862M [00:24<05:22, 2.37MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 99.8M/862M [00:24<04:01, 3.15MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 102M/862M [00:26<05:48, 2.18MB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 102M/862M [00:26<06:39, 1.90MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 103M/862M [00:26<05:18, 2.38MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:27<03:50, 3.28MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:28<51:22, 245kB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:28<37:14, 338kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 108M/862M [00:28<26:20, 477kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:30<21:18, 588kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 111M/862M [00:30<16:11, 774kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 112M/862M [00:30<11:37, 1.08MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:32<11:04, 1.13MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 115M/862M [00:32<10:16, 1.21MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 115M/862M [00:33<09:36, 1.29MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:34<08:15, 1.50MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 119M/862M [00:34<07:03, 1.76MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 120M/862M [00:34<05:12, 2.38MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<06:32, 1.89MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<07:04, 1.74MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 124M/862M [00:36<05:30, 2.23MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:36<04:00, 3.06MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<1:31:20, 134kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<1:05:10, 188kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 129M/862M [00:38<45:50, 267kB/s]  .vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:40<34:51, 350kB/s].vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:40<25:37, 475kB/s].vector_cache/glove.6B.zip:  15%|█▌        | 133M/862M [00:40<18:09, 669kB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:42<15:34, 778kB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:42<13:23, 905kB/s].vector_cache/glove.6B.zip:  16%|█▌        | 136M/862M [00:42<09:53, 1.22MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 137M/862M [00:42<07:07, 1.69MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:44<08:47, 1.37MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:44<07:22, 1.63MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:44<05:27, 2.20MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:46<06:37, 1.81MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:46<07:04, 1.69MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 144M/862M [00:46<05:27, 2.19MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 146M/862M [00:46<04:00, 2.97MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:48<07:06, 1.68MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 148M/862M [00:48<06:12, 1.92MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 149M/862M [00:48<04:38, 2.56MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 151M/862M [00:50<06:01, 1.97MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:50<06:36, 1.79MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:50<05:13, 2.26MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:52<05:33, 2.12MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 156M/862M [00:52<05:05, 2.31MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 157M/862M [00:52<03:51, 3.05MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 160M/862M [00:54<05:26, 2.15MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 160M/862M [00:54<04:58, 2.35MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 162M/862M [00:54<03:43, 3.14MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:56<05:22, 2.16MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:56<04:46, 2.43MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 166M/862M [00:56<03:38, 3.19MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 168M/862M [00:58<05:17, 2.19MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 168M/862M [00:58<04:53, 2.37MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 170M/862M [00:58<03:42, 3.11MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [00:59<05:19, 2.16MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [01:00<04:53, 2.35MB/s].vector_cache/glove.6B.zip:  20%|██        | 174M/862M [01:00<03:42, 3.09MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:01<05:17, 2.16MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:02<04:51, 2.35MB/s].vector_cache/glove.6B.zip:  21%|██        | 178M/862M [01:02<03:41, 3.09MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:03<05:16, 2.15MB/s].vector_cache/glove.6B.zip:  21%|██        | 181M/862M [01:04<04:50, 2.35MB/s].vector_cache/glove.6B.zip:  21%|██        | 182M/862M [01:04<03:37, 3.13MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:05<05:13, 2.16MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:05<05:57, 1.89MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 185M/862M [01:06<04:40, 2.42MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:06<03:23, 3.32MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:07<10:59, 1.02MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:07<08:40, 1.29MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 190M/862M [01:08<06:17, 1.78MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:08<04:34, 2.44MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:09<1:09:43, 160kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:09<51:03, 219kB/s]  .vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:10<36:16, 307kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:10<25:23, 437kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:11<1:49:32, 101kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:11<1:17:45, 143kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 199M/862M [01:11<54:32, 203kB/s]  .vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:13<40:39, 271kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:13<29:35, 372kB/s].vector_cache/glove.6B.zip:  24%|██▎       | 203M/862M [01:13<20:56, 525kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:15<17:10, 638kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:15<13:08, 833kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 207M/862M [01:15<09:27, 1.15MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<09:10, 1.19MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<07:37, 1.43MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 211M/862M [01:17<05:37, 1.93MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:19<06:17, 1.72MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:19<06:47, 1.59MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 214M/862M [01:19<05:16, 2.05MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 217M/862M [01:19<03:48, 2.83MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 217M/862M [01:21<10:20, 1.04MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 218M/862M [01:21<08:25, 1.27MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 219M/862M [01:21<06:08, 1.74MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 221M/862M [01:23<06:37, 1.61MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:23<07:01, 1.52MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:23<05:30, 1.94MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 225M/862M [01:23<03:57, 2.68MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:25<14:07, 751kB/s] .vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:25<11:05, 956kB/s].vector_cache/glove.6B.zip:  26%|██▋       | 227M/862M [01:25<08:02, 1.32MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:27<07:54, 1.33MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:27<07:53, 1.34MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 231M/862M [01:27<06:06, 1.72MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:27<04:24, 2.38MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:29<15:47, 663kB/s] .vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:29<12:13, 856kB/s].vector_cache/glove.6B.zip:  27%|██▋       | 236M/862M [01:29<08:47, 1.19MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:31<08:23, 1.24MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:31<08:17, 1.25MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 239M/862M [01:31<06:17, 1.65MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:31<04:31, 2.29MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:33<08:28, 1.22MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 243M/862M [01:33<07:04, 1.46MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 244M/862M [01:33<05:13, 1.97MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 246M/862M [01:35<05:52, 1.74MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:35<06:24, 1.60MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:35<04:58, 2.06MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 249M/862M [01:35<03:36, 2.83MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:37<06:50, 1.49MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:37<05:54, 1.72MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 252M/862M [01:37<04:24, 2.30MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:39<05:17, 1.92MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:39<04:49, 2.10MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 257M/862M [01:39<03:38, 2.77MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:41<04:43, 2.12MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:41<05:34, 1.80MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:41<04:27, 2.26MB/s].vector_cache/glove.6B.zip:  30%|███       | 263M/862M [01:41<03:14, 3.08MB/s].vector_cache/glove.6B.zip:  31%|███       | 263M/862M [01:43<14:20, 696kB/s] .vector_cache/glove.6B.zip:  31%|███       | 264M/862M [01:43<11:08, 895kB/s].vector_cache/glove.6B.zip:  31%|███       | 265M/862M [01:43<08:03, 1.23MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:45<07:46, 1.27MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<07:38, 1.30MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<05:53, 1.68MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:45<04:13, 2.33MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 272M/862M [01:47<13:31, 728kB/s] .vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:47<10:33, 932kB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:47<07:36, 1.29MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:49<07:25, 1.32MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:49<07:20, 1.33MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:49<05:41, 1.72MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:49<04:05, 2.38MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:51<13:25, 723kB/s] .vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:51<10:27, 927kB/s].vector_cache/glove.6B.zip:  33%|███▎      | 282M/862M [01:51<07:34, 1.28MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:53<07:22, 1.31MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:53<07:18, 1.32MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 285M/862M [01:53<05:33, 1.73MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:53<04:03, 2.36MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:55<05:37, 1.70MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 289M/862M [01:55<05:01, 1.90MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 290M/862M [01:55<03:46, 2.52MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:57<04:40, 2.03MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:57<05:22, 1.77MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:57<04:17, 2.21MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [01:57<03:06, 3.04MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 297M/862M [01:59<12:16, 768kB/s] .vector_cache/glove.6B.zip:  34%|███▍      | 297M/862M [01:59<09:37, 979kB/s].vector_cache/glove.6B.zip:  35%|███▍      | 298M/862M [01:59<06:57, 1.35MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:01<06:52, 1.36MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:01<06:55, 1.35MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 302M/862M [02:01<05:16, 1.77MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 303M/862M [02:01<03:49, 2.43MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 305M/862M [02:03<06:00, 1.55MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 305M/862M [02:03<05:13, 1.78MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 307M/862M [02:03<03:54, 2.37MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:05<04:43, 1.95MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:05<05:21, 1.72MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 310M/862M [02:05<04:15, 2.16MB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:05<03:05, 2.96MB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:07<13:14, 691kB/s] .vector_cache/glove.6B.zip:  36%|███▋      | 314M/862M [02:07<10:15, 891kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 315M/862M [02:07<07:22, 1.24MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 317M/862M [02:09<07:08, 1.27MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:09<07:01, 1.29MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:09<05:20, 1.70MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 321M/862M [02:09<03:50, 2.35MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:11<08:02, 1.12MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:11<06:38, 1.35MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 323M/862M [02:11<04:51, 1.85MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:13<05:20, 1.68MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:13<05:44, 1.56MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 327M/862M [02:13<04:25, 2.02MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 329M/862M [02:13<03:13, 2.76MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:15<05:36, 1.58MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:15<04:54, 1.81MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 332M/862M [02:15<03:38, 2.43MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 334M/862M [02:17<04:27, 1.97MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 334M/862M [02:17<05:06, 1.72MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 335M/862M [02:17<04:02, 2.17MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:17<02:55, 2.99MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:19<14:00, 624kB/s] .vector_cache/glove.6B.zip:  39%|███▉      | 339M/862M [02:19<10:46, 810kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:19<07:44, 1.12MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 342M/862M [02:21<07:16, 1.19MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 343M/862M [02:21<06:03, 1.43MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 344M/862M [02:21<04:28, 1.93MB/s].vector_cache/glove.6B.zip:  40%|████      | 347M/862M [02:23<04:59, 1.72MB/s].vector_cache/glove.6B.zip:  40%|████      | 347M/862M [02:23<05:23, 1.59MB/s].vector_cache/glove.6B.zip:  40%|████      | 347M/862M [02:23<04:14, 2.02MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:23<03:04, 2.77MB/s].vector_cache/glove.6B.zip:  41%|████      | 351M/862M [02:25<12:28, 683kB/s] .vector_cache/glove.6B.zip:  41%|████      | 351M/862M [02:25<09:30, 896kB/s].vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:25<06:50, 1.24MB/s].vector_cache/glove.6B.zip:  41%|████      | 354M/862M [02:25<04:53, 1.73MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<11:47, 717kB/s] .vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<10:08, 834kB/s].vector_cache/glove.6B.zip:  41%|████▏     | 356M/862M [02:27<07:33, 1.12MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:27<05:21, 1.57MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<12:43, 659kB/s] .vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<09:51, 850kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 361M/862M [02:29<07:04, 1.18MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:31<06:44, 1.23MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:31<06:33, 1.27MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:31<05:03, 1.64MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:31<03:37, 2.27MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:33<12:31, 658kB/s] .vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:33<09:40, 851kB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:33<06:57, 1.18MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<06:38, 1.23MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<05:29, 1.49MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 373M/862M [02:35<04:01, 2.02MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 376M/862M [02:37<04:40, 1.73MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 376M/862M [02:37<05:04, 1.60MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 377M/862M [02:37<03:55, 2.06MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 379M/862M [02:37<02:51, 2.82MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 380M/862M [02:39<04:52, 1.65MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 380M/862M [02:39<04:18, 1.86MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:39<03:14, 2.48MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 384M/862M [02:41<03:58, 2.00MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 384M/862M [02:41<03:42, 2.15MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:41<02:46, 2.86MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 388M/862M [02:43<03:40, 2.15MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 389M/862M [02:43<03:16, 2.40MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 390M/862M [02:43<02:31, 3.12MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 392M/862M [02:43<01:51, 4.22MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 392M/862M [02:45<12:28, 628kB/s] .vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:45<10:27, 748kB/s].vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:45<07:40, 1.02MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:45<05:31, 1.41MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:47<05:51, 1.32MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:47<04:57, 1.56MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 398M/862M [02:47<03:40, 2.10MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 401M/862M [02:49<04:15, 1.81MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 401M/862M [02:49<03:50, 2.00MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 402M/862M [02:49<02:51, 2.68MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<03:39, 2.08MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<04:11, 1.82MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 406M/862M [02:51<03:19, 2.29MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 409M/862M [02:51<02:24, 3.14MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 409M/862M [02:53<17:50, 423kB/s] .vector_cache/glove.6B.zip:  47%|████▋     | 409M/862M [02:53<13:19, 567kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:53<09:29, 793kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 413M/862M [02:54<08:13, 911kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 413M/862M [02:55<07:25, 1.01MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 414M/862M [02:55<05:32, 1.35MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:55<03:57, 1.87MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 417M/862M [02:56<06:07, 1.21MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 418M/862M [02:57<05:06, 1.45MB/s].vector_cache/glove.6B.zip:  49%|████▊     | 419M/862M [02:57<03:45, 1.97MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 421M/862M [02:58<04:13, 1.74MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<04:31, 1.62MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<03:33, 2.06MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 425M/862M [02:59<02:33, 2.85MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 426M/862M [03:00<16:46, 434kB/s] .vector_cache/glove.6B.zip:  49%|████▉     | 426M/862M [03:01<12:32, 580kB/s].vector_cache/glove.6B.zip:  50%|████▉     | 427M/862M [03:01<08:56, 811kB/s].vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:02<07:47, 925kB/s].vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:03<07:04, 1.02MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 431M/862M [03:03<05:20, 1.35MB/s].vector_cache/glove.6B.zip:  50%|█████     | 433M/862M [03:03<03:48, 1.88MB/s].vector_cache/glove.6B.zip:  50%|█████     | 434M/862M [03:04<10:17, 694kB/s] .vector_cache/glove.6B.zip:  50%|█████     | 434M/862M [03:05<07:57, 896kB/s].vector_cache/glove.6B.zip:  51%|█████     | 436M/862M [03:05<05:42, 1.24MB/s].vector_cache/glove.6B.zip:  51%|█████     | 438M/862M [03:06<05:34, 1.27MB/s].vector_cache/glove.6B.zip:  51%|█████     | 438M/862M [03:07<05:28, 1.29MB/s].vector_cache/glove.6B.zip:  51%|█████     | 439M/862M [03:07<04:12, 1.67MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 442M/862M [03:07<03:01, 2.31MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 442M/862M [03:08<10:36, 660kB/s] .vector_cache/glove.6B.zip:  51%|█████▏    | 443M/862M [03:09<08:12, 852kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 444M/862M [03:09<05:53, 1.18MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 446M/862M [03:10<05:36, 1.24MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 447M/862M [03:11<05:33, 1.24MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 447M/862M [03:11<04:12, 1.64MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 448M/862M [03:11<03:07, 2.21MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:12<03:44, 1.84MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:13<03:23, 2.03MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:13<02:33, 2.68MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:14<03:15, 2.09MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:14<03:47, 1.79MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:15<03:01, 2.24MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:15<02:11, 3.07MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:16<08:41, 773kB/s] .vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:16<06:47, 988kB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:17<04:53, 1.37MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 463M/862M [03:18<04:54, 1.35MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 463M/862M [03:18<04:10, 1.59MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:19<03:04, 2.15MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:20<03:33, 1.85MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:20<03:58, 1.66MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:21<03:08, 2.09MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:21<02:16, 2.87MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:22<09:28, 688kB/s] .vector_cache/glove.6B.zip:  55%|█████▍    | 472M/862M [03:22<07:21, 885kB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:23<05:16, 1.23MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:24<05:04, 1.27MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:24<04:58, 1.30MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:25<03:49, 1.68MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 479M/862M [03:25<02:44, 2.33MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:26<08:44, 729kB/s] .vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:26<06:50, 932kB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:27<04:55, 1.29MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:28<04:47, 1.32MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:28<04:44, 1.33MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 485M/862M [03:29<03:36, 1.74MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 487M/862M [03:29<02:35, 2.41MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 488M/862M [03:30<04:51, 1.28MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 489M/862M [03:30<04:05, 1.52MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:31<03:01, 2.05MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 492M/862M [03:32<03:26, 1.79MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 493M/862M [03:32<03:47, 1.63MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 493M/862M [03:33<02:57, 2.08MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 496M/862M [03:33<02:07, 2.88MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 497M/862M [03:34<05:44, 1.06MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 497M/862M [03:34<04:41, 1.30MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 498M/862M [03:35<03:25, 1.77MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:36<03:40, 1.64MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:36<03:08, 1.91MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 502M/862M [03:36<02:22, 2.53MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 505M/862M [03:38<02:56, 2.03MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 505M/862M [03:38<03:23, 1.76MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:38<02:41, 2.20MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 509M/862M [03:39<01:56, 3.04MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 509M/862M [03:40<07:40, 767kB/s] .vector_cache/glove.6B.zip:  59%|█████▉    | 509M/862M [03:40<06:00, 977kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:40<04:21, 1.34MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 513M/862M [03:42<04:17, 1.35MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 513M/862M [03:42<04:14, 1.37MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 514M/862M [03:42<03:16, 1.77MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 517M/862M [03:43<02:21, 2.45MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 517M/862M [03:44<19:52, 289kB/s] .vector_cache/glove.6B.zip:  60%|██████    | 518M/862M [03:44<14:32, 395kB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:44<10:17, 555kB/s].vector_cache/glove.6B.zip:  60%|██████    | 521M/862M [03:46<08:23, 676kB/s].vector_cache/glove.6B.zip:  61%|██████    | 522M/862M [03:46<07:08, 795kB/s].vector_cache/glove.6B.zip:  61%|██████    | 522M/862M [03:46<05:15, 1.08MB/s].vector_cache/glove.6B.zip:  61%|██████    | 525M/862M [03:47<03:44, 1.51MB/s].vector_cache/glove.6B.zip:  61%|██████    | 526M/862M [03:48<05:26, 1.03MB/s].vector_cache/glove.6B.zip:  61%|██████    | 526M/862M [03:48<04:25, 1.27MB/s].vector_cache/glove.6B.zip:  61%|██████    | 527M/862M [03:48<03:14, 1.72MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 530M/862M [03:50<03:27, 1.60MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 530M/862M [03:50<03:40, 1.51MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 531M/862M [03:50<02:49, 1.95MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 533M/862M [03:50<02:03, 2.68MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 534M/862M [03:52<03:28, 1.58MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 534M/862M [03:52<03:02, 1.80MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:52<02:14, 2.42MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 538M/862M [03:54<02:44, 1.97MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 538M/862M [03:54<03:06, 1.73MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 539M/862M [03:54<02:25, 2.22MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 541M/862M [03:54<01:45, 3.04MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 542M/862M [03:56<03:38, 1.46MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 543M/862M [03:56<02:52, 1.85MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 545M/862M [03:56<02:06, 2.52MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 546M/862M [03:58<02:49, 1.86MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 547M/862M [03:58<02:42, 1.95MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 548M/862M [03:58<02:03, 2.54MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:00<02:25, 2.14MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:00<02:20, 2.22MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 552M/862M [04:00<01:45, 2.93MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:02<02:17, 2.23MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:02<02:45, 1.86MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 556M/862M [04:02<02:09, 2.37MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 558M/862M [04:02<01:34, 3.22MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:04<03:12, 1.57MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:04<02:42, 1.86MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:04<02:02, 2.47MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 562M/862M [04:04<01:29, 3.36MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 563M/862M [04:06<04:54, 1.01MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 563M/862M [04:06<03:59, 1.25MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 565M/862M [04:06<02:54, 1.70MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 567M/862M [04:08<03:04, 1.60MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 567M/862M [04:08<03:12, 1.53MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 568M/862M [04:08<02:29, 1.96MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 571M/862M [04:08<01:47, 2.72MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 571M/862M [04:10<13:26, 360kB/s] .vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:10<09:55, 488kB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:10<07:01, 686kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:12<05:56, 804kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:12<05:13, 914kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:12<03:52, 1.23MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 579M/862M [04:12<02:45, 1.71MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 580M/862M [04:14<04:04, 1.16MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 580M/862M [04:14<03:20, 1.40MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 582M/862M [04:14<02:27, 1.90MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 584M/862M [04:16<02:44, 1.69MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 584M/862M [04:16<03:00, 1.54MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 585M/862M [04:16<02:19, 1.99MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 587M/862M [04:16<01:40, 2.75MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 588M/862M [04:18<03:41, 1.24MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 588M/862M [04:18<03:05, 1.48MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 590M/862M [04:18<02:16, 2.00MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 592M/862M [04:20<02:33, 1.76MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 592M/862M [04:20<02:47, 1.61MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 593M/862M [04:20<02:09, 2.07MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 595M/862M [04:20<01:34, 2.83MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 596M/862M [04:22<02:46, 1.59MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:22<02:24, 1.83MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:22<01:46, 2.47MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:24<02:13, 1.97MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:24<02:00, 2.16MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:24<01:29, 2.89MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:26<02:02, 2.11MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:26<02:22, 1.80MB/s].vector_cache/glove.6B.zip:  70%|███████   | 606M/862M [04:26<01:54, 2.25MB/s].vector_cache/glove.6B.zip:  71%|███████   | 608M/862M [04:26<01:22, 3.09MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:28<05:28, 772kB/s] .vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:28<04:43, 892kB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:28<04:04, 1.03MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:28<03:35, 1.17MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:28<03:14, 1.30MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:28<02:57, 1.42MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:29<02:44, 1.53MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:29<02:34, 1.63MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:29<02:27, 1.70MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:29<02:21, 1.77MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:29<02:16, 1.84MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:29<02:07, 1.97MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:29<02:05, 2.00MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:30<02:03, 2.03MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:30<02:05, 1.99MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:59, 2.09MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:57, 2.13MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:56, 2.14MB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:30<01:56, 2.14MB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:30<01:55, 2.16MB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:30<01:53, 2.18MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 614M/862M [04:31<01:53, 2.19MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:31<01:51, 2.21MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:31<01:51, 2.22MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:31<01:50, 2.23MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 616M/862M [04:31<01:50, 2.24MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 616M/862M [04:31<01:49, 2.24MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 616M/862M [04:31<01:49, 2.25MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:49, 2.24MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:48, 2.25MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:48, 2.26MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:47, 2.27MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:32<01:47, 2.27MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:32<01:47, 2.27MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:32<01:47, 2.28MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:32<01:46, 2.29MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:33<01:44, 2.32MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:33<01:44, 2.32MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:33<01:43, 2.35MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:33<01:38, 2.46MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:33<01:44, 2.31MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:33<01:39, 2.43MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:33<04:26, 906kB/s] .vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:33<03:35, 1.12MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:34<02:56, 1.37MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:34<02:32, 1.58MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:34<02:15, 1.77MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:34<02:06, 1.90MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:34<01:52, 2.12MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:34<01:50, 2.17MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:34<01:40, 2.37MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:35<01:37, 2.45MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 624M/862M [04:35<01:34, 2.51MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 624M/862M [04:35<01:32, 2.57MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 625M/862M [04:35<01:28, 2.69MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 625M/862M [04:35<15:54, 249kB/s] .vector_cache/glove.6B.zip:  72%|███████▏  | 625M/862M [04:35<11:48, 335kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 625M/862M [04:36<08:39, 456kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 625M/862M [04:36<06:33, 602kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:36<04:56, 798kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:36<03:48, 1.03MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:36<03:11, 1.23MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 627M/862M [04:36<02:43, 1.44MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 627M/862M [04:36<02:15, 1.73MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 627M/862M [04:36<02:01, 1.93MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 628M/862M [04:36<01:51, 2.10MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 628M/862M [04:37<01:38, 2.37MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 628M/862M [04:37<01:36, 2.41MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:37<01:32, 2.53MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:37<05:00, 777kB/s] .vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:37<04:04, 954kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:38<03:14, 1.19MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:38<02:37, 1.47MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:38<02:14, 1.72MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:38<01:56, 1.98MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:38<01:41, 2.27MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:38<01:32, 2.49MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 632M/862M [04:38<01:25, 2.69MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 632M/862M [04:38<01:19, 2.88MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:39<01:15, 3.04MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:39<23:23, 163kB/s] .vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:39<17:12, 222kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:39<12:23, 308kB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:40<08:57, 425kB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:40<06:32, 580kB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 635M/862M [04:40<04:48, 788kB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 636M/862M [04:40<03:37, 1.04MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 636M/862M [04:40<02:47, 1.35MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 637M/862M [04:40<02:12, 1.70MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 637M/862M [04:41<05:54, 636kB/s] .vector_cache/glove.6B.zip:  74%|███████▍  | 637M/862M [04:41<05:32, 677kB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 637M/862M [04:41<04:15, 879kB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:42<03:13, 1.16MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 639M/862M [04:42<02:28, 1.51MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 639M/862M [04:42<01:55, 1.93MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 640M/862M [04:42<01:32, 2.40MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 641M/862M [04:42<01:17, 2.85MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 641M/862M [04:43<06:57, 529kB/s] .vector_cache/glove.6B.zip:  74%|███████▍  | 641M/862M [04:43<05:52, 628kB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:43<04:23, 836kB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 642M/862M [04:44<03:15, 1.12MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 643M/862M [04:44<02:26, 1.49MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 644M/862M [04:44<01:52, 1.94MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 645M/862M [04:44<01:27, 2.47MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 645M/862M [04:45<15:04, 240kB/s] .vector_cache/glove.6B.zip:  75%|███████▍  | 645M/862M [04:45<12:09, 298kB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:45<08:54, 405kB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:46<06:22, 565kB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 647M/862M [04:46<04:34, 782kB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 649M/862M [04:46<03:20, 1.07MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 649M/862M [04:47<04:05, 866kB/s] .vector_cache/glove.6B.zip:  75%|███████▌  | 649M/862M [04:47<04:11, 845kB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 650M/862M [04:47<03:17, 1.08MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 651M/862M [04:47<02:25, 1.46MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 652M/862M [04:48<01:48, 1.95MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 653M/862M [04:48<01:20, 2.59MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 653M/862M [04:49<04:38, 750kB/s] .vector_cache/glove.6B.zip:  76%|███████▌  | 654M/862M [04:49<04:22, 795kB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 654M/862M [04:49<03:20, 1.04MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 655M/862M [04:49<02:25, 1.42MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 657M/862M [04:50<01:47, 1.92MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 658M/862M [04:51<02:45, 1.24MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 658M/862M [04:51<04:00, 851kB/s] .vector_cache/glove.6B.zip:  76%|███████▋  | 658M/862M [04:51<03:17, 1.03MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:51<02:26, 1.39MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 660M/862M [04:52<01:46, 1.89MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 662M/862M [04:53<02:21, 1.42MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 662M/862M [04:53<02:30, 1.34MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:53<01:55, 1.73MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 664M/862M [04:53<01:25, 2.32MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:54<01:03, 3.09MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:55<2:56:32, 18.5kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:55<2:05:07, 26.1kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:55<1:27:47, 37.2kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 668M/862M [04:55<1:01:10, 53.0kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:56<42:26, 75.7kB/s]  .vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:57<32:34, 98.3kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:57<24:05, 133kB/s] .vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:57<17:09, 186kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 672M/862M [04:57<11:59, 264kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 674M/862M [04:57<08:21, 375kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 674M/862M [04:59<47:45, 65.6kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 674M/862M [04:59<34:29, 90.8kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [04:59<24:22, 128kB/s] .vector_cache/glove.6B.zip:  78%|███████▊  | 676M/862M [04:59<16:59, 182kB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 678M/862M [05:01<12:29, 245kB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 678M/862M [05:01<09:43, 315kB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 679M/862M [05:01<07:02, 434kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 681M/862M [05:01<04:57, 611kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 682M/862M [05:03<04:11, 714kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 683M/862M [05:03<03:50, 778kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 683M/862M [05:03<02:52, 1.04MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 685M/862M [05:03<02:02, 1.45MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 686M/862M [05:03<01:28, 1.98MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 687M/862M [05:05<06:42, 436kB/s] .vector_cache/glove.6B.zip:  80%|███████▉  | 687M/862M [05:05<05:26, 537kB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 687M/862M [05:05<03:59, 730kB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 689M/862M [05:05<02:48, 1.02MB/s].vector_cache/glove.6B.zip:  80%|████████  | 691M/862M [05:07<02:55, 976kB/s] .vector_cache/glove.6B.zip:  80%|████████  | 691M/862M [05:07<02:49, 1.01MB/s].vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:07<02:07, 1.33MB/s].vector_cache/glove.6B.zip:  80%|████████  | 693M/862M [05:07<01:31, 1.84MB/s].vector_cache/glove.6B.zip:  81%|████████  | 695M/862M [05:09<01:59, 1.40MB/s].vector_cache/glove.6B.zip:  81%|████████  | 695M/862M [05:09<02:11, 1.27MB/s].vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:09<01:41, 1.63MB/s].vector_cache/glove.6B.zip:  81%|████████  | 697M/862M [05:09<01:13, 2.24MB/s].vector_cache/glove.6B.zip:  81%|████████  | 699M/862M [05:11<01:36, 1.69MB/s].vector_cache/glove.6B.zip:  81%|████████  | 699M/862M [05:11<01:51, 1.46MB/s].vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:11<01:27, 1.86MB/s].vector_cache/glove.6B.zip:  81%|████████▏ | 702M/862M [05:11<01:02, 2.55MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 703M/862M [05:13<01:33, 1.70MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 703M/862M [05:13<01:53, 1.40MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:13<01:31, 1.74MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 706M/862M [05:13<01:05, 2.37MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 707M/862M [05:15<01:32, 1.67MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:15<01:42, 1.51MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:15<01:19, 1.95MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 710M/862M [05:15<00:57, 2.66MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 712M/862M [05:17<01:27, 1.72MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 712M/862M [05:17<01:29, 1.68MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 713M/862M [05:17<01:09, 2.15MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 715M/862M [05:17<00:49, 2.96MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 716M/862M [05:19<05:36, 435kB/s] .vector_cache/glove.6B.zip:  83%|████████▎ | 716M/862M [05:19<04:20, 561kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:19<03:07, 775kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 720M/862M [05:21<02:33, 930kB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 720M/862M [05:21<02:21, 1.00MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:21<01:46, 1.32MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 723M/862M [05:21<01:15, 1.85MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 724M/862M [05:23<02:40, 860kB/s] .vector_cache/glove.6B.zip:  84%|████████▍ | 724M/862M [05:23<02:22, 965kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:23<01:46, 1.29MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 727M/862M [05:23<01:14, 1.81MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 728M/862M [05:25<02:02, 1.10MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 728M/862M [05:25<01:45, 1.27MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:25<01:17, 1.70MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 732M/862M [05:27<01:17, 1.69MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 733M/862M [05:27<01:19, 1.64MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 733M/862M [05:27<01:01, 2.10MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 736M/862M [05:29<01:02, 2.01MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 737M/862M [05:29<01:08, 1.84MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 737M/862M [05:29<00:53, 2.32MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:31<00:56, 2.15MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:31<01:04, 1.89MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 742M/862M [05:31<00:50, 2.38MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 745M/862M [05:33<00:53, 2.19MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 745M/862M [05:33<01:00, 1.94MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 746M/862M [05:33<00:47, 2.44MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 749M/862M [05:35<00:51, 2.22MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 749M/862M [05:35<00:57, 1.96MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:35<00:45, 2.46MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 753M/862M [05:36<00:49, 2.23MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 753M/862M [05:37<00:56, 1.93MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:37<00:43, 2.48MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 756M/862M [05:37<00:31, 3.38MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 757M/862M [05:38<01:22, 1.28MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 757M/862M [05:39<01:17, 1.35MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:39<00:59, 1.76MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 761M/862M [05:40<00:56, 1.78MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 761M/862M [05:41<01:00, 1.68MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:41<00:46, 2.14MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 765M/862M [05:42<00:47, 2.04MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 765M/862M [05:43<00:52, 1.86MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:43<00:40, 2.39MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 769M/862M [05:43<00:28, 3.27MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 769M/862M [05:44<01:21, 1.14MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:44<01:15, 1.23MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:45<00:56, 1.62MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 773M/862M [05:46<00:52, 1.68MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:46<00:54, 1.61MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:47<00:42, 2.07MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 778M/862M [05:48<00:42, 1.99MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 778M/862M [05:48<00:46, 1.83MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 779M/862M [05:49<00:36, 2.31MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 782M/862M [05:50<00:37, 2.14MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 782M/862M [05:50<00:41, 1.91MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:50<00:33, 2.41MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 786M/862M [05:52<00:34, 2.20MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 786M/862M [05:52<00:39, 1.91MB/s].vector_cache/glove.6B.zip:  91%|█████████▏| 787M/862M [05:52<00:31, 2.40MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 790M/862M [05:54<00:32, 2.20MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 790M/862M [05:54<00:37, 1.94MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:54<00:28, 2.48MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 793M/862M [05:54<00:20, 3.39MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 794M/862M [05:56<00:55, 1.23MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 794M/862M [05:56<00:52, 1.30MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 795M/862M [05:56<00:39, 1.70MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 798M/862M [05:58<00:36, 1.73MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 798M/862M [05:58<00:52, 1.22MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [05:58<00:42, 1.49MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 800M/862M [05:58<00:30, 2.01MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 802M/862M [06:00<00:34, 1.74MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:00<00:35, 1.67MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:00<00:27, 2.14MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 806M/862M [06:02<00:27, 2.04MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 807M/862M [06:02<00:29, 1.85MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 807M/862M [06:02<00:23, 2.34MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 811M/862M [06:04<00:23, 2.16MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 811M/862M [06:04<00:27, 1.90MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 812M/862M [06:04<00:21, 2.39MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 815M/862M [06:06<00:21, 2.19MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 815M/862M [06:06<00:24, 1.94MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 816M/862M [06:06<00:18, 2.49MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 818M/862M [06:06<00:13, 3.37MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 819M/862M [06:08<00:26, 1.64MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 819M/862M [06:08<00:29, 1.48MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 819M/862M [06:08<00:24, 1.75MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:08<00:22, 1.92MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:08<00:20, 2.08MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:09<00:18, 2.22MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 821M/862M [06:09<00:17, 2.35MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 821M/862M [06:09<00:16, 2.50MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 821M/862M [06:09<00:15, 2.59MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 822M/862M [06:09<00:14, 2.82MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 822M/862M [06:09<00:15, 2.60MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 822M/862M [06:09<00:14, 2.84MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 823M/862M [06:09<00:14, 2.68MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 823M/862M [06:10<00:35, 1.10MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 823M/862M [06:10<00:29, 1.31MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:10<00:23, 1.62MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:10<00:22, 1.69MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:10<00:18, 2.03MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:10<00:16, 2.32MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:11<00:15, 2.37MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:11<00:13, 2.68MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 826M/862M [06:11<00:12, 2.88MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 826M/862M [06:11<00:12, 2.96MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 826M/862M [06:11<00:11, 3.08MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 827M/862M [06:11<00:11, 2.98MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 827M/862M [06:12<00:28, 1.24MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 827M/862M [06:12<00:28, 1.24MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:12<00:22, 1.53MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:12<00:18, 1.84MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:12<00:15, 2.13MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 829M/862M [06:12<00:13, 2.41MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 829M/862M [06:13<00:12, 2.64MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 830M/862M [06:13<00:11, 2.85MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 830M/862M [06:13<00:10, 3.01MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:13<00:09, 3.33MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:13<00:10, 3.04MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:14<01:05, 475kB/s] .vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:14<00:52, 586kB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 832M/862M [06:14<00:39, 773kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 832M/862M [06:14<00:29, 1.01MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:14<00:23, 1.28MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:14<00:18, 1.58MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 834M/862M [06:15<00:15, 1.90MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 834M/862M [06:15<00:12, 2.18MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 834M/862M [06:15<00:11, 2.46MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 835M/862M [06:15<00:10, 2.71MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 835M/862M [06:16<00:27, 962kB/s] .vector_cache/glove.6B.zip:  97%|█████████▋| 835M/862M [06:16<00:25, 1.04MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 836M/862M [06:16<00:20, 1.30MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 836M/862M [06:16<00:15, 1.64MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:16<00:12, 2.00MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:16<00:11, 2.10MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:16<00:10, 2.47MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 838M/862M [06:17<00:10, 2.25MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 838M/862M [06:17<00:09, 2.54MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 838M/862M [06:17<00:09, 2.53MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 839M/862M [06:17<00:08, 2.68MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 839M/862M [06:17<00:08, 2.77MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 839M/862M [06:17<00:09, 2.49MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 839M/862M [06:18<01:13, 309kB/s] .vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:18<00:57, 392kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:18<00:42, 526kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:18<00:31, 706kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:18<00:23, 915kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:18<00:17, 1.19MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:18<00:15, 1.31MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:19<00:12, 1.62MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:19<00:10, 1.96MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:19<00:10, 1.98MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:19<00:08, 2.31MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:19<00:07, 2.55MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:19<00:07, 2.64MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:20<00:24, 749kB/s] .vector_cache/glove.6B.zip:  98%|█████████▊| 844M/862M [06:20<00:20, 901kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 844M/862M [06:20<00:16, 1.11MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 844M/862M [06:20<00:13, 1.31MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:20<00:11, 1.53MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:20<00:09, 1.72MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:20<00:08, 1.92MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 846M/862M [06:21<00:08, 2.05MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 846M/862M [06:21<00:07, 2.19MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 846M/862M [06:21<00:06, 2.31MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 847M/862M [06:21<00:06, 2.39MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 847M/862M [06:21<00:06, 2.46MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 847M/862M [06:21<00:05, 2.53MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 848M/862M [06:22<00:14, 1.04MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 848M/862M [06:22<00:11, 1.20MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 848M/862M [06:22<00:09, 1.43MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:22<00:08, 1.66MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:22<00:07, 1.88MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 849M/862M [06:22<00:06, 2.08MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:22<00:05, 2.23MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:23<00:05, 2.37MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:23<00:04, 2.48MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 851M/862M [06:23<00:04, 2.56MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 851M/862M [06:23<00:04, 2.62MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:23<00:04, 2.66MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:24<00:09, 1.09MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:24<00:08, 1.26MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:24<00:06, 1.50MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:24<00:05, 1.74MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:24<00:04, 2.05MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:24<00:03, 2.24MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 854M/862M [06:24<00:03, 2.42MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 854M/862M [06:25<00:03, 2.56MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 855M/862M [06:25<00:02, 2.67MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 855M/862M [06:25<00:02, 2.75MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 855M/862M [06:25<00:02, 2.82MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:25<00:02, 2.96MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:26<00:23, 275kB/s] .vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:26<00:17, 355kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:26<00:12, 480kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:26<00:08, 642kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:26<00:05, 842kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 858M/862M [06:26<00:04, 1.08MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 858M/862M [06:26<00:03, 1.34MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 858M/862M [06:27<00:02, 1.62MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 859M/862M [06:27<00:01, 1.90MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 859M/862M [06:27<00:01, 2.16MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:27<00:01, 2.42MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:28<00:02, 1.04MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:28<00:01, 1.09MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:28<00:01, 1.34MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:28<00:00, 1.63MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:28<00:00, 1.92MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 862M/862M [06:28<00:00, 2.19MB/s].vector_cache/glove.6B.zip: 862MB [06:28, 2.22MB/s]                           
  0%|          | 0/400000 [00:00<?, ?it/s]  0%|          | 856/400000 [00:00<00:46, 8538.80it/s]  0%|          | 1738/400000 [00:00<00:46, 8619.96it/s]  1%|          | 2636/400000 [00:00<00:45, 8720.82it/s]  1%|          | 3532/400000 [00:00<00:45, 8789.46it/s]  1%|          | 4432/400000 [00:00<00:44, 8850.29it/s]  1%|▏         | 5365/400000 [00:00<00:43, 8986.42it/s]  2%|▏         | 6200/400000 [00:00<00:44, 8785.15it/s]  2%|▏         | 7089/400000 [00:00<00:44, 8816.28it/s]  2%|▏         | 7962/400000 [00:00<00:44, 8789.37it/s]  2%|▏         | 8810/400000 [00:01<00:44, 8693.14it/s]  2%|▏         | 9663/400000 [00:01<00:45, 8637.66it/s]  3%|▎         | 10511/400000 [00:01<00:46, 8460.46it/s]  3%|▎         | 11347/400000 [00:01<00:47, 8224.13it/s]  3%|▎         | 12164/400000 [00:01<00:47, 8171.93it/s]  3%|▎         | 12999/400000 [00:01<00:47, 8222.61it/s]  3%|▎         | 13819/400000 [00:01<00:47, 8212.38it/s]  4%|▎         | 14639/400000 [00:01<00:48, 7923.47it/s]  4%|▍         | 15482/400000 [00:01<00:47, 8066.28it/s]  4%|▍         | 16290/400000 [00:01<00:47, 8037.51it/s]  4%|▍         | 17150/400000 [00:02<00:46, 8197.59it/s]  4%|▍         | 17976/400000 [00:02<00:46, 8206.37it/s]  5%|▍         | 18871/400000 [00:02<00:45, 8414.17it/s]  5%|▍         | 19795/400000 [00:02<00:43, 8645.69it/s]  5%|▌         | 20678/400000 [00:02<00:43, 8698.93it/s]  5%|▌         | 21603/400000 [00:02<00:42, 8856.02it/s]  6%|▌         | 22491/400000 [00:02<00:43, 8742.93it/s]  6%|▌         | 23368/400000 [00:02<00:45, 8236.49it/s]  6%|▌         | 24273/400000 [00:02<00:44, 8462.98it/s]  6%|▋         | 25158/400000 [00:02<00:43, 8574.77it/s]  7%|▋         | 26066/400000 [00:03<00:42, 8719.95it/s]  7%|▋         | 26961/400000 [00:03<00:42, 8784.59it/s]  7%|▋         | 27843/400000 [00:03<00:42, 8681.90it/s]  7%|▋         | 28714/400000 [00:03<00:42, 8669.99it/s]  7%|▋         | 29591/400000 [00:03<00:42, 8699.06it/s]  8%|▊         | 30503/400000 [00:03<00:41, 8820.06it/s]  8%|▊         | 31418/400000 [00:03<00:41, 8915.23it/s]  8%|▊         | 32311/400000 [00:03<00:43, 8431.10it/s]  8%|▊         | 33161/400000 [00:03<00:43, 8359.68it/s]  9%|▊         | 34002/400000 [00:03<00:44, 8226.42it/s]  9%|▊         | 34829/400000 [00:04<00:45, 8105.31it/s]  9%|▉         | 35643/400000 [00:04<00:45, 8050.88it/s]  9%|▉         | 36451/400000 [00:04<00:46, 7850.06it/s]  9%|▉         | 37239/400000 [00:04<00:46, 7756.00it/s] 10%|▉         | 38100/400000 [00:04<00:45, 7993.15it/s] 10%|▉         | 38958/400000 [00:04<00:44, 8160.38it/s] 10%|▉         | 39778/400000 [00:04<00:44, 8083.71it/s] 10%|█         | 40589/400000 [00:04<00:44, 8011.62it/s] 10%|█         | 41433/400000 [00:04<00:44, 8134.69it/s] 11%|█         | 42249/400000 [00:05<00:44, 7998.59it/s] 11%|█         | 43073/400000 [00:05<00:44, 8068.11it/s] 11%|█         | 43882/400000 [00:05<00:45, 7861.83it/s] 11%|█         | 44729/400000 [00:05<00:44, 8033.29it/s] 11%|█▏        | 45630/400000 [00:05<00:42, 8301.45it/s] 12%|█▏        | 46496/400000 [00:05<00:42, 8404.07it/s] 12%|█▏        | 47407/400000 [00:05<00:40, 8603.40it/s] 12%|█▏        | 48271/400000 [00:05<00:42, 8332.12it/s] 12%|█▏        | 49121/400000 [00:05<00:41, 8379.85it/s] 12%|█▏        | 49962/400000 [00:05<00:42, 8290.58it/s] 13%|█▎        | 50794/400000 [00:06<00:43, 7992.08it/s] 13%|█▎        | 51643/400000 [00:06<00:42, 8131.15it/s] 13%|█▎        | 52460/400000 [00:06<00:44, 7887.75it/s] 13%|█▎        | 53253/400000 [00:06<00:44, 7850.04it/s] 14%|█▎        | 54041/400000 [00:06<00:45, 7635.55it/s] 14%|█▎        | 54808/400000 [00:06<00:45, 7598.48it/s] 14%|█▍        | 55653/400000 [00:06<00:43, 7834.47it/s] 14%|█▍        | 56440/400000 [00:06<00:45, 7589.10it/s] 14%|█▍        | 57204/400000 [00:06<00:45, 7569.37it/s] 14%|█▍        | 57964/400000 [00:07<00:46, 7313.01it/s] 15%|█▍        | 58700/400000 [00:07<00:47, 7205.04it/s] 15%|█▍        | 59424/400000 [00:07<00:48, 7094.60it/s] 15%|█▌        | 60146/400000 [00:07<00:47, 7130.06it/s] 15%|█▌        | 61078/400000 [00:07<00:44, 7669.01it/s] 15%|█▌        | 61933/400000 [00:07<00:42, 7911.85it/s] 16%|█▌        | 62799/400000 [00:07<00:41, 8121.43it/s] 16%|█▌        | 63621/400000 [00:07<00:41, 8065.30it/s] 16%|█▌        | 64434/400000 [00:07<00:42, 7948.42it/s] 16%|█▋        | 65234/400000 [00:07<00:42, 7910.59it/s] 17%|█▋        | 66029/400000 [00:08<00:43, 7626.15it/s] 17%|█▋        | 66869/400000 [00:08<00:42, 7842.53it/s] 17%|█▋        | 67737/400000 [00:08<00:41, 8074.15it/s] 17%|█▋        | 68557/400000 [00:08<00:40, 8110.29it/s] 17%|█▋        | 69467/400000 [00:08<00:39, 8381.72it/s] 18%|█▊        | 70331/400000 [00:08<00:38, 8455.79it/s] 18%|█▊        | 71184/400000 [00:08<00:38, 8476.61it/s] 18%|█▊        | 72103/400000 [00:08<00:37, 8676.74it/s] 18%|█▊        | 72974/400000 [00:08<00:38, 8506.83it/s] 18%|█▊        | 73885/400000 [00:08<00:37, 8678.52it/s] 19%|█▊        | 74756/400000 [00:09<00:37, 8590.30it/s] 19%|█▉        | 75640/400000 [00:09<00:37, 8653.28it/s] 19%|█▉        | 76507/400000 [00:09<00:37, 8547.96it/s] 19%|█▉        | 77364/400000 [00:09<00:40, 7982.45it/s] 20%|█▉        | 78273/400000 [00:09<00:38, 8283.00it/s] 20%|█▉        | 79111/400000 [00:09<00:40, 8007.85it/s] 20%|█▉        | 79920/400000 [00:09<00:40, 7893.95it/s] 20%|██        | 80716/400000 [00:09<00:41, 7688.19it/s] 20%|██        | 81553/400000 [00:09<00:40, 7878.64it/s] 21%|██        | 82405/400000 [00:10<00:39, 8058.32it/s] 21%|██        | 83229/400000 [00:10<00:39, 8110.24it/s] 21%|██        | 84046/400000 [00:10<00:38, 8127.06it/s] 21%|██        | 84861/400000 [00:10<00:41, 7679.88it/s] 21%|██▏       | 85636/400000 [00:10<00:43, 7277.17it/s] 22%|██▏       | 86373/400000 [00:10<00:43, 7272.25it/s] 22%|██▏       | 87107/400000 [00:10<00:42, 7281.54it/s] 22%|██▏       | 87853/400000 [00:10<00:42, 7334.17it/s] 22%|██▏       | 88645/400000 [00:10<00:41, 7499.92it/s] 22%|██▏       | 89536/400000 [00:10<00:39, 7871.42it/s] 23%|██▎       | 90331/400000 [00:11<00:41, 7506.99it/s] 23%|██▎       | 91166/400000 [00:11<00:39, 7740.25it/s] 23%|██▎       | 92002/400000 [00:11<00:38, 7914.00it/s] 23%|██▎       | 92826/400000 [00:11<00:38, 8008.68it/s] 23%|██▎       | 93731/400000 [00:11<00:36, 8294.00it/s] 24%|██▎       | 94567/400000 [00:11<00:36, 8283.37it/s] 24%|██▍       | 95400/400000 [00:11<00:36, 8252.47it/s] 24%|██▍       | 96290/400000 [00:11<00:36, 8434.83it/s] 24%|██▍       | 97137/400000 [00:11<00:36, 8390.42it/s] 25%|██▍       | 98053/400000 [00:11<00:35, 8605.78it/s] 25%|██▍       | 98917/400000 [00:12<00:35, 8599.35it/s] 25%|██▍       | 99779/400000 [00:12<00:35, 8416.89it/s] 25%|██▌       | 100639/400000 [00:12<00:35, 8469.16it/s] 25%|██▌       | 101488/400000 [00:12<00:35, 8472.93it/s] 26%|██▌       | 102398/400000 [00:12<00:34, 8646.90it/s] 26%|██▌       | 103265/400000 [00:12<00:36, 8233.74it/s] 26%|██▌       | 104094/400000 [00:12<00:36, 8155.47it/s] 26%|██▌       | 104981/400000 [00:12<00:35, 8356.00it/s] 26%|██▋       | 105853/400000 [00:12<00:34, 8460.29it/s] 27%|██▋       | 106711/400000 [00:13<00:34, 8494.02it/s] 27%|██▋       | 107563/400000 [00:13<00:35, 8288.29it/s] 27%|██▋       | 108395/400000 [00:13<00:36, 8021.56it/s] 27%|██▋       | 109201/400000 [00:13<00:36, 7938.89it/s] 28%|██▊       | 110024/400000 [00:13<00:36, 8022.74it/s] 28%|██▊       | 110876/400000 [00:13<00:35, 8164.22it/s] 28%|██▊       | 111695/400000 [00:13<00:35, 8018.35it/s] 28%|██▊       | 112522/400000 [00:13<00:35, 8089.35it/s] 28%|██▊       | 113353/400000 [00:13<00:35, 8152.46it/s] 29%|██▊       | 114248/400000 [00:13<00:34, 8376.17it/s] 29%|██▉       | 115185/400000 [00:14<00:32, 8650.94it/s] 29%|██▉       | 116055/400000 [00:14<00:32, 8662.83it/s] 29%|██▉       | 116947/400000 [00:14<00:32, 8738.02it/s] 29%|██▉       | 117823/400000 [00:14<00:33, 8358.43it/s] 30%|██▉       | 118696/400000 [00:14<00:33, 8464.10it/s] 30%|██▉       | 119591/400000 [00:14<00:32, 8602.53it/s] 30%|███       | 120455/400000 [00:14<00:33, 8470.44it/s] 30%|███       | 121349/400000 [00:14<00:32, 8603.88it/s] 31%|███       | 122212/400000 [00:14<00:35, 7898.88it/s] 31%|███       | 123015/400000 [00:14<00:35, 7872.79it/s] 31%|███       | 123839/400000 [00:15<00:34, 7979.18it/s] 31%|███       | 124675/400000 [00:15<00:34, 8088.68it/s] 31%|███▏      | 125532/400000 [00:15<00:33, 8225.13it/s] 32%|███▏      | 126377/400000 [00:15<00:33, 8290.79it/s] 32%|███▏      | 127264/400000 [00:15<00:32, 8455.36it/s] 32%|███▏      | 128113/400000 [00:15<00:32, 8409.13it/s] 32%|███▏      | 128957/400000 [00:15<00:33, 7979.06it/s] 32%|███▏      | 129798/400000 [00:15<00:33, 8102.36it/s] 33%|███▎      | 130613/400000 [00:15<00:34, 7906.04it/s] 33%|███▎      | 131408/400000 [00:16<00:33, 7903.23it/s] 33%|███▎      | 132215/400000 [00:16<00:33, 7952.41it/s] 33%|███▎      | 133013/400000 [00:16<00:33, 7944.71it/s] 33%|███▎      | 133810/400000 [00:16<00:34, 7806.55it/s] 34%|███▎      | 134593/400000 [00:16<00:35, 7573.50it/s] 34%|███▍      | 135435/400000 [00:16<00:33, 7807.95it/s] 34%|███▍      | 136282/400000 [00:16<00:33, 7957.48it/s] 34%|███▍      | 137101/400000 [00:16<00:32, 8025.48it/s] 34%|███▍      | 137906/400000 [00:16<00:33, 7920.00it/s] 35%|███▍      | 138714/400000 [00:16<00:32, 7967.25it/s] 35%|███▍      | 139616/400000 [00:17<00:31, 8255.36it/s] 35%|███▌      | 140446/400000 [00:17<00:31, 8155.40it/s] 35%|███▌      | 141265/400000 [00:17<00:31, 8165.03it/s] 36%|███▌      | 142084/400000 [00:17<00:31, 8128.82it/s] 36%|███▌      | 142899/400000 [00:17<00:31, 8051.61it/s] 36%|███▌      | 143719/400000 [00:17<00:31, 8093.93it/s] 36%|███▌      | 144530/400000 [00:17<00:32, 7885.61it/s] 36%|███▋      | 145368/400000 [00:17<00:31, 8027.14it/s] 37%|███▋      | 146196/400000 [00:17<00:31, 8099.46it/s] 37%|███▋      | 147008/400000 [00:17<00:31, 8102.90it/s] 37%|███▋      | 147862/400000 [00:18<00:30, 8227.61it/s] 37%|███▋      | 148686/400000 [00:18<00:30, 8138.08it/s] 37%|███▋      | 149512/400000 [00:18<00:30, 8171.31it/s] 38%|███▊      | 150349/400000 [00:18<00:30, 8229.74it/s] 38%|███▊      | 151173/400000 [00:18<00:30, 8167.10it/s] 38%|███▊      | 152105/400000 [00:18<00:29, 8478.63it/s] 38%|███▊      | 152989/400000 [00:18<00:28, 8580.97it/s] 38%|███▊      | 153850/400000 [00:18<00:28, 8503.63it/s] 39%|███▊      | 154703/400000 [00:18<00:28, 8481.87it/s] 39%|███▉      | 155553/400000 [00:18<00:29, 8428.29it/s] 39%|███▉      | 156455/400000 [00:19<00:28, 8594.89it/s] 39%|███▉      | 157317/400000 [00:19<00:28, 8487.29it/s] 40%|███▉      | 158168/400000 [00:19<00:29, 8162.51it/s] 40%|███▉      | 158993/400000 [00:19<00:29, 8187.76it/s] 40%|███▉      | 159815/400000 [00:19<00:30, 7976.44it/s] 40%|████      | 160667/400000 [00:19<00:29, 8131.39it/s] 40%|████      | 161483/400000 [00:19<00:29, 8010.27it/s] 41%|████      | 162304/400000 [00:19<00:29, 8066.93it/s] 41%|████      | 163177/400000 [00:19<00:28, 8252.81it/s] 41%|████      | 164034/400000 [00:20<00:28, 8345.29it/s] 41%|████      | 164953/400000 [00:20<00:27, 8578.67it/s] 41%|████▏     | 165814/400000 [00:20<00:27, 8373.67it/s] 42%|████▏     | 166655/400000 [00:20<00:28, 8231.02it/s] 42%|████▏     | 167506/400000 [00:20<00:27, 8311.09it/s] 42%|████▏     | 168340/400000 [00:20<00:28, 8139.49it/s] 42%|████▏     | 169157/400000 [00:20<00:28, 8062.09it/s] 42%|████▏     | 169988/400000 [00:20<00:28, 8134.89it/s] 43%|████▎     | 170844/400000 [00:20<00:27, 8255.99it/s] 43%|████▎     | 171672/400000 [00:20<00:28, 7916.16it/s] 43%|████▎     | 172468/400000 [00:21<00:29, 7695.14it/s] 43%|████▎     | 173274/400000 [00:21<00:29, 7799.91it/s] 44%|████▎     | 174102/400000 [00:21<00:28, 7934.83it/s] 44%|████▎     | 174929/400000 [00:21<00:28, 8030.57it/s] 44%|████▍     | 175777/400000 [00:21<00:27, 8158.52it/s] 44%|████▍     | 176595/400000 [00:21<00:28, 7970.65it/s] 44%|████▍     | 177395/400000 [00:21<00:27, 7970.71it/s] 45%|████▍     | 178194/400000 [00:21<00:28, 7882.75it/s] 45%|████▍     | 178984/400000 [00:21<00:28, 7717.61it/s] 45%|████▍     | 179758/400000 [00:21<00:28, 7713.89it/s] 45%|████▌     | 180601/400000 [00:22<00:27, 7913.93it/s] 45%|████▌     | 181418/400000 [00:22<00:27, 7988.64it/s] 46%|████▌     | 182261/400000 [00:22<00:26, 8113.96it/s] 46%|████▌     | 183075/400000 [00:22<00:26, 8098.98it/s] 46%|████▌     | 183900/400000 [00:22<00:26, 8141.75it/s] 46%|████▌     | 184716/400000 [00:22<00:26, 8028.93it/s] 46%|████▋     | 185520/400000 [00:22<00:26, 8010.99it/s] 47%|████▋     | 186400/400000 [00:22<00:25, 8230.29it/s] 47%|████▋     | 187302/400000 [00:22<00:25, 8450.34it/s] 47%|████▋     | 188229/400000 [00:22<00:24, 8679.03it/s] 47%|████▋     | 189105/400000 [00:23<00:24, 8700.62it/s] 47%|████▋     | 189978/400000 [00:23<00:24, 8438.62it/s] 48%|████▊     | 190876/400000 [00:23<00:24, 8592.42it/s] 48%|████▊     | 191796/400000 [00:23<00:23, 8763.85it/s] 48%|████▊     | 192716/400000 [00:23<00:23, 8888.40it/s] 48%|████▊     | 193608/400000 [00:23<00:23, 8793.35it/s] 49%|████▊     | 194490/400000 [00:23<00:23, 8727.05it/s] 49%|████▉     | 195365/400000 [00:23<00:24, 8438.89it/s] 49%|████▉     | 196213/400000 [00:23<00:24, 8321.35it/s] 49%|████▉     | 197102/400000 [00:24<00:23, 8481.45it/s] 49%|████▉     | 197987/400000 [00:24<00:23, 8587.44it/s] 50%|████▉     | 198848/400000 [00:24<00:24, 8338.94it/s] 50%|████▉     | 199685/400000 [00:24<00:25, 7767.18it/s] 50%|█████     | 200473/400000 [00:24<00:25, 7797.63it/s] 50%|█████     | 201266/400000 [00:24<00:25, 7832.98it/s] 51%|█████     | 202146/400000 [00:24<00:24, 8097.87it/s] 51%|█████     | 202974/400000 [00:24<00:24, 8150.85it/s] 51%|█████     | 203894/400000 [00:24<00:23, 8437.21it/s] 51%|█████     | 204759/400000 [00:24<00:22, 8498.57it/s] 51%|█████▏    | 205613/400000 [00:25<00:23, 8239.58it/s] 52%|█████▏    | 206442/400000 [00:25<00:23, 8183.63it/s] 52%|█████▏    | 207297/400000 [00:25<00:23, 8287.60it/s] 52%|█████▏    | 208211/400000 [00:25<00:23, 8278.59it/s] 52%|█████▏    | 209041/400000 [00:25<00:23, 8253.39it/s] 52%|█████▏    | 209868/400000 [00:25<00:23, 8117.17it/s] 53%|█████▎    | 210712/400000 [00:25<00:23, 8211.30it/s] 53%|█████▎    | 211535/400000 [00:25<00:23, 7971.34it/s] 53%|█████▎    | 212385/400000 [00:25<00:23, 8121.49it/s] 53%|█████▎    | 213240/400000 [00:26<00:22, 8243.87it/s] 54%|█████▎    | 214069/400000 [00:26<00:22, 8256.02it/s] 54%|█████▎    | 214979/400000 [00:26<00:21, 8490.82it/s] 54%|█████▍    | 215890/400000 [00:26<00:21, 8665.20it/s] 54%|█████▍    | 216780/400000 [00:26<00:20, 8733.00it/s] 54%|█████▍    | 217725/400000 [00:26<00:20, 8933.87it/s] 55%|█████▍    | 218621/400000 [00:26<00:20, 8826.87it/s] 55%|█████▍    | 219567/400000 [00:26<00:20, 9005.76it/s] 55%|█████▌    | 220470/400000 [00:26<00:20, 8866.50it/s] 55%|█████▌    | 221416/400000 [00:26<00:19, 9034.43it/s] 56%|█████▌    | 222322/400000 [00:27<00:20, 8666.26it/s] 56%|█████▌    | 223194/400000 [00:27<00:21, 8296.16it/s] 56%|█████▌    | 224031/400000 [00:27<00:21, 8275.70it/s] 56%|█████▌    | 224923/400000 [00:27<00:20, 8457.59it/s] 56%|█████▋    | 225783/400000 [00:27<00:20, 8499.37it/s] 57%|█████▋    | 226636/400000 [00:27<00:20, 8474.53it/s] 57%|█████▋    | 227486/400000 [00:27<00:21, 8200.19it/s] 57%|█████▋    | 228310/400000 [00:27<00:21, 8093.11it/s] 57%|█████▋    | 229179/400000 [00:27<00:20, 8261.29it/s] 58%|█████▊    | 230123/400000 [00:27<00:19, 8581.65it/s] 58%|█████▊    | 231064/400000 [00:28<00:19, 8812.39it/s] 58%|█████▊    | 231951/400000 [00:28<00:19, 8745.83it/s] 58%|█████▊    | 232852/400000 [00:28<00:18, 8822.81it/s] 58%|█████▊    | 233779/400000 [00:28<00:18, 8951.36it/s] 59%|█████▊    | 234716/400000 [00:28<00:18, 9070.73it/s] 59%|█████▉    | 235626/400000 [00:28<00:18, 8936.19it/s] 59%|█████▉    | 236522/400000 [00:28<00:18, 8687.81it/s] 59%|█████▉    | 237394/400000 [00:28<00:19, 8341.29it/s] 60%|█████▉    | 238234/400000 [00:28<00:19, 8105.30it/s] 60%|█████▉    | 239071/400000 [00:29<00:19, 8182.09it/s] 60%|█████▉    | 239919/400000 [00:29<00:19, 8268.37it/s] 60%|██████    | 240749/400000 [00:29<00:19, 8200.94it/s] 60%|██████    | 241572/400000 [00:29<00:19, 8066.12it/s] 61%|██████    | 242435/400000 [00:29<00:19, 8226.42it/s] 61%|██████    | 243367/400000 [00:29<00:18, 8525.97it/s] 61%|██████    | 244224/400000 [00:29<00:18, 8416.85it/s] 61%|██████▏   | 245069/400000 [00:29<00:18, 8282.62it/s] 61%|██████▏   | 245901/400000 [00:29<00:18, 8159.16it/s] 62%|██████▏   | 246720/400000 [00:29<00:18, 8135.31it/s] 62%|██████▏   | 247608/400000 [00:30<00:18, 8344.31it/s] 62%|██████▏   | 248472/400000 [00:30<00:17, 8429.96it/s] 62%|██████▏   | 249317/400000 [00:30<00:17, 8409.76it/s] 63%|██████▎   | 250160/400000 [00:30<00:17, 8378.44it/s] 63%|██████▎   | 251038/400000 [00:30<00:17, 8492.84it/s] 63%|██████▎   | 251957/400000 [00:30<00:17, 8689.93it/s] 63%|██████▎   | 252828/400000 [00:30<00:17, 8220.12it/s] 63%|██████▎   | 253657/400000 [00:30<00:18, 7746.22it/s] 64%|██████▎   | 254442/400000 [00:30<00:19, 7407.51it/s] 64%|██████▍   | 255194/400000 [00:31<00:20, 7198.54it/s] 64%|██████▍   | 255990/400000 [00:31<00:19, 7409.24it/s] 64%|██████▍   | 256739/400000 [00:31<00:19, 7370.42it/s] 64%|██████▍   | 257590/400000 [00:31<00:18, 7677.44it/s] 65%|██████▍   | 258424/400000 [00:31<00:18, 7863.59it/s] 65%|██████▍   | 259242/400000 [00:31<00:17, 7955.73it/s] 65%|██████▌   | 260130/400000 [00:31<00:17, 8211.76it/s] 65%|██████▌   | 260996/400000 [00:31<00:16, 8339.71it/s] 65%|██████▌   | 261874/400000 [00:31<00:16, 8464.79it/s] 66%|██████▌   | 262740/400000 [00:31<00:16, 8521.46it/s] 66%|██████▌   | 263635/400000 [00:32<00:15, 8644.36it/s] 66%|██████▌   | 264502/400000 [00:32<00:15, 8584.77it/s] 66%|██████▋   | 265363/400000 [00:32<00:16, 8254.26it/s] 67%|██████▋   | 266193/400000 [00:32<00:16, 8225.30it/s] 67%|██████▋   | 267019/400000 [00:32<00:16, 8224.75it/s] 67%|██████▋   | 267844/400000 [00:32<00:16, 8103.69it/s] 67%|██████▋   | 268657/400000 [00:32<00:16, 7915.20it/s] 67%|██████▋   | 269451/400000 [00:32<00:16, 7849.48it/s] 68%|██████▊   | 270303/400000 [00:32<00:16, 8036.36it/s] 68%|██████▊   | 271183/400000 [00:32<00:15, 8250.67it/s] 68%|██████▊   | 272071/400000 [00:33<00:15, 8428.52it/s] 68%|██████▊   | 272974/400000 [00:33<00:14, 8597.74it/s] 68%|██████▊   | 273837/400000 [00:33<00:14, 8550.01it/s] 69%|██████▊   | 274742/400000 [00:33<00:14, 8693.53it/s] 69%|██████▉   | 275614/400000 [00:33<00:14, 8634.37it/s] 69%|██████▉   | 276503/400000 [00:33<00:14, 8708.18it/s] 69%|██████▉   | 277392/400000 [00:33<00:13, 8761.84it/s] 70%|██████▉   | 278270/400000 [00:33<00:14, 8640.32it/s] 70%|██████▉   | 279183/400000 [00:33<00:13, 8779.16it/s] 70%|███████   | 280063/400000 [00:33<00:13, 8724.48it/s] 70%|███████   | 280966/400000 [00:34<00:13, 8813.92it/s] 70%|███████   | 281849/400000 [00:34<00:13, 8452.18it/s] 71%|███████   | 282699/400000 [00:34<00:14, 7986.35it/s] 71%|███████   | 283506/400000 [00:34<00:15, 7711.57it/s] 71%|███████   | 284322/400000 [00:34<00:14, 7839.57it/s] 71%|███████▏  | 285128/400000 [00:34<00:14, 7902.34it/s] 71%|███████▏  | 285923/400000 [00:34<00:14, 7915.49it/s] 72%|███████▏  | 286720/400000 [00:34<00:14, 7931.04it/s] 72%|███████▏  | 287516/400000 [00:34<00:14, 7922.06it/s] 72%|███████▏  | 288310/400000 [00:35<00:14, 7791.09it/s] 72%|███████▏  | 289104/400000 [00:35<00:14, 7832.07it/s] 72%|███████▏  | 289927/400000 [00:35<00:13, 7947.08it/s] 73%|███████▎  | 290802/400000 [00:35<00:13, 8170.71it/s] 73%|███████▎  | 291665/400000 [00:35<00:13, 8301.85it/s] 73%|███████▎  | 292583/400000 [00:35<00:12, 8544.89it/s] 73%|███████▎  | 293512/400000 [00:35<00:12, 8753.65it/s] 74%|███████▎  | 294391/400000 [00:35<00:12, 8734.76it/s] 74%|███████▍  | 295267/400000 [00:35<00:12, 8521.25it/s] 74%|███████▍  | 296123/400000 [00:35<00:13, 7979.67it/s] 74%|███████▍  | 296943/400000 [00:36<00:12, 8044.26it/s] 74%|███████▍  | 297855/400000 [00:36<00:12, 8337.01it/s] 75%|███████▍  | 298708/400000 [00:36<00:12, 8392.78it/s] 75%|███████▍  | 299636/400000 [00:36<00:11, 8639.88it/s] 75%|███████▌  | 300506/400000 [00:36<00:11, 8569.49it/s] 75%|███████▌  | 301415/400000 [00:36<00:11, 8717.37it/s] 76%|███████▌  | 302358/400000 [00:36<00:10, 8915.99it/s] 76%|███████▌  | 303254/400000 [00:36<00:10, 8810.63it/s] 76%|███████▌  | 304166/400000 [00:36<00:10, 8900.81it/s] 76%|███████▋  | 305059/400000 [00:36<00:10, 8795.26it/s] 76%|███████▋  | 305941/400000 [00:37<00:10, 8751.12it/s] 77%|███████▋  | 306869/400000 [00:37<00:10, 8901.29it/s] 77%|███████▋  | 307761/400000 [00:37<00:10, 8872.18it/s] 77%|███████▋  | 308650/400000 [00:37<00:10, 8825.93it/s] 77%|███████▋  | 309534/400000 [00:37<00:10, 8724.22it/s] 78%|███████▊  | 310408/400000 [00:37<00:10, 8457.57it/s] 78%|███████▊  | 311257/400000 [00:37<00:10, 8362.22it/s] 78%|███████▊  | 312096/400000 [00:37<00:10, 8259.96it/s] 78%|███████▊  | 312964/400000 [00:37<00:10, 8379.08it/s] 78%|███████▊  | 313804/400000 [00:38<00:10, 8159.51it/s] 79%|███████▊  | 314736/400000 [00:38<00:10, 8474.17it/s] 79%|███████▉  | 315674/400000 [00:38<00:09, 8726.70it/s] 79%|███████▉  | 316552/400000 [00:38<00:09, 8718.66it/s] 79%|███████▉  | 317485/400000 [00:38<00:09, 8893.19it/s] 80%|███████▉  | 318378/400000 [00:38<00:09, 8882.58it/s] 80%|███████▉  | 319319/400000 [00:38<00:08, 9034.44it/s] 80%|████████  | 320266/400000 [00:38<00:08, 9158.48it/s] 80%|████████  | 321184/400000 [00:38<00:08, 9029.15it/s] 81%|████████  | 322120/400000 [00:38<00:08, 9125.53it/s] 81%|████████  | 323035/400000 [00:39<00:08, 9053.06it/s] 81%|████████  | 323942/400000 [00:39<00:08, 9030.98it/s] 81%|████████  | 324846/400000 [00:39<00:08, 9015.59it/s] 81%|████████▏ | 325749/400000 [00:39<00:08, 8446.66it/s] 82%|████████▏ | 326602/400000 [00:39<00:08, 8346.38it/s] 82%|████████▏ | 327460/400000 [00:39<00:08, 8414.25it/s] 82%|████████▏ | 328322/400000 [00:39<00:08, 8472.62it/s] 82%|████████▏ | 329184/400000 [00:39<00:08, 8515.44it/s] 83%|████████▎ | 330038/400000 [00:39<00:08, 8486.97it/s] 83%|████████▎ | 330953/400000 [00:39<00:07, 8672.40it/s] 83%|████████▎ | 331828/400000 [00:40<00:07, 8692.86it/s] 83%|████████▎ | 332728/400000 [00:40<00:07, 8781.45it/s] 83%|████████▎ | 333665/400000 [00:40<00:07, 8948.52it/s] 84%|████████▎ | 334562/400000 [00:40<00:07, 8872.21it/s] 84%|████████▍ | 335479/400000 [00:40<00:07, 8956.45it/s] 84%|████████▍ | 336407/400000 [00:40<00:07, 9049.95it/s] 84%|████████▍ | 337334/400000 [00:40<00:06, 9112.38it/s] 85%|████████▍ | 338287/400000 [00:40<00:06, 9230.80it/s] 85%|████████▍ | 339212/400000 [00:40<00:06, 8688.03it/s] 85%|████████▌ | 340089/400000 [00:40<00:07, 8288.51it/s] 85%|████████▌ | 340927/400000 [00:41<00:07, 8034.85it/s] 85%|████████▌ | 341790/400000 [00:41<00:07, 8203.04it/s] 86%|████████▌ | 342658/400000 [00:41<00:06, 8340.39it/s] 86%|████████▌ | 343498/400000 [00:41<00:06, 8299.42it/s] 86%|████████▌ | 344376/400000 [00:41<00:06, 8437.36it/s] 86%|████████▋ | 345290/400000 [00:41<00:06, 8636.05it/s] 87%|████████▋ | 346214/400000 [00:41<00:06, 8807.27it/s] 87%|████████▋ | 347139/400000 [00:41<00:05, 8935.53it/s] 87%|████████▋ | 348036/400000 [00:41<00:05, 8681.92it/s] 87%|████████▋ | 348908/400000 [00:42<00:06, 8394.77it/s] 87%|████████▋ | 349752/400000 [00:42<00:06, 8220.75it/s] 88%|████████▊ | 350667/400000 [00:42<00:05, 8477.61it/s] 88%|████████▊ | 351528/400000 [00:42<00:05, 8515.70it/s] 88%|████████▊ | 352383/400000 [00:42<00:05, 8400.28it/s] 88%|████████▊ | 353226/400000 [00:42<00:05, 8160.07it/s] 89%|████████▊ | 354046/400000 [00:42<00:05, 8048.30it/s] 89%|████████▊ | 354963/400000 [00:42<00:05, 8354.08it/s] 89%|████████▉ | 355862/400000 [00:42<00:05, 8535.02it/s] 89%|████████▉ | 356739/400000 [00:42<00:05, 8602.41it/s] 89%|████████▉ | 357603/400000 [00:43<00:04, 8571.82it/s] 90%|████████▉ | 358526/400000 [00:43<00:04, 8758.06it/s] 90%|████████▉ | 359440/400000 [00:43<00:04, 8866.49it/s] 90%|█████████ | 360373/400000 [00:43<00:04, 8999.68it/s] 90%|█████████ | 361275/400000 [00:43<00:04, 8804.37it/s] 91%|█████████ | 362158/400000 [00:43<00:04, 8798.54it/s] 91%|█████████ | 363095/400000 [00:43<00:04, 8962.09it/s] 91%|█████████ | 364016/400000 [00:43<00:03, 9034.82it/s] 91%|█████████ | 364921/400000 [00:43<00:03, 8963.62it/s] 91%|█████████▏| 365819/400000 [00:43<00:03, 8776.21it/s] 92%|█████████▏| 366699/400000 [00:44<00:03, 8342.44it/s] 92%|█████████▏| 367539/400000 [00:44<00:03, 8161.34it/s] 92%|█████████▏| 368360/400000 [00:44<00:03, 8085.79it/s] 92%|█████████▏| 369176/400000 [00:44<00:03, 8104.86it/s] 93%|█████████▎| 370096/400000 [00:44<00:03, 8404.82it/s] 93%|█████████▎| 370976/400000 [00:44<00:03, 8517.04it/s] 93%|█████████▎| 371910/400000 [00:44<00:03, 8745.85it/s] 93%|█████████▎| 372837/400000 [00:44<00:03, 8895.91it/s] 93%|█████████▎| 373731/400000 [00:44<00:02, 8885.91it/s] 94%|█████████▎| 374658/400000 [00:44<00:02, 8997.37it/s] 94%|█████████▍| 375560/400000 [00:45<00:02, 8863.84it/s] 94%|█████████▍| 376449/400000 [00:45<00:02, 8420.75it/s] 94%|█████████▍| 377348/400000 [00:45<00:02, 8583.50it/s] 95%|█████████▍| 378212/400000 [00:45<00:02, 8406.82it/s] 95%|█████████▍| 379057/400000 [00:45<00:02, 8221.93it/s] 95%|█████████▍| 379916/400000 [00:45<00:02, 8327.74it/s] 95%|█████████▌| 380762/400000 [00:45<00:02, 8366.08it/s] 95%|█████████▌| 381601/400000 [00:45<00:02, 8295.11it/s] 96%|█████████▌| 382433/400000 [00:45<00:02, 7983.93it/s] 96%|█████████▌| 383236/400000 [00:46<00:02, 7916.52it/s] 96%|█████████▌| 384050/400000 [00:46<00:01, 7981.31it/s] 96%|█████████▌| 384961/400000 [00:46<00:01, 8288.29it/s] 96%|█████████▋| 385905/400000 [00:46<00:01, 8602.38it/s] 97%|█████████▋| 386772/400000 [00:46<00:01, 8605.30it/s] 97%|█████████▋| 387637/400000 [00:46<00:01, 8380.28it/s] 97%|█████████▋| 388543/400000 [00:46<00:01, 8571.43it/s] 97%|█████████▋| 389448/400000 [00:46<00:01, 8707.37it/s] 98%|█████████▊| 390344/400000 [00:46<00:01, 8780.31it/s] 98%|█████████▊| 391225/400000 [00:46<00:01, 8731.88it/s] 98%|█████████▊| 392111/400000 [00:47<00:00, 8768.08it/s] 98%|█████████▊| 392990/400000 [00:47<00:00, 8661.35it/s] 98%|█████████▊| 393916/400000 [00:47<00:00, 8830.70it/s] 99%|█████████▊| 394855/400000 [00:47<00:00, 8991.06it/s] 99%|█████████▉| 395756/400000 [00:47<00:00, 8689.43it/s] 99%|█████████▉| 396629/400000 [00:47<00:00, 8245.42it/s] 99%|█████████▉| 397461/400000 [00:47<00:00, 8196.30it/s]100%|█████████▉| 398286/400000 [00:47<00:00, 8167.67it/s]100%|█████████▉| 399110/400000 [00:47<00:00, 8186.97it/s]100%|█████████▉| 399967/400000 [00:48<00:00, 8297.39it/s]100%|█████████▉| 399999/400000 [00:48<00:00, 8330.80it/s]>>>model:  <mlmodels.model_tch.textcnn.Model object at 0x7f9102f3d4e0> <class 'mlmodels.model_tch.textcnn.Model'>
Spliting original file to train/valid set...
Preprocessing the text...
Creating tabular datasets...It might take a while to finish!
Building vocaulary...
Train Epoch: 1 	 Loss: 0.011152528983158444 	 Accuracy: 53
Train Epoch: 1 	 Loss: 0.011150202822924457 	 Accuracy: 55

  model saves at 55% accuracy 

  #### Inference Need return ypred, ytrue ######################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 1, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64, 'train': False}
Spliting original file to train/valid set...
Preprocessing the text...
Creating tabular datasets...It might take a while to finish!
Building vocaulary...

  {'hypermodel_pars': {}, 'data_pars': {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64, 'train': False}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}} index out of range: Tried to access index 15740 out of table with 15734 rows. at /pytorch/aten/src/TH/generic/THTensorEvenMoreMath.cpp:237 

  


### Running {'model_pars': {'model_uri': 'model_tch.matchzoo_models.py', 'model': 'BERT', 'pretrained': 0, 'embedding_output_dim': 100, 'mode': 'bert-base-uncased', 'dropout_rate': 0.2}, 'data_pars': {'dataset': 'WIKI_QA', 'data_path': 'dataset/nlp/', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 10, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': 'ztest/model_tch/MATCHZOO/BERT/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'WIKI_QA', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'train_batch_size': 4, 'test_batch_size': 1} {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'} 

  #### Setup Model   ############################################## 

  {'model_pars': {'model_uri': 'model_tch.matchzoo_models.py', 'model': 'BERT', 'pretrained': 0, 'embedding_output_dim': 100, 'mode': 'bert-base-uncased', 'dropout_rate': 0.2}, 'data_pars': {'dataset': 'WIKI_QA', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'train_batch_size': 4, 'test_batch_size': 1}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 5, 'epochs': 10, 'learning_rate': 5e-05, 'beta1': 0.9, 'beta2': 0.98, 'eps': 1e-08, 'warmup_steps': 6, 't_total': -1}, 'out_pars': {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'}} 'model_pars' 

  benchmark file saved at /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark/text/ 

  Empty DataFrame
Columns: [date_run, model_uri, json, dataset_uri, metric, metric_name]
Index: [] 

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 133, in benchmark_run
    return_ytrue=1)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 352, in predict
    ypred = model0(x_test)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/nn/modules/module.py", line 547, in __call__
    result = self.forward(*input, **kwargs)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 238, in forward
    emb_x = self.embed(x)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/nn/modules/module.py", line 547, in __call__
    result = self.forward(*input, **kwargs)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/nn/modules/sparse.py", line 114, in forward
    self.norm_type, self.scale_grad_by_freq, self.sparse)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/nn/functional.py", line 1467, in embedding
    return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse)
RuntimeError: index out of range: Tried to access index 15740 out of table with 15734 rows. at /pytorch/aten/src/TH/generic/THTensorEvenMoreMath.cpp:237
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 120, in benchmark_run
    model     = module.Model(model_pars, data_pars, compute_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/matchzoo_models.py", line 241, in __init__
    mpars =json_norm(model_pars['model_pars'])
KeyError: 'model_pars'
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do nlp_reuters 
