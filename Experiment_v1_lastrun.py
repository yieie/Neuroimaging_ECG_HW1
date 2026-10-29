#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.4),
    on 十月 29, 2026, at 14:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import csv
import os
from datetime import datetime

# 1. 自動建立 log 資料夾 (如果資料夾不存在，會自動創建)
log_dir = 'marker_log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.4'
expName = 'Experiment_v1'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'age': '',
    'gender': ['Male', 'Female', 'Other'],
    'birthday': 'YYYY-MM-DD',
    'group': [1, 2],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1280, 720)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data/' + expInfo['participant'] + '_' + expName + '_' + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\NCKU\\Desktop\\class\\Neuro\\Neuroimaging_ECG_HW1\\Experiment_v1_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "routine_01_Instruction" ---
    instr_text = visual.TextStim(win=win, name='instr_text',
        text='歡迎參加本實驗\n\n1.請確認已正確配戴 Polar H10 心率帶。\n2.實驗過程中請保持身體放鬆、勿大幅度移動。\n3.本實驗包含：靜坐基準測量、慢呼吸引導與吹氣球任務。\n\n準備好後，請按下 [空白鍵 Space] 開始練習與測量。',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    # Run 'Begin Experiment' code from code
    import threading
    import time
    import urllib.parse
    import urllib.request
    
    def send_marker(label):
        """送 marker 到 WebPolarReader，並把精確時間存進 PsychoPy 的 csv。
        用背景執行緒送出，不會卡住畫面。"""
        t = time.time()                       # 系統時間（秒），與 marker 的毫秒時間同一個時鐘
        thisExp.addData(label + '_epoch', t)  # PsychoPy csv 也留一份精確時間
        full = f"{label}"             # marker 名稱附上 PsychoPy 的時間，方便事後核對
        url = "http://localhost:8765/marker?label=" + urllib.parse.quote(full)
        def _go():
            try:
                urllib.request.urlopen(url, timeout=1)
            except Exception as e:
                print("marker 送出失敗：", label, e)
        threading.Thread(target=_go, daemon=True).start()
        
    
    # 自動抓取 Runner 開啟時填寫的 Participant 與 Session
    # 若填寫留空，會給予預設值 'anonymous' 與 '1'
    participant_id = expInfo.get('participant', 'anonymous')
    session_id = expInfo.get('session', '1')
    
    # 組合檔名並放在 maker_log/ 資料夾下
    # 範例檔名: maker_log/sub-P001_sess-01_marker_20261014_112500.csv
    time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = os.path.join(log_dir, f"sub-{participant_id}_sess-{session_id}_marker_{time_str}.csv")
    
    # 開啟檔案並寫入標題欄位 (Header)
    with open(log_filename, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Participant',            # 受試者 ID
            'Session',                # 場次 ID
            'Trial_Index',            # 循環/試驗次數
            'Event_Name',             # 事件名稱 (如: Inhale, Exhale, Deflate)
            'Marker_Code',            # Marker 編號
            'Local_ISO_Time',         # 本地 ISO 時間 (與網站/雲端 timestamp 對齊)
            'Local_Epoch_Time',       # 本地 Epoch 時間 (浮點數，方便做秒數扣減)
            'PsychoPy_Relative_t'     # Routine 內的相對時間 (t)
        ])
    
    print(f"[Log Setup] 成功建立紀錄檔：{log_filename}")
    
    # --- Initialize components for Routine "routine_02_Baseline_A_Notice" ---
    notice = visual.TextStim(win=win, name='notice',
        text='',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "routine_02_Baseline_A_Countdown" ---
    countdown = visual.TextStim(win=win, name='countdown',
        text='',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "routine_02_Baseline_A_Exper" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "routine_03_Task_breath_Instr" ---
    Task_breath = visual.TextStim(win=win, name='Task_breath',
        text='【慢呼吸實驗說明】\n\n請跟隨畫面圓形進行 4 秒鼻吸氣、6 秒嘴吐氣。\n本次實驗將持續5分鐘，共30次循環。\n\n請按下 [空白鍵 Space] 開始進入實驗！',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_8 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "routine_03_Task_breath_Countdown" ---
    Task_breath_Countdown = visual.TextStim(win=win, name='Task_breath_Countdown',
        text='',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "routine_03_Task_breath" ---
    circle_border = visual.ShapeStim(
        win=win, name='circle_border',
        size=(0.6, 0.6), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=(0.0000, 0.0000, 0.0000),
        opacity=None, depth=0.0, interpolate=True)
    circle_guide = visual.ShapeStim(
        win=win, name='circle_guide',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(0.0000, 0.0000, 0.0000), fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    inhale = visual.ImageStim(
        win=win,
        name='inhale', 
        image='inhale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    exhale = visual.ImageStim(
        win=win,
        name='exhale', 
        image='breath.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.2), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "routine_04_Task_Break" ---
    break_text = visual.TextStim(win=win, name='break_text',
        text='慢呼吸實驗已結束，請稍作休息\n\n下一階段為吹氣球實驗，將於7分鐘後開始\n',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "routine_05_Task_blow_Instr" ---
    Task_blow = visual.TextStim(win=win, name='Task_blow',
        text='【吹氣球實驗說明】\n\n請跟隨畫面指示進行：4 秒鼻吸氣 ， 6 秒對氣球吐氣。\n本次實驗將進行5分鐘，共6大組吹氣流程。\n\n注意事項：\n1.請對氣球連續吹 4 口氣，期間請勿將氣球移開嘴巴，也不要讓氣球洩氣！\n2.吸氣時： 氣球維持壓在嘴唇上，用「鼻子」吸氣。\n3.待畫面出現【請將氣球放氣】時，再將氣球放氣\n\n準備完畢請按下 [空白鍵 Space] 開始進入實驗！',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_9 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # --- Initialize components for Routine "routine_05_Task_blow_Countdown" ---
    Task_blow_Countdown = visual.TextStim(win=win, name='Task_blow_Countdown',
        text='',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "routine_05_Task_blow" ---
    circle_border_blow = visual.ShapeStim(
        win=win, name='circle_border_blow',
        size=(0.6, 0.6), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=(0.0000, 0.0000, 0.0000),
        opacity=None, depth=0.0, interpolate=True)
    circle_guide_blow = visual.ShapeStim(
        win=win, name='circle_guide_blow',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(0.0000, 0.0000, 0.0000), fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    inhale_blow = visual.ImageStim(
        win=win,
        name='inhale_blow', 
        image='inhale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    exhale_blow = visual.ImageStim(
        win=win,
        name='exhale_blow', 
        image='blowing-balloon.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_blow = visual.TextStim(win=win, name='text_blow',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.2), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    # Run 'Begin Experiment' code from code_10
    total_blow_trials = 1
    
    # --- Initialize components for Routine "routine_05_Task_blow" ---
    circle_border_blow = visual.ShapeStim(
        win=win, name='circle_border_blow',
        size=(0.6, 0.6), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=(0.0000, 0.0000, 0.0000),
        opacity=None, depth=0.0, interpolate=True)
    circle_guide_blow = visual.ShapeStim(
        win=win, name='circle_guide_blow',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(0.0000, 0.0000, 0.0000), fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    inhale_blow = visual.ImageStim(
        win=win,
        name='inhale_blow', 
        image='inhale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    exhale_blow = visual.ImageStim(
        win=win,
        name='exhale_blow', 
        image='blowing-balloon.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_blow = visual.TextStim(win=win, name='text_blow',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.2), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    # Run 'Begin Experiment' code from code_10
    total_blow_trials = 1
    
    # --- Initialize components for Routine "routine_05_Task_blow_deflate" ---
    circle_border_blow_2 = visual.ShapeStim(
        win=win, name='circle_border_blow_2',
        size=(0.6, 0.6), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=(0.0000, 0.0000, 0.0000),
        opacity=None, depth=0.0, interpolate=True)
    circle_guide_blow_2 = visual.ShapeStim(
        win=win, name='circle_guide_blow_2',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(0.0000, 0.0000, 0.0000), fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    inhale_blow_2 = visual.ImageStim(
        win=win,
        name='inhale_blow_2', 
        image='inhale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    exhale_blow_2 = visual.ImageStim(
        win=win,
        name='exhale_blow_2', 
        image='blowing-balloon.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    deflate = visual.TextStim(win=win, name='deflate',
        text='請將氣球放氣 並持續跟隨呼吸節奏',
        font='Microsoft JhengHei',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    text_blow_2 = visual.TextStim(win=win, name='text_blow_2',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.2), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "routine_05_Task_blow" ---
    circle_border_blow = visual.ShapeStim(
        win=win, name='circle_border_blow',
        size=(0.6, 0.6), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='white', fillColor=(0.0000, 0.0000, 0.0000),
        opacity=None, depth=0.0, interpolate=True)
    circle_guide_blow = visual.ShapeStim(
        win=win, name='circle_guide_blow',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(0.0000, 0.0000, 0.0000), fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    inhale_blow = visual.ImageStim(
        win=win,
        name='inhale_blow', 
        image='inhale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    exhale_blow = visual.ImageStim(
        win=win,
        name='exhale_blow', 
        image='blowing-balloon.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_blow = visual.TextStim(win=win, name='text_blow',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.2), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    # Run 'Begin Experiment' code from code_10
    total_blow_trials = 1
    
    # --- Initialize components for Routine "routine_05_Task_blow_post" ---
    Task_blow_post = visual.TextStim(win=win, name='Task_blow_post',
        text='吹氣球實驗已結束，請您稍作休息\n3分鐘後將結束全數實驗流程。',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Microsoft JhengHei',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "routine_06_Exper_End" ---
    Exper_End = visual.TextStim(win=win, name='Exper_End',
        text='感謝您的配合，實驗已全數結束',
        font='Microsoft JhengHei',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=2.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_10 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "routine_01_Instruction" ---
    # create an object to store info about Routine routine_01_Instruction
    routine_01_Instruction = data.Routine(
        name='routine_01_Instruction',
        components=[instr_text, key_resp],
    )
    routine_01_Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from code
    ## 1. 取得當前本地精準時間
    #now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #now_epoch = time.time()
    #
    ## 2. 發送 Marker 代碼
    #marker_code = '100'
    #send_marker(marker_code)
    #
    ## 3. 即時寫入 log/ 資料夾下的 CSV
    #with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
    #    writer = csv.writer(f)
    #    writer.writerow([
    #        participant_id,
    #        session_id,
    #        0,
    #        "Exper_Begin",
    #        marker_code,
    #        now_iso,
    #        f"{now_epoch:.6f}",
    #        f"{t:.4f}"
    #    ])
    #
    ## 控制台除錯印出
    #print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Exper_Begin | Time: {now_iso}")
    # store start times for routine_01_Instruction
    routine_01_Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_01_Instruction.tStart = globalClock.getTime(format='float')
    routine_01_Instruction.status = STARTED
    thisExp.addData('routine_01_Instruction.started', routine_01_Instruction.tStart)
    routine_01_Instruction.maxDuration = None
    # keep track of which components have finished
    routine_01_InstructionComponents = routine_01_Instruction.components
    for thisComponent in routine_01_Instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_01_Instruction" ---
    thisExp.currentRoutine = routine_01_Instruction
    routine_01_Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        
        # if instr_text is starting this frame...
        if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.tStart = t  # local t and not account for scr refresh
            instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_text.started')
            # update status
            instr_text.status = STARTED
            instr_text.setAutoDraw(True)
        
        # if instr_text is active this frame...
        if instr_text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_01_Instruction,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_01_Instruction.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_01_Instruction.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_01_Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_01_Instruction" ---
    for thisComponent in routine_01_Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_01_Instruction
    routine_01_Instruction.tStop = globalClock.getTime(format='float')
    routine_01_Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_01_Instruction.stopped', routine_01_Instruction.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "routine_01_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine_02_Baseline_A_Notice" ---
    # create an object to store info about Routine routine_02_Baseline_A_Notice
    routine_02_Baseline_A_Notice = data.Routine(
        name='routine_02_Baseline_A_Notice',
        components=[notice, key_resp_2],
    )
    routine_02_Baseline_A_Notice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for routine_02_Baseline_A_Notice
    routine_02_Baseline_A_Notice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_02_Baseline_A_Notice.tStart = globalClock.getTime(format='float')
    routine_02_Baseline_A_Notice.status = STARTED
    thisExp.addData('routine_02_Baseline_A_Notice.started', routine_02_Baseline_A_Notice.tStart)
    routine_02_Baseline_A_Notice.maxDuration = None
    # keep track of which components have finished
    routine_02_Baseline_A_NoticeComponents = routine_02_Baseline_A_Notice.components
    for thisComponent in routine_02_Baseline_A_Notice.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_02_Baseline_A_Notice" ---
    thisExp.currentRoutine = routine_02_Baseline_A_Notice
    routine_02_Baseline_A_Notice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *notice* updates
        
        # if notice is starting this frame...
        if notice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notice.frameNStart = frameN  # exact frame index
            notice.tStart = t  # local t and not account for scr refresh
            notice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'notice.started')
            # update status
            notice.status = STARTED
            notice.setAutoDraw(True)
        
        # if notice is active this frame...
        if notice.status == STARTED:
            # update params
            notice.setText('【靜坐基準測量】\n\n請保持舒適坐姿，雙眼注視中央「+」字\n維持自然呼吸，放鬆心情\n（時間：5 分鐘）\n\n準備好後，請按下 [空白鍵 Space] 開始測量。', log=False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_02_Baseline_A_Notice,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_02_Baseline_A_Notice.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_02_Baseline_A_Notice.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_02_Baseline_A_Notice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_02_Baseline_A_Notice" ---
    for thisComponent in routine_02_Baseline_A_Notice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_02_Baseline_A_Notice
    routine_02_Baseline_A_Notice.tStop = globalClock.getTime(format='float')
    routine_02_Baseline_A_Notice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_02_Baseline_A_Notice.stopped', routine_02_Baseline_A_Notice.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "routine_02_Baseline_A_Notice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine_02_Baseline_A_Countdown" ---
    # create an object to store info about Routine routine_02_Baseline_A_Countdown
    routine_02_Baseline_A_Countdown = data.Routine(
        name='routine_02_Baseline_A_Countdown',
        components=[countdown],
    )
    routine_02_Baseline_A_Countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for routine_02_Baseline_A_Countdown
    routine_02_Baseline_A_Countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_02_Baseline_A_Countdown.tStart = globalClock.getTime(format='float')
    routine_02_Baseline_A_Countdown.status = STARTED
    thisExp.addData('routine_02_Baseline_A_Countdown.started', routine_02_Baseline_A_Countdown.tStart)
    routine_02_Baseline_A_Countdown.maxDuration = None
    # keep track of which components have finished
    routine_02_Baseline_A_CountdownComponents = routine_02_Baseline_A_Countdown.components
    for thisComponent in routine_02_Baseline_A_Countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_02_Baseline_A_Countdown" ---
    thisExp.currentRoutine = routine_02_Baseline_A_Countdown
    routine_02_Baseline_A_Countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *countdown* updates
        
        # if countdown is starting this frame...
        if countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown.frameNStart = frameN  # exact frame index
            countdown.tStart = t  # local t and not account for scr refresh
            countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'countdown.started')
            # update status
            countdown.status = STARTED
            countdown.setAutoDraw(True)
        
        # if countdown is active this frame...
        if countdown.status == STARTED:
            # update params
            countdown.setText(f"【靜坐基準測量】{3 - int(t)} 秒後開始", log=False)
        
        # if countdown is stopping this frame...
        if countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                countdown.tStop = t  # not accounting for scr refresh
                countdown.tStopRefresh = tThisFlipGlobal  # on global time
                countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countdown.stopped')
                # update status
                countdown.status = FINISHED
                countdown.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_02_Baseline_A_Countdown,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_02_Baseline_A_Countdown.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_02_Baseline_A_Countdown.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_02_Baseline_A_Countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_02_Baseline_A_Countdown" ---
    for thisComponent in routine_02_Baseline_A_Countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_02_Baseline_A_Countdown
    routine_02_Baseline_A_Countdown.tStop = globalClock.getTime(format='float')
    routine_02_Baseline_A_Countdown.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_02_Baseline_A_Countdown.stopped', routine_02_Baseline_A_Countdown.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_02_Baseline_A_Countdown.maxDurationReached:
        routineTimer.addTime(-routine_02_Baseline_A_Countdown.maxDuration)
    elif routine_02_Baseline_A_Countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_02_Baseline_A_Exper" ---
    # create an object to store info about Routine routine_02_Baseline_A_Exper
    routine_02_Baseline_A_Exper = data.Routine(
        name='routine_02_Baseline_A_Exper',
        components=[cross, text_5],
    )
    routine_02_Baseline_A_Exper.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    sent_2min = False
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '220'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Baseline_Exper_Begin",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Baseline_Exper_Begin | Time: {now_iso}")
    # store start times for routine_02_Baseline_A_Exper
    routine_02_Baseline_A_Exper.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_02_Baseline_A_Exper.tStart = globalClock.getTime(format='float')
    routine_02_Baseline_A_Exper.status = STARTED
    thisExp.addData('routine_02_Baseline_A_Exper.started', routine_02_Baseline_A_Exper.tStart)
    routine_02_Baseline_A_Exper.maxDuration = None
    # keep track of which components have finished
    routine_02_Baseline_A_ExperComponents = routine_02_Baseline_A_Exper.components
    for thisComponent in routine_02_Baseline_A_Exper.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_02_Baseline_A_Exper" ---
    thisExp.currentRoutine = routine_02_Baseline_A_Exper
    routine_02_Baseline_A_Exper.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 300.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 300-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        # Run 'Each Frame' code from code_3
        if not sent_2min and t >= 120:
            # 1. 取得當前本地精準時間
            now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            now_epoch = time.time()
        
            # 2. 發送 Marker 代碼
            marker_code = '221'
            send_marker(marker_code)
        
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    0,
                    "Baseline_Exper_End",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
        
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Baseline_Exper_End | Time: {now_iso}")
            
            # 2. 發送 Marker 代碼
            marker_code = '310'
            send_marker(marker_code)
        
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    0,
                    "Breath_Pre_Begin",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
        
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Pre_Begin | Time: {now_iso}")
            sent_2min = True
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            text_5.setText(f"目前經過時間：({int(t)//60} min)", log=False)
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 300-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.tStopRefresh = tThisFlipGlobal  # on global time
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_02_Baseline_A_Exper,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_02_Baseline_A_Exper.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_02_Baseline_A_Exper.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_02_Baseline_A_Exper.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_02_Baseline_A_Exper" ---
    for thisComponent in routine_02_Baseline_A_Exper.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_02_Baseline_A_Exper
    routine_02_Baseline_A_Exper.tStop = globalClock.getTime(format='float')
    routine_02_Baseline_A_Exper.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_02_Baseline_A_Exper.stopped', routine_02_Baseline_A_Exper.tStop)
    # Run 'End Routine' code from code_3
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '311'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Breath_Pre_End",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Pre_End | Time: {now_iso}")
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_02_Baseline_A_Exper.maxDurationReached:
        routineTimer.addTime(-routine_02_Baseline_A_Exper.maxDuration)
    elif routine_02_Baseline_A_Exper.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-300.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_03_Task_breath_Instr" ---
    # create an object to store info about Routine routine_03_Task_breath_Instr
    routine_03_Task_breath_Instr = data.Routine(
        name='routine_03_Task_breath_Instr',
        components=[Task_breath, key_resp_8],
    )
    routine_03_Task_breath_Instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_8
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # Run 'Begin Routine' code from code_4
    # 1. 取得當前本地精準時間
    #now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #now_epoch = time.time()
    #
    ## 2. 發送 Marker 代碼
    #marker_code = '300'
    #send_marker(marker_code)
    #
    ## 3. 即時寫入 log/ 資料夾下的 CSV
    #with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
    #    writer = csv.writer(f)
    #    writer.writerow([
    #        participant_id,
    #        session_id,
    #        0,
    #        "Breath_Instr",
    #        marker_code,
    #        now_iso,
    #        f"{now_epoch:.6f}",
    #        f"{t:.4f}"
    #    ])
    #
    ## 控制台除錯印出
    #print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Instr | Time: {now_iso}")
    # store start times for routine_03_Task_breath_Instr
    routine_03_Task_breath_Instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_03_Task_breath_Instr.tStart = globalClock.getTime(format='float')
    routine_03_Task_breath_Instr.status = STARTED
    thisExp.addData('routine_03_Task_breath_Instr.started', routine_03_Task_breath_Instr.tStart)
    routine_03_Task_breath_Instr.maxDuration = None
    # keep track of which components have finished
    routine_03_Task_breath_InstrComponents = routine_03_Task_breath_Instr.components
    for thisComponent in routine_03_Task_breath_Instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_03_Task_breath_Instr" ---
    thisExp.currentRoutine = routine_03_Task_breath_Instr
    routine_03_Task_breath_Instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_breath* updates
        
        # if Task_breath is starting this frame...
        if Task_breath.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_breath.frameNStart = frameN  # exact frame index
            Task_breath.tStart = t  # local t and not account for scr refresh
            Task_breath.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_breath, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Task_breath.started')
            # update status
            Task_breath.status = STARTED
            Task_breath.setAutoDraw(True)
        
        # if Task_breath is active this frame...
        if Task_breath.status == STARTED:
            # update params
            pass
        
        # *key_resp_8* updates
        waitOnFlip = False
        
        # if key_resp_8 is starting this frame...
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            # update status
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_03_Task_breath_Instr,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_03_Task_breath_Instr.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_03_Task_breath_Instr.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_03_Task_breath_Instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_03_Task_breath_Instr" ---
    for thisComponent in routine_03_Task_breath_Instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_03_Task_breath_Instr
    routine_03_Task_breath_Instr.tStop = globalClock.getTime(format='float')
    routine_03_Task_breath_Instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_03_Task_breath_Instr.stopped', routine_03_Task_breath_Instr.tStop)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    thisExp.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        thisExp.addData('key_resp_8.rt', key_resp_8.rt)
        thisExp.addData('key_resp_8.duration', key_resp_8.duration)
    thisExp.nextEntry()
    # the Routine "routine_03_Task_breath_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine_03_Task_breath_Countdown" ---
    # create an object to store info about Routine routine_03_Task_breath_Countdown
    routine_03_Task_breath_Countdown = data.Routine(
        name='routine_03_Task_breath_Countdown',
        components=[Task_breath_Countdown],
    )
    routine_03_Task_breath_Countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for routine_03_Task_breath_Countdown
    routine_03_Task_breath_Countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_03_Task_breath_Countdown.tStart = globalClock.getTime(format='float')
    routine_03_Task_breath_Countdown.status = STARTED
    thisExp.addData('routine_03_Task_breath_Countdown.started', routine_03_Task_breath_Countdown.tStart)
    routine_03_Task_breath_Countdown.maxDuration = None
    # keep track of which components have finished
    routine_03_Task_breath_CountdownComponents = routine_03_Task_breath_Countdown.components
    for thisComponent in routine_03_Task_breath_Countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_03_Task_breath_Countdown" ---
    thisExp.currentRoutine = routine_03_Task_breath_Countdown
    routine_03_Task_breath_Countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_breath_Countdown* updates
        
        # if Task_breath_Countdown is starting this frame...
        if Task_breath_Countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_breath_Countdown.frameNStart = frameN  # exact frame index
            Task_breath_Countdown.tStart = t  # local t and not account for scr refresh
            Task_breath_Countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_breath_Countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Task_breath_Countdown.started')
            # update status
            Task_breath_Countdown.status = STARTED
            Task_breath_Countdown.setAutoDraw(True)
        
        # if Task_breath_Countdown is active this frame...
        if Task_breath_Countdown.status == STARTED:
            # update params
            Task_breath_Countdown.setText(f"【慢呼吸實驗】{5 - int(t)} 秒後開始", log=False)
        
        # if Task_breath_Countdown is stopping this frame...
        if Task_breath_Countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task_breath_Countdown.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Task_breath_Countdown.tStop = t  # not accounting for scr refresh
                Task_breath_Countdown.tStopRefresh = tThisFlipGlobal  # on global time
                Task_breath_Countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Task_breath_Countdown.stopped')
                # update status
                Task_breath_Countdown.status = FINISHED
                Task_breath_Countdown.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_03_Task_breath_Countdown,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_03_Task_breath_Countdown.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_03_Task_breath_Countdown.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_03_Task_breath_Countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_03_Task_breath_Countdown" ---
    for thisComponent in routine_03_Task_breath_Countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_03_Task_breath_Countdown
    routine_03_Task_breath_Countdown.tStop = globalClock.getTime(format='float')
    routine_03_Task_breath_Countdown.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_03_Task_breath_Countdown.stopped', routine_03_Task_breath_Countdown.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_03_Task_breath_Countdown.maxDurationReached:
        routineTimer.addTime(-routine_03_Task_breath_Countdown.maxDuration)
    elif routine_03_Task_breath_Countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=30, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "routine_03_Task_breath" ---
        # create an object to store info about Routine routine_03_Task_breath
        routine_03_Task_breath = data.Routine(
            name='routine_03_Task_breath',
            components=[circle_border, circle_guide, inhale, exhale, text],
        )
        routine_03_Task_breath.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        # 1. 取得當前本地精準時間
        now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        now_epoch = time.time()
        current_trial = trials.thisN + 1
        
        # 2. 發送 Marker 代碼
        marker_code = '320'
        if current_trial == 1:
            send_marker(marker_code)
        
        # 3. 即時寫入 log/ 資料夾下的 CSV
        with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                participant_id,
                session_id,
                current_trial,
                "Breath_Exper_Begin",
                marker_code,
                now_iso,
                f"{now_epoch:.6f}",
                f"{t:.4f}"
            ])
        
        # 控制台除錯印出
        print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Exper_{current_trial}_Begin | Time: {now_iso}")
        # store start times for routine_03_Task_breath
        routine_03_Task_breath.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        routine_03_Task_breath.tStart = globalClock.getTime(format='float')
        routine_03_Task_breath.status = STARTED
        thisExp.addData('routine_03_Task_breath.started', routine_03_Task_breath.tStart)
        routine_03_Task_breath.maxDuration = None
        # keep track of which components have finished
        routine_03_Task_breathComponents = routine_03_Task_breath.components
        for thisComponent in routine_03_Task_breath.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "routine_03_Task_breath" ---
        thisExp.currentRoutine = routine_03_Task_breath
        routine_03_Task_breath.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_border* updates
            
            # if circle_border is starting this frame...
            if circle_border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_border.frameNStart = frameN  # exact frame index
                circle_border.tStart = t  # local t and not account for scr refresh
                circle_border.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_border, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_border.started')
                # update status
                circle_border.status = STARTED
                circle_border.setAutoDraw(True)
            
            # if circle_border is active this frame...
            if circle_border.status == STARTED:
                # update params
                circle_border.setLineColor('skyblue' if t < 4.0 else 'orange', log=False)
            
            # if circle_border is stopping this frame...
            if circle_border.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_border.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_border.tStop = t  # not accounting for scr refresh
                    circle_border.tStopRefresh = tThisFlipGlobal  # on global time
                    circle_border.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_border.stopped')
                    # update status
                    circle_border.status = FINISHED
                    circle_border.setAutoDraw(False)
            
            # *circle_guide* updates
            
            # if circle_guide is starting this frame...
            if circle_guide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_guide.frameNStart = frameN  # exact frame index
                circle_guide.tStart = t  # local t and not account for scr refresh
                circle_guide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_guide, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_guide.started')
                # update status
                circle_guide.status = STARTED
                circle_guide.setAutoDraw(True)
            
            # if circle_guide is active this frame...
            if circle_guide.status == STARTED:
                # update params
                circle_guide.setFillColor('skyblue' if t < 4.0 else 'orange', log=False)
                circle_guide.setSize((0.1 + 0.5 * (t / 4.0), 0.1 + 0.5 * (t / 4.0)) if t < 4.0 else (0.6 - 0.5 * ((t - 4.0) / 6.0), 0.6 - 0.5 * ((t - 4.0) / 6.0)), log=False)
            
            # if circle_guide is stopping this frame...
            if circle_guide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_guide.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_guide.tStop = t  # not accounting for scr refresh
                    circle_guide.tStopRefresh = tThisFlipGlobal  # on global time
                    circle_guide.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_guide.stopped')
                    # update status
                    circle_guide.status = FINISHED
                    circle_guide.setAutoDraw(False)
            
            # *inhale* updates
            
            # if inhale is starting this frame...
            if inhale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inhale.frameNStart = frameN  # exact frame index
                inhale.tStart = t  # local t and not account for scr refresh
                inhale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inhale, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'inhale.started')
                # update status
                inhale.status = STARTED
                inhale.setAutoDraw(True)
            
            # if inhale is active this frame...
            if inhale.status == STARTED:
                # update params
                inhale.setSize((0.15 + 0.05 * (t / 4.0), 0.15 + 0.05 * (t / 4.0)), log=False)
            
            # if inhale is stopping this frame...
            if inhale.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inhale.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    inhale.tStop = t  # not accounting for scr refresh
                    inhale.tStopRefresh = tThisFlipGlobal  # on global time
                    inhale.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'inhale.stopped')
                    # update status
                    inhale.status = FINISHED
                    inhale.setAutoDraw(False)
            
            # *exhale* updates
            
            # if exhale is starting this frame...
            if exhale.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                exhale.frameNStart = frameN  # exact frame index
                exhale.tStart = t  # local t and not account for scr refresh
                exhale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(exhale, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exhale.started')
                # update status
                exhale.status = STARTED
                exhale.setAutoDraw(True)
            
            # if exhale is active this frame...
            if exhale.status == STARTED:
                # update params
                exhale.setSize((0.2 - 0.05 * ((t - 4.0) / 6.0), 0.2 - 0.05 * ((t - 4.0) / 6.0)), log=False)
            
            # if exhale is stopping this frame...
            if exhale.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > exhale.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    exhale.tStop = t  # not accounting for scr refresh
                    exhale.tStopRefresh = tThisFlipGlobal  # on global time
                    exhale.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exhale.stopped')
                    # update status
                    exhale.status = FINISHED
                    exhale.setAutoDraw(False)
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                text.setText(f"鼻吸氣 ({4 - int(t)}s)" if t < 4.0 else f"嘴吐氣 ({10 - int(t)}s)", log=False)
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=routine_03_Task_breath,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                routine_03_Task_breath.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if routine_03_Task_breath.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in routine_03_Task_breath.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "routine_03_Task_breath" ---
        for thisComponent in routine_03_Task_breath.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for routine_03_Task_breath
        routine_03_Task_breath.tStop = globalClock.getTime(format='float')
        routine_03_Task_breath.tStopRefresh = tThisFlipGlobal
        thisExp.addData('routine_03_Task_breath.stopped', routine_03_Task_breath.tStop)
        # Run 'End Routine' code from code_6
        # 1. 取得當前本地精準時間
        now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        now_epoch = time.time()
        current_trial = trials.thisN + 1
        
        # 2. 發送 Marker 代碼
        marker_code = '321'
        if current_trial == 30:
            send_marker(marker_code)
        
        # 3. 即時寫入 log/ 資料夾下的 CSV
        with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                participant_id,
                session_id,
                0,
                "Breath_Exper_End",
                marker_code,
                now_iso,
                f"{now_epoch:.6f}",
                f"{t:.4f}"
            ])
        
        # 控制台除錯印出
        print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Exper_{current_trial}_end | Time: {now_iso}")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routine_03_Task_breath.maxDurationReached:
            routineTimer.addTime(-routine_03_Task_breath.maxDuration)
        elif routine_03_Task_breath.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 30 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_04_Task_Break" ---
    # create an object to store info about Routine routine_04_Task_Break
    routine_04_Task_Break = data.Routine(
        name='routine_04_Task_Break',
        components=[break_text, text_2],
    )
    routine_04_Task_Break.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_7
    sent_3min = False
    sent_5min = False
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '330'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Breath_Post_Begin",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Post_Begin | Time: {now_iso}")
    # store start times for routine_04_Task_Break
    routine_04_Task_Break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_04_Task_Break.tStart = globalClock.getTime(format='float')
    routine_04_Task_Break.status = STARTED
    thisExp.addData('routine_04_Task_Break.started', routine_04_Task_Break.tStart)
    routine_04_Task_Break.maxDuration = None
    # keep track of which components have finished
    routine_04_Task_BreakComponents = routine_04_Task_Break.components
    for thisComponent in routine_04_Task_Break.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_04_Task_Break" ---
    thisExp.currentRoutine = routine_04_Task_Break
    routine_04_Task_Break.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 420.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        
        # if break_text is starting this frame...
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_text.started')
            # update status
            break_text.status = STARTED
            break_text.setAutoDraw(True)
        
        # if break_text is active this frame...
        if break_text.status == STARTED:
            # update params
            pass
        
        # if break_text is stopping this frame...
        if break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_text.tStartRefresh + 420-frameTolerance:
                # keep track of stop time/frame for later
                break_text.tStop = t  # not accounting for scr refresh
                break_text.tStopRefresh = tThisFlipGlobal  # on global time
                break_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_text.stopped')
                # update status
                break_text.status = FINISHED
                break_text.setAutoDraw(False)
        # Run 'Each Frame' code from code_7
        if not sent_3min and t >= 180:
            # 1. 取得當前本地精準時間
            now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            now_epoch = time.time()
        
            # 2. 發送 Marker 代碼
            marker_code = '331'
            send_marker(marker_code)
        
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    0,
                    "Breath_Post_End",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
        
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Breath_Post_End | Time: {now_iso}")
            sent_3min = True
            
        if not sent_5min and t >= 300:
            # 1. 取得當前本地精準時間
            now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            now_epoch = time.time()
        
            # 2. 發送 Marker 代碼
            marker_code = '510'
            send_marker(marker_code)
        
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    0,
                    "Blow_Pre_Begin",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
        
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Pre_Begin | Time: {now_iso}")
            sent_5min = True
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            text_2.setText(f"目前經過時間：({int(t)//60} min)", log=False)
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 420-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_04_Task_Break,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_04_Task_Break.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_04_Task_Break.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_04_Task_Break.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_04_Task_Break" ---
    for thisComponent in routine_04_Task_Break.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_04_Task_Break
    routine_04_Task_Break.tStop = globalClock.getTime(format='float')
    routine_04_Task_Break.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_04_Task_Break.stopped', routine_04_Task_Break.tStop)
    # Run 'End Routine' code from code_7
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '511'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Blow_Pre_End",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Pre_End | Time: {now_iso}")
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_04_Task_Break.maxDurationReached:
        routineTimer.addTime(-routine_04_Task_Break.maxDuration)
    elif routine_04_Task_Break.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-420.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_05_Task_blow_Instr" ---
    # create an object to store info about Routine routine_05_Task_blow_Instr
    routine_05_Task_blow_Instr = data.Routine(
        name='routine_05_Task_blow_Instr',
        components=[Task_blow, key_resp_9],
    )
    routine_05_Task_blow_Instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_9
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # store start times for routine_05_Task_blow_Instr
    routine_05_Task_blow_Instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_05_Task_blow_Instr.tStart = globalClock.getTime(format='float')
    routine_05_Task_blow_Instr.status = STARTED
    thisExp.addData('routine_05_Task_blow_Instr.started', routine_05_Task_blow_Instr.tStart)
    routine_05_Task_blow_Instr.maxDuration = None
    # keep track of which components have finished
    routine_05_Task_blow_InstrComponents = routine_05_Task_blow_Instr.components
    for thisComponent in routine_05_Task_blow_Instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_05_Task_blow_Instr" ---
    thisExp.currentRoutine = routine_05_Task_blow_Instr
    routine_05_Task_blow_Instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_blow* updates
        
        # if Task_blow is starting this frame...
        if Task_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_blow.frameNStart = frameN  # exact frame index
            Task_blow.tStart = t  # local t and not account for scr refresh
            Task_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Task_blow.started')
            # update status
            Task_blow.status = STARTED
            Task_blow.setAutoDraw(True)
        
        # if Task_blow is active this frame...
        if Task_blow.status == STARTED:
            # update params
            pass
        
        # *key_resp_9* updates
        waitOnFlip = False
        
        # if key_resp_9 is starting this frame...
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            # update status
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_05_Task_blow_Instr,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_05_Task_blow_Instr.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_05_Task_blow_Instr.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_05_Task_blow_Instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_05_Task_blow_Instr" ---
    for thisComponent in routine_05_Task_blow_Instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_05_Task_blow_Instr
    routine_05_Task_blow_Instr.tStop = globalClock.getTime(format='float')
    routine_05_Task_blow_Instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_05_Task_blow_Instr.stopped', routine_05_Task_blow_Instr.tStop)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    thisExp.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        thisExp.addData('key_resp_9.rt', key_resp_9.rt)
        thisExp.addData('key_resp_9.duration', key_resp_9.duration)
    thisExp.nextEntry()
    # the Routine "routine_05_Task_blow_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine_05_Task_blow_Countdown" ---
    # create an object to store info about Routine routine_05_Task_blow_Countdown
    routine_05_Task_blow_Countdown = data.Routine(
        name='routine_05_Task_blow_Countdown',
        components=[Task_blow_Countdown],
    )
    routine_05_Task_blow_Countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for routine_05_Task_blow_Countdown
    routine_05_Task_blow_Countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_05_Task_blow_Countdown.tStart = globalClock.getTime(format='float')
    routine_05_Task_blow_Countdown.status = STARTED
    thisExp.addData('routine_05_Task_blow_Countdown.started', routine_05_Task_blow_Countdown.tStart)
    routine_05_Task_blow_Countdown.maxDuration = None
    # keep track of which components have finished
    routine_05_Task_blow_CountdownComponents = routine_05_Task_blow_Countdown.components
    for thisComponent in routine_05_Task_blow_Countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_05_Task_blow_Countdown" ---
    thisExp.currentRoutine = routine_05_Task_blow_Countdown
    routine_05_Task_blow_Countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_blow_Countdown* updates
        
        # if Task_blow_Countdown is starting this frame...
        if Task_blow_Countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_blow_Countdown.frameNStart = frameN  # exact frame index
            Task_blow_Countdown.tStart = t  # local t and not account for scr refresh
            Task_blow_Countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_blow_Countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Task_blow_Countdown.started')
            # update status
            Task_blow_Countdown.status = STARTED
            Task_blow_Countdown.setAutoDraw(True)
        
        # if Task_blow_Countdown is active this frame...
        if Task_blow_Countdown.status == STARTED:
            # update params
            Task_blow_Countdown.setText(f"【吹氣球實驗】{5 - int(t)} 秒後開始", log=False)
        
        # if Task_blow_Countdown is stopping this frame...
        if Task_blow_Countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task_blow_Countdown.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Task_blow_Countdown.tStop = t  # not accounting for scr refresh
                Task_blow_Countdown.tStopRefresh = tThisFlipGlobal  # on global time
                Task_blow_Countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Task_blow_Countdown.stopped')
                # update status
                Task_blow_Countdown.status = FINISHED
                Task_blow_Countdown.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_05_Task_blow_Countdown,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_05_Task_blow_Countdown.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_05_Task_blow_Countdown.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_05_Task_blow_Countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_05_Task_blow_Countdown" ---
    for thisComponent in routine_05_Task_blow_Countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_05_Task_blow_Countdown
    routine_05_Task_blow_Countdown.tStop = globalClock.getTime(format='float')
    routine_05_Task_blow_Countdown.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_05_Task_blow_Countdown.stopped', routine_05_Task_blow_Countdown.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_05_Task_blow_Countdown.maxDurationReached:
        routineTimer.addTime(-routine_05_Task_blow_Countdown.maxDuration)
    elif routine_05_Task_blow_Countdown.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_05_Task_blow" ---
    # create an object to store info about Routine routine_05_Task_blow
    routine_05_Task_blow = data.Routine(
        name='routine_05_Task_blow',
        components=[circle_border_blow, circle_guide_blow, inhale_blow, exhale_blow, text_blow],
    )
    routine_05_Task_blow.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_10
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    current_trial = total_blow_trials
    
    # 2. 發送 Marker 代碼
    marker_code = '520'
    if current_trial == 1:
        send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            current_trial,
            "Blow_Exper_Begin",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_Begin | Time: {now_iso}")
    # store start times for routine_05_Task_blow
    routine_05_Task_blow.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_05_Task_blow.tStart = globalClock.getTime(format='float')
    routine_05_Task_blow.status = STARTED
    thisExp.addData('routine_05_Task_blow.started', routine_05_Task_blow.tStart)
    routine_05_Task_blow.maxDuration = None
    # keep track of which components have finished
    routine_05_Task_blowComponents = routine_05_Task_blow.components
    for thisComponent in routine_05_Task_blow.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_05_Task_blow" ---
    thisExp.currentRoutine = routine_05_Task_blow
    routine_05_Task_blow.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circle_border_blow* updates
        
        # if circle_border_blow is starting this frame...
        if circle_border_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_border_blow.frameNStart = frameN  # exact frame index
            circle_border_blow.tStart = t  # local t and not account for scr refresh
            circle_border_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_border_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_border_blow.started')
            # update status
            circle_border_blow.status = STARTED
            circle_border_blow.setAutoDraw(True)
        
        # if circle_border_blow is active this frame...
        if circle_border_blow.status == STARTED:
            # update params
            circle_border_blow.setLineColor('skyblue' if t < 4.0 else 'orange', log=False)
        
        # if circle_border_blow is stopping this frame...
        if circle_border_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle_border_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                circle_border_blow.tStop = t  # not accounting for scr refresh
                circle_border_blow.tStopRefresh = tThisFlipGlobal  # on global time
                circle_border_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_border_blow.stopped')
                # update status
                circle_border_blow.status = FINISHED
                circle_border_blow.setAutoDraw(False)
        
        # *circle_guide_blow* updates
        
        # if circle_guide_blow is starting this frame...
        if circle_guide_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_guide_blow.frameNStart = frameN  # exact frame index
            circle_guide_blow.tStart = t  # local t and not account for scr refresh
            circle_guide_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_guide_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_guide_blow.started')
            # update status
            circle_guide_blow.status = STARTED
            circle_guide_blow.setAutoDraw(True)
        
        # if circle_guide_blow is active this frame...
        if circle_guide_blow.status == STARTED:
            # update params
            circle_guide_blow.setFillColor('skyblue' if t < 4.0 else 'orange', log=False)
            circle_guide_blow.setSize((0.1 + 0.5 * (t / 4.0), 0.1 + 0.5 * (t / 4.0)) if t < 4.0 else (0.6 - 0.5 * ((t - 4.0) / 6.0), 0.6 - 0.5 * ((t - 4.0) / 6.0)), log=False)
        
        # if circle_guide_blow is stopping this frame...
        if circle_guide_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle_guide_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                circle_guide_blow.tStop = t  # not accounting for scr refresh
                circle_guide_blow.tStopRefresh = tThisFlipGlobal  # on global time
                circle_guide_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_guide_blow.stopped')
                # update status
                circle_guide_blow.status = FINISHED
                circle_guide_blow.setAutoDraw(False)
        
        # *inhale_blow* updates
        
        # if inhale_blow is starting this frame...
        if inhale_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inhale_blow.frameNStart = frameN  # exact frame index
            inhale_blow.tStart = t  # local t and not account for scr refresh
            inhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inhale_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inhale_blow.started')
            # update status
            inhale_blow.status = STARTED
            inhale_blow.setAutoDraw(True)
        
        # if inhale_blow is active this frame...
        if inhale_blow.status == STARTED:
            # update params
            inhale_blow.setSize((0.15 + 0.05 * (t / 4.0), 0.15 + 0.05 * (t / 4.0)), log=False)
        
        # if inhale_blow is stopping this frame...
        if inhale_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > inhale_blow.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                inhale_blow.tStop = t  # not accounting for scr refresh
                inhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                inhale_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'inhale_blow.stopped')
                # update status
                inhale_blow.status = FINISHED
                inhale_blow.setAutoDraw(False)
        
        # *exhale_blow* updates
        
        # if exhale_blow is starting this frame...
        if exhale_blow.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            exhale_blow.frameNStart = frameN  # exact frame index
            exhale_blow.tStart = t  # local t and not account for scr refresh
            exhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exhale_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exhale_blow.started')
            # update status
            exhale_blow.status = STARTED
            exhale_blow.setAutoDraw(True)
        
        # if exhale_blow is active this frame...
        if exhale_blow.status == STARTED:
            # update params
            exhale_blow.setSize((0.2 - 0.05 * ((t - 4.0) / 6.0), 0.2 - 0.05 * ((t - 4.0) / 6.0)), log=False)
        
        # if exhale_blow is stopping this frame...
        if exhale_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exhale_blow.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                exhale_blow.tStop = t  # not accounting for scr refresh
                exhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                exhale_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exhale_blow.stopped')
                # update status
                exhale_blow.status = FINISHED
                exhale_blow.setAutoDraw(False)
        
        # *text_blow* updates
        
        # if text_blow is starting this frame...
        if text_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blow.frameNStart = frameN  # exact frame index
            text_blow.tStart = t  # local t and not account for scr refresh
            text_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blow.started')
            # update status
            text_blow.status = STARTED
            text_blow.setAutoDraw(True)
        
        # if text_blow is active this frame...
        if text_blow.status == STARTED:
            # update params
            text_blow.setText(f"鼻吸氣 ({4 - int(t)}s)" if t < 4.0 else f"吹氣球 ({10 - int(t)}s)", log=False)
        
        # if text_blow is stopping this frame...
        if text_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text_blow.tStop = t  # not accounting for scr refresh
                text_blow.tStopRefresh = tThisFlipGlobal  # on global time
                text_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blow.stopped')
                # update status
                text_blow.status = FINISHED
                text_blow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_05_Task_blow,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_05_Task_blow.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_05_Task_blow.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_05_Task_blow.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_05_Task_blow" ---
    for thisComponent in routine_05_Task_blow.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_05_Task_blow
    routine_05_Task_blow.tStop = globalClock.getTime(format='float')
    routine_05_Task_blow.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_05_Task_blow.stopped', routine_05_Task_blow.tStop)
    # Run 'End Routine' code from code_10
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    current_trial = total_blow_trials
    
    # 2. 發送 Marker 代碼
    marker_code = '521'
    if current_trial == 30:
        send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            current_trial,
            "Blow_Exper_End",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_End | Time: {now_iso}")
    
    total_blow_trials += 1
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_05_Task_blow.maxDurationReached:
        routineTimer.addTime(-routine_05_Task_blow.maxDuration)
    elif routine_05_Task_blow.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler2(
        name='trials_5',
        nReps=7, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            globals()[paramName] = thisTrial_5[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_5 in trials_5:
        trials_5.status = STARTED
        if hasattr(thisTrial_5, 'status'):
            thisTrial_5.status = STARTED
        currentLoop = trials_5
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                globals()[paramName] = thisTrial_5[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler2(
            name='trials_4',
            nReps=3, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_4 in trials_4:
            trials_4.status = STARTED
            if hasattr(thisTrial_4, 'status'):
                thisTrial_4.status = STARTED
            currentLoop = trials_4
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    globals()[paramName] = thisTrial_4[paramName]
            
            # --- Prepare to start Routine "routine_05_Task_blow" ---
            # create an object to store info about Routine routine_05_Task_blow
            routine_05_Task_blow = data.Routine(
                name='routine_05_Task_blow',
                components=[circle_border_blow, circle_guide_blow, inhale_blow, exhale_blow, text_blow],
            )
            routine_05_Task_blow.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_10
            # 1. 取得當前本地精準時間
            now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            now_epoch = time.time()
            current_trial = total_blow_trials
            
            # 2. 發送 Marker 代碼
            marker_code = '520'
            if current_trial == 1:
                send_marker(marker_code)
            
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    current_trial,
                    "Blow_Exper_Begin",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
            
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_Begin | Time: {now_iso}")
            # store start times for routine_05_Task_blow
            routine_05_Task_blow.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            routine_05_Task_blow.tStart = globalClock.getTime(format='float')
            routine_05_Task_blow.status = STARTED
            thisExp.addData('routine_05_Task_blow.started', routine_05_Task_blow.tStart)
            routine_05_Task_blow.maxDuration = None
            # keep track of which components have finished
            routine_05_Task_blowComponents = routine_05_Task_blow.components
            for thisComponent in routine_05_Task_blow.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "routine_05_Task_blow" ---
            thisExp.currentRoutine = routine_05_Task_blow
            routine_05_Task_blow.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 10.0:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_4, 'status') and thisTrial_4.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *circle_border_blow* updates
                
                # if circle_border_blow is starting this frame...
                if circle_border_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    circle_border_blow.frameNStart = frameN  # exact frame index
                    circle_border_blow.tStart = t  # local t and not account for scr refresh
                    circle_border_blow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(circle_border_blow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_border_blow.started')
                    # update status
                    circle_border_blow.status = STARTED
                    circle_border_blow.setAutoDraw(True)
                
                # if circle_border_blow is active this frame...
                if circle_border_blow.status == STARTED:
                    # update params
                    circle_border_blow.setLineColor('skyblue' if t < 4.0 else 'orange', log=False)
                
                # if circle_border_blow is stopping this frame...
                if circle_border_blow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > circle_border_blow.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        circle_border_blow.tStop = t  # not accounting for scr refresh
                        circle_border_blow.tStopRefresh = tThisFlipGlobal  # on global time
                        circle_border_blow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'circle_border_blow.stopped')
                        # update status
                        circle_border_blow.status = FINISHED
                        circle_border_blow.setAutoDraw(False)
                
                # *circle_guide_blow* updates
                
                # if circle_guide_blow is starting this frame...
                if circle_guide_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    circle_guide_blow.frameNStart = frameN  # exact frame index
                    circle_guide_blow.tStart = t  # local t and not account for scr refresh
                    circle_guide_blow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(circle_guide_blow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_guide_blow.started')
                    # update status
                    circle_guide_blow.status = STARTED
                    circle_guide_blow.setAutoDraw(True)
                
                # if circle_guide_blow is active this frame...
                if circle_guide_blow.status == STARTED:
                    # update params
                    circle_guide_blow.setFillColor('skyblue' if t < 4.0 else 'orange', log=False)
                    circle_guide_blow.setSize((0.1 + 0.5 * (t / 4.0), 0.1 + 0.5 * (t / 4.0)) if t < 4.0 else (0.6 - 0.5 * ((t - 4.0) / 6.0), 0.6 - 0.5 * ((t - 4.0) / 6.0)), log=False)
                
                # if circle_guide_blow is stopping this frame...
                if circle_guide_blow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > circle_guide_blow.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        circle_guide_blow.tStop = t  # not accounting for scr refresh
                        circle_guide_blow.tStopRefresh = tThisFlipGlobal  # on global time
                        circle_guide_blow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'circle_guide_blow.stopped')
                        # update status
                        circle_guide_blow.status = FINISHED
                        circle_guide_blow.setAutoDraw(False)
                
                # *inhale_blow* updates
                
                # if inhale_blow is starting this frame...
                if inhale_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inhale_blow.frameNStart = frameN  # exact frame index
                    inhale_blow.tStart = t  # local t and not account for scr refresh
                    inhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inhale_blow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'inhale_blow.started')
                    # update status
                    inhale_blow.status = STARTED
                    inhale_blow.setAutoDraw(True)
                
                # if inhale_blow is active this frame...
                if inhale_blow.status == STARTED:
                    # update params
                    inhale_blow.setSize((0.15 + 0.05 * (t / 4.0), 0.15 + 0.05 * (t / 4.0)), log=False)
                
                # if inhale_blow is stopping this frame...
                if inhale_blow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > inhale_blow.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        inhale_blow.tStop = t  # not accounting for scr refresh
                        inhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                        inhale_blow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'inhale_blow.stopped')
                        # update status
                        inhale_blow.status = FINISHED
                        inhale_blow.setAutoDraw(False)
                
                # *exhale_blow* updates
                
                # if exhale_blow is starting this frame...
                if exhale_blow.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                    # keep track of start time/frame for later
                    exhale_blow.frameNStart = frameN  # exact frame index
                    exhale_blow.tStart = t  # local t and not account for scr refresh
                    exhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exhale_blow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exhale_blow.started')
                    # update status
                    exhale_blow.status = STARTED
                    exhale_blow.setAutoDraw(True)
                
                # if exhale_blow is active this frame...
                if exhale_blow.status == STARTED:
                    # update params
                    exhale_blow.setSize((0.2 - 0.05 * ((t - 4.0) / 6.0), 0.2 - 0.05 * ((t - 4.0) / 6.0)), log=False)
                
                # if exhale_blow is stopping this frame...
                if exhale_blow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > exhale_blow.tStartRefresh + 6.0-frameTolerance:
                        # keep track of stop time/frame for later
                        exhale_blow.tStop = t  # not accounting for scr refresh
                        exhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                        exhale_blow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'exhale_blow.stopped')
                        # update status
                        exhale_blow.status = FINISHED
                        exhale_blow.setAutoDraw(False)
                
                # *text_blow* updates
                
                # if text_blow is starting this frame...
                if text_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_blow.frameNStart = frameN  # exact frame index
                    text_blow.tStart = t  # local t and not account for scr refresh
                    text_blow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_blow, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blow.started')
                    # update status
                    text_blow.status = STARTED
                    text_blow.setAutoDraw(True)
                
                # if text_blow is active this frame...
                if text_blow.status == STARTED:
                    # update params
                    text_blow.setText(f"鼻吸氣 ({4 - int(t)}s)" if t < 4.0 else f"吹氣球 ({10 - int(t)}s)", log=False)
                
                # if text_blow is stopping this frame...
                if text_blow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_blow.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_blow.tStop = t  # not accounting for scr refresh
                        text_blow.tStopRefresh = tThisFlipGlobal  # on global time
                        text_blow.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_blow.stopped')
                        # update status
                        text_blow.status = FINISHED
                        text_blow.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=routine_05_Task_blow,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    routine_05_Task_blow.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if routine_05_Task_blow.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in routine_05_Task_blow.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "routine_05_Task_blow" ---
            for thisComponent in routine_05_Task_blow.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for routine_05_Task_blow
            routine_05_Task_blow.tStop = globalClock.getTime(format='float')
            routine_05_Task_blow.tStopRefresh = tThisFlipGlobal
            thisExp.addData('routine_05_Task_blow.stopped', routine_05_Task_blow.tStop)
            # Run 'End Routine' code from code_10
            # 1. 取得當前本地精準時間
            now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            now_epoch = time.time()
            current_trial = total_blow_trials
            
            # 2. 發送 Marker 代碼
            marker_code = '521'
            if current_trial == 30:
                send_marker(marker_code)
            
            # 3. 即時寫入 log/ 資料夾下的 CSV
            with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    participant_id,
                    session_id,
                    current_trial,
                    "Blow_Exper_End",
                    marker_code,
                    now_iso,
                    f"{now_epoch:.6f}",
                    f"{t:.4f}"
                ])
            
            # 控制台除錯印出
            print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_End | Time: {now_iso}")
            
            total_blow_trials += 1
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routine_05_Task_blow.maxDurationReached:
                routineTimer.addTime(-routine_05_Task_blow.maxDuration)
            elif routine_05_Task_blow.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            # mark thisTrial_4 as finished
            if hasattr(thisTrial_4, 'status'):
                thisTrial_4.status = FINISHED
            # if awaiting a pause, pause now
            if trials_4.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trials_4.status = STARTED
            thisExp.nextEntry()
            
        # completed 3 repeats of 'trials_4'
        trials_4.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "routine_05_Task_blow_deflate" ---
        # create an object to store info about Routine routine_05_Task_blow_deflate
        routine_05_Task_blow_deflate = data.Routine(
            name='routine_05_Task_blow_deflate',
            components=[circle_border_blow_2, circle_guide_blow_2, inhale_blow_2, exhale_blow_2, deflate, text_blow_2],
        )
        routine_05_Task_blow_deflate.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_5
        # 1. 取得當前本地精準時間
        now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        now_epoch = time.time()
        current_trial = total_blow_trials
        
        # 2. 發送 Marker 代碼
        marker_code = '520'
        if current_trial == 1:
            send_marker(marker_code)
        
        # 3. 即時寫入 log/ 資料夾下的 CSV
        with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                participant_id,
                session_id,
                current_trial,
                "Blow_Exper_Begin",
                marker_code,
                now_iso,
                f"{now_epoch:.6f}",
                f"{t:.4f}"
            ])
        
        # 控制台除錯印出
        print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_Begin | Time: {now_iso}")
        # store start times for routine_05_Task_blow_deflate
        routine_05_Task_blow_deflate.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        routine_05_Task_blow_deflate.tStart = globalClock.getTime(format='float')
        routine_05_Task_blow_deflate.status = STARTED
        thisExp.addData('routine_05_Task_blow_deflate.started', routine_05_Task_blow_deflate.tStart)
        routine_05_Task_blow_deflate.maxDuration = None
        # keep track of which components have finished
        routine_05_Task_blow_deflateComponents = routine_05_Task_blow_deflate.components
        for thisComponent in routine_05_Task_blow_deflate.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "routine_05_Task_blow_deflate" ---
        thisExp.currentRoutine = routine_05_Task_blow_deflate
        routine_05_Task_blow_deflate.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_5, 'status') and thisTrial_5.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_border_blow_2* updates
            
            # if circle_border_blow_2 is starting this frame...
            if circle_border_blow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_border_blow_2.frameNStart = frameN  # exact frame index
                circle_border_blow_2.tStart = t  # local t and not account for scr refresh
                circle_border_blow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_border_blow_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_border_blow_2.started')
                # update status
                circle_border_blow_2.status = STARTED
                circle_border_blow_2.setAutoDraw(True)
            
            # if circle_border_blow_2 is active this frame...
            if circle_border_blow_2.status == STARTED:
                # update params
                circle_border_blow_2.setLineColor('skyblue' if t < 4.0 else 'orange', log=False)
            
            # if circle_border_blow_2 is stopping this frame...
            if circle_border_blow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_border_blow_2.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_border_blow_2.tStop = t  # not accounting for scr refresh
                    circle_border_blow_2.tStopRefresh = tThisFlipGlobal  # on global time
                    circle_border_blow_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_border_blow_2.stopped')
                    # update status
                    circle_border_blow_2.status = FINISHED
                    circle_border_blow_2.setAutoDraw(False)
            
            # *circle_guide_blow_2* updates
            
            # if circle_guide_blow_2 is starting this frame...
            if circle_guide_blow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle_guide_blow_2.frameNStart = frameN  # exact frame index
                circle_guide_blow_2.tStart = t  # local t and not account for scr refresh
                circle_guide_blow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_guide_blow_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_guide_blow_2.started')
                # update status
                circle_guide_blow_2.status = STARTED
                circle_guide_blow_2.setAutoDraw(True)
            
            # if circle_guide_blow_2 is active this frame...
            if circle_guide_blow_2.status == STARTED:
                # update params
                circle_guide_blow_2.setFillColor('skyblue' if t < 4.0 else 'orange', log=False)
                circle_guide_blow_2.setSize((0.1 + 0.5 * (t / 4.0), 0.1 + 0.5 * (t / 4.0)) if t < 4.0 else (0.6 - 0.5 * ((t - 4.0) / 6.0), 0.6 - 0.5 * ((t - 4.0) / 6.0)), log=False)
            
            # if circle_guide_blow_2 is stopping this frame...
            if circle_guide_blow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_guide_blow_2.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_guide_blow_2.tStop = t  # not accounting for scr refresh
                    circle_guide_blow_2.tStopRefresh = tThisFlipGlobal  # on global time
                    circle_guide_blow_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_guide_blow_2.stopped')
                    # update status
                    circle_guide_blow_2.status = FINISHED
                    circle_guide_blow_2.setAutoDraw(False)
            
            # *inhale_blow_2* updates
            
            # if inhale_blow_2 is starting this frame...
            if inhale_blow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inhale_blow_2.frameNStart = frameN  # exact frame index
                inhale_blow_2.tStart = t  # local t and not account for scr refresh
                inhale_blow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inhale_blow_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'inhale_blow_2.started')
                # update status
                inhale_blow_2.status = STARTED
                inhale_blow_2.setAutoDraw(True)
            
            # if inhale_blow_2 is active this frame...
            if inhale_blow_2.status == STARTED:
                # update params
                inhale_blow_2.setSize((0.15 + 0.05 * (t / 4.0), 0.15 + 0.05 * (t / 4.0)), log=False)
            
            # if inhale_blow_2 is stopping this frame...
            if inhale_blow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inhale_blow_2.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    inhale_blow_2.tStop = t  # not accounting for scr refresh
                    inhale_blow_2.tStopRefresh = tThisFlipGlobal  # on global time
                    inhale_blow_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'inhale_blow_2.stopped')
                    # update status
                    inhale_blow_2.status = FINISHED
                    inhale_blow_2.setAutoDraw(False)
            
            # *exhale_blow_2* updates
            
            # if exhale_blow_2 is starting this frame...
            if exhale_blow_2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                exhale_blow_2.frameNStart = frameN  # exact frame index
                exhale_blow_2.tStart = t  # local t and not account for scr refresh
                exhale_blow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(exhale_blow_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exhale_blow_2.started')
                # update status
                exhale_blow_2.status = STARTED
                exhale_blow_2.setAutoDraw(True)
            
            # if exhale_blow_2 is active this frame...
            if exhale_blow_2.status == STARTED:
                # update params
                exhale_blow_2.setSize((0.2 - 0.05 * ((t - 4.0) / 6.0), 0.2 - 0.05 * ((t - 4.0) / 6.0)), log=False)
            
            # if exhale_blow_2 is stopping this frame...
            if exhale_blow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > exhale_blow_2.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    exhale_blow_2.tStop = t  # not accounting for scr refresh
                    exhale_blow_2.tStopRefresh = tThisFlipGlobal  # on global time
                    exhale_blow_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'exhale_blow_2.stopped')
                    # update status
                    exhale_blow_2.status = FINISHED
                    exhale_blow_2.setAutoDraw(False)
            
            # *deflate* updates
            
            # if deflate is starting this frame...
            if deflate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                deflate.frameNStart = frameN  # exact frame index
                deflate.tStart = t  # local t and not account for scr refresh
                deflate.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(deflate, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'deflate.started')
                # update status
                deflate.status = STARTED
                deflate.setAutoDraw(True)
            
            # if deflate is active this frame...
            if deflate.status == STARTED:
                # update params
                pass
            
            # if deflate is stopping this frame...
            if deflate.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > deflate.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    deflate.tStop = t  # not accounting for scr refresh
                    deflate.tStopRefresh = tThisFlipGlobal  # on global time
                    deflate.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'deflate.stopped')
                    # update status
                    deflate.status = FINISHED
                    deflate.setAutoDraw(False)
            
            # *text_blow_2* updates
            
            # if text_blow_2 is starting this frame...
            if text_blow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blow_2.frameNStart = frameN  # exact frame index
                text_blow_2.tStart = t  # local t and not account for scr refresh
                text_blow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blow_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blow_2.started')
                # update status
                text_blow_2.status = STARTED
                text_blow_2.setAutoDraw(True)
            
            # if text_blow_2 is active this frame...
            if text_blow_2.status == STARTED:
                # update params
                text_blow_2.setText(f"鼻吸氣 ({4 - int(t)}s)" if t < 4.0 else f"吹氣球 ({10 - int(t)}s)", log=False)
            
            # if text_blow_2 is stopping this frame...
            if text_blow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_blow_2.tStartRefresh + 10.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_blow_2.tStop = t  # not accounting for scr refresh
                    text_blow_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_blow_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blow_2.stopped')
                    # update status
                    text_blow_2.status = FINISHED
                    text_blow_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=routine_05_Task_blow_deflate,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                routine_05_Task_blow_deflate.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if routine_05_Task_blow_deflate.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in routine_05_Task_blow_deflate.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "routine_05_Task_blow_deflate" ---
        for thisComponent in routine_05_Task_blow_deflate.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for routine_05_Task_blow_deflate
        routine_05_Task_blow_deflate.tStop = globalClock.getTime(format='float')
        routine_05_Task_blow_deflate.tStopRefresh = tThisFlipGlobal
        thisExp.addData('routine_05_Task_blow_deflate.stopped', routine_05_Task_blow_deflate.tStop)
        # Run 'End Routine' code from code_5
        # 1. 取得當前本地精準時間
        now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        now_epoch = time.time()
        current_trial = total_blow_trials
        
        # 2. 發送 Marker 代碼
        marker_code = '521'
        if current_trial == 30:
            send_marker(marker_code)
        
        # 3. 即時寫入 log/ 資料夾下的 CSV
        with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                participant_id,
                session_id,
                current_trial,
                "Blow_Exper_End",
                marker_code,
                now_iso,
                f"{now_epoch:.6f}",
                f"{t:.4f}"
            ])
        
        # 控制台除錯印出
        print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_End | Time: {now_iso}")
        
        total_blow_trials += 1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routine_05_Task_blow_deflate.maxDurationReached:
            routineTimer.addTime(-routine_05_Task_blow_deflate.maxDuration)
        elif routine_05_Task_blow_deflate.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        # mark thisTrial_5 as finished
        if hasattr(thisTrial_5, 'status'):
            thisTrial_5.status = FINISHED
        # if awaiting a pause, pause now
        if trials_5.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_5.status = STARTED
        thisExp.nextEntry()
        
    # completed 7 repeats of 'trials_5'
    trials_5.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_05_Task_blow" ---
    # create an object to store info about Routine routine_05_Task_blow
    routine_05_Task_blow = data.Routine(
        name='routine_05_Task_blow',
        components=[circle_border_blow, circle_guide_blow, inhale_blow, exhale_blow, text_blow],
    )
    routine_05_Task_blow.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_10
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    current_trial = total_blow_trials
    
    # 2. 發送 Marker 代碼
    marker_code = '520'
    if current_trial == 1:
        send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            current_trial,
            "Blow_Exper_Begin",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_Begin | Time: {now_iso}")
    # store start times for routine_05_Task_blow
    routine_05_Task_blow.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_05_Task_blow.tStart = globalClock.getTime(format='float')
    routine_05_Task_blow.status = STARTED
    thisExp.addData('routine_05_Task_blow.started', routine_05_Task_blow.tStart)
    routine_05_Task_blow.maxDuration = None
    # keep track of which components have finished
    routine_05_Task_blowComponents = routine_05_Task_blow.components
    for thisComponent in routine_05_Task_blow.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_05_Task_blow" ---
    thisExp.currentRoutine = routine_05_Task_blow
    routine_05_Task_blow.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *circle_border_blow* updates
        
        # if circle_border_blow is starting this frame...
        if circle_border_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_border_blow.frameNStart = frameN  # exact frame index
            circle_border_blow.tStart = t  # local t and not account for scr refresh
            circle_border_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_border_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_border_blow.started')
            # update status
            circle_border_blow.status = STARTED
            circle_border_blow.setAutoDraw(True)
        
        # if circle_border_blow is active this frame...
        if circle_border_blow.status == STARTED:
            # update params
            circle_border_blow.setLineColor('skyblue' if t < 4.0 else 'orange', log=False)
        
        # if circle_border_blow is stopping this frame...
        if circle_border_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle_border_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                circle_border_blow.tStop = t  # not accounting for scr refresh
                circle_border_blow.tStopRefresh = tThisFlipGlobal  # on global time
                circle_border_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_border_blow.stopped')
                # update status
                circle_border_blow.status = FINISHED
                circle_border_blow.setAutoDraw(False)
        
        # *circle_guide_blow* updates
        
        # if circle_guide_blow is starting this frame...
        if circle_guide_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            circle_guide_blow.frameNStart = frameN  # exact frame index
            circle_guide_blow.tStart = t  # local t and not account for scr refresh
            circle_guide_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(circle_guide_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'circle_guide_blow.started')
            # update status
            circle_guide_blow.status = STARTED
            circle_guide_blow.setAutoDraw(True)
        
        # if circle_guide_blow is active this frame...
        if circle_guide_blow.status == STARTED:
            # update params
            circle_guide_blow.setFillColor('skyblue' if t < 4.0 else 'orange', log=False)
            circle_guide_blow.setSize((0.1 + 0.5 * (t / 4.0), 0.1 + 0.5 * (t / 4.0)) if t < 4.0 else (0.6 - 0.5 * ((t - 4.0) / 6.0), 0.6 - 0.5 * ((t - 4.0) / 6.0)), log=False)
        
        # if circle_guide_blow is stopping this frame...
        if circle_guide_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > circle_guide_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                circle_guide_blow.tStop = t  # not accounting for scr refresh
                circle_guide_blow.tStopRefresh = tThisFlipGlobal  # on global time
                circle_guide_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_guide_blow.stopped')
                # update status
                circle_guide_blow.status = FINISHED
                circle_guide_blow.setAutoDraw(False)
        
        # *inhale_blow* updates
        
        # if inhale_blow is starting this frame...
        if inhale_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inhale_blow.frameNStart = frameN  # exact frame index
            inhale_blow.tStart = t  # local t and not account for scr refresh
            inhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inhale_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inhale_blow.started')
            # update status
            inhale_blow.status = STARTED
            inhale_blow.setAutoDraw(True)
        
        # if inhale_blow is active this frame...
        if inhale_blow.status == STARTED:
            # update params
            inhale_blow.setSize((0.15 + 0.05 * (t / 4.0), 0.15 + 0.05 * (t / 4.0)), log=False)
        
        # if inhale_blow is stopping this frame...
        if inhale_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > inhale_blow.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                inhale_blow.tStop = t  # not accounting for scr refresh
                inhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                inhale_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'inhale_blow.stopped')
                # update status
                inhale_blow.status = FINISHED
                inhale_blow.setAutoDraw(False)
        
        # *exhale_blow* updates
        
        # if exhale_blow is starting this frame...
        if exhale_blow.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            exhale_blow.frameNStart = frameN  # exact frame index
            exhale_blow.tStart = t  # local t and not account for scr refresh
            exhale_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exhale_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exhale_blow.started')
            # update status
            exhale_blow.status = STARTED
            exhale_blow.setAutoDraw(True)
        
        # if exhale_blow is active this frame...
        if exhale_blow.status == STARTED:
            # update params
            exhale_blow.setSize((0.2 - 0.05 * ((t - 4.0) / 6.0), 0.2 - 0.05 * ((t - 4.0) / 6.0)), log=False)
        
        # if exhale_blow is stopping this frame...
        if exhale_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exhale_blow.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                exhale_blow.tStop = t  # not accounting for scr refresh
                exhale_blow.tStopRefresh = tThisFlipGlobal  # on global time
                exhale_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exhale_blow.stopped')
                # update status
                exhale_blow.status = FINISHED
                exhale_blow.setAutoDraw(False)
        
        # *text_blow* updates
        
        # if text_blow is starting this frame...
        if text_blow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blow.frameNStart = frameN  # exact frame index
            text_blow.tStart = t  # local t and not account for scr refresh
            text_blow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blow.started')
            # update status
            text_blow.status = STARTED
            text_blow.setAutoDraw(True)
        
        # if text_blow is active this frame...
        if text_blow.status == STARTED:
            # update params
            text_blow.setText(f"鼻吸氣 ({4 - int(t)}s)" if t < 4.0 else f"吹氣球 ({10 - int(t)}s)", log=False)
        
        # if text_blow is stopping this frame...
        if text_blow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blow.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text_blow.tStop = t  # not accounting for scr refresh
                text_blow.tStopRefresh = tThisFlipGlobal  # on global time
                text_blow.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blow.stopped')
                # update status
                text_blow.status = FINISHED
                text_blow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_05_Task_blow,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_05_Task_blow.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_05_Task_blow.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_05_Task_blow.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_05_Task_blow" ---
    for thisComponent in routine_05_Task_blow.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_05_Task_blow
    routine_05_Task_blow.tStop = globalClock.getTime(format='float')
    routine_05_Task_blow.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_05_Task_blow.stopped', routine_05_Task_blow.tStop)
    # Run 'End Routine' code from code_10
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    current_trial = total_blow_trials
    
    # 2. 發送 Marker 代碼
    marker_code = '521'
    if current_trial == 30:
        send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            current_trial,
            "Blow_Exper_End",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Exper_{current_trial}_End | Time: {now_iso}")
    
    total_blow_trials += 1
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_05_Task_blow.maxDurationReached:
        routineTimer.addTime(-routine_05_Task_blow.maxDuration)
    elif routine_05_Task_blow.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_05_Task_blow_post" ---
    # create an object to store info about Routine routine_05_Task_blow_post
    routine_05_Task_blow_post = data.Routine(
        name='routine_05_Task_blow_post',
        components=[Task_blow_post, text_4],
    )
    routine_05_Task_blow_post.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '530'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Blow_Post_Begin",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Post_Begin | Time: {now_iso}")
    # store start times for routine_05_Task_blow_post
    routine_05_Task_blow_post.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_05_Task_blow_post.tStart = globalClock.getTime(format='float')
    routine_05_Task_blow_post.status = STARTED
    thisExp.addData('routine_05_Task_blow_post.started', routine_05_Task_blow_post.tStart)
    routine_05_Task_blow_post.maxDuration = None
    # keep track of which components have finished
    routine_05_Task_blow_postComponents = routine_05_Task_blow_post.components
    for thisComponent in routine_05_Task_blow_post.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_05_Task_blow_post" ---
    thisExp.currentRoutine = routine_05_Task_blow_post
    routine_05_Task_blow_post.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 180.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task_blow_post* updates
        
        # if Task_blow_post is starting this frame...
        if Task_blow_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task_blow_post.frameNStart = frameN  # exact frame index
            Task_blow_post.tStart = t  # local t and not account for scr refresh
            Task_blow_post.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task_blow_post, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Task_blow_post.started')
            # update status
            Task_blow_post.status = STARTED
            Task_blow_post.setAutoDraw(True)
        
        # if Task_blow_post is active this frame...
        if Task_blow_post.status == STARTED:
            # update params
            pass
        
        # if Task_blow_post is stopping this frame...
        if Task_blow_post.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task_blow_post.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                Task_blow_post.tStop = t  # not accounting for scr refresh
                Task_blow_post.tStopRefresh = tThisFlipGlobal  # on global time
                Task_blow_post.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Task_blow_post.stopped')
                # update status
                Task_blow_post.status = FINISHED
                Task_blow_post.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            text_4.setText(f"目前經過時間：({int(t)//60} min)", log=False)
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.tStopRefresh = tThisFlipGlobal  # on global time
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_05_Task_blow_post,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_05_Task_blow_post.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_05_Task_blow_post.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_05_Task_blow_post.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_05_Task_blow_post" ---
    for thisComponent in routine_05_Task_blow_post.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_05_Task_blow_post
    routine_05_Task_blow_post.tStop = globalClock.getTime(format='float')
    routine_05_Task_blow_post.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_05_Task_blow_post.stopped', routine_05_Task_blow_post.tStop)
    # Run 'End Routine' code from code_11
    # 1. 取得當前本地精準時間
    now_iso = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    now_epoch = time.time()
    
    # 2. 發送 Marker 代碼
    marker_code = '531'
    send_marker(marker_code)
    
    # 3. 即時寫入 log/ 資料夾下的 CSV
    with open(log_filename, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            participant_id,
            session_id,
            0,
            "Blow_Post_End",
            marker_code,
            now_iso,
            f"{now_epoch:.6f}",
            f"{t:.4f}"
        ])
    
    # 控制台除錯印出
    print(f"[Log Saved] Sub: {participant_id} | Sess: {session_id} | Event: Blow_Post_End | Time: {now_iso}")
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_05_Task_blow_post.maxDurationReached:
        routineTimer.addTime(-routine_05_Task_blow_post.maxDuration)
    elif routine_05_Task_blow_post.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-180.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "routine_06_Exper_End" ---
    # create an object to store info about Routine routine_06_Exper_End
    routine_06_Exper_End = data.Routine(
        name='routine_06_Exper_End',
        components=[Exper_End, key_resp_10],
    )
    routine_06_Exper_End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_10
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # store start times for routine_06_Exper_End
    routine_06_Exper_End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_06_Exper_End.tStart = globalClock.getTime(format='float')
    routine_06_Exper_End.status = STARTED
    thisExp.addData('routine_06_Exper_End.started', routine_06_Exper_End.tStart)
    routine_06_Exper_End.maxDuration = None
    # keep track of which components have finished
    routine_06_Exper_EndComponents = routine_06_Exper_End.components
    for thisComponent in routine_06_Exper_End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_06_Exper_End" ---
    thisExp.currentRoutine = routine_06_Exper_End
    routine_06_Exper_End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Exper_End* updates
        
        # if Exper_End is starting this frame...
        if Exper_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Exper_End.frameNStart = frameN  # exact frame index
            Exper_End.tStart = t  # local t and not account for scr refresh
            Exper_End.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Exper_End, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Exper_End.started')
            # update status
            Exper_End.status = STARTED
            Exper_End.setAutoDraw(True)
        
        # if Exper_End is active this frame...
        if Exper_End.status == STARTED:
            # update params
            pass
        
        # *key_resp_10* updates
        waitOnFlip = False
        
        # if key_resp_10 is starting this frame...
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            # update status
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_06_Exper_End,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            routine_06_Exper_End.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if routine_06_Exper_End.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in routine_06_Exper_End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_06_Exper_End" ---
    for thisComponent in routine_06_Exper_End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_06_Exper_End
    routine_06_Exper_End.tStop = globalClock.getTime(format='float')
    routine_06_Exper_End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_06_Exper_End.stopped', routine_06_Exper_End.tStop)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    thisExp.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        thisExp.addData('key_resp_10.rt', key_resp_10.rt)
        thisExp.addData('key_resp_10.duration', key_resp_10.duration)
    thisExp.nextEntry()
    # the Routine "routine_06_Exper_End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
