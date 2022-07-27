#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on July 26, 2022, at 11:51
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
expName = '220627_SST_ABCD_practice_version'  # from the Builder filename that created this script
expInfo = {'participant': '', 'visit': '001/002', 'handedness(l/r/a)': 'r'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['visit'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\OSLadmin\\Desktop\\22MoTasks\\220707SST_psychopy\\220627_SST_ABCD_practice_version.py',
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
    size=[3440, 1440], fullscr=True, screen=0, 
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
    text='SST-practice\n\nPlease press 6 or 7 to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_titlepage = keyboard.Keyboard()
right_arrow_key = 'MIDDLE'
left_arrow_key = 'POINTER'

if expInfo['handedness(l/r/a)'] == 'l':
    right_arrow_key = 'POINTER'
    left_arrow_key = 'MIDDLE'

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruction_image = 'images/Instructions_Scanner_RightHanded.bmp'
right_arrow_key = 'MIDDLE'
left_arrow_key = 'POINTER'

if expInfo['handedness(l/r/a)'] == 'l':
    instruction_image = 'images/Instructions_Scanner_LeftHanded.bmp'
    right_arrow_key = 'POINTER'
    left_arrow_key = 'MIDDLE'
image_instructions = visual.ImageStim(
    win=win,
    name='image_instructions', 
    image=instruction_image, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_instructions = keyboard.Keyboard()

# Initialize components for Routine "TestReady"
TestReadyClock = core.Clock()
test_ready_instructions = 'We are now ready to begin the game!\nREMEMBER: When you see the LEFT arrow, \npress your %s finger.\nWhen you see the RIGHT arrow, \npress your %s finger.\nIf you see an UP arrow, STOP yourself from pressing to the left or the right arrow.\nPress the correct key as FAST as you can. Stopping and going are equally important!\n\nPress your index or middle finger to continue.'%(left_arrow_key,right_arrow_key)
text_testready = visual.TextStim(win=win, name='text_testready',
    text=test_ready_instructions,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_testready = keyboard.Keyboard()

# Initialize components for Routine "BeginFix"
BeginFixClock = core.Clock()
text_beginfix = visual.TextStim(win=win, name='text_beginfix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

go_stop_trial_dur = 1
SSD = .05
PrevStopACC = 0
STEflag = 0
STEcount = 0
STEadjstop_nback = 0
updated_trial_label = ''
prev_VST_trial_num = 0
real_stop_nback = 0
block_variable_stop_trial_success_percentage = 0
image_stimulus = visual.ImageStim(
    win=win,
    name='image_stimulus', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_go_stop_trial = keyboard.Keyboard()
image_stop = visual.ImageStim(
    win=win,
    name='image_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.2, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_image_stop = keyboard.Keyboard()

# Initialize components for Routine "Fix"
FixClock = core.Clock()
FixDur = 0

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

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_ITI = visual.TextStim(win=win, name='text_ITI',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ITI = keyboard.Keyboard()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_goodbye = visual.TextStim(win=win, name='text_goodbye',
    text='All done!\n\nPlease tell the experimenter you are finished.',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_goodbye = keyboard.Keyboard()

# Initialize components for Routine "Practice_feedback"
Practice_feedbackClock = core.Clock()
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
        theseKeys = key_resp_titlepage.getKeys(keyList=['6','7', 'space'], waitRelease=False)
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

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instructions.keys = []
key_resp_instructions.rt = []
_key_resp_instructions_allKeys = []
# keep track of which components have finished
InstructionsComponents = [image_instructions, key_resp_instructions]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_instructions* updates
    if image_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_instructions.frameNStart = frameN  # exact frame index
        image_instructions.tStart = t  # local t and not account for scr refresh
        image_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_instructions, 'tStartRefresh')  # time at next scr refresh
        image_instructions.setAutoDraw(True)
    
    # *key_resp_instructions* updates
    waitOnFlip = False
    if key_resp_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions.frameNStart = frameN  # exact frame index
        key_resp_instructions.tStart = t  # local t and not account for scr refresh
        key_resp_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions, 'tStartRefresh')  # time at next scr refresh
        key_resp_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions.getKeys(keyList=['6', '7', 'space'], waitRelease=False)
        _key_resp_instructions_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_allKeys):
            key_resp_instructions.keys = _key_resp_instructions_allKeys[-1].name  # just the last key pressed
            key_resp_instructions.rt = _key_resp_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_instructions.started', image_instructions.tStartRefresh)
thisExp.addData('image_instructions.stopped', image_instructions.tStopRefresh)
# check responses
if key_resp_instructions.keys in ['', [], None]:  # No response was made
    key_resp_instructions.keys = None
thisExp.addData('key_resp_instructions.keys',key_resp_instructions.keys)
if key_resp_instructions.keys != None:  # we had a response
    thisExp.addData('key_resp_instructions.rt', key_resp_instructions.rt)
thisExp.addData('key_resp_instructions.started', key_resp_instructions.tStartRefresh)
thisExp.addData('key_resp_instructions.stopped', key_resp_instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TestReady"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_testready.keys = []
key_resp_testready.rt = []
_key_resp_testready_allKeys = []
# keep track of which components have finished
TestReadyComponents = [text_testready, key_resp_testready]
for thisComponent in TestReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TestReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TestReady"-------
while continueRoutine:
    # get current time
    t = TestReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TestReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_testready* updates
    if text_testready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_testready.frameNStart = frameN  # exact frame index
        text_testready.tStart = t  # local t and not account for scr refresh
        text_testready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_testready, 'tStartRefresh')  # time at next scr refresh
        text_testready.setAutoDraw(True)
    
    # *key_resp_testready* updates
    waitOnFlip = False
    if key_resp_testready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_testready.frameNStart = frameN  # exact frame index
        key_resp_testready.tStart = t  # local t and not account for scr refresh
        key_resp_testready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_testready, 'tStartRefresh')  # time at next scr refresh
        key_resp_testready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_testready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_testready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_testready.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_testready.getKeys(keyList=['6', '7', 'space'], waitRelease=False)
        _key_resp_testready_allKeys.extend(theseKeys)
        if len(_key_resp_testready_allKeys):
            key_resp_testready.keys = _key_resp_testready_allKeys[-1].name  # just the last key pressed
            key_resp_testready.rt = _key_resp_testready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestReady"-------
for thisComponent in TestReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_testready.started', text_testready.tStartRefresh)
thisExp.addData('text_testready.stopped', text_testready.tStopRefresh)
# check responses
if key_resp_testready.keys in ['', [], None]:  # No response was made
    key_resp_testready.keys = None
thisExp.addData('key_resp_testready.keys',key_resp_testready.keys)
if key_resp_testready.keys != None:  # we had a response
    thisExp.addData('key_resp_testready.rt', key_resp_testready.rt)
thisExp.addData('key_resp_testready.started', key_resp_testready.tStartRefresh)
thisExp.addData('key_resp_testready.stopped', key_resp_testready.tStopRefresh)
thisExp.nextEntry()
# the Routine "TestReady" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BeginFix"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
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
thisExp.addData('text_beginfix.started', text_beginfix.tStartRefresh)
thisExp.addData('text_beginfix.stopped', text_beginfix.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practice_list.xlsx'),
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
        go_stop_trial_dur = 1
        image_stop_dur = 0
    elif trial_type == 'VariableStopTrial':
        if STEflag == 0:
            if VST_count > 0:
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
            if SSD < .1:
                SSD = .05
                STEflag = 0
            else:
                SSD = SSD - .1
                STEflag = 0
        go_stop_trial_dur = SSD
        image_stop_dur = .3
    '''
    Xi changed image_stop_due to be .3 on variable stop trials based on the changes in 2021. 
    However, this change is not reflected in the 2018 e-prime files. 
    Issue 4 (short Stop Signal durations when SSD is long): 
    Xi made sure SSDmin is 50ms: • The task has been changed to have a fixed Stop Signal duration. 
        “We have changed the task to ensure that the Stop signal duration is always 300 msec in duration, a change which we believe will have a negligible impact on any longitudinal comparisons.” (Garavan et al., 2021, p. 13)
    Issue 2 (no Go stimuli at 0 SSD): • “To avoid potential confusion, the task has been modified to ensure that the SSD does not drop below 50 msec thereby ensuring presentation of the Go stimulus on all trials. ” (Garavan et al., 2021, p. 12) 
    ''' 
    key_resp_go_stop_trial.keys = []
    key_resp_go_stop_trial.rt = []
    _key_resp_go_stop_trial_allKeys = []
    key_resp_image_stop.keys = []
    key_resp_image_stop.rt = []
    _key_resp_image_stop_allKeys = []
    # keep track of which components have finished
    Go_Stop_trialComponents = [image_stimulus, key_resp_go_stop_trial, image_stop, key_resp_image_stop]
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
        '''STE (stop trigger error): any key press before the stop sign comes up on the variable stop trials
        If response is made during the SSD: 
        1. Flag trial as an STE
        2. Change next trialtype to a VariableStopTrial
        3. Increase the Stop_nback count for the next trial
        '''
        
        
        '''
        If STEflag = 1 Then
         If SSDDur < 100 Then
          SSDDur = 50
          STEflag = 0
         Else
          SSDDur = SSDDur - 100
          STEflag = 0
         End If
        '''
        
        # *image_stimulus* updates
        if image_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_stimulus.frameNStart = frameN  # exact frame index
            image_stimulus.tStart = t  # local t and not account for scr refresh
            image_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_stimulus, 'tStartRefresh')  # time at next scr refresh
            image_stimulus.setAutoDraw(True)
        if image_stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_stimulus.tStartRefresh + go_stop_trial_dur-frameTolerance:
                # keep track of stop time/frame for later
                image_stimulus.tStop = t  # not accounting for scr refresh
                image_stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_stimulus, 'tStopRefresh')  # time at next scr refresh
                image_stimulus.setAutoDraw(False)
        if image_stimulus.status == STARTED:  # only update if drawing
            image_stimulus.setImage(stimulus, log=False)
        
        # *key_resp_go_stop_trial* updates
        waitOnFlip = False
        if key_resp_go_stop_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_go_stop_trial.frameNStart = frameN  # exact frame index
            key_resp_go_stop_trial.tStart = t  # local t and not account for scr refresh
            key_resp_go_stop_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_go_stop_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_go_stop_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_go_stop_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_go_stop_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_go_stop_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_go_stop_trial.tStartRefresh + go_stop_trial_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_go_stop_trial.tStop = t  # not accounting for scr refresh
                key_resp_go_stop_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_go_stop_trial, 'tStopRefresh')  # time at next scr refresh
                key_resp_go_stop_trial.status = FINISHED
        if key_resp_go_stop_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_go_stop_trial.getKeys(keyList=['6', '7'], waitRelease=False)
            _key_resp_go_stop_trial_allKeys.extend(theseKeys)
            if len(_key_resp_go_stop_trial_allKeys):
                key_resp_go_stop_trial.keys = _key_resp_go_stop_trial_allKeys[0].name  # just the first key pressed
                key_resp_go_stop_trial.rt = _key_resp_go_stop_trial_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_stop* updates
        if image_stop.status == NOT_STARTED and tThisFlip >= go_stop_trial_dur-frameTolerance:
            # keep track of start time/frame for later
            image_stop.frameNStart = frameN  # exact frame index
            image_stop.tStart = t  # local t and not account for scr refresh
            image_stop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_stop, 'tStartRefresh')  # time at next scr refresh
            image_stop.setAutoDraw(True)
        if image_stop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_stop.tStartRefresh + image_stop_dur-frameTolerance:
                # keep track of stop time/frame for later
                image_stop.tStop = t  # not accounting for scr refresh
                image_stop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_stop, 'tStopRefresh')  # time at next scr refresh
                image_stop.setAutoDraw(False)
        if image_stop.status == STARTED:  # only update if drawing
            image_stop.setImage('images/Stop_Arrow.BMP', log=False)
        
        # *key_resp_image_stop* updates
        waitOnFlip = False
        if key_resp_image_stop.status == NOT_STARTED and tThisFlip >= go_stop_trial_dur-frameTolerance:
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
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_image_stop.tStartRefresh + image_stop_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_image_stop.tStop = t  # not accounting for scr refresh
                key_resp_image_stop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_image_stop, 'tStopRefresh')  # time at next scr refresh
                key_resp_image_stop.status = FINISHED
        if key_resp_image_stop.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_image_stop.getKeys(keyList=['6', '7'], waitRelease=False)
            _key_resp_image_stop_allKeys.extend(theseKeys)
            if len(_key_resp_image_stop_allKeys):
                key_resp_image_stop.keys = _key_resp_image_stop_allKeys[0].name  # just the first key pressed
                key_resp_image_stop.rt = _key_resp_image_stop_allKeys[0].rt
                # was this correct?
                if (key_resp_image_stop.keys == str('None')) or (key_resp_image_stop.keys == 'None'):
                    key_resp_image_stop.corr = 1
                else:
                    key_resp_image_stop.corr = 0
        
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
        if key_resp_go_stop_trial.keys in ['', [], None]:
            STEflag = 0
        else:
            STEflag = 1
            image_stop_dur = 0 
    trials_loop.addData('image_stimulus.started', image_stimulus.tStartRefresh)
    trials_loop.addData('image_stimulus.stopped', image_stimulus.tStopRefresh)
    # check responses
    if key_resp_go_stop_trial.keys in ['', [], None]:  # No response was made
        key_resp_go_stop_trial.keys = None
    trials_loop.addData('key_resp_go_stop_trial.keys',key_resp_go_stop_trial.keys)
    if key_resp_go_stop_trial.keys != None:  # we had a response
        trials_loop.addData('key_resp_go_stop_trial.rt', key_resp_go_stop_trial.rt)
    trials_loop.addData('key_resp_go_stop_trial.started', key_resp_go_stop_trial.tStartRefresh)
    trials_loop.addData('key_resp_go_stop_trial.stopped', key_resp_go_stop_trial.tStopRefresh)
    trials_loop.addData('image_stop.started', image_stop.tStartRefresh)
    trials_loop.addData('image_stop.stopped', image_stop.tStopRefresh)
    # check responses
    if key_resp_image_stop.keys in ['', [], None]:  # No response was made
        key_resp_image_stop.keys = None
        # was no response the correct answer?!
        if str('None').lower() == 'none':
           key_resp_image_stop.corr = 1;  # correct non-response
        else:
           key_resp_image_stop.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_loop (TrialHandler)
    trials_loop.addData('key_resp_image_stop.keys',key_resp_image_stop.keys)
    trials_loop.addData('key_resp_image_stop.corr', key_resp_image_stop.corr)
    if key_resp_image_stop.keys != None:  # we had a response
        trials_loop.addData('key_resp_image_stop.rt', key_resp_image_stop.rt)
    trials_loop.addData('key_resp_image_stop.started', key_resp_image_stop.tStartRefresh)
    trials_loop.addData('key_resp_image_stop.stopped', key_resp_image_stop.tStopRefresh)
    # the Routine "Go_Stop_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Fix"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Calculate trial fixation duration (GoFixDur = Hold - GoRT + Jitter)
    if trial_type == 'GoTrial':
        if key_resp_go_stop_trial.keys != None:
            FixDur = 1 - key_resp_go_stop_trial.rt
        else:
            FixDur = 0
    elif trial_type == 'VariableStopTrial':
        if STEflag == 0:
            if SSD > .7:
                FixDur = 0
            else: 
                FixDur = 1 - (SSD + image_stop_dur)
        if STEflag == 1:
            FixDur = 1 - key_resp_go_stop_trial.rt
    
    '''
    The original ABCD's script is conflicting with the 
    new change that the STOPdur will always be .3s when
    STEflag != 1:
    
        'Check to see if StopDur <> 0
    If StopDur = 0 Then
     StopDurAdj = StopDur
    Else
     If c.GetAttrib("StopSignal.RT") > 0 Then
      StopDurAdj = c.GetAttrib("StopSignal.RT")
     Else
      StopDurAdj = StopDur
     End If 
    End If
    
    the 2nd condition, if there is a key press during the
    stop signal, this first rt will be used to increase 
    the duration of the fixation. This is conflicting because
    the stop duration is always .3ms and even if there is a key
    press during the stop duration, the stop signal will not
    terminate. So this 2nd condition is not implemented in our version.
    '''
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
        if text_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_fix.frameNStart = frameN  # exact frame index
            text_fix.tStart = t  # local t and not account for scr refresh
            text_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_fix, 'tStartRefresh')  # time at next scr refresh
            text_fix.setAutoDraw(True)
        if text_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_fix.tStartRefresh + FixDur-frameTolerance:
                # keep track of stop time/frame for later
                text_fix.tStop = t  # not accounting for scr refresh
                text_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_fix, 'tStopRefresh')  # time at next scr refresh
                text_fix.setAutoDraw(False)
        
        # *key_resp_fix* updates
        waitOnFlip = False
        if key_resp_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_fix.tStartRefresh + FixDur-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_fix.tStop = t  # not accounting for scr refresh
                key_resp_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_fix, 'tStopRefresh')  # time at next scr refresh
                key_resp_fix.status = FINISHED
        if key_resp_fix.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_fix.getKeys(keyList=['6', '7'], waitRelease=False)
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
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_ITI.setText('+')
    key_resp_ITI.keys = []
    key_resp_ITI.rt = []
    _key_resp_ITI_allKeys = []
    # keep track of which components have finished
    ITIComponents = [text_ITI, key_resp_ITI]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_ITI* updates
        if text_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ITI.frameNStart = frameN  # exact frame index
            text_ITI.tStart = t  # local t and not account for scr refresh
            text_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ITI, 'tStartRefresh')  # time at next scr refresh
            text_ITI.setAutoDraw(True)
        if text_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_ITI.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                text_ITI.tStop = t  # not accounting for scr refresh
                text_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_ITI, 'tStopRefresh')  # time at next scr refresh
                text_ITI.setAutoDraw(False)
        
        # *key_resp_ITI* updates
        waitOnFlip = False
        if key_resp_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_ITI.frameNStart = frameN  # exact frame index
            key_resp_ITI.tStart = t  # local t and not account for scr refresh
            key_resp_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_ITI, 'tStartRefresh')  # time at next scr refresh
            key_resp_ITI.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_ITI.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_ITI.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_ITI.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_ITI.tStop = t  # not accounting for scr refresh
                key_resp_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_ITI, 'tStopRefresh')  # time at next scr refresh
                key_resp_ITI.status = FINISHED
        if key_resp_ITI.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_ITI.getKeys(keyList=['6', '7'], waitRelease=False)
            _key_resp_ITI_allKeys.extend(theseKeys)
            if len(_key_resp_ITI_allKeys):
                key_resp_ITI.keys = _key_resp_ITI_allKeys[0].name  # just the first key pressed
                key_resp_ITI.rt = _key_resp_ITI_allKeys[0].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_loop.addData('text_ITI.started', text_ITI.tStartRefresh)
    trials_loop.addData('text_ITI.stopped', text_ITI.tStopRefresh)
    # check responses
    if key_resp_ITI.keys in ['', [], None]:  # No response was made
        key_resp_ITI.keys = None
    trials_loop.addData('key_resp_ITI.keys',key_resp_ITI.keys)
    if key_resp_ITI.keys != None:  # we had a response
        trials_loop.addData('key_resp_ITI.rt', key_resp_ITI.rt)
    trials_loop.addData('key_resp_ITI.started', key_resp_ITI.tStartRefresh)
    trials_loop.addData('key_resp_ITI.stopped', key_resp_ITI.tStopRefresh)
    # on variable stop trials, successful inhibition means 0 keypress throughout the trial including during the fixation and jitter
    # two types of inhibition "failure": 1. key press post SSD; 2. STE (stop trigger error): key  press during SSD before stop signal (participant's fast and correct hit)
    trial_count += 1
    if trial_type == 'VariableStopTrial':
        STEcount += STEflag
        if STEflag == 0:
            VST_count += 1
            if key_resp_image_stop.keys in ['', [], None] and key_resp_fix.keys in ['', [], None] and key_resp_ITI.keys in ['', [], None]:
                PrevStopACC = 1
                updated_trial_label = "stop_success"
                SC += 1
            elif key_resp_image_stop.keys != None or key_resp_fix.keys != None or key_resp_ITI.keys != None:
                PrevStopACC = 0
                updated_trial_label = "stop_failure"
                SF += 1
                if key_resp_image_stop.keys != None:
                    SF_RT_sum = SF_RT_sum + SSD + key_resp_image_stop.rt
                elif key_resp_image_stop.keys in ['', [], None] and key_resp_fix.keys != None:
                    SF_RT_sum = SF_RT_sum + SSD + .3 + key_resp_fix.rt
                elif key_resp_image_stop.keys in ['', [], None] and key_resp_fix.keys in ['', [], None] and key_resp_ITI.keys != None:
                    SF_RT_sum = SF_RT_sum + SSD + .3 + FixDur + key_resp_ITI.rt
                SF_RT = SF_RT_sum/SF
            if prev_VST_trial_num == 0:
                real_stop_nback = trial_count - 1
            else:
                real_stop_nback = trial_count - prev_VST_trial_num - 1
            prev_VST_trial_num = trial_count
        elif STEflag == 1:
            real_stop_nback = 0
            # as STE is no longer counted as a VST
            Go_trial_count += 1
            Go_RT_sum = Go_RT_sum + key_resp_go_stop_trial.rt
            Go_RT = Go_RT_sum/Go_trial_count
            if key_resp_go_stop_trial.keys in str(correct_answer):
                updated_trial_label = "STE_correct_go"
                CG += 1
            else: 
                updated_trial_label = "STE_incorrect_go"
                IG += 1
    elif trial_type == 'GoTrial':
        Go_trial_count += 1
        real_stop_nback = 0
        if key_resp_go_stop_trial.keys != None:
            Go_RT_sum = Go_RT_sum + key_resp_go_stop_trial.rt
            Go_RT = Go_RT_sum/Go_trial_count
            if key_resp_go_stop_trial.keys in str(correct_answer):
                updated_trial_label = "correct_go"
                CG += 1
            else: 
                updated_trial_label = "incorrect_go"
                IG += 1
        elif key_resp_go_stop_trial.keys in ['', [], None]:
            if key_resp_ITI.keys != None:
                Go_RT_sum = Go_RT_sum + 1 + key_resp_ITI.rt
                Go_RT = Go_RT_sum/Go_trial_count
                # late go trials' fixation duration is always 0 
                # this errror include both correct and incorrect late gos during the ITI duration
                updated_trial_label = "late_go"
                LG += 1
            elif key_resp_ITI.keys in ['', [], None]:
                Go_RT_sum = Go_RT_sum + 1 + jitter
                Go_RT = Go_RT_sum/Go_trial_count
                updated_trial_label = "go_omission"
                GO += 1 # GO is go omission, unlike Go, which is go trials
    if VST_count > 0:
        PF_SSR = SC/VST_count
    if Go_trial_count > 0:
        PF_CG = CG/Go_trial_count
        PF_IG = IG/Go_trial_count
        PF_LG = LG/Go_trial_count
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
    
    # script debugging variables
    thisExp.addData('STEcount', STEcount)
    thisExp.addData('STEflag', STEflag)
    thisExp.addData('Real_trial_type', trial_type)
    thisExp.addData('image_stop_dur', image_stop_dur)
    thisExp.addData('updated_trial_label', updated_trial_label)
    thisExp.addData('go_stop_trial_dur', go_stop_trial_dur)
    thisExp.addData('SSD', SSD)
    thisExp.addData('FixDur', FixDur)
    thisExp.addData('real_stop_nback', real_stop_nback)
    
    thisExp.addData('recorded_key_resp_go_stop_trial', key_resp_go_stop_trial.rt)
    thisExp.addData('recorded_key_resp_image_stop.rt', key_resp_image_stop.rt)
    thisExp.addData('recorded_key_resp_fix.rt', key_resp_fix.rt)
    thisExp.addData('recorded_key_resp_ITI.rt', key_resp_ITI.rt)
    
    # constantly updated performance red flags
    # Go trial stats include STE trials as participants are naive to the actual trial type, 
    # so their STE responses shall be included in computing their overall go trial performance
    
    # 1 means red flag
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
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
# Total no. Go trials < 300, for two completed runs (1 session)
# 1 means red flag is present    
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

# ------Prepare to start Routine "Practice_feedback"-------
continueRoutine = True
# update component parameters for each repeat
'''
informing participants about their mean RT on go trials, 
number of go omissions (with a reminder that this should be 0), 
and p(respond|signal) (with a reminder that this should be close to .50). 
The feedback could even include an explicit measure of response slowing. (Verbruggen et al., 2019) 
'''
block_variable_stop_trial_success_percentage = PF_SSR*100
# the probability of responding to the stop signals. My understanding is p(respond|signal) = 1-p(inhibit|signal) and here premature (STEs) are not included in the computation
# it is suggested that <.25 or >.75 may mean that SSRT estimation becomes unreliable
block_feedback_msg = 'When you saw a left/right arrow,\nyour average response time was %s sec,\nand you did not respond for %s time(s).\nWhen you saw an up arrow,\nyou stopped responding %s percent of the time.\n\n%s%s%s%s%s%s'%(round(Go_RT,1), GO, round(block_variable_stop_trial_success_percentage,1), PFlag_CG, PFlag_IG, PFlag_LG, PFlag_GO, PFlag_SSR, PF_SFRTvGRT)
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
Practice_feedbackComponents = [text_block_feedback, key_resp_block_feedback]
for thisComponent in Practice_feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Practice_feedback"-------
while continueRoutine:
    # get current time
    t = Practice_feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Practice_feedbackClock)
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
    for thisComponent in Practice_feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice_feedback"-------
for thisComponent in Practice_feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_block_feedback.started', text_block_feedback.tStartRefresh)
thisExp.addData('text_block_feedback.stopped', text_block_feedback.tStopRefresh)
# check responses
if key_resp_block_feedback.keys in ['', [], None]:  # No response was made
    key_resp_block_feedback.keys = None
thisExp.addData('key_resp_block_feedback.keys',key_resp_block_feedback.keys)
if key_resp_block_feedback.keys != None:  # we had a response
    thisExp.addData('key_resp_block_feedback.rt', key_resp_block_feedback.rt)
thisExp.addData('key_resp_block_feedback.started', key_resp_block_feedback.tStartRefresh)
thisExp.addData('key_resp_block_feedback.stopped', key_resp_block_feedback.tStopRefresh)
thisExp.nextEntry()
# the Routine "Practice_feedback" was not non-slip safe, so reset the non-slip timer
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
