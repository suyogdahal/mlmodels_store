
  /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json 

  test_benchmark GITHUB_REPOSITORT GITHUB_SHA 

  Running command test_benchmark 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/389fb45d9650cca63a4024bfe3872fd162e5be0f', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/refs/heads/dev/', 'repo': 'arita37/mlmodels', 'branch': 'refs/heads/dev', 'sha': '389fb45d9650cca63a4024bfe3872fd162e5be0f', 'workflow': 'test_benchmark'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_benchmark

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/389fb45d9650cca63a4024bfe3872fd162e5be0f

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/389fb45d9650cca63a4024bfe3872fd162e5be0f

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
>>>model:  <mlmodels.model_gluon.fb_prophet.Model object at 0x7fa4822ac470> <class 'mlmodels.model_gluon.fb_prophet.Model'>

  #### Inference Need return ypred, ytrue ######################### 

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-10 17:11:30.069876
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   14.3339
metric_name                                  mean_absolute_error
Name: 0, dtype: object 

  date_run                              2020-05-10 17:11:30.072596
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   215.367
metric_name                                   mean_squared_error
Name: 1, dtype: object 

  date_run                              2020-05-10 17:11:30.075104
model_uri                              model_gluon/fb_prophet.py
json           [{'model_uri': 'model_gluon/fb_prophet.py'}, {...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   14.4309
metric_name                                median_absolute_error
Name: 2, dtype: object 

  date_run                              2020-05-10 17:11:30.077855
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
>>>model:  <mlmodels.model_keras.armdn.Model object at 0x7fa476492518> <class 'mlmodels.model_keras.armdn.Model'>

  #### Loading dataset   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Epoch 1/10

1/1 [==============================] - 1s 1s/step - loss: 351365.5000
Epoch 2/10

1/1 [==============================] - 0s 86ms/step - loss: 228124.4375
Epoch 3/10

1/1 [==============================] - 0s 76ms/step - loss: 124700.9219
Epoch 4/10

1/1 [==============================] - 0s 85ms/step - loss: 62631.9844
Epoch 5/10

1/1 [==============================] - 0s 88ms/step - loss: 32185.2168
Epoch 6/10

1/1 [==============================] - 0s 76ms/step - loss: 18117.7500
Epoch 7/10

1/1 [==============================] - 0s 77ms/step - loss: 11323.4355
Epoch 8/10

1/1 [==============================] - 0s 86ms/step - loss: 7736.0366
Epoch 9/10

1/1 [==============================] - 0s 79ms/step - loss: 5689.0073
Epoch 10/10

1/1 [==============================] - 0s 89ms/step - loss: 4451.7798

  #### Inference Need return ypred, ytrue ######################### 
[[ 9.25108567e-02  1.17012491e+01  1.03517160e+01  8.76600361e+00
   1.06215248e+01  1.08660212e+01  1.10876932e+01  1.07971525e+01
   1.08599987e+01  1.07546015e+01  1.20140257e+01  1.00905151e+01
   1.04977474e+01  1.05590000e+01  9.98902607e+00  1.04130487e+01
   1.08819990e+01  9.87847519e+00  7.89010239e+00  1.12875156e+01
   9.64954853e+00  1.11710110e+01  1.04075813e+01  1.18218679e+01
   8.94526386e+00  9.87323093e+00  1.04358406e+01  9.44140625e+00
   9.80605793e+00  1.00021706e+01  1.20269461e+01  8.72920227e+00
   1.01091452e+01  9.75950146e+00  8.84280586e+00  1.10995579e+01
   9.68612194e+00  9.77503300e+00  1.01312914e+01  8.09256840e+00
   1.03767118e+01  1.16421881e+01  1.03757334e+01  8.89156437e+00
   1.08596811e+01  1.00733137e+01  9.94974422e+00  1.08321705e+01
   9.89259243e+00  1.11992588e+01  9.56822491e+00  1.15214167e+01
   1.06582603e+01  1.16680346e+01  1.02181053e+01  1.17019882e+01
   1.13525991e+01  9.05959702e+00  9.25841713e+00  1.01881142e+01
  -3.33173752e-01  6.33604109e-01 -3.39846611e-02 -3.56346369e-03
  -1.86732328e+00 -1.69154704e-02  1.21848309e+00 -1.45819616e+00
  -1.65516809e-01  6.83197141e-01 -1.95265889e-01 -2.03558087e-01
  -5.43068707e-01 -1.52472162e+00  6.85132384e-01 -3.53485942e-01
  -5.67086935e-01 -1.50734055e+00 -1.31606829e+00  1.24557137e-01
  -1.34796739e+00  9.27828491e-01 -2.00440216e+00 -8.64762366e-01
  -2.63868153e-01  2.46280432e-01 -1.60660863e+00  1.09810805e+00
   3.28181028e-01  2.72189975e-01 -4.99304593e-01  6.90491259e-01
   4.09377098e-01  1.61606479e+00  7.65326321e-01 -2.45571971e+00
  -1.70441210e+00  7.45502830e-01 -1.53086197e+00 -7.15788603e-02
  -2.46997118e-01 -4.35893536e-02  7.41794348e-01  1.98596263e+00
  -1.50406480e-01 -8.02080393e-01  1.03899372e+00 -1.08891916e+00
   5.91915369e-01  4.31843698e-01  2.98473448e-01 -1.74855292e-02
   1.46159577e+00 -5.36068261e-01 -2.15934944e+00  1.15590954e+00
  -1.58506954e+00  4.81989384e-01  4.69767898e-01  7.28296489e-02
  -8.22576642e-01 -3.71382236e-02  8.79149079e-01  4.80195880e-01
  -9.34432745e-02 -2.97571969e+00  2.66249609e+00  9.24453974e-01
   1.59557736e+00  5.21790743e-01 -5.63642919e-01 -4.47339535e-01
   1.44104266e+00 -2.00564814e+00  9.33211148e-02  1.49735975e+00
   1.86755151e-01  5.03110647e-01 -5.67717314e-01  6.70939207e-01
   3.32753032e-01  4.33354437e-01  9.61462259e-01 -6.27185106e-01
  -1.63254142e-02 -7.78988361e-01 -6.12221718e-01  7.06163466e-01
  -1.30263209e-01  4.30976540e-01  7.62775064e-01  6.36884212e-01
   2.10405278e+00  5.88539243e-02  3.13278651e+00  1.49713302e+00
   1.18974197e+00  7.37720132e-01 -6.59061909e-01  2.17704207e-01
  -5.28938413e-01 -7.50600100e-01 -1.10457830e-01 -1.63494670e+00
  -1.10341465e+00 -5.67541063e-01 -6.90653920e-03 -9.10842419e-01
   1.87145734e+00  2.86982059e-01 -1.77675223e+00 -1.47298515e+00
   2.89999068e-01 -8.27065110e-01 -5.26572704e-01 -1.08185959e+00
  -1.35834265e+00 -2.05083832e-01 -6.59690052e-02  1.95179546e+00
   5.64328671e-01  8.80639553e+00  1.01972923e+01  1.05986805e+01
   1.07588005e+01  1.08531885e+01  1.02684965e+01  9.15140533e+00
   9.28684711e+00  1.04471340e+01  1.14876738e+01  8.85570812e+00
   1.09931707e+01  1.00602331e+01  1.02634754e+01  1.04807367e+01
   1.12898321e+01  9.83563900e+00  1.11514330e+01  1.01717081e+01
   8.65972805e+00  1.02799540e+01  8.23648643e+00  1.07603235e+01
   1.03648109e+01  1.25790873e+01  9.97324276e+00  8.79015732e+00
   1.11779413e+01  1.12058983e+01  1.13011551e+01  1.15919027e+01
   9.14476109e+00  1.01930418e+01  1.00736237e+01  1.02651787e+01
   1.01856461e+01  1.14075890e+01  1.15593176e+01  9.53751564e+00
   1.08987980e+01  1.07601500e+01  1.09184437e+01  7.84902620e+00
   1.15290947e+01  1.14424534e+01  1.18483667e+01  8.84766006e+00
   1.04010582e+01  1.20143518e+01  9.38155079e+00  1.11240139e+01
   1.13227377e+01  1.01394825e+01  1.02999001e+01  1.15905533e+01
   1.06794710e+01  1.10534945e+01  8.89991570e+00  1.04205017e+01
   6.58086896e-01  2.37489760e-01  4.94486153e-01  7.28327692e-01
   1.78458154e-01  3.98180604e-01  2.06585765e-01  2.81250453e+00
   5.70104837e-01  3.01399374e+00  5.65321565e-01  4.14052010e-01
   2.28539968e+00  1.15075994e+00  3.01398516e-01  1.86137545e+00
   8.84292483e-01  1.51306105e+00  7.06709385e-01  2.05233955e+00
   4.05127406e-01  5.70347786e-01  1.23804569e+00  8.14921677e-01
   8.18600774e-01  1.57267261e+00  1.58539367e+00  1.06483090e+00
   5.90239406e-01  1.04608464e+00  2.12297583e+00  2.29126620e+00
   6.32045269e-01  1.02642667e+00  1.91239059e+00  2.14376020e+00
   6.71662867e-01  1.30394173e+00  1.54518998e+00  1.51062655e+00
   2.04057217e+00  2.29380918e+00  5.70994973e-01  1.49758744e+00
   3.70735645e-01  2.01242471e+00  4.26145434e-01  2.04812002e+00
   2.85657501e+00  8.88477027e-01  1.52116084e+00  4.14413095e-01
   3.02428675e+00  1.19765067e+00  2.46609092e-01  7.08624005e-01
   5.68458438e-01  3.07981443e+00  1.02564955e+00  3.14941168e-01
   1.19822001e+00  1.63243842e+00  2.04967403e+00  1.86794591e+00
   1.65680671e+00  7.65712857e-01  1.34266484e+00  1.12569451e+00
   1.39458048e+00  1.43126798e+00  1.11509562e+00  2.33650255e+00
   1.73229933e+00  2.02688408e+00  2.61486101e+00  6.49219990e-01
   7.78491855e-01  1.76901758e+00  1.02057612e+00  1.32201493e+00
   6.99286103e-01  1.78892493e+00  9.64300871e-01  5.01184344e-01
   8.19555283e-01  6.85739934e-01  7.96252549e-01  2.58240390e+00
   3.28653276e-01  3.06955147e+00  8.87312531e-01  2.44104385e+00
   2.17944360e+00  3.94919276e-01  1.35700822e-01  2.13792801e-01
   3.01206946e-01  3.97838712e-01  7.76182294e-01  1.19701684e+00
   1.53534031e+00  4.73469913e-01  2.12178612e+00  1.66188419e-01
   9.50109959e-02  2.60167027e+00  1.23806655e+00  1.07630014e+00
   5.59090555e-01  7.87918866e-01  1.56997609e+00  1.40395808e+00
   1.26577854e+00  8.59452128e-01  2.13420272e-01  2.14370131e-01
   1.21154070e+00  1.94225955e+00  2.59230733e-01  4.70841765e-01
   1.50075474e+01 -3.32897663e-01 -7.89237833e+00]]

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-10 17:11:36.839572
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   91.2691
metric_name                                  mean_absolute_error
Name: 4, dtype: object 

  date_run                              2020-05-10 17:11:36.842395
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                    8354.2
metric_name                                   mean_squared_error
Name: 5, dtype: object 

  date_run                              2020-05-10 17:11:36.844632
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                   91.5527
metric_name                                median_absolute_error
Name: 6, dtype: object 

  date_run                              2020-05-10 17:11:36.847528
model_uri                                   model_keras.armdn.py
json           [{'model_uri': 'model_keras.armdn.py', 'lstm_h...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  -747.178
metric_name                                             r2_score
Name: 7, dtype: object 

  


### Running {'hypermodel_pars': {}, 'data_pars': {'forecast_length': 60, 'backcast_length': 100, 'train_data_path': 'dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': 'dataset/timeseries/stock/qqq_us_test.csv', 'col_Xinput': ['Close'], 'col_ytarget': 'Close'}, 'model_pars': {'model_uri': 'model_tch.nbeats.py', 'forecast_length': 60, 'backcast_length': 100, 'stack_types': ['NBeatsNet.GENERIC_BLOCK', 'NBeatsNet.GENERIC_BLOCK'], 'device': 'cpu', 'nb_blocks_per_stack': 3, 'thetas_dims': [7, 8], 'share_weights_in_stack': 0, 'hidden_layer_units': 256}, 'compute_pars': {'batch_size': 100, 'disable_plot': 1, 'norm_constant': 1.0, 'result_path': 'ztest/model_tch/nbeats/n_beats_{}test.png', 'model_path': 'ztest/mycheckpoint'}, 'out_pars': {'out_path': 'mlmodels/ztest/model_tch/nbeats/', 'model_checkpoint': 'ztest/model_tch/nbeats/model_checkpoint/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'forecast_length': 60, 'backcast_length': 100, 'train_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_train.csv', 'test_data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/stock/qqq_us_test.csv', 'col_Xinput': ['Close'], 'col_ytarget': 'Close'} {'out_path': 'mlmodels/ztest/model_tch/nbeats/', 'model_checkpoint': 'ztest/model_tch/nbeats/model_checkpoint/'} 

  #### Setup Model   ############################################## 
| N-Beats
| --  Stack Nbeatsnet.Generic_Block (#0) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @140343846273488
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @140342904890312
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=100, forecast_length=60, share_thetas=False) at @140342904890816
| --  Stack Nbeatsnet.Generic_Block (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @140342904891320
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @140342904891824
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=100, forecast_length=60, share_thetas=False) at @140342904892328

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.nbeats.Model object at 0x7fa475d0e0f0> <class 'mlmodels.model_tch.nbeats.Model'>
[[0.40504701]
 [0.40695405]
 [0.39710839]
 ...
 [0.93587014]
 [0.95086039]
 [0.95547277]]
--- fiting ---
grad_step = 000000, loss = 0.750113
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.710874
grad_step = 000002, loss = 0.681538
grad_step = 000003, loss = 0.650479
grad_step = 000004, loss = 0.612818
grad_step = 000005, loss = 0.567596
grad_step = 000006, loss = 0.519978
grad_step = 000007, loss = 0.480350
grad_step = 000008, loss = 0.459210
grad_step = 000009, loss = 0.440745
grad_step = 000010, loss = 0.406463
grad_step = 000011, loss = 0.378575
grad_step = 000012, loss = 0.358856
grad_step = 000013, loss = 0.344163
grad_step = 000014, loss = 0.332155
grad_step = 000015, loss = 0.320025
grad_step = 000016, loss = 0.305637
grad_step = 000017, loss = 0.289037
grad_step = 000018, loss = 0.272305
grad_step = 000019, loss = 0.257453
grad_step = 000020, loss = 0.242619
grad_step = 000021, loss = 0.227226
grad_step = 000022, loss = 0.213323
grad_step = 000023, loss = 0.200625
grad_step = 000024, loss = 0.188174
grad_step = 000025, loss = 0.176933
grad_step = 000026, loss = 0.166943
grad_step = 000027, loss = 0.156785
grad_step = 000028, loss = 0.146375
grad_step = 000029, loss = 0.136935
grad_step = 000030, loss = 0.128357
grad_step = 000031, loss = 0.119485
grad_step = 000032, loss = 0.110618
grad_step = 000033, loss = 0.102599
grad_step = 000034, loss = 0.095377
grad_step = 000035, loss = 0.088643
grad_step = 000036, loss = 0.082275
grad_step = 000037, loss = 0.076158
grad_step = 000038, loss = 0.070663
grad_step = 000039, loss = 0.065780
grad_step = 000040, loss = 0.060838
grad_step = 000041, loss = 0.056062
grad_step = 000042, loss = 0.051849
grad_step = 000043, loss = 0.047861
grad_step = 000044, loss = 0.043980
grad_step = 000045, loss = 0.040384
grad_step = 000046, loss = 0.037103
grad_step = 000047, loss = 0.034176
grad_step = 000048, loss = 0.031470
grad_step = 000049, loss = 0.028894
grad_step = 000050, loss = 0.026649
grad_step = 000051, loss = 0.024610
grad_step = 000052, loss = 0.022606
grad_step = 000053, loss = 0.020785
grad_step = 000054, loss = 0.019128
grad_step = 000055, loss = 0.017567
grad_step = 000056, loss = 0.016128
grad_step = 000057, loss = 0.014810
grad_step = 000058, loss = 0.013633
grad_step = 000059, loss = 0.012549
grad_step = 000060, loss = 0.011564
grad_step = 000061, loss = 0.010692
grad_step = 000062, loss = 0.009850
grad_step = 000063, loss = 0.009070
grad_step = 000064, loss = 0.008367
grad_step = 000065, loss = 0.007702
grad_step = 000066, loss = 0.007106
grad_step = 000067, loss = 0.006570
grad_step = 000068, loss = 0.006077
grad_step = 000069, loss = 0.005620
grad_step = 000070, loss = 0.005208
grad_step = 000071, loss = 0.004844
grad_step = 000072, loss = 0.004497
grad_step = 000073, loss = 0.004192
grad_step = 000074, loss = 0.003925
grad_step = 000075, loss = 0.003671
grad_step = 000076, loss = 0.003445
grad_step = 000077, loss = 0.003250
grad_step = 000078, loss = 0.003077
grad_step = 000079, loss = 0.002920
grad_step = 000080, loss = 0.002787
grad_step = 000081, loss = 0.002671
grad_step = 000082, loss = 0.002563
grad_step = 000083, loss = 0.002475
grad_step = 000084, loss = 0.002396
grad_step = 000085, loss = 0.002326
grad_step = 000086, loss = 0.002268
grad_step = 000087, loss = 0.002219
grad_step = 000088, loss = 0.002178
grad_step = 000089, loss = 0.002145
grad_step = 000090, loss = 0.002117
grad_step = 000091, loss = 0.002090
grad_step = 000092, loss = 0.002069
grad_step = 000093, loss = 0.002049
grad_step = 000094, loss = 0.002033
grad_step = 000095, loss = 0.002020
grad_step = 000096, loss = 0.002009
grad_step = 000097, loss = 0.001999
grad_step = 000098, loss = 0.001992
grad_step = 000099, loss = 0.001984
grad_step = 000100, loss = 0.001977
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.001971
grad_step = 000102, loss = 0.001965
grad_step = 000103, loss = 0.001959
grad_step = 000104, loss = 0.001954
grad_step = 000105, loss = 0.001949
grad_step = 000106, loss = 0.001943
grad_step = 000107, loss = 0.001939
grad_step = 000108, loss = 0.001934
grad_step = 000109, loss = 0.001929
grad_step = 000110, loss = 0.001925
grad_step = 000111, loss = 0.001920
grad_step = 000112, loss = 0.001915
grad_step = 000113, loss = 0.001910
grad_step = 000114, loss = 0.001906
grad_step = 000115, loss = 0.001901
grad_step = 000116, loss = 0.001896
grad_step = 000117, loss = 0.001892
grad_step = 000118, loss = 0.001887
grad_step = 000119, loss = 0.001882
grad_step = 000120, loss = 0.001879
grad_step = 000121, loss = 0.001878
grad_step = 000122, loss = 0.001885
grad_step = 000123, loss = 0.001913
grad_step = 000124, loss = 0.001940
grad_step = 000125, loss = 0.001938
grad_step = 000126, loss = 0.001870
grad_step = 000127, loss = 0.001849
grad_step = 000128, loss = 0.001886
grad_step = 000129, loss = 0.001880
grad_step = 000130, loss = 0.001837
grad_step = 000131, loss = 0.001833
grad_step = 000132, loss = 0.001855
grad_step = 000133, loss = 0.001848
grad_step = 000134, loss = 0.001814
grad_step = 000135, loss = 0.001815
grad_step = 000136, loss = 0.001831
grad_step = 000137, loss = 0.001815
grad_step = 000138, loss = 0.001793
grad_step = 000139, loss = 0.001796
grad_step = 000140, loss = 0.001802
grad_step = 000141, loss = 0.001789
grad_step = 000142, loss = 0.001774
grad_step = 000143, loss = 0.001776
grad_step = 000144, loss = 0.001778
grad_step = 000145, loss = 0.001766
grad_step = 000146, loss = 0.001755
grad_step = 000147, loss = 0.001755
grad_step = 000148, loss = 0.001754
grad_step = 000149, loss = 0.001745
grad_step = 000150, loss = 0.001736
grad_step = 000151, loss = 0.001733
grad_step = 000152, loss = 0.001732
grad_step = 000153, loss = 0.001725
grad_step = 000154, loss = 0.001716
grad_step = 000155, loss = 0.001711
grad_step = 000156, loss = 0.001708
grad_step = 000157, loss = 0.001704
grad_step = 000158, loss = 0.001697
grad_step = 000159, loss = 0.001690
grad_step = 000160, loss = 0.001685
grad_step = 000161, loss = 0.001681
grad_step = 000162, loss = 0.001676
grad_step = 000163, loss = 0.001669
grad_step = 000164, loss = 0.001663
grad_step = 000165, loss = 0.001657
grad_step = 000166, loss = 0.001652
grad_step = 000167, loss = 0.001647
grad_step = 000168, loss = 0.001641
grad_step = 000169, loss = 0.001635
grad_step = 000170, loss = 0.001629
grad_step = 000171, loss = 0.001622
grad_step = 000172, loss = 0.001616
grad_step = 000173, loss = 0.001609
grad_step = 000174, loss = 0.001603
grad_step = 000175, loss = 0.001597
grad_step = 000176, loss = 0.001590
grad_step = 000177, loss = 0.001585
grad_step = 000178, loss = 0.001586
grad_step = 000179, loss = 0.001597
grad_step = 000180, loss = 0.001620
grad_step = 000181, loss = 0.001640
grad_step = 000182, loss = 0.001626
grad_step = 000183, loss = 0.001583
grad_step = 000184, loss = 0.001550
grad_step = 000185, loss = 0.001557
grad_step = 000186, loss = 0.001599
grad_step = 000187, loss = 0.001644
grad_step = 000188, loss = 0.001691
grad_step = 000189, loss = 0.001678
grad_step = 000190, loss = 0.001633
grad_step = 000191, loss = 0.001528
grad_step = 000192, loss = 0.001522
grad_step = 000193, loss = 0.001593
grad_step = 000194, loss = 0.001583
grad_step = 000195, loss = 0.001546
grad_step = 000196, loss = 0.001539
grad_step = 000197, loss = 0.001518
grad_step = 000198, loss = 0.001485
grad_step = 000199, loss = 0.001499
grad_step = 000200, loss = 0.001527
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.001520
grad_step = 000202, loss = 0.001508
grad_step = 000203, loss = 0.001523
grad_step = 000204, loss = 0.001539
grad_step = 000205, loss = 0.001518
grad_step = 000206, loss = 0.001517
grad_step = 000207, loss = 0.001533
grad_step = 000208, loss = 0.001533
grad_step = 000209, loss = 0.001524
grad_step = 000210, loss = 0.001545
grad_step = 000211, loss = 0.001555
grad_step = 000212, loss = 0.001558
grad_step = 000213, loss = 0.001551
grad_step = 000214, loss = 0.001555
grad_step = 000215, loss = 0.001523
grad_step = 000216, loss = 0.001487
grad_step = 000217, loss = 0.001461
grad_step = 000218, loss = 0.001438
grad_step = 000219, loss = 0.001418
grad_step = 000220, loss = 0.001420
grad_step = 000221, loss = 0.001429
grad_step = 000222, loss = 0.001435
grad_step = 000223, loss = 0.001456
grad_step = 000224, loss = 0.001491
grad_step = 000225, loss = 0.001541
grad_step = 000226, loss = 0.001606
grad_step = 000227, loss = 0.001723
grad_step = 000228, loss = 0.001761
grad_step = 000229, loss = 0.001779
grad_step = 000230, loss = 0.001630
grad_step = 000231, loss = 0.001470
grad_step = 000232, loss = 0.001393
grad_step = 000233, loss = 0.001452
grad_step = 000234, loss = 0.001550
grad_step = 000235, loss = 0.001555
grad_step = 000236, loss = 0.001486
grad_step = 000237, loss = 0.001399
grad_step = 000238, loss = 0.001395
grad_step = 000239, loss = 0.001455
grad_step = 000240, loss = 0.001486
grad_step = 000241, loss = 0.001467
grad_step = 000242, loss = 0.001410
grad_step = 000243, loss = 0.001377
grad_step = 000244, loss = 0.001392
grad_step = 000245, loss = 0.001426
grad_step = 000246, loss = 0.001440
grad_step = 000247, loss = 0.001418
grad_step = 000248, loss = 0.001387
grad_step = 000249, loss = 0.001368
grad_step = 000250, loss = 0.001373
grad_step = 000251, loss = 0.001391
grad_step = 000252, loss = 0.001402
grad_step = 000253, loss = 0.001401
grad_step = 000254, loss = 0.001386
grad_step = 000255, loss = 0.001369
grad_step = 000256, loss = 0.001358
grad_step = 000257, loss = 0.001356
grad_step = 000258, loss = 0.001360
grad_step = 000259, loss = 0.001368
grad_step = 000260, loss = 0.001375
grad_step = 000261, loss = 0.001378
grad_step = 000262, loss = 0.001378
grad_step = 000263, loss = 0.001375
grad_step = 000264, loss = 0.001371
grad_step = 000265, loss = 0.001365
grad_step = 000266, loss = 0.001360
grad_step = 000267, loss = 0.001356
grad_step = 000268, loss = 0.001353
grad_step = 000269, loss = 0.001351
grad_step = 000270, loss = 0.001350
grad_step = 000271, loss = 0.001350
grad_step = 000272, loss = 0.001354
grad_step = 000273, loss = 0.001360
grad_step = 000274, loss = 0.001375
grad_step = 000275, loss = 0.001398
grad_step = 000276, loss = 0.001447
grad_step = 000277, loss = 0.001517
grad_step = 000278, loss = 0.001654
grad_step = 000279, loss = 0.001778
grad_step = 000280, loss = 0.001953
grad_step = 000281, loss = 0.001859
grad_step = 000282, loss = 0.001670
grad_step = 000283, loss = 0.001395
grad_step = 000284, loss = 0.001336
grad_step = 000285, loss = 0.001482
grad_step = 000286, loss = 0.001571
grad_step = 000287, loss = 0.001492
grad_step = 000288, loss = 0.001343
grad_step = 000289, loss = 0.001347
grad_step = 000290, loss = 0.001453
grad_step = 000291, loss = 0.001458
grad_step = 000292, loss = 0.001366
grad_step = 000293, loss = 0.001315
grad_step = 000294, loss = 0.001363
grad_step = 000295, loss = 0.001412
grad_step = 000296, loss = 0.001375
grad_step = 000297, loss = 0.001318
grad_step = 000298, loss = 0.001312
grad_step = 000299, loss = 0.001349
grad_step = 000300, loss = 0.001368
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.001340
grad_step = 000302, loss = 0.001306
grad_step = 000303, loss = 0.001303
grad_step = 000304, loss = 0.001323
grad_step = 000305, loss = 0.001337
grad_step = 000306, loss = 0.001324
grad_step = 000307, loss = 0.001302
grad_step = 000308, loss = 0.001292
grad_step = 000309, loss = 0.001300
grad_step = 000310, loss = 0.001311
grad_step = 000311, loss = 0.001312
grad_step = 000312, loss = 0.001302
grad_step = 000313, loss = 0.001290
grad_step = 000314, loss = 0.001284
grad_step = 000315, loss = 0.001285
grad_step = 000316, loss = 0.001290
grad_step = 000317, loss = 0.001292
grad_step = 000318, loss = 0.001290
grad_step = 000319, loss = 0.001284
grad_step = 000320, loss = 0.001279
grad_step = 000321, loss = 0.001275
grad_step = 000322, loss = 0.001274
grad_step = 000323, loss = 0.001275
grad_step = 000324, loss = 0.001276
grad_step = 000325, loss = 0.001277
grad_step = 000326, loss = 0.001276
grad_step = 000327, loss = 0.001274
grad_step = 000328, loss = 0.001272
grad_step = 000329, loss = 0.001269
grad_step = 000330, loss = 0.001267
grad_step = 000331, loss = 0.001264
grad_step = 000332, loss = 0.001262
grad_step = 000333, loss = 0.001260
grad_step = 000334, loss = 0.001259
grad_step = 000335, loss = 0.001257
grad_step = 000336, loss = 0.001256
grad_step = 000337, loss = 0.001255
grad_step = 000338, loss = 0.001253
grad_step = 000339, loss = 0.001252
grad_step = 000340, loss = 0.001251
grad_step = 000341, loss = 0.001250
grad_step = 000342, loss = 0.001248
grad_step = 000343, loss = 0.001247
grad_step = 000344, loss = 0.001246
grad_step = 000345, loss = 0.001245
grad_step = 000346, loss = 0.001244
grad_step = 000347, loss = 0.001242
grad_step = 000348, loss = 0.001241
grad_step = 000349, loss = 0.001240
grad_step = 000350, loss = 0.001239
grad_step = 000351, loss = 0.001238
grad_step = 000352, loss = 0.001237
grad_step = 000353, loss = 0.001237
grad_step = 000354, loss = 0.001240
grad_step = 000355, loss = 0.001247
grad_step = 000356, loss = 0.001270
grad_step = 000357, loss = 0.001331
grad_step = 000358, loss = 0.001506
grad_step = 000359, loss = 0.001909
grad_step = 000360, loss = 0.002952
grad_step = 000361, loss = 0.003906
grad_step = 000362, loss = 0.004659
grad_step = 000363, loss = 0.002377
grad_step = 000364, loss = 0.001401
grad_step = 000365, loss = 0.002689
grad_step = 000366, loss = 0.002789
grad_step = 000367, loss = 0.001464
grad_step = 000368, loss = 0.001781
grad_step = 000369, loss = 0.002405
grad_step = 000370, loss = 0.001559
grad_step = 000371, loss = 0.001544
grad_step = 000372, loss = 0.002127
grad_step = 000373, loss = 0.001550
grad_step = 000374, loss = 0.001423
grad_step = 000375, loss = 0.001960
grad_step = 000376, loss = 0.001392
grad_step = 000377, loss = 0.001447
grad_step = 000378, loss = 0.001703
grad_step = 000379, loss = 0.001337
grad_step = 000380, loss = 0.001400
grad_step = 000381, loss = 0.001547
grad_step = 000382, loss = 0.001270
grad_step = 000383, loss = 0.001393
grad_step = 000384, loss = 0.001444
grad_step = 000385, loss = 0.001240
grad_step = 000386, loss = 0.001397
grad_step = 000387, loss = 0.001346
grad_step = 000388, loss = 0.001253
grad_step = 000389, loss = 0.001347
grad_step = 000390, loss = 0.001302
grad_step = 000391, loss = 0.001237
grad_step = 000392, loss = 0.001325
grad_step = 000393, loss = 0.001253
grad_step = 000394, loss = 0.001244
grad_step = 000395, loss = 0.001292
grad_step = 000396, loss = 0.001233
grad_step = 000397, loss = 0.001243
grad_step = 000398, loss = 0.001267
grad_step = 000399, loss = 0.001224
grad_step = 000400, loss = 0.001233
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.001252
grad_step = 000402, loss = 0.001211
grad_step = 000403, loss = 0.001230
grad_step = 000404, loss = 0.001232
grad_step = 000405, loss = 0.001207
grad_step = 000406, loss = 0.001220
grad_step = 000407, loss = 0.001220
grad_step = 000408, loss = 0.001203
grad_step = 000409, loss = 0.001211
grad_step = 000410, loss = 0.001212
grad_step = 000411, loss = 0.001197
grad_step = 000412, loss = 0.001205
grad_step = 000413, loss = 0.001204
grad_step = 000414, loss = 0.001194
grad_step = 000415, loss = 0.001198
grad_step = 000416, loss = 0.001198
grad_step = 000417, loss = 0.001191
grad_step = 000418, loss = 0.001191
grad_step = 000419, loss = 0.001193
grad_step = 000420, loss = 0.001187
grad_step = 000421, loss = 0.001186
grad_step = 000422, loss = 0.001188
grad_step = 000423, loss = 0.001183
grad_step = 000424, loss = 0.001182
grad_step = 000425, loss = 0.001182
grad_step = 000426, loss = 0.001181
grad_step = 000427, loss = 0.001177
grad_step = 000428, loss = 0.001178
grad_step = 000429, loss = 0.001177
grad_step = 000430, loss = 0.001174
grad_step = 000431, loss = 0.001174
grad_step = 000432, loss = 0.001173
grad_step = 000433, loss = 0.001172
grad_step = 000434, loss = 0.001170
grad_step = 000435, loss = 0.001169
grad_step = 000436, loss = 0.001168
grad_step = 000437, loss = 0.001167
grad_step = 000438, loss = 0.001166
grad_step = 000439, loss = 0.001164
grad_step = 000440, loss = 0.001163
grad_step = 000441, loss = 0.001162
grad_step = 000442, loss = 0.001161
grad_step = 000443, loss = 0.001160
grad_step = 000444, loss = 0.001159
grad_step = 000445, loss = 0.001158
grad_step = 000446, loss = 0.001157
grad_step = 000447, loss = 0.001156
grad_step = 000448, loss = 0.001155
grad_step = 000449, loss = 0.001154
grad_step = 000450, loss = 0.001153
grad_step = 000451, loss = 0.001152
grad_step = 000452, loss = 0.001151
grad_step = 000453, loss = 0.001149
grad_step = 000454, loss = 0.001148
grad_step = 000455, loss = 0.001147
grad_step = 000456, loss = 0.001146
grad_step = 000457, loss = 0.001145
grad_step = 000458, loss = 0.001144
grad_step = 000459, loss = 0.001143
grad_step = 000460, loss = 0.001142
grad_step = 000461, loss = 0.001140
grad_step = 000462, loss = 0.001139
grad_step = 000463, loss = 0.001138
grad_step = 000464, loss = 0.001137
grad_step = 000465, loss = 0.001136
grad_step = 000466, loss = 0.001134
grad_step = 000467, loss = 0.001133
grad_step = 000468, loss = 0.001132
grad_step = 000469, loss = 0.001131
grad_step = 000470, loss = 0.001130
grad_step = 000471, loss = 0.001129
grad_step = 000472, loss = 0.001128
grad_step = 000473, loss = 0.001126
grad_step = 000474, loss = 0.001124
grad_step = 000475, loss = 0.001122
grad_step = 000476, loss = 0.001120
grad_step = 000477, loss = 0.001119
grad_step = 000478, loss = 0.001118
grad_step = 000479, loss = 0.001117
grad_step = 000480, loss = 0.001116
grad_step = 000481, loss = 0.001114
grad_step = 000482, loss = 0.001113
grad_step = 000483, loss = 0.001112
grad_step = 000484, loss = 0.001110
grad_step = 000485, loss = 0.001109
grad_step = 000486, loss = 0.001107
grad_step = 000487, loss = 0.001106
grad_step = 000488, loss = 0.001104
grad_step = 000489, loss = 0.001102
grad_step = 000490, loss = 0.001101
grad_step = 000491, loss = 0.001100
grad_step = 000492, loss = 0.001099
grad_step = 000493, loss = 0.001098
grad_step = 000494, loss = 0.001099
grad_step = 000495, loss = 0.001100
grad_step = 000496, loss = 0.001102
grad_step = 000497, loss = 0.001102
grad_step = 000498, loss = 0.001102
grad_step = 000499, loss = 0.001102
grad_step = 000500, loss = 0.001102
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.001099
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

  date_run                              2020-05-10 17:11:54.457389
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.277758
metric_name                                  mean_absolute_error
Name: 8, dtype: object 

  date_run                              2020-05-10 17:11:54.462309
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.213223
metric_name                                   mean_squared_error
Name: 9, dtype: object 

  date_run                              2020-05-10 17:11:54.467417
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                  0.149866
metric_name                                median_absolute_error
Name: 10, dtype: object 

  date_run                              2020-05-10 17:11:54.471203
model_uri                                    model_tch.nbeats.py
json           [{'forecast_length': 60, 'backcast_length': 10...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                     -2.24
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
0   2020-05-10 17:11:30.069876  ...    mean_absolute_error
1   2020-05-10 17:11:30.072596  ...     mean_squared_error
2   2020-05-10 17:11:30.075104  ...  median_absolute_error
3   2020-05-10 17:11:30.077855  ...               r2_score
4   2020-05-10 17:11:36.839572  ...    mean_absolute_error
5   2020-05-10 17:11:36.842395  ...     mean_squared_error
6   2020-05-10 17:11:36.844632  ...  median_absolute_error
7   2020-05-10 17:11:36.847528  ...               r2_score
8   2020-05-10 17:11:54.457389  ...    mean_absolute_error
9   2020-05-10 17:11:54.462309  ...     mean_squared_error
10  2020-05-10 17:11:54.467417  ...  median_absolute_error
11  2020-05-10 17:11:54.471203  ...               r2_score

[12 rows x 6 columns] 
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
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
0it [00:00, ?it/s]  0%|          | 0/9912422 [00:00<?, ?it/s] 30%|███       | 3014656/9912422 [00:00<00:00, 30036662.71it/s]9920512it [00:00, 32989280.31it/s]                             
0it [00:00, ?it/s]32768it [00:00, 666170.43it/s]
0it [00:00, ?it/s]  6%|▋         | 106496/1648877 [00:00<00:01, 1004668.45it/s]1654784it [00:00, 12372440.90it/s]                           
0it [00:00, ?it/s]8192it [00:00, 245269.03it/s]>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87a819e780> <class 'mlmodels.model_tch.torchhub.Model'>
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
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87458e2da0> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet18', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet18/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet152', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet152/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet152/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87a8154e48> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet152', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet152/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet152/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet34', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet34/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet34/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet34/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87458e2dd8> <class 'mlmodels.model_tch.torchhub.Model'>

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
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87a8154e48> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x0_5', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x0_5/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x0_5/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet50_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet50_2/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet50_2/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f875ab52cf8> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet50_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet50_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet50_2/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet101', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet101/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet101/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87a819ef98> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet101', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet101/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet101/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet50', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnet50/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet50/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f875ab52cf8> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnet50', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnet50/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnet50/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'wide_resnet101_2', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': 'ztest/model_tch/torchhub/wide_resnet101_2/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/wide_resnet101_2/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/wide_resnet101_2/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87a819ef98> <class 'mlmodels.model_tch.torchhub.Model'>

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
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f875ab52cf8> <class 'mlmodels.model_tch.torchhub.Model'>

  {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'shufflenet_v2_x1_0', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'train': True}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/shufflenet_v2_x1_0/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/shufflenet_v2_x1_0/'}} default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'> 

  


### Running {'hypermodel_pars': {'learning_rate': {'type': 'log_uniform', 'init': 0.01, 'range': [0.001, 0.1]}}, 'model_pars': {'model_uri': 'model_tch.torchhub.py', 'repo_uri': 'pytorch/vision', 'model': 'resnext50_32x4d', 'num_classes': 10, 'pretrained': 0, '_comment': '0: False, 1: True', 'num_layers': 5, 'size': 6, 'size_layer': 128, 'output_size': 6, 'timestep': 4, 'epoch': 2}, 'data_pars': {'dataset': 'torchvision.datasets:MNIST', 'data_path': 'dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'}, 'compute_pars': {'distributed': 'mpi', 'max_batch_sample': 10, 'epochs': 5, 'learning_rate': 0.001}, 'out_pars': {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': 'ztest/model_tch/torchhub/resnext50_32x4d/'}} ############################################ 

  #### Model URI and Config JSON 

  data_pars out_pars {'dataset': 'torchvision.datasets:MNIST', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 100, 'test_batch_size': 10, 'transform_uri': 'mlmodels.preprocess.image:torch_transform_mnist'} {'checkpointdir': 'ztest/model_tch/torchhub/resnext50_32x4d/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/resnext50_32x4d/'} 

  #### Setup Model   ############################################## 

  #### Fit  ####################################################### 
>>>model:  <mlmodels.model_tch.torchhub.Model object at 0x7f87458e30b8> <class 'mlmodels.model_tch.torchhub.Model'>

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
>>>model:  <mlmodels.model_tch.textcnn.Model object at 0x7f1acf5f21d0> <class 'mlmodels.model_tch.textcnn.Model'>
Spliting original file to train/valid set...

  Download en 
Collecting en_core_web_sm==2.2.5
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.5/en_core_web_sm-2.2.5.tar.gz (12.0 MB)
Requirement already satisfied: spacy>=2.2.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from en_core_web_sm==2.2.5) (2.2.4)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (4.46.0)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.0.3)
Requirement already satisfied: srsly<1.1.0,>=1.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.6.0)
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (45.2.0)
Requirement already satisfied: thinc==7.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (7.4.0)
Requirement already satisfied: catalogue<1.1.0,>=0.0.7 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.0)
Requirement already satisfied: blis<0.5.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.4.1)
Requirement already satisfied: plac<1.2.0,>=0.9.6 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.1.3)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.23.0)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.2)
Requirement already satisfied: numpy>=1.15.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.18.4)
Requirement already satisfied: importlib-metadata>=0.20; python_version < "3.8" in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.6.0)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.25.9)
Requirement already satisfied: idna<3,>=2.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2.9)
Requirement already satisfied: chardet<4,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2020.4.5.1)
Requirement already satisfied: zipp>=0.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from importlib-metadata>=0.20; python_version < "3.8"->catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.1.0)
Building wheels for collected packages: en-core-web-sm
  Building wheel for en-core-web-sm (setup.py): started
  Building wheel for en-core-web-sm (setup.py): finished with status 'done'
  Created wheel for en-core-web-sm: filename=en_core_web_sm-2.2.5-py3-none-any.whl size=12011738 sha256=f90d6f0cfbb7294f1993d9de2a4af3601add47a8ff493dfd58c6f2fe7336ff2e
  Stored in directory: /tmp/pip-ephem-wheel-cache-cya5ktn4/wheels/b5/94/56/596daa677d7e91038cbddfcf32b591d0c915a1b3a3e3d3c79d
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
>>>model:  <mlmodels.model_keras.textcnn.Model object at 0x7f1a671d8048> <class 'mlmodels.model_keras.textcnn.Model'>
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
  917504/17464789 [>.............................] - ETA: 0s
 3506176/17464789 [=====>........................] - ETA: 0s
 7315456/17464789 [===========>..................] - ETA: 0s
11247616/17464789 [==================>...........] - ETA: 0s
15089664/17464789 [========================>.....] - ETA: 0s
17465344/17464789 [==============================] - 0s 0us/step
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-10 17:13:14.854114: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-10 17:13:14.858201: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095190000 Hz
2020-05-10 17:13:14.858319: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55b7c1d3da90 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-10 17:13:14.858329: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 9s - loss: 7.4826 - accuracy: 0.5120
 2000/25000 [=>............................] - ETA: 6s - loss: 7.6360 - accuracy: 0.5020
 3000/25000 [==>...........................] - ETA: 5s - loss: 7.7331 - accuracy: 0.4957
 4000/25000 [===>..........................] - ETA: 4s - loss: 7.7893 - accuracy: 0.4920
 5000/25000 [=====>........................] - ETA: 4s - loss: 7.7617 - accuracy: 0.4938
 6000/25000 [======>.......................] - ETA: 3s - loss: 7.6998 - accuracy: 0.4978
 7000/25000 [=======>......................] - ETA: 3s - loss: 7.6557 - accuracy: 0.5007
 8000/25000 [========>.....................] - ETA: 3s - loss: 7.6187 - accuracy: 0.5031
 9000/25000 [=========>....................] - ETA: 3s - loss: 7.6070 - accuracy: 0.5039
10000/25000 [===========>..................] - ETA: 2s - loss: 7.5854 - accuracy: 0.5053
11000/25000 [============>.................] - ETA: 2s - loss: 7.5690 - accuracy: 0.5064
12000/25000 [=============>................] - ETA: 2s - loss: 7.5785 - accuracy: 0.5058
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6018 - accuracy: 0.5042
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6162 - accuracy: 0.5033
15000/25000 [=================>............] - ETA: 1s - loss: 7.6482 - accuracy: 0.5012
16000/25000 [==================>...........] - ETA: 1s - loss: 7.6570 - accuracy: 0.5006
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6585 - accuracy: 0.5005
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6538 - accuracy: 0.5008
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6594 - accuracy: 0.5005
20000/25000 [=======================>......] - ETA: 0s - loss: 7.6628 - accuracy: 0.5002
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6586 - accuracy: 0.5005
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6624 - accuracy: 0.5003
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6833 - accuracy: 0.4989
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6673 - accuracy: 0.5000
25000/25000 [==============================] - 5s 220us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### Inference Need return ypred, ytrue ######################### 
Loading data...

  ### Calculate Metrics    ######################################## 

  date_run                              2020-05-10 17:13:25.557786
model_uri                                 model_keras.textcnn.py
json           [{'model_uri': 'model_keras.textcnn.py', 'maxl...
dataset_uri                   /HOBBIES_1_001_CA_1_validation.csv
metric                                                       0.5
metric_name                                       accuracy_score
Name: 0, dtype: object 

  benchmark file saved at /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark/text_classification/ 

                       date_run               model_uri  ... metric     metric_name
0  2020-05-10 17:13:25.557786  model_keras.textcnn.py  ...    0.5  accuracy_score

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
2020-05-10 17:13:30.184474: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-10 17:13:30.189226: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095190000 Hz
2020-05-10 17:13:30.189402: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x561aa886bd20 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-10 17:13:30.189413: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

>>>model:  <mlmodels.model_keras.namentity_crm_bilstm.Model object at 0x7fb7bed7fd30> <class 'mlmodels.model_keras.namentity_crm_bilstm.Model'>
Train on 1 samples, validate on 1 samples
Epoch 1/1

1/1 [==============================] - 1s 900ms/step - loss: 1.9033 - crf_viterbi_accuracy: 0.0133 - val_loss: 1.7646 - val_crf_viterbi_accuracy: 0.0000e+00

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
>>>model:  <mlmodels.model_keras.textcnn.Model object at 0x7fb7b4127f60> <class 'mlmodels.model_keras.textcnn.Model'>
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 9s - loss: 7.3446 - accuracy: 0.5210
 2000/25000 [=>............................] - ETA: 6s - loss: 7.5900 - accuracy: 0.5050
 3000/25000 [==>...........................] - ETA: 5s - loss: 7.5388 - accuracy: 0.5083
 4000/25000 [===>..........................] - ETA: 4s - loss: 7.6283 - accuracy: 0.5025
 5000/25000 [=====>........................] - ETA: 4s - loss: 7.5225 - accuracy: 0.5094
 6000/25000 [======>.......................] - ETA: 3s - loss: 7.5414 - accuracy: 0.5082
 7000/25000 [=======>......................] - ETA: 3s - loss: 7.5199 - accuracy: 0.5096
 8000/25000 [========>.....................] - ETA: 3s - loss: 7.5075 - accuracy: 0.5104
 9000/25000 [=========>....................] - ETA: 3s - loss: 7.5286 - accuracy: 0.5090
10000/25000 [===========>..................] - ETA: 2s - loss: 7.5317 - accuracy: 0.5088
11000/25000 [============>.................] - ETA: 2s - loss: 7.4980 - accuracy: 0.5110
12000/25000 [=============>................] - ETA: 2s - loss: 7.5210 - accuracy: 0.5095
13000/25000 [==============>...............] - ETA: 2s - loss: 7.5451 - accuracy: 0.5079
14000/25000 [===============>..............] - ETA: 2s - loss: 7.5516 - accuracy: 0.5075
15000/25000 [=================>............] - ETA: 1s - loss: 7.5307 - accuracy: 0.5089
16000/25000 [==================>...........] - ETA: 1s - loss: 7.5487 - accuracy: 0.5077
17000/25000 [===================>..........] - ETA: 1s - loss: 7.5449 - accuracy: 0.5079
18000/25000 [====================>.........] - ETA: 1s - loss: 7.5704 - accuracy: 0.5063
19000/25000 [=====================>........] - ETA: 1s - loss: 7.5996 - accuracy: 0.5044
20000/25000 [=======================>......] - ETA: 0s - loss: 7.5984 - accuracy: 0.5045
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6235 - accuracy: 0.5028
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6401 - accuracy: 0.5017
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6433 - accuracy: 0.5015
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6590 - accuracy: 0.5005
25000/25000 [==============================] - 5s 219us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
>>>model:  <mlmodels.model_tch.transformer_sentence.Model object at 0x7fb76fe870b8> <class 'mlmodels.model_tch.transformer_sentence.Model'>

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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_keras.Autokeras notfound, No module named 'autokeras', tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 140, in benchmark_run
    metric_val = metric_eval(actual=ytrue, pred=ypred,  metric_name=metric)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 60, in metric_eval
    metric = getattr(importlib.import_module("sklearn.metrics"), metric_name)
AttributeError: module 'sklearn.metrics' has no attribute 'accuracy, f1_score'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 119, in benchmark_run
    module    = module_load(model_uri)   # "model_tch.torchhub.py"
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
NameError: Module model_tch.transformer_classifier notfound, No module named 'util_transformer', tuple index out of range
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 126, in benchmark_run
    model, session = module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_sentence.py", line 164, in fit
    output_path      = out_pars["model_path"]
KeyError: 'model_path'
.vector_cache/glove.6B.zip: 0.00B [00:00, ?B/s].vector_cache/glove.6B.zip:   0%|          | 8.19k/862M [00:00<23:50:45, 10.0kB/s].vector_cache/glove.6B.zip:   0%|          | 49.2k/862M [00:00<16:55:40, 14.1kB/s].vector_cache/glove.6B.zip:   0%|          | 221k/862M [00:01<11:54:14, 20.1kB/s] .vector_cache/glove.6B.zip:   0%|          | 901k/862M [00:01<8:20:26, 28.7kB/s] .vector_cache/glove.6B.zip:   0%|          | 3.63M/862M [00:01<5:49:23, 41.0kB/s].vector_cache/glove.6B.zip:   1%|          | 7.93M/862M [00:01<4:03:26, 58.5kB/s].vector_cache/glove.6B.zip:   1%|▏         | 12.8M/862M [00:01<2:49:32, 83.5kB/s].vector_cache/glove.6B.zip:   2%|▏         | 18.1M/862M [00:01<1:58:01, 119kB/s] .vector_cache/glove.6B.zip:   2%|▏         | 21.3M/862M [00:01<1:22:26, 170kB/s].vector_cache/glove.6B.zip:   3%|▎         | 26.8M/862M [00:01<57:24, 243kB/s]  .vector_cache/glove.6B.zip:   3%|▎         | 29.9M/862M [00:01<40:11, 345kB/s].vector_cache/glove.6B.zip:   4%|▍         | 35.3M/862M [00:02<28:01, 492kB/s].vector_cache/glove.6B.zip:   4%|▍         | 38.3M/862M [00:02<19:41, 697kB/s].vector_cache/glove.6B.zip:   5%|▍         | 43.0M/862M [00:02<13:47, 990kB/s].vector_cache/glove.6B.zip:   5%|▌         | 46.9M/862M [00:02<09:43, 1.40MB/s].vector_cache/glove.6B.zip:   6%|▌         | 52.0M/862M [00:02<06:50, 1.97MB/s].vector_cache/glove.6B.zip:   6%|▌         | 52.7M/862M [00:03<09:02, 1.49MB/s].vector_cache/glove.6B.zip:   6%|▋         | 54.9M/862M [00:03<06:29, 2.07MB/s].vector_cache/glove.6B.zip:   7%|▋         | 56.8M/862M [00:05<08:28, 1.58MB/s].vector_cache/glove.6B.zip:   7%|▋         | 57.1M/862M [00:05<08:18, 1.61MB/s].vector_cache/glove.6B.zip:   7%|▋         | 57.9M/862M [00:05<06:25, 2.08MB/s].vector_cache/glove.6B.zip:   7%|▋         | 61.0M/862M [00:07<06:44, 1.98MB/s].vector_cache/glove.6B.zip:   7%|▋         | 61.3M/862M [00:07<06:21, 2.10MB/s].vector_cache/glove.6B.zip:   7%|▋         | 62.7M/862M [00:07<04:49, 2.76MB/s].vector_cache/glove.6B.zip:   8%|▊         | 65.1M/862M [00:09<06:08, 2.16MB/s].vector_cache/glove.6B.zip:   8%|▊         | 65.5M/862M [00:09<05:41, 2.33MB/s].vector_cache/glove.6B.zip:   8%|▊         | 67.1M/862M [00:09<04:19, 3.07MB/s].vector_cache/glove.6B.zip:   8%|▊         | 69.2M/862M [00:11<06:08, 2.15MB/s].vector_cache/glove.6B.zip:   8%|▊         | 69.6M/862M [00:11<05:39, 2.33MB/s].vector_cache/glove.6B.zip:   8%|▊         | 71.2M/862M [00:11<04:17, 3.07MB/s].vector_cache/glove.6B.zip:   9%|▊         | 73.4M/862M [00:14<08:05, 1.63MB/s].vector_cache/glove.6B.zip:   9%|▊         | 73.4M/862M [00:14<18:51, 697kB/s] .vector_cache/glove.6B.zip:   9%|▊         | 73.6M/862M [00:14<16:03, 819kB/s].vector_cache/glove.6B.zip:   9%|▊         | 73.9M/862M [00:14<12:26, 1.06MB/s].vector_cache/glove.6B.zip:   9%|▊         | 75.1M/862M [00:14<09:01, 1.45MB/s].vector_cache/glove.6B.zip:   9%|▉         | 77.2M/862M [00:14<06:29, 2.02MB/s].vector_cache/glove.6B.zip:   9%|▉         | 77.5M/862M [00:15<17:02, 767kB/s] .vector_cache/glove.6B.zip:   9%|▉         | 79.5M/862M [00:15<12:06, 1.08MB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.6M/862M [00:17<11:56, 1.09MB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.7M/862M [00:17<13:41, 950kB/s] .vector_cache/glove.6B.zip:   9%|▉         | 81.8M/862M [00:17<16:34, 785kB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.8M/862M [00:17<21:16, 611kB/s].vector_cache/glove.6B.zip:   9%|▉         | 81.9M/862M [00:17<22:51, 569kB/s].vector_cache/glove.6B.zip:  10%|▉         | 81.9M/862M [00:18<24:05, 540kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.0M/862M [00:18<25:46, 504kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.0M/862M [00:18<24:08, 538kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.1M/862M [00:18<22:18, 583kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.2M/862M [00:18<21:06, 616kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.2M/862M [00:18<21:34, 603kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.3M/862M [00:18<21:06, 616kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.4M/862M [00:18<19:35, 664kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.5M/862M [00:18<16:59, 765kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.6M/862M [00:18<15:51, 820kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.7M/862M [00:19<15:12, 854kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.8M/862M [00:19<15:28, 839kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.9M/862M [00:19<14:18, 908kB/s].vector_cache/glove.6B.zip:  10%|▉         | 83.1M/862M [00:19<13:43, 946kB/s].vector_cache/glove.6B.zip:  10%|▉         | 83.2M/862M [00:19<13:05, 992kB/s].vector_cache/glove.6B.zip:  10%|▉         | 83.3M/862M [00:19<12:11, 1.06MB/s].vector_cache/glove.6B.zip:  10%|▉         | 83.5M/862M [00:19<10:37, 1.22MB/s].vector_cache/glove.6B.zip:  10%|▉         | 83.7M/862M [00:19<08:58, 1.45MB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.0M/862M [00:19<07:58, 1.63MB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.3M/862M [00:20<06:53, 1.88MB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.5M/862M [00:20<06:29, 1.99MB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.7M/862M [00:20<07:04, 1.83MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.0M/862M [00:20<06:24, 2.02MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.3M/862M [00:20<05:46, 2.24MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.4M/862M [00:20<06:26, 2.01MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.5M/862M [00:20<08:10, 1.58MB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.8M/862M [00:20<07:09, 1.81MB/s].vector_cache/glove.6B.zip:  10%|▉         | 86.1M/862M [00:20<06:21, 2.03MB/s].vector_cache/glove.6B.zip:  10%|█         | 86.3M/862M [00:20<07:15, 1.78MB/s].vector_cache/glove.6B.zip:  10%|█         | 86.4M/862M [00:21<08:34, 1.51MB/s].vector_cache/glove.6B.zip:  10%|█         | 86.5M/862M [00:21<09:10, 1.41MB/s].vector_cache/glove.6B.zip:  10%|█         | 86.6M/862M [00:21<10:05, 1.28MB/s].vector_cache/glove.6B.zip:  10%|█         | 86.9M/862M [00:21<08:20, 1.55MB/s].vector_cache/glove.6B.zip:  10%|█         | 87.5M/862M [00:21<06:34, 1.96MB/s].vector_cache/glove.6B.zip:  10%|█         | 87.8M/862M [00:21<05:46, 2.24MB/s].vector_cache/glove.6B.zip:  10%|█         | 88.2M/862M [00:21<04:58, 2.60MB/s].vector_cache/glove.6B.zip:  10%|█         | 88.8M/862M [00:21<04:10, 3.09MB/s].vector_cache/glove.6B.zip:  10%|█         | 89.3M/862M [00:21<03:42, 3.48MB/s].vector_cache/glove.6B.zip:  10%|█         | 89.8M/862M [00:22<03:21, 3.82MB/s].vector_cache/glove.6B.zip:  10%|█         | 90.4M/862M [00:22<03:02, 4.23MB/s].vector_cache/glove.6B.zip:  11%|█         | 90.9M/862M [00:22<02:50, 4.52MB/s].vector_cache/glove.6B.zip:  11%|█         | 91.5M/862M [00:22<02:38, 4.86MB/s].vector_cache/glove.6B.zip:  11%|█         | 91.7M/862M [00:22<03:46, 3.40MB/s].vector_cache/glove.6B.zip:  11%|█         | 92.0M/862M [00:22<04:21, 2.94MB/s].vector_cache/glove.6B.zip:  11%|█         | 92.5M/862M [00:22<03:43, 3.44MB/s].vector_cache/glove.6B.zip:  11%|█         | 93.0M/862M [00:23<08:53, 1.44MB/s].vector_cache/glove.6B.zip:  11%|█         | 93.4M/862M [00:23<07:30, 1.70MB/s].vector_cache/glove.6B.zip:  11%|█         | 94.2M/862M [00:23<05:46, 2.22MB/s].vector_cache/glove.6B.zip:  11%|█         | 94.8M/862M [00:23<04:45, 2.68MB/s].vector_cache/glove.6B.zip:  11%|█         | 95.6M/862M [00:23<03:46, 3.39MB/s].vector_cache/glove.6B.zip:  11%|█         | 96.3M/862M [00:23<03:16, 3.90MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.2M/862M [00:25<08:15, 1.54MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.3M/862M [00:25<10:38, 1.20MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.7M/862M [00:25<08:23, 1.52MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 98.5M/862M [00:25<06:23, 1.99MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 99.2M/862M [00:25<05:02, 2.53MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 99.8M/862M [00:25<04:08, 3.07MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 101M/862M [00:26<03:24, 3.72MB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 101M/862M [00:27<08:39, 1.46MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 101M/862M [00:27<10:34, 1.20MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 102M/862M [00:27<08:20, 1.52MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 102M/862M [00:27<06:34, 1.93MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 103M/862M [00:27<05:00, 2.53MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 104M/862M [00:27<04:06, 3.07MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 105M/862M [00:28<03:14, 3.90MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 105M/862M [00:29<16:24, 769kB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:29<15:38, 806kB/s].vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:29<11:51, 1.06MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 107M/862M [00:29<08:44, 1.44MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 108M/862M [00:29<06:40, 1.89MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 108M/862M [00:29<05:07, 2.45MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 109M/862M [00:30<04:04, 3.08MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:31<29:50, 420kB/s] .vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:31<25:01, 501kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:31<18:32, 676kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 111M/862M [00:31<13:26, 931kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 112M/862M [00:31<09:47, 1.28MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 113M/862M [00:31<07:15, 1.72MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:33<17:20, 720kB/s] .vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:33<16:16, 767kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:33<12:22, 1.01MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 115M/862M [00:33<09:07, 1.36MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 117M/862M [00:33<06:47, 1.83MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:33<05:04, 2.45MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:35<1:04:11, 193kB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:35<49:02, 253kB/s]  .vector_cache/glove.6B.zip:  14%|█▎        | 119M/862M [00:35<35:18, 351kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 120M/862M [00:35<25:08, 492kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 121M/862M [00:35<17:59, 687kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 122M/862M [00:37<16:55, 729kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 122M/862M [00:37<2:08:44, 95.8kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:37<1:30:21, 136kB/s] .vector_cache/glove.6B.zip:  14%|█▍        | 124M/862M [00:37<1:03:35, 193kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 125M/862M [00:37<44:54, 274kB/s]  .vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:37<31:50, 385kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:39<32:22, 379kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:39<26:46, 458kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:39<19:33, 627kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 128M/862M [00:39<14:07, 866kB/s].vector_cache/glove.6B.zip:  15%|█▍        | 129M/862M [00:39<10:14, 1.19MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:39<07:37, 1.60MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:41<13:17, 918kB/s] .vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:41<16:51, 724kB/s].vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:41<13:40, 891kB/s].vector_cache/glove.6B.zip:  15%|█▌        | 132M/862M [00:41<10:07, 1.20MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 133M/862M [00:41<07:29, 1.62MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:41<05:36, 2.16MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:43<15:50, 765kB/s] .vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:43<14:38, 828kB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:43<11:09, 1.09MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 136M/862M [00:43<08:11, 1.48MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 138M/862M [00:43<06:03, 1.99MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:45<11:02, 1.09MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:45<14:24, 837kB/s] .vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:45<11:45, 1.02MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 140M/862M [00:45<08:38, 1.39MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:45<06:17, 1.91MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 142M/862M [00:45<04:45, 2.52MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:47<18:29, 648kB/s] .vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:47<18:25, 651kB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:47<14:06, 850kB/s].vector_cache/glove.6B.zip:  17%|█▋        | 144M/862M [00:47<10:16, 1.16MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 146M/862M [00:47<07:27, 1.60MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:49<11:56, 999kB/s] .vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:49<13:43, 869kB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:49<10:56, 1.09MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 149M/862M [00:49<08:01, 1.48MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 151M/862M [00:49<05:47, 2.05MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 151M/862M [00:51<19:51, 597kB/s] .vector_cache/glove.6B.zip:  18%|█▊        | 151M/862M [00:51<18:25, 643kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:51<14:04, 841kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 153M/862M [00:51<10:10, 1.16MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:51<07:20, 1.61MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:53<46:23, 254kB/s] .vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:53<36:57, 319kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 156M/862M [00:53<26:54, 437kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 157M/862M [00:53<19:07, 614kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:55<15:58, 733kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:55<15:39, 748kB/s].vector_cache/glove.6B.zip:  19%|█▊        | 160M/862M [00:55<12:06, 966kB/s].vector_cache/glove.6B.zip:  19%|█▊        | 161M/862M [00:55<08:44, 1.34MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 163M/862M [00:56<08:40, 1.34MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:57<09:54, 1.17MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:57<07:55, 1.47MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 166M/862M [00:57<05:48, 2.00MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 168M/862M [00:58<07:04, 1.64MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 168M/862M [00:59<08:07, 1.42MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 168M/862M [00:59<06:30, 1.78MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 170M/862M [00:59<04:47, 2.41MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [01:00<06:53, 1.67MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [01:01<07:51, 1.46MB/s].vector_cache/glove.6B.zip:  20%|██        | 173M/862M [01:01<06:15, 1.84MB/s].vector_cache/glove.6B.zip:  20%|██        | 175M/862M [01:01<04:35, 2.49MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:02<07:20, 1.56MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:03<08:29, 1.35MB/s].vector_cache/glove.6B.zip:  20%|██        | 177M/862M [01:03<06:49, 1.68MB/s].vector_cache/glove.6B.zip:  21%|██        | 179M/862M [01:03<04:59, 2.28MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:04<06:59, 1.63MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:05<07:51, 1.45MB/s].vector_cache/glove.6B.zip:  21%|██        | 181M/862M [01:05<06:15, 1.81MB/s].vector_cache/glove.6B.zip:  21%|██        | 183M/862M [01:05<04:34, 2.47MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:06<07:55, 1.43MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:07<08:40, 1.30MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 185M/862M [01:07<06:44, 1.68MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 187M/862M [01:07<04:52, 2.31MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:08<07:03, 1.59MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:09<08:25, 1.33MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:09<06:45, 1.66MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 191M/862M [01:09<04:56, 2.26MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:10<06:54, 1.61MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:11<07:09, 1.56MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 194M/862M [01:11<05:34, 2.00MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 196M/862M [01:11<04:02, 2.75MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:12<16:21, 678kB/s] .vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:12<13:29, 822kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 198M/862M [01:13<09:56, 1.11MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:13<07:04, 1.56MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:14<10:33:40, 17.4kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:14<7:25:23, 24.7kB/s] .vector_cache/glove.6B.zip:  23%|██▎       | 202M/862M [01:15<5:11:49, 35.3kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:16<3:39:09, 50.0kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:16<2:35:57, 70.2kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 206M/862M [01:17<1:49:41, 99.7kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<1:16:36, 142kB/s] .vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:18<1:04:16, 169kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:18<46:39, 233kB/s]  .vector_cache/glove.6B.zip:  24%|██▍       | 210M/862M [01:19<33:01, 329kB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:20<24:58, 433kB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:20<19:42, 549kB/s].vector_cache/glove.6B.zip:  25%|██▍       | 214M/862M [01:21<14:20, 753kB/s].vector_cache/glove.6B.zip:  25%|██▌       | 217M/862M [01:22<11:43, 916kB/s].vector_cache/glove.6B.zip:  25%|██▌       | 218M/862M [01:22<10:25, 1.03MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 218M/862M [01:22<07:47, 1.38MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 221M/862M [01:23<05:32, 1.93MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 221M/862M [01:24<24:06, 443kB/s] .vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:24<19:04, 560kB/s].vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:24<13:53, 767kB/s].vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:26<11:23, 931kB/s].vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:26<10:10, 1.04MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 227M/862M [01:26<07:34, 1.40MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 229M/862M [01:26<05:25, 1.95MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:28<10:19, 1.02MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:28<09:19, 1.13MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 231M/862M [01:28<07:03, 1.49MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:30<06:37, 1.58MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:30<06:48, 1.54MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 235M/862M [01:30<05:14, 1.99MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 237M/862M [01:30<03:46, 2.75MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:32<10:47, 964kB/s] .vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:32<09:42, 1.07MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 239M/862M [01:32<07:14, 1.43MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:32<05:12, 1.99MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:34<07:47, 1.33MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:34<06:52, 1.50MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 243M/862M [01:34<05:06, 2.02MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 246M/862M [01:34<03:41, 2.78MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 246M/862M [01:36<13:08, 781kB/s] .vector_cache/glove.6B.zip:  29%|██▊       | 246M/862M [01:36<13:07, 782kB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:36<10:08, 1.01MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 248M/862M [01:36<07:19, 1.40MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 250M/862M [01:38<07:38, 1.34MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:38<07:17, 1.40MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:38<05:34, 1.83MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 254M/862M [01:40<05:34, 1.81MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:40<05:46, 1.76MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 256M/862M [01:40<04:29, 2.25MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 259M/862M [01:42<04:49, 2.08MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:42<05:13, 1.93MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:42<04:03, 2.48MB/s].vector_cache/glove.6B.zip:  30%|███       | 261M/862M [01:42<03:01, 3.31MB/s].vector_cache/glove.6B.zip:  30%|███       | 263M/862M [01:44<05:13, 1.91MB/s].vector_cache/glove.6B.zip:  30%|███       | 263M/862M [01:44<05:29, 1.82MB/s].vector_cache/glove.6B.zip:  31%|███       | 264M/862M [01:44<04:18, 2.32MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:46<04:39, 2.13MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:46<05:05, 1.95MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:46<03:57, 2.50MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 270M/862M [01:46<02:53, 3.42MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:48<10:20, 954kB/s] .vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:48<09:03, 1.09MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:48<06:47, 1.45MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:50<06:22, 1.54MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:50<06:18, 1.55MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<04:51, 2.01MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:52<05:00, 1.94MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:52<05:17, 1.83MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 280M/862M [01:52<04:09, 2.33MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:54<04:30, 2.14MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<04:53, 1.97MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<03:51, 2.50MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:56<04:18, 2.23MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:56<04:53, 1.96MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 289M/862M [01:56<03:47, 2.52MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 291M/862M [01:56<02:45, 3.45MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:58<09:56, 957kB/s] .vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:58<08:46, 1.08MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:58<06:32, 1.45MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [02:00<06:08, 1.54MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [02:00<06:05, 1.55MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 297M/862M [02:00<04:38, 2.03MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:00<03:20, 2.81MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 300M/862M [02:02<16:09, 580kB/s] .vector_cache/glove.6B.zip:  35%|███▍      | 300M/862M [02:02<13:08, 713kB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:02<09:37, 973kB/s].vector_cache/glove.6B.zip:  35%|███▌      | 304M/862M [02:03<08:15, 1.13MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 304M/862M [02:04<07:29, 1.24MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 305M/862M [02:04<05:40, 1.64MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 308M/862M [02:05<05:29, 1.68MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 308M/862M [02:06<05:32, 1.67MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:06<04:17, 2.15MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 312M/862M [02:07<04:32, 2.02MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 312M/862M [02:08<04:52, 1.88MB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:08<03:46, 2.42MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 315M/862M [02:08<02:45, 3.30MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 316M/862M [02:09<07:20, 1.24MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 317M/862M [02:10<06:21, 1.43MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:10<04:43, 1.92MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 320M/862M [02:11<05:03, 1.79MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 321M/862M [02:11<05:08, 1.76MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:12<03:59, 2.25MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 325M/862M [02:13<04:18, 2.08MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 325M/862M [02:13<04:38, 1.93MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:14<03:38, 2.45MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 329M/862M [02:15<04:02, 2.20MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 329M/862M [02:15<04:24, 2.02MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:16<03:25, 2.59MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 333M/862M [02:16<02:28, 3.57MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 333M/862M [02:17<1:16:11, 116kB/s].vector_cache/glove.6B.zip:  39%|███▊      | 333M/862M [02:17<54:53, 161kB/s]  .vector_cache/glove.6B.zip:  39%|███▊      | 334M/862M [02:17<38:40, 228kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 335M/862M [02:18<27:11, 323kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 337M/862M [02:19<21:36, 405kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 337M/862M [02:19<16:44, 523kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:19<12:05, 722kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:20<08:33, 1.02MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 341M/862M [02:21<11:11, 776kB/s] .vector_cache/glove.6B.zip:  40%|███▉      | 341M/862M [02:21<09:22, 927kB/s].vector_cache/glove.6B.zip:  40%|███▉      | 342M/862M [02:21<06:53, 1.26MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 344M/862M [02:22<04:55, 1.76MB/s].vector_cache/glove.6B.zip:  40%|████      | 345M/862M [02:23<08:37, 998kB/s] .vector_cache/glove.6B.zip:  40%|████      | 345M/862M [02:23<07:37, 1.13MB/s].vector_cache/glove.6B.zip:  40%|████      | 346M/862M [02:23<05:42, 1.50MB/s].vector_cache/glove.6B.zip:  41%|████      | 349M/862M [02:25<05:25, 1.57MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:25<05:18, 1.61MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:25<04:02, 2.11MB/s].vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:25<02:57, 2.87MB/s].vector_cache/glove.6B.zip:  41%|████      | 353M/862M [02:27<05:35, 1.51MB/s].vector_cache/glove.6B.zip:  41%|████      | 354M/862M [02:27<05:25, 1.56MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<04:06, 2.06MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 356M/862M [02:27<03:01, 2.79MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 358M/862M [02:29<05:08, 1.63MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 358M/862M [02:29<05:05, 1.65MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<03:56, 2.13MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<04:09, 2.00MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<05:32, 1.50MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<06:25, 1.30MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<07:03, 1.18MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<07:44, 1.08MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:32<08:34, 973kB/s] .vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:32<09:25, 884kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:32<10:04, 826kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:32<10:35, 787kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:32<10:54, 764kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:32<10:46, 773kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:32<10:40, 780kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:32<10:20, 805kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:32<10:02, 829kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:33<09:35, 868kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:33<09:39, 862kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:33<07:57, 1.04MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:33<06:04, 1.37MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 365M/862M [02:33<04:23, 1.88MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 366M/862M [02:33<04:14, 1.95MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:33<03:12, 2.58MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:33<02:30, 3.27MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:33<02:03, 4.00MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:34<01:45, 4.67MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 370M/862M [02:35<09:07, 900kB/s] .vector_cache/glove.6B.zip:  43%|████▎     | 370M/862M [02:35<07:57, 1.03MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 371M/862M [02:35<05:55, 1.38MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<04:19, 1.89MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 374M/862M [02:37<05:09, 1.57MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 374M/862M [02:37<05:03, 1.61MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 375M/862M [02:37<03:53, 2.08MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 378M/862M [02:39<04:05, 1.98MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 378M/862M [02:39<04:21, 1.85MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 379M/862M [02:39<03:24, 2.36MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:39<02:27, 3.25MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:41<11:02, 724kB/s] .vector_cache/glove.6B.zip:  44%|████▍     | 383M/862M [02:41<09:09, 873kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 383M/862M [02:41<06:42, 1.19MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:41<04:47, 1.66MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:43<08:04, 982kB/s] .vector_cache/glove.6B.zip:  45%|████▍     | 387M/862M [02:43<07:03, 1.12MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 388M/862M [02:43<05:16, 1.50MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 391M/862M [02:45<05:01, 1.57MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 391M/862M [02:45<04:54, 1.60MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 392M/862M [02:45<03:46, 2.08MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:47<03:57, 1.97MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:47<04:11, 1.86MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 396M/862M [02:47<03:14, 2.40MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 398M/862M [02:47<02:22, 3.26MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 399M/862M [02:49<05:16, 1.46MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 399M/862M [02:49<05:04, 1.52MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 400M/862M [02:49<03:52, 1.98MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 403M/862M [02:51<04:00, 1.91MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 403M/862M [02:51<04:12, 1.82MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 404M/862M [02:51<03:13, 2.36MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 406M/862M [02:51<02:20, 3.23MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 407M/862M [02:53<06:58, 1.09MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 407M/862M [02:53<06:10, 1.23MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 408M/862M [02:53<04:36, 1.64MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:53<03:17, 2.28MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:55<10:13, 735kB/s] .vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:55<08:29, 885kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 412M/862M [02:55<06:13, 1.20MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 415M/862M [02:55<04:25, 1.69MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 415M/862M [02:57<11:52, 627kB/s] .vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:57<09:37, 773kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:57<07:00, 1.06MB/s].vector_cache/glove.6B.zip:  49%|████▊     | 419M/862M [02:57<04:58, 1.49MB/s].vector_cache/glove.6B.zip:  49%|████▊     | 419M/862M [02:59<10:24, 709kB/s] .vector_cache/glove.6B.zip:  49%|████▊     | 420M/862M [02:59<08:35, 859kB/s].vector_cache/glove.6B.zip:  49%|████▉     | 421M/862M [02:59<06:17, 1.17MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 423M/862M [02:59<04:28, 1.64MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 424M/862M [03:01<07:17, 1.00MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 424M/862M [03:01<06:24, 1.14MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 425M/862M [03:01<04:44, 1.54MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 427M/862M [03:01<03:24, 2.13MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 428M/862M [03:03<06:51, 1.06MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 428M/862M [03:03<10:50, 668kB/s] .vector_cache/glove.6B.zip:  50%|████▉     | 428M/862M [03:03<08:53, 814kB/s].vector_cache/glove.6B.zip:  50%|████▉     | 429M/862M [03:03<06:31, 1.11MB/s].vector_cache/glove.6B.zip:  50%|█████     | 432M/862M [03:05<05:40, 1.27MB/s].vector_cache/glove.6B.zip:  50%|█████     | 432M/862M [03:05<05:15, 1.36MB/s].vector_cache/glove.6B.zip:  50%|█████     | 433M/862M [03:05<03:59, 1.79MB/s].vector_cache/glove.6B.zip:  51%|█████     | 436M/862M [03:07<03:59, 1.78MB/s].vector_cache/glove.6B.zip:  51%|█████     | 436M/862M [03:07<04:02, 1.75MB/s].vector_cache/glove.6B.zip:  51%|█████     | 437M/862M [03:07<03:05, 2.29MB/s].vector_cache/glove.6B.zip:  51%|█████     | 439M/862M [03:07<02:15, 3.12MB/s].vector_cache/glove.6B.zip:  51%|█████     | 440M/862M [03:09<05:08, 1.37MB/s].vector_cache/glove.6B.zip:  51%|█████     | 440M/862M [03:09<04:51, 1.45MB/s].vector_cache/glove.6B.zip:  51%|█████     | 441M/862M [03:09<03:40, 1.91MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 443M/862M [03:09<02:41, 2.59MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 444M/862M [03:11<04:11, 1.66MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 444M/862M [03:11<04:11, 1.66MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 445M/862M [03:11<03:11, 2.18MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 448M/862M [03:11<02:18, 2.99MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 448M/862M [03:13<06:02, 1.14MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 449M/862M [03:13<05:30, 1.25MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 449M/862M [03:13<04:09, 1.66MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:13<03:03, 2.24MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:15<03:58, 1.72MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<04:00, 1.71MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<03:03, 2.23MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:15<02:18, 2.95MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<03:26, 1.97MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<03:37, 1.87MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:17<02:47, 2.42MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:17<02:05, 3.22MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:31, 1.90MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:39, 1.83MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 462M/862M [03:19<02:51, 2.34MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:06, 2.13MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:24, 1.94MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 466M/862M [03:21<02:38, 2.50MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:21<01:56, 3.39MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<04:15, 1.54MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<04:08, 1.58MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 470M/862M [03:23<03:08, 2.08MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:23<02:19, 2.80MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<03:37, 1.79MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<03:41, 1.75MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 474M/862M [03:25<02:52, 2.25MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:25<02:04, 3.09MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<06:31, 983kB/s] .vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<05:42, 1.12MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 478M/862M [03:27<04:16, 1.50MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:27<03:04, 2.07MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 481M/862M [03:29<05:25, 1.17MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:29<04:55, 1.29MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:29<03:43, 1.70MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:29<02:40, 2.35MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 485M/862M [03:31<05:05, 1.23MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 486M/862M [03:31<04:42, 1.33MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 487M/862M [03:31<03:31, 1.77MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 489M/862M [03:31<02:32, 2.45MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:33<05:16, 1.18MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:33<04:48, 1.29MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 491M/862M [03:33<03:37, 1.70MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 494M/862M [03:34<03:34, 1.72MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 494M/862M [03:35<03:37, 1.69MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 495M/862M [03:35<02:45, 2.22MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 497M/862M [03:35<02:01, 3.00MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 498M/862M [03:36<03:41, 1.64MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 498M/862M [03:37<03:39, 1.66MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 499M/862M [03:37<02:47, 2.17MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:37<02:02, 2.96MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 502M/862M [03:38<04:05, 1.47MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 502M/862M [03:39<03:57, 1.52MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 503M/862M [03:39<03:00, 1.99MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:39<02:08, 2.76MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:40<14:27, 411kB/s] .vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:41<11:10, 531kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 507M/862M [03:41<08:03, 734kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 510M/862M [03:42<06:35, 889kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 510M/862M [03:42<05:39, 1.04MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:43<04:10, 1.40MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 514M/862M [03:43<02:57, 1.96MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 514M/862M [03:44<12:08, 477kB/s] .vector_cache/glove.6B.zip:  60%|█████▉    | 515M/862M [03:44<09:32, 608kB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 515M/862M [03:45<06:55, 835kB/s].vector_cache/glove.6B.zip:  60%|██████    | 518M/862M [03:46<05:46, 992kB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:46<05:03, 1.13MB/s].vector_cache/glove.6B.zip:  60%|██████    | 520M/862M [03:47<03:44, 1.53MB/s].vector_cache/glove.6B.zip:  61%|██████    | 522M/862M [03:47<02:40, 2.12MB/s].vector_cache/glove.6B.zip:  61%|██████    | 523M/862M [03:48<04:55, 1.15MB/s].vector_cache/glove.6B.zip:  61%|██████    | 523M/862M [03:48<04:29, 1.26MB/s].vector_cache/glove.6B.zip:  61%|██████    | 524M/862M [03:49<03:23, 1.66MB/s].vector_cache/glove.6B.zip:  61%|██████    | 527M/862M [03:50<03:18, 1.69MB/s].vector_cache/glove.6B.zip:  61%|██████    | 527M/862M [03:50<03:02, 1.84MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 528M/862M [03:50<02:18, 2.42MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 531M/862M [03:52<02:40, 2.06MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 531M/862M [03:52<02:35, 2.12MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 532M/862M [03:52<01:57, 2.80MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 534M/862M [03:53<01:27, 3.76MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 535M/862M [03:54<04:45, 1.15MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 535M/862M [03:54<04:15, 1.28MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:54<03:12, 1.69MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 539M/862M [03:56<03:09, 1.71MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 539M/862M [03:56<03:09, 1.70MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 540M/862M [03:56<02:26, 2.20MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 543M/862M [03:58<02:36, 2.04MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 543M/862M [03:58<02:44, 1.94MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 544M/862M [03:58<02:08, 2.47MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 547M/862M [04:00<02:23, 2.20MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 548M/862M [04:00<02:34, 2.04MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 549M/862M [04:00<02:01, 2.59MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:02<02:17, 2.26MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 552M/862M [04:02<02:29, 2.08MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 553M/862M [04:02<01:56, 2.67MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:02<01:23, 3.65MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 556M/862M [04:04<10:08, 504kB/s] .vector_cache/glove.6B.zip:  64%|██████▍   | 556M/862M [04:04<07:57, 641kB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 557M/862M [04:04<05:44, 887kB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:04<04:03, 1.25MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:06<06:25, 784kB/s] .vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:06<05:23, 934kB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 561M/862M [04:06<03:58, 1.26MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 564M/862M [04:08<03:37, 1.37MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 564M/862M [04:08<03:22, 1.47MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 565M/862M [04:08<02:34, 1.92MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 568M/862M [04:10<02:37, 1.86MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 568M/862M [04:10<02:40, 1.83MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 569M/862M [04:10<02:04, 2.35MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:12<02:16, 2.12MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:12<02:25, 2.00MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:12<01:53, 2.54MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:14<02:08, 2.23MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:14<02:20, 2.04MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 577M/862M [04:14<01:50, 2.58MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 580M/862M [04:16<02:04, 2.26MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 581M/862M [04:16<02:15, 2.08MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 582M/862M [04:16<01:46, 2.63MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 584M/862M [04:18<02:01, 2.28MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 585M/862M [04:18<02:12, 2.09MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 586M/862M [04:18<01:44, 2.64MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:20<01:59, 2.29MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:20<02:10, 2.09MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 590M/862M [04:20<01:43, 2.64MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 593M/862M [04:22<01:57, 2.29MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 593M/862M [04:22<02:08, 2.09MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 594M/862M [04:22<01:39, 2.69MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 596M/862M [04:22<01:12, 3.68MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:24<06:06, 723kB/s] .vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:24<05:03, 872kB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:24<03:43, 1.18MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:26<03:19, 1.31MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:26<03:02, 1.43MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:26<02:16, 1.90MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:26<01:38, 2.61MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:28<03:28, 1.23MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:28<03:09, 1.35MB/s].vector_cache/glove.6B.zip:  70%|███████   | 606M/862M [04:28<02:23, 1.78MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:30<02:22, 1.77MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:30<02:23, 1.76MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:30<01:51, 2.26MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:32<01:59, 2.08MB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:32<02:06, 1.97MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:32<01:37, 2.55MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:10, 3.49MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:34<06:33, 621kB/s] .vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:34<05:18, 767kB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:34<03:52, 1.05MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:36<03:22, 1.19MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:36<03:02, 1.32MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:36<02:17, 1.74MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:37<02:16, 1.74MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:38<02:15, 1.74MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 627M/862M [04:38<01:43, 2.28MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:38<01:14, 3.12MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:39<03:12, 1.20MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:40<02:54, 1.33MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:40<02:11, 1.75MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:41<02:10, 1.75MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:42<02:11, 1.73MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 635M/862M [04:42<01:41, 2.24MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:43<01:48, 2.06MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:44<01:54, 1.96MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 639M/862M [04:44<01:27, 2.53MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:44<01:03, 3.47MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:45<04:11, 876kB/s] .vector_cache/glove.6B.zip:  75%|███████▍  | 643M/862M [04:45<03:32, 1.04MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 643M/862M [04:46<02:37, 1.39MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:47<02:26, 1.48MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 647M/862M [04:47<02:19, 1.55MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 648M/862M [04:48<01:46, 2.02MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 650M/862M [04:48<01:15, 2.80MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 651M/862M [04:49<16:44, 211kB/s] .vector_cache/glove.6B.zip:  75%|███████▌  | 651M/862M [04:49<12:18, 286kB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 652M/862M [04:50<08:43, 402kB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 655M/862M [04:51<06:37, 522kB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 655M/862M [04:51<05:14, 659kB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 656M/862M [04:52<03:48, 905kB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:53<03:12, 1.06MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:53<03:08, 1.08MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:53<02:47, 1.21MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:54<02:16, 1.48MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 660M/862M [04:54<01:44, 1.93MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 661M/862M [04:54<01:19, 2.53MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 662M/862M [04:54<01:01, 3.26MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:55<02:17, 1.45MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:55<02:17, 1.44MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:55<02:06, 1.57MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 664M/862M [04:55<01:46, 1.86MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 664M/862M [04:56<01:27, 2.28MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 665M/862M [04:56<01:12, 2.73MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:56<00:56, 3.48MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:56<00:45, 4.28MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:57<03:07, 1.04MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:57<02:51, 1.14MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:57<02:22, 1.36MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 668M/862M [04:57<01:47, 1.81MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:58<01:18, 2.46MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:59<02:01, 1.58MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:59<01:57, 1.62MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 672M/862M [04:59<01:30, 2.10MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [04:59<01:04, 2.91MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [05:01<10:17, 303kB/s] .vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [05:01<07:43, 403kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 676M/862M [05:01<05:30, 561kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 679M/862M [05:03<04:19, 704kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 680M/862M [05:03<03:33, 854kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 681M/862M [05:03<02:36, 1.16MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 684M/862M [05:05<02:18, 1.29MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 684M/862M [05:05<02:07, 1.40MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 685M/862M [05:05<01:36, 1.84MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 688M/862M [05:07<01:36, 1.81MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 688M/862M [05:07<01:37, 1.78MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 689M/862M [05:07<01:15, 2.29MB/s].vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:09<01:21, 2.09MB/s].vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:09<01:26, 1.97MB/s].vector_cache/glove.6B.zip:  80%|████████  | 693M/862M [05:09<01:06, 2.55MB/s].vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:09<00:47, 3.50MB/s].vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:11<14:12, 195kB/s] .vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:11<10:24, 266kB/s].vector_cache/glove.6B.zip:  81%|████████  | 697M/862M [05:11<07:20, 374kB/s].vector_cache/glove.6B.zip:  81%|████████  | 699M/862M [05:11<05:07, 531kB/s].vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:13<04:56, 546kB/s].vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:13<03:55, 689kB/s].vector_cache/glove.6B.zip:  81%|████████▏ | 701M/862M [05:13<02:49, 949kB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:13<01:58, 1.33MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:15<05:22, 490kB/s] .vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:15<04:13, 622kB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 705M/862M [05:15<03:02, 860kB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 707M/862M [05:15<02:09, 1.20MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:17<02:28, 1.03MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 709M/862M [05:17<02:10, 1.18MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 709M/862M [05:17<01:37, 1.57MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 712M/862M [05:19<01:32, 1.61MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 713M/862M [05:19<01:30, 1.65MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 714M/862M [05:19<01:09, 2.13MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 716M/862M [05:19<00:49, 2.95MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:21<04:44, 512kB/s] .vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:21<03:44, 649kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 718M/862M [05:21<02:42, 892kB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:23<02:15, 1.04MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:23<02:00, 1.18MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 722M/862M [05:23<01:29, 1.57MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:25<01:25, 1.61MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:25<01:23, 1.65MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 726M/862M [05:25<01:02, 2.17MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 728M/862M [05:25<00:44, 2.98MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:27<02:32, 874kB/s] .vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:27<02:09, 1.03MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 730M/862M [05:27<01:35, 1.38MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 733M/862M [05:29<01:27, 1.47MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 733M/862M [05:29<01:18, 1.64MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 735M/862M [05:29<00:58, 2.19MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 737M/862M [05:31<01:04, 1.94MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 738M/862M [05:31<01:01, 2.02MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 739M/862M [05:31<00:46, 2.67MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:31<00:33, 3.65MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:33<08:23, 240kB/s] .vector_cache/glove.6B.zip:  86%|████████▌ | 742M/862M [05:33<06:12, 324kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 743M/862M [05:33<04:23, 454kB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 745M/862M [05:35<03:20, 583kB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 746M/862M [05:35<02:40, 724kB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 747M/862M [05:35<01:56, 991kB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:37<01:38, 1.14MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:37<01:29, 1.26MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 751M/862M [05:37<01:06, 1.66MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:38<01:04, 1.69MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:39<01:03, 1.71MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 755M/862M [05:39<00:48, 2.20MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:40<00:51, 2.04MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:41<00:53, 1.94MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 759M/862M [05:41<00:41, 2.47MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 761M/862M [05:41<00:29, 3.38MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:42<01:34, 1.06MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:43<01:23, 1.20MB/s].vector_cache/glove.6B.zip:  89%|████████▊ | 763M/862M [05:43<01:01, 1.61MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 765M/862M [05:43<00:43, 2.23MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:44<01:28, 1.09MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:45<01:18, 1.22MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 767M/862M [05:45<00:58, 1.62MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:46<00:55, 1.65MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:46<00:54, 1.67MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 771M/862M [05:47<00:41, 2.16MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:48<00:43, 2.02MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 775M/862M [05:48<00:45, 1.92MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 776M/862M [05:49<00:35, 2.46MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 778M/862M [05:50<00:38, 2.19MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 779M/862M [05:50<00:40, 2.04MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 780M/862M [05:51<00:31, 2.58MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:52<00:35, 2.26MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:52<00:38, 2.04MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 784M/862M [05:53<00:30, 2.59MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 786M/862M [05:53<00:21, 3.55MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 787M/862M [05:54<01:54, 657kB/s] .vector_cache/glove.6B.zip:  91%|█████████▏| 787M/862M [05:54<01:33, 808kB/s].vector_cache/glove.6B.zip:  91%|█████████▏| 788M/862M [05:55<01:07, 1.10MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:55<00:46, 1.54MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:56<02:38, 450kB/s] .vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:56<02:02, 580kB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 792M/862M [05:56<01:27, 804kB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 794M/862M [05:57<01:00, 1.13MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 795M/862M [05:58<01:09, 970kB/s] .vector_cache/glove.6B.zip:  92%|█████████▏| 795M/862M [05:58<00:59, 1.12MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 796M/862M [05:58<00:44, 1.49MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [05:59<00:30, 2.08MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [06:00<01:18, 800kB/s] .vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [06:00<01:05, 956kB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 800M/862M [06:00<00:48, 1.29MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:01<00:33, 1.80MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:02<01:07, 872kB/s] .vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:02<00:57, 1.03MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 804M/862M [06:02<00:41, 1.39MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 806M/862M [06:02<00:28, 1.93MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 807M/862M [06:04<00:48, 1.13MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 808M/862M [06:04<00:43, 1.26MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 809M/862M [06:04<00:32, 1.67MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 811M/862M [06:06<00:30, 1.69MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 812M/862M [06:06<00:29, 1.71MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 813M/862M [06:06<00:22, 2.21MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 816M/862M [06:08<00:22, 2.04MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 816M/862M [06:08<00:23, 1.94MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 817M/862M [06:08<00:18, 2.52MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 819M/862M [06:08<00:12, 3.45MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:10<00:57, 734kB/s] .vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:10<00:47, 888kB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 821M/862M [06:10<00:33, 1.21MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 823M/862M [06:10<00:23, 1.69MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:12<00:40, 951kB/s] .vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:12<00:34, 1.10MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:12<00:25, 1.48MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:14<00:22, 1.55MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:14<00:21, 1.58MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 829M/862M [06:14<00:16, 2.06MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 832M/862M [06:16<00:15, 1.95MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 832M/862M [06:16<00:15, 1.89MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:16<00:11, 2.41MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 836M/862M [06:18<00:11, 2.16MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:18<00:12, 2.02MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:18<00:09, 2.57MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:20<00:09, 2.25MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:20<00:10, 2.07MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:20<00:07, 2.63MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:22<00:07, 2.28MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:22<00:08, 2.06MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 846M/862M [06:22<00:06, 2.61MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:24<00:05, 2.27MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:24<00:06, 2.11MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:24<00:04, 2.67MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:26<00:04, 2.29MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:26<00:04, 2.10MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 854M/862M [06:26<00:03, 2.65MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:28<00:02, 2.29MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:28<00:02, 2.10MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 858M/862M [06:28<00:01, 2.65MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:30<00:00, 2.29MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:30<00:00, 2.10MB/s].vector_cache/glove.6B.zip: 862MB [06:30, 2.21MB/s]                           
  0%|          | 0/400000 [00:00<?, ?it/s]  0%|          | 876/400000 [00:00<00:45, 8755.81it/s]  0%|          | 1757/400000 [00:00<00:45, 8770.26it/s]  1%|          | 2680/400000 [00:00<00:44, 8902.93it/s]  1%|          | 3602/400000 [00:00<00:44, 8993.26it/s]  1%|          | 4489/400000 [00:00<00:44, 8953.28it/s]  1%|▏         | 5378/400000 [00:00<00:44, 8932.54it/s]  2%|▏         | 6291/400000 [00:00<00:43, 8990.50it/s]  2%|▏         | 7221/400000 [00:00<00:43, 9079.71it/s]  2%|▏         | 8198/400000 [00:00<00:42, 9275.58it/s]  2%|▏         | 9092/400000 [00:01<00:42, 9139.22it/s]  2%|▏         | 9997/400000 [00:01<00:42, 9110.66it/s]  3%|▎         | 10941/400000 [00:01<00:42, 9205.39it/s]  3%|▎         | 11859/400000 [00:01<00:42, 9197.20it/s]  3%|▎         | 12874/400000 [00:01<00:40, 9461.37it/s]  3%|▎         | 13828/400000 [00:01<00:40, 9483.92it/s]  4%|▎         | 14774/400000 [00:01<00:40, 9398.56it/s]  4%|▍         | 15713/400000 [00:01<00:41, 9252.97it/s]  4%|▍         | 16646/400000 [00:01<00:41, 9274.04it/s]  4%|▍         | 17635/400000 [00:01<00:40, 9445.55it/s]  5%|▍         | 18584/400000 [00:02<00:40, 9458.48it/s]  5%|▍         | 19545/400000 [00:02<00:40, 9500.61it/s]  5%|▌         | 20496/400000 [00:02<00:40, 9405.68it/s]  5%|▌         | 21500/400000 [00:02<00:39, 9585.78it/s]  6%|▌         | 22460/400000 [00:02<00:39, 9541.44it/s]  6%|▌         | 23415/400000 [00:02<00:39, 9433.58it/s]  6%|▌         | 24360/400000 [00:02<00:39, 9421.76it/s]  6%|▋         | 25303/400000 [00:02<00:40, 9344.85it/s]  7%|▋         | 26247/400000 [00:02<00:39, 9370.74it/s]  7%|▋         | 27185/400000 [00:02<00:39, 9353.13it/s]  7%|▋         | 28121/400000 [00:03<00:39, 9331.68it/s]  7%|▋         | 29055/400000 [00:03<00:39, 9301.29it/s]  7%|▋         | 29986/400000 [00:03<00:40, 9184.65it/s]  8%|▊         | 30905/400000 [00:03<00:40, 9140.38it/s]  8%|▊         | 31820/400000 [00:03<00:40, 9108.58it/s]  8%|▊         | 32732/400000 [00:03<00:40, 9041.07it/s]  8%|▊         | 33637/400000 [00:03<00:42, 8649.83it/s]  9%|▊         | 34520/400000 [00:03<00:42, 8701.32it/s]  9%|▉         | 35421/400000 [00:03<00:41, 8788.67it/s]  9%|▉         | 36325/400000 [00:03<00:41, 8862.27it/s]  9%|▉         | 37230/400000 [00:04<00:40, 8914.92it/s] 10%|▉         | 38191/400000 [00:04<00:39, 9110.89it/s] 10%|▉         | 39105/400000 [00:04<00:42, 8576.33it/s] 10%|▉         | 39971/400000 [00:04<00:58, 6197.95it/s] 10%|█         | 40791/400000 [00:04<00:53, 6686.32it/s] 10%|█         | 41657/400000 [00:04<00:49, 7176.85it/s] 11%|█         | 42531/400000 [00:04<00:47, 7581.75it/s] 11%|█         | 43357/400000 [00:04<00:45, 7772.67it/s] 11%|█         | 44247/400000 [00:05<00:44, 8077.24it/s] 11%|█▏        | 45125/400000 [00:05<00:42, 8274.34it/s] 11%|█▏        | 45991/400000 [00:05<00:42, 8385.07it/s] 12%|█▏        | 46846/400000 [00:05<00:42, 8403.86it/s] 12%|█▏        | 47787/400000 [00:05<00:40, 8681.88it/s] 12%|█▏        | 48709/400000 [00:05<00:39, 8834.46it/s] 12%|█▏        | 49624/400000 [00:05<00:39, 8924.69it/s] 13%|█▎        | 50523/400000 [00:05<00:39, 8763.50it/s] 13%|█▎        | 51468/400000 [00:05<00:38, 8958.15it/s] 13%|█▎        | 52389/400000 [00:05<00:38, 8972.16it/s] 13%|█▎        | 53324/400000 [00:06<00:38, 9080.76it/s] 14%|█▎        | 54241/400000 [00:06<00:37, 9105.69it/s] 14%|█▍        | 55154/400000 [00:06<00:37, 9088.75it/s] 14%|█▍        | 56125/400000 [00:06<00:37, 9265.74it/s] 14%|█▍        | 57059/400000 [00:06<00:36, 9286.14it/s] 14%|█▍        | 57989/400000 [00:06<00:37, 9205.83it/s] 15%|█▍        | 58933/400000 [00:06<00:36, 9272.72it/s] 15%|█▍        | 59873/400000 [00:06<00:36, 9308.09it/s] 15%|█▌        | 60805/400000 [00:06<00:36, 9262.40it/s] 15%|█▌        | 61736/400000 [00:06<00:36, 9274.98it/s] 16%|█▌        | 62664/400000 [00:07<00:36, 9181.03it/s] 16%|█▌        | 63583/400000 [00:07<00:36, 9161.19it/s] 16%|█▌        | 64500/400000 [00:07<00:36, 9091.94it/s] 16%|█▋        | 65410/400000 [00:07<00:37, 9041.28it/s] 17%|█▋        | 66315/400000 [00:07<00:37, 8966.47it/s] 17%|█▋        | 67216/400000 [00:07<00:37, 8976.98it/s] 17%|█▋        | 68126/400000 [00:07<00:36, 9013.29it/s] 17%|█▋        | 69028/400000 [00:07<00:36, 9003.78it/s] 17%|█▋        | 69963/400000 [00:07<00:36, 9103.65it/s] 18%|█▊        | 70874/400000 [00:07<00:36, 9100.49it/s] 18%|█▊        | 71797/400000 [00:08<00:35, 9137.86it/s] 18%|█▊        | 72712/400000 [00:08<00:35, 9099.05it/s] 18%|█▊        | 73623/400000 [00:08<00:36, 8929.90it/s] 19%|█▊        | 74543/400000 [00:08<00:36, 9007.69it/s] 19%|█▉        | 75445/400000 [00:08<00:36, 8949.65it/s] 19%|█▉        | 76376/400000 [00:08<00:35, 9052.49it/s] 19%|█▉        | 77326/400000 [00:08<00:35, 9182.15it/s] 20%|█▉        | 78246/400000 [00:08<00:35, 9171.93it/s] 20%|█▉        | 79164/400000 [00:08<00:35, 9122.45it/s] 20%|██        | 80079/400000 [00:08<00:35, 9129.69it/s] 20%|██        | 80993/400000 [00:09<00:35, 9111.53it/s] 20%|██        | 81905/400000 [00:09<00:34, 9098.93it/s] 21%|██        | 82816/400000 [00:09<00:35, 9024.73it/s] 21%|██        | 83719/400000 [00:09<00:35, 8963.60it/s] 21%|██        | 84616/400000 [00:09<00:35, 8936.87it/s] 21%|██▏       | 85510/400000 [00:09<00:35, 8809.98it/s] 22%|██▏       | 86413/400000 [00:09<00:35, 8873.04it/s] 22%|██▏       | 87301/400000 [00:09<00:35, 8841.51it/s] 22%|██▏       | 88186/400000 [00:09<00:36, 8626.85it/s] 22%|██▏       | 89071/400000 [00:09<00:35, 8690.81it/s] 22%|██▏       | 89971/400000 [00:10<00:35, 8779.11it/s] 23%|██▎       | 90884/400000 [00:10<00:34, 8879.32it/s] 23%|██▎       | 91789/400000 [00:10<00:34, 8928.00it/s] 23%|██▎       | 92686/400000 [00:10<00:34, 8939.51it/s] 23%|██▎       | 93639/400000 [00:10<00:33, 9107.08it/s] 24%|██▎       | 94551/400000 [00:10<00:33, 9092.24it/s] 24%|██▍       | 95462/400000 [00:10<00:33, 8972.50it/s] 24%|██▍       | 96409/400000 [00:10<00:33, 9116.11it/s] 24%|██▍       | 97343/400000 [00:10<00:33, 9161.83it/s] 25%|██▍       | 98261/400000 [00:10<00:33, 9140.53it/s] 25%|██▍       | 99180/400000 [00:11<00:32, 9154.51it/s] 25%|██▌       | 100096/400000 [00:11<00:32, 9119.34it/s] 25%|██▌       | 101009/400000 [00:11<00:33, 9032.63it/s] 25%|██▌       | 101913/400000 [00:11<00:33, 8870.07it/s] 26%|██▌       | 102803/400000 [00:11<00:33, 8877.99it/s] 26%|██▌       | 103692/400000 [00:11<00:33, 8875.92it/s] 26%|██▌       | 104603/400000 [00:11<00:33, 8942.79it/s] 26%|██▋       | 105509/400000 [00:11<00:32, 8977.17it/s] 27%|██▋       | 106408/400000 [00:11<00:33, 8895.95it/s] 27%|██▋       | 107299/400000 [00:11<00:32, 8883.84it/s] 27%|██▋       | 108188/400000 [00:12<00:33, 8784.49it/s] 27%|██▋       | 109074/400000 [00:12<00:33, 8806.88it/s] 27%|██▋       | 109969/400000 [00:12<00:32, 8846.90it/s] 28%|██▊       | 110854/400000 [00:12<00:32, 8817.41it/s] 28%|██▊       | 111746/400000 [00:12<00:32, 8846.28it/s] 28%|██▊       | 112638/400000 [00:12<00:32, 8867.44it/s] 28%|██▊       | 113533/400000 [00:12<00:32, 8890.29it/s] 29%|██▊       | 114429/400000 [00:12<00:32, 8909.09it/s] 29%|██▉       | 115320/400000 [00:12<00:32, 8873.18it/s] 29%|██▉       | 116208/400000 [00:13<00:32, 8776.54it/s] 29%|██▉       | 117086/400000 [00:13<00:32, 8756.39it/s] 29%|██▉       | 117983/400000 [00:13<00:31, 8818.86it/s] 30%|██▉       | 118874/400000 [00:13<00:31, 8843.71it/s] 30%|██▉       | 119759/400000 [00:13<00:31, 8821.94it/s] 30%|███       | 120642/400000 [00:13<00:32, 8641.04it/s] 30%|███       | 121525/400000 [00:13<00:32, 8694.75it/s] 31%|███       | 122426/400000 [00:13<00:31, 8784.68it/s] 31%|███       | 123306/400000 [00:13<00:31, 8789.24it/s] 31%|███       | 124186/400000 [00:13<00:31, 8763.26it/s] 31%|███▏      | 125087/400000 [00:14<00:31, 8834.97it/s] 31%|███▏      | 125983/400000 [00:14<00:30, 8870.30it/s] 32%|███▏      | 126872/400000 [00:14<00:30, 8873.59it/s] 32%|███▏      | 127761/400000 [00:14<00:30, 8877.55it/s] 32%|███▏      | 128649/400000 [00:14<00:30, 8862.93it/s] 32%|███▏      | 129536/400000 [00:14<00:30, 8864.73it/s] 33%|███▎      | 130423/400000 [00:14<00:30, 8864.39it/s] 33%|███▎      | 131310/400000 [00:14<00:30, 8806.51it/s] 33%|███▎      | 132191/400000 [00:14<00:30, 8749.39it/s] 33%|███▎      | 133073/400000 [00:14<00:30, 8768.71it/s] 33%|███▎      | 133954/400000 [00:15<00:30, 8779.81it/s] 34%|███▎      | 134853/400000 [00:15<00:29, 8839.04it/s] 34%|███▍      | 135738/400000 [00:15<00:29, 8820.98it/s] 34%|███▍      | 136621/400000 [00:15<00:29, 8784.00it/s] 34%|███▍      | 137500/400000 [00:15<00:29, 8761.46it/s] 35%|███▍      | 138379/400000 [00:15<00:29, 8767.49it/s] 35%|███▍      | 139278/400000 [00:15<00:29, 8832.56it/s] 35%|███▌      | 140178/400000 [00:15<00:29, 8880.92it/s] 35%|███▌      | 141072/400000 [00:15<00:29, 8896.84it/s] 35%|███▌      | 141962/400000 [00:15<00:29, 8797.92it/s] 36%|███▌      | 142861/400000 [00:16<00:29, 8852.73it/s] 36%|███▌      | 143807/400000 [00:16<00:28, 9026.38it/s] 36%|███▌      | 144745/400000 [00:16<00:27, 9128.74it/s] 36%|███▋      | 145659/400000 [00:16<00:28, 9032.62it/s] 37%|███▋      | 146564/400000 [00:16<00:28, 8963.92it/s] 37%|███▋      | 147462/400000 [00:16<00:28, 8935.43it/s] 37%|███▋      | 148357/400000 [00:16<00:28, 8751.02it/s] 37%|███▋      | 149251/400000 [00:16<00:28, 8803.20it/s] 38%|███▊      | 150161/400000 [00:16<00:28, 8889.24it/s] 38%|███▊      | 151051/400000 [00:16<00:28, 8877.82it/s] 38%|███▊      | 151945/400000 [00:17<00:27, 8896.20it/s] 38%|███▊      | 152852/400000 [00:17<00:27, 8945.44it/s] 38%|███▊      | 153747/400000 [00:17<00:27, 8935.67it/s] 39%|███▊      | 154645/400000 [00:17<00:27, 8946.39it/s] 39%|███▉      | 155540/400000 [00:17<00:27, 8931.85it/s] 39%|███▉      | 156434/400000 [00:17<00:27, 8929.14it/s] 39%|███▉      | 157341/400000 [00:17<00:27, 8969.22it/s] 40%|███▉      | 158268/400000 [00:17<00:26, 9054.79it/s] 40%|███▉      | 159198/400000 [00:17<00:26, 9124.21it/s] 40%|████      | 160111/400000 [00:17<00:26, 9072.72it/s] 40%|████      | 161019/400000 [00:18<00:26, 9068.65it/s] 40%|████      | 161971/400000 [00:18<00:25, 9198.82it/s] 41%|████      | 162905/400000 [00:18<00:25, 9238.32it/s] 41%|████      | 163844/400000 [00:18<00:25, 9282.44it/s] 41%|████      | 164773/400000 [00:18<00:25, 9263.98it/s] 41%|████▏     | 165700/400000 [00:18<00:25, 9264.39it/s] 42%|████▏     | 166627/400000 [00:18<00:25, 9246.12it/s] 42%|████▏     | 167553/400000 [00:18<00:25, 9249.66it/s] 42%|████▏     | 168479/400000 [00:18<00:25, 9236.82it/s] 42%|████▏     | 169403/400000 [00:18<00:25, 9184.39it/s] 43%|████▎     | 170342/400000 [00:19<00:24, 9243.73it/s] 43%|████▎     | 171272/400000 [00:19<00:24, 9260.14it/s] 43%|████▎     | 172214/400000 [00:19<00:24, 9306.19it/s] 43%|████▎     | 173145/400000 [00:19<00:24, 9261.81it/s] 44%|████▎     | 174072/400000 [00:19<00:24, 9093.92it/s] 44%|████▎     | 174983/400000 [00:19<00:24, 9075.25it/s] 44%|████▍     | 175933/400000 [00:19<00:24, 9196.39it/s] 44%|████▍     | 176908/400000 [00:19<00:23, 9355.10it/s] 44%|████▍     | 177864/400000 [00:19<00:23, 9415.39it/s] 45%|████▍     | 178823/400000 [00:19<00:23, 9464.35it/s] 45%|████▍     | 179771/400000 [00:20<00:23, 9429.31it/s] 45%|████▌     | 180776/400000 [00:20<00:22, 9606.67it/s] 45%|████▌     | 181738/400000 [00:20<00:23, 9307.27it/s] 46%|████▌     | 182672/400000 [00:20<00:23, 9104.74it/s] 46%|████▌     | 183586/400000 [00:20<00:23, 9108.94it/s] 46%|████▌     | 184542/400000 [00:20<00:23, 9238.35it/s] 46%|████▋     | 185497/400000 [00:20<00:22, 9327.45it/s] 47%|████▋     | 186432/400000 [00:20<00:22, 9318.45it/s] 47%|████▋     | 187398/400000 [00:20<00:22, 9416.01it/s] 47%|████▋     | 188381/400000 [00:20<00:22, 9535.56it/s] 47%|████▋     | 189336/400000 [00:21<00:22, 9526.01it/s] 48%|████▊     | 190297/400000 [00:21<00:21, 9549.01it/s] 48%|████▊     | 191253/400000 [00:21<00:22, 9476.36it/s] 48%|████▊     | 192202/400000 [00:21<00:22, 9311.47it/s] 48%|████▊     | 193135/400000 [00:21<00:22, 9273.05it/s] 49%|████▊     | 194064/400000 [00:21<00:22, 9264.65it/s] 49%|████▉     | 195016/400000 [00:21<00:21, 9339.49it/s] 49%|████▉     | 195992/400000 [00:21<00:21, 9459.40it/s] 49%|████▉     | 196958/400000 [00:21<00:21, 9517.93it/s] 49%|████▉     | 197911/400000 [00:21<00:21, 9485.00it/s] 50%|████▉     | 198860/400000 [00:22<00:21, 9331.60it/s] 50%|████▉     | 199815/400000 [00:22<00:21, 9395.25it/s] 50%|█████     | 200761/400000 [00:22<00:21, 9413.95it/s] 50%|█████     | 201703/400000 [00:22<00:21, 9305.94it/s] 51%|█████     | 202635/400000 [00:22<00:21, 9153.26it/s] 51%|█████     | 203574/400000 [00:22<00:21, 9220.24it/s] 51%|█████     | 204497/400000 [00:22<00:21, 9130.66it/s] 51%|█████▏    | 205411/400000 [00:22<00:21, 9006.31it/s] 52%|█████▏    | 206345/400000 [00:22<00:21, 9103.25it/s] 52%|█████▏    | 207257/400000 [00:23<00:21, 9082.02it/s] 52%|█████▏    | 208166/400000 [00:23<00:21, 9083.78it/s] 52%|█████▏    | 209091/400000 [00:23<00:20, 9132.25it/s] 53%|█████▎    | 210022/400000 [00:23<00:20, 9184.51it/s] 53%|█████▎    | 210942/400000 [00:23<00:20, 9186.66it/s] 53%|█████▎    | 211861/400000 [00:23<00:20, 9168.69it/s] 53%|█████▎    | 212779/400000 [00:23<00:20, 9151.40it/s] 53%|█████▎    | 213697/400000 [00:23<00:20, 9159.75it/s] 54%|█████▎    | 214634/400000 [00:23<00:20, 9220.56it/s] 54%|█████▍    | 215557/400000 [00:23<00:20, 9201.53it/s] 54%|█████▍    | 216478/400000 [00:24<00:20, 9045.59it/s] 54%|█████▍    | 217396/400000 [00:24<00:20, 9084.49it/s] 55%|█████▍    | 218330/400000 [00:24<00:19, 9156.95it/s] 55%|█████▍    | 219262/400000 [00:24<00:19, 9205.13it/s] 55%|█████▌    | 220194/400000 [00:24<00:19, 9237.64it/s] 55%|█████▌    | 221166/400000 [00:24<00:19, 9375.78it/s] 56%|█████▌    | 222105/400000 [00:24<00:18, 9374.32it/s] 56%|█████▌    | 223060/400000 [00:24<00:18, 9424.58it/s] 56%|█████▌    | 224003/400000 [00:24<00:18, 9371.04it/s] 56%|█████▌    | 224941/400000 [00:24<00:18, 9315.99it/s] 56%|█████▋    | 225873/400000 [00:25<00:18, 9278.10it/s] 57%|█████▋    | 226802/400000 [00:25<00:19, 9041.25it/s] 57%|█████▋    | 227742/400000 [00:25<00:18, 9144.21it/s] 57%|█████▋    | 228669/400000 [00:25<00:18, 9180.06it/s] 57%|█████▋    | 229588/400000 [00:25<00:18, 9027.41it/s] 58%|█████▊    | 230492/400000 [00:25<00:18, 8991.30it/s] 58%|█████▊    | 231393/400000 [00:25<00:18, 8974.93it/s] 58%|█████▊    | 232342/400000 [00:25<00:18, 9121.10it/s] 58%|█████▊    | 233294/400000 [00:25<00:18, 9236.59it/s] 59%|█████▊    | 234230/400000 [00:25<00:17, 9271.71it/s] 59%|█████▉    | 235158/400000 [00:26<00:17, 9242.90it/s] 59%|█████▉    | 236083/400000 [00:26<00:17, 9238.80it/s] 59%|█████▉    | 237008/400000 [00:26<00:17, 9228.10it/s] 59%|█████▉    | 237932/400000 [00:26<00:17, 9209.26it/s] 60%|█████▉    | 238859/400000 [00:26<00:17, 9226.76it/s] 60%|█████▉    | 239782/400000 [00:26<00:17, 9217.45it/s] 60%|██████    | 240704/400000 [00:26<00:17, 9089.41it/s] 60%|██████    | 241625/400000 [00:26<00:17, 9124.06it/s] 61%|██████    | 242555/400000 [00:26<00:17, 9173.80it/s] 61%|██████    | 243481/400000 [00:26<00:17, 9197.12it/s] 61%|██████    | 244401/400000 [00:27<00:17, 9104.53it/s] 61%|██████▏   | 245312/400000 [00:27<00:17, 9002.81it/s] 62%|██████▏   | 246232/400000 [00:27<00:16, 9059.77it/s] 62%|██████▏   | 247164/400000 [00:27<00:16, 9133.72it/s] 62%|██████▏   | 248105/400000 [00:27<00:16, 9212.49it/s] 62%|██████▏   | 249027/400000 [00:27<00:16, 9028.50it/s] 62%|██████▏   | 249932/400000 [00:27<00:16, 9006.14it/s] 63%|██████▎   | 250887/400000 [00:27<00:16, 9160.78it/s] 63%|██████▎   | 251840/400000 [00:27<00:15, 9266.53it/s] 63%|██████▎   | 252769/400000 [00:27<00:15, 9272.05it/s] 63%|██████▎   | 253699/400000 [00:28<00:15, 9279.75it/s] 64%|██████▎   | 254628/400000 [00:28<00:15, 9210.75it/s] 64%|██████▍   | 255565/400000 [00:28<00:15, 9255.21it/s] 64%|██████▍   | 256511/400000 [00:28<00:15, 9314.37it/s] 64%|██████▍   | 257445/400000 [00:28<00:15, 9320.74it/s] 65%|██████▍   | 258378/400000 [00:28<00:15, 9156.59it/s] 65%|██████▍   | 259295/400000 [00:28<00:15, 9117.01it/s] 65%|██████▌   | 260208/400000 [00:28<00:15, 9039.48it/s] 65%|██████▌   | 261128/400000 [00:28<00:15, 9085.27it/s] 66%|██████▌   | 262044/400000 [00:28<00:15, 9105.75it/s] 66%|██████▌   | 262959/400000 [00:29<00:15, 9116.71it/s] 66%|██████▌   | 263871/400000 [00:29<00:15, 9027.19it/s] 66%|██████▌   | 264775/400000 [00:29<00:15, 9002.14it/s] 66%|██████▋   | 265728/400000 [00:29<00:14, 9152.71it/s] 67%|██████▋   | 266645/400000 [00:29<00:14, 9060.98it/s] 67%|██████▋   | 267555/400000 [00:29<00:14, 9070.91it/s] 67%|██████▋   | 268463/400000 [00:29<00:14, 8972.56it/s] 67%|██████▋   | 269373/400000 [00:29<00:14, 9007.63it/s] 68%|██████▊   | 270288/400000 [00:29<00:14, 9043.09it/s] 68%|██████▊   | 271193/400000 [00:29<00:14, 8961.84it/s] 68%|██████▊   | 272107/400000 [00:30<00:14, 9012.94it/s] 68%|██████▊   | 273009/400000 [00:30<00:14, 8934.24it/s] 68%|██████▊   | 273912/400000 [00:30<00:14, 8960.22it/s] 69%|██████▊   | 274809/400000 [00:30<00:13, 8947.19it/s] 69%|██████▉   | 275708/400000 [00:30<00:13, 8957.45it/s] 69%|██████▉   | 276606/400000 [00:30<00:13, 8963.16it/s] 69%|██████▉   | 277503/400000 [00:30<00:13, 8864.62it/s] 70%|██████▉   | 278390/400000 [00:30<00:13, 8861.33it/s] 70%|██████▉   | 279308/400000 [00:30<00:13, 8951.44it/s] 70%|███████   | 280221/400000 [00:31<00:13, 9002.89it/s] 70%|███████   | 281145/400000 [00:31<00:13, 9070.87it/s] 71%|███████   | 282060/400000 [00:31<00:12, 9091.79it/s] 71%|███████   | 282982/400000 [00:31<00:12, 9127.07it/s] 71%|███████   | 283913/400000 [00:31<00:12, 9179.71it/s] 71%|███████   | 284832/400000 [00:31<00:12, 9176.97it/s] 71%|███████▏  | 285750/400000 [00:31<00:12, 9150.17it/s] 72%|███████▏  | 286666/400000 [00:31<00:12, 9054.68it/s] 72%|███████▏  | 287572/400000 [00:31<00:12, 9049.53it/s] 72%|███████▏  | 288478/400000 [00:31<00:12, 8964.22it/s] 72%|███████▏  | 289386/400000 [00:32<00:12, 8997.45it/s] 73%|███████▎  | 290287/400000 [00:32<00:12, 8990.10it/s] 73%|███████▎  | 291187/400000 [00:32<00:12, 8976.70it/s] 73%|███████▎  | 292101/400000 [00:32<00:11, 9022.60it/s] 73%|███████▎  | 293004/400000 [00:32<00:11, 8979.04it/s] 73%|███████▎  | 293903/400000 [00:32<00:11, 8916.89it/s] 74%|███████▎  | 294795/400000 [00:32<00:11, 8917.54it/s] 74%|███████▍  | 295687/400000 [00:32<00:11, 8911.08it/s] 74%|███████▍  | 296603/400000 [00:32<00:11, 8983.37it/s] 74%|███████▍  | 297502/400000 [00:32<00:11, 8912.92it/s] 75%|███████▍  | 298411/400000 [00:33<00:11, 8964.88it/s] 75%|███████▍  | 299314/400000 [00:33<00:11, 8983.72it/s] 75%|███████▌  | 300238/400000 [00:33<00:11, 9043.58it/s] 75%|███████▌  | 301169/400000 [00:33<00:10, 9119.95it/s] 76%|███████▌  | 302101/400000 [00:33<00:10, 9177.13it/s] 76%|███████▌  | 303020/400000 [00:33<00:10, 9091.27it/s] 76%|███████▌  | 303930/400000 [00:33<00:10, 8974.40it/s] 76%|███████▌  | 304851/400000 [00:33<00:10, 9043.30it/s] 76%|███████▋  | 305768/400000 [00:33<00:10, 9080.13it/s] 77%|███████▋  | 306680/400000 [00:33<00:10, 9090.79it/s] 77%|███████▋  | 307594/400000 [00:34<00:10, 9105.11it/s] 77%|███████▋  | 308505/400000 [00:34<00:10, 9053.68it/s] 77%|███████▋  | 309411/400000 [00:34<00:10, 9005.87it/s] 78%|███████▊  | 310312/400000 [00:34<00:10, 8961.11it/s] 78%|███████▊  | 311209/400000 [00:34<00:10, 8866.96it/s] 78%|███████▊  | 312170/400000 [00:34<00:09, 9075.88it/s] 78%|███████▊  | 313109/400000 [00:34<00:09, 9165.32it/s] 79%|███████▊  | 314028/400000 [00:34<00:09, 9171.69it/s] 79%|███████▊  | 314947/400000 [00:34<00:09, 9122.47it/s] 79%|███████▉  | 315886/400000 [00:34<00:09, 9199.54it/s] 79%|███████▉  | 316810/400000 [00:35<00:09, 9208.50it/s] 79%|███████▉  | 317767/400000 [00:35<00:08, 9313.93it/s] 80%|███████▉  | 318740/400000 [00:35<00:08, 9434.52it/s] 80%|███████▉  | 319685/400000 [00:35<00:08, 9385.21it/s] 80%|████████  | 320630/400000 [00:35<00:08, 9401.96it/s] 80%|████████  | 321576/400000 [00:35<00:08, 9418.58it/s] 81%|████████  | 322519/400000 [00:35<00:08, 9383.76it/s] 81%|████████  | 323466/400000 [00:35<00:08, 9408.62it/s] 81%|████████  | 324408/400000 [00:35<00:08, 9296.00it/s] 81%|████████▏ | 325339/400000 [00:35<00:08, 9268.52it/s] 82%|████████▏ | 326267/400000 [00:36<00:08, 9209.22it/s] 82%|████████▏ | 327252/400000 [00:36<00:07, 9389.89it/s] 82%|████████▏ | 328193/400000 [00:36<00:07, 9359.73it/s] 82%|████████▏ | 329130/400000 [00:36<00:07, 9051.17it/s] 83%|████████▎ | 330079/400000 [00:36<00:07, 9178.36it/s] 83%|████████▎ | 331029/400000 [00:36<00:07, 9270.87it/s] 83%|████████▎ | 331958/400000 [00:36<00:07, 9252.53it/s] 83%|████████▎ | 332922/400000 [00:36<00:07, 9363.85it/s] 83%|████████▎ | 333860/400000 [00:36<00:07, 9271.93it/s] 84%|████████▎ | 334789/400000 [00:36<00:07, 9112.61it/s] 84%|████████▍ | 335702/400000 [00:37<00:07, 9114.88it/s] 84%|████████▍ | 336615/400000 [00:37<00:07, 9018.51it/s] 84%|████████▍ | 337546/400000 [00:37<00:06, 9101.90it/s] 85%|████████▍ | 338481/400000 [00:37<00:06, 9171.88it/s] 85%|████████▍ | 339422/400000 [00:37<00:06, 9239.18it/s] 85%|████████▌ | 340361/400000 [00:37<00:06, 9281.36it/s] 85%|████████▌ | 341303/400000 [00:37<00:06, 9320.57it/s] 86%|████████▌ | 342236/400000 [00:37<00:06, 9205.14it/s] 86%|████████▌ | 343158/400000 [00:37<00:06, 9117.36it/s] 86%|████████▌ | 344071/400000 [00:37<00:06, 9023.25it/s] 86%|████████▌ | 344976/400000 [00:38<00:06, 9028.97it/s] 86%|████████▋ | 345880/400000 [00:38<00:06, 9002.57it/s] 87%|████████▋ | 346808/400000 [00:38<00:05, 9081.68it/s] 87%|████████▋ | 347717/400000 [00:38<00:05, 9064.83it/s] 87%|████████▋ | 348624/400000 [00:38<00:05, 9051.47it/s] 87%|████████▋ | 349555/400000 [00:38<00:05, 9125.67it/s] 88%|████████▊ | 350486/400000 [00:38<00:05, 9179.27it/s] 88%|████████▊ | 351405/400000 [00:38<00:05, 9168.64it/s] 88%|████████▊ | 352323/400000 [00:38<00:05, 9087.19it/s] 88%|████████▊ | 353233/400000 [00:39<00:05, 8922.90it/s] 89%|████████▊ | 354143/400000 [00:39<00:05, 8975.02it/s] 89%|████████▉ | 355063/400000 [00:39<00:04, 9039.71it/s] 89%|████████▉ | 355968/400000 [00:39<00:04, 8891.86it/s] 89%|████████▉ | 356861/400000 [00:39<00:04, 8903.01it/s] 89%|████████▉ | 357752/400000 [00:39<00:04, 8604.64it/s] 90%|████████▉ | 358643/400000 [00:39<00:04, 8693.84it/s] 90%|████████▉ | 359515/400000 [00:39<00:04, 8568.02it/s] 90%|█████████ | 360374/400000 [00:39<00:04, 8388.95it/s] 90%|█████████ | 361267/400000 [00:39<00:04, 8542.71it/s] 91%|█████████ | 362129/400000 [00:40<00:04, 8562.34it/s] 91%|█████████ | 363053/400000 [00:40<00:04, 8752.45it/s] 91%|█████████ | 363968/400000 [00:40<00:04, 8866.73it/s] 91%|█████████ | 364857/400000 [00:40<00:03, 8798.76it/s] 91%|█████████▏| 365758/400000 [00:40<00:03, 8859.20it/s] 92%|█████████▏| 366646/400000 [00:40<00:03, 8739.06it/s] 92%|█████████▏| 367531/400000 [00:40<00:03, 8769.09it/s] 92%|█████████▏| 368438/400000 [00:40<00:03, 8854.78it/s] 92%|█████████▏| 369325/400000 [00:40<00:03, 8764.90it/s] 93%|█████████▎| 370205/400000 [00:40<00:03, 8774.13it/s] 93%|█████████▎| 371108/400000 [00:41<00:03, 8848.66it/s] 93%|█████████▎| 372013/400000 [00:41<00:03, 8905.52it/s] 93%|█████████▎| 372905/400000 [00:41<00:03, 8833.65it/s] 93%|█████████▎| 373789/400000 [00:41<00:03, 8598.89it/s] 94%|█████████▎| 374651/400000 [00:41<00:03, 8423.44it/s] 94%|█████████▍| 375520/400000 [00:41<00:02, 8499.89it/s] 94%|█████████▍| 376466/400000 [00:41<00:02, 8765.65it/s] 94%|█████████▍| 377436/400000 [00:41<00:02, 9024.21it/s] 95%|█████████▍| 378424/400000 [00:41<00:02, 9264.07it/s] 95%|█████████▍| 379444/400000 [00:41<00:02, 9523.92it/s] 95%|█████████▌| 380442/400000 [00:42<00:02, 9655.56it/s] 95%|█████████▌| 381412/400000 [00:42<00:01, 9582.82it/s] 96%|█████████▌| 382374/400000 [00:42<00:01, 9050.57it/s] 96%|█████████▌| 383288/400000 [00:42<00:01, 8728.73it/s] 96%|█████████▌| 384170/400000 [00:42<00:01, 8459.96it/s] 96%|█████████▋| 385057/400000 [00:42<00:01, 8577.04it/s] 96%|█████████▋| 385921/400000 [00:42<00:01, 8196.43it/s] 97%|█████████▋| 386798/400000 [00:42<00:01, 8358.36it/s] 97%|█████████▋| 387683/400000 [00:42<00:01, 8498.18it/s] 97%|█████████▋| 388613/400000 [00:43<00:01, 8721.62it/s] 97%|█████████▋| 389510/400000 [00:43<00:01, 8792.76it/s] 98%|█████████▊| 390393/400000 [00:43<00:01, 8629.63it/s] 98%|█████████▊| 391313/400000 [00:43<00:00, 8790.71it/s] 98%|█████████▊| 392218/400000 [00:43<00:00, 8864.24it/s] 98%|█████████▊| 393163/400000 [00:43<00:00, 9029.66it/s] 99%|█████████▊| 394104/400000 [00:43<00:00, 9140.06it/s] 99%|█████████▉| 395054/400000 [00:43<00:00, 9243.23it/s] 99%|█████████▉| 396049/400000 [00:43<00:00, 9441.55it/s] 99%|█████████▉| 396996/400000 [00:43<00:00, 9352.16it/s] 99%|█████████▉| 397933/400000 [00:44<00:00, 9337.94it/s]100%|█████████▉| 398911/400000 [00:44<00:00, 9464.03it/s]100%|█████████▉| 399859/400000 [00:44<00:00, 9430.05it/s]100%|█████████▉| 399999/400000 [00:44<00:00, 9037.13it/s]>>>model:  <mlmodels.model_tch.textcnn.Model object at 0x7fb77967ab70> <class 'mlmodels.model_tch.textcnn.Model'>
Spliting original file to train/valid set...
Preprocessing the text...
Creating tabular datasets...It might take a while to finish!
Building vocaulary...
Train Epoch: 1 	 Loss: 0.011147055162039609 	 Accuracy: 49
Train Epoch: 1 	 Loss: 0.01096027531352729 	 Accuracy: 73

  model saves at 73% accuracy 

  #### Inference Need return ypred, ytrue ######################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 1, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64, 'train': False}
Spliting original file to train/valid set...
Preprocessing the text...
Creating tabular datasets...It might take a while to finish!
Building vocaulary...

  ### Calculate Metrics    ######################################## 

  {'hypermodel_pars': {}, 'data_pars': {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64, 'train': False}, 'model_pars': {'model_uri': 'model_tch.textcnn.py', 'dim_channel': 100, 'kernel_height': [3, 4, 5], 'dropout_rate': 0.5, 'num_class': 2}, 'compute_pars': {'learning_rate': 0.001, 'epochs': 1, 'checkpointdir': './output/text_cnn_tch/checkpoint/'}, 'out_pars': {'path': './output/text_cnn_tch/model.h5', 'checkpointdir': './output/text_cnn_tch/checkpoint/'}} module 'sklearn.metrics' has no attribute 'accuracy, f1_score' 

  


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
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 140, in benchmark_run
    metric_val = metric_eval(actual=ytrue, pred=ypred,  metric_name=metric)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 60, in metric_eval
    metric = getattr(importlib.import_module("sklearn.metrics"), metric_name)
AttributeError: module 'sklearn.metrics' has no attribute 'accuracy, f1_score'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py", line 120, in benchmark_run
    model     = module.Model(model_pars, data_pars, compute_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/matchzoo_models.py", line 241, in __init__
    mpars =json_norm(model_pars['model_pars'])
KeyError: 'model_pars'
python /home/runner/work/mlmodels/mlmodels/mlmodels/benchmark.py --do nlp_reuters 
