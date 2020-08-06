## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py


### Error 1, [Traceback at line 37](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L37)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
<br />    from mlmodels.mode_tf.raw  import temporal_fusion_google
<br />ModuleNotFoundError: No module named 'mlmodels.mode_tf'



### Error 2, [Traceback at line 160](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L160)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1365, in _do_call
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



### Error 3, [Traceback at line 172](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L172)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1290, in restore
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



### Error 4, [Traceback at line 223](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L223)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1300, in restore
<br />    names_to_keys = object_graph_key_mapping(save_path)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1618, in object_graph_key_mapping
<br />    object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 915, in get_tensor
<br />    return CheckpointReader_GetTensor(self, compat.as_bytes(tensor_str))
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key _CHECKPOINTABLE_OBJECT_GRAPH not found in checkpoint
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 5, [Traceback at line 234](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-00-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L234)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
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
<br />[master f3c75e0] ml_store
<br /> 1 file changed, 234 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   071195f..f3c75e0  master -> master
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
<br />[[ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
<br />   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
<br />  -1.11487105e+00 -1.95210529e+00]
<br /> [ 6.13636707e-01  3.16658895e-01  1.34710546e+00 -1.89526695e+00
<br />  -7.60458095e-01  8.97291174e-02 -3.29051549e-01  4.10265745e-01
<br />   8.59870972e-01 -1.04906775e+00]
<br /> [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
<br />  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
<br />  -4.38997664e-01  3.21265914e-01]
<br /> [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
<br />   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
<br />   4.95158611e-01  6.61681076e-01]
<br /> [ 1.14377130e+00  7.27813500e-01  3.52494364e-01  5.15073614e-01
<br />   1.17718111e+00 -2.78253447e+00 -1.94332341e+00  5.84646610e-01
<br />   3.24274243e-01 -2.36436952e-01]
<br /> [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
<br />  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
<br />  -1.05354607e+00  7.85226920e-01]
<br /> [ 1.24549398e+00 -7.22391905e-01  1.11813340e+00  1.09899633e+00
<br />   1.00277655e+00 -9.01634490e-01 -5.32234021e-01 -8.22467189e-01
<br />   7.21711292e-01  6.74396105e-01]
<br /> [ 1.06040861e+00  5.10307597e-01  5.01725109e-01 -9.15791849e-01
<br />  -9.07318361e-01 -4.07252043e-01 -1.79612295e-01  9.84951672e-01
<br />   1.07125243e+00 -5.93343754e-01]
<br /> [ 1.36586461e+00  3.95860270e+00  5.48129585e-01  6.48643644e-01
<br />   8.49176066e-01  1.07343294e-01  1.38631426e+00 -1.39881282e+00
<br />   8.17678188e-02 -1.63744959e+00]
<br /> [ 7.83440538e-01 -5.11884476e-02  8.24584625e-01 -7.25597119e-01
<br />   9.31717197e-01 -8.67768678e-01  3.03085711e+00 -1.35977326e-01
<br />  -7.97269785e-01  6.54580153e-01]
<br /> [ 1.07258847e+00 -5.86523939e-01 -1.34267579e+00 -1.23685338e+00
<br />   1.24328724e+00  8.75838928e-01 -3.26499498e-01  6.23362177e-01
<br />  -4.34956683e-01  1.11438298e+00]
<br /> [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
<br />  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
<br />  -8.32395348e-01 -4.46699203e-01]
<br /> [ 8.76994650e-01  1.23225307e+00 -8.67787223e-01 -2.54179868e-01
<br />   8.91891405e-01  1.39984394e+00 -8.77281519e-01 -7.81911683e-01
<br />  -4.37508983e-01 -1.44087602e+00]
<br /> [ 1.14809657e+00 -7.33271604e-01  2.62467445e-01  8.36004719e-01
<br />   1.17353145e+00  1.54335911e+00  2.84748111e-01  7.58805660e-01
<br />   8.84908814e-01  2.76499305e-01]
<br /> [ 1.77547698e+00 -2.03394449e-01 -1.98837863e-01  2.42669441e-01
<br />   9.64350564e-01  2.01830179e-01 -5.45774168e-01  6.61020288e-01
<br />   1.79215821e+00 -7.00398505e-01]
<br /> [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
<br />  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
<br />  -1.14870423e+00 -9.50909251e-01]
<br /> [ 1.25704434e+00 -1.82391985e+00 -6.12406973e-01  1.16707517e+00
<br />  -6.23732812e-01 -3.96687001e-02  8.16043684e-01  8.85825799e-01
<br />   1.89861649e-01  3.93109245e-01]
<br /> [ 6.91743730e-01  1.00978733e+00 -1.21333813e+00 -1.55694156e+00
<br />  -1.20257258e+00 -6.12442128e-01 -2.69836174e+00 -1.39351805e-01
<br />  -7.28537489e-01  7.22518992e-02]
<br /> [ 1.58463774e+00  5.71209961e-02 -1.77183179e-02 -7.99547491e-01
<br />   1.32970299e+00 -2.91594596e-01 -1.10771250e+00 -2.58982853e-01
<br />   1.89293198e-01 -1.71939447e+00]
<br /> [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
<br />  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
<br />   7.80469930e-01  1.10861676e+00]
<br /> [ 1.16777676e+00 -6.65754518e-01 -1.23312074e+00 -1.67419581e+00
<br />   1.01313574e+00  8.25029824e-01 -1.20464572e-01 -4.98213564e-01
<br />  -3.10984978e-01 -1.18231813e+00]
<br /> [ 8.95623122e-01 -2.29820588e+00 -1.95225583e-02  1.45652739e+00
<br />  -1.85064099e+00  3.16637236e-01  1.11337266e-01 -2.66412594e+00
<br />  -4.26428618e-01 -8.39988915e-01]
<br /> [ 7.75285326e-01  1.47016034e+00  1.03298378e+00 -8.70008223e-01
<br />   7.86556511e-01  3.69190470e-01 -1.43195745e-01  8.53282186e-01
<br />  -1.39711730e-01 -2.22414029e-01]
<br /> [ 1.03967316e+00 -7.31530982e-01  3.61847316e-01 -1.56573815e+00
<br />   9.59288190e-01  1.01382247e+00 -1.78791289e+00 -2.22711263e+00
<br />  -1.69933360e+00 -4.24492791e-01]
<br /> [ 6.81889336e-01 -1.15498263e+00  1.22895559e+00 -1.77632196e-01
<br />   9.98545187e-01 -1.51045638e+00 -2.75846063e-01  1.01120706e+00
<br />  -1.47656266e+00  1.30970591e+00]]
<br />
<br />  #### metrics   ##################################################### 
<br />{}
<br />
<br />  #### Plot   ######################################################## 
<br />
<br />  #### Save/Load   ################################################### 
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br /><__main__.Model object at 0x7f2039f90eb8>
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
<br />  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f2039f90f28> 
<br />
<br />  #### Fit   ######################################################## 
<br />
<br />  #### Predict   #################################################### 
<br />[[ 1.18559003e+00  8.64644065e-02  1.23289919e+00 -2.14246673e+00
<br />   1.03334100e+00 -8.30168864e-01  3.67231814e-01  4.51615951e-01
<br />   1.10417433e+00 -4.22856961e-01]
<br /> [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
<br />   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
<br />   4.95158611e-01  6.61681076e-01]
<br /> [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
<br />  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
<br />   9.49808815e-01 -8.80189065e-01]
<br /> [ 6.81889336e-01 -1.15498263e+00  1.22895559e+00 -1.77632196e-01
<br />   9.98545187e-01 -1.51045638e+00 -2.75846063e-01  1.01120706e+00
<br />  -1.47656266e+00  1.30970591e+00]
<br /> [ 1.36586461e+00  3.95860270e+00  5.48129585e-01  6.48643644e-01
<br />   8.49176066e-01  1.07343294e-01  1.38631426e+00 -1.39881282e+00
<br />   8.17678188e-02 -1.63744959e+00]
<br /> [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
<br />  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
<br />  -8.32395348e-01 -4.46699203e-01]
<br /> [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
<br />  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
<br />  -4.38997664e-01  3.21265914e-01]
<br /> [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
<br />  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
<br />   1.05132077e+00  6.06548400e-01]
<br /> [ 7.75285326e-01  1.47016034e+00  1.03298378e+00 -8.70008223e-01
<br />   7.86556511e-01  3.69190470e-01 -1.43195745e-01  8.53282186e-01
<br />  -1.39711730e-01 -2.22414029e-01]
<br /> [ 9.26869810e-01  3.92334911e-01 -4.23478297e-01  4.48380651e-01
<br />  -1.09230828e+00  1.12532350e+00 -9.48439656e-01  1.04053390e-01
<br />   5.28003422e-01  1.00796648e+00]
<br /> [ 7.90323893e-01  1.61336137e+00 -2.09424782e+00 -3.74804687e-01
<br />   9.15884042e-01 -7.49969617e-01  3.10272288e-01  2.05462410e+00
<br />   5.34095368e-02 -2.28765829e-01]
<br /> [ 9.80427414e-01  1.93752881e+00 -2.30839743e-01  3.66332015e-01
<br />   1.10018476e+00 -1.04458938e+00 -3.44987210e-01  2.05117344e+00
<br />   5.85662000e-01 -2.79308500e+00]
<br /> [ 4.41189807e-01  4.79852371e-01 -1.92003697e-01 -1.55269878e+00
<br />  -1.88873982e+00  5.78464420e-01  3.98598388e-01 -9.61263599e-01
<br />  -1.45832446e+00 -3.05376438e+00]
<br /> [ 7.88018455e-01  3.01960045e-01  7.00982122e-01 -3.94689681e-01
<br />  -1.20376927e+00 -1.17181338e+00  7.55392029e-01  9.84012237e-01
<br />  -5.59681422e-01 -1.98937450e-01]
<br /> [ 8.76994650e-01  1.23225307e+00 -8.67787223e-01 -2.54179868e-01
<br />   8.91891405e-01  1.39984394e+00 -8.77281519e-01 -7.81911683e-01
<br />  -4.37508983e-01 -1.44087602e+00]
<br /> [ 8.15836116e-01 -1.39169388e+00  2.50598029e+00  4.50217742e-01
<br />  -8.82869820e-01  6.27437083e-01 -1.19586151e+00  7.51337235e-01
<br />   1.40395436e-01  1.91979229e+00]
<br /> [ 8.61462558e-01  7.43205537e-02 -1.34501002e+00 -1.99560718e-01
<br />  -1.47533915e+00 -6.54603169e-01 -3.14563862e-01  3.18014296e-01
<br />  -8.90271552e-01 -1.29525789e+00]
<br /> [ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
<br />   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
<br />  -1.11487105e+00 -1.95210529e+00]
<br /> [ 1.09488485e+00 -6.96245395e-02 -1.16444148e-01  3.53870427e-01
<br />  -1.44189096e+00 -1.86955017e-01  1.29118890e+00 -1.53236162e-01
<br />  -2.43250851e+00 -2.27729800e+00]
<br /> [ 7.73703613e-01  1.27852808e+00 -2.11416392e+00 -4.42229280e-01
<br />   1.06821044e+00  3.23527354e-01 -2.50644065e+00 -1.09991490e-01
<br />   8.54894544e-03 -4.11639163e-01]
<br /> [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
<br />   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
<br />  -2.23708651e+00 -4.14846901e-01]
<br /> [ 1.66752297e+00  1.22372221e+00 -4.59930104e-01 -5.93679025e-02
<br />  -4.93856997e-01  1.44898940e+00 -1.18110317e+00 -4.77580855e-01
<br />   2.59999942e-02 -7.90799954e-01]
<br /> [ 8.59823751e-01  1.71957132e-01 -3.48984191e-01  4.90561044e-01
<br />  -1.15649503e+00 -1.39528303e+00  6.14726276e-01 -5.22356465e-01
<br />  -3.69255902e-01 -9.77773002e-01]
<br /> [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
<br />  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
<br />  -1.14870423e+00 -9.50909251e-01]
<br /> [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
<br />  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
<br />  -9.34181843e-01  9.54495667e-01]]
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
<br />[[ 6.25673373e-01  5.92472801e-01  6.74570707e-01  1.19783084e+00
<br />   1.23187251e+00  1.70459417e+00 -7.67309826e-01  1.04008915e+00
<br />  -9.18440038e-01  1.46089238e+00]
<br /> [ 6.21530991e-01 -1.50957268e+00 -1.01932039e-01 -1.08071069e+00
<br />  -1.13742855e+00  7.25474004e-01  7.98063795e-01 -3.91782562e-02
<br />  -2.28754171e-01  7.43356544e-01]
<br /> [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
<br />  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
<br />  -9.34181843e-01  9.54495667e-01]
<br /> [ 3.54133613e-01  2.11124755e-01  9.21450069e-01  1.65275673e-02
<br />   9.03945451e-01  1.77187720e-01  9.54250872e-02 -1.11647002e+00
<br />   8.09271010e-02  6.07501958e-02]
<br /> [ 1.66752297e+00  1.22372221e+00 -4.59930104e-01 -5.93679025e-02
<br />  -4.93856997e-01  1.44898940e+00 -1.18110317e+00 -4.77580855e-01
<br />   2.59999942e-02 -7.90799954e-01]
<br /> [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
<br />  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
<br />  -1.14870423e+00 -9.50909251e-01]
<br /> [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
<br />   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
<br />   7.84770651e-01  4.92336556e-01]
<br /> [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
<br />  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
<br />   1.05132077e+00  6.06548400e-01]
<br /> [ 8.71225789e-01 -2.09752935e-01 -4.56987858e-01  9.35147780e-01
<br />  -8.73535822e-01  1.81252782e+00  9.25501215e-01  1.40109881e-01
<br />  -1.41914878e+00  1.06898597e+00]
<br /> [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
<br />  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
<br />  -4.38997664e-01  3.21265914e-01]
<br /> [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
<br />  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
<br />   7.80469930e-01  1.10861676e+00]
<br /> [ 6.91743730e-01  1.00978733e+00 -1.21333813e+00 -1.55694156e+00
<br />  -1.20257258e+00 -6.12442128e-01 -2.69836174e+00 -1.39351805e-01
<br />  -7.28537489e-01  7.22518992e-02]
<br /> [ 1.64661853e+00 -1.52568032e+00 -6.06998398e-01  7.95026094e-01
<br />   1.08480038e+00 -3.74438319e-01  4.29526140e-01  1.34048197e-01
<br />   1.20205486e+00  1.06222724e-01]
<br /> [ 1.32857949e+00 -5.63236604e-01 -1.06179676e+00  2.39014596e+00
<br />  -1.68450770e+00  2.45422849e-01 -5.69148654e-01  1.15259914e+00
<br />  -2.24235772e-01  1.32247779e-01]
<br /> [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
<br />   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
<br />   4.95158611e-01  6.61681076e-01]
<br /> [ 1.46893146e+00 -1.47115693e+00  5.85910431e-01 -8.30171895e-01
<br />   1.03345052e+00 -8.80577600e-01 -9.55425262e-01 -2.79097722e-01
<br />   1.62284909e+00  2.06578332e+00]
<br /> [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
<br />   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
<br />  -2.23708651e+00 -4.14846901e-01]
<br /> [ 1.03967316e+00 -7.31530982e-01  3.61847316e-01 -1.56573815e+00
<br />   9.59288190e-01  1.01382247e+00 -1.78791289e+00 -2.22711263e+00
<br />  -1.69933360e+00 -4.24492791e-01]
<br /> [ 8.59823751e-01  1.71957132e-01 -3.48984191e-01  4.90561044e-01
<br />  -1.15649503e+00 -1.39528303e+00  6.14726276e-01 -5.22356465e-01
<br />  -3.69255902e-01 -9.77773002e-01]
<br /> [ 1.12641981e+00 -6.29441604e-01  1.10100020e+00 -1.11343610e+00
<br />   9.44595066e-01 -6.74100249e-02 -1.83400197e-01  1.16143998e+00
<br />  -2.75293863e-02  7.80027135e-01]
<br /> [ 4.73307772e-01 -9.73267585e-01 -2.28140691e-01  1.75167729e-01
<br />  -1.01366961e+00 -5.34836927e-02  3.93787731e-01 -1.83061987e-01
<br />  -2.21028902e-01  5.80330113e-01]
<br /> [ 1.06702918e+00 -4.29142278e-01  3.50167159e-01  1.20845633e+00
<br />   7.51480619e-01  1.11570180e+00 -4.79157099e-01  8.40861558e-01
<br />  -1.02887218e-01  1.71647264e-02]
<br /> [ 1.27991386e+00 -8.71422066e-01 -3.24032329e-01 -8.64829941e-01
<br />  -9.68539694e-01  6.08749082e-01  5.07984337e-01  5.61638097e-01
<br />   1.51475038e+00 -1.51107661e+00]
<br /> [ 1.18559003e+00  8.64644065e-02  1.23289919e+00 -2.14246673e+00
<br />   1.03334100e+00 -8.30168864e-01  3.67231814e-01  4.51615951e-01
<br />   1.10417433e+00 -4.22856961e-01]
<br /> [ 8.57719529e-01  9.81122462e-02 -2.60466059e-01  1.06032751e+00
<br />  -1.39003042e+00 -1.71116766e+00  2.65642403e-01  1.65712464e+00
<br />   1.41767401e+00  4.45096710e-01]]
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
<br />[master 2e90a74] ml_store
<br /> 1 file changed, 321 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   f3c75e0..2e90a74  master -> master
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
<br />  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7fed701d3978> 
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
<br />[master ab0fa84] ml_store
<br /> 1 file changed, 108 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   2e90a74..ab0fa84  master -> master
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
