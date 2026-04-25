# Chemprop Molecule Property Prediction

一个基于 Chemprop 1.6.1 的分子性质预测项目，用于预测催化剂和材料的多种性质。

## 📁 项目结构

```
PythonProject/
├── data/                # 数据目录
│   ├── catalytic_data.csv  # 多任务训练数据（吸附能、过电势、活性、选择性）
│   ├── data.csv            # 单任务训练数据
│   └── predict_smiles.csv  # 预测测试数据
├── models/              # 模型保存目录
│   └── fold_0/          # 交叉验证折叠
│       └── model_0/      # 训练模型
│           └── model.pt   # 模型权重文件
├── train.py             # 模型训练脚本
├── predict.py           # 预测功能验证脚本
├── main.py              # 完整流程执行脚本
├── generate_csv.py      # 数据集生成脚本
└── check_env.py         # 环境检查脚本
```

## 🔧 环境配置
Anaconda下
### Python 版本
- Python 3.10.20

### 依赖库版本

| 库 | 版本 | 用途 |
|-----|------|------|
| chemprop | 1.6.1 | 分子性质预测框架 |
| torch | 2.0.1 | 深度学习框架 |
| numpy | 1.24.4 | 数值计算 |
| scikit-learn | 1.3.2 | 机器学习工具 |
| pandas | 2.3.3 | 数据处理 |
| rdkit | 2026.3.1 | 分子处理 |
| tqdm | 4.67.3 | 进度显示 |

### 环境安装

```bash
# 1. 创建并激活虚拟环境
conda create -n chemeng python=3.10
conda activate chemeng

# 2. 安装 PyTorch
pip install torch==2.0.1+cpu torchvision==0.15.2+cpu --index-url https://download.pytorch.org/whl/cpu

# 3. 安装依赖
pip install numpy==1.24.4 scikit-learn==1.3.2 pandas==2.3.3 rdkit==2026.3.1 tqdm==4.67.3

# 4. 安装 Chemprop 1.6.1
pip install chemprop==1.6.1

# 5. 验证环境
python check_env.py
```

## 🚀 使用方法

### 完整流程
```bash
python main.py
```

### 分步运行
```bash
# 1. 生成数据集
python generate_csv.py

# 2. 训练模型
python train.py

# 3. 验证预测功能
python predict.py
```

### 手动预测
```bash
python -m chemprop.train.make_predictions \
    --test_path data/predict_smiles.csv \
    --preds_path data/predictions.csv \
    --checkpoint_paths models/fold_0/model_0/model.pt \
    --num_workers 0 \
    --no_cuda
```

## 📊 模型性能

- **训练数据**：6个分子的多任务数据
- **验证指标**：RMSE = 0.530701
- **训练轮次**：10 epochs
- **模型架构**：MPN (Message Passing Neural Network)

## 🎯 应用场景

- **催化剂设计**：预测新分子的催化活性
- **材料筛选**：快速评估分子性质
- **虚拟筛选**：高通量预测
- **学术研究**：分子结构-性质关系分析

## 📝 注意事项

- 本项目使用 CPU 模式运行（`--no_cuda`）
- 训练数据为示例数据，实际应用需要扩充
- 模型性能会随数据集规模和质量提升

## 📄 许可证

MIT License

## 🔗 参考资料

- [Chemprop GitHub Repository](https://github.com/chemprop/chemprop)
- [PyTorch Documentation](https://pytorch.org/docs/stable/)
- [RDKit Documentation](https://www.rdkit.org/docs/)
