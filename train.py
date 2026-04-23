# -*- coding: utf-8 -*-
import sys
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

os.makedirs("data", exist_ok=True)

try:
    from chemprop.args import TrainArgs
    from chemprop.train.run_training import run_training
    from chemprop.train import cross_validate
except ImportError as e:
    print(f"[ERROR] Import failed: {e}")
    print("[SOLUTION] Run: pip install --force-reinstall chemprop==1.6.1 numpy==1.24.4")
    sys.exit(1)

DATA_PATH = "data/catalytic_data.csv"
SAVE_DIR = "models/"
EPOCHS = 10

if __name__ == '__main__':
    if not os.path.exists(DATA_PATH):
        print(f"[ERROR] Dataset not found: {DATA_PATH}, please run generate_csv.py first")
        sys.exit(1)

    args = TrainArgs().parse_args([
        "--data_path", DATA_PATH,
        "--save_dir", SAVE_DIR,
        "--epochs", str(EPOCHS),
        "--batch_size", "16",
        "--dataset_type", "regression",
        "--num_workers", "0",
        "--no_cuda",
        "--split_type", "random",
        "--metric", "rmse",
        "--seed", "42"
    ])

    try:
        cross_validate(args, train_func=run_training)
        print(f"[OK] Training complete! Models saved to {SAVE_DIR}")
    except Exception as e:
        print(f"[ERROR] Training failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)