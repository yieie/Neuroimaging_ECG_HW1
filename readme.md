### Neuroimaging_ECG_HW1
#### 吹氣球運動Demo影片
---
下載PsychoPy
https://psychopy.org/download.html

PsychoPy Standalone (Stable)版本

註：
若PsychoPy無法點擊開始，可建立一個TXT檔，將下列文字複製貼上，將附檔名更改完.bat，連點就可以開始PsychoPy

記得把檔案位址改成自己的

```bat
@echo off
set PYTHONUTF8=1
"C:\Program Files\PsychoPy\python.exe" -c "import psychopy.app; psychopy.app.startApp()"
```

#### 實驗開始方式
---
- 執行polar_bridge.py

此步為自動在PolarH10設立marker

要先有python環境

執行
```
python polar_bridge.py
```
會出現一個localhost的網址
貼上瀏覽器後會出現與原本Polar_H10相同的頁面
左下角會顯示有沒有成功跟PsychoPy建立連結

> 📌 **Notice**：
> 不可以直接連點打開VerityCollectionToolv0.057.html
> 這樣會沒辦法自動建立marker

詳細程式執行方式如下
(待補)

- 開始實驗
PsychoPy runner視窗，點擊左上角"+"，打開.psyexp檔
可以切換Pilot(測試)/Run(正式開始)
按下Destop Run的播放按鈕，實驗就會開始
<img width="1066" height="913" alt="image" src="https://github.com/user-attachments/assets/f3231557-9c0f-4ee8-ad3f-404a57153dd9" />

實驗會記錄當下受試的marker時間點在marker_log資料夾
可依此來與網頁上接收到的marker以及訊號來對齊

#### 修改實驗
---
PsychoPy Builder頁面
左上角可以開啟過去建立的實驗.psyexp檔
開啟後就可以針對每個routine來修改

