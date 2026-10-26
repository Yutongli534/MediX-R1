# MediX-R1

医疗多模态助手代码：基于 verl 的复合奖励强化学习训练 + vLLM 评测流水线 + 多智能体应用层。

| 目录 | 内容 |
|------|------|
| `training/` | 训练代码（verl 框架，GRPO/DAPO/GSPO，复合奖励函数） |
| `eval/` | 评测流水线 v1（vLLM 生成 + LLM-as-judge + 分数聚合） |
| `eval2/` | 评测流水线 v2（含结果合并脚本） |
| `medix-agent-swarm/` | 多智能体应用层（Skills-Agent、Swarm、双层记忆、约束系统、Milvus RAG） |

各目录下的 README 有详细安装与运行说明。

## 多智能体应用层

`medix-agent-swarm/` 提供医疗问诊的多智能体编排：

- 9 个可自动发现的 Skills（知识库检索、风险评估、症状分析、ICD-10 编码、指南检索、深度研究等）
- 3 个专业 Agent（健康咨询 / 诊断推理 / 循证研究）与去中心化 Swarm 协作
- 短期会话记忆 + 长期 Mem0 记忆，带熵管理与去重
- YAML 约束校验与输出自动修复
- Milvus Lite 医学知识库（10 篇文档）

当前以文本问诊为主，尚未接入 `training/` 产出的 VLM 权重；影像工具是后续扩展点。

### 快速开始

```bash
cd medix-agent-swarm
pip install -r requirements.txt

# 在仓库根目录创建 config.py（模板见 config.example.py），填入 LLM / Mem0 key
cp ../config.example.py ../config.py

python knowledge/scripts/import_hardcoded_data.py
python main.py
```

`config.py` 不入库。首次运行会下载 `BAAI/bge-small-zh-v1.5` 嵌入模型。

## 说明

- 训练数据：[MBZUAI/medix-rl-data](https://huggingface.co/datasets/MBZUAI/medix-rl-data)
- `config.py` 不入库，请按 `config.example.py` 或 `training/examples/reward_function/medical.py` 中的字段自行创建
- `images/` 为训练曲线与训练报告，`eval2/results/`、`eval2/logs/` 为一次评测的产出记录
