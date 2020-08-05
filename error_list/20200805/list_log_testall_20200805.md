## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py


### Error 1, [Traceback at line 37](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L37)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
<br />    from mlmodels.mode_tf.raw  import temporal_fusion_google
<br />ModuleNotFoundError: No module named 'mlmodels.mode_tf'



### Error 2, [Traceback at line 152](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L152)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1365, in _do_call
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



### Error 3, [Traceback at line 164](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L164)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1290, in restore
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



### Error 4, [Traceback at line 215](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L215)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1300, in restore
<br />    names_to_keys = object_graph_key_mapping(save_path)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1618, in object_graph_key_mapping
<br />    object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 915, in get_tensor
<br />    return CheckpointReader_GetTensor(self, compat.as_bytes(tensor_str))
<br />tensorflow.python.framework.errors_impl.NotFoundError: Key _CHECKPOINTABLE_OBJECT_GRAPH not found in checkpoint
<br />
<br />During handling of the above exception, another exception occurred:
<br />



### Error 5, [Traceback at line 226](https://github.com/arita37/mlmodels_store/blob/master/log_testall/log_testall_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L226)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
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
<br />[master a5198b3] ml_store
<br /> 1 file changed, 235 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   fd7a6fa..a5198b3  master -> master
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
<br />[[ 1.39198128 -0.19022103 -0.53722302 -0.44873803  0.70455707 -0.67244804
<br />  -0.70134443 -0.55749472  0.93916874  0.15626385]
<br /> [ 1.838294    0.50274088  0.12910158  1.55880554  1.32551412  0.1094027
<br />   1.40754    -1.2197444   2.44936865  1.6169496 ]
<br /> [ 0.70017571  0.55607351  0.08968641  1.69380911  0.88239331  0.19686978
<br />  -0.56378873  0.16986926 -1.16400797 -0.6011568 ]
<br /> [ 0.86146256  0.07432055 -1.34501002 -0.19956072 -1.47533915 -0.65460317
<br />  -0.31456386  0.3180143  -0.89027155 -1.29525789]
<br /> [ 1.18468624 -1.00016919 -0.59384307  1.04499441  0.96548233  0.6085147
<br />  -0.625342   -0.0693287  -0.10839207 -0.34390071]
<br /> [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
<br />  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
<br /> [ 0.68188934 -1.15498263  1.22895559 -0.1776322   0.99854519 -1.51045638
<br />  -0.27584606  1.01120706 -1.47656266  1.30970591]
<br /> [ 0.47330777 -0.97326759 -0.22814069  0.17516773 -1.01366961 -0.05348369
<br />   0.39378773 -0.18306199 -0.2210289   0.58033011]
<br /> [ 0.88883881  1.03368687 -0.04970258  0.80884436  0.81405135  1.78975468
<br />   1.14690038  0.45128402 -1.68405999  0.46664327]
<br /> [ 1.09488485 -0.06962454 -0.11644415  0.35387043 -1.44189096 -0.18695502
<br />   1.2911889  -0.15323616 -2.43250851 -2.277298  ]
<br /> [ 0.61363671  0.3166589   1.34710546 -1.89526695 -0.76045809  0.08972912
<br />  -0.32905155  0.41026575  0.85987097 -1.04906775]
<br /> [ 1.16777676 -0.66575452 -1.23312074 -1.67419581  1.01313574  0.82502982
<br />  -0.12046457 -0.49821356 -0.31098498 -1.18231813]
<br /> [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
<br />  -0.94843966  0.10405339  0.52800342  1.00796648]
<br /> [ 0.87699465  1.23225307 -0.86778722 -0.25417987  0.89189141  1.39984394
<br />  -0.87728152 -0.78191168 -0.43750898 -1.44087602]
<br /> [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
<br />   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]
<br /> [ 1.34728643 -0.36453805  0.08075099 -0.45971768 -0.8894876   1.70548352
<br />   0.09499611  0.24050555 -0.9994265  -0.76780375]
<br /> [ 1.64661853 -1.52568032 -0.6069984   0.79502609  1.08480038 -0.37443832
<br />   0.42952614  0.1340482   1.20205486  0.10622272]
<br /> [ 0.6675918  -0.45252497 -0.60598132  1.16128569 -1.44620987  1.06996554
<br />   1.92381543 -1.04553425  0.35528451  1.80358898]
<br /> [ 1.06040861  0.5103076   0.50172511 -0.91579185 -0.90731836 -0.40725204
<br />  -0.17961229  0.98495167  1.07125243 -0.59334375]
<br /> [ 1.18559003  0.08646441  1.23289919 -2.14246673  1.033341   -0.83016886
<br />   0.36723181  0.45161595  1.10417433 -0.42285696]
<br /> [ 0.85877496  2.29371761 -1.47023709 -0.83001099 -0.67204982 -1.01951985
<br />   0.59921324 -0.21465384  1.02124813  0.60640394]
<br /> [ 1.77547698 -0.20339445 -0.19883786  0.24266944  0.96435056  0.20183018
<br />  -0.54577417  0.66102029  1.79215821 -0.7003985 ]
<br /> [ 1.4468218   0.80745592  1.49810818  0.31223869 -0.68243019 -0.19332164
<br />   0.28807817 -2.07680202  0.94750117 -0.30097615]
<br /> [ 1.32720112 -0.16119832  0.6024509  -0.28638492 -0.5789623  -0.87088765
<br />   1.37975819  0.50142959 -0.47861407 -0.89264667]
<br /> [ 0.98042741  1.93752881 -0.23083974  0.36633201  1.10018476 -1.04458938
<br />  -0.34498721  2.05117344  0.585662   -2.793085  ]]
<br />
<br />  #### metrics   ##################################################### 
<br />{}
<br />
<br />  #### Plot   ######################################################## 
<br />
<br />  #### Save/Load   ################################################### 
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br />{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<br /><__main__.Model object at 0x7f6935c84eb8>
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
<br />  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f6935c84f28> 
<br />
<br />  #### Fit   ######################################################## 
<br />
<br />  #### Predict   #################################################### 
<br />[[ 0.10593645 -0.73728963  0.65032321  0.16466507 -1.53556118  0.77817418
<br />   0.05031709  0.30981676  1.05132077  0.6065484 ]
<br /> [ 0.87699465  1.23225307 -0.86778722 -0.25417987  0.89189141  1.39984394
<br />  -0.87728152 -0.78191168 -0.43750898 -1.44087602]
<br /> [ 0.44689516  0.38653915  1.35010682 -0.85145566  0.85063796  1.00088142
<br />  -1.1601701  -0.38483225  1.45810824 -0.33128317]
<br /> [ 0.93621125  0.20437739 -1.49419377  0.61223252 -0.98437725  0.74488454
<br />   0.49434165 -0.03628129 -0.83239535 -0.4466992 ]
<br /> [ 0.55853873 -0.51634791 -0.51814555  0.3511169   0.82550695 -0.06877046
<br />  -0.9520621  -1.34776494  1.47073986 -1.4614036 ]
<br /> [ 1.34728643 -0.36453805  0.08075099 -0.45971768 -0.8894876   1.70548352
<br />   0.09499611  0.24050555 -0.9994265  -0.76780375]
<br /> [ 1.25704434 -1.82391985 -0.61240697  1.16707517 -0.62373281 -0.0396687
<br />   0.81604368  0.8858258   0.18986165  0.39310924]
<br /> [ 0.85982375  0.17195713 -0.34898419  0.49056104 -1.15649503 -1.39528303
<br />   0.61472628 -0.52235647 -0.3692559  -0.977773  ]
<br /> [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
<br />  -1.75592564  0.61798553 -0.18417633  0.85270406]
<br /> [ 1.06523311 -0.66486777  1.00806543 -1.94504696 -1.23017555 -0.91542437
<br />   0.33722094  1.22515585 -1.05354607  0.78522692]
<br /> [ 1.66752297  1.22372221 -0.4599301  -0.0593679  -0.493857    1.4489894
<br />  -1.18110317 -0.47758085  0.02599999 -0.79079995]
<br /> [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
<br />  -0.94843966  0.10405339  0.52800342  1.00796648]
<br /> [ 0.69211449 -0.06065249  2.05635552 -2.413503    1.17456965 -1.77756638
<br />  -0.28173627 -0.77785883  1.11584111  1.76024923]
<br /> [ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
<br />  -0.3169012   0.43499832  0.9104236   1.21987438]
<br /> [ 1.46893146 -1.47115693  0.58591043 -0.8301719   1.03345052 -0.8805776
<br />  -0.95542526 -0.27909772  1.62284909  2.06578332]
<br /> [ 0.56998385 -0.53302033 -0.17545897 -1.42655542  0.60660431  1.76795995
<br />  -0.11598519 -0.47537288  0.47761018 -0.93391466]
<br /> [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
<br />   1.10223673  0.81434313  0.78046993  1.10861676]
<br /> [ 1.4468218   0.80745592  1.49810818  0.31223869 -0.68243019 -0.19332164
<br />   0.28807817 -2.07680202  0.94750117 -0.30097615]
<br /> [ 1.18947778 -0.68067814 -0.05682448 -0.08450803  0.82178321 -0.29736188
<br />  -0.18657899  0.417302    0.78477065  0.49233656]
<br /> [ 1.18468624 -1.00016919 -0.59384307  1.04499441  0.96548233  0.6085147
<br />  -0.625342   -0.0693287  -0.10839207 -0.34390071]
<br /> [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
<br />  -1.1077125  -0.25898285  0.1892932  -1.71939447]
<br /> [ 1.03967316 -0.73153098  0.36184732 -1.56573815  0.95928819  1.01382247
<br />  -1.78791289 -2.22711263 -1.6993336  -0.42449279]
<br /> [ 1.838294    0.50274088  0.12910158  1.55880554  1.32551412  0.1094027
<br />   1.40754    -1.2197444   2.44936865  1.6169496 ]
<br /> [ 0.78801845  0.30196005  0.70098212 -0.39468968 -1.20376927 -1.17181338
<br />   0.75539203  0.98401224 -0.55968142 -0.19893745]
<br /> [ 0.88861146  0.84958685 -0.03091142 -0.12215402 -1.14722826 -0.68085157
<br />  -0.32606131 -1.06787658 -0.07667936  0.35571726]]
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
<br />[[ 8.15836116e-01 -1.39169388e+00  2.50598029e+00  4.50217742e-01
<br />  -8.82869820e-01  6.27437083e-01 -1.19586151e+00  7.51337235e-01
<br />   1.40395436e-01  1.91979229e+00]
<br /> [ 6.81889336e-01 -1.15498263e+00  1.22895559e+00 -1.77632196e-01
<br />   9.98545187e-01 -1.51045638e+00 -2.75846063e-01  1.01120706e+00
<br />  -1.47656266e+00  1.30970591e+00]
<br /> [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
<br />  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
<br />  -8.32395348e-01 -4.46699203e-01]
<br /> [ 1.06702918e+00 -4.29142278e-01  3.50167159e-01  1.20845633e+00
<br />   7.51480619e-01  1.11570180e+00 -4.79157099e-01  8.40861558e-01
<br />  -1.02887218e-01  1.71647264e-02]
<br /> [ 4.67397905e-01 -2.37875265e-01 -1.54491194e-01 -7.55662765e-01
<br />  -5.47062239e-01  1.85143789e+00 -1.46405357e+00  2.09096677e-01
<br />   1.55501599e+00 -9.24323185e-02]
<br /> [ 6.21530991e-01 -1.50957268e+00 -1.01932039e-01 -1.08071069e+00
<br />  -1.13742855e+00  7.25474004e-01  7.98063795e-01 -3.91782562e-02
<br />  -2.28754171e-01  7.43356544e-01]
<br /> [ 6.92114488e-01 -6.06524918e-02  2.05635552e+00 -2.41350300e+00
<br />   1.17456965e+00 -1.77756638e+00 -2.81736269e-01 -7.77858827e-01
<br />   1.11584111e+00  1.76024923e+00]
<br /> [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
<br />   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
<br />   1.40925339e+00  9.66539250e-01]
<br /> [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
<br />   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
<br />   4.95158611e-01  6.61681076e-01]
<br /> [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
<br />   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
<br />  -2.23708651e+00 -4.14846901e-01]
<br /> [ 7.90323893e-01  1.61336137e+00 -2.09424782e+00 -3.74804687e-01
<br />   9.15884042e-01 -7.49969617e-01  3.10272288e-01  2.05462410e+00
<br />   5.34095368e-02 -2.28765829e-01]
<br /> [ 1.18468624e+00 -1.00016919e+00 -5.93843067e-01  1.04499441e+00
<br />   9.65482331e-01  6.08514698e-01 -6.25342001e-01 -6.93286967e-02
<br />  -1.08392067e-01 -3.43900709e-01]
<br /> [ 9.80427414e-01  1.93752881e+00 -2.30839743e-01  3.66332015e-01
<br />   1.10018476e+00 -1.04458938e+00 -3.44987210e-01  2.05117344e+00
<br />   5.85662000e-01 -2.79308500e+00]
<br /> [ 1.14377130e+00  7.27813500e-01  3.52494364e-01  5.15073614e-01
<br />   1.17718111e+00 -2.78253447e+00 -1.94332341e+00  5.84646610e-01
<br />   3.24274243e-01 -2.36436952e-01]
<br /> [ 3.54133613e-01  2.11124755e-01  9.21450069e-01  1.65275673e-02
<br />   9.03945451e-01  1.77187720e-01  9.54250872e-02 -1.11647002e+00
<br />   8.09271010e-02  6.07501958e-02]
<br /> [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
<br />   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
<br />  -1.30572692e+00 -8.61316361e-01]
<br /> [ 6.23688521e-01  1.20660790e+00  9.03999174e-01 -2.82863552e-01
<br />  -1.18913787e+00 -2.66326884e-01  1.42361443e+00  1.06897162e+00
<br />   4.03714310e-02  1.57546791e+00]
<br /> [ 1.37661405e+00 -6.00225330e-01  7.25916853e-01 -3.79517516e-01
<br />  -6.27546260e-01 -1.01480369e+00  9.66220863e-01  4.35986196e-01
<br />  -6.87487393e-01  3.32107876e+00]
<br /> [ 1.12641981e+00 -6.29441604e-01  1.10100020e+00 -1.11343610e+00
<br />   9.44595066e-01 -6.74100249e-02 -1.83400197e-01  1.16143998e+00
<br />  -2.75293863e-02  7.80027135e-01]
<br /> [ 1.24549398e+00 -7.22391905e-01  1.11813340e+00  1.09899633e+00
<br />   1.00277655e+00 -9.01634490e-01 -5.32234021e-01 -8.22467189e-01
<br />   7.21711292e-01  6.74396105e-01]
<br /> [ 1.16777676e+00 -6.65754518e-01 -1.23312074e+00 -1.67419581e+00
<br />   1.01313574e+00  8.25029824e-01 -1.20464572e-01 -4.98213564e-01
<br />  -3.10984978e-01 -1.18231813e+00]
<br /> [ 8.88389445e-01  2.82995534e-01  1.79558917e-02  1.08030817e-01
<br />  -8.49671873e-01  2.94176190e-02 -5.03973949e-01 -1.34793129e-01
<br />   1.04921829e+00 -1.27046078e+00]
<br /> [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
<br />  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
<br />   7.80469930e-01  1.10861676e+00]
<br /> [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
<br />  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
<br />   1.12368489e-01 -1.78175491e-02]
<br /> [ 5.63077902e-01 -1.17598267e+00 -1.74180344e-01  1.01012718e+00
<br />   1.06796368e+00  9.20017933e-01 -1.68198840e-01 -1.95057341e-01
<br />   8.05393424e-01  4.61164100e-01]]
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
<br />[master d8c9e5c] ml_store
<br /> 1 file changed, 271 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   a5198b3..d8c9e5c  master -> master
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
<br />  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7fee1d08b7f0> 
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
<br />[master 9f4dfdd] ml_store
<br /> 1 file changed, 108 insertions(+)
<br />To github.com:arita37/mlmodels_store.git
<br />   d8c9e5c..9f4dfdd  master -> master
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
<br />From github.com:arita37/mlmodels_store
<br />   9f4dfdd..faca6c7  master     -> origin/master
<br />Updating 9f4dfdd..faca6c7
<br />Fast-forward
<br /> ...-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py | 617 +++++++++++++++++++++
<br /> 1 file changed, 617 insertions(+)
<br /> create mode 100644 log_pullrequest/log_pr_2020-05-12-04-10_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py
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
