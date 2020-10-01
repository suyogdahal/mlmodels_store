## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py


### Error 1, [Traceback at line 72](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L72)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 2, [Traceback at line 105](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L105)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 3, [Traceback at line 134](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L134)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 4, [Traceback at line 167](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L167)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 5, [Traceback at line 196](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L196)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 6, [Traceback at line 229](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L229)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 7, [Traceback at line 258](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L258)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 8, [Traceback at line 291](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L291)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 9, [Traceback at line 320](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L320)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 10, [Traceback at line 353](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L353)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 11, [Traceback at line 382](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L382)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 12, [Traceback at line 415](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L415)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 13, [Traceback at line 444](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L444)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 14, [Traceback at line 477](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L477)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 15, [Traceback at line 506](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L506)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 16, [Traceback at line 539](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L539)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 17, [Traceback at line 568](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L568)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 18, [Traceback at line 601](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L601)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 19, [Traceback at line 630](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L630)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 20, [Traceback at line 663](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L663)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 21, [Traceback at line 692](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L692)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 22, [Traceback at line 725](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L725)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 23, [Traceback at line 754](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L754)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 24, [Traceback at line 787](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L787)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 25, [Traceback at line 816](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L816)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 26, [Traceback at line 849](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L849)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 27, [Traceback at line 878](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L878)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 28, [Traceback at line 911](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L911)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 29, [Traceback at line 940](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L940)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 30, [Traceback at line 973](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L973)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 31, [Traceback at line 1002](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1002)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 32, [Traceback at line 1035](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1035)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 33, [Traceback at line 1064](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1064)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 34, [Traceback at line 1097](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1097)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 35, [Traceback at line 1126](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1126)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 36, [Traceback at line 1159](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1159)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 37, [Traceback at line 1188](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1188)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 38, [Traceback at line 1221](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1221)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 39, [Traceback at line 1250](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1250)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 40, [Traceback at line 1283](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1283)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 41, [Traceback at line 1312](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1312)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 42, [Traceback at line 1345](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1345)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 43, [Traceback at line 1374](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1374)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 44, [Traceback at line 1407](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1407)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 45, [Traceback at line 1436](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1436)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 46, [Traceback at line 1469](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1469)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 47, [Traceback at line 1498](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1498)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 48, [Traceback at line 1531](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1531)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 49, [Traceback at line 1560](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1560)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 50, [Traceback at line 1593](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1593)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 51, [Traceback at line 1622](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1622)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 52, [Traceback at line 1655](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1655)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 53, [Traceback at line 1681](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1681)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 54, [Traceback at line 1703](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1703)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 55, [Traceback at line 1720](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1720)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 292, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 56, [Traceback at line 1746](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1746)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 57, [Traceback at line 1768](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1768)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 58, [Traceback at line 1790](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1790)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 59, [Traceback at line 1812](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1812)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 60, [Traceback at line 1829](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1829)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 61, [Traceback at line 1855](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1855)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 62, [Traceback at line 1877](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1877)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 63, [Traceback at line 1894](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1894)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 64, [Traceback at line 1922](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1922)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
<br />    return module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/fb_prophet.py", line 89, in fit
<br />    train_df, test_df = get_dataset(data_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/fb_prophet.py", line 24, in get_dataset
<br />    train_col = data_pars["col_Xinput"]
<br />KeyError: 'col_Xinput'



### Error 65, [Traceback at line 1950](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1950)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 66, [Traceback at line 1967](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1967)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 67, [Traceback at line 1993](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L1993)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'



### Error 68, [Traceback at line 2010](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2010)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 69, [Traceback at line 2037](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2037)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 411, in fit_cli
<br />    model = model_create(module, model_p, data_p, compute_p)  # Exact map JSON and paramters
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 111, in model_create
<br />    model = module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 51, in __init__
<br />    texts, embeddings_index = get_dataset(data_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textvae.py", line 269, in get_dataset
<br />    with codecs.open(data_pars["train_data_path"], encoding='utf-8') as f:
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/codecs.py", line 897, in open
<br />    file = builtins.open(filename, mode, buffering)
<br />FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv'



### Error 70, [Traceback at line 2062](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2062)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 71, [Traceback at line 2137](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2137)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 72, [Traceback at line 2163](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2163)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 73, [Traceback at line 2180](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2180)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 74, [Traceback at line 2187](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2187)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_keras.Autokeras notfound, No module named 'autokeras', tuple index out of range



### Error 75, [Traceback at line 2206](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2206)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 76, [Traceback at line 2326](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2326)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 77, [Traceback at line 2352](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2352)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_classifier.py", line 39, in <module>
<br />    from util_transformer import (convert_examples_to_features, output_modes,
<br />ModuleNotFoundError: No module named 'util_transformer'



### Error 78, [Traceback at line 2369](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2369)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 79, [Traceback at line 2376](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2376)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_tch.transformer_classifier notfound, No module named 'util_transformer', tuple index out of range



### Error 80, [Traceback at line 2395](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2395)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 294, in config_get_pars
<br />    out_p     = path_norm_dict( js.get("out_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 81, [Traceback at line 2466](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2466)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/textcnn.py", line 153, in create_tabular_dataset
<br />    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
<br />    return util.load_model(name, **overrides)
<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
<br />    raise IOError(Errors.E050.format(name=name))
<br />OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.



### Error 82, [Traceback at line 2477](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2477)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 414, in fit_cli
<br />    model, sess = fit(module, model, data_pars=data_p, compute_pars=compute_p, out_pars=out_p)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 123, in fit
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



### Error 83, [Traceback at line 2506](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2506)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 292, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 84, [Traceback at line 2532](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2532)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 85, [Traceback at line 2562](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2562)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 86, [Traceback at line 2569](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2569)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 87, [Traceback at line 2588](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2588)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 88, [Traceback at line 2618](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2618)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 89, [Traceback at line 2625](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2625)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 90, [Traceback at line 2644](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2644)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 91, [Traceback at line 2674](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2674)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 92, [Traceback at line 2681](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2681)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 93, [Traceback at line 2700](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2700)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 94, [Traceback at line 2730](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2730)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 95, [Traceback at line 2737](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2737)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 96, [Traceback at line 2756](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2756)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 97, [Traceback at line 2786](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2786)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 98, [Traceback at line 2793](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2793)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 99, [Traceback at line 2812](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2812)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 100, [Traceback at line 2842](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2842)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 101, [Traceback at line 2849](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2849)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 102, [Traceback at line 2868](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2868)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 103, [Traceback at line 2898](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2898)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 104, [Traceback at line 2905](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2905)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 105, [Traceback at line 2924](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2924)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 106, [Traceback at line 2954](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2954)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 107, [Traceback at line 2961](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L2961)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 108, [Traceback at line 3075](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3075)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/fb_prophet.py", line 104, in save
<br />    path = save_pars["outpath"]
<br />KeyError: 'outpath'



### Error 109, [Traceback at line 3164](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3164)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/armdn.py", line 210, in save
<br />    path = save_pars["outpath"]
<br />KeyError: 'outpath'



### Error 110, [Traceback at line 3721](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3721)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/nbeats.py", line 296, in save
<br />    grad_step       = save_pars['grad_step']
<br />KeyError: 'grad_step'



### Error 111, [Traceback at line 3742](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3742)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 112, [Traceback at line 3772](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3772)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 113, [Traceback at line 3779](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3779)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 114, [Traceback at line 3798](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3798)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 115, [Traceback at line 3828](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3828)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 116, [Traceback at line 3835](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3835)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 117, [Traceback at line 3854](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3854)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 118, [Traceback at line 3884](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3884)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 119, [Traceback at line 3891](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3891)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 120, [Traceback at line 3910](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3910)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 121, [Traceback at line 3940](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3940)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 122, [Traceback at line 3947](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3947)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 123, [Traceback at line 3966](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3966)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 124, [Traceback at line 3996](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L3996)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 125, [Traceback at line 4003](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4003)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 126, [Traceback at line 4022](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4022)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 127, [Traceback at line 4052](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4052)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 128, [Traceback at line 4059](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4059)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 129, [Traceback at line 4078](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4078)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 130, [Traceback at line 4108](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4108)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 131, [Traceback at line 4115](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4115)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 132, [Traceback at line 4134](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4134)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 70, in module_load
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



### Error 133, [Traceback at line 4164](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4164)<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 82, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 134, [Traceback at line 4171](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4171)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 410, in fit_cli
<br />    module = module_load(model_uri)  # '1_lstm.py
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 87, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon notfound, create_model() takes exactly 1 positional argument (0 given), tuple index out of range



### Error 135, [Traceback at line 4731](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4731)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/nbeats.py", line 296, in save
<br />    grad_step       = save_pars['grad_step']
<br />KeyError: 'grad_step'



### Error 136, [Traceback at line 4752](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4752)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 407, in fit_cli
<br />    model_p, data_p, compute_p, out_p = config_get_pars(config_file, arg.config_mode)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 292, in config_get_pars
<br />    data_p    = path_norm_dict( js.get("data_pars") )
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 201, in path_norm_dict
<br />    for k,v in ddict.items():
<br />AttributeError: 'NoneType' object has no attribute 'items'



### Error 137, [Traceback at line 4846](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4846)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/armdn.py", line 210, in save
<br />    path = save_pars["outpath"]
<br />KeyError: 'outpath'



### Error 138, [Traceback at line 4962](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4962)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 418, in fit_cli
<br />    save(module, model, sess, save_pars)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 161, in save
<br />    return module.save(model, session, save_pars, **kwarg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/fb_prophet.py", line 104, in save
<br />    path = save_pars["outpath"]
<br />KeyError: 'outpath'



### Error 139, [Traceback at line 4988](https://github.com/arita37/mlmodels_store/blob/master/log_json/log_json_2020-05-11-06-06_f3819ba2d2a4e525f7f9ec0cef0a000f860c50b0.py#L4988)<br />  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
<br />    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 510, in main
<br />    fit_cli(arg)
<br />  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 408, in fit_cli
<br />    model_uri = model_p['model_uri']
<br />KeyError: 'model_uri'
