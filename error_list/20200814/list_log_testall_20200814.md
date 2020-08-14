## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py


### Error 1, [Traceback at line 37](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L37)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
<br />    from mlmodels.mode_tf.raw  import temporal_fusion_google
<br />ModuleNotFoundError: No module named 'mlmodels.mode_tf'



### Error 2, [Traceback at line 158](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L158)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1365, in _do_call
<br />    return fn(*args)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1350, in _run_fn
<br />    target_list, run_metadata)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1443, in _call_tf_sessionrun
<br />    run_metadata)
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key Variable not found in checkpoint
<br />	 [[{{node save_1/RestoreV2}}]]
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 3, [Traceback at line 170](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L170)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1290, in restore
<br />    {self.saver_def.filename_tensor_name: save_path})
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 956, in run
<br />    run_metadata_ptr)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1180, in _run
<br />    feed_dict_tensor, options, run_metadata)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1359, in _do_run
<br />    run_metadata)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1384, in _do_call
<br />    raise type(e)(node_def, op, message)
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key Variable not found in checkpoint
<br />	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]
<br />
<br />Original stack trace for 'save_1/RestoreV2':
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
<br />    test(data_path="", pars_choice="test01", config_mode="test")
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
<br />    session = load(out_pars)
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
<br />    return load_tf(load_pars)
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 474, in load_tf
<br />    saver      = tf.compat.v1.train.Saver()
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 828, in __init__
<br />    self.build()
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 840, in build
<br />    self._build(self._filename, build_save=True, build_restore=True)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 878, in _build
<br />    build_restore=build_restore)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 508, in _build_internal
<br />    restore_sequentially, reshape)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 328, in _AddRestoreOps
<br />    restore_sequentially)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 575, in bulk_restore
<br />    return io_ops.restore_v2(filename_tensor, names, slices, dtypes)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/gen_io_ops.py", line 1696, in restore_v2
<br />    name=name)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/op_def_library.py", line 794, in _apply_op_helper
<br />    op_def=op_def)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/util/deprecation.py", line 507, in new_func
<br />    return func(*args, **kwargs)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3357, in create_op
<br />    attrs, op_def, compute_device)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3426, in _create_op_internal
<br />    op_def=op_def)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 1748, in __init__
<br />    self._traceback = tf_stack.extract_stack()
<br />
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 4, [Traceback at line 221](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L221)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1300, in restore
<br />    names_to_keys = object_graph_key_mapping(save_path)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1618, in object_graph_key_mapping
<br />    object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 915, in get_tensor
<br />    return CheckpointReader_GetTensor(self, compat.as_bytes(tensor_str))
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key _CHECKPOINTABLE_OBJECT_GRAPH not found in checkpoint
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 5, [Traceback at line 232](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-08-13_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L232)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
<br />    test(data_path="", pars_choice="test01", config_mode="test")
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
<br />    session = load(out_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
<br />    return load_tf(load_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 477, in load_tf
<br />    saver.restore(sess,  full_name)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1306, in restore
<br />    err, "a Variable name or other graph key that is missing")
<br />tensorflow.python.framework.errors_impl.NotFoundError: Restoring from checkpoint failed. This is most likely due to a Variable name or other graph key that is missing from the checkpoint. Please ensure that you have not altered the graph expected based on the checkpoint. Original error:
<br />
<br />Key Variable not found in checkpoint
<br />	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]
<br />
<br />Original stack trace for 'save_1/RestoreV2':
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
<br />    test(data_path="", pars_choice="test01", config_mode="test")
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
<br />    session = load(out_pars)
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
<br />    return load_tf(load_pars)
<br />  File "home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 474, in load_tf
<br />    saver      = tf.compat.v1.train.Saver()
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 828, in __init__
<br />    self.build()
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 840, in build
<br />    self._build(self._filename, build_save=True, build_restore=True)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 878, in _build
<br />    build_restore=build_restore)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 508, in _build_internal
<br />    restore_sequentially, reshape)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 328, in _AddRestoreOps
<br />    restore_sequentially)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 575, in bulk_restore
<br />    return io_ops.restore_v2(filename_tensor, names, slices, dtypes)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/gen_io_ops.py", line 1696, in restore_v2
<br />    name=name)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/op_def_library.py", line 794, in _apply_op_helper
<br />    op_def=op_def)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/util/deprecation.py", line 507, in new_func
<br />    return func(*args, **kwargs)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3357, in create_op
<br />    attrs, op_def, compute_device)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3426, in _create_op_internal
<br />    op_def=op_def)
<br />  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 1748, in __init__
<br />    self._traceback = tf_stack.extract_stack()
<br />
<br />
<br />   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
<br />Fetching origin
<br />Already up to date.
<br />Logs
<br />README.md
<br />README_actions.md
<br />create_error_file.py
<br />create_github_issues.py
<br />error_list
<br />log_benchmark
<br />log_dataloader
<br />log_import
<br />log_json
<br />log_jupyter
<br />log_pullrequest
<br />log_test_cli
<br />log_testall
<br />test_jupyter
<br />[master 9bcd499] ml_store
<br /> 1 file changed, 234 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   97a589f..9bcd499  master -> master
<br />
<br />
<br />
<br />
<br />
<br /> ************************************************************************************************************************
<br />
<br />  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Loading dataset   ############################################# 
<br />
<br />  #### Model init, fit   ############################################# 
<br />
<br />  #### save the trained model  ####################################### 
<br />
<br />  #### Predict   ##################################################### 
<br />[[ 7.75285326e-01  1.47016034e+00  1.03298378e+00 -8.70008223e-01
<br />   7.86556511e-01  3.69190470e-01 -1.43195745e-01  8.53282186e-01
<br />  -1.39711730e-01 -2.22414029e-01]
<br /> [ 1.22867367e+00  1.34373116e-01 -1.82420406e-01 -2.68371304e-01
<br />  -1.73963799e+00 -1.31675626e-01 -9.26871939e-01  1.01855247e+00
<br />   1.23055820e+00 -4.91125138e-01]
<br /> [ 8.95623122e-01 -2.29820588e+00 -1.95225583e-02  1.45652739e+00
<br />  -1.85064099e+00  3.16637236e-01  1.11337266e-01 -2.66412594e+00
<br />  -4.26428618e-01 -8.39988915e-01]
<br /> [ 1.17867274e+00 -5.99804531e-01 -6.94693595e-01  1.12341216e+00
<br />   1.17899425e+00  3.05267040e-01  1.33526763e-02  1.38877940e+00
<br />  -6.61344243e-01  6.21803504e-01]
<br /> [ 5.63077902e-01 -1.17598267e+00 -1.74180344e-01  1.01012718e+00
<br />   1.06796368e+00  9.20017933e-01 -1.68198840e-01 -1.95057341e-01
<br />   8.05393424e-01  4.61164100e-01]
<br /> [ 8.58774962e-01  2.29371761e+00 -1.47023709e+00 -8.30010986e-01
<br />  -6.72049816e-01 -1.01951985e+00  5.99213235e-01 -2.14653842e-01
<br />   1.02124813e+00  6.06403944e-01]
<br /> [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
<br />   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
<br />  -1.30572692e+00 -8.61316361e-01]
<br /> [ 1.01195228e+00 -1.88141087e+00  1.70018815e+00  4.97269099e-01
<br />  -9.17664624e-01  2.37332699e-01 -1.09033833e+00 -2.14444405e+00
<br />  -3.69562425e-01  6.08783659e-01]
<br /> [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
<br />   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
<br />   1.40925339e+00  9.66539250e-01]
<br /> [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
<br />  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
<br />   1.05132077e+00  6.06548400e-01]
<br /> [ 7.88018455e-01  3.01960045e-01  7.00982122e-01 -3.94689681e-01
<br />  -1.20376927e+00 -1.17181338e+00  7.55392029e-01  9.84012237e-01
<br />  -5.59681422e-01 -1.98937450e-01]
<br /> [ 7.22978007e-01  1.85535621e-01  9.15499268e-01  3.94428030e-01
<br />  -8.49830738e-01  7.25522558e-01 -1.50504326e-01  1.49588477e+00
<br />   6.75453809e-01 -4.38200267e-01]
<br /> [ 1.77547698e+00 -2.03394449e-01 -1.98837863e-01  2.42669441e-01
<br />   9.64350564e-01  2.01830179e-01 -5.45774168e-01  6.61020288e-01
<br />   1.79215821e+00 -7.00398505e-01]
<br /> [ 1.32857949e+00 -5.63236604e-01 -1.06179676e+00  2.39014596e+00
<br />  -1.68450770e+00  2.45422849e-01 -5.69148654e-01  1.15259914e+00
<br />  -2.24235772e-01  1.32247779e-01]
<br /> [ 6.91743730e-01  1.00978733e+00 -1.21333813e+00 -1.55694156e+00
<br />  -1.20257258e+00 -6.12442128e-01 -2.69836174e+00 -1.39351805e-01
<br />  -7.28537489e-01  7.22518992e-02]
<br /> [ 1.18559003e+00  8.64644065e-02  1.23289919e+00 -2.14246673e+00
<br />   1.03334100e+00 -8.30168864e-01  3.67231814e-01  4.51615951e-01
<br />   1.10417433e+00 -4.22856961e-01]
<br /> [ 9.26869810e-01  3.92334911e-01 -4.23478297e-01  4.48380651e-01
<br />  -1.09230828e+00  1.12532350e+00 -9.48439656e-01  1.04053390e-01
<br />   5.28003422e-01  1.00796648e+00]
<br /> [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
<br />  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
<br />  -4.38997664e-01  3.21265914e-01]
<br /> [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
<br />   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
<br />   7.63804802e-02 -1.87316098e+00]
<br /> [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
<br />  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
<br />  -1.14870423e+00 -9.50909251e-01]
<br /> [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
<br />   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
<br />  -2.23708651e+00 -4.14846901e-01]
<br /> [ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
<br />   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
<br />  -1.11487105e+00 -1.95210529e+00]
<br /> [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
<br />  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
<br />   1.12368489e-01 -1.78175491e-02]
<br /> [ 6.10942600e-01 -2.79099641e+00 -1.33520272e+00 -4.56117555e-01
<br />  -9.44959948e-01 -9.79890252e-01 -1.56993672e-01  6.92574348e-01
<br />  -4.78672356e-01 -1.06460122e-01]
<br /> [ 1.16777676e+00 -6.65754518e-01 -1.23312074e+00 -1.67419581e+00
<br />   1.01313574e+00  8.25029824e-01 -1.20464572e-01 -4.98213564e-01
<br />  -3.10984978e-01 -1.18231813e+00]]
<br />
<br />  #### metrics   ##################################################### 
<br />{}
<br />
<br />  #### Plot   ######################################################## 
<br />
<br />  #### Save/Load   ################################################### 
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br /><__main__.Model object at 0x7f87af45feb8>
<br />
<br />  #### Module init   ############################################ 
<br />
<br />  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Model init   ############################################ 
<br />
<br />  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f87c97e66a0> 
<br />
<br />  #### Fit   ######################################################## 
<br />
<br />  #### Predict   #################################################### 
<br />[[ 0.44118981  0.47985237 -0.1920037  -1.55269878 -1.88873982  0.57846442
<br />   0.39859839 -0.9612636  -1.45832446 -3.05376438]
<br /> [ 0.85729649  0.9561217  -0.82609743 -0.70584051  1.13872896  1.19268607
<br />   0.28267571 -0.23794194  1.15528789  0.6210827 ]
<br /> [ 1.18947778 -0.68067814 -0.05682448 -0.08450803  0.82178321 -0.29736188
<br />  -0.18657899  0.417302    0.78477065  0.49233656]
<br /> [ 1.01177337  0.09574677  0.73140252  1.0334508  -1.42203164 -0.14627327
<br />  -0.01745495 -0.85749682 -0.93418184  0.95449567]
<br /> [ 1.64661853 -1.52568032 -0.6069984   0.79502609  1.08480038 -0.37443832
<br />   0.42952614  0.1340482   1.20205486  0.10622272]
<br /> [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
<br />  -1.75592564  0.61798553 -0.18417633  0.85270406]
<br /> [ 0.68188934 -1.15498263  1.22895559 -0.1776322   0.99854519 -1.51045638
<br />  -0.27584606  1.01120706 -1.47656266  1.30970591]
<br /> [ 0.87122579 -0.20975294 -0.45698786  0.93514778 -0.87353582  1.81252782
<br />   0.92550121  0.14010988 -1.41914878  1.06898597]
<br /> [ 0.35413361  0.21112476  0.92145007  0.01652757  0.90394545  0.17718772
<br />   0.09542509 -1.11647002  0.0809271   0.0607502 ]
<br /> [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
<br />   1.10223673  0.81434313  0.78046993  1.10861676]
<br /> [ 0.79032389  1.61336137 -2.09424782 -0.37480469  0.91588404 -0.74996962
<br />   0.31027229  2.0546241   0.05340954 -0.22876583]
<br /> [ 0.9292506  -1.10657307 -1.95816909 -0.3592241  -1.21258781  0.5053819
<br />   0.54264529  1.2179409  -1.94068096  0.67780757]
<br /> [ 0.69211449 -0.06065249  2.05635552 -2.413503    1.17456965 -1.77756638
<br />  -0.28173627 -0.77785883  1.11584111  1.76024923]
<br /> [ 0.55853873 -0.51634791 -0.51814555  0.3511169   0.82550695 -0.06877046
<br />  -0.9520621  -1.34776494  1.47073986 -1.4614036 ]
<br /> [ 1.32720112 -0.16119832  0.6024509  -0.28638492 -0.5789623  -0.87088765
<br />   1.37975819  0.50142959 -0.47861407 -0.89264667]
<br /> [ 0.345716   -0.41302931 -0.46867382  1.83471763  0.77151441  0.56438286
<br />   0.02186284  2.13782807 -0.785534    0.85328122]
<br /> [ 1.39198128 -0.19022103 -0.53722302 -0.44873803  0.70455707 -0.67244804
<br />  -0.70134443 -0.55749472  0.93916874  0.15626385]
<br /> [ 1.06702918 -0.42914228  0.35016716  1.20845633  0.75148062  1.1157018
<br />  -0.4791571   0.84086156 -0.10288722  0.01716473]
<br /> [ 0.78344054 -0.05118845  0.82458463 -0.72559712  0.9317172  -0.86776868
<br />   3.03085711 -0.13597733 -0.79726979  0.65458015]
<br /> [ 1.66752297  1.22372221 -0.4599301  -0.0593679  -0.493857    1.4489894
<br />  -1.18110317 -0.47758085  0.02599999 -0.79079995]
<br /> [ 0.62368852  1.2066079   0.90399917 -0.28286355 -1.18913787 -0.26632688
<br />   1.42361443  1.06897162  0.04037143  1.57546791]
<br /> [ 0.85877496  2.29371761 -1.47023709 -0.83001099 -0.67204982 -1.01951985
<br />   0.59921324 -0.21465384  1.02124813  0.60640394]
<br /> [ 0.10593645 -0.73728963  0.65032321  0.16466507 -1.53556118  0.77817418
<br />   0.05031709  0.30981676  1.05132077  0.6065484 ]
<br /> [ 0.78801845  0.30196005  0.70098212 -0.39468968 -1.20376927 -1.17181338
<br />   0.75539203  0.98401224 -0.55968142 -0.19893745]
<br /> [ 0.88838944  0.28299553  0.01795589  0.10803082 -0.84967187  0.02941762
<br />  -0.50397395 -0.13479313  1.04921829 -1.27046078]]
<br />None
<br />
<br />  #### Get  metrics   ################################################ 
<br />
<br />  #### Save   ######################################################## 
<br />
<br />  #### Load   ######################################################## 
<br />
<br />  ############ Model preparation   ################################## 
<br />
<br />  #### Module init   ############################################ 
<br />
<br />  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Model init   ############################################ 
<br />
<br />  ############ Model fit   ########################################## 
<br />fit success None
<br />
<br />  ############ Prediction############################################ 
<br />[[ 1.39198128e+00 -1.90221025e-01 -5.37223024e-01 -4.48738033e-01
<br />   7.04557071e-01 -6.72448039e-01 -7.01344426e-01 -5.57494722e-01
<br />   9.39168744e-01  1.56263850e-01]
<br /> [ 1.13545112e+00  8.61623101e-01  4.90616924e-02 -2.08639057e+00
<br />  -1.11469020e+00  3.61801641e-01 -8.06178212e-01  4.25920177e-01
<br />   4.90803971e-02 -5.96086335e-01]
<br /> [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
<br />   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
<br />  -1.30572692e+00 -8.61316361e-01]
<br /> [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
<br />  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
<br />   9.49808815e-01 -8.80189065e-01]
<br /> [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
<br />  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
<br />   7.80469930e-01  1.10861676e+00]
<br /> [ 8.57296491e-01  9.56121704e-01 -8.26097432e-01 -7.05840507e-01
<br />   1.13872896e+00  1.19268607e+00  2.82675712e-01 -2.37941936e-01
<br />   1.15528789e+00  6.21082701e-01]
<br /> [ 3.45715997e-01 -4.13029310e-01 -4.68673816e-01  1.83471763e+00
<br />   7.71514409e-01  5.64382855e-01  2.18628366e-02  2.13782807e+00
<br />  -7.85533997e-01  8.53281222e-01]
<br /> [ 8.98917161e-01  5.57439453e-01 -7.58067329e-01  1.81038744e-01
<br />   8.41467206e-01  1.10717545e+00  6.93366226e-01  1.44287693e+00
<br />  -5.39681562e-01 -8.08847196e-01]
<br /> [ 7.00175710e-01  5.56073510e-01  8.96864073e-02  1.69380911e+00
<br />   8.82393314e-01  1.96869779e-01 -5.63788735e-01  1.69869255e-01
<br />  -1.16400797e+00 -6.01156801e-01]
<br /> [ 1.12641981e+00 -6.29441604e-01  1.10100020e+00 -1.11343610e+00
<br />   9.44595066e-01 -6.74100249e-02 -1.83400197e-01  1.16143998e+00
<br />  -2.75293863e-02  7.80027135e-01]
<br /> [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
<br />   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
<br />   7.84770651e-01  4.92336556e-01]
<br /> [ 7.83440538e-01 -5.11884476e-02  8.24584625e-01 -7.25597119e-01
<br />   9.31717197e-01 -8.67768678e-01  3.03085711e+00 -1.35977326e-01
<br />  -7.97269785e-01  6.54580153e-01]
<br /> [ 8.58774962e-01  2.29371761e+00 -1.47023709e+00 -8.30010986e-01
<br />  -6.72049816e-01 -1.01951985e+00  5.99213235e-01 -2.14653842e-01
<br />   1.02124813e+00  6.06403944e-01]
<br /> [ 7.75285326e-01  1.47016034e+00  1.03298378e+00 -8.70008223e-01
<br />   7.86556511e-01  3.69190470e-01 -1.43195745e-01  8.53282186e-01
<br />  -1.39711730e-01 -2.22414029e-01]
<br /> [ 1.58463774e+00  5.71209961e-02 -1.77183179e-02 -7.99547491e-01
<br />   1.32970299e+00 -2.91594596e-01 -1.10771250e+00 -2.58982853e-01
<br />   1.89293198e-01 -1.71939447e+00]
<br /> [ 1.24549398e+00 -7.22391905e-01  1.11813340e+00  1.09899633e+00
<br />   1.00277655e+00 -9.01634490e-01 -5.32234021e-01 -8.22467189e-01
<br />   7.21711292e-01  6.74396105e-01]
<br /> [ 8.71225789e-01 -2.09752935e-01 -4.56987858e-01  9.35147780e-01
<br />  -8.73535822e-01  1.81252782e+00  9.25501215e-01  1.40109881e-01
<br />  -1.41914878e+00  1.06898597e+00]
<br /> [ 1.46893146e+00 -1.47115693e+00  5.85910431e-01 -8.30171895e-01
<br />   1.03345052e+00 -8.80577600e-01 -9.55425262e-01 -2.79097722e-01
<br />   1.62284909e+00  2.06578332e+00]
<br /> [ 1.32720112e+00 -1.61198320e-01  6.02450901e-01 -2.86384915e-01
<br />  -5.78962302e-01 -8.70887650e-01  1.37975819e+00  5.01429590e-01
<br />  -4.78614074e-01 -8.92646674e-01]
<br /> [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
<br />  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
<br />  -9.34181843e-01  9.54495667e-01]
<br /> [ 1.27991386e+00 -8.71422066e-01 -3.24032329e-01 -8.64829941e-01
<br />  -9.68539694e-01  6.08749082e-01  5.07984337e-01  5.61638097e-01
<br />   1.51475038e+00 -1.51107661e+00]
<br /> [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
<br />   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
<br />   7.63804802e-02 -1.87316098e+00]
<br /> [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
<br />  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
<br />  -1.05354607e+00  7.85226920e-01]
<br /> [ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
<br />   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
<br />  -1.11487105e+00 -1.95210529e+00]
<br /> [ 4.67397905e-01 -2.37875265e-01 -1.54491194e-01 -7.55662765e-01
<br />  -5.47062239e-01  1.85143789e+00 -1.46405357e+00  2.09096677e-01
<br />   1.55501599e+00 -9.24323185e-02]]
<br />None
<br />
<br />  ############ Save/ Load ############################################ 
<br />
<br />   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
<br />Fetching origin
<br />Already up to date.
<br />Logs
<br />README.md
<br />README_actions.md
<br />create_error_file.py
<br />create_github_issues.py
<br />error_list
<br />log_benchmark
<br />log_dataloader
<br />log_import
<br />log_json
<br />log_jupyter
<br />log_pullrequest
<br />log_test_cli
<br />log_testall
<br />test_jupyter
<br />[master c94f662] ml_store
<br /> 1 file changed, 296 insertions(+)
<br />Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
<br />To github.com:arita37/mlmodels_store.git
<br />   9bcd499..c94f662  master -> master
<br />
<br />
<br />
<br />
<br />
<br /> ************************************************************************************************************************
<br />
<br />  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_sklearn.py 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Loading dataset   ############################################# 
<br />
<br />  #### Model init, fit   ############################################# 
<br />
<br />  #### save the trained model  ####################################### 
<br />
<br />  #### Predict   ##################################################### 
<br />
<br />  #### metrics   ##################################################### 
<br />{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}
<br />{'roc_auc_score': 1.0}
<br />
<br />  #### Plot   ######################################################## 
<br />
<br />  #### Save/Load   ################################################### 
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_sklearn/model.pkl'}
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_sklearn/model.pkl'}
<br />RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
<br />                       max_depth=4, max_features='auto', max_leaf_nodes=None,
<br />                       min_impurity_decrease=0.0, min_impurity_split=None,
<br />                       min_samples_leaf=1, min_samples_split=2,
<br />                       min_weight_fraction_leaf=0.0, n_estimators=10,
<br />                       n_jobs=None, oob_score=False, random_state=0, verbose=0,
<br />                       warm_start=False)
<br />{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}
<br />{'roc_auc_score': 1.0}
<br />
<br />  #### Module init   ############################################ 
<br />
<br />  <module 'mlmodels.model_sklearn.model_sklearn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_sklearn.py'> 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Model init   ############################################ 
<br />
<br />  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f0139707978> 
<br />
<br />  #### Fit   ######################################################## 
<br />
<br />  #### Predict   #################################################### 
<br />None
<br />
<br />  #### Get  metrics   ################################################ 
<br />{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}
<br />
<br />  #### Save   ######################################################## 
<br />
<br />  #### Load   ######################################################## 
<br />
<br />  ############ Model preparation   ################################## 
<br />
<br />  #### Module init   ############################################ 
<br />
<br />  <module 'mlmodels.model_sklearn.model_sklearn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_sklearn.py'> 
<br />
<br />  #### Loading params   ############################################## 
<br />
<br />  #### Path params   ########################################## 
<br />
<br />  #### Model init   ############################################ 
<br />
<br />  ############ Model fit   ########################################## 
<br />fit success None
<br />
<br />  ############ Prediction############################################ 
<br />None
<br />
<br />  ############ Save/ Load ############################################ 
<br />/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/sklearn/ensemble/forest.py:245: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.
<br />  "10 in version 0.20 to 100 in 0.22.", FutureWarning)
<br />
<br />   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
<br />Fetching origin
<br />Already up to date.
<br />Logs
<br />README.md
<br />README_actions.md
<br />create_error_file.py
<br />create_github_issues.py
<br />error_list
<br />log_benchmark
<br />log_dataloader
<br />log_import
<br />log_json
<br />log_jupyter
<br />log_pullrequest
<br />log_test_cli
<br />log_testall
<br />test_jupyter
<br />[master 5916e91] ml_store
<br /> 1 file changed, 109 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   c94f662..5916e91  master -> master
<br />
<br />
<br />
<br />
<br />
<br /> ************************************************************************************************************************
<br />
<br />  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//pplm.py 
<br /> Generating text ... 
<br />= Prefix of sentence =
<br /><|endoftext|>The potato
<br />
<br /> Unperturbed generated text :
<br />
<br /><|endoftext|>The potato-shaped, potato-eating insect of modern times (Ophiocordyceps elegans) has a unique ability to adapt quickly to a wide range of environments. It is able to survive in many different environments, including the Arctic, deserts
<br />
<br /> Perturbed generated text :
<br />
<br /><|endoftext|>The potato bomb is nothing new. It's been on the news a lot since 9/11. In fact, since the bombing in Paris last November, a bomb has been detonated in every major European country in the European Union.
<br />
<br />The bomb in Brussels
<br />
<br />
<br />   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
<br />Fetching origin
<br />Already up to date.
<br />Logs
<br />README.md
<br />README_actions.md
<br />create_error_file.py
<br />create_github_issues.py
<br />error_list
<br />log_benchmark
<br />log_dataloader
<br />log_import
<br />log_json
<br />log_jupyter
<br />log_pullrequest
<br />log_test_cli
<br />log_testall
<br />test_jupyter
