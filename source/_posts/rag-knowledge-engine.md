---
title: RAG 知识引擎
date: 2024-03-05 00:00:00
categories: 技术
tags: [RAG, 知识引擎，AI, 大模型]
cover: /images/tinyBlocks_1.1update.png
location: 上海
---

# RAG 知识引擎

欢迎使用 RAG 知识搜索引擎！请选择知识领域并输入您的问题。

<!-- Import marked.js for Markdown rendering -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

<div class="rag-container">

## 选择知识领域

<div class="knowledge-selector">
  <div class="selector-header">
    <button id="config-btn" class="config-btn">
      <i class="fas fa-cog"></i>
      API 配置
    </button>
  </div>
  <div class="selector-buttons">
    <button class="knowledge-btn active" data-type="abaqus">
      <i class="fas fa-cube"></i>
      <span>ABAQUS</span>
    </button>
    <button class="knowledge-btn" data-type="comsol">
      <i class="fas fa-wave-square"></i>
      <span>COMSOL</span>
    </button>
    <button class="knowledge-btn" data-type="starccm">
      <i class="fas fa-wind"></i>
      <span>Star-CCM+</span>
    </button>
    <button class="knowledge-btn" data-type="ansys">
      <i class="fas fa-tools"></i>
      <span>ANSYS</span>
    </button>
    <button class="knowledge-btn" data-type="cpp">
      <i class="fas fa-code"></i>
      <span>C++ 编程</span>
    </button>
    <button class="knowledge-btn" data-type="python">
      <i class="fab fa-python"></i>
      <span>Python 编程</span>
    </button>
    <button class="knowledge-btn" data-type="subroutine">
      <i class="fas fa-microchip"></i>
      <span>子程序开发</span>
    </button>
    <button class="knowledge-btn" data-type="llm">
      <i class="fas fa-brain"></i>
      <span>大模型开发</span>
    </button>
  </div>
</div>

<div id="config-modal" class="modal">
  <div class="modal-content">
    <div class="modal-header">
      <h3><i class="fas fa-cog"></i> API 配置</h3>
      <button class="close-btn" onclick="closeConfigModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="config-section">
        <h4>模型选择</h4>
        <div class="input-group">
          <label>选择模型:</label>
          <select id="model-select" style="width: 100%; padding: 10px; border-radius: 6px; border: 2px solid var(--anzhiyu-border-color, #e0e0e0); background: #fff; color: #333; font-size: 14px;" disabled>
            <option value="qwen-plus" selected>Qwen-Plus (固定使用)</option>
          </select>
          <small>统一使用 Qwen-Plus 模型，确保回答质量和速度的平衡</small>
        </div>
      </div>
      <div class="config-section">
        <h4>API 密钥</h4>
        <div class="input-group">
          <label>Qwen API Key:</label>
          <input type="password" id="qwen-api-key" placeholder="请输入通义千问 API 密钥" autocomplete="off">
          <small>获取地址：<a href="https://bailian.console.aliyun.com/" target="_blank">阿里云百炼平台</a></small>
        </div>
      </div>
      <div class="config-section">
        <h4>模型参数</h4>
        <div class="input-group">
          <label>Temperature:</label>
          <input type="number" id="temperature" min="0" max="2" step="0.1" value="0.7">
          <small>控制随机性 (0-2)，越大越随机</small>
        </div>
        <div class="input-group">
          <label>Top K:</label>
          <input type="number" id="top-k" min="1" max="10" value="5">
          <small>检索相关文档数量</small>
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="save-btn" onclick="saveConfig()">
        <i class="fas fa-save"></i>
        保存配置
      </button>
      <button class="test-btn" onclick="testConnection()">
        <i class="fas fa-plug"></i>
        测试连接
      </button>
    </div>
  </div>
</div>

## 输入问题

<div class="search-container">
  <div class="search-box">
    <textarea id="question-input" class="question-input" placeholder="请输入您的问题，例如：如何在 ABAQUS 中创建用户自定义单元？" rows="4"></textarea>
    <div class="search-actions">
      <span class="search-info">模型：<strong id="current-model-info">Qwen-Flash</strong> | Top K: <strong id="current-topk-info">5</strong></span>
      <button id="search-btn" class="search-btn">
        <i class="fas fa-search"></i>
        搜索答案
      </button>
    </div>
  </div>
</div>

## 搜索结果

<div id="result-container" class="result-container">
  <div class="result-placeholder">
    <i class="fas fa-lightbulb"></i>
    <p>选择知识领域并输入问题，点击搜索按钮获取答案</p>
  </div>
</div>

## 搜索历史

<div id="history-container" class="history-container">
  <div class="history-header">
    <h3>最近搜索</h3>
    <button id="clear-history" class="clear-history-btn">清空历史</button>
  </div>
  <div id="history-list" class="history-list">
    <p class="history-empty">暂无搜索历史</p>
  </div>
</div>

</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
.rag-container {
  margin: 20px 0;
}

.knowledge-selector {
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: var(--anzhiyu-shadow);
}

.selector-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-highlight-color);
}

.config-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: var(--anzhiyu-main);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.config-btn:hover {
  background: var(--anzhiyu-main-light, var(--anzhiyu-main));
  transform: translateY(-2px);
}

.selector-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.knowledge-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  color: var(--font-color);
  transition: all 0.3s ease;
}

.knowledge-btn:hover {
  background: var(--anzhiyu-main);
  color: white;
  transform: translateY(-2px);
}

.knowledge-btn.active {
  background: var(--anzhiyu-main);
  color: white;
  border-color: var(--anzhiyu-main);
}

.knowledge-btn i {
  font-size: 16px;
}

.modal {
  display: none;
  position: fixed;
  z-index: 9999;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal.show {
  display: flex !important;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid var(--anzhiyu-border-color, #e0e0e0);
}

.modal-header h3 {
  margin: 0;
  font-size: 18px;
  color: var(--text-highlight-color);
}

.close-btn {
  background: none;
  border: none;
  font-size: 28px;
  color: var(--light-grey, #999);
  cursor: pointer;
}

.close-btn:hover {
  color: var(--text-highlight-color);
}

.modal-body {
  padding: 20px;
}

.config-section {
  margin-bottom: 25px;
}

.config-section h4 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-highlight-color);
  margin-bottom: 15px;
}

.radio-group {
  display: flex;
  gap: 20px;
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 14px;
  color: var(--font-color);
}

.radio-label input[type="radio"] {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  font-size: 13px;
  font-weight: 500;
  color: var(--font-color);
  margin-bottom: 8px;
}

.input-group input {
  width: 100%;
  padding: 10px 12px;
  border: 2px solid var(--anzhiyu-border-color, #e0e0e0);
  border-radius: 6px;
  font-size: 14px;
  background: #fff;
  color: #333;
  box-sizing: border-box;
}

.input-group input:focus {
  outline: none;
  border-color: var(--anzhiyu-main);
}

.input-group small {
  display: block;
  margin-top: 5px;
  font-size: 11px;
  color: var(--light-grey, #999);
}

.modal-footer {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  padding: 20px;
  border-top: 1px solid var(--anzhiyu-border-color, #e0e0e0);
}

.save-btn, .test-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.save-btn {
  background: var(--anzhiyu-main);
  color: white;
}

.save-btn:hover {
  background: var(--anzhiyu-main-light, var(--anzhiyu-main));
  transform: translateY(-2px);
}

.test-btn {
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  color: var(--font-color);
  border: 2px solid var(--anzhiyu-border-color, #e0e0e0);
}

.test-btn:hover {
  background: var(--anzhiyu-main);
  color: white;
  border-color: var(--anzhiyu-main);
}

.search-container {
  margin: 20px 0;
}

.search-box {
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  padding: 20px;
  box-shadow: var(--anzhiyu-shadow);
}

.question-input {
  width: 100%;
  padding: 15px;
  border: 2px solid var(--anzhiyu-border-color, #e0e0e0);
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
  resize: vertical;
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  color: #333 !important;
  box-sizing: border-box;
}

.question-input:focus {
  outline: none;
  border-color: var(--anzhiyu-main);
}

.search-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  gap: 10px;
}

.search-info {
  font-size: 13px;
  color: var(--light-grey, #999);
}

.search-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  background: var(--anzhiyu-main);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.search-btn:hover {
  background: var(--anzhiyu-main-light, var(--anzhiyu-main));
  transform: translateY(-2px);
}

.search-btn:disabled {
  background: var(--light-grey, #999);
  cursor: not-allowed;
  transform: none;
}

.search-btn.loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  top: 50%;
  left: 50%;
  margin-top: -8px;
  margin-left: -8px;
  border: 2px solid transparent;
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.result-container {
  margin: 20px 0;
}

.result-placeholder {
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  padding: 60px 20px;
  text-align: center;
  box-shadow: var(--anzhiyu-shadow);
}

.result-placeholder i {
  font-size: 48px;
  color: var(--anzhiyu-main);
  margin-bottom: 20px;
  opacity: 0.5;
}

.result-placeholder p {
  color: var(--light-grey, #999);
  font-size: 14px;
}

.result-content {
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  padding: 25px;
  box-shadow: var(--anzhiyu-shadow);
}

.result-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid var(--anzhiyu-border-color, #e0e0e0);
}

.result-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-highlight-color);
}

.result-meta {
  font-size: 12px;
  color: var(--light-grey, #999);
}

.result-body {
  font-size: 14px;
  line-height: 1.8;
  color: var(--font-color);
  white-space: pre-wrap;
}

.sources-section {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid var(--anzhiyu-border-color, #e0e0e0);
}

.sources-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-highlight-color);
  margin-bottom: 10px;
}

.source-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  border-radius: 6px;
  margin-bottom: 8px;
  font-size: 13px;
  color: var(--font-color);
}

.source-item i {
  color: var(--anzhiyu-main);
}

.history-container {
  margin: 20px 0;
  background: var(--anzhiyu-card-bg);
  border-radius: 12px;
  padding: 20px;
  box-shadow: var(--anzhiyu-shadow);
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.history-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-highlight-color);
  margin: 0;
}

.clear-history-btn {
  padding: 6px 12px;
  background: transparent;
  border: 1px solid var(--anzhiyu-border-color, #e0e0e0);
  border-radius: 6px;
  font-size: 12px;
  color: var(--font-color);
  cursor: pointer;
}

.clear-history-btn:hover {
  background: var(--anzhiyu-main);
  color: white;
  border-color: var(--anzhiyu-main);
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.history-empty {
  text-align: center;
  color: var(--light-grey, #999);
  font-size: 13px;
  padding: 20px;
}

.history-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 15px;
  background: var(--anzhiyu-card-bg-secondary, #f5f5f5);
  border-radius: 8px;
  cursor: pointer;
}

.history-item:hover {
  background: var(--anzhiyu-main);
  color: white;
}

.history-item-content {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}

.history-item-icon {
  color: var(--anzhiyu-main);
}

.history-item:hover .history-item-icon {
  color: white;
}

.history-item-text {
  font-size: 13px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.history-item-time {
  font-size: 11px;
  color: var(--light-grey, #999);
  white-space: nowrap;
}

.history-item:hover .history-item-time {
  color: rgba(255, 255, 255, 0.8);
}

.error-message {
  background: #fee;
  border: 1px solid #fcc;
  border-radius: 8px;
  padding: 15px;
  color: #c33;
  font-size: 14px;
}

.test-result {
  margin-top: 10px;
  padding: 10px;
  border-radius: 6px;
  font-size: 13px;
}

.test-result.success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.test-result.error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Markdown rendering styles */
.markdown-body {
  font-size: 14px;
  line-height: 1.6;
  color: var(--font-color, #333);
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
  margin-top: 24px;
  margin-bottom: 16px;
  font-weight: 600;
  line-height: 1.25;
  color: var(--text-highlight-color, #1a1a1a);
}

.markdown-body h1 {
  font-size: 24px;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--anzhiyu-border-color, #eaecef);
}

.markdown-body h2 {
  font-size: 20px;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--anzhiyu-border-color, #eaecef);
}

.markdown-body h3 {
  font-size: 16px;
}

.markdown-body p {
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-body strong {
  font-weight: 600;
  color: var(--anzhiyu-main, #409EFF);
}

.markdown-body code {
  padding: 0.2em 0.4em;
  margin: 0;
  font-size: 85%;
  background-color: var(--anzhiyu-card-bg-secondary, #f6f8fa);
  border-radius: 6px;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  color: var(--font-color, #24292e);
}

.markdown-body pre {
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: var(--anzhiyu-card-bg-secondary, #f6f8fa);
  border-radius: 6px;
}

.markdown-body pre code {
  display: inline;
  max-width: auto;
  overflow: visible;
  line-height: inherit;
  padding: 0;
  margin: 0;
  font-size: 13px;
  word-break: normal;
  white-space: pre;
  background: transparent;
  border: 0;
}

.markdown-body ul,
.markdown-body ol {
  padding-left: 2em;
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-body li {
  margin-top: 0.25em;
}

.markdown-body li + li {
  margin-top: 0.25em;
}

.markdown-body blockquote {
  padding: 0 1em;
  color: var(--light-grey, #6a737d);
  border-left: 0.25em solid var(--anzhiyu-main, #409EFF);
  margin: 0 0 16px 0;
}

.markdown-body table {
  display: block;
  width: 100%;
  overflow: auto;
  border-spacing: 0;
  border-collapse: collapse;
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-body table th,
.markdown-body table td {
  padding: 6px 13px;
  border: 1px solid var(--anzhiyu-border-color, #dfe2e5);
}

.markdown-body table tr {
  background-color: var(--anzhiyu-card-bg, #fff);
  border-top: 1px solid var(--anzhiyu-border-color, #c6cbd1);
}

.markdown-body table tr:nth-child(2n) {
  background-color: var(--anzhiyu-card-bg-secondary, #f6f8fa);
}

.markdown-body hr {
  height: 0.25em;
  padding: 0;
  margin: 24px 0;
  background-color: var(--anzhiyu-border-color, #e1e4e8);
  border: 0;
}

.markdown-body a {
  color: var(--anzhiyu-main, #0366d6);
  text-decoration: none;
}

.markdown-body a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .knowledge-btn {
    flex: 1 1 calc(50% - 10px);
    justify-content: center;
  }
  
  .search-actions {
    flex-direction: column;
  }
  
  .search-info {
    text-align: center;
  }
  
  .search-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>

<script>
(function() {
  let selectedKnowledgeType = 'abaqus';
  let searchHistory = [];
  let apiConfig = {
    qwenApiKey: '',
    model: 'qwen-plus',
    temperature: 0.5,
    topK: 5
  };

  function init() {
    const buttons = document.querySelectorAll('.knowledge-btn');
    buttons.forEach(btn => {
      btn.addEventListener('click', function() {
        buttons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        selectedKnowledgeType = this.dataset.type;
        console.log('Selected:', selectedKnowledgeType);
      });
    });

    const configBtn = document.getElementById('config-btn');
    if (configBtn) {
      configBtn.addEventListener('click', openConfigModal);
    }

    const searchBtn = document.getElementById('search-btn');
    if (searchBtn) {
      searchBtn.addEventListener('click', performSearch);
    }

    const questionInput = document.getElementById('question-input');
    if (questionInput) {
      questionInput.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
          performSearch();
        }
      });
    }

    const clearBtn = document.getElementById('clear-history');
    if (clearBtn) {
      clearBtn.addEventListener('click', clearHistory);
    }

    loadConfig();
    loadHistory();
    updateModelInfo();
  }

  function openConfigModal() {
    const modal = document.getElementById('config-modal');
    if (modal) {
      modal.classList.add('show');
      loadConfigToForm();
    }
  }

  function closeConfigModal() {
    const modal = document.getElementById('config-modal');
    if (modal) {
      modal.classList.remove('show');
    }
  }

  window.onclick = function(event) {
    const modal = document.getElementById('config-modal');
    if (event.target === modal) {
      closeConfigModal();
    }
  }

  function loadConfigToForm() {
    document.getElementById('qwen-api-key').value = apiConfig.qwenApiKey || '';
    document.getElementById('model-select').value = apiConfig.model || 'qwen-flash';
    document.getElementById('temperature').value = apiConfig.temperature || 0.7;
    document.getElementById('top-k').value = apiConfig.topK || 5;
  }

  function saveConfig() {
    apiConfig.qwenApiKey = document.getElementById('qwen-api-key').value.trim();
    apiConfig.model = document.getElementById('model-select').value.trim();
    apiConfig.temperature = parseFloat(document.getElementById('temperature').value) || 0.7;
    apiConfig.topK = parseInt(document.getElementById('top-k').value) || 5;
    localStorage.setItem('rag_api_config', JSON.stringify(apiConfig));
    updateModelInfo();
    alert('配置已保存！');
    closeConfigModal();
  }

  function loadConfig() {
    const saved = localStorage.getItem('rag_api_config');
    if (saved) {
      try {
        apiConfig = JSON.parse(saved);
      } catch (e) {
        console.error('Load config failed:', e);
      }
    }
  }

  function updateModelInfo() {
    const topkInfo = document.getElementById('current-topk-info');
    const modelInfo = document.getElementById('current-model-info');
    if (topkInfo) {
      topkInfo.textContent = apiConfig.topK;
    }
    if (modelInfo) {
      const modelNames = { 'qwen-flash': 'Qwen-Flash(快)', 'qwen-plus': 'Qwen-Plus', 'qwen-max': 'Qwen-Max' };
      modelInfo.textContent = modelNames[apiConfig.model] || 'Qwen';
    }
  }

  async function testConnection() {
    const testBtn = document.querySelector('.test-btn');
    let testResult = document.getElementById('test-result');
    if (!testResult) {
      testResult = document.createElement('div');
      testResult.id = 'test-result';
      testResult.className = 'test-result';
      document.querySelector('.modal-footer').parentNode.insertBefore(testResult, document.querySelector('.modal-footer'));
    }
    testBtn.disabled = true;
    testBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 测试中...';
    if (!apiConfig.qwenApiKey) {
      testResult.className = 'test-result error';
      testResult.innerHTML = '<i class="fas fa-exclamation-circle"></i> 请先输入 API Key';
      testBtn.disabled = false;
      testBtn.innerHTML = '<i class="fas fa-plug"></i> 测试连接';
      return;
    }
    try {
      const response = await fetch('https://dashscope.aliyuncs.com/compatible-mode/v1/models', {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + apiConfig.qwenApiKey
        }
      });
      if (response.ok) {
        testResult.className = 'test-result success';
        testResult.innerHTML = '<i class="fas fa-check-circle"></i> API Key 验证成功！';
      } else {
        const error = await response.json();
        testResult.className = 'test-result error';
        testResult.innerHTML = '<i class="fas fa-exclamation-circle"></i> API Key 无效：' + (error.message || '请检查 API Key 是否正确');
      }
    } catch (error) {
      testResult.className = 'test-result error';
      testResult.innerHTML = '<i class="fas fa-exclamation-circle"></i> 测试失败：' + error.message;
    }
    testBtn.disabled = false;
    testBtn.innerHTML = '<i class="fas fa-plug"></i> 测试连接';
  }

  async function performSearch() {
    const questionInput = document.getElementById('question-input');
    const searchBtn = document.getElementById('search-btn');
    const question = questionInput.value.trim();
    if (!question) {
      alert('请输入您的问题');
      return;
    }
    if (!apiConfig.qwenApiKey) {
      alert('请先配置 API 密钥！点击右上角"API 配置"进行设置。');
      openConfigModal();
      return;
    }
    searchBtn.classList.add('loading');
    searchBtn.disabled = true;
    const resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = '<div class="result-placeholder"><i class="fas fa-spinner fa-spin"></i><p>正在调用大模型生成答案...</p></div>';
    try {
      const response = await callQwenAPI(question, selectedKnowledgeType);
      displayResult(response);
      addToHistory(question, selectedKnowledgeType);
    } catch (error) {
      resultContainer.innerHTML = '<div class="error-message"><i class="fas fa-exclamation-circle"></i> 搜索失败：' + error.message + '</div>';
    } finally {
      searchBtn.classList.remove('loading');
      searchBtn.disabled = false;
    }
  }

  async function callQwenAPI(question, type) {
    const promptTemplates = {
      abaqus: `【角色】你是 ABAQUS 有限元分析专家
【任务】针对用户问题提供简洁精准的技术解答
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接给出操作步骤或解决方案
3. 提供必要的命令或代码（如果有）

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁专业的解答，直接给出步骤，不要废话]

【用户问题】{question}

请简洁回答，直接给出操作步骤。`,
      
      comsol: `【角色】你是 COMSOL Multiphysics 多物理场仿真专家
【任务】针对用户问题提供简洁精准的建模指导
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接说明建模步骤
3. 给出关键参数设置（如果有）

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁专业的解答，直接给出步骤]

【用户问题】{question}

请简洁回答，直接给出操作步骤。`,
      
      starccm: `【角色】你是 Star-CCM+ 计算流体力学专家
【任务】针对用户问题提供简洁精准的 CFD 指导
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接说明设置步骤
3. 给出关键参数（如果有）

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁专业的解答，直接给出步骤]

【用户问题】{question}

请简洁回答，直接给出操作步骤。`,
      
      ansys: `【角色】你是 ANSYS 仿真分析专家
【任务】针对用户问题提供简洁精准的仿真指导
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接说明操作步骤
3. 给出关键参数（如果有）

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁专业的解答，直接给出步骤]

【用户问题】{question}

请简洁回答，直接给出操作步骤。`,
      
      cpp: `【角色】你是 C++ 高级开发工程师
【任务】针对用户问题提供简洁的代码解决方案
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接给出代码示例
3. 简要说明关键点

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁的解答，直接给代码]

【用户问题】{question}

请简洁回答，直接给出代码。`,
      
      python: `【角色】你是 Python 高级开发工程师
【任务】针对用户问题提供简洁的代码解决方案
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接给出代码示例
3. 简要说明关键点

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁的解答，直接给代码]

【用户问题】{question}

请简洁回答，直接给出代码。`,
      
      subroutine: `【角色】你是 CAE 二次开发专家，精通 FORTRAN 和子程序开发
【任务】针对用户问题提供简洁的子程序实现方案
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接给出子程序代码
3. 说明关键参数

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁的解答，直接给代码]

【用户问题】{question}

请简洁回答，直接给出代码。`,
      
      llm: `【角色】你是大模型开发专家
【任务】针对用户问题提供简洁的技术方案
【要求】
1. **严格从用户问题原文中提取 1-5 个关键词**（只能使用问题中实际出现的词汇）
2. 直接给出实现方案或代码
3. 简要说明关键点

【输出格式】
**关键词**：[仅列出用户问题中的原词]
**解答**：[简洁的解答，直接给方案或代码]

【用户问题】{question}

请简洁回答，直接给出方案或代码。`
    };
    
    // 构建系统提示
    const systemPrompt = '你是专业的 AI 助手，专注于仿真软件和编程开发领域。回答要：\n1. **严格从用户问题原文中提取关键词，只能使用问题中的原词**\n2. 简洁直接，不要废话\n3. 直接给出步骤或代码\n4. 不要添加"常见错误"、"注意事项"等额外内容';
    
    // 替换模板中的占位符
    const userPrompt = promptTemplates[type]?.replace('{question}', question) || promptTemplates.abaqus.replace('{question}', question);
    
    const response = await fetch('https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + apiConfig.qwenApiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'qwen-plus', // 固定使用 qwen-plus
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt }
        ],
        temperature: 0.5, // 降低随机性，提高准确性
        top_p: 0.8,
        max_tokens: 2000 // 限制最大长度，加快响应
      })
    });
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.message || errorData.error?.message || 'API 请求失败 (' + response.status + ')');
    }
    
    const data = await response.json();
    if (!data.choices || !data.choices[0] || !data.choices[0].message) {
      throw new Error('API 返回数据格式异常');
    }
    
    return {
      answer: data.choices[0].message.content,
      sources: ['通义千问 (Qwen-Plus)'],
      question: question,
      type: type,
      model: 'Qwen-Plus',
      timestamp: new Date().toISOString()
    };
  }

  function displayResult(response) {
    const resultContainer = document.getElementById('result-container');
    const sourcesHtml = response.sources.map(s => '<div class="source-item"><i class="fas fa-file-alt"></i> ' + s + '</div>').join('');
    
    // Use marked.js to render Markdown
    const renderedAnswer = marked.parse(response.answer);
    
    resultContainer.innerHTML = '<div class="result-content"><div class="result-header"><span class="result-title">搜索结果</span><span class="result-meta">' + response.type + ' | ' + response.model + ' | ' + new Date(response.timestamp).toLocaleString() + '</span></div><div class="result-body markdown-body">' + renderedAnswer + '</div><div class="sources-section"><div class="sources-title"><i class="fas fa-database"></i> 参考资料</div>' + sourcesHtml + '</div></div>';
  }

  function addToHistory(question, type) {
    const historyItem = { question: question, type: type, time: new Date().toLocaleString() };
    searchHistory.unshift(historyItem);
    if (searchHistory.length > 10) {
      searchHistory = searchHistory.slice(0, 10);
    }
    localStorage.setItem('rag_search_history', JSON.stringify(searchHistory));
    renderHistory();
  }

  function loadHistory() {
    const saved = localStorage.getItem('rag_search_history');
    if (saved) {
      searchHistory = JSON.parse(saved);
      renderHistory();
    }
  }

  function renderHistory() {
    const historyList = document.getElementById('history-list');
    if (!historyList) return;
    if (searchHistory.length === 0) {
      historyList.innerHTML = '<p class="history-empty">暂无搜索历史</p>';
      return;
    }
    const typeNames = { abaqus: 'ABAQUS', comsol: 'COMSOL', starccm: 'Star-CCM+', ansys: 'ANSYS', cpp: 'C++', python: 'Python', subroutine: '子程序', llm: '大模型' };
    historyList.innerHTML = searchHistory.map((item, i) => '<div class="history-item" onclick="repeatSearch(' + i + ')"><div class="history-item-content"><i class="fas fa-history history-item-icon"></i><span class="history-item-text">' + item.question + '</span></div><span class="history-item-time">' + (typeNames[item.type] || item.type) + '</span></div>').join('');
  }

  window.repeatSearch = function(index) {
    const item = searchHistory[index];
    document.getElementById('question-input').value = item.question;
    const buttons = document.querySelectorAll('.knowledge-btn');
    buttons.forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.type === item.type) {
        btn.classList.add('active');
      }
    });
    selectedKnowledgeType = item.type;
    performSearch();
  }

  function clearHistory() {
    searchHistory = [];
    localStorage.removeItem('rag_search_history');
    renderHistory();
  }

  window.saveConfig = saveConfig;
  window.closeConfigModal = closeConfigModal;
  window.testConnection = testConnection;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>

## 支持的知识领域

| 领域 | 说明 | 适用场景 |
|------|------|----------|
| ABAQUS | 有限元分析软件 | 结构仿真、非线性分析、子程序开发 |
| COMSOL | 多物理场仿真 | 多物理场耦合建模、参数分析 |
| Star-CCM+ | CFD 流体仿真 | 流体动力学、传热仿真 |
| ANSYS | 综合仿真平台 | 结构、热、流体仿真 |
| C++ | 编程语言 | 高性能计算、软件开发 |
| Python | 编程语言 | 数据科学、自动化、脚本开发 |
| 子程序开发 | CAE 二次开发 | UMAT、UEL、API 开发 |
| 大模型开发 | AI 开发技术 | Prompt、RAG、Agent 开发 |

## 使用说明

1. **选择知识领域**：点击上方的领域按钮
2. **配置 API**：点击右上角"API 配置"，输入 API 密钥
3. **输入问题**：在文本框中输入您的问题
4. **获取答案**：点击搜索按钮

## 注意事项

<div class="notice-box" style="background: #e7f3ff; border: 1px solid #2196f3; border-radius: 8px; padding: 15px; margin: 20px 0;">
  <p style="margin: 0; color: #0d47a1; font-size: 14px;">
    <i class="fas fa-info-circle"></i> 
    <strong>当前状态：直连大模型模式</strong><br>
    系统直接调用通义千问 (Qwen) 大模型 API，无需后端服务。<br>
    每个知识领域都有专门的 Prompt 模板，确保回答的专业性。
  </p>
</div>
