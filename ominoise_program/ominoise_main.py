#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Feb  4 10:48:32 2020
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

# Added by Zhihan
print('Code not over-written!')

# Added by Zhihan
import csv

CONDITIONS = ['condition_1', 'condition_2', 'condition_3', 'condition_4']  # must use alphanumerics and underscores
NUM_LISTS = 32

def random_wlists_indices_assignment():

    wlists_indices = np.arange(1, NUM_LISTS+1)
    # np.random.seed(42), don't use random seed here; we want each participant to see a different order
    wlists_indices_random = np.random.choice(wlists_indices, size=NUM_LISTS, replace=False)
    wlists_indices_assignment = np.split(wlists_indices_random, 4)

    for i, c in enumerate(CONDITIONS):
        with open(f'./csvs/{c}_wlists_indices.csv', 'w') as csv_f:
            csv_writer = csv.writer(csv_f)
            csv_writer.writerow(['wlist_index'])
            for wlists_index in wlists_indices_assignment[i]:
                csv_writer.writerow([wlists_index])

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'ominoise_main'  # from the Builder filename that created this script
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
    originPath='/Users/labuser/Desktop/ominoise_program/ominoise_main.py',
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

# Initialize components for Routine "_instructions"
_instructionsClock = core.Clock()
__instructions = visual.TextStim(win=win, name='__instructions',
    text='TODO: ominoise instructions\n\nTODO: press space bar to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
__continue = keyboard.Keyboard()

# Initialize components for Routine "RMshow_noise"
RMshow_noiseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "RMshow_list"
RMshow_listClock = core.Clock()
RMshow_list_text = visual.TextStim(win=win, name='RMshow_list_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
RMshow_list_resp = keyboard.Keyboard()

# Initialize components for Routine "RMshow_word"
RMshow_wordClock = core.Clock()
RMshow_word_text = visual.TextStim(win=win, name='RMshow_word_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
RMshow_word_resp = keyboard.Keyboard()

# Initialize components for Routine "_see_word"
_see_wordClock = core.Clock()

# Initialize components for Routine "_bye"
_byeClock = core.Clock()
_bye_text = visual.TextStim(win=win, name='_bye_text',
    text='Todo: Bye bye!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
_bye_keyboard = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "_instructions"-------
# update component parameters for each repeat
__continue.keys = []
__continue.rt = []
# keep track of which components have finished
_instructionsComponents = [__instructions, __continue]
for thisComponent in _instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "_instructions"-------
while continueRoutine:
    # get current time
    t = _instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *__instructions* updates
    if __instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        __instructions.frameNStart = frameN  # exact frame index
        __instructions.tStart = t  # local t and not account for scr refresh
        __instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(__instructions, 'tStartRefresh')  # time at next scr refresh
        __instructions.setAutoDraw(True)

    # *__continue* updates
    waitOnFlip = False
    if __continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        __continue.frameNStart = frameN  # exact frame index
        __continue.tStart = t  # local t and not account for scr refresh
        __continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(__continue, 'tStartRefresh')  # time at next scr refresh
        __continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(__continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(__continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if __continue.status == STARTED and not waitOnFlip:
        theseKeys = __continue.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            __continue.keys = theseKeys.name  # just the last key pressed
            __continue.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_instructions"-------
for thisComponent in _instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('__instructions.started', __instructions.tStartRefresh)
thisExp.addData('__instructions.stopped', __instructions.tStopRefresh)
# check responses
if __continue.keys in ['', [], None]:  # No response was made
    __continue.keys = None
thisExp.addData('__continue.keys',__continue.keys)
if __continue.keys != None:  # we had a response
    thisExp.addData('__continue.rt', __continue.rt)
thisExp.addData('__continue.started', __continue.tStartRefresh)
thisExp.addData('__continue.stopped', __continue.tStopRefresh)
thisExp.nextEntry()
# the Routine "_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
_loop_noises = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('csvs/noise_conditions.csv'),
    seed=None, name='_loop_noises')
thisExp.addLoop(_loop_noises)  # add the loop to the experiment
this_loop_noise = _loop_noises.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = this_loop_noise.rgb)
if this_loop_noise != None:
    for paramName in this_loop_noise:  # assign each variable to their corresponding value
        exec('{} = this_loop_noise[paramName]'.format(paramName))

for this_loop_noise in _loop_noises:
    currentLoop = _loop_noises
    # abbreviate parameter names if possible (e.g. rgb = this_loop_noise.rgb)
    if this_loop_noise != None:
        for paramName in this_loop_noise:
            exec('{} = this_loop_noise[paramName]'.format(paramName))

    # ------Prepare to start Routine "RMshow_noise"-------
    # update component parameters for each repeat
    text.setText(condition)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    RMshow_noiseComponents = [text, key_resp]
    for thisComponent in RMshow_noiseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RMshow_noiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True

    # -------Run Routine "RMshow_noise"-------
    while continueRoutine:
        # get current time
        t = RMshow_noiseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RMshow_noiseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

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
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed

                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RMshow_noiseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "RMshow_noise"-------
    for thisComponent in RMshow_noiseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    _loop_noises.addData('text.started', text.tStartRefresh)
    _loop_noises.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    _loop_noises.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        _loop_noises.addData('key_resp.rt', key_resp.rt)
    _loop_noises.addData('key_resp.started', key_resp.tStartRefresh)
    _loop_noises.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "RMshow_noise" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    _loop_lists = data.TrialHandler(nReps=1, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('csvs/{0}_wlists_indices.csv'.format(condition)),  # ADDED BY ZHIHAN
        seed=None, name='_loop_lists')
    thisExp.addLoop(_loop_lists)  # add the loop to the experiment
    this_loop_list = _loop_lists.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = this_loop_list.rgb)
    if this_loop_list != None:
        for paramName in this_loop_list:
            exec('{} = this_loop_list[paramName]'.format(paramName))

    for this_loop_list in _loop_lists:
        currentLoop = _loop_lists
        # abbreviate parameter names if possible (e.g. rgb = this_loop_list.rgb)
        if this_loop_list != None:
            for paramName in this_loop_list:
                exec('{} = this_loop_list[paramName]'.format(paramName))

        # ------Prepare to start Routine "RMshow_list"-------
        # update component parameters for each repeat
        RMshow_list_text.setText('List index: ' + str(wlistIndex))  # ADDED BY ZHIHAN
        RMshow_list_resp.keys = []
        RMshow_list_resp.rt = []
        # keep track of which components have finished
        RMshow_listComponents = [RMshow_list_text, RMshow_list_resp]
        for thisComponent in RMshow_listComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RMshow_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True

        # -------Run Routine "RMshow_list"-------
        while continueRoutine:
            # get current time
            t = RMshow_listClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RMshow_listClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *RMshow_list_text* updates
            if RMshow_list_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RMshow_list_text.frameNStart = frameN  # exact frame index
                RMshow_list_text.tStart = t  # local t and not account for scr refresh
                RMshow_list_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RMshow_list_text, 'tStartRefresh')  # time at next scr refresh
                RMshow_list_text.setAutoDraw(True)
            if RMshow_list_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RMshow_list_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RMshow_list_text.tStop = t  # not accounting for scr refresh
                    RMshow_list_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(RMshow_list_text, 'tStopRefresh')  # time at next scr refresh
                    RMshow_list_text.setAutoDraw(False)

            # *RMshow_list_resp* updates
            waitOnFlip = False
            if RMshow_list_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RMshow_list_resp.frameNStart = frameN  # exact frame index
                RMshow_list_resp.tStart = t  # local t and not account for scr refresh
                RMshow_list_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RMshow_list_resp, 'tStartRefresh')  # time at next scr refresh
                RMshow_list_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RMshow_list_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RMshow_list_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if RMshow_list_resp.status == STARTED and not waitOnFlip:
                theseKeys = RMshow_list_resp.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed

                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    RMshow_list_resp.keys = theseKeys.name  # just the last key pressed
                    RMshow_list_resp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RMshow_listComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "RMshow_list"-------
        for thisComponent in RMshow_listComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        _loop_lists.addData('RMshow_list_text.started', RMshow_list_text.tStartRefresh)
        _loop_lists.addData('RMshow_list_text.stopped', RMshow_list_text.tStopRefresh)
        # check responses
        if RMshow_list_resp.keys in ['', [], None]:  # No response was made
            RMshow_list_resp.keys = None
        _loop_lists.addData('RMshow_list_resp.keys',RMshow_list_resp.keys)
        if RMshow_list_resp.keys != None:  # we had a response
            _loop_lists.addData('RMshow_list_resp.rt', RMshow_list_resp.rt)
        _loop_lists.addData('RMshow_list_resp.started', RMshow_list_resp.tStartRefresh)
        _loop_lists.addData('RMshow_list_resp.stopped', RMshow_list_resp.tStopRefresh)
        # the Routine "RMshow_list" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

        # set up handler to look after randomisation of conditions etc
        _loop_words = data.TrialHandler(nReps=1, method='random',
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('csvs/{0}.csv'.format(wlistIndex)),  # Added by Zhihan
            seed=None, name='_loop_words')
        thisExp.addLoop(_loop_words)  # add the loop to the experiment
        this_loop_word = _loop_words.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = this_loop_word.rgb)
        if this_loop_word != None:
            for paramName in this_loop_word:
                exec('{} = this_loop_word[paramName]'.format(paramName))

        for this_loop_word in _loop_words:
            currentLoop = _loop_words
            # abbreviate parameter names if possible (e.g. rgb = this_loop_word.rgb)
            if this_loop_word != None:
                for paramName in this_loop_word:
                    exec('{} = this_loop_word[paramName]'.format(paramName))

            # ------Prepare to start Routine "RMshow_word"-------
            # update component parameters for each repeat
            RMshow_word_text.setText(word)
            RMshow_word_resp.keys = []
            RMshow_word_resp.rt = []
            # keep track of which components have finished
            RMshow_wordComponents = [RMshow_word_text, RMshow_word_resp]
            for thisComponent in RMshow_wordComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            RMshow_wordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True

            # -------Run Routine "RMshow_word"-------
            while continueRoutine:
                # get current time
                t = RMshow_wordClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=RMshow_wordClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame

                # *RMshow_word_text* updates
                if RMshow_word_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RMshow_word_text.frameNStart = frameN  # exact frame index
                    RMshow_word_text.tStart = t  # local t and not account for scr refresh
                    RMshow_word_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RMshow_word_text, 'tStartRefresh')  # time at next scr refresh
                    RMshow_word_text.setAutoDraw(True)
                if RMshow_word_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RMshow_word_text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        RMshow_word_text.tStop = t  # not accounting for scr refresh
                        RMshow_word_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(RMshow_word_text, 'tStopRefresh')  # time at next scr refresh
                        RMshow_word_text.setAutoDraw(False)

                # *RMshow_word_resp* updates
                waitOnFlip = False
                if RMshow_word_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RMshow_word_resp.frameNStart = frameN  # exact frame index
                    RMshow_word_resp.tStart = t  # local t and not account for scr refresh
                    RMshow_word_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RMshow_word_resp, 'tStartRefresh')  # time at next scr refresh
                    RMshow_word_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(RMshow_word_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(RMshow_word_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if RMshow_word_resp.status == STARTED and not waitOnFlip:
                    theseKeys = RMshow_word_resp.getKeys(keyList=['space'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed

                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        RMshow_word_resp.keys = theseKeys.name  # just the last key pressed
                        RMshow_word_resp.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False

                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()

                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RMshow_wordComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "RMshow_word"-------
            for thisComponent in RMshow_wordComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            _loop_words.addData('RMshow_word_text.started', RMshow_word_text.tStartRefresh)
            _loop_words.addData('RMshow_word_text.stopped', RMshow_word_text.tStopRefresh)
            # check responses
            if RMshow_word_resp.keys in ['', [], None]:  # No response was made
                RMshow_word_resp.keys = None
            _loop_words.addData('RMshow_word_resp.keys',RMshow_word_resp.keys)
            if RMshow_word_resp.keys != None:  # we had a response
                _loop_words.addData('RMshow_word_resp.rt', RMshow_word_resp.rt)
            _loop_words.addData('RMshow_word_resp.started', RMshow_word_resp.tStartRefresh)
            _loop_words.addData('RMshow_word_resp.stopped', RMshow_word_resp.tStopRefresh)
            # the Routine "RMshow_word" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()

            # ------Prepare to start Routine "_see_word"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            _see_wordComponents = []
            for thisComponent in _see_wordComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            _see_wordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True

            # -------Run Routine "_see_word"-------
            while continueRoutine:
                # get current time
                t = _see_wordClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=_see_wordClock)
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
                for thisComponent in _see_wordComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "_see_word"-------
            for thisComponent in _see_wordComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "_see_word" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()

        # completed 1 repeats of '_loop_words'

        thisExp.nextEntry()

    # completed 1 repeats of '_loop_lists'

    thisExp.nextEntry()

# completed 1 repeats of '_loop_noises'


# ------Prepare to start Routine "_bye"-------
# update component parameters for each repeat
_bye_keyboard.keys = []
_bye_keyboard.rt = []
# keep track of which components have finished
_byeComponents = [_bye_text, _bye_keyboard]
for thisComponent in _byeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
_byeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "_bye"-------
while continueRoutine:
    # get current time
    t = _byeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=_byeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *_bye_text* updates
    if _bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        _bye_text.frameNStart = frameN  # exact frame index
        _bye_text.tStart = t  # local t and not account for scr refresh
        _bye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(_bye_text, 'tStartRefresh')  # time at next scr refresh
        _bye_text.setAutoDraw(True)
    if _bye_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > _bye_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            _bye_text.tStop = t  # not accounting for scr refresh
            _bye_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(_bye_text, 'tStopRefresh')  # time at next scr refresh
            _bye_text.setAutoDraw(False)

    # *_bye_keyboard* updates
    waitOnFlip = False
    if _bye_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        _bye_keyboard.frameNStart = frameN  # exact frame index
        _bye_keyboard.tStart = t  # local t and not account for scr refresh
        _bye_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(_bye_keyboard, 'tStartRefresh')  # time at next scr refresh
        _bye_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(_bye_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(_bye_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if _bye_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = _bye_keyboard.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            _bye_keyboard.keys = theseKeys.name  # just the last key pressed
            _bye_keyboard.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in _byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "_bye"-------
for thisComponent in _byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('_bye_text.started', _bye_text.tStartRefresh)
thisExp.addData('_bye_text.stopped', _bye_text.tStopRefresh)
# check responses
if _bye_keyboard.keys in ['', [], None]:  # No response was made
    _bye_keyboard.keys = None
thisExp.addData('_bye_keyboard.keys',_bye_keyboard.keys)
if _bye_keyboard.keys != None:  # we had a response
    thisExp.addData('_bye_keyboard.rt', _bye_keyboard.rt)
thisExp.addData('_bye_keyboard.started', _bye_keyboard.tStartRefresh)
thisExp.addData('_bye_keyboard.stopped', _bye_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "_bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()  # write messages out to all targets
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
