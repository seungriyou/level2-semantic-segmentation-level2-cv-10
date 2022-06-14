_base_ = [
    '/opt/ml/input/level2-semantic-segmentation-level2-cv-10/mmsegmentation/configs/_youngwoo_/_base_/models/upernet_r50.py',
    '/opt/ml/input/level2-semantic-segmentation-level2-cv-10/mmsegmentation/configs/_youngwoo_/_base_/datasets/custom.py', 
    '/opt/ml/input/level2-semantic-segmentation-level2-cv-10/mmsegmentation/configs/_youngwoo_/_base_/default_runtime_fp16.py',
    '/opt/ml/input/level2-semantic-segmentation-level2-cv-10/mmsegmentation/configs/_youngwoo_/_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(num_classes=11), auxiliary_head=dict(num_classes=11))

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.01)

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)


