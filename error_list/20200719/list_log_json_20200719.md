## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py


### Error 1, [Traceback at line 77](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L77)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 2, [Traceback at line 112](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L112)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 3, [Traceback at line 145](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L145)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 4, [Traceback at line 180](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L180)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 5, [Traceback at line 213](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L213)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 6, [Traceback at line 248](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L248)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 7, [Traceback at line 281](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L281)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 8, [Traceback at line 316](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L316)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 9, [Traceback at line 349](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L349)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 10, [Traceback at line 384](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L384)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 11, [Traceback at line 417](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L417)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 12, [Traceback at line 452](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L452)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 13, [Traceback at line 485](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L485)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 14, [Traceback at line 520](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L520)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 15, [Traceback at line 553](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L553)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 16, [Traceback at line 588](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L588)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 17, [Traceback at line 621](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L621)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 18, [Traceback at line 656](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L656)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 19, [Traceback at line 689](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L689)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 20, [Traceback at line 724](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L724)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 21, [Traceback at line 757](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L757)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 22, [Traceback at line 792](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L792)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 23, [Traceback at line 825](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L825)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 24, [Traceback at line 860](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L860)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 25, [Traceback at line 893](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L893)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 26, [Traceback at line 928](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L928)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 27, [Traceback at line 961](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L961)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 28, [Traceback at line 996](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L996)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 29, [Traceback at line 1029](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1029)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 30, [Traceback at line 1064](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1064)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 31, [Traceback at line 1097](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1097)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 32, [Traceback at line 1132](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1132)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 33, [Traceback at line 1165](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1165)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 34, [Traceback at line 1200](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1200)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 35, [Traceback at line 1233](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1233)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 36, [Traceback at line 1268](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1268)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 37, [Traceback at line 1301](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1301)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 38, [Traceback at line 1336](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1336)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 39, [Traceback at line 1369](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1369)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 40, [Traceback at line 1404](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1404)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 41, [Traceback at line 1437](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1437)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 42, [Traceback at line 1472](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1472)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 43, [Traceback at line 1505](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1505)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 44, [Traceback at line 1540](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1540)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 45, [Traceback at line 1573](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1573)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 46, [Traceback at line 1608](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1608)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 47, [Traceback at line 1641](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1641)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 48, [Traceback at line 1676](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1676)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 49, [Traceback at line 1709](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1709)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 50, [Traceback at line 1744](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1744)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 51, [Traceback at line 1777](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1777)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 207, in fit
<br />    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/torchhub.py", line 46, in _train
<br />    for i,batch in enumerate(train_itr):
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
<br />    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
<br />    return self.collate_fn(data)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
<br />    return [default_collate(samples) for samples in transposed]
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
<br />    raise TypeError(default_collate_err_msg_format.format(elem_type))
<br />TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>



### Error 52, [Traceback at line 1812](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1812)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 53, [Traceback at line 1840](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1840)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 54, [Traceback at line 1864](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1864)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 55, [Traceback at line 1883](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1883)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 56, [Traceback at line 1911](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1911)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 57, [Traceback at line 1935](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1935)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 58, [Traceback at line 1959](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1959)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 59, [Traceback at line 1983](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L1983)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 60, [Traceback at line 2002](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2002)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 61, [Traceback at line 2030](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2030)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 62, [Traceback at line 2054](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2054)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 63, [Traceback at line 2073](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2073)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 64, [Traceback at line 2101](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2101)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 65, [Traceback at line 2125](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2125)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 66, [Traceback at line 2144](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2144)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 67, [Traceback at line 2172](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2172)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 68, [Traceback at line 2191](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2191)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 69, [Traceback at line 2222](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2222)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    model = model_create(module, model_p, data_p, compute_p)  # Exact map JSON and paramters
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 113, in model_create
<br />    model = module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 51, in __init__
<br />    texts, embeddings_index = get_dataset(data_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 269, in get_dataset
<br />    with codecs.open(data_pars["train_data_path"], encoding='utf-8') as f:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/codecs.py", line 897, in open
<br />    file = builtins.open(filename, mode, buffering)
<br />FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv'



### Error 70, [Traceback at line 2249](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2249)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 71, [Traceback at line 2330](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2330)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 72, [Traceback at line 2360](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2360)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/Autokeras.py", line 12, in <module>
<br />    import autokeras as ak
<br />ModuleNotFoundError: No module named 'autokeras'



### Error 73, [Traceback at line 2377](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2377)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 74, [Traceback at line 2384](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2384)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_keras.Autokeras notfound, No module named 'autokeras', tuple index out of range



### Error 75, [Traceback at line 2405](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2405)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 76, [Traceback at line 2531](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2531)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 77, [Traceback at line 2559](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2559)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 78, [Traceback at line 2578](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2578)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 296, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 79, [Traceback at line 2653](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2653)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 153, in create_tabular_dataset
<br />    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
<br />    return util.load_model(name, **overrides)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
<br />    raise IOError(Errors.E050.format(name=name))
<br />OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.



### Error 80, [Traceback at line 2664](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2664)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 421, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 125, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 291, in fit
<br />    train_iter, valid_iter, vocab = get_dataset(data_pars, out_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 334, in get_dataset
<br />    trainset, validset, vocab = create_tabular_dataset( data_pars['train_path'], data_pars['valid_path'], lang, pretrained_emb)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 159, in create_tabular_dataset
<br />    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)  
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
<br />    return util.load_model(name, **overrides)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
<br />    raise IOError(Errors.E050.format(name=name))
<br />OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.



### Error 81, [Traceback at line 2695](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2695)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 82, [Traceback at line 2725](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2725)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 83, [Traceback at line 2755](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2755)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 84, [Traceback at line 2762](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2762)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 85, [Traceback at line 2785](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2785)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 86, [Traceback at line 2815](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2815)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 87, [Traceback at line 2822](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2822)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 88, [Traceback at line 2845](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2845)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 89, [Traceback at line 2875](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2875)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 90, [Traceback at line 2882](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2882)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 91, [Traceback at line 2905](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2905)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 92, [Traceback at line 2935](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2935)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 93, [Traceback at line 2942](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2942)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 94, [Traceback at line 2965](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2965)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 95, [Traceback at line 2995](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L2995)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 96, [Traceback at line 3002](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3002)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 97, [Traceback at line 3025](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3025)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 98, [Traceback at line 3055](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3055)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 99, [Traceback at line 3062](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3062)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 100, [Traceback at line 3085](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3085)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 101, [Traceback at line 3115](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3115)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 102, [Traceback at line 3122](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3122)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 103, [Traceback at line 3145](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3145)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 104, [Traceback at line 3175](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3175)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 105, [Traceback at line 3182](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3182)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 106, [Traceback at line 3208](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3208)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 107, [Traceback at line 3227](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3227)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 108, [Traceback at line 3246](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3246)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 109, [Traceback at line 3267](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3267)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 110, [Traceback at line 3297](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3297)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 111, [Traceback at line 3304](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3304)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 112, [Traceback at line 3327](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3327)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 113, [Traceback at line 3357](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3357)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 114, [Traceback at line 3364](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3364)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 115, [Traceback at line 3387](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3387)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 116, [Traceback at line 3417](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3417)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 117, [Traceback at line 3424](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3424)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 118, [Traceback at line 3447](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3447)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 119, [Traceback at line 3477](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3477)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 120, [Traceback at line 3484](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3484)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 121, [Traceback at line 3507](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3507)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 122, [Traceback at line 3537](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3537)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 123, [Traceback at line 3544](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3544)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 124, [Traceback at line 3567](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3567)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 125, [Traceback at line 3597](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3597)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 126, [Traceback at line 3604](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3604)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 127, [Traceback at line 3627](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3627)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 128, [Traceback at line 3657](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3657)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 129, [Traceback at line 3664](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3664)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 130, [Traceback at line 3687](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3687)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py", line 15, in <module>
<br />    from gluonts.model.deepar import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
<br />    from ._estimator import DeepAREstimator
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
<br />    from gluonts.distribution import DistributionOutput, StudentTOutput
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
<br />    from . import bijection
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
<br />    class Bijection:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
<br />    @validated()
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
<br />    **init_fields,
<br />  File "pydantic/main.py", line 778, in pydantic.main.create_model
<br />TypeError: create_model() takes exactly 1 positional argument (0 given)



### Error 131, [Traceback at line 3717](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3717)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 132, [Traceback at line 3724](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3724)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 417, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 133, [Traceback at line 3750](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3750)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 134, [Traceback at line 3769](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3769)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 135, [Traceback at line 3797](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3797)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 136, [Traceback at line 3821](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3821)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 412, in fit_cli
<br />    path      = out_p['path']
<br />KeyError: 'path'



### Error 137, [Traceback at line 3845](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-21-15_1f36c00be3a0e28b634b1ba3bd0de78bfdb3dba5.py#L3845)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 527, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'
