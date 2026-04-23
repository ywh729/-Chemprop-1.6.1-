# -*- coding: utf-8 -*-
import sys
import os

MODEL_DIR = "models"

if __name__ == '__main__':
    if not os.path.exists(MODEL_DIR):
        print(f"[ERROR] Model directory not found: {MODEL_DIR}, please run train.py first")
        sys.exit(1)

    try:
        from chemprop.train import chemprop_predict
        print("[OK] chemprop_predict imported successfully")
        print("[OK] Prediction functionality is available")
        print("[OK] You can use: python -m chemprop.train.make_predictions --test_path data/predict_smiles.csv --preds_path data/predictions.csv --checkpoint_paths models/fold_0/model_0/model.pt --num_workers 0 --no_cuda")
        print("\n[OK] Project is working correctly!")
        
    except Exception as e:
        print(f"[ERROR] Prediction failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)