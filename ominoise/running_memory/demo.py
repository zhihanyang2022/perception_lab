#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Feb 13 11:51:41 2020
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

# my imports
import time
import keyboard as k

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'demo'  # from the Builder filename that created this script
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
    originPath='/Users/yangzhihan/Desktop/projects/perception_lab/demo_program/demo.py',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
instructions_keyresp = keyboard.Keyboard()

# Initialize components for Routine "show_condition"
show_conditionClock = core.Clock()
show_condition_text = visual.TextStim(win=win, name='show_condition_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
instructions_keyresp.keys = []
instructions_keyresp.rt = []
# keep track of which components have finished
instructionsComponents = [instructions_text, instructions_keyresp]
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
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)

    # *instructions_keyresp* updates
    waitOnFlip = False
    if instructions_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_keyresp.frameNStart = frameN  # exact frame index
        instructions_keyresp.tStart = t  # local t and not account for scr refresh
        instructions_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_keyresp, 'tStartRefresh')  # time at next scr refresh
        instructions_keyresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_keyresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = instructions_keyresp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            instructions_keyresp.keys = theseKeys.name  # just the last key pressed
            instructions_keyresp.rt = theseKeys.rt
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
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
# check responses
if instructions_keyresp.keys in ['', [], None]:  # No response was made
    instructions_keyresp.keys = None
thisExp.addData('instructions_keyresp.keys',instructions_keyresp.keys)
if instructions_keyresp.keys != None:  # we had a response
    thisExp.addData('instructions_keyresp.rt', instructions_keyresp.rt)
thisExp.addData('instructions_keyresp.started', instructions_keyresp.tStartRefresh)
thisExp.addData('instructions_keyresp.stopped', instructions_keyresp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# =====

# utility functions

# def init_timestamps(component):
#     component.tStart = None
#     component.tStop = None
#     component.tStartRefresh = None
#     component.tStopRefresh = None
#     if hasattr(component, 'status'):
#         component.status = NOT_STARTED

class ComponentTimer():

    def __init__(self):
        self.tStartRefresh = None
        self.tStopRefresh = None

# initialize containers for used components
used_components = []

# level 1: loop through the noise conditions
loop_noises = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('csvs/noise_conditions.csv'),
    seed=None, name='loop_noises')

for thisNoise in loop_noises:
    condition = thisNoise['condition']

    # level 2: loop through the set of word lists
    # print(condition)
    loop_lists = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('csvs/condition_{}_wlists_indices.csv'.format(condition)),
        seed=None, name='loop_lists')

    for thisList in loop_lists:
        wlist_index = thisList['wlist_index'] # initialize variable "wlist_index"

        # level 3: loop through words
        # print(wlist_index)
        loop_words = data.TrialHandler(nReps=1, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('csvs/{}.csv'.format(wlist_index)),
            seed=None, name='loop_words')

        recallTimer = ComponentTimer()

        for thisWord in loop_words:
            word = thisWord['word'] # initialize variable "word"

            show_condition_text.setText(word)  # show word on screen

            show_conditionComponents = [show_condition_text]
            show_condition_text.status = NOT_STARTED  # can't remove this, cause continueRoutine = False
            # for thisComponent in show_conditionComponents: init_timestamps(thisComponent)

            # reset timers
            # t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")  # how far is the next frame flip in ms, all local flip clocks are used with frameTolerance
            show_conditionClock.reset(-_timeToFirstFrame)  # so that when it is the next frame, clock is zero
            frameN = -1
            continueRoutine = True

            routineTimer.reset(0.01000)  # conventional clock, each word gets displayed for 3 seconds
            while continueRoutine and routineTimer.getTime() > 0:

                ### update timers
                t = show_conditionClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=show_conditionClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames

                ### update/draw components on each frame

                # *show_condition_text* updates
                if show_condition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    show_condition_text.setAutoDraw(True)
                    show_condition_text.status = NOT_STARTED  # so that the timestamp attributes won't get updated again

                ### check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()

                ### check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break

                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in show_conditionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                ### refresh the screen (we've been predicting this for a while...)
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "show_condition"-------
            for thisComponent in show_conditionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # trials.addData('show_condition_text.started', show_condition_text.tStartRefresh)
            # trials.addData('show_condition_text.stopped', show_condition_text.tStopRefresh)
            # thisExp.nextEntry()

        is_first_frame = True
        while True:
            if defaultKeyboard.getKeys(keyList=["space"]):
                win.timeOnFlip(recallTimer, 'tStopRefresh')
                win.flip()
                used_components.append(recallTimer)  # process the timestamps later
                break
            else:
                if is_first_frame:
                    win.timeOnFlip(recallTimer, 'tStartRefresh')
                    # or recallTimer.tStartRefresh = win.getFutureFlipTime(clock=None)
                    is_first_frame = False
                show_condition_text.setText("****")
                show_condition_text.setAutoDraw(True)
                win.flip()

# completed 1 repeats of 'trials'

### save information from used components into a csv file

for i, cmp in enumerate(used_components):
    print('index {} | start: {} | stop: {}'.format(i+1, cmp.tStartRefresh, cmp.tStopRefresh))

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
