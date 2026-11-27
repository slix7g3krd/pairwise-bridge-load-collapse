# pairwise-bridge-load-collapse

## 领域

游戏、图形与多媒体

## 主题

沙盒桥梁承重与坍塌结算

## 说明

应力迭代收敛、载荷接触回溯、结构版本快照。

初始状态下 `game/bridge_load.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
