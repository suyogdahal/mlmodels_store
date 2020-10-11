## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py


### Error 1, [Traceback at line 37](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L37)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
<br />    from mlmodels.mode_tf.raw  import temporal_fusion_google
<br />ModuleNotFoundError: No module named 'mlmodels.mode_tf'



### Error 2, [Traceback at line 158](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L158)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1365, in _do_call
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



### Error 3, [Traceback at line 170](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L170)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1290, in restore
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



### Error 4, [Traceback at line 221](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L221)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1300, in restore
<br />    names_to_keys = object_graph_key_mapping(save_path)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1618, in object_graph_key_mapping
<br />    object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 915, in get_tensor
<br />    return CheckpointReader_GetTensor(self, compat.as_bytes(tensor_str))
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key _CHECKPOINTABLE_OBJECT_GRAPH not found in checkpoint
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 5, [Traceback at line 232](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-11-20-12_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L232)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
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
<br />[master 8596592] ml_store
<br /> 1 file changed, 234 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   ce8a702..8596592  master -> master
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
<br />[[ 5.58538729e-01 -5.16347909e-01 -5.18145552e-01  3.51116897e-01
<br />   8.25506954e-01 -6.87704631e-02 -9.52062101e-01 -1.34776494e+00
<br />   1.47073986e+00 -1.46140360e+00]
<br /> [ 6.91743730e-01  1.00978733e+00 -1.21333813e+00 -1.55694156e+00
<br />  -1.20257258e+00 -6.12442128e-01 -2.69836174e+00 -1.39351805e-01
<br />  -7.28537489e-01  7.22518992e-02]
<br /> [ 8.57719529e-01  9.81122462e-02 -2.60466059e-01  1.06032751e+00
<br />  -1.39003042e+00 -1.71116766e+00  2.65642403e-01  1.65712464e+00
<br />   1.41767401e+00  4.45096710e-01]
<br /> [ 7.22978007e-01  1.85535621e-01  9.15499268e-01  3.94428030e-01
<br />  -8.49830738e-01  7.25522558e-01 -1.50504326e-01  1.49588477e+00
<br />   6.75453809e-01 -4.38200267e-01]
<br /> [ 1.18559003e+00  8.64644065e-02  1.23289919e+00 -2.14246673e+00
<br />   1.03334100e+00 -8.30168864e-01  3.67231814e-01  4.51615951e-01
<br />   1.10417433e+00 -4.22856961e-01]
<br /> [ 8.95623122e-01 -2.29820588e+00 -1.95225583e-02  1.45652739e+00
<br />  -1.85064099e+00  3.16637236e-01  1.11337266e-01 -2.66412594e+00
<br />  -4.26428618e-01 -8.39988915e-01]
<br /> [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
<br />  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
<br />  -8.32395348e-01 -4.46699203e-01]
<br /> [ 9.29250600e-01 -1.10657307e+00 -1.95816909e+00 -3.59224096e-01
<br />  -1.21258781e+00  5.05381903e-01  5.42645295e-01  1.21794090e+00
<br />  -1.94068096e+00  6.77807571e-01]
<br /> [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
<br />   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
<br />   7.63804802e-02 -1.87316098e+00]
<br /> [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
<br />  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
<br />   1.05132077e+00  6.06548400e-01]
<br /> [ 1.32720112e+00 -1.61198320e-01  6.02450901e-01 -2.86384915e-01
<br />  -5.78962302e-01 -8.70887650e-01  1.37975819e+00  5.01429590e-01
<br />  -4.78614074e-01 -8.92646674e-01]
<br /> [ 7.61706684e-01 -1.48515645e+00  1.30253554e+00 -5.92461285e-01
<br />  -1.64162479e+00 -2.30490794e+00 -1.34869645e+00 -3.18171727e-02
<br />   1.12487742e-01 -3.62612088e-01]
<br /> [ 8.98917161e-01  5.57439453e-01 -7.58067329e-01  1.81038744e-01
<br />   8.41467206e-01  1.10717545e+00  6.93366226e-01  1.44287693e+00
<br />  -5.39681562e-01 -8.08847196e-01]
<br /> [ 1.24549398e+00 -7.22391905e-01  1.11813340e+00  1.09899633e+00
<br />   1.00277655e+00 -9.01634490e-01 -5.32234021e-01 -8.22467189e-01
<br />   7.21711292e-01  6.74396105e-01]
<br /> [ 8.78643802e-01  1.03703898e+00 -4.77124206e-01  6.72619748e-01
<br />  -1.04948638e+00  2.42887697e+00  5.24750492e-01  1.00568668e+00
<br />   3.53567216e-01 -3.59901817e-02]
<br /> [ 7.00175710e-01  5.56073510e-01  8.96864073e-02  1.69380911e+00
<br />   8.82393314e-01  1.96869779e-01 -5.63788735e-01  1.69869255e-01
<br />  -1.16400797e+00 -6.01156801e-01]
<br /> [ 3.45715997e-01 -4.13029310e-01 -4.68673816e-01  1.83471763e+00
<br />   7.71514409e-01  5.64382855e-01  2.18628366e-02  2.13782807e+00
<br />  -7.85533997e-01  8.53281222e-01]
<br /> [ 1.14377130e+00  7.27813500e-01  3.52494364e-01  5.15073614e-01
<br />   1.17718111e+00 -2.78253447e+00 -1.94332341e+00  5.84646610e-01
<br />   3.24274243e-01 -2.36436952e-01]
<br /> [ 7.73703613e-01  1.27852808e+00 -2.11416392e+00 -4.42229280e-01
<br />   1.06821044e+00  3.23527354e-01 -2.50644065e+00 -1.09991490e-01
<br />   8.54894544e-03 -4.11639163e-01]
<br /> [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
<br />  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
<br />  -1.14870423e+00 -9.50909251e-01]
<br /> [ 1.02817479e+00 -5.08457134e-01  1.76533510e+00  7.77419205e-01
<br />   6.17714185e-01 -1.18771172e-01  4.50155513e-01 -1.98998184e-01
<br />   1.86647138e+00  8.70969803e-01]
<br /> [ 8.72267394e-01 -2.51630386e+00 -7.75070287e-01 -5.95667881e-01
<br />   1.02600767e+00 -3.09121319e-01  1.74643509e+00  5.10937774e-01
<br />   1.71066184e+00  1.41640538e-01]
<br /> [ 1.16755486e+00  3.53600971e-02  7.14789597e-01 -1.53879325e+00
<br />   1.10863359e+00 -4.47895185e-01 -1.75592564e+00  6.17985534e-01
<br />  -1.84176326e-01  8.52704062e-01]
<br /> [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
<br />  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
<br />  -4.38997664e-01  3.21265914e-01]
<br /> [ 4.46895161e-01  3.86539145e-01  1.35010682e+00 -8.51455657e-01
<br />   8.50637963e-01  1.00088142e+00 -1.16017010e+00 -3.84832249e-01
<br />   1.45810824e+00 -3.31283170e-01]]
<br />
<br />  #### metrics   ##################################################### 
<br />{}
<br />
<br />  #### Plot   ######################################################## 
<br />
<br />  #### Save/Load   ################################################### 
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br /><__main__.Model object at 0x7f4be11faeb8>
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
<br />  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f4be11faf28> 
<br />
<br />  #### Fit   ######################################################## 
<br />
<br />  #### Predict   #################################################### 
<br />[[ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
<br />  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
<br />   7.80469930e-01  1.10861676e+00]
<br /> [ 1.44682180e+00  8.07455917e-01  1.49810818e+00  3.12238689e-01
<br />  -6.82430193e-01 -1.93321640e-01  2.88078167e-01 -2.07680202e+00
<br />   9.47501167e-01 -3.00976154e-01]
<br /> [ 1.34728643e+00 -3.64538050e-01  8.07509886e-02 -4.59717681e-01
<br />  -8.89487596e-01  1.70548352e+00  9.49961101e-02  2.40505552e-01
<br />  -9.99426501e-01 -7.67803746e-01]
<br /> [ 1.14809657e+00 -7.33271604e-01  2.62467445e-01  8.36004719e-01
<br />   1.17353145e+00  1.54335911e+00  2.84748111e-01  7.58805660e-01
<br />   8.84908814e-01  2.76499305e-01]
<br /> [ 5.58538729e-01 -5.16347909e-01 -5.18145552e-01  3.51116897e-01
<br />   8.25506954e-01 -6.87704631e-02 -9.52062101e-01 -1.34776494e+00
<br />   1.47073986e+00 -1.46140360e+00]
<br /> [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
<br />   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
<br />   7.84770651e-01  4.92336556e-01]
<br /> [ 7.61706684e-01 -1.48515645e+00  1.30253554e+00 -5.92461285e-01
<br />  -1.64162479e+00 -2.30490794e+00 -1.34869645e+00 -3.18171727e-02
<br />   1.12487742e-01 -3.62612088e-01]
<br /> [ 1.46893146e+00 -1.47115693e+00  5.85910431e-01 -8.30171895e-01
<br />   1.03345052e+00 -8.80577600e-01 -9.55425262e-01 -2.79097722e-01
<br />   1.62284909e+00  2.06578332e+00]
<br /> [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
<br />   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
<br />   7.63804802e-02 -1.87316098e+00]
<br /> [ 8.61462558e-01  7.43205537e-02 -1.34501002e+00 -1.99560718e-01
<br />  -1.47533915e+00 -6.54603169e-01 -3.14563862e-01  3.18014296e-01
<br />  -8.90271552e-01 -1.29525789e+00]
<br /> [ 1.64661853e+00 -1.52568032e+00 -6.06998398e-01  7.95026094e-01
<br />   1.08480038e+00 -3.74438319e-01  4.29526140e-01  1.34048197e-01
<br />   1.20205486e+00  1.06222724e-01]
<br /> [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
<br />  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
<br />   1.05132077e+00  6.06548400e-01]
<br /> [ 9.29250600e-01 -1.10657307e+00 -1.95816909e+00 -3.59224096e-01
<br />  -1.21258781e+00  5.05381903e-01  5.42645295e-01  1.21794090e+00
<br />  -1.94068096e+00  6.77807571e-01]
<br /> [ 1.13545112e+00  8.61623101e-01  4.90616924e-02 -2.08639057e+00
<br />  -1.11469020e+00  3.61801641e-01 -8.06178212e-01  4.25920177e-01
<br />   4.90803971e-02 -5.96086335e-01]
<br /> [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
<br />   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
<br />  -1.30572692e+00 -8.61316361e-01]
<br /> [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
<br />  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
<br />   1.12368489e-01 -1.78175491e-02]
<br /> [ 5.69983848e-01 -5.33020326e-01 -1.75458969e-01 -1.42655542e+00
<br />   6.06604307e-01  1.76795995e+00 -1.15985185e-01 -4.75372875e-01
<br />   4.77610182e-01 -9.33914656e-01]
<br /> [ 1.66752297e+00  1.22372221e+00 -4.59930104e-01 -5.93679025e-02
<br />  -4.93856997e-01  1.44898940e+00 -1.18110317e+00 -4.77580855e-01
<br />   2.59999942e-02 -7.90799954e-01]
<br /> [ 7.88018455e-01  3.01960045e-01  7.00982122e-01 -3.94689681e-01
<br />  -1.20376927e+00 -1.17181338e+00  7.55392029e-01  9.84012237e-01
<br />  -5.59681422e-01 -1.98937450e-01]
<br /> [ 8.59823751e-01  1.71957132e-01 -3.48984191e-01  4.90561044e-01
<br />  -1.15649503e+00 -1.39528303e+00  6.14726276e-01 -5.22356465e-01
<br />  -3.69255902e-01 -9.77773002e-01]
<br /> [ 9.67037267e-01  3.82715174e-01 -8.06184817e-01 -2.88997343e-01
<br />   9.08526041e-01 -3.91816240e-01  1.62091229e+00  6.84001328e-01
<br />  -3.53409983e-01 -2.51674208e-01]
<br /> [ 1.02242019e+00  1.85300949e+00  6.44353666e-01  1.42251373e-01
<br />   1.15080755e+00  5.13505480e-01 -4.59942831e-01  3.72456852e-01
<br />  -1.48489803e-01  3.71670291e-01]
<br /> [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
<br />  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
<br />  -9.34181843e-01  9.54495667e-01]
<br /> [ 6.67591795e-01 -4.52524973e-01 -6.05981321e-01  1.16128569e+00
<br />  -1.44620987e+00  1.06996554e+00  1.92381543e+00 -1.04553425e+00
<br />   3.55284507e-01  1.80358898e+00]
<br /> [ 6.13636707e-01  3.16658895e-01  1.34710546e+00 -1.89526695e+00
<br />  -7.60458095e-01  8.97291174e-02 -3.29051549e-01  4.10265745e-01
<br />   8.59870972e-01 -1.04906775e+00]]
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
<br />[[ 1.02242019  1.85300949  0.64435367  0.14225137  1.15080755  0.51350548
<br />  -0.45994283  0.37245685 -0.1484898   0.37167029]
<br /> [ 1.66752297  1.22372221 -0.4599301  -0.0593679  -0.493857    1.4489894
<br />  -1.18110317 -0.47758085  0.02599999 -0.79079995]
<br /> [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
<br />   1.10223673  0.81434313  0.78046993  1.10861676]
<br /> [ 0.98379959 -0.40724002  0.93272141  0.16056499 -1.278618   -0.12014998
<br />   0.19975956  0.38560229  0.71829074 -0.5301198 ]
<br /> [ 0.88883881  1.03368687 -0.04970258  0.80884436  0.81405135  1.78975468
<br />   1.14690038  0.45128402 -1.68405999  0.46664327]
<br /> [ 1.16777676 -0.66575452 -1.23312074 -1.67419581  1.01313574  0.82502982
<br />  -0.12046457 -0.49821356 -0.31098498 -1.18231813]
<br /> [ 0.85729649  0.9561217  -0.82609743 -0.70584051  1.13872896  1.19268607
<br />   0.28267571 -0.23794194  1.15528789  0.6210827 ]
<br /> [ 0.55853873 -0.51634791 -0.51814555  0.3511169   0.82550695 -0.06877046
<br />  -0.9520621  -1.34776494  1.47073986 -1.4614036 ]
<br /> [ 0.85877496  2.29371761 -1.47023709 -0.83001099 -0.67204982 -1.01951985
<br />   0.59921324 -0.21465384  1.02124813  0.60640394]
<br /> [ 0.99785516 -0.6001388   0.45794708  0.14676526 -0.93355729  0.57180488
<br />   0.57296273 -0.03681766  0.11236849 -0.01781755]
<br /> [ 0.78344054 -0.05118845  0.82458463 -0.72559712  0.9317172  -0.86776868
<br />   3.03085711 -0.13597733 -0.79726979  0.65458015]
<br /> [ 0.345716   -0.41302931 -0.46867382  1.83471763  0.77151441  0.56438286
<br />   0.02186284  2.13782807 -0.785534    0.85328122]
<br /> [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
<br />  -1.1077125  -0.25898285  0.1892932  -1.71939447]
<br /> [ 0.44689516  0.38653915  1.35010682 -0.85145566  0.85063796  1.00088142
<br />  -1.1601701  -0.38483225  1.45810824 -0.33128317]
<br /> [ 0.62368852  1.2066079   0.90399917 -0.28286355 -1.18913787 -0.26632688
<br />   1.42361443  1.06897162  0.04037143  1.57546791]
<br /> [ 1.07258847 -0.58652394 -1.34267579 -1.23685338  1.24328724  0.87583893
<br />  -0.3264995   0.62336218 -0.43495668  1.11438298]
<br /> [ 0.79032389  1.61336137 -2.09424782 -0.37480469  0.91588404 -0.74996962
<br />   0.31027229  2.0546241   0.05340954 -0.22876583]
<br /> [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
<br />  -1.75592564  0.61798553 -0.18417633  0.85270406]
<br /> [ 0.61363671  0.3166589   1.34710546 -1.89526695 -0.76045809  0.08972912
<br />  -0.32905155  0.41026575  0.85987097 -1.04906775]
<br /> [ 0.85335555 -0.70435033 -0.67938378 -0.04586669 -1.29936179 -0.21873346
<br />   0.59003946  1.53920701 -1.14870423 -0.95090925]
<br /> [ 0.6236295   0.98635218  1.45391758 -0.46615486  0.93640333  1.38499134
<br />   0.03494359 -1.07296428  0.49515861  0.66168108]
<br /> [ 0.6109426  -2.79099641 -1.33520272 -0.45611756 -0.94495995 -0.97989025
<br />  -0.15699367  0.69257435 -0.47867236 -0.10646012]
<br /> [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
<br />  -1.09033833 -2.14444405 -0.36956243  0.60878366]
<br /> [ 0.62567337  0.5924728   0.67457071  1.19783084  1.23187251  1.70459417
<br />  -0.76730983  1.04008915 -0.91844004  1.46089238]
<br /> [ 1.39198128 -0.19022103 -0.53722302 -0.44873803  0.70455707 -0.67244804
<br />  -0.70134443 -0.55749472  0.93916874  0.15626385]]
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
<br />[master 90cd7ff] ml_store
<br /> 1 file changed, 296 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   8596592..90cd7ff  master -> master
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
<br />  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f8659275978> 
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
<br />[master aa11e29] ml_store
<br /> 1 file changed, 108 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   90cd7ff..aa11e29  master -> master
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
<br />Warning: Permanently added the RSA host key for IP address '140.82.114.3' to the list of known hosts.
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
