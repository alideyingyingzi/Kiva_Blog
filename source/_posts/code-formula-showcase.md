---
title: 代码与公式展示
date: 2024-03-05 00:00:00
categories: 技术
tags: [代码，数学公式，展示]
location: 上海
---

# 代码与公式展示

这是一个用于展示代码片段和数学公式的页面，使用安知鱼主题自带的代码高亮样式。

<!-- 引入 Font Awesome 图标库 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- 引入 MathJax 用于渲染数学公式 -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- 数学公式渲染脚本 -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const formulaSection = document.querySelector('.math-formula-section');
    if (formulaSection && window.MathJax && MathJax.typesetPromise) {
      setTimeout(() => {
        MathJax.typesetPromise([formulaSection]).then(() => {
          console.log('数学公式渲染完成');
        }).catch(err => console.log('数学公式渲染失败:', err));
      }, 500);
    }
    
    // 添加平滑滚动效果
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          // 计算目标位置并平滑滚动
          const offsetTop = targetElement.offsetTop - 100; // 减去头部导航的高度
          window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
          });
          
          // 更新 URL hash（但不立即跳转）
          history.pushState(null, null, targetId);
        }
      });
    });
  });
</script>

## 代码示例

### Python - 快速排序

```python
# Python 示例：快速排序算法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### C++ - 矩阵乘法

```cpp
#include <iostream>
#include <vector>

using namespace std;

// 矩阵乘法
vector<vector<int>> matrixMultiply(
    const vector<vector<int>>& A,
    const vector<vector<int>>& B
) {
    int n = A.size();
    int m = B[0].size();
    int k = B.size();
    vector<vector<int>> C(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int p = 0; p < k; ++p) {
                C[i][j] += A[i][p] * B[p][j];
            }
        }
    }
    return C;
}
```

### Python - 机器学习

```python
# 机器学习示例：线性回归
import numpy as np

class LinearRegression:
    """线性回归模型"""
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        """训练模型"""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X):
        """预测"""
        return np.dot(X, self.weights) + self.bias
```

<!-- 数学公式展示区域 -->
<div class="math-formula-section">
  <h3><i class="fas fa-square-root-variable"></i> 数学公式示例</h3>
  
  <div class="formula-item" id="formula-inline">
    <h4>行内公式</h4>
    <p>爱因斯坦的质能方程：$E = mc^2$，其中 $E$ 是能量，$m$ 是质量，$c$ 是光速。</p>
  </div>
  
  <div class="formula-item" id="formula-gaussian">
    <h4>高斯积分</h4>
    <div class="formula-display">
      $$
      \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
      $$
    </div>
  </div>
  
  <div class="formula-item" id="formula-matrix">
    <h4>矩阵表示</h4>
    <div class="formula-display">
      $$
      \mathbf{A} = \begin{pmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} \\
      a_{21} & a_{22} & \cdots & a_{2n} \\
      \vdots & \vdots & \ddots & \vdots \\
      a_{m1} & a_{m2} & \cdots & a_{mn}
      \end{pmatrix}
      $$
    </div>
  </div>
  
  <div class="formula-item" id="formula-heat">
    <h4>热传导方程</h4>
    <div class="formula-display">
      $$
      \frac{\partial u}{\partial t} = \alpha \nabla^2 u
      $$
    </div>
  </div>
  
  <div class="formula-item" id="formula-normal">
    <h4>正态分布</h4>
    <div class="formula-display">
      $$
      f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
      $$
    </div>
  </div>
  
  <div class="formula-item" id="formula-loss">
    <h4>线性回归损失函数</h4>
    <div class="formula-display">
      $$
      J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
      $$
    </div>
    <p class="formula-note">对应上面 Python 代码中的损失函数</p>
  </div>
</div>

<!-- 公式导航目录 -->
<div class="formula-toc">
  <h3><i class="fas fa-list"></i> 公式导航</h3>
  <ul>
    <li><a href="#formula-inline">行内公式</a></li>
    <li><a href="#formula-gaussian">高斯积分</a></li>
    <li><a href="#formula-matrix">矩阵表示</a></li>
    <li><a href="#formula-heat">热传导方程</a></li>
    <li><a href="#formula-normal">正态分布</a></li>
    <li><a href="#formula-loss">线性回归损失函数</a></li>
  </ul>
</div>

<style>
/* 数学公式区域 */
.math-formula-section {
  margin: 30px 0;
  padding: 30px;
  background: var(--anzhiyu-card-bg, #fff);
  border-radius: 12px;
}

.math-formula-section h3 {
  margin: 0 0 25px 0;
  font-size: 20px;
  color: var(--text-highlight-color, #1a1a1a);
  display: flex;
  align-items: center;
  gap: 10px;
}

.math-formula-section h3 i {
  color: var(--anzhiyu-main, #409EFF);
}

.formula-item {
  margin: 25px 0;
}

.formula-item h4 {
  margin: 0 0 12px 0;
  font-size: 16px;
  color: var(--anzhiyu-main, #409EFF);
  font-weight: 600;
}

.formula-item p {
  margin: 0;
  line-height: 1.8;
}

.formula-display {
  padding: 15px;
  overflow-x: auto;
  text-align: center;
  margin: 12px 0;
}

.formula-note {
  margin-top: 10px;
  font-size: 13px;
  color: var(--font-color, #666);
  font-style: italic;
}

/* 确保数学公式不被代码样式影响 */
.math-formula-section pre,
.math-formula-section code {
  background: transparent !important;
  color: inherit !important;
  font-family: inherit !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* 数学公式颜色 */
.math-formula-section mjx-container {
  color: #000 !important;
}

/* 公式导航目录 */
.formula-toc {
  margin: 30px 0;
  padding: 25px;
  background: var(--anzhiyu-card-bg, #fff);
  border-radius: 12px;
  border-left: 4px solid var(--anzhiyu-main, #409EFF);
}

.formula-toc h3 {
  margin: 0 0 15px 0;
  font-size: 18px;
  color: var(--text-highlight-color, #1a1a1a);
  display: flex;
  align-items: center;
  gap: 10px;
}

.formula-toc h3 i {
  color: var(--anzhiyu-main, #409EFF);
}

.formula-toc ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.formula-toc li {
  margin: 8px 0;
}

.formula-toc li a {
  color: var(--anzhiyu-main, #409EFF);
  text-decoration: none;
  padding: 6px 12px;
  display: block;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.formula-toc li a:hover {
  background: var(--anzhiyu-main, #409EFF);
  color: #fff;
  transform: translateX(5px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .math-formula-section {
    padding: 20px;
  }
  
  .formula-toc {
    padding: 15px;
  }
  
  .formula-toc h3 {
    font-size: 16px;
  }
}
</style>

## 使用说明

### 代码展示

页面使用**安知鱼主题自带的代码高亮**，支持：

- ✅ **语法高亮** - 使用主题配置的 `mac` 风格
- ✅ **多语言支持** - Python、C++、Java、JavaScript 等
- ✅ **复制按钮** - 一键复制代码
- ✅ **语言标识** - 显示代码语言
- ✅ **代码折叠** - 可折叠代码块
- ✅ **高度限制** - 超过限制自动折叠


### 公式导航

页面提供了**公式导航目录**，点击可以快速跳转到对应的公式位置。

### 添加代码块

使用 Markdown 标准语法：

````markdown
```python
# Python 代码示例
def hello():
    print("Hello World")
```
````

### 主题配置

在主题配置文件中修改代码块样式（`themes/hexo-theme-anzhiyu-dev/_config.yml`）：

```yaml
highlight_theme: mac # darker / pale night / light / ocean / mac / mac light / false
highlight_copy: true # 复制按钮
highlight_lang: true # 语言标识
highlight_shrink: false # 代码折叠
highlight_height_limit: 330 # 高度限制（px）
code_word_wrap: false # 自动换行
```
