#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on July 25, 2022, at 15:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

'''
PI: BJ Casey

Stop Signal Task
- Optional practice block (25 trials, ~1min)
- 2 test runs; ~5min each
- 300 "Go" trials, 60 variable-delay "stop" trials; divided equally between the 2 runs
- "Stop" trials are separated by 3-7 "go" trials
- "Go" trials: 
    + R/L arrow displayed for up to 1000ms
    + if there is a response, screen immediately advances to a fixation cross, otherwise, arrow remains for 1000ms
    + fixation cross displayed for 1000ms - "go" duration + jitter
- Variable-delay "Stop" trails:
    + R/L arrow (SSD) displayed for 0-900ms; duration is adjusted on a trial-by-trial basis; starting at 50ms, duration is increased or decreased by 50ms (up to a max duration of 900ms) based on the the subject's performance/accuracy on prior "stop" trial (i.e. if previous stop trial was incorrect, the SSD duration of the next stop trial is decreased by 50ms; if previous stop trial was correct, the SSD duration of the next stop trial is increased by 50ms. If a response is detected within this window, screen immediately advances to fixation cross.
    + "stop" signal (up arrow) is displayed for 100-300ms; note: variable "go" duration + "stop" signal duration not to exceed 1000ms.
    + fixation cross displayed for 1000ms - variable "go" duration - "stop" signal duration(if presented) + jitter
'''


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = '220722_SST_ABCD_scanner_version'  # from the Builder filename that created this script
expInfo = {'participant': '', 'visit': '001/002', 'run': '001', 'trialorder': '1', 'handedness(l/r/a)': 'r'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['visit'], expInfo['run'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\OSLadmin\\Desktop\\22MoTasks\\220707SST_psychopy\\220722_SST_ABCD_scanner_version.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "TitlePage"
TitlePageClock = core.Clock()
text_titlepage = visual.TextStim(win=win, name='text_titlepage',
    text='SST',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_titlepage = keyboard.Keyboard()
right_arrow_key = 'MIDDLE'
left_arrow_key = 'POINTER'
allowed_index_key = '6'
allowed_middle_key = '7'
dominant_hand = 'right'
if expInfo['handedness(l/r/a)'] == 'l':
    right_arrow_key = 'POINTER'
    left_arrow_key = 'MIDDLE'
    allowed_index_key = '3'
    allowed_middle_key = '2'
    dominant_hand = 'left'


# Initialize components for Routine "TestReady1"
TestReady1Clock = core.Clock()
text_testready1 = visual.TextStim(win=win, name='text_testready1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_testready1 = keyboard.Keyboard()

# Initialize components for Routine "TestReady2"
TestReady2Clock = core.Clock()
text_testready2 = visual.TextStim(win=win, name='text_testready2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_testready2 = keyboard.Keyboard()

# Initialize components for Routine "TestReady3"
TestReady3Clock = core.Clock()
text_testready3 = visual.TextStim(win=win, name='text_testready3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_test_ready3 = keyboard.Keyboard()

# Initialize components for Routine "TestReady4"
TestReady4Clock = core.Clock()
text_testready4 = visual.TextStim(win=win, name='text_testready4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_testready4 = keyboard.Keyboard()

# Initialize components for Routine "Waiting4Scanner"
Waiting4ScannerClock = core.Clock()
text_waiting4scanner = visual.TextStim(win=win, name='text_waiting4scanner',
    text='Waiting for scanner...',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_waiting4scanner = keyboard.Keyboard()
text_scanner_wait = visual.TextStim(win=win, name='text_scanner_wait',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "BeginFix"
BeginFixClock = core.Clock()
text_beginfix = visual.TextStim(win=win, name='text_beginfix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
run_counter = 0

# Initialize components for Routine "Go_Stop_trial"
Go_Stop_trialClock = core.Clock()
trial_count = 0

# Xi added performance red flags
# Correct Go < 60%
PF_CG = 0
# Incorrect Go > 30%
PF_IG = 0
# Late Go > 30%
PF_LG = 0
# Go Omissions > 30%
PF_GO = 0
# Total no. Go trials < 300, for two completed runs (1 session)
PF_TNG = 0
Go_trial_count = 0
VST_count = 0
# Stop Success Rate < 20% or > 80%
PF_SSR = 0
# Stop Fail RT > Go RT by any amount (1ms or greater)
PF_SFRTvGRT = 0
CG = 0
IG = 0
LG = 0
GO = 0
SC = 0
SF = 0
SF_RT = 0
SF_RT_sum = 0
Go_RT = 0
Go_RT_sum = 0
PFlag_CG = 0
PFlag_IG = 0
PFlag_LG = 0
PFlag_GO = 0
PFlag_SSR = 0
image_stimulus = visual.ImageStim(
    win=win,
    name='image_stimulus', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_image_stimulus = keyboard.Keyboard()
image_stop = visual.ImageStim(
    win=win,
    name='image_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_image_stop = keyboard.Keyboard()

# Initialize components for Routine "Fix"
FixClock = core.Clock()
FixDur_frames = 0

'''
double check: does this mean correct response during the fixation
is also coded as hit?
'Set TrialCode
If Go.ACC = 1 Or Fix.RESP = c.GetAttrib("CorrectAnswer") Then
 c.SetAttrib "TrialCode", "CorrectGo"
Else
 c.SetAttrib "TrialCode", "IncorrectGo"
End If
'''
text_fix = visual.TextStim(win=win, name='text_fix',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_fix = keyboard.Keyboard()

# Initialize components for Routine "EndFix"
EndFixClock = core.Clock()
text_endfix = visual.TextStim(win=win, name='text_endfix',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block_feedback"
Block_feedbackClock = core.Clock()
# default block feedback msg when no block-based red flag was raised 
block_feedback_msg = ''
text_block_feedback = visual.TextStim(win=win, name='text_block_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_block_feedback = keyboard.Keyboard()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_goodbye = visual.TextStim(win=win, name='text_goodbye',
    text='All done!',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_goodbye = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TitlePage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_titlepage.keys = []
key_resp_titlepage.rt = []
_key_resp_titlepage_allKeys = []
# keep track of which components have finished
TitlePageComponents = [text_titlepage, key_resp_titlepage]
for thisComponent in TitlePageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TitlePageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TitlePage"-------
while continueRoutine:
    # get current time
    t = TitlePageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TitlePageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_titlepage* updates
    if text_titlepage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_titlepage.frameNStart = frameN  # exact frame index
        text_titlepage.tStart = t  # local t and not account for scr refresh
        text_titlepage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_titlepage, 'tStartRefresh')  # time at next scr refresh
        text_titlepage.setAutoDraw(True)
    
    # *key_resp_titlepage* updates
    waitOnFlip = False
    if key_resp_titlepage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_titlepage.frameNStart = frameN  # exact frame index
        key_resp_titlepage.tStart = t  # local t and not account for scr refresh
        key_resp_titlepage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_titlepage, 'tStartRefresh')  # time at next scr refresh
        key_resp_titlepage.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_titlepage.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_titlepage.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_titlepage.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_titlepage.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_titlepage_allKeys.extend(theseKeys)
        if len(_key_resp_titlepage_allKeys):
            key_resp_titlepage.keys = _key_resp_titlepage_allKeys[-1].name  # just the last key pressed
            key_resp_titlepage.rt = _key_resp_titlepage_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TitlePageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TitlePage"-------
for thisComponent in TitlePageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_titlepage.started', text_titlepage.tStartRefresh)
thisExp.addData('text_titlepage.stopped', text_titlepage.tStopRefresh)
# check responses
if key_resp_titlepage.keys in ['', [], None]:  # No response was made
    key_resp_titlepage.keys = None
thisExp.addData('key_resp_titlepage.keys',key_resp_titlepage.keys)
if key_resp_titlepage.keys != None:  # we had a response
    thisExp.addData('key_resp_titlepage.rt', key_resp_titlepage.rt)
thisExp.addData('key_resp_titlepage.started', key_resp_titlepage.tStartRefresh)
thisExp.addData('key_resp_titlepage.stopped', key_resp_titlepage.tStopRefresh)
thisExp.nextEntry()
# the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_RunProc = data.TrialHandler(nReps=(3-int(expInfo['run'])), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_RunProc')
thisExp.addLoop(trials_RunProc)  # add the loop to the experiment
thisTrials_RunProc = trials_RunProc.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_RunProc.rgb)
if thisTrials_RunProc != None:
    for paramName in thisTrials_RunProc:
        exec('{} = thisTrials_RunProc[paramName]'.format(paramName))

for thisTrials_RunProc in trials_RunProc:
    currentLoop = trials_RunProc
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_RunProc.rgb)
    if thisTrials_RunProc != None:
        for paramName in thisTrials_RunProc:
            exec('{} = thisTrials_RunProc[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TestReady1"-------
    continueRoutine = True
    # update component parameters for each repeat
    test_ready_instruction1 = 'We are now ready to begin the game! \n\nPress your %s pointer finger to continue.'%(dominant_hand)
    text_testready1.setText(test_ready_instruction1)
    key_resp_testready1.keys = []
    key_resp_testready1.rt = []
    _key_resp_testready1_allKeys = []
    # keep track of which components have finished
    TestReady1Components = [text_testready1, key_resp_testready1]
    for thisComponent in TestReady1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestReady1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestReady1"-------
    while continueRoutine:
        # get current time
        t = TestReady1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestReady1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_testready1* updates
        if text_testready1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_testready1.frameNStart = frameN  # exact frame index
            text_testready1.tStart = t  # local t and not account for scr refresh
            text_testready1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_testready1, 'tStartRefresh')  # time at next scr refresh
            text_testready1.setAutoDraw(True)
        
        # *key_resp_testready1* updates
        waitOnFlip = False
        if key_resp_testready1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_testready1.frameNStart = frameN  # exact frame index
            key_resp_testready1.tStart = t  # local t and not account for scr refresh
            key_resp_testready1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_testready1, 'tStartRefresh')  # time at next scr refresh
            key_resp_testready1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_testready1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_testready1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_testready1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_testready1.getKeys(keyList=[allowed_index_key, 'space'], waitRelease=False)
            _key_resp_testready1_allKeys.extend(theseKeys)
            if len(_key_resp_testready1_allKeys):
                key_resp_testready1.keys = _key_resp_testready1_allKeys[-1].name  # just the last key pressed
                key_resp_testready1.rt = _key_resp_testready1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestReady1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestReady1"-------
    for thisComponent in TestReady1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_testready1.started', text_testready1.tStartRefresh)
    trials_RunProc.addData('text_testready1.stopped', text_testready1.tStopRefresh)
    # check responses
    if key_resp_testready1.keys in ['', [], None]:  # No response was made
        key_resp_testready1.keys = None
    trials_RunProc.addData('key_resp_testready1.keys',key_resp_testready1.keys)
    if key_resp_testready1.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_testready1.rt', key_resp_testready1.rt)
    trials_RunProc.addData('key_resp_testready1.started', key_resp_testready1.tStartRefresh)
    trials_RunProc.addData('key_resp_testready1.stopped', key_resp_testready1.tStopRefresh)
    # the Routine "TestReady1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TestReady2"-------
    continueRoutine = True
    # update component parameters for each repeat
    test_ready_instruction2 = 'REMEMBER: When you see the LEFT arrow, press your %s %s finger.\nWhen you see the RIGHT arrow, press your %s %s finger.\n\nPress your %s pointer finger to continue.'%(dominant_hand, left_arrow_key, dominant_hand, right_arrow_key, dominant_hand)
    text_testready2.setText(test_ready_instruction2)
    key_resp_testready2.keys = []
    key_resp_testready2.rt = []
    _key_resp_testready2_allKeys = []
    # keep track of which components have finished
    TestReady2Components = [text_testready2, key_resp_testready2]
    for thisComponent in TestReady2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestReady2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestReady2"-------
    while continueRoutine:
        # get current time
        t = TestReady2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestReady2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_testready2* updates
        if text_testready2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_testready2.frameNStart = frameN  # exact frame index
            text_testready2.tStart = t  # local t and not account for scr refresh
            text_testready2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_testready2, 'tStartRefresh')  # time at next scr refresh
            text_testready2.setAutoDraw(True)
        
        # *key_resp_testready2* updates
        waitOnFlip = False
        if key_resp_testready2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_testready2.frameNStart = frameN  # exact frame index
            key_resp_testready2.tStart = t  # local t and not account for scr refresh
            key_resp_testready2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_testready2, 'tStartRefresh')  # time at next scr refresh
            key_resp_testready2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_testready2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_testready2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_testready2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_testready2.getKeys(keyList=[allowed_index_key, 'space'], waitRelease=False)
            _key_resp_testready2_allKeys.extend(theseKeys)
            if len(_key_resp_testready2_allKeys):
                key_resp_testready2.keys = _key_resp_testready2_allKeys[-1].name  # just the last key pressed
                key_resp_testready2.rt = _key_resp_testready2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestReady2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestReady2"-------
    for thisComponent in TestReady2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_testready2.started', text_testready2.tStartRefresh)
    trials_RunProc.addData('text_testready2.stopped', text_testready2.tStopRefresh)
    # check responses
    if key_resp_testready2.keys in ['', [], None]:  # No response was made
        key_resp_testready2.keys = None
    trials_RunProc.addData('key_resp_testready2.keys',key_resp_testready2.keys)
    if key_resp_testready2.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_testready2.rt', key_resp_testready2.rt)
    trials_RunProc.addData('key_resp_testready2.started', key_resp_testready2.tStartRefresh)
    trials_RunProc.addData('key_resp_testready2.stopped', key_resp_testready2.tStopRefresh)
    # the Routine "TestReady2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TestReady3"-------
    continueRoutine = True
    # update component parameters for each repeat
    test_ready_instruction3 = 'If you see an UP arrow, STOP yourself from pressing to the left or the right arrow.\n\nPress your %s middle finger to continue.'%(dominant_hand)
    text_testready3.setText(test_ready_instruction3)
    key_resp_test_ready3.keys = []
    key_resp_test_ready3.rt = []
    _key_resp_test_ready3_allKeys = []
    # keep track of which components have finished
    TestReady3Components = [text_testready3, key_resp_test_ready3]
    for thisComponent in TestReady3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestReady3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestReady3"-------
    while continueRoutine:
        # get current time
        t = TestReady3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestReady3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_testready3* updates
        if text_testready3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_testready3.frameNStart = frameN  # exact frame index
            text_testready3.tStart = t  # local t and not account for scr refresh
            text_testready3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_testready3, 'tStartRefresh')  # time at next scr refresh
            text_testready3.setAutoDraw(True)
        
        # *key_resp_test_ready3* updates
        waitOnFlip = False
        if key_resp_test_ready3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_test_ready3.frameNStart = frameN  # exact frame index
            key_resp_test_ready3.tStart = t  # local t and not account for scr refresh
            key_resp_test_ready3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_test_ready3, 'tStartRefresh')  # time at next scr refresh
            key_resp_test_ready3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_test_ready3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_test_ready3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_test_ready3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_test_ready3.getKeys(keyList=[allowed_middle_key, 'space'], waitRelease=False)
            _key_resp_test_ready3_allKeys.extend(theseKeys)
            if len(_key_resp_test_ready3_allKeys):
                key_resp_test_ready3.keys = _key_resp_test_ready3_allKeys[-1].name  # just the last key pressed
                key_resp_test_ready3.rt = _key_resp_test_ready3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestReady3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestReady3"-------
    for thisComponent in TestReady3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_testready3.started', text_testready3.tStartRefresh)
    trials_RunProc.addData('text_testready3.stopped', text_testready3.tStopRefresh)
    # check responses
    if key_resp_test_ready3.keys in ['', [], None]:  # No response was made
        key_resp_test_ready3.keys = None
    trials_RunProc.addData('key_resp_test_ready3.keys',key_resp_test_ready3.keys)
    if key_resp_test_ready3.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_test_ready3.rt', key_resp_test_ready3.rt)
    trials_RunProc.addData('key_resp_test_ready3.started', key_resp_test_ready3.tStartRefresh)
    trials_RunProc.addData('key_resp_test_ready3.stopped', key_resp_test_ready3.tStopRefresh)
    # the Routine "TestReady3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TestReady4"-------
    continueRoutine = True
    # update component parameters for each repeat
    test_ready_instruction4 = 'Press the correct key as FAST as you can. Stopping and going are equally important!\n\nPress your %s middle finger to continue.'%(dominant_hand)
    text_testready4.setText(test_ready_instruction4)
    key_resp_testready4.keys = []
    key_resp_testready4.rt = []
    _key_resp_testready4_allKeys = []
    # keep track of which components have finished
    TestReady4Components = [text_testready4, key_resp_testready4]
    for thisComponent in TestReady4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestReady4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestReady4"-------
    while continueRoutine:
        # get current time
        t = TestReady4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestReady4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_testready4* updates
        if text_testready4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_testready4.frameNStart = frameN  # exact frame index
            text_testready4.tStart = t  # local t and not account for scr refresh
            text_testready4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_testready4, 'tStartRefresh')  # time at next scr refresh
            text_testready4.setAutoDraw(True)
        
        # *key_resp_testready4* updates
        waitOnFlip = False
        if key_resp_testready4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_testready4.frameNStart = frameN  # exact frame index
            key_resp_testready4.tStart = t  # local t and not account for scr refresh
            key_resp_testready4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_testready4, 'tStartRefresh')  # time at next scr refresh
            key_resp_testready4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_testready4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_testready4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_testready4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_testready4.getKeys(keyList=[allowed_middle_key, 'space'], waitRelease=False)
            _key_resp_testready4_allKeys.extend(theseKeys)
            if len(_key_resp_testready4_allKeys):
                key_resp_testready4.keys = _key_resp_testready4_allKeys[-1].name  # just the last key pressed
                key_resp_testready4.rt = _key_resp_testready4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestReady4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestReady4"-------
    for thisComponent in TestReady4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_testready4.started', text_testready4.tStartRefresh)
    trials_RunProc.addData('text_testready4.stopped', text_testready4.tStopRefresh)
    # check responses
    if key_resp_testready4.keys in ['', [], None]:  # No response was made
        key_resp_testready4.keys = None
    trials_RunProc.addData('key_resp_testready4.keys',key_resp_testready4.keys)
    if key_resp_testready4.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_testready4.rt', key_resp_testready4.rt)
    trials_RunProc.addData('key_resp_testready4.started', key_resp_testready4.tStartRefresh)
    trials_RunProc.addData('key_resp_testready4.stopped', key_resp_testready4.tStopRefresh)
    # the Routine "TestReady4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Waiting4Scanner"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_waiting4scanner.keys = []
    key_resp_waiting4scanner.rt = []
    _key_resp_waiting4scanner_allKeys = []
    # keep track of which components have finished
    Waiting4ScannerComponents = [text_waiting4scanner, key_resp_waiting4scanner, text_scanner_wait]
    for thisComponent in Waiting4ScannerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Waiting4ScannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Waiting4Scanner"-------
    while continueRoutine:
        # get current time
        t = Waiting4ScannerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Waiting4ScannerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_waiting4scanner* updates
        if text_waiting4scanner.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_waiting4scanner.frameNStart = frameN  # exact frame index
            text_waiting4scanner.tStart = t  # local t and not account for scr refresh
            text_waiting4scanner.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_waiting4scanner, 'tStartRefresh')  # time at next scr refresh
            text_waiting4scanner.setAutoDraw(True)
        
        # *key_resp_waiting4scanner* updates
        waitOnFlip = False
        if key_resp_waiting4scanner.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_waiting4scanner.frameNStart = frameN  # exact frame index
            key_resp_waiting4scanner.tStart = t  # local t and not account for scr refresh
            key_resp_waiting4scanner.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_waiting4scanner, 'tStartRefresh')  # time at next scr refresh
            key_resp_waiting4scanner.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_waiting4scanner.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_waiting4scanner.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_waiting4scanner.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_waiting4scanner.getKeys(keyList=['apostrophe'], waitRelease=False)
            _key_resp_waiting4scanner_allKeys.extend(theseKeys)
            if len(_key_resp_waiting4scanner_allKeys):
                key_resp_waiting4scanner.keys = _key_resp_waiting4scanner_allKeys[-1].name  # just the last key pressed
                key_resp_waiting4scanner.rt = _key_resp_waiting4scanner_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_scanner_wait* updates
        if text_scanner_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_scanner_wait.frameNStart = frameN  # exact frame index
            text_scanner_wait.tStart = t  # local t and not account for scr refresh
            text_scanner_wait.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_scanner_wait, 'tStartRefresh')  # time at next scr refresh
            text_scanner_wait.setAutoDraw(True)
        if text_scanner_wait.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_scanner_wait.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_scanner_wait.tStop = t  # not accounting for scr refresh
                text_scanner_wait.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_scanner_wait, 'tStopRefresh')  # time at next scr refresh
                text_scanner_wait.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting4ScannerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Waiting4Scanner"-------
    for thisComponent in Waiting4ScannerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_waiting4scanner.started', text_waiting4scanner.tStartRefresh)
    trials_RunProc.addData('text_waiting4scanner.stopped', text_waiting4scanner.tStopRefresh)
    # check responses
    if key_resp_waiting4scanner.keys in ['', [], None]:  # No response was made
        key_resp_waiting4scanner.keys = None
    trials_RunProc.addData('key_resp_waiting4scanner.keys',key_resp_waiting4scanner.keys)
    if key_resp_waiting4scanner.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_waiting4scanner.rt', key_resp_waiting4scanner.rt)
    trials_RunProc.addData('key_resp_waiting4scanner.started', key_resp_waiting4scanner.tStartRefresh)
    trials_RunProc.addData('key_resp_waiting4scanner.stopped', key_resp_waiting4scanner.tStopRefresh)
    trials_RunProc.addData('text_scanner_wait.started', text_scanner_wait.tStartRefresh)
    trials_RunProc.addData('text_scanner_wait.stopped', text_scanner_wait.tStopRefresh)
    # the Routine "Waiting4Scanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "BeginFix"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # variables that refresh after each run/block
    block_trial_count = 0
    run_counter += 1
    
    go_stop_trial_dur_frames = int(1*1000/(1000/round(expInfo['frameRate'])))
    SSD = .05
    PrevStopACC = 0
    STEflag = 0
    STEcount = 0
    STEadjstop_nback = 0
    updated_trial_label = ''
    prev_VST_trial_num = 0
    real_stop_nback = 0
    block_VST_count = 0
    
    # block-based performance variables refresh for each run
    block_Go_trial_count = 0
    block_VST_count = 0
    block_CG = 0
    block_IG = 0
    block_LG = 0
    block_GO = 0
    block_SF = 0
    block_SC = 0
    block_PF_CG = 0
    block_PF_IG = 0
    block_PF_LG = 0
    block_PF_GO = 0
    block_PF_SSR = 0
    block_SF_RT = 0
    block_SF_RT_sum = 0
    block_Go_RT = 0
    block_Go_RT_sum = 0
    
    Block_PF_TNG = 0
    Block_PFlag_CG = 0
    Block_PFlag_IG = 0
    Block_PFlag_LG = 0
    Block_PFlag_GO = 0
    Block_PFlag_SSR = 0
    Block_PF_SFRTvGRT = 0
    
    block_variable_stop_trial_success_percentage= 0
    # keep track of which components have finished
    BeginFixComponents = [text_beginfix]
    for thisComponent in BeginFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BeginFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BeginFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BeginFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BeginFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_beginfix* updates
        if text_beginfix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_beginfix.frameNStart = frameN  # exact frame index
            text_beginfix.tStart = t  # local t and not account for scr refresh
            text_beginfix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_beginfix, 'tStartRefresh')  # time at next scr refresh
            text_beginfix.setAutoDraw(True)
        if text_beginfix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_beginfix.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_beginfix.tStop = t  # not accounting for scr refresh
                text_beginfix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_beginfix, 'tStopRefresh')  # time at next scr refresh
                text_beginfix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BeginFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BeginFix"-------
    for thisComponent in BeginFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_beginfix.started', text_beginfix.tStartRefresh)
    trials_RunProc.addData('text_beginfix.stopped', text_beginfix.tStopRefresh)
    if int(expInfo['run']) == 1 and run_counter == 1:
        if int(expInfo['trialorder']) == 1:
            conditions_file = 'Time_versions/TestList1A.xlsx'
    else:
        conditions_file = 'Time_versions/TestList1B.xlsx'
    
    # record frame duration after system initialization
    # send warning if frames are dropped
    # 4ms difference is tolerated as 4ms*180trials <1s
    '''win = visual.Window()
    win.recordFrameIntervals = True
    logging.console.setLevel(logging.WARNING)
    print('Overall, %i frames were dropped.' % win.nDroppedFrames)
    '''
    
    # set up handler to look after randomisation of conditions etc
    trials_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conditions_file),
        seed=None, name='trials_loop')
    thisExp.addLoop(trials_loop)  # add the loop to the experiment
    thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    for thisTrials_loop in trials_loop:
        currentLoop = trials_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
        if thisTrials_loop != None:
            for paramName in thisTrials_loop:
                exec('{} = thisTrials_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Go_Stop_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        if STEflag == 1:
            trial_type = 'VariableStopTrial'
        
        if trial_type == 'GoTrial':
            image_stimulus_dur_frames = int(1*1000/(1000/expInfo['frameRate']))
            image_stop_dur_frames = 0
        elif trial_type == 'VariableStopTrial':
            if STEflag == 0:
                if block_VST_count > 0:
                    SSD = SSD + (PrevStopACC*2-1) *.05
                    # if the previous VST inhibition is successful, the next VST gets harder with longer SSD
                    # if the previous VST inhibition is unsuccessful, the next VST gets easier with shorter SSD
                    if SSD < .05:
                        SSD = .05
                        # based on the paper, SSD min will be 50ms, so the go sign will always be presented on VSTs
                    elif SSD > .9:
                        SSD = .9
                        # this is the SSDmax in ABCD's version
                        # it appears that VST length >1sec is later compensated by shorter end fixation duration (5s by default)
                        # however, this is not shown in the ABCD's script
                # first ever stop trial, SSD is defaulted to be 50ms
            elif STEflag == 1:
                if SSD < .1 or SSD == .1:
                    SSD = .05
                    STEflag = 0
                else:
                    SSD = SSD - .1
                    STEflag = 0
            image_stimulus_dur_frames = int(SSD*1000/(1000/expInfo['frameRate']))
            image_stop_dur_frames = int(.3*1000/(1000/expInfo['frameRate']))
        image_stimulus.setImage(stimulus)
        key_resp_image_stimulus.keys = []
        key_resp_image_stimulus.rt = []
        _key_resp_image_stimulus_allKeys = []
        image_stop.setImage('images/Stop_Arrow.BMP')
        key_resp_image_stop.keys = []
        key_resp_image_stop.rt = []
        _key_resp_image_stop_allKeys = []
        # keep track of which components have finished
        Go_Stop_trialComponents = [image_stimulus, key_resp_image_stimulus, image_stop, key_resp_image_stop]
        for thisComponent in Go_Stop_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Go_Stop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Go_Stop_trial"-------
        while continueRoutine:
            # get current time
            t = Go_Stop_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Go_Stop_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stimulus* updates
            if image_stimulus.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                image_stimulus.frameNStart = frameN  # exact frame index
                image_stimulus.tStart = t  # local t and not account for scr refresh
                image_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stimulus, 'tStartRefresh')  # time at next scr refresh
                image_stimulus.setAutoDraw(True)
            if image_stimulus.status == STARTED:
                if frameN >= (image_stimulus.frameNStart + image_stimulus_dur_frames):
                    # keep track of stop time/frame for later
                    image_stimulus.tStop = t  # not accounting for scr refresh
                    image_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_stimulus, 'tStopRefresh')  # time at next scr refresh
                    image_stimulus.setAutoDraw(False)
            
            # *key_resp_image_stimulus* updates
            waitOnFlip = False
            if key_resp_image_stimulus.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                key_resp_image_stimulus.frameNStart = frameN  # exact frame index
                key_resp_image_stimulus.tStart = t  # local t and not account for scr refresh
                key_resp_image_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_image_stimulus, 'tStartRefresh')  # time at next scr refresh
                key_resp_image_stimulus.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_image_stimulus.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_image_stimulus.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_image_stimulus.status == STARTED:
                if frameN >= (key_resp_image_stimulus.frameNStart + image_stimulus_dur_frames):
                    # keep track of stop time/frame for later
                    key_resp_image_stimulus.tStop = t  # not accounting for scr refresh
                    key_resp_image_stimulus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_image_stimulus, 'tStopRefresh')  # time at next scr refresh
                    key_resp_image_stimulus.status = FINISHED
            if key_resp_image_stimulus.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_image_stimulus.getKeys(keyList=[allowed_middle_key, allowed_index_key], waitRelease=False)
                _key_resp_image_stimulus_allKeys.extend(theseKeys)
                if len(_key_resp_image_stimulus_allKeys):
                    key_resp_image_stimulus.keys = _key_resp_image_stimulus_allKeys[0].name  # just the first key pressed
                    key_resp_image_stimulus.rt = _key_resp_image_stimulus_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_stop* updates
            if image_stop.status == NOT_STARTED and image_stimulus.status==FINISHED:
                # keep track of start time/frame for later
                image_stop.frameNStart = frameN  # exact frame index
                image_stop.tStart = t  # local t and not account for scr refresh
                image_stop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stop, 'tStartRefresh')  # time at next scr refresh
                image_stop.setAutoDraw(True)
            if image_stop.status == STARTED:
                if frameN >= (image_stop.frameNStart + image_stop_dur_frames):
                    # keep track of stop time/frame for later
                    image_stop.tStop = t  # not accounting for scr refresh
                    image_stop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_stop, 'tStopRefresh')  # time at next scr refresh
                    image_stop.setAutoDraw(False)
            
            # *key_resp_image_stop* updates
            waitOnFlip = False
            if key_resp_image_stop.status == NOT_STARTED and image_stimulus.status==FINISHED:
                # keep track of start time/frame for later
                key_resp_image_stop.frameNStart = frameN  # exact frame index
                key_resp_image_stop.tStart = t  # local t and not account for scr refresh
                key_resp_image_stop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_image_stop, 'tStartRefresh')  # time at next scr refresh
                key_resp_image_stop.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_image_stop.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_image_stop.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_image_stop.status == STARTED:
                if frameN >= (key_resp_image_stop.frameNStart + image_stop_dur_frames):
                    # keep track of stop time/frame for later
                    key_resp_image_stop.tStop = t  # not accounting for scr refresh
                    key_resp_image_stop.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_image_stop, 'tStopRefresh')  # time at next scr refresh
                    key_resp_image_stop.status = FINISHED
            if key_resp_image_stop.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_image_stop.getKeys(keyList=[allowed_middle_key, allowed_index_key], waitRelease=False)
                _key_resp_image_stop_allKeys.extend(theseKeys)
                if len(_key_resp_image_stop_allKeys):
                    key_resp_image_stop.keys = _key_resp_image_stop_allKeys[0].name  # just the first key pressed
                    key_resp_image_stop.rt = _key_resp_image_stop_allKeys[0].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Go_Stop_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Go_Stop_trial"-------
        for thisComponent in Go_Stop_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if trial_type == 'VariableStopTrial':
            if key_resp_image_stimulus.keys in ['', [], None]:
                STEflag = 0
            else:
                STEflag = 1
        trials_loop.addData('image_stimulus.started', image_stimulus.tStartRefresh)
        trials_loop.addData('image_stimulus.stopped', image_stimulus.tStopRefresh)
        # check responses
        if key_resp_image_stimulus.keys in ['', [], None]:  # No response was made
            key_resp_image_stimulus.keys = None
        trials_loop.addData('key_resp_image_stimulus.keys',key_resp_image_stimulus.keys)
        if key_resp_image_stimulus.keys != None:  # we had a response
            trials_loop.addData('key_resp_image_stimulus.rt', key_resp_image_stimulus.rt)
        trials_loop.addData('key_resp_image_stimulus.started', key_resp_image_stimulus.tStartRefresh)
        trials_loop.addData('key_resp_image_stimulus.stopped', key_resp_image_stimulus.tStopRefresh)
        trials_loop.addData('image_stop.started', image_stop.tStartRefresh)
        trials_loop.addData('image_stop.stopped', image_stop.tStopRefresh)
        # check responses
        if key_resp_image_stop.keys in ['', [], None]:  # No response was made
            key_resp_image_stop.keys = None
        trials_loop.addData('key_resp_image_stop.keys',key_resp_image_stop.keys)
        if key_resp_image_stop.keys != None:  # we had a response
            trials_loop.addData('key_resp_image_stop.rt', key_resp_image_stop.rt)
        trials_loop.addData('key_resp_image_stop.started', key_resp_image_stop.tStartRefresh)
        trials_loop.addData('key_resp_image_stop.stopped', key_resp_image_stop.tStopRefresh)
        # the Routine "Go_Stop_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Fix"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Calculate trial fixation duration
        if trial_type == 'GoTrial':
            if key_resp_image_stimulus.keys != None:
                # to make timing more accurate
                FixDur_frames = int((1 - key_resp_image_stimulus.rt + jitter)*1000/(1000/expInfo['frameRate']))
            else:
                FixDur_frames = int(jitter*1000/(1000/expInfo['frameRate']))
        elif trial_type == 'VariableStopTrial':
            if STEflag == 0:
                #if key_resp_image_stimulus.keys in ['', [], None]:
                FixDur_frames = int((1 - SSD - .3 + jitter)*1000/(1000/expInfo['frameRate']))
                #elif key_resp_image_stop.keys != None:  
                    # FixDur = 1 - SSD - key_resp_image_stop.rt + jitter
                    # ABCD's 21 version: so failed inhibition when the stop sign came up
                    # may make a trial longer (.3-key_resp_image_stop.rt)
            if STEflag == 1:
                FixDur_frames = int((1 - key_resp_image_stimulus.rt + jitter)*1000/(1000/expInfo['frameRate']))
                # FixDur = 1 - key_resp_image_stimulus.rt - .3 + jitter
                # ABCD's 21 version, so STE makes a trial shorter
        text_fix.setText('+')
        key_resp_fix.keys = []
        key_resp_fix.rt = []
        _key_resp_fix_allKeys = []
        # keep track of which components have finished
        FixComponents = [text_fix, key_resp_fix]
        for thisComponent in FixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Fix"-------
        while continueRoutine:
            # get current time
            t = FixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fix* updates
            if text_fix.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                text_fix.frameNStart = frameN  # exact frame index
                text_fix.tStart = t  # local t and not account for scr refresh
                text_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fix, 'tStartRefresh')  # time at next scr refresh
                text_fix.setAutoDraw(True)
            if text_fix.status == STARTED:
                if frameN >= (text_fix.frameNStart + FixDur_frames):
                    # keep track of stop time/frame for later
                    text_fix.tStop = t  # not accounting for scr refresh
                    text_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_fix, 'tStopRefresh')  # time at next scr refresh
                    text_fix.setAutoDraw(False)
            
            # *key_resp_fix* updates
            waitOnFlip = False
            if key_resp_fix.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                key_resp_fix.frameNStart = frameN  # exact frame index
                key_resp_fix.tStart = t  # local t and not account for scr refresh
                key_resp_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_fix, 'tStartRefresh')  # time at next scr refresh
                key_resp_fix.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_fix.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_fix.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_fix.status == STARTED:
                if frameN >= (key_resp_fix.frameNStart + FixDur_frames):
                    # keep track of stop time/frame for later
                    key_resp_fix.tStop = t  # not accounting for scr refresh
                    key_resp_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_fix, 'tStopRefresh')  # time at next scr refresh
                    key_resp_fix.status = FINISHED
            if key_resp_fix.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_fix.getKeys(keyList=[allowed_middle_key, allowed_index_key], waitRelease=False)
                _key_resp_fix_allKeys.extend(theseKeys)
                if len(_key_resp_fix_allKeys):
                    key_resp_fix.keys = _key_resp_fix_allKeys[0].name  # just the first key pressed
                    key_resp_fix.rt = _key_resp_fix_allKeys[0].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fix"-------
        for thisComponent in FixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # on variable stop trials, successful inhibition means 0 keypress throughout the trial including during the fixation and jitter
        # two types of inhibition "failure": 1. key press post SSD; 2. STE (stop trigger error): key  press during SSD before stop signal (participant's fast and correct hit)
        block_trial_count += 1
        trial_count += 1
        if trial_type == 'GoTrial':
            block_Go_trial_count += 1
            Go_trial_count += 1
            real_stop_nback = 0
            if key_resp_image_stimulus.keys != None:
                block_Go_RT_sum = block_Go_RT_sum + key_resp_image_stimulus.rt
                Go_RT_sum = Go_RT_sum + key_resp_image_stimulus.rt
                block_Go_RT = block_Go_RT_sum/block_Go_trial_count
                Go_RT = Go_RT_sum/Go_trial_count
                if key_resp_image_stimulus.keys in str(correct_answer):
                    updated_trial_label = "correct_go"
                    block_CG += 1
                    CG += 1
                else: 
                    updated_trial_label = "incorrect_go"
                    block_IG += 1
                    IG += 1
            elif key_resp_image_stimulus.keys in ['', [], None]:
                if key_resp_fix.keys in ['', [], None]:
                    # go omission's RT is regarded to be the trial duration
                    # if this calculation is not ideal, please remove GO trials
                    # in your later go rt calculation
                    block_Go_RT_sum = block_Go_RT_sum + 1 + jitter
                    Go_RT_sum = Go_RT_sum + 1 + jitter
                    block_Go_RT = block_Go_RT_sum/block_Go_trial_count
                    Go_RT = Go_RT_sum/Go_trial_count
                    updated_trial_label = "go_omission"
                    block_GO += 1 # GO is go omission, unlike Go, which is go trials
                    GO += 1
                elif key_resp_fix.keys != None:
                    block_Go_RT_sum = block_Go_RT_sum + 1 + key_resp_fix.rt
                    Go_RT_sum = Go_RT_sum + 1 + key_resp_fix.rt
                    block_Go_RT = block_Go_RT_sum/block_Go_trial_count
                    Go_RT = Go_RT_sum/Go_trial_count
                    # this errror include both correct and incorrect late gos during the fixation
                    updated_trial_label = "late_go"
                    block_LG += 1
                    LG += 1
        elif trial_type == 'VariableStopTrial':
            STEcount += STEflag
            if STEflag == 0:
                block_VST_count += 1
                VST_count += 1
                if key_resp_image_stop.keys in ['', [], None] and key_resp_fix.keys in ['', [], None]:
                    PrevStopACC = 1
                    updated_trial_label = "stop_correct"
                    block_SC += 1
                    SC += 1
                elif key_resp_image_stop.keys != None or key_resp_fix.keys != None:
                    PrevStopACC = 0
                    updated_trial_label = "stop_failure"
                    block_SF += 1
                    SF += 1
                    if key_resp_image_stop.keys != None:
                        block_SF_RT_sum = block_SF_RT_sum + SSD + key_resp_image_stop.rt
                        SF_RT_sum = SF_RT_sum + SSD + key_resp_image_stop.rt
                    elif key_resp_image_stop.keys in ['', [], None] and key_resp_fix.keys != None:
                        block_SF_RT_sum = block_SF_RT_sum + SSD + .3 + key_resp_fix.rt
                        SF_RT_sum = SF_RT_sum + SSD + .3 + key_resp_fix.rt
                    block_SF_RT = block_SF_RT_sum/block_SF
                    SF_RT = SF_RT_sum/SF
                if prev_VST_trial_num == 0:
                    real_stop_nback = block_trial_count - 1
                else:
                    real_stop_nback = block_trial_count - prev_VST_trial_num - 1
                prev_VST_trial_num = block_trial_count
            elif STEflag == 1:
                block_Go_trial_count += 1
                real_stop_nback = 0
                # as STE is no longer counted as a VST in this version
                Go_trial_count += 1
                block_Go_RT_sum = block_Go_RT_sum + key_resp_image_stimulus.rt
                Go_RT_sum = Go_RT_sum + key_resp_image_stimulus.rt
                block_Go_RT = block_Go_RT_sum/block_Go_trial_count
                Go_RT = Go_RT_sum/Go_trial_count
                if key_resp_image_stimulus.keys in str(correct_answer):
                    updated_trial_label = "STE_correct_go"
                    block_CG += 1
                    CG += 1
                else: 
                    updated_trial_label = "STE_incorrect_go"
                    block_IG += 1
                    IG += 1
        
        if block_VST_count > 0:
            block_PF_SSR = block_SC/block_VST_count
            PF_SSR = SC/VST_count
        if block_Go_trial_count > 0:
            block_PF_CG = block_CG/block_Go_trial_count
            PF_CG = CG/Go_trial_count
            block_PF_IG = block_IG/block_Go_trial_count
            PF_IG = IG/Go_trial_count
            block_PF_LG = block_LG/block_Go_trial_count
            PF_LG = LG/Go_trial_count
            block_PF_GO = block_GO/block_Go_trial_count
            PF_GO = GO/Go_trial_count
        # correct_go & incorrect_go are computed separately
        # from STE correct and incorrect go trials
        # only the first key press is recorded; please change if 
        # you need. It may be over-complicated to examine additional key presses
        # (quick correction, multiple key presses)
        
        # the original ABCD's script also updates stop_nback in
        # the original list; this version tracks updated stop_nback
        # instead
        
        # Go_RT, calculated here, is the average response time on all types of Go trials including STE, go omissions
        # SF_RT, calculated here, is the average response time on only the failed stop trials
        
        thisExp.addData('updated_trial_label', updated_trial_label)
        thisExp.addData('real_stop_nback', real_stop_nback)
        
        '''script debugging variables
        thisExp.addData('STEflag', STEflag)
        thisExp.addData('image_stop_dur_frames', image_stop_dur_frames)
        thisExp.addData('image_stimulus_dur_frames', image_stimulus_dur_frames)
        thisExp.addData('SSD', SSD)
        thisExp.addData('FixDur', FixDur_frames)
        
        thisExp.addData('recorded_key_resp_go_stop_trial', key_resp_image_stimulus.rt)
        thisExp.addData('recorded_key_resp_image_stop.rt', key_resp_image_stop.rt)
        thisExp.addData('recorded_key_resp_fix.rt', key_resp_fix.rt)
        
        # constantly updated performance red flags
        # Go trial stats include STE trials as participants are naive to the actual trial type, 
        # so their STE responses shall be included in computing their overall go trial performance
        
        # 1 means red flag
        thisExp.addData('block_trial_count', block_trial_count)
        thisExp.addData('block_Go_trial_count', block_Go_trial_count)
        thisExp.addData('block_VST_count', block_VST_count)
        thisExp.addData('block_CG', block_CG)
        thisExp.addData('block_IG', block_IG)
        thisExp.addData('block_LG', block_LG)
        thisExp.addData('block_GO', block_GO)
        thisExp.addData('block_SF', block_SF)
        thisExp.addData('block_SC', block_SC)
        thisExp.addData('block_PF_CG', block_PF_CG)
        thisExp.addData('block_PF_IG', block_PF_IG)
        thisExp.addData('block_PF_LG', block_PF_LG)
        thisExp.addData('block_PF_GO', block_PF_GO)
        thisExp.addData('block_PF_SSR', block_PF_SSR)
        thisExp.addData('block_SF_RT', block_SF_RT)
        thisExp.addData('block_Go_RT', block_Go_RT)
        
        # overall/cumulative performance
        thisExp.addData('trial_count', trial_count)
        thisExp.addData('Go_trial_count', Go_trial_count)
        thisExp.addData('VST_count', VST_count)
        thisExp.addData('CG', CG)
        thisExp.addData('IG', IG)
        thisExp.addData('LG', LG)
        thisExp.addData('GO', GO)
        thisExp.addData('SF', SF)
        thisExp.addData('SC', SC)
        thisExp.addData('PF_CG', PF_CG)
        thisExp.addData('PF_IG', PF_IG)
        thisExp.addData('PF_LG', PF_LG)
        thisExp.addData('PF_GO', PF_GO)
        thisExp.addData('PF_SSR', PF_SSR)
        thisExp.addData('SF_RT', SF_RT)
        thisExp.addData('Go_RT', Go_RT)
        '''
        trials_loop.addData('text_fix.started', text_fix.tStartRefresh)
        trials_loop.addData('text_fix.stopped', text_fix.tStopRefresh)
        # check responses
        if key_resp_fix.keys in ['', [], None]:  # No response was made
            key_resp_fix.keys = None
        trials_loop.addData('key_resp_fix.keys',key_resp_fix.keys)
        if key_resp_fix.keys != None:  # we had a response
            trials_loop.addData('key_resp_fix.rt', key_resp_fix.rt)
        trials_loop.addData('key_resp_fix.started', key_resp_fix.tStartRefresh)
        trials_loop.addData('key_resp_fix.stopped', key_resp_fix.tStopRefresh)
        # the Routine "Fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_loop'
    
    # get names of stimulus parameters
    if trials_loop.trialList in ([], [None], None):
        params = []
    else:
        params = trials_loop.trialList[0].keys()
    # save data for this loop
    trials_loop.saveAsExcel(filename + '.xlsx', sheetName='trials_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_loop.saveAsText(filename + 'trials_loop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "EndFix"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_endfix.setText('+')
    # keep track of which components have finished
    EndFixComponents = [text_endfix]
    for thisComponent in EndFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EndFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EndFix"-------
    while continueRoutine:
        # get current time
        t = EndFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EndFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_endfix* updates
        if text_endfix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_endfix.frameNStart = frameN  # exact frame index
            text_endfix.tStart = t  # local t and not account for scr refresh
            text_endfix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_endfix, 'tStartRefresh')  # time at next scr refresh
            text_endfix.setAutoDraw(True)
        if text_endfix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_endfix.tStartRefresh + end_fix_dur-frameTolerance:
                # keep track of stop time/frame for later
                text_endfix.tStop = t  # not accounting for scr refresh
                text_endfix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_endfix, 'tStopRefresh')  # time at next scr refresh
                text_endfix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EndFix"-------
    for thisComponent in EndFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('run_counter', run_counter)
    thisExp.addData('trial_count', trial_count)
    thisExp.addData('block_trial_count', block_trial_count)
    
    #block_feedback
    if block_PF_CG < .6:
        Block_PFlag_CG = 1
    else: 
        Block_PFlag_CG = 0
        
    if block_PF_IG > .3:
        Block_PFlag_IG = 1
    else: 
        Block_PFlag_IG = 0
        
    if block_PF_LG > .3:
        Block_PFlag_LG = 1
    else: 
        Block_PFlag_LG = 0
        
    if block_PF_GO > .3:
        Block_PFlag_GO = 1
    else: 
        Block_PFlag_GO = 0
    
    if block_PF_SSR < .2 or block_PF_SSR > .8:
        Block_PFlag_SSR = 1
    else:
        Block_PFlag_SSR = 0
    
    # Stop Fail RT > Go RT by any amount (1ms or greater)
    if block_SF_RT > block_Go_RT:
        Block_PF_SFRTvGRT = 1
    else:
        Block_PF_SFRTvGRT = 0
    
    thisExp.addData('Block_PF_TNG', Block_PF_TNG)
    thisExp.addData('Block_PFlag_CG', Block_PFlag_CG)
    thisExp.addData('Block_PFlag_IG', Block_PFlag_IG)
    thisExp.addData('Block_PFlag_LG', Block_PFlag_LG)
    thisExp.addData('Block_PFlag_GO', Block_PFlag_GO)
    thisExp.addData('Block_PFlag_SSR', Block_PFlag_SSR)
    thisExp.addData('Block_PF_SFRTvGRT', Block_PF_SFRTvGRT)
    trials_RunProc.addData('text_endfix.started', text_endfix.tStartRefresh)
    trials_RunProc.addData('text_endfix.stopped', text_endfix.tStopRefresh)
    # the Routine "EndFix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Block_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    '''
    informing participants about their mean RT on go trials, 
    number of go omissions (with a reminder that this should be 0), 
    and p(respond|signal) (with a reminder that this should be close to .50). 
    The feedback could even include an explicit measure of response slowing. (Verbruggen et al., 2019) 
    '''
    block_variable_stop_trial_success_percentage = block_PF_SSR*100
    # the probability of responding to the stop signals. My understanding is p(respond|signal) = 1-p(inhibit|signal) and here premature (STEs) are not included in the computation
    # it is suggested that <.25 or >.75 may mean that SSRT estimation becomes unreliable
    block_feedback_msg = 'When you saw a left/right arrow,\nyour average response time was %s sec,\nand you did not respond for %s time(s).\nWhen you saw an up arrow,\nyou stopped responding %s percent of the time.\n\n%s%s%s%s%s%s'%(round(block_Go_RT,1), block_GO, round(block_variable_stop_trial_success_percentage,1), Block_PFlag_CG, Block_PFlag_IG, Block_PFlag_LG, Block_PFlag_GO, Block_PFlag_SSR, Block_PF_SFRTvGRT)
    '''
    #block_feedback
    if PF_CG < .6:
        Block_PFlag_CG = 1
        # many false responses, late responses or omissions
    else: 
        Block_PFlag_CG = 0
        
    if PF_IG > .3:
        Block_PFlag_IG = 1
        # many false responses
    else: 
        Block_PFlag_IG = 0
        
    if PF_LG > .3:
        Block_PFlag_LG = 1
        # many late response
    else: 
        Block_PFlag_LG = 0
        
    if PF_GO > .3:
        Block_PFlag_GO = 1
        # many omissions
    else: 
        Block_PFlag_GO = 0
    
    if PF_SSR < .2 or PF_SSR > .8:
        Block_PFlag_SSR = 1
        # many inhibition failures (impulsivity or misunderstand instructions) OR too many inhibition success (may be due to slow responding, i.e. waiting for the up arrrow)
    else:
        Block_PFlag_SSR = 0
    
    # Stop Fail RT > Go RT by any amount (1ms or greater)
    if SF_RT > Go_RT:
        Block_PF_SFRTvGRT = 1
        # many inhibition failures (impulsivity or misunderstand instructions) 
    else:
        Block_PF_SFRTvGRT = 0
    '''
    text_block_feedback.setText(block_feedback_msg)
    key_resp_block_feedback.keys = []
    key_resp_block_feedback.rt = []
    _key_resp_block_feedback_allKeys = []
    # keep track of which components have finished
    Block_feedbackComponents = [text_block_feedback, key_resp_block_feedback]
    for thisComponent in Block_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_feedback"-------
    while continueRoutine:
        # get current time
        t = Block_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_block_feedback* updates
        if text_block_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_block_feedback.frameNStart = frameN  # exact frame index
            text_block_feedback.tStart = t  # local t and not account for scr refresh
            text_block_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_block_feedback, 'tStartRefresh')  # time at next scr refresh
            text_block_feedback.setAutoDraw(True)
        
        # *key_resp_block_feedback* updates
        waitOnFlip = False
        if key_resp_block_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_block_feedback.frameNStart = frameN  # exact frame index
            key_resp_block_feedback.tStart = t  # local t and not account for scr refresh
            key_resp_block_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_block_feedback, 'tStartRefresh')  # time at next scr refresh
            key_resp_block_feedback.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_block_feedback.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_block_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_block_feedback.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_block_feedback.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_block_feedback_allKeys.extend(theseKeys)
            if len(_key_resp_block_feedback_allKeys):
                key_resp_block_feedback.keys = _key_resp_block_feedback_allKeys[-1].name  # just the last key pressed
                key_resp_block_feedback.rt = _key_resp_block_feedback_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_feedback"-------
    for thisComponent in Block_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_block_feedback.started', text_block_feedback.tStartRefresh)
    trials_RunProc.addData('text_block_feedback.stopped', text_block_feedback.tStopRefresh)
    # check responses
    if key_resp_block_feedback.keys in ['', [], None]:  # No response was made
        key_resp_block_feedback.keys = None
    trials_RunProc.addData('key_resp_block_feedback.keys',key_resp_block_feedback.keys)
    if key_resp_block_feedback.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_block_feedback.rt', key_resp_block_feedback.rt)
    trials_RunProc.addData('key_resp_block_feedback.started', key_resp_block_feedback.tStartRefresh)
    trials_RunProc.addData('key_resp_block_feedback.stopped', key_resp_block_feedback.tStopRefresh)
    # the Routine "Block_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed (3-int(expInfo['run'])) repeats of 'trials_RunProc'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
# Total no. Go trials < 300, for two completed runs (1 session)
# 1 means red flag is present
if Go_trial_count < 300:
    PF_TNG = 1
else:
    PF_TNG = 0
    
if PF_CG < .6:
    PFlag_CG = 1
else: 
    PFlag_CG = 0
    
if PF_IG > .3:
    PFlag_IG = 1
else: 
    PFlag_IG = 0
    
if PF_LG > .3:
    PFlag_LG = 1
else: 
    PFlag_LG = 0
    
if PF_GO > .3:
    PFlag_GO = 1
else: 
    PFlag_GO = 0

if PF_SSR < .2 or PF_SSR > .8:
    PFlag_SSR = 1
else:
    PFlag_SSR = 0

# Stop Fail RT > Go RT by any amount (1ms or greater)
if SF_RT > Go_RT:
    PF_SFRTvGRT = 1
else:
    PF_SFRTvGRT = 0

thisExp.addData('PF_TNG', PF_TNG)
thisExp.addData('PFlag_CG', PFlag_CG)
thisExp.addData('PFlag_IG', PFlag_IG)
thisExp.addData('PFlag_LG', PFlag_LG)
thisExp.addData('PFlag_GO', PFlag_GO)
thisExp.addData('PFlag_SSR', PFlag_SSR)
thisExp.addData('PF_SFRTvGRT', PF_SFRTvGRT)
key_resp_goodbye.keys = []
key_resp_goodbye.rt = []
_key_resp_goodbye_allKeys = []
# keep track of which components have finished
GoodbyeComponents = [text_goodbye, key_resp_goodbye]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_goodbye* updates
    if text_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_goodbye.frameNStart = frameN  # exact frame index
        text_goodbye.tStart = t  # local t and not account for scr refresh
        text_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_goodbye, 'tStartRefresh')  # time at next scr refresh
        text_goodbye.setAutoDraw(True)
    
    # *key_resp_goodbye* updates
    waitOnFlip = False
    if key_resp_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_goodbye.frameNStart = frameN  # exact frame index
        key_resp_goodbye.tStart = t  # local t and not account for scr refresh
        key_resp_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_goodbye, 'tStartRefresh')  # time at next scr refresh
        key_resp_goodbye.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_goodbye.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_goodbye.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_goodbye.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_goodbye.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_goodbye_allKeys.extend(theseKeys)
        if len(_key_resp_goodbye_allKeys):
            key_resp_goodbye.keys = _key_resp_goodbye_allKeys[-1].name  # just the last key pressed
            key_resp_goodbye.rt = _key_resp_goodbye_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_goodbye.started', text_goodbye.tStartRefresh)
thisExp.addData('text_goodbye.stopped', text_goodbye.tStopRefresh)
# check responses
if key_resp_goodbye.keys in ['', [], None]:  # No response was made
    key_resp_goodbye.keys = None
thisExp.addData('key_resp_goodbye.keys',key_resp_goodbye.keys)
if key_resp_goodbye.keys != None:  # we had a response
    thisExp.addData('key_resp_goodbye.rt', key_resp_goodbye.rt)
thisExp.addData('key_resp_goodbye.started', key_resp_goodbye.tStartRefresh)
thisExp.addData('key_resp_goodbye.stopped', key_resp_goodbye.tStopRefresh)
thisExp.nextEntry()
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
