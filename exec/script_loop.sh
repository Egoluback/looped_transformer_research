
n_gpu=0

# Linear Regression  ###################################################################################################
b=30
T=15
python scripts/train.py --config configs/base_loop.yaml \
    --training.curriculum.loops.start $T \
    --training.curriculum.loops.end $b \
    --training.n_loop_window $T \
    --wandb.name "custom_experiment" \
    --gpu.n_gpu $n_gpu
