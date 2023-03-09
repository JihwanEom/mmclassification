dataset_type = 'CustomDataset'
data = dict(
    samples_per_gpu=16,
    workers_per_gpu=8,
    persistent_workers=False,
    train=dict(
        type=dataset_type, 
        data_prefix='data/label/POA',
        ann_file=None),
    val=dict(
        type=dataset_type,
        data_prefix='data/label/POA',
        ann_file=None,
        test_mode=True),
    test=dict(
        type=dataset_type,
        data_prefix='data/label/POA',
        ann_file=None,
        test_mode=True))
