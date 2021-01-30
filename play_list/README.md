# 解析iTunes播放列表

知识点：
+ XML和属性列表文件
+ Python列表和字典
+ Python的set对象
+ 使用numpy数组
+ 直方图和散点图
+ 使用matplotlib库绘制简单的图
+ 创建和保存数据文件

## 需求
    在ITunes播放列表文件中查找重复的乐曲音轨，并绘制各种统计数据，如音轨长度和评分。

## 技术方案
### 1、解析XML
使用plistlib库
```python
        with open("test-data/pl2.xml", "rb") as file:
            pl = plistlib.load(file)
        tracks = pl["Tracks"]
```

### 2、绘制统计数据
使用numpy库
```python
    x = np.array(durations, np.int32)
    x = x/60000.0
    y = np.array(ratings, np.int32)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), -1, 110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')
    pyplot.subplot(2, 1, 2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')
    pyplot.show()
```