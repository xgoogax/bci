#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Fri Oct 25 16:39:20 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel
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
psychopyVersion = '3.2.4'
expName = 'exp'  # from the Builder filename that created this script
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
    originPath='/Users/agatawlaszczyk/Documents/bci/exp_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "prawa"
prawaClock = core.Clock()
bodziec_prawa = visual.TextStim(win=win, name='bodziec_prawa',
    text='PRAWA REKA',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
relaksacja = visual.TextStim(win=win, name='relaksacja',
    text=' + ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "lewa"
lewaClock = core.Clock()
relaksacja2 = visual.TextStim(win=win, name='relaksacja2',
    text=' + ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
bodziec_lewa = visual.TextStim(win=win, name='bodziec_lewa',
    text='LEWA REKA',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
powtorzenia = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='powtorzenia')
thisExp.addLoop(powtorzenia)  # add the loop to the experiment
thisPowtorzenia = powtorzenia.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPowtorzenia.rgb)
if thisPowtorzenia != None:
    for paramName in thisPowtorzenia:
        exec('{} = thisPowtorzenia[paramName]'.format(paramName))

for thisPowtorzenia in powtorzenia:
    currentLoop = powtorzenia
    # abbreviate parameter names if possible (e.g. rgb = thisPowtorzenia.rgb)
    if thisPowtorzenia != None:
        for paramName in thisPowtorzenia:
            exec('{} = thisPowtorzenia[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prawa"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    prawaComponents = [bodziec_prawa, relaksacja]
    for thisComponent in prawaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prawaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "prawa"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prawaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prawaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bodziec_prawa* updates
        if bodziec_prawa.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            bodziec_prawa.frameNStart = frameN  # exact frame index
            bodziec_prawa.tStart = t  # local t and not account for scr refresh
            bodziec_prawa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bodziec_prawa, 'tStartRefresh')  # time at next scr refresh
            bodziec_prawa.setAutoDraw(True)
        if bodziec_prawa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bodziec_prawa.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                bodziec_prawa.tStop = t  # not accounting for scr refresh
                bodziec_prawa.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bodziec_prawa, 'tStopRefresh')  # time at next scr refresh
                bodziec_prawa.setAutoDraw(False)
        
        # *relaksacja* updates
        if relaksacja.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            relaksacja.frameNStart = frameN  # exact frame index
            relaksacja.tStart = t  # local t and not account for scr refresh
            relaksacja.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(relaksacja, 'tStartRefresh')  # time at next scr refresh
            relaksacja.setAutoDraw(True)
        if relaksacja.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > relaksacja.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                relaksacja.tStop = t  # not accounting for scr refresh
                relaksacja.frameNStop = frameN  # exact frame index
                win.timeOnFlip(relaksacja, 'tStopRefresh')  # time at next scr refresh
                relaksacja.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prawaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prawa"-------
    for thisComponent in prawaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    powtorzenia.addData('bodziec_prawa.started', bodziec_prawa.tStartRefresh)
    powtorzenia.addData('bodziec_prawa.stopped', bodziec_prawa.tStopRefresh)
    powtorzenia.addData('relaksacja.started', relaksacja.tStartRefresh)
    powtorzenia.addData('relaksacja.stopped', relaksacja.tStopRefresh)
    
    # ------Prepare to start Routine "lewa"-------
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    lewaComponents = [relaksacja2, bodziec_lewa]
    for thisComponent in lewaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    lewaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "lewa"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lewaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=lewaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *relaksacja2* updates
        if relaksacja2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            relaksacja2.frameNStart = frameN  # exact frame index
            relaksacja2.tStart = t  # local t and not account for scr refresh
            relaksacja2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(relaksacja2, 'tStartRefresh')  # time at next scr refresh
            relaksacja2.setAutoDraw(True)
        if relaksacja2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > relaksacja2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                relaksacja2.tStop = t  # not accounting for scr refresh
                relaksacja2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(relaksacja2, 'tStopRefresh')  # time at next scr refresh
                relaksacja2.setAutoDraw(False)
        
        # *bodziec_lewa* updates
        if bodziec_lewa.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            bodziec_lewa.frameNStart = frameN  # exact frame index
            bodziec_lewa.tStart = t  # local t and not account for scr refresh
            bodziec_lewa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bodziec_lewa, 'tStartRefresh')  # time at next scr refresh
            bodziec_lewa.setAutoDraw(True)
        if bodziec_lewa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bodziec_lewa.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                bodziec_lewa.tStop = t  # not accounting for scr refresh
                bodziec_lewa.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bodziec_lewa, 'tStopRefresh')  # time at next scr refresh
                bodziec_lewa.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lewaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "lewa"-------
    for thisComponent in lewaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    powtorzenia.addData('relaksacja2.started', relaksacja2.tStartRefresh)
    powtorzenia.addData('relaksacja2.stopped', relaksacja2.tStopRefresh)
    powtorzenia.addData('bodziec_lewa.started', bodziec_lewa.tStartRefresh)
    powtorzenia.addData('bodziec_lewa.stopped', bodziec_lewa.tStopRefresh)
    thisExp.nextEntry()
    
# completed 50 repeats of 'powtorzenia'


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
