---
title: PPT 风格图片轮播展示
date: 2026-03-16 12:00:00
categories: [技术]
tags: [前端, 轮播, PPT]
---

# PPT 风格图片轮播展示

这是一个类似 PPT 的图片轮播界面，你可以左右切换查看不同的图片。

<!-- 测试按钮 -->
<button onclick="alert('测试按钮可以点击！')" style="background: red; color: white; padding: 20px; font-size: 20px; margin: 20px;">测试按钮</button>

<!-- 轮播容器测试 -->
<div style="border: 2px solid blue; padding: 20px; margin: 20px;">
  <h3>轮播容器区域</h3>
  <p>如果能看到这个蓝色边框，说明轮播容器是可见的</p>
</div>

## 轮播展示

<div class="ppt-carousel">
<div class="ppt-container" onclick="handleContainerClick(event)">
<div class="ppt-slides">
<div class="ppt-slide active">
<img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=beautiful%20landscape%20mountain%20lake%20sunset&image_size=landscape_16_9" alt="风景图片 1">
<div class="ppt-caption">美丽的山水日落</div>
</div>
<div class="ppt-slide">
<img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=modern%20city%20skyline%20night%20lights&image_size=landscape_16_9" alt="城市夜景">
<div class="ppt-caption">现代城市夜景</div>
</div>
<div class="ppt-slide">
<img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=colorful%20autumn%20forest%20trees&image_size=landscape_16_9" alt="秋季森林">
<div class="ppt-caption">多彩的秋季森林</div>
</div>
<div class="ppt-slide">
<img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=ocean%20beach%20waves%20palm%20trees&image_size=landscape_16_9" alt="海滩风景">
<div class="ppt-caption">热带海滩风光</div>
</div>
</div>

<div class="ppt-click-areas">
<div class="ppt-click-left" onclick="plusSlides(-1)"></div>
<div class="ppt-click-right" onclick="plusSlides(1)"></div>
</div>

<button class="ppt-prev" onclick="plusSlides(-1)">
<span class="arrow-left"></span>
</button>
<button class="ppt-next" onclick="plusSlides(1)">
<span class="arrow-right"></span>
</button>

<div class="ppt-indicators">
<span class="ppt-dot active" onclick="currentSlide(1)"></span>
<span class="ppt-dot" onclick="currentSlide(2)"></span>
<span class="ppt-dot" onclick="currentSlide(3)"></span>
<span class="ppt-dot" onclick="currentSlide(4)"></span>
</div>
</div>
</div>

## 如何使用

1. 点击左右箭头切换图片
2. 点击底部的圆点直接跳转到对应图片
3. 图片会自动播放（每5秒切换一次）

## 技术实现

这个轮播使用了纯 HTML、CSS 和 JavaScript 实现，无需任何外部库。

### 特点
- 响应式设计，适配不同屏幕尺寸
- 平滑的过渡动画
- 自动播放功能
- 触摸支持（移动端可左右滑动）
- 支持键盘左右键控制

<style>
/* PPT 轮播样式 */
.ppt-carousel {
  margin: 20px 0;
  position: relative;
  max-width: 100%;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.ppt-container {
  position: relative;
  width: 100%;
  height: 500px;
  background: #f5f5f5;
}

.ppt-slides {
  display: flex;
  transition: transform 0.5s ease-in-out;
  height: 100%;
}

.ppt-slide {
  min-width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.ppt-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.ppt-slide:hover img {
  transform: scale(1.05);
}

.ppt-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 20px;
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  animation: fadeIn 0.5s ease;
}

.ppt-prev,
.ppt-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  width: 60px;
  height: 60px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.ppt-prev {
  left: 30px;
}

.ppt-next {
  right: 30px;
}

.ppt-prev:hover,
.ppt-next:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  animation: float 2s ease-in-out infinite;
  transform: translateY(-50%) scale(1.1);
}

/* 漂浮动画 */
@keyframes float {
  0% {
    transform: translateY(-50%) scale(1.1);
  }
  50% {
    transform: translateY(-60%) scale(1.1);
  }
  100% {
    transform: translateY(-50%) scale(1.1);
  }
}

.ppt-prev {
  left: 20px;
}

.ppt-next {
  right: 20px;
}

.ppt-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 10;
}

.ppt-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s ease;
}

.ppt-dot.active {
  background: rgba(255, 255, 255, 1);
  transform: scale(1.2);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .ppt-container {
    height: 300px;
  }
  
  .ppt-prev,
  .ppt-next {
    width: 40px;
    height: 40px;
    font-size: 20px;
  }
  
  .ppt-caption {
    font-size: 16px;
    padding: 15px;
  }
}

/* 动画效果 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 纯 CSS 箭头 */
.arrow-left,
.arrow-right {
  display: inline-block;
  width: 20px;
  height: 20px;
  border-top: 3px solid #ffffff;
  border-left: 3px solid #ffffff;
  margin: 0 5px;
}

.arrow-left {
  transform: rotate(-45deg);
}

.arrow-right {
  transform: rotate(135deg);
}

/* 箭头文字 */
.arrow-text {
  color: #ffffff;
  font-size: 14px;
  font-weight: bold;
  margin: 0 5px;
}

/* 响应式箭头 */
@media (max-width: 768px) {
  .arrow-left,
  .arrow-right {
    width: 16px;
    height: 16px;
    border-top-width: 2px;
    border-left-width: 2px;
  }
  
  .arrow-text {
    font-size: 12px;
  }
}

/* 点击区域 */
.ppt-click-areas {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 5;
  pointer-events: none;
}

.ppt-click-left,
.ppt-click-right {
  position: absolute;
  top: 0;
  height: 100%;
  width: 30%;
  cursor: pointer;
  pointer-events: auto;
  transition: all 0.3s ease;
}

.ppt-click-left {
  left: 0;
}

.ppt-click-right {
  right: 0;
}

.ppt-click-left:hover {
  background: linear-gradient(to right, rgba(255, 255, 255, 0.1), transparent);
}

.ppt-click-right:hover {
  background: linear-gradient(to left, rgba(255, 255, 255, 0.1), transparent);
}
</style>

<script>
// PPT 轮播脚本
let slideIndex = 1;
let slideInterval;

// 初始化轮播
function initCarousel() {
  showSlides(slideIndex);
  startAutoSlide();
  
  // 添加键盘控制
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
      plusSlides(-1);
    } else if (e.key === 'ArrowRight') {
      plusSlides(1);
    }
  });
  
  // 添加触摸支持
  let touchStartX = 0;
  let touchEndX = 0;
  
  document.querySelector('.ppt-container').addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
  }, false);
  
  document.querySelector('.ppt-container').addEventListener('touchend', function(e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, false);
  
  function handleSwipe() {
    if (touchEndX < touchStartX - 50) {
      plusSlides(1); // 向左滑动
    } else if (touchEndX > touchStartX + 50) {
      plusSlides(-1); // 向右滑动
    }
  }
}

// 切换幻灯片
function plusSlides(n) {
  showSlides(slideIndex += n);
  resetAutoSlide();
}

// 跳转到指定幻灯片
function currentSlide(n) {
  showSlides(slideIndex = n);
  resetAutoSlide();
}

// 显示幻灯片
function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("ppt-slide");
  let dots = document.getElementsByClassName("ppt-dot");
  
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  
  // 显示所有幻灯片（用于轮播切换）
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "flex";
  }
  
  // 移除所有指示器的 active 类
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  
  // 激活当前指示器
  dots[slideIndex - 1].className += " active";
  
  // 更新轮播位置
  document.querySelector('.ppt-slides').style.transform = `translateX(-${(slideIndex - 1) * 100}%)`;
  
  // 触发懒加载图片
  setTimeout(function() {
    let currentSlide = slides[slideIndex - 1];
    let img = currentSlide.querySelector('img');
    if (img && img.getAttribute('data-lazy-src')) {
      img.src = img.getAttribute('data-lazy-src');
      img.removeAttribute('data-lazy-src');
    }
  }, 100);
}

// 开始自动播放
function startAutoSlide() {
  slideInterval = setInterval(function() {
    plusSlides(1);
  }, 5000); // 每5秒切换一次
}

// 重置自动播放
function resetAutoSlide() {
  clearInterval(slideInterval);
  startAutoSlide();
}

// 处理容器点击事件
function handleContainerClick(event) {
  // 阻止事件冒泡，避免点击图片时触发容器点击
  event.stopPropagation();
}

// 页面加载完成后初始化
window.onload = initCarousel;
</script>
