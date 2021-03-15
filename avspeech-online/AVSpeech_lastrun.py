#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue Dec 15 17:30:43 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'AVSpeech'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/BrangLab/Desktop/Pavlovia Experiments/avspeech-online/AVSpeech_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "init"
initClock = core.Clock()
import random 
random.seed()

# Number of items
num_practice = 8
num_stim = 40
num_trials = 120
# Allow fewer than the full number of trials to run
# Specify the number to run here.
trials_to_run = 120

stim = {}
stim['AudNames'] = ['bag','base','beard','bible','bid','fad','fat','fill','fine','fist','bank','beer','bias','bill','bye','fast','file','fish','fit','five','gag','gas','guild','guile','gig','dad','dash','dill','dine','disk','gang','gear','guise','gill','guy','dance','dial','dish','digs','dive']
stim['Answers'] = [['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['F','D','T','TH'],['F','D','T','TH'],['F','D','T','TH'],['F','D','T','TH'],['F','D','T','TH'],['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['B','G','D','TH'],['F','D','T','TH'],['F','D','T','TH'],['F','D','T','TH'],['F','D','G','TH'],['F','D','T','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','TH'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','TH'],['G','B','D','T'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH'],['D','F','T','TH']]
stim['AudOnsets'] = [0.5397, 0.5204, 0.5329, 0.5310,0.5417,0.5428,0.5478, 0.5244, 0.5294, 0.5384, 0.5306, 0.5331, 0.5316, 0.5228, 0.5087, 0.5257, 0.5201, 0.5492, 0.5201, 0.5355, 0.5407, 0.5458, 0.5314, 0.5275, 0.5457, 0.5456, 0.5177, 0.5355, 0.5337, 0.5319, 0.5211, 0.5260, 0.5196, 0.5337, 0.5308, 0.5395, 0.5391, 0.5029, 0.5185, 0.5300]
stim['FrameAdj'] = [0, 1, 0, 0, 0, -2, -1, 1, -2, -2, 0, 1, 0, 1, -2, 0, -2, 0, -2, -2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, -2, 1, 0, 0, 0, 0, -3, 1, 1]
# FrameAdj: negative value is the number of times to hold the first frame, positive value is the number of frames to skip

# From MATLAB:
# This seems to be randomizing whether the stim lists are in order or are shuffled order.
# This order determines which condition they're paired with before randomizing, so it matters.
#DATA.StimCounterBalance = randperm(2);
#DATA.StimCounterBalance = DATA.StimCounterBalance(1:numBlocks);
#STIM.Aud_List = [];
#STIM.IncongV_List = [];
#for i=1:numBlocks
#    if DATA.StimCounterBalance(i)==1
#        STIM.Aud_List(i,:) = STIM.Aud_List_Orig;
#        STIM.IncongV_List(i,:) = STIM.IncongV_List_Orig;
#    else
#        STIM.Aud_List(i,:) = STIM.Aud_List_Orig([11:20 1:10 31:40 21:30 ]);
#        STIM.IncongV_List(i,:) = STIM.IncongV_List_Orig([11:20 1:10 31:40 21:30 ]);
#    end
#end
balancer = random.randint(1,2)
# print(balancer)
incongV_list_orig = [x for x in range(20,40)] + [x for x in range(0,20)]
if balancer ==1 :
    aud_list_orig = [x for x in range(0, 40)]
else:
    aud_list_orig = [x for x in range(10,20)] + [x for x in range(0, 10)] +[x for x in range(30,40)] + [x for x in range(20,30)]
    incongV_list_orig = incongV_list_orig[10:20] + incongV_list_orig[0:10] + incongV_list_orig[30:40] + incongV_list_orig[20:30]
# print(aud_list_orig)
# print(incongV_list_orig)

# Get the practice items
practice = []
practiceVisList = [-1, 34, 33, -1, 15, 5, -1, -1]
practiceAudList = [10, 34, 13, 25, 35, 5, 2, 39]
practiceCondList = [2, 8, 10, 3, 12, 5, 1, 4];
corrAnsList = ['s','k','l','s','s','d','s','s']
corrAnsIdx = [0, 2, 3, 0, 0, 1, 0, 0]
# Get these as an array of dicts so each practice iteration is a single array item.
# This makes randomizing trials easier (below).
# Less important for practice, except for consistency in the data format.
for pIdx in range(0, num_practice):
    p = {'AudList': practiceAudList[pIdx], 'VisList': practiceVisList[pIdx], 'CorrAns': corrAnsList[pIdx], 'CorrAnsIdx': corrAnsIdx[pIdx], 'Condition': practiceCondList[pIdx]}
    practice.append(p)

pract_idx = 0
stim_idx = 0

# Get a list of all the stimulus trial combinations and randomize it.
trialList = []
trialsAudList = aud_list_orig + aud_list_orig + aud_list_orig
trialsVisList = [-1 for x in range(0,40)] + aud_list_orig + incongV_list_orig
trialsConditionList = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12]
for tIdx in range(0, num_trials):
    t = {'AudList': trialsAudList[tIdx], 'VisList': trialsVisList[tIdx], 'Condition': trialsConditionList[tIdx]}
    trialList.append(t)

random.shuffle(trialList)
# print(trials)

print(len(stim))
print(len(practice))

# When they miss a trial, increase response time
# by .25 sec up to max 2 sec.
non_missed_trials = 0
rt = 1.25

# Initialize components for Routine "practicePrompt"
practicePromptClock = core.Clock()
blackScreen = visual.Rect(
    win=win, name='blackScreen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
doPracticePrompt = visual.TextStim(win=win, name='doPracticePrompt',
    text="Do you want to do the practice tasks?\n\nSelect 'y' for YES or 'n' for NO to skip the practice.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
doPracticeResp = keyboard.Keyboard()

# Initialize components for Routine "practiceInstruction"
practiceInstructionClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
practInstr = visual.TextStim(win=win, name='practInstr',
    text='First, we will go through 8 practice trials.\n\nIn this activity, you will hear a word on each trial, followed by 4 response choices. \nPress the button for the first letter/sound of the word you heard (e.g. "g" or "th").\nThe \'1\' key corresponds to the first option shown, the \'2\' key to the second, \'9\' to the third, and \'0\' to the final option.\n\nSome trials will be harder to hear than others, and some of the words may be fake words. If you are ever unsure, please give it your best guess.\n\nPress any button to continue.',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
practInstResp = keyboard.Keyboard()

# Initialize components for Routine "BlankScreen"
BlankScreenClock = core.Clock()
BlackBlank = visual.Rect(
    win=win, name='BlackBlank',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "practiceDisplay"
practiceDisplayClock = core.Clock()
sound_stim_pract = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_stim_pract')
sound_stim_pract.setVolume(1)
noise_pract = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='noise_pract')
noise_pract.setVolume(1)

# Initialize components for Routine "practiceResponse"
practiceResponseClock = core.Clock()
blackRectP = visual.Rect(
    win=win, name='blackRectP',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
PracticeRespOptions = visual.TextStim(win=win, name='PracticeRespOptions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PracticeResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceCorrectFeedback"
practiceCorrectFeedbackClock = core.Clock()
blackRectCorr = visual.Rect(
    win=win, name='blackRectCorr',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
practiceCorr = visual.TextStim(win=win, name='practiceCorr',
    text='Correct!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceIncorrectFeedback"
practiceIncorrectFeedbackClock = core.Clock()
blackRectIncorr = visual.Rect(
    win=win, name='blackRectIncorr',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_incorrect = visual.TextStim(win=win, name='text_incorrect',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceNoAnsFeedback"
practiceNoAnsFeedbackClock = core.Clock()
rectNoAns = visual.Rect(
    win=win, name='rectNoAns',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
practNoAnsText = visual.TextStim(win=win, name='practNoAnsText',
    text='No key was pressed. \n\n The correct answer was: \n' + stim['Answers'][(practice[pract_idx]['AudList'])][practice[pract_idx]['CorrAnsIdx']],
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "increment_pract_idx"
increment_pract_idxClock = core.Clock()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
blackScreen2 = visual.Rect(
    win=win, name='blackScreen2',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='In this activity, you will hear a word being spoken on each trial, followed by 4 response choices. \nPress the button for the first letter/sound of the word you heard (e.g. "g" or "th").\nThe \'1\' key corresponds to the first option shown, the \'2\' key to the second, \'9\' to the third, and \'0\' to the final option.\n\nSome trials will be harder to hear than others, and some of the words may be fake words. Please try your best to choose whichever letter was most similar to what you heard. \nIf you are ever unsure, please give it your best guess.\n\nThis task will take 5 minutes. \n\nPress any button to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "stimDisplay"
stimDisplayClock = core.Clock()
sound_stim = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_stim')
sound_stim.setVolume(1)
noise_stim = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='noise_stim')
noise_stim.setVolume(1)

# Initialize components for Routine "stimResponse"
stimResponseClock = core.Clock()
BlackRectStim = visual.Rect(
    win=win, name='BlackRectStim',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
StimRespOpts = visual.TextStim(win=win, name='StimRespOpts',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
StimResponseKey = keyboard.Keyboard()

# Initialize components for Routine "rt_adjust"
rt_adjustClock = core.Clock()

# Initialize components for Routine "Inc_stim_idx"
Inc_stim_idxClock = core.Clock()

# Initialize components for Routine "BlankScreen"
BlankScreenClock = core.Clock()
BlackBlank = visual.Rect(
    win=win, name='BlackBlank',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "init"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "init"-------
while continueRoutine:
    # get current time
    t = initClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init"-------
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practicePrompt"-------
continueRoutine = True
# update component parameters for each repeat
doPracticeResp.keys = []
doPracticeResp.rt = []
_doPracticeResp_allKeys = []
# keep track of which components have finished
practicePromptComponents = [blackScreen, doPracticePrompt, doPracticeResp]
for thisComponent in practicePromptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practicePromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practicePrompt"-------
while continueRoutine:
    # get current time
    t = practicePromptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practicePromptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackScreen* updates
    if blackScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blackScreen.frameNStart = frameN  # exact frame index
        blackScreen.tStart = t  # local t and not account for scr refresh
        blackScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blackScreen, 'tStartRefresh')  # time at next scr refresh
        blackScreen.setAutoDraw(True)
    
    # *doPracticePrompt* updates
    if doPracticePrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        doPracticePrompt.frameNStart = frameN  # exact frame index
        doPracticePrompt.tStart = t  # local t and not account for scr refresh
        doPracticePrompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(doPracticePrompt, 'tStartRefresh')  # time at next scr refresh
        doPracticePrompt.setAutoDraw(True)
    
    # *doPracticeResp* updates
    if doPracticeResp.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        doPracticeResp.frameNStart = frameN  # exact frame index
        doPracticeResp.tStart = t  # local t and not account for scr refresh
        doPracticeResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(doPracticeResp, 'tStartRefresh')  # time at next scr refresh
        doPracticeResp.status = STARTED
        # keyboard checking is just starting
        doPracticeResp.clock.reset()  # now t=0
    if doPracticeResp.status == STARTED:
        theseKeys = doPracticeResp.getKeys(keyList=['y', 'n'], waitRelease=False)
        _doPracticeResp_allKeys.extend(theseKeys)
        if len(_doPracticeResp_allKeys):
            doPracticeResp.keys = _doPracticeResp_allKeys[-1].name  # just the last key pressed
            doPracticeResp.rt = _doPracticeResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practicePromptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practicePrompt"-------
for thisComponent in practicePromptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blackScreen.started', blackScreen.tStartRefresh)
thisExp.addData('blackScreen.stopped', blackScreen.tStopRefresh)
thisExp.addData('doPracticePrompt.started', doPracticePrompt.tStartRefresh)
thisExp.addData('doPracticePrompt.stopped', doPracticePrompt.tStopRefresh)
# check responses
if doPracticeResp.keys in ['', [], None]:  # No response was made
    doPracticeResp.keys = None
thisExp.addData('doPracticeResp.keys',doPracticeResp.keys)
if doPracticeResp.keys != None:  # we had a response
    thisExp.addData('doPracticeResp.rt', doPracticeResp.rt)
thisExp.addData('doPracticeResp.started', doPracticeResp.tStart)
thisExp.addData('doPracticeResp.stopped', doPracticeResp.tStop)
thisExp.nextEntry()
if (doPracticeResp.keys == 'y'):
    doPractice = 1
else:
    doPractice = 0
# the Routine "practicePrompt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceInstruction"-------
continueRoutine = True
# update component parameters for each repeat
practInstResp.keys = []
practInstResp.rt = []
_practInstResp_allKeys = []
# keep track of which components have finished
practiceInstructionComponents = [polygon, practInstr, practInstResp]
for thisComponent in practiceInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceInstruction"-------
while continueRoutine:
    # get current time
    t = practiceInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *practInstr* updates
    if practInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practInstr.frameNStart = frameN  # exact frame index
        practInstr.tStart = t  # local t and not account for scr refresh
        practInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practInstr, 'tStartRefresh')  # time at next scr refresh
        practInstr.setAutoDraw(True)
    
    # *practInstResp* updates
    waitOnFlip = False
    if practInstResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practInstResp.frameNStart = frameN  # exact frame index
        practInstResp.tStart = t  # local t and not account for scr refresh
        practInstResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practInstResp, 'tStartRefresh')  # time at next scr refresh
        practInstResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practInstResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practInstResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practInstResp.status == STARTED and not waitOnFlip:
        theseKeys = practInstResp.getKeys(keyList=None, waitRelease=False)
        _practInstResp_allKeys.extend(theseKeys)
        if len(_practInstResp_allKeys):
            practInstResp.keys = _practInstResp_allKeys[-1].name  # just the last key pressed
            practInstResp.rt = _practInstResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceInstruction"-------
for thisComponent in practiceInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('practInstr.started', practInstr.tStartRefresh)
thisExp.addData('practInstr.stopped', practInstr.tStopRefresh)
# check responses
if practInstResp.keys in ['', [], None]:  # No response was made
    practInstResp.keys = None
thisExp.addData('practInstResp.keys',practInstResp.keys)
if practInstResp.keys != None:  # we had a response
    thisExp.addData('practInstResp.rt', practInstResp.rt)
thisExp.addData('practInstResp.started', practInstResp.tStartRefresh)
thisExp.addData('practInstResp.stopped', practInstResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceLoop = data.TrialHandler(nReps=doPractice, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)  # add the loop to the experiment
thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in practiceLoop:
    currentLoop = practiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler(nReps=num_practice, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceTrials')
    thisExp.addLoop(practiceTrials)  # add the loop to the experiment
    thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    for thisPracticeTrial in practiceTrials:
        currentLoop = practiceTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                exec('{} = thisPracticeTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlankScreen"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        BlankScreenComponents = [BlackBlank]
        for thisComponent in BlankScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlankScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BlankScreen"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlankScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlankScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BlackBlank* updates
            if BlackBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlackBlank.frameNStart = frameN  # exact frame index
                BlackBlank.tStart = t  # local t and not account for scr refresh
                BlackBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlackBlank, 'tStartRefresh')  # time at next scr refresh
                BlackBlank.setAutoDraw(True)
            if BlackBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BlackBlank.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    BlackBlank.tStop = t  # not accounting for scr refresh
                    BlackBlank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BlackBlank, 'tStopRefresh')  # time at next scr refresh
                    BlackBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlankScreen"-------
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceTrials.addData('BlackBlank.started', BlackBlank.tStartRefresh)
        practiceTrials.addData('BlackBlank.stopped', BlackBlank.tStopRefresh)
        
        # ------Prepare to start Routine "practiceDisplay"-------
        continueRoutine = True
        # update component parameters for each repeat
        from psychopy import visual, core, event, sound
        
        print("pract_idx:")
        print(pract_idx)
        audioFileIdx = int(practice[pract_idx]['AudList']) 
        print(audioFileIdx)
        audioFile = stim['AudNames'][audioFileIdx]
        
        # Check if this is a noise condition
        if practice[pract_idx]['Condition'] % 2 == 1:
            noiseFile = 'audio_clipped_ogg/pink_noise.ogg'
        else:
            noiseFile = 'audio_clipped_ogg/no_noise.ogg'
            
        visualFileIdx = int(practice[pract_idx]['VisList'])
        print(visualFileIdx)
        if visualFileIdx == -1:
            visualFile = 'degraded'
        else:
            visualFile = stim['AudNames'][visualFileIdx]
        
        # Add extensions
        visualFile = visualFile + '.mp4'
        audioFile = audioFile + '.ogg'
        movieFile = 'visual' + '/' + visualFile
        soundFile = 'audio_clipped_ogg' + '/' +  audioFile
        #practSound = sound.Sound(soundFile)
        
        #mov = visual.MovieStim3(win, movieFile, size=(320, 240),
        #    flipVert=False, flipHoriz=False, loop=False)
        #globalClock = core.Clock()
        #nextFlip = win.getFutureFlipTime(clock='ptb')
        
        #stimSound.play(when=nextFlip)  # sync with screen refresh
        #print(audioFile)
        #print(movieFile)
        
        #while mov.status != visual.FINISHED:
        #    mov.draw()
        #    win.flip()
            # if event.getKeys():
            #     break
        
        frameN = stim['FrameAdj'][visualFileIdx]
        movie_stim_pract = visual.MovieStim3(
            win=win, name='movie_stim_pract',
            noAudio = True,
            filename=movieFile,
            ori=0, pos=(0, 0), opacity=1,
            loop=False,
            depth=-1.0,
            )
        sound_stim_pract.setSound(soundFile, hamming=True)
        sound_stim_pract.setVolume(1, log=False)
        noise_pract.setSound(noiseFile, hamming=True)
        noise_pract.setVolume(1, log=False)
        # keep track of which components have finished
        practiceDisplayComponents = [movie_stim_pract, sound_stim_pract, noise_pract]
        for thisComponent in practiceDisplayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceDisplay"-------
        while continueRoutine:
            # get current time
            t = practiceDisplayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceDisplayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *movie_stim_pract* updates
            if movie_stim_pract.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie_stim_pract.frameNStart = frameN  # exact frame index
                movie_stim_pract.tStart = t  # local t and not account for scr refresh
                movie_stim_pract.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie_stim_pract, 'tStartRefresh')  # time at next scr refresh
                movie_stim_pract.setAutoDraw(True)
            if movie_stim_pract.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > movie_stim_pract.tStartRefresh + 1.1-frameTolerance:
                    # keep track of stop time/frame for later
                    movie_stim_pract.tStop = t  # not accounting for scr refresh
                    movie_stim_pract.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(movie_stim_pract, 'tStopRefresh')  # time at next scr refresh
                    movie_stim_pract.setAutoDraw(False)
            if movie_stim_pract.status == FINISHED:  # force-end the routine
                continueRoutine = False
            # start/stop sound_stim_pract
            if sound_stim_pract.status == NOT_STARTED and tThisFlip >= stim['AudOnsets'][(practice[pract_idx]['AudList'])]-frameTolerance:
                # keep track of start time/frame for later
                sound_stim_pract.frameNStart = frameN  # exact frame index
                sound_stim_pract.tStart = t  # local t and not account for scr refresh
                sound_stim_pract.tStartRefresh = tThisFlipGlobal  # on global time
                sound_stim_pract.play(when=win)  # sync with win flip
            # start/stop noise_pract
            if noise_pract.status == NOT_STARTED and tThisFlip >= stim['AudOnsets'][(practice[pract_idx]['AudList'])]-frameTolerance:
                # keep track of start time/frame for later
                noise_pract.frameNStart = frameN  # exact frame index
                noise_pract.tStart = t  # local t and not account for scr refresh
                noise_pract.tStartRefresh = tThisFlipGlobal  # on global time
                noise_pract.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceDisplayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceDisplay"-------
        for thisComponent in practiceDisplayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('audioFileIdx', audioFileIdx)
        thisExp.addData('visualFileIdx', visualFileIdx)
        practiceTrials.addData('movie_stim_pract.started', movie_stim_pract.tStartRefresh)
        practiceTrials.addData('movie_stim_pract.stopped', movie_stim_pract.tStopRefresh)
        sound_stim_pract.stop()  # ensure sound has stopped at end of routine
        practiceTrials.addData('sound_stim_pract.started', sound_stim_pract.tStartRefresh)
        practiceTrials.addData('sound_stim_pract.stopped', sound_stim_pract.tStopRefresh)
        noise_pract.stop()  # ensure sound has stopped at end of routine
        practiceTrials.addData('noise_pract.started', noise_pract.tStartRefresh)
        practiceTrials.addData('noise_pract.stopped', noise_pract.tStopRefresh)
        # the Routine "practiceDisplay" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "practiceResponse"-------
        continueRoutine = True
        routineTimer.add(1.250000)
        # update component parameters for each repeat
        responseOptions = stim['Answers'][(practice[pract_idx]['AudList'])].copy()
        print(responseOptions)
        random.shuffle(responseOptions)
        print(responseOptions)
        
        responseOptionText = responseOptions[0] + \
            '\t\t\t' + responseOptions[1] + \
            '\t\t\t' + responseOptions[2] + \
            '\t\t\t' + responseOptions[3]
            
        correctAnswerIdx = practice[pract_idx]['CorrAnsIdx']
        print(correctAnswerIdx)
        correctAnsText = stim['Answers'][(practice[pract_idx]['AudList'])][correctAnswerIdx]
        print(correctAnsText)
        
        shuffledCorrIdx = responseOptions.index(correctAnsText)
        print(shuffledCorrIdx)
        
        if shuffledCorrIdx == 0:
            correctAnswer = '1'
        elif shuffledCorrIdx == 1:
            correctAnswer = '2'
        elif shuffledCorrIdx == 2:
            correctAnswer = '9'
        elif shuffledCorrIdx == 3:
            correctAnswer = '0'
        print(correctAnswer)
        PracticeRespOptions.setText(responseOptionText)
        PracticeResponse.keys = []
        PracticeResponse.rt = []
        _PracticeResponse_allKeys = []
        # keep track of which components have finished
        practiceResponseComponents = [blackRectP, PracticeRespOptions, PracticeResponse]
        for thisComponent in practiceResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceResponse"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceResponseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceResponseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackRectP* updates
            if blackRectP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackRectP.frameNStart = frameN  # exact frame index
                blackRectP.tStart = t  # local t and not account for scr refresh
                blackRectP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackRectP, 'tStartRefresh')  # time at next scr refresh
                blackRectP.setAutoDraw(True)
            if blackRectP.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackRectP.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    blackRectP.tStop = t  # not accounting for scr refresh
                    blackRectP.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackRectP, 'tStopRefresh')  # time at next scr refresh
                    blackRectP.setAutoDraw(False)
            
            # *PracticeRespOptions* updates
            if PracticeRespOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeRespOptions.frameNStart = frameN  # exact frame index
                PracticeRespOptions.tStart = t  # local t and not account for scr refresh
                PracticeRespOptions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeRespOptions, 'tStartRefresh')  # time at next scr refresh
                PracticeRespOptions.setAutoDraw(True)
            if PracticeRespOptions.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PracticeRespOptions.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    PracticeRespOptions.tStop = t  # not accounting for scr refresh
                    PracticeRespOptions.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracticeRespOptions, 'tStopRefresh')  # time at next scr refresh
                    PracticeRespOptions.setAutoDraw(False)
            
            # *PracticeResponse* updates
            waitOnFlip = False
            if PracticeResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeResponse.frameNStart = frameN  # exact frame index
                PracticeResponse.tStart = t  # local t and not account for scr refresh
                PracticeResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeResponse, 'tStartRefresh')  # time at next scr refresh
                PracticeResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeResponse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PracticeResponse.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    PracticeResponse.tStop = t  # not accounting for scr refresh
                    PracticeResponse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracticeResponse, 'tStopRefresh')  # time at next scr refresh
                    PracticeResponse.status = FINISHED
            if PracticeResponse.status == STARTED and not waitOnFlip:
                theseKeys = PracticeResponse.getKeys(keyList=['1', '2', '9', '0'], waitRelease=False)
                _PracticeResponse_allKeys.extend(theseKeys)
                if len(_PracticeResponse_allKeys):
                    PracticeResponse.keys = _PracticeResponse_allKeys[0].name  # just the first key pressed
                    PracticeResponse.rt = _PracticeResponse_allKeys[0].rt
                    # was this correct?
                    if (PracticeResponse.keys == str(correctAnswer)) or (PracticeResponse.keys == correctAnswer):
                        PracticeResponse.corr = 1
                    else:
                        PracticeResponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceResponse"-------
        for thisComponent in practiceResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        responseOptions = responseOptions[0] + " " + responseOptions[1] + " " + responseOptions[2] + " " + responseOptions[3]
        
        thisExp.addData('responseOptions', responseOptions)
        thisExp.addData('correctResponse', correctAnswer)
        practiceTrials.addData('blackRectP.started', blackRectP.tStartRefresh)
        practiceTrials.addData('blackRectP.stopped', blackRectP.tStopRefresh)
        practiceTrials.addData('PracticeRespOptions.started', PracticeRespOptions.tStartRefresh)
        practiceTrials.addData('PracticeRespOptions.stopped', PracticeRespOptions.tStopRefresh)
        # check responses
        if PracticeResponse.keys in ['', [], None]:  # No response was made
            PracticeResponse.keys = None
            # was no response the correct answer?!
            if str(correctAnswer).lower() == 'none':
               PracticeResponse.corr = 1;  # correct non-response
            else:
               PracticeResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceTrials (TrialHandler)
        practiceTrials.addData('PracticeResponse.keys',PracticeResponse.keys)
        practiceTrials.addData('PracticeResponse.corr', PracticeResponse.corr)
        if PracticeResponse.keys != None:  # we had a response
            practiceTrials.addData('PracticeResponse.rt', PracticeResponse.rt)
        practiceTrials.addData('PracticeResponse.started', PracticeResponse.tStartRefresh)
        practiceTrials.addData('PracticeResponse.stopped', PracticeResponse.tStopRefresh)
        
        if PracticeResponse.keys is None:
            showIncorrectFeedback = 0
            showNoAnswer = 1
        else:
            showNoAnswer = 0
            if PracticeResponse.corr==0:
                showIncorrectFeedback = 1
            else:
                showIncorrectFeedback = 0
        
        # set up handler to look after randomisation of conditions etc
        practCorrect = data.TrialHandler(nReps=PracticeResponse.corr, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practCorrect')
        thisExp.addLoop(practCorrect)  # add the loop to the experiment
        thisPractCorrect = practCorrect.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractCorrect.rgb)
        if thisPractCorrect != None:
            for paramName in thisPractCorrect:
                exec('{} = thisPractCorrect[paramName]'.format(paramName))
        
        for thisPractCorrect in practCorrect:
            currentLoop = practCorrect
            # abbreviate parameter names if possible (e.g. rgb = thisPractCorrect.rgb)
            if thisPractCorrect != None:
                for paramName in thisPractCorrect:
                    exec('{} = thisPractCorrect[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "practiceCorrectFeedback"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            practiceCorrectFeedbackComponents = [blackRectCorr, practiceCorr]
            for thisComponent in practiceCorrectFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            practiceCorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "practiceCorrectFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = practiceCorrectFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=practiceCorrectFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blackRectCorr* updates
                if blackRectCorr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blackRectCorr.frameNStart = frameN  # exact frame index
                    blackRectCorr.tStart = t  # local t and not account for scr refresh
                    blackRectCorr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blackRectCorr, 'tStartRefresh')  # time at next scr refresh
                    blackRectCorr.setAutoDraw(True)
                if blackRectCorr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blackRectCorr.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        blackRectCorr.tStop = t  # not accounting for scr refresh
                        blackRectCorr.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blackRectCorr, 'tStopRefresh')  # time at next scr refresh
                        blackRectCorr.setAutoDraw(False)
                
                # *practiceCorr* updates
                if practiceCorr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    practiceCorr.frameNStart = frameN  # exact frame index
                    practiceCorr.tStart = t  # local t and not account for scr refresh
                    practiceCorr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(practiceCorr, 'tStartRefresh')  # time at next scr refresh
                    practiceCorr.setAutoDraw(True)
                if practiceCorr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > practiceCorr.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        practiceCorr.tStop = t  # not accounting for scr refresh
                        practiceCorr.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(practiceCorr, 'tStopRefresh')  # time at next scr refresh
                        practiceCorr.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practiceCorrectFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practiceCorrectFeedback"-------
            for thisComponent in practiceCorrectFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            practCorrect.addData('blackRectCorr.started', blackRectCorr.tStartRefresh)
            practCorrect.addData('blackRectCorr.stopped', blackRectCorr.tStopRefresh)
            practCorrect.addData('practiceCorr.started', practiceCorr.tStartRefresh)
            practCorrect.addData('practiceCorr.stopped', practiceCorr.tStopRefresh)
        # completed PracticeResponse.corr repeats of 'practCorrect'
        
        
        # set up handler to look after randomisation of conditions etc
        practIncorrect = data.TrialHandler(nReps=showIncorrectFeedback, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practIncorrect')
        thisExp.addLoop(practIncorrect)  # add the loop to the experiment
        thisPractIncorrect = practIncorrect.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractIncorrect.rgb)
        if thisPractIncorrect != None:
            for paramName in thisPractIncorrect:
                exec('{} = thisPractIncorrect[paramName]'.format(paramName))
        
        for thisPractIncorrect in practIncorrect:
            currentLoop = practIncorrect
            # abbreviate parameter names if possible (e.g. rgb = thisPractIncorrect.rgb)
            if thisPractIncorrect != None:
                for paramName in thisPractIncorrect:
                    exec('{} = thisPractIncorrect[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "practiceIncorrectFeedback"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            text_incorrect.setText('Incorrect. \n\n The correct answer was: \n' + \
(stim['Answers'][(practice[pract_idx]['AudList'])][(practice[pract_idx]['CorrAnsIdx'])]) )
            # keep track of which components have finished
            practiceIncorrectFeedbackComponents = [blackRectIncorr, text_incorrect]
            for thisComponent in practiceIncorrectFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            practiceIncorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "practiceIncorrectFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = practiceIncorrectFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blackRectIncorr* updates
                if blackRectIncorr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blackRectIncorr.frameNStart = frameN  # exact frame index
                    blackRectIncorr.tStart = t  # local t and not account for scr refresh
                    blackRectIncorr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blackRectIncorr, 'tStartRefresh')  # time at next scr refresh
                    blackRectIncorr.setAutoDraw(True)
                if blackRectIncorr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blackRectIncorr.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        blackRectIncorr.tStop = t  # not accounting for scr refresh
                        blackRectIncorr.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blackRectIncorr, 'tStopRefresh')  # time at next scr refresh
                        blackRectIncorr.setAutoDraw(False)
                
                # *text_incorrect* updates
                if text_incorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_incorrect.frameNStart = frameN  # exact frame index
                    text_incorrect.tStart = t  # local t and not account for scr refresh
                    text_incorrect.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_incorrect, 'tStartRefresh')  # time at next scr refresh
                    text_incorrect.setAutoDraw(True)
                if text_incorrect.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_incorrect.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_incorrect.tStop = t  # not accounting for scr refresh
                        text_incorrect.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_incorrect, 'tStopRefresh')  # time at next scr refresh
                        text_incorrect.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practiceIncorrectFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practiceIncorrectFeedback"-------
            for thisComponent in practiceIncorrectFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            practIncorrect.addData('blackRectIncorr.started', blackRectIncorr.tStartRefresh)
            practIncorrect.addData('blackRectIncorr.stopped', blackRectIncorr.tStopRefresh)
            practIncorrect.addData('text_incorrect.started', text_incorrect.tStartRefresh)
            practIncorrect.addData('text_incorrect.stopped', text_incorrect.tStopRefresh)
        # completed showIncorrectFeedback repeats of 'practIncorrect'
        
        
        # set up handler to look after randomisation of conditions etc
        practNoAns = data.TrialHandler(nReps=showNoAnswer, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practNoAns')
        thisExp.addLoop(practNoAns)  # add the loop to the experiment
        thisPractNoAn = practNoAns.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractNoAn.rgb)
        if thisPractNoAn != None:
            for paramName in thisPractNoAn:
                exec('{} = thisPractNoAn[paramName]'.format(paramName))
        
        for thisPractNoAn in practNoAns:
            currentLoop = practNoAns
            # abbreviate parameter names if possible (e.g. rgb = thisPractNoAn.rgb)
            if thisPractNoAn != None:
                for paramName in thisPractNoAn:
                    exec('{} = thisPractNoAn[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "practiceNoAnsFeedback"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            # keep track of which components have finished
            practiceNoAnsFeedbackComponents = [rectNoAns, practNoAnsText]
            for thisComponent in practiceNoAnsFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            practiceNoAnsFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "practiceNoAnsFeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = practiceNoAnsFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=practiceNoAnsFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rectNoAns* updates
                if rectNoAns.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rectNoAns.frameNStart = frameN  # exact frame index
                    rectNoAns.tStart = t  # local t and not account for scr refresh
                    rectNoAns.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rectNoAns, 'tStartRefresh')  # time at next scr refresh
                    rectNoAns.setAutoDraw(True)
                if rectNoAns.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rectNoAns.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        rectNoAns.tStop = t  # not accounting for scr refresh
                        rectNoAns.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rectNoAns, 'tStopRefresh')  # time at next scr refresh
                        rectNoAns.setAutoDraw(False)
                
                # *practNoAnsText* updates
                if practNoAnsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    practNoAnsText.frameNStart = frameN  # exact frame index
                    practNoAnsText.tStart = t  # local t and not account for scr refresh
                    practNoAnsText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(practNoAnsText, 'tStartRefresh')  # time at next scr refresh
                    practNoAnsText.setAutoDraw(True)
                if practNoAnsText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > practNoAnsText.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        practNoAnsText.tStop = t  # not accounting for scr refresh
                        practNoAnsText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(practNoAnsText, 'tStopRefresh')  # time at next scr refresh
                        practNoAnsText.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practiceNoAnsFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practiceNoAnsFeedback"-------
            for thisComponent in practiceNoAnsFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            practNoAns.addData('rectNoAns.started', rectNoAns.tStartRefresh)
            practNoAns.addData('rectNoAns.stopped', rectNoAns.tStopRefresh)
            practNoAns.addData('practNoAnsText.started', practNoAnsText.tStartRefresh)
            practNoAns.addData('practNoAnsText.stopped', practNoAnsText.tStopRefresh)
        # completed showNoAnswer repeats of 'practNoAns'
        
        
        # ------Prepare to start Routine "increment_pract_idx"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        increment_pract_idxComponents = []
        for thisComponent in increment_pract_idxComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        increment_pract_idxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "increment_pract_idx"-------
        while continueRoutine:
            # get current time
            t = increment_pract_idxClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=increment_pract_idxClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in increment_pract_idxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "increment_pract_idx"-------
        for thisComponent in increment_pract_idxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pract_idx = pract_idx+1
        # the Routine "increment_pract_idx" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_practice repeats of 'practiceTrials'
    
# completed doPractice repeats of 'practiceLoop'


# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [blackScreen2, text, key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blackScreen2* updates
    if blackScreen2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blackScreen2.frameNStart = frameN  # exact frame index
        blackScreen2.tStart = t  # local t and not account for scr refresh
        blackScreen2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blackScreen2, 'tStartRefresh')  # time at next scr refresh
        blackScreen2.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blackScreen2.started', blackScreen2.tStartRefresh)
thisExp.addData('blackScreen2.stopped', blackScreen2.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
stimTrials = data.TrialHandler(nReps=trials_to_run, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='stimTrials')
thisExp.addLoop(stimTrials)  # add the loop to the experiment
thisStimTrial = stimTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStimTrial.rgb)
if thisStimTrial != None:
    for paramName in thisStimTrial:
        exec('{} = thisStimTrial[paramName]'.format(paramName))

for thisStimTrial in stimTrials:
    currentLoop = stimTrials
    # abbreviate parameter names if possible (e.g. rgb = thisStimTrial.rgb)
    if thisStimTrial != None:
        for paramName in thisStimTrial:
            exec('{} = thisStimTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stimDisplay"-------
    continueRoutine = True
    # update component parameters for each repeat
    print("stim_idx:")
    print(stim_idx)
    
    audioFileIdx = int(trialList[stim_idx]['AudList']) 
    print(audioFileIdx)
    audioFile = stim['AudNames'][audioFileIdx]
    
    visualFileIdx = int(trialList[stim_idx]['VisList']) 
    print(visualFileIdx)
    
    
    if visualFileIdx == -1:
        visualFile = 'degraded'
    else:
        visualFile = stim['AudNames'][visualFileIdx]
    
    if trialList[stim_idx]['Condition'] % 2 == 1:
        noiseFile = 'audio_clipped_ogg/pink_noise.ogg'
    else:
        noiseFile = 'audio_clipped_ogg/no_noise.ogg'
        
    # Add extensions
    visualFile = visualFile + '.mp4'
    audioFile = audioFile + '.ogg'
    movieFile = 'visual/'+ visualFile
    soundFile = 'audio_clipped_ogg/' + audioFile
    stimSound = sound.Sound(soundFile)
    frameN = stim["FrameAdj"][visualFileIdx] - 1;
    
    #mov = visual.MovieStim3(win, movieFile, size=(320, 240),
    #    flipVert=False, flipHoriz=False, loop=False)
    #globalClock = core.Clock()
    #nextFlip = win.getFutureFlipTime(clock='ptb')
    
    #stimSound.play(when=nextFlip)  # sync with screen refresh
    #print(audioFile)
    #print(movieFile)
    
    #while mov.status != visual.FINISHED:
    #    mov.draw()
    #    win.flip()
        # if event.getKeys():
        #     break
    
    #thisExp.addData('audioFileIdx', audioFileIdx)
    #thisExp.addData('visualFileIdx', visualFileIdx)
    
    
    movie_stim = visual.MovieStim3(
        win=win, name='movie_stim',
        noAudio = False,
        filename=movieFile,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=-1.0,
        )
    sound_stim.setSound(soundFile, hamming=True)
    sound_stim.setVolume(1, log=False)
    noise_stim.setSound(noiseFile, hamming=True)
    noise_stim.setVolume(1, log=False)
    # keep track of which components have finished
    stimDisplayComponents = [movie_stim, sound_stim, noise_stim]
    for thisComponent in stimDisplayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimDisplay"-------
    while continueRoutine:
        # get current time
        t = stimDisplayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimDisplayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_stim* updates
        if movie_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie_stim.frameNStart = frameN  # exact frame index
            movie_stim.tStart = t  # local t and not account for scr refresh
            movie_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie_stim, 'tStartRefresh')  # time at next scr refresh
            movie_stim.setAutoDraw(True)
        if movie_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie_stim.tStartRefresh + 1.1-frameTolerance:
                # keep track of stop time/frame for later
                movie_stim.tStop = t  # not accounting for scr refresh
                movie_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie_stim, 'tStopRefresh')  # time at next scr refresh
                movie_stim.setAutoDraw(False)
        if movie_stim.status == FINISHED:  # force-end the routine
            continueRoutine = False
        # start/stop sound_stim
        if sound_stim.status == NOT_STARTED and tThisFlip >= stim['AudOnsets'][(trialList[stim_idx]['AudList'])]-frameTolerance:
            # keep track of start time/frame for later
            sound_stim.frameNStart = frameN  # exact frame index
            sound_stim.tStart = t  # local t and not account for scr refresh
            sound_stim.tStartRefresh = tThisFlipGlobal  # on global time
            sound_stim.play(when=win)  # sync with win flip
        # start/stop noise_stim
        if noise_stim.status == NOT_STARTED and tThisFlip >= stim['AudOnsets'][(trialList[stim_idx]['AudList'])]-frameTolerance:
            # keep track of start time/frame for later
            noise_stim.frameNStart = frameN  # exact frame index
            noise_stim.tStart = t  # local t and not account for scr refresh
            noise_stim.tStartRefresh = tThisFlipGlobal  # on global time
            noise_stim.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimDisplayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimDisplay"-------
    for thisComponent in stimDisplayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('audioFileIdx', audioFileIdx)
    thisExp.addData('visualFileIdx', visualFileIdx)
    stimTrials.addData('movie_stim.started', movie_stim.tStartRefresh)
    stimTrials.addData('movie_stim.stopped', movie_stim.tStopRefresh)
    sound_stim.stop()  # ensure sound has stopped at end of routine
    stimTrials.addData('sound_stim.started', sound_stim.tStartRefresh)
    stimTrials.addData('sound_stim.stopped', sound_stim.tStopRefresh)
    noise_stim.stop()  # ensure sound has stopped at end of routine
    stimTrials.addData('noise_stim.started', noise_stim.tStartRefresh)
    stimTrials.addData('noise_stim.stopped', noise_stim.tStopRefresh)
    # the Routine "stimDisplay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    responseOptions = stim['Answers'][(trialList[stim_idx]['AudList'])].copy()
    print(responseOptions)
    random.shuffle(responseOptions)
    print(responseOptions)
    
    responseOptionText = responseOptions[0] + \
        '\t\t\t' + responseOptions[1] + \
        '\t\t\t' + responseOptions[2] + \
        '\t\t\t' + responseOptions[3]
        
    
    StimRespOpts.setText(responseOptionText)
    StimResponseKey.keys = []
    StimResponseKey.rt = []
    _StimResponseKey_allKeys = []
    # keep track of which components have finished
    stimResponseComponents = [BlackRectStim, StimRespOpts, StimResponseKey]
    for thisComponent in stimResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimResponse"-------
    while continueRoutine:
        # get current time
        t = stimResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlackRectStim* updates
        if BlackRectStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlackRectStim.frameNStart = frameN  # exact frame index
            BlackRectStim.tStart = t  # local t and not account for scr refresh
            BlackRectStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlackRectStim, 'tStartRefresh')  # time at next scr refresh
            BlackRectStim.setAutoDraw(True)
        if BlackRectStim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlackRectStim.tStartRefresh + rt-frameTolerance:
                # keep track of stop time/frame for later
                BlackRectStim.tStop = t  # not accounting for scr refresh
                BlackRectStim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlackRectStim, 'tStopRefresh')  # time at next scr refresh
                BlackRectStim.setAutoDraw(False)
        
        # *StimRespOpts* updates
        if StimRespOpts.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimRespOpts.frameNStart = frameN  # exact frame index
            StimRespOpts.tStart = t  # local t and not account for scr refresh
            StimRespOpts.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimRespOpts, 'tStartRefresh')  # time at next scr refresh
            StimRespOpts.setAutoDraw(True)
        if StimRespOpts.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimRespOpts.tStartRefresh + rt-frameTolerance:
                # keep track of stop time/frame for later
                StimRespOpts.tStop = t  # not accounting for scr refresh
                StimRespOpts.frameNStop = frameN  # exact frame index
                win.timeOnFlip(StimRespOpts, 'tStopRefresh')  # time at next scr refresh
                StimRespOpts.setAutoDraw(False)
        
        # *StimResponseKey* updates
        waitOnFlip = False
        if StimResponseKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StimResponseKey.frameNStart = frameN  # exact frame index
            StimResponseKey.tStart = t  # local t and not account for scr refresh
            StimResponseKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimResponseKey, 'tStartRefresh')  # time at next scr refresh
            StimResponseKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(StimResponseKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(StimResponseKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if StimResponseKey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimResponseKey.tStartRefresh + rt-frameTolerance:
                # keep track of stop time/frame for later
                StimResponseKey.tStop = t  # not accounting for scr refresh
                StimResponseKey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(StimResponseKey, 'tStopRefresh')  # time at next scr refresh
                StimResponseKey.status = FINISHED
        if StimResponseKey.status == STARTED and not waitOnFlip:
            theseKeys = StimResponseKey.getKeys(keyList=['1', '2', '9', '0'], waitRelease=False)
            _StimResponseKey_allKeys.extend(theseKeys)
            if len(_StimResponseKey_allKeys):
                StimResponseKey.keys = _StimResponseKey_allKeys[0].name  # just the first key pressed
                StimResponseKey.rt = _StimResponseKey_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimResponse"-------
    for thisComponent in stimResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    responseOptions = responseOptions[0] + " " + responseOptions[1] + " " + responseOptions[2] + " " + responseOptions[3]
    
    thisExp.addData('responseOptions', responseOptions)
    
    stimTrials.addData('BlackRectStim.started', BlackRectStim.tStartRefresh)
    stimTrials.addData('BlackRectStim.stopped', BlackRectStim.tStopRefresh)
    stimTrials.addData('StimRespOpts.started', StimRespOpts.tStartRefresh)
    stimTrials.addData('StimRespOpts.stopped', StimRespOpts.tStopRefresh)
    # check responses
    if StimResponseKey.keys in ['', [], None]:  # No response was made
        StimResponseKey.keys = None
    stimTrials.addData('StimResponseKey.keys',StimResponseKey.keys)
    if StimResponseKey.keys != None:  # we had a response
        stimTrials.addData('StimResponseKey.rt', StimResponseKey.rt)
    stimTrials.addData('StimResponseKey.started', StimResponseKey.tStartRefresh)
    stimTrials.addData('StimResponseKey.stopped', StimResponseKey.tStopRefresh)
    # the Routine "stimResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rt_adjust"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    rt_adjustComponents = []
    for thisComponent in rt_adjustComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rt_adjustClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rt_adjust"-------
    while continueRoutine:
        # get current time
        t = rt_adjustClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rt_adjustClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rt_adjustComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rt_adjust"-------
    for thisComponent in rt_adjustComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print(StimResponseKey.keys)
    print(non_missed_trials)
    print(rt)
    if StimResponseKey.keys is None:
        non_missed_trials = 0
        if rt <= 1.75:
            # Increase to a maximum of 2 seconds
            rt = rt + 0.25  
    else:
        non_missed_trials += 1
    
    if non_missed_trials >= 10 and rt >= 1.5:
        # Decrease to a minimum of 1.25 seconds
        rt = rt - 0.25
    print(rt)
    # the Routine "rt_adjust" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Inc_stim_idx"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Inc_stim_idxComponents = []
    for thisComponent in Inc_stim_idxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Inc_stim_idxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Inc_stim_idx"-------
    while continueRoutine:
        # get current time
        t = Inc_stim_idxClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Inc_stim_idxClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Inc_stim_idxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Inc_stim_idx"-------
    for thisComponent in Inc_stim_idxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stim_idx = stim_idx + 1
    # the Routine "Inc_stim_idx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "BlankScreen"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankScreenComponents = [BlackBlank]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlankScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlankScreen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlankScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlackBlank* updates
        if BlackBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlackBlank.frameNStart = frameN  # exact frame index
            BlackBlank.tStart = t  # local t and not account for scr refresh
            BlackBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlackBlank, 'tStartRefresh')  # time at next scr refresh
            BlackBlank.setAutoDraw(True)
        if BlackBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlackBlank.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                BlackBlank.tStop = t  # not accounting for scr refresh
                BlackBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlackBlank, 'tStopRefresh')  # time at next scr refresh
                BlackBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlankScreen"-------
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimTrials.addData('BlackBlank.started', BlackBlank.tStartRefresh)
    stimTrials.addData('BlackBlank.stopped', BlackBlank.tStopRefresh)
    thisExp.nextEntry()
    
# completed trials_to_run repeats of 'stimTrials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
