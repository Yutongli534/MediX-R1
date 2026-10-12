# MediX-R1

医疗多模态助手（Medical VLM）项目代码：基于 verl 的复合奖励强化学习训练 + vLLM 评测流水线。

本仓库仅包含代码部分：

| 目录 | 内容 |
|------|------|
| `training/` | 训练代码（verl 框架，GRPO/DAPO/GSPO，复合奖励函数） |
| `eval/` | 评测流水线 v1（vLLM 生成 + LLM-as-judge + 分数聚合） |
| `eval2/` | 评测流水线 v2（含结果合并脚本） |

各目录下的 README 有详细安装与运行说明。

## 说明

- 训练数据：[MBZUAI/medix-rl-data](https://huggingface.co/datasets/MBZUAI/medix-rl-data)
- `config.py`（LLM judge 的 API 配置）不入库，请按 `training/examples/reward_function/medical.py` 中的 `LLM_CONFIG` 字段（`base_url` / `api_key` / `model_name`）自行创建
- `images/` 为训练曲线与训练报告，`eval2/results/`、`eval2/logs/` 为一次评测的产出记录
