/***************** 
 * Avspeech Test *
 *****************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'AVSpeech';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(initRoutineBegin());
flowScheduler.add(initRoutineEachFrame());
flowScheduler.add(initRoutineEnd());
flowScheduler.add(practicePromptRoutineBegin());
flowScheduler.add(practicePromptRoutineEachFrame());
flowScheduler.add(practicePromptRoutineEnd());
flowScheduler.add(practiceInstructionRoutineBegin());
flowScheduler.add(practiceInstructionRoutineEachFrame());
flowScheduler.add(practiceInstructionRoutineEnd());
const practiceLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopLoopBegin, practiceLoopLoopScheduler);
flowScheduler.add(practiceLoopLoopScheduler);
flowScheduler.add(practiceLoopLoopEnd);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const stimTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(stimTrialsLoopBegin, stimTrialsLoopScheduler);
flowScheduler.add(stimTrialsLoopScheduler);
flowScheduler.add(stimTrialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "init"
  initClock = new util.Clock();
  function range(start, stop, step) {
      // from https://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range
      if (typeof stop == 'undefined') {
          // one param defined
          stop = start;
          start = 0;
      }
  
      if (typeof step == 'undefined') {
          step = 1;
      }
  
      if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
          return [];
      }
  
      var result = [];
      for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
          result.push(i);
      }
  
      return result;
  };
  
  // From https://javascript.info/task/shuffle
  /*
  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      let j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
  */
  
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  Array.prototype.append = [].push;
  
  random = Math.random;
  
  shuffle = util.shuffle;
  
  document.body.style.cursor='none';
  win=psychoJS.window;
  win.mouseVisible = false;
  
  var p, t;
  num_practice = 8;
  num_stim = 40;
  num_trials = 120;
  trials_to_run = 120;
  stim = {};
  stim["AudNames"] = ["bag", "base", "beard", "bible", "bid", "fad", "fat", "fill", "fine", "fist", "bank", "beer", "bias", "bill", "bye", "fast", "file", "fish", "fit", "five", "gag", "gas", "guild", "guile", "gig", "dad", "dash", "dill", "dine", "disk", "gang", "gear", "guise", "gill", "guy", "dance", "dial", "dish", "digs", "dive"];
  stim["Answers"] = [["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["B", "G", "D", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["F", "D", "T", "TH"], ["F", "D", "G", "TH"], ["F", "D", "T", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "TH"], ["G", "B", "D", "T"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"], ["D", "F", "T", "TH"]];
  stim["AudOnsets"] = [0.5397, 0.5204, 0.5329, 0.531, 0.5417, 0.5428, 0.5478, 0.5244, 0.5294, 0.5384, 0.5306, 0.5331, 0.5316, 0.5228, 0.5087, 0.5257, 0.5201, 0.5492, 0.5201, 0.5355, 0.5407, 0.5458, 0.5314, 0.5275, 0.5457, 0.5456, 0.5177, 0.5355, 0.5337, 0.5319, 0.5211, 0.526, 0.5196, 0.5337, 0.5308, 0.5395, 0.5391, 0.5029, 0.5185, 0.53];
  stim["FrameAdj"] = [0, 1, 0, 0, 0, (- 2), (- 1), 1, (- 2), (- 2), 0, 1, 0, 1, (- 2), 0, (- 2), 0, (- 2), (- 2), 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, (- 2), 1, 0, 0, 0, 0, (- 3), 1, 1];
  
  balancer = random();
  incongV_list = range(20, 40);
  incongV_list = incongV_list.concat(range(0, 20));
  if (balancer < 0.5) {
      aud_list_orig = range(0, 40);
      incongV_list_orig = incongV_list;
  } else {
      aud_list_orig = range(10,20);
      aud_list_orig = aud_list_orig.concat(range(0,10));
      aud_list_orig = aud_list_orig.concat(range(30,40));
      aud_list_orig = aud_list_orig.concat(range(20,30));
      incongV_list_orig = incongV_list.slice(10,20);
      incongV_list_orig = incongV_list_orig.concat(incongV_list.slice(0,10));
      incongV_list_orig = incongV_list_orig.concat(incongV_list.slice(30,40));
      incongV_list_orig = incongV_list_orig.concat(incongV_list.slice(20,30));
  }
  //console.log(balancer);
  //console.log(aud_list_orig);
  
  practice = [];
  practiceVisList = [(- 1), 34, 33, (- 1), 15, 5, (- 1), (- 1)];
  practiceAudList = [10, 34, 13, 25, 35, 5, 2, 39];
  practiceCondList = [2, 8, 10, 3, 12, 5, 1, 4];
  corrAnsList = ['s','k','l','s','s','d','s','s']; 
  corrAnsIdx = [0, 2, 3, 0, 0, 1, 0, 0];
  for (var pIdx = 0, _pj_a = num_practice; (pIdx < _pj_a); pIdx += 1) {
      p = {"AudList": practiceAudList[pIdx], "VisList": practiceVisList[pIdx], "CorrAns": corrAnsList[pIdx], "CorrAnsIdx": corrAnsIdx[pIdx], "Condition": practiceCondList[pIdx]};
      practice.push(p);
  }
  pract_idx = 0;
  stim_idx = 0;
  trialList = [];
  trialsAudList = aud_list_orig.concat(aud_list_orig).concat(aud_list_orig);
  trialsVisList = function () {
      var _pj_a = [], _pj_b = range(0, 40);
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var x = _pj_b[_pj_c];
          _pj_a.push((- 1));
      }
      return _pj_a;
  }.call(this);
  trialsVisList = trialsVisList.concat(aud_list_orig).concat(incongV_list_orig);
  trialsConditionList = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12];
  for (var tIdx = 0, _pj_a = num_trials; (tIdx < _pj_a); tIdx += 1) {
      t = {"AudList": trialsAudList[tIdx], "VisList": trialsVisList[tIdx], "Condition": trialsConditionList[tIdx]};
      trialList.push(t);
  }
  shuffle(trialList);
  
  console.log(stim.length);
  console.log(practice.length);
  
  // When they miss a trial, increase response time
  // by .25 sec up to max 2 sec.
  
  non_missed_trials = 0;
  rt = 1.25;
  // Initialize components for Routine "practicePrompt"
  practicePromptClock = new util.Clock();
  blackScreen = new visual.Rect ({
    win: psychoJS.window, name: 'blackScreen', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  doPracticePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'doPracticePrompt',
    text: "Do you want to do the practice tasks?\n\nSelect 'y' for YES or 'n' for NO to skip the practice.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  doPracticeResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceInstruction"
  practiceInstructionClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  practInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'practInstr',
    text: 'First, we will go through 8 practice trials.\n\nIn this activity, you will hear a word on each trial, followed by 4 response choices. \nPress the button for the first letter/sound of the word you heard (e.g. "g" or "th").\nThe \'1\' key corresponds to the first option shown, the \'2\' key to the second, \'9\' to the third, and \'0\' to the final option.\n\nSome trials will be harder to hear than others, and some of the words may be fake words. If you are ever unsure, please give it your best guess.\n\nPress any button to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  practInstResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "BlankScreen"
  BlankScreenClock = new util.Clock();
  BlackBlank = new visual.Rect ({
    win: psychoJS.window, name: 'BlackBlank', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "practiceDisplay"
  practiceDisplayClock = new util.Clock();
  sound_stim_pract = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_stim_pract.setVolume(1);
  noise_pract = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  noise_pract.setVolume(1);
  // Initialize components for Routine "practiceResponse"
  practiceResponseClock = new util.Clock();
  blackRectP = new visual.Rect ({
    win: psychoJS.window, name: 'blackRectP', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  PracticeRespOptions = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeRespOptions',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PracticeResponse = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceCorrectFeedback"
  practiceCorrectFeedbackClock = new util.Clock();
  blackRectCorr = new visual.Rect ({
    win: psychoJS.window, name: 'blackRectCorr', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  practiceCorr = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceCorr',
    text: 'Correct!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practiceIncorrectFeedback"
  practiceIncorrectFeedbackClock = new util.Clock();
  blackRectIncorr = new visual.Rect ({
    win: psychoJS.window, name: 'blackRectIncorr', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text_incorrect = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_incorrect',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practiceNoAnsFeedback"
  practiceNoAnsFeedbackClock = new util.Clock();
  rectNoAns = new visual.Rect ({
    win: psychoJS.window, name: 'rectNoAns', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  practNoAnsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'practNoAnsText',
    text: ('No key was pressed. \n\n The correct answer was: \n' + stim['Answers'][practice[pract_idx]['AudList']][practice[pract_idx]['CorrAnsIdx']]),
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "increment_pract_idx"
  increment_pract_idxClock = new util.Clock();
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  blackScreen2 = new visual.Rect ({
    win: psychoJS.window, name: 'blackScreen2', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In this activity, you will hear a word being spoken on each trial, followed by 4 response choices. \nPress the button for the first letter/sound of the word you heard (e.g. "g" or "th").\nThe \'1\' key corresponds to the first option shown, the \'2\' key to the second, \'9\' to the third, and \'0\' to the final option.\n\nSome trials will be harder to hear than others, and some of the words may be fake words. Please try your best to choose whichever letter was most similar to what you heard. \nIf you are ever unsure, please give it your best guess.\n\nThis task will take 5 minutes. \n\nPress any button to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stimDisplay"
  stimDisplayClock = new util.Clock();
  sound_stim = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_stim.setVolume(1);
  noise_stim = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  noise_stim.setVolume(1);
  // Initialize components for Routine "stimResponse"
  stimResponseClock = new util.Clock();
  BlackRectStim = new visual.Rect ({
    win: psychoJS.window, name: 'BlackRectStim', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  StimRespOpts = new visual.TextStim({
    win: psychoJS.window,
    name: 'StimRespOpts',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  StimResponseKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rt_adjust"
  rt_adjustClock = new util.Clock();
  // Initialize components for Routine "Inc_stim_idx"
  Inc_stim_idxClock = new util.Clock();
  // Initialize components for Routine "BlankScreen"
  BlankScreenClock = new util.Clock();
  BlackBlank = new visual.Rect ({
    win: psychoJS.window, name: 'BlackBlank', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function initRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'init'-------
    t = 0;
    initClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    initComponents = [];
    
    for (const thisComponent of initComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function initRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'init'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = initClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of initComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function initRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'init'-------
    for (const thisComponent of initComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practicePromptRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practicePrompt'-------
    t = 0;
    practicePromptClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    doPracticeResp.keys = undefined;
    doPracticeResp.rt = undefined;
    _doPracticeResp_allKeys = [];
    // keep track of which components have finished
    practicePromptComponents = [];
    practicePromptComponents.push(blackScreen);
    practicePromptComponents.push(doPracticePrompt);
    practicePromptComponents.push(doPracticeResp);
    
    for (const thisComponent of practicePromptComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practicePromptRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practicePrompt'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practicePromptClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackScreen* updates
    if (t >= 0.0 && blackScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackScreen.tStart = t;  // (not accounting for frame time here)
      blackScreen.frameNStart = frameN;  // exact frame index
      
      blackScreen.setAutoDraw(true);
    }

    
    // *doPracticePrompt* updates
    if (t >= 0.0 && doPracticePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      doPracticePrompt.tStart = t;  // (not accounting for frame time here)
      doPracticePrompt.frameNStart = frameN;  // exact frame index
      
      doPracticePrompt.setAutoDraw(true);
    }

    
    // *doPracticeResp* updates
    if (t >= 0.5 && doPracticeResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      doPracticeResp.tStart = t;  // (not accounting for frame time here)
      doPracticeResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      doPracticeResp.clock.reset();
      doPracticeResp.start();
    }

    if (doPracticeResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = doPracticeResp.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _doPracticeResp_allKeys = _doPracticeResp_allKeys.concat(theseKeys);
      if (_doPracticeResp_allKeys.length > 0) {
        doPracticeResp.keys = _doPracticeResp_allKeys[_doPracticeResp_allKeys.length - 1].name;  // just the last key pressed
        doPracticeResp.rt = _doPracticeResp_allKeys[_doPracticeResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practicePromptComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practicePromptRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practicePrompt'-------
    for (const thisComponent of practicePromptComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('doPracticeResp.keys', doPracticeResp.keys);
    if (typeof doPracticeResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('doPracticeResp.rt', doPracticeResp.rt);
        routineTimer.reset();
        }
    
    doPracticeResp.stop();
    if ((doPracticeResp.keys === "y")) {
        doPractice = 1;
    } else {
        doPractice = 0;
    }
    
    // the Routine "practicePrompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceInstructionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceInstruction'-------
    t = 0;
    practiceInstructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    practInstResp.keys = undefined;
    practInstResp.rt = undefined;
    _practInstResp_allKeys = [];
    import {u3} from 'psychopy/hardware/labjacks';
    import * as time from 'time';
    var d;
    d = new u3.U3();
    for (var i = 0, _pj_a = 5; (i < _pj_a); i += 1) {
        d.setFIOState(7, 1);
        d.setFIOState(7, 0);
        time.sleep(0.1);
    }
    
    // keep track of which components have finished
    practiceInstructionComponents = [];
    practiceInstructionComponents.push(polygon);
    practiceInstructionComponents.push(practInstr);
    practiceInstructionComponents.push(practInstResp);
    
    for (const thisComponent of practiceInstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceInstructionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceInstruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceInstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    
    // *practInstr* updates
    if (t >= 0.0 && practInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practInstr.tStart = t;  // (not accounting for frame time here)
      practInstr.frameNStart = frameN;  // exact frame index
      
      practInstr.setAutoDraw(true);
    }

    
    // *practInstResp* updates
    if (t >= 0.0 && practInstResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practInstResp.tStart = t;  // (not accounting for frame time here)
      practInstResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practInstResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practInstResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practInstResp.clearEvents(); });
    }

    if (practInstResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = practInstResp.getKeys({keyList: [], waitRelease: false});
      _practInstResp_allKeys = _practInstResp_allKeys.concat(theseKeys);
      if (_practInstResp_allKeys.length > 0) {
        practInstResp.keys = _practInstResp_allKeys[_practInstResp_allKeys.length - 1].name;  // just the last key pressed
        practInstResp.rt = _practInstResp_allKeys[_practInstResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceInstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceInstructionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceInstruction'-------
    for (const thisComponent of practiceInstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practInstResp.keys', practInstResp.keys);
    if (typeof practInstResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practInstResp.rt', practInstResp.rt);
        routineTimer.reset();
        }
    
    practInstResp.stop();
    // the Routine "practiceInstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practiceLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: doPractice, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practiceLoop'
  });
  psychoJS.experiment.addLoop(practiceLoop); // add the loop to the experiment
  currentLoop = practiceLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeLoop of practiceLoop) {
    const snapshot = practiceLoop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(practiceTrialsLoopBegin, practiceTrialsLoopScheduler);
    thisScheduler.add(practiceTrialsLoopScheduler);
    thisScheduler.add(practiceTrialsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practiceTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practiceTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: num_practice, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practiceTrials'
  });
  psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
  currentLoop = practiceTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeTrial of practiceTrials) {
    const snapshot = practiceTrials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(BlankScreenRoutineBegin(snapshot));
    thisScheduler.add(BlankScreenRoutineEachFrame(snapshot));
    thisScheduler.add(BlankScreenRoutineEnd(snapshot));
    thisScheduler.add(practiceDisplayRoutineBegin(snapshot));
    thisScheduler.add(practiceDisplayRoutineEachFrame(snapshot));
    thisScheduler.add(practiceDisplayRoutineEnd(snapshot));
    thisScheduler.add(practiceResponseRoutineBegin(snapshot));
    thisScheduler.add(practiceResponseRoutineEachFrame(snapshot));
    thisScheduler.add(practiceResponseRoutineEnd(snapshot));
    const practCorrectLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(practCorrectLoopBegin, practCorrectLoopScheduler);
    thisScheduler.add(practCorrectLoopScheduler);
    thisScheduler.add(practCorrectLoopEnd);
    const practIncorrectLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(practIncorrectLoopBegin, practIncorrectLoopScheduler);
    thisScheduler.add(practIncorrectLoopScheduler);
    thisScheduler.add(practIncorrectLoopEnd);
    const practNoAnsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(practNoAnsLoopBegin, practNoAnsLoopScheduler);
    thisScheduler.add(practNoAnsLoopScheduler);
    thisScheduler.add(practNoAnsLoopEnd);
    thisScheduler.add(increment_pract_idxRoutineBegin(snapshot));
    thisScheduler.add(increment_pract_idxRoutineEachFrame(snapshot));
    thisScheduler.add(increment_pract_idxRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practCorrectLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practCorrect = new TrialHandler({
    psychoJS: psychoJS,
    nReps: PracticeResponse.corr, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practCorrect'
  });
  psychoJS.experiment.addLoop(practCorrect); // add the loop to the experiment
  currentLoop = practCorrect;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractCorrect of practCorrect) {
    const snapshot = practCorrect.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practiceCorrectFeedbackRoutineBegin(snapshot));
    thisScheduler.add(practiceCorrectFeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(practiceCorrectFeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practCorrectLoopEnd() {
  psychoJS.experiment.removeLoop(practCorrect);

  return Scheduler.Event.NEXT;
}

function practIncorrectLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practIncorrect = new TrialHandler({
    psychoJS: psychoJS,
    nReps: showIncorrectFeedback, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practIncorrect'
  });
  psychoJS.experiment.addLoop(practIncorrect); // add the loop to the experiment
  currentLoop = practIncorrect;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractIncorrect of practIncorrect) {
    const snapshot = practIncorrect.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practiceIncorrectFeedbackRoutineBegin(snapshot));
    thisScheduler.add(practiceIncorrectFeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(practiceIncorrectFeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practIncorrectLoopEnd() {
  psychoJS.experiment.removeLoop(practIncorrect);

  return Scheduler.Event.NEXT;
}

function practNoAnsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practNoAns = new TrialHandler({
    psychoJS: psychoJS,
    nReps: showNoAnswer, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practNoAns'
  });
  psychoJS.experiment.addLoop(practNoAns); // add the loop to the experiment
  currentLoop = practNoAns;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractNoAn of practNoAns) {
    const snapshot = practNoAns.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practiceNoAnsFeedbackRoutineBegin(snapshot));
    thisScheduler.add(practiceNoAnsFeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(practiceNoAnsFeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practNoAnsLoopEnd() {
  psychoJS.experiment.removeLoop(practNoAns);

  return Scheduler.Event.NEXT;
}

function practiceTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(practiceTrials);

  return Scheduler.Event.NEXT;
}

function practiceLoopLoopEnd() {
  psychoJS.experiment.removeLoop(practiceLoop);

  return Scheduler.Event.NEXT;
}

function stimTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  stimTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trials_to_run, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'stimTrials'
  });
  psychoJS.experiment.addLoop(stimTrials); // add the loop to the experiment
  currentLoop = stimTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisStimTrial of stimTrials) {
    const snapshot = stimTrials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(stimDisplayRoutineBegin(snapshot));
    thisScheduler.add(stimDisplayRoutineEachFrame(snapshot));
    thisScheduler.add(stimDisplayRoutineEnd(snapshot));
    thisScheduler.add(stimResponseRoutineBegin(snapshot));
    thisScheduler.add(stimResponseRoutineEachFrame(snapshot));
    thisScheduler.add(stimResponseRoutineEnd(snapshot));
    thisScheduler.add(rt_adjustRoutineBegin(snapshot));
    thisScheduler.add(rt_adjustRoutineEachFrame(snapshot));
    thisScheduler.add(rt_adjustRoutineEnd(snapshot));
    thisScheduler.add(Inc_stim_idxRoutineBegin(snapshot));
    thisScheduler.add(Inc_stim_idxRoutineEachFrame(snapshot));
    thisScheduler.add(Inc_stim_idxRoutineEnd(snapshot));
    thisScheduler.add(BlankScreenRoutineBegin(snapshot));
    thisScheduler.add(BlankScreenRoutineEachFrame(snapshot));
    thisScheduler.add(BlankScreenRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function stimTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(stimTrials);

  return Scheduler.Event.NEXT;
}

function BlankScreenRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'BlankScreen'-------
    t = 0;
    BlankScreenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    BlankScreenComponents = [];
    BlankScreenComponents.push(BlackBlank);
    
    for (const thisComponent of BlankScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function BlankScreenRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'BlankScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = BlankScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BlackBlank* updates
    if (t >= 0.0 && BlackBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlackBlank.tStart = t;  // (not accounting for frame time here)
      BlackBlank.frameNStart = frameN;  // exact frame index
      
      BlackBlank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BlackBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BlackBlank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BlankScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function BlankScreenRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'BlankScreen'-------
    for (const thisComponent of BlankScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function practiceDisplayRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceDisplay'-------
    t = 0;
    practiceDisplayClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    var audioFile, audioFileIdx, globalClock, mov, movieFile, nextFlip, soundFile, stimSound, visualFile, visualFileIdx;
    console.log("pract_idx:");
    console.log(pract_idx);
    
    audioFileIdx = Number.parseInt(practice[pract_idx]["AudList"]);
    console.log(audioFileIdx);
    audioFile = stim["AudNames"][audioFileIdx];
    
    // Check if this is a noise condition
    if (practice[pract_idx]['Condition'] % 2 == 1){
        noiseFile = "audio_clipped_mp3/pink_noise.mp3";
    } else {
        noiseFile= "audio_clipped_mp3/no_noise.mp3";
    }
    
    visualFileIdx = Number.parseInt(practice[pract_idx]["VisList"]);
    console.log(visualFileIdx);
    if ((visualFileIdx === (- 1))) {
        visualFile = "degraded";
    } else {
        visualFile = stim["AudNames"][visualFileIdx];
    }
    visualFile = (visualFile + ".mp4");
    audioFile = (audioFile + ".mp3");
    movieFile = (("visual/") + visualFile);
    soundFile = (("audio_clipped_mp3/") + audioFile);
    
    // Correct frame index for offsets
    // (frameN=-1 starts the video at the first frame)
    frameN = stim["FrameAdj"][visualFileIdx] - 1;
    console.log(movieFile);
    console.log(soundFile);
    console.log(noiseFile);
    movie_stim_practClock = new util.Clock();
    movie_stim_pract = new visual.MovieStim({
      win: psychoJS.window,
      name: 'movie_stim_pract',
      units: undefined,
      movie: movieFile,
      pos: [0, 0],
      size: undefined,
      ori: 0,
      opacity: 1,
      loop: false,
      noAudio: true,
      });
    sound_stim_pract = new sound.Sound({
    win: psychoJS.window,
    value: soundFile,
    secs: -1,
    });
    sound_stim_pract.setVolume(1);
    noise_pract = new sound.Sound({
    win: psychoJS.window,
    value: noiseFile,
    secs: -1,
    });
    noise_pract.setVolume(1);
    movie_stim_pract._movie.currentTime = 0
    movie_stim_pract.play();
    // keep track of which components have finished
    practiceDisplayComponents = [];
    practiceDisplayComponents.push(movie_stim_pract);
    practiceDisplayComponents.push(sound_stim_pract);
    practiceDisplayComponents.push(noise_pract);
    
    for (const thisComponent of practiceDisplayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceDisplayRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceDisplay'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceDisplayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    console.log(movie_stim_pract.status);
    
    // *movie_stim_pract* updates
    if (t >= 0.0 && movie_stim_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_stim_pract.tStart = t;  // (not accounting for frame time here)
      movie_stim_pract.frameNStart = frameN;  // exact frame index
      
      movie_stim_pract.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie_stim_pract.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie_stim_pract.setAutoDraw(false);
    }

    if (movie_stim_pract.status === PsychoJS.Status.FINISHED) {  // force-end the routine
        continueRoutine = false;
    }
    // start/stop sound_stim_pract
    if (t >= stim['AudOnsets'][practice[pract_idx]['AudList']] && sound_stim_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_stim_pract.tStart = t;  // (not accounting for frame time here)
      sound_stim_pract.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_stim_pract.play(); });  // screen flip
      sound_stim_pract.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_stim_pract.getDuration() + sound_stim_pract.tStart)     && sound_stim_pract.status === PsychoJS.Status.STARTED) {
      sound_stim_pract.stop();  // stop the sound (if longer than duration)
      sound_stim_pract.status = PsychoJS.Status.FINISHED;
    }
    // start/stop noise_pract
    if (t >= stim['AudOnsets'][practice[pract_idx]['AudList']] && noise_pract.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noise_pract.tStart = t;  // (not accounting for frame time here)
      noise_pract.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ noise_pract.play(); });  // screen flip
      noise_pract.status = PsychoJS.Status.STARTED;
    }
    if (t >= (noise_pract.getDuration() + noise_pract.tStart)     && noise_pract.status === PsychoJS.Status.STARTED) {
      noise_pract.stop();  // stop the sound (if longer than duration)
      noise_pract.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceDisplayComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceDisplayRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceDisplay'-------
    for (const thisComponent of practiceDisplayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    thisExp.addData('audioFileIdx', audioFileIdx)
    thisExp.addData('visualFileIdx', visualFileIdx)
    sound_stim_pract.stop();  // ensure sound has stopped at end of routine
    noise_pract.stop();  // ensure sound has stopped at end of routine
    movie_stim_pract.stop();
    
    // the Routine "practiceDisplay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceResponseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceResponse'-------
    t = 0;
    practiceResponseClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.250000);
    // update component parameters for each repeat
    responseOptions = stim["Answers"][practice[pract_idx]["AudList"]].slice();
    shuffle(responseOptions);
    
    responseOptionText = responseOptions[0] + "\t\t\t" + responseOptions[1] + "\t\t\t" + responseOptions[2] + "\t\t\t" + responseOptions[3];
    
    correctAnswerIdx = practice[pract_idx]["CorrAnsIdx"];
    correctAnsText = stim["Answers"][practice[pract_idx]["AudList"]][correctAnswerIdx];
    
    shuffledCorrIdx = responseOptions.indexOf(correctAnsText);
    
    if ((shuffledCorrIdx === 0)) {
        correctAnswer = "1";
    } else {
        if ((shuffledCorrIdx === 1)) {
            correctAnswer = "2";
        } else {
            if ((shuffledCorrIdx === 2)) {
                correctAnswer = "9";
            } else {
                if ((shuffledCorrIdx === 3)) {
                    correctAnswer = "0";
                }
            }
        }
    }
    
    PracticeRespOptions.setText(responseOptionText);
    PracticeResponse.keys = undefined;
    PracticeResponse.rt = undefined;
    _PracticeResponse_allKeys = [];
    // keep track of which components have finished
    practiceResponseComponents = [];
    practiceResponseComponents.push(blackRectP);
    practiceResponseComponents.push(PracticeRespOptions);
    practiceResponseComponents.push(PracticeResponse);
    
    for (const thisComponent of practiceResponseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceResponseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceResponse'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackRectP* updates
    if (t >= 0.0 && blackRectP.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackRectP.tStart = t;  // (not accounting for frame time here)
      blackRectP.frameNStart = frameN;  // exact frame index
      
      blackRectP.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blackRectP.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blackRectP.setAutoDraw(false);
    }
    
    // *PracticeRespOptions* updates
    if (t >= 0.0 && PracticeRespOptions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeRespOptions.tStart = t;  // (not accounting for frame time here)
      PracticeRespOptions.frameNStart = frameN;  // exact frame index
      
      PracticeRespOptions.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PracticeRespOptions.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PracticeRespOptions.setAutoDraw(false);
    }
    
    // *PracticeResponse* updates
    if (t >= 0.0 && PracticeResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeResponse.tStart = t;  // (not accounting for frame time here)
      PracticeResponse.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeResponse.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeResponse.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PracticeResponse.clearEvents(); });
    }

    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PracticeResponse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PracticeResponse.status = PsychoJS.Status.FINISHED;
  }

    if (PracticeResponse.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeResponse.getKeys({keyList: ['1', '2', '9', '0'], waitRelease: false});
      _PracticeResponse_allKeys = _PracticeResponse_allKeys.concat(theseKeys);
      if (_PracticeResponse_allKeys.length > 0) {
        PracticeResponse.keys = _PracticeResponse_allKeys[0].name;  // just the first key pressed
        PracticeResponse.rt = _PracticeResponse_allKeys[0].rt;
        // was this correct?
        if (PracticeResponse.keys == correctAnswer) {
            PracticeResponse.corr = 1;
        } else {
            PracticeResponse.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceResponseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceResponseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceResponse'-------
    for (const thisComponent of practiceResponseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    responseOptions = ((((((responseOptions[0] + " ") + responseOptions[1]) + " ") + responseOptions[2]) + " ") + responseOptions[3]);
    thisExp.addData("responseOptions", responseOptions);
    thisExp.addData("correctResponse", correctAnswer);
    // was no response the correct answer?!
    if (PracticeResponse.keys === undefined) {
      if (['None','none',undefined].includes(correctAnswer)) {
         PracticeResponse.corr = 1;  // correct non-response
      } else {
         PracticeResponse.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('PracticeResponse.keys', PracticeResponse.keys);
    psychoJS.experiment.addData('PracticeResponse.corr', PracticeResponse.corr);
    if (typeof PracticeResponse.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PracticeResponse.rt', PracticeResponse.rt);
        routineTimer.reset();
        }
    
    PracticeResponse.stop();
    if ((PracticeResponse.keys === undefined)) {
        showIncorrectFeedback = 0;
        showNoAnswer = 1;
    } else {
        showNoAnswer = 0;
        if ((PracticeResponse.corr === 0)) {
            showIncorrectFeedback = 1;
        } else {
            showIncorrectFeedback = 0;
        }
    }
    
    return Scheduler.Event.NEXT;
  };
}

function practiceCorrectFeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceCorrectFeedback'-------
    t = 0;
    practiceCorrectFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    practiceCorrectFeedbackComponents = [];
    practiceCorrectFeedbackComponents.push(blackRectCorr);
    practiceCorrectFeedbackComponents.push(practiceCorr);
    
    for (const thisComponent of practiceCorrectFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceCorrectFeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceCorrectFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceCorrectFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackRectCorr* updates
    if (t >= 0.0 && blackRectCorr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackRectCorr.tStart = t;  // (not accounting for frame time here)
      blackRectCorr.frameNStart = frameN;  // exact frame index
      
      blackRectCorr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blackRectCorr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blackRectCorr.setAutoDraw(false);
    }
    
    // *practiceCorr* updates
    if (t >= 0.0 && practiceCorr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceCorr.tStart = t;  // (not accounting for frame time here)
      practiceCorr.frameNStart = frameN;  // exact frame index
      
      practiceCorr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practiceCorr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practiceCorr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceCorrectFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceCorrectFeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceCorrectFeedback'-------
    for (const thisComponent of practiceCorrectFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function practiceIncorrectFeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceIncorrectFeedback'-------
    t = 0;
    practiceIncorrectFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    text_incorrect.setText(('Incorrect. \n\n The correct answer was: \n' + stim['Answers'][practice[pract_idx]['AudList']][practice[pract_idx]['CorrAnsIdx']]));
    // keep track of which components have finished
    practiceIncorrectFeedbackComponents = [];
    practiceIncorrectFeedbackComponents.push(blackRectIncorr);
    practiceIncorrectFeedbackComponents.push(text_incorrect);
    
    for (const thisComponent of practiceIncorrectFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceIncorrectFeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceIncorrectFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceIncorrectFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackRectIncorr* updates
    if (t >= 0.0 && blackRectIncorr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackRectIncorr.tStart = t;  // (not accounting for frame time here)
      blackRectIncorr.frameNStart = frameN;  // exact frame index
      
      blackRectIncorr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blackRectIncorr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blackRectIncorr.setAutoDraw(false);
    }
    
    // *text_incorrect* updates
    if (t >= 0.0 && text_incorrect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_incorrect.tStart = t;  // (not accounting for frame time here)
      text_incorrect.frameNStart = frameN;  // exact frame index
      
      text_incorrect.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_incorrect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_incorrect.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceIncorrectFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceIncorrectFeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceIncorrectFeedback'-------
    for (const thisComponent of practiceIncorrectFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function practiceNoAnsFeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practiceNoAnsFeedback'-------
    t = 0;
    practiceNoAnsFeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    practiceNoAnsFeedbackComponents = [];
    practiceNoAnsFeedbackComponents.push(rectNoAns);
    practiceNoAnsFeedbackComponents.push(practNoAnsText);
    
    for (const thisComponent of practiceNoAnsFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceNoAnsFeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practiceNoAnsFeedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceNoAnsFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rectNoAns* updates
    if (t >= 0.0 && rectNoAns.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectNoAns.tStart = t;  // (not accounting for frame time here)
      rectNoAns.frameNStart = frameN;  // exact frame index
      
      rectNoAns.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rectNoAns.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rectNoAns.setAutoDraw(false);
    }
    
    // *practNoAnsText* updates
    if (t >= 0.0 && practNoAnsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practNoAnsText.tStart = t;  // (not accounting for frame time here)
      practNoAnsText.frameNStart = frameN;  // exact frame index
      
      practNoAnsText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practNoAnsText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practNoAnsText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceNoAnsFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceNoAnsFeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practiceNoAnsFeedback'-------
    for (const thisComponent of practiceNoAnsFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function increment_pract_idxRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'increment_pract_idx'-------
    t = 0;
    increment_pract_idxClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    increment_pract_idxComponents = [];
    
    for (const thisComponent of increment_pract_idxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function increment_pract_idxRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'increment_pract_idx'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = increment_pract_idxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of increment_pract_idxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function increment_pract_idxRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'increment_pract_idx'-------
    for (const thisComponent of increment_pract_idxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    pract_idx = (pract_idx + 1);
    
    // the Routine "increment_pract_idx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function instructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(blackScreen2);
    instructionsComponents.push(text);
    instructionsComponents.push(key_resp);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function instructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackScreen2* updates
    if (t >= 0.0 && blackScreen2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackScreen2.tStart = t;  // (not accounting for frame time here)
      blackScreen2.frameNStart = frameN;  // exact frame index
      
      blackScreen2.setAutoDraw(true);
    }

    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function stimDisplayRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stimDisplay'-------
    t = 0;
    stimDisplayClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    console.log("stim_idx:");
    console.log(stim_idx);
    audioFileIdx = Number.parseInt(trialList[stim_idx]["AudList"]);
    console.log(audioFileIdx);
    audioFile = stim["AudNames"][audioFileIdx];
    visualFileIdx = Number.parseInt(trialList[stim_idx]["VisList"]);
    console.log(visualFileIdx);
    if ((visualFileIdx === (- 1))) {
        visualFile = "degraded";
    } else {
        visualFile = stim["AudNames"][visualFileIdx];
    }
    
    if (trialList[stim_idx]['Condition']%2 == 1){
        noiseFile = "audio_clipped_mp3/pink_noise.mp3";
    } else {
        noiseFile = "audio_clipped_mp3/no_noise.mp3";
    }
    
    visualFile = (visualFile + ".mp4");
    audioFile = (audioFile + ".mp3");
    movieFile = ("visual/" + visualFile);
    soundFile = ("audio_clipped_mp3/" + audioFile);
    frameN = stim["FrameAdj"][visualFileIdx] - 1;
    
    /*
    stimSound = new sound.Sound(soundFile);
    mov = new visual.MovieStim3(win, movieFile, {"size": [320, 240], "flipVert": false, "flipHoriz": false, "loop": false});
    globalClock = new core.Clock();
    nextFlip = win.getFutureFlipTime({"clock": "ptb"});
    stimSound.play({"when": nextFlip});
    console.log(audioFile);
    console.log(movieFile);
    while ((mov.status !== visual.FINISHED)) {
        mov.draw();
        win.flip();
    }
    */
    psychoJS.experiment.addData("audioFileIdx", audioFileIdx);
    psychoJS.experiment.addData("visualFileIdx", visualFileIdx);
    movie_stimClock = new util.Clock();
    movie_stim = new visual.MovieStim({
      win: psychoJS.window,
      name: 'movie_stim',
      units: undefined,
      movie: movieFile,
      pos: [0, 0],
      size: undefined,
      ori: 0,
      opacity: 1,
      loop: false,
      noAudio: false,
      });
    sound_stim = new sound.Sound({
    win: psychoJS.window,
    value: soundFile,
    secs: -1,
    });
    sound_stim.setVolume(1);
    noise_stim = new sound.Sound({
    win: psychoJS.window,
    value: noiseFile,
    secs: -1,
    });
    noise_stim.setVolume(1);
    movie_stim._movie.currentTime = 0
    movie_stim.play();
    // keep track of which components have finished
    stimDisplayComponents = [];
    stimDisplayComponents.push(movie_stim);
    stimDisplayComponents.push(sound_stim);
    stimDisplayComponents.push(noise_stim);
    
    for (const thisComponent of stimDisplayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function stimDisplayRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stimDisplay'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stimDisplayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie_stim* updates
    if (t >= 0.0 && movie_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_stim.tStart = t;  // (not accounting for frame time here)
      movie_stim.frameNStart = frameN;  // exact frame index
      
      movie_stim.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie_stim.setAutoDraw(false);
    }

    if (movie_stim.status === PsychoJS.Status.FINISHED) {  // force-end the routine
        continueRoutine = false;
    }
    // start/stop sound_stim
    if (t >= stim['AudOnsets'][trialList[stim_idx]['AudList']] && sound_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_stim.tStart = t;  // (not accounting for frame time here)
      sound_stim.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_stim.play(); });  // screen flip
      sound_stim.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_stim.getDuration() + sound_stim.tStart)     && sound_stim.status === PsychoJS.Status.STARTED) {
      sound_stim.stop();  // stop the sound (if longer than duration)
      sound_stim.status = PsychoJS.Status.FINISHED;
    }
    // start/stop noise_stim
    if (t >= stim['AudOnsets'][trialList[stim_idx]['AudList']] && noise_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noise_stim.tStart = t;  // (not accounting for frame time here)
      noise_stim.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ noise_stim.play(); });  // screen flip
      noise_stim.status = PsychoJS.Status.STARTED;
    }
    if (t >= (noise_stim.getDuration() + noise_stim.tStart)     && noise_stim.status === PsychoJS.Status.STARTED) {
      noise_stim.stop();  // stop the sound (if longer than duration)
      noise_stim.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimDisplayComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function stimDisplayRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stimDisplay'-------
    for (const thisComponent of stimDisplayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    thisExp.addData("audioFileIdx", audioFileIdx);
    thisExp.addData("visualFileIdx", visualFileIdx);
    
    sound_stim.stop();  // ensure sound has stopped at end of routine
    noise_stim.stop();  // ensure sound has stopped at end of routine
    movie_stim.stop();
    
    // the Routine "stimDisplay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function stimResponseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stimResponse'-------
    t = 0;
    stimResponseClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    responseOptions = stim["Answers"][trialList[stim_idx]["AudList"]].slice();
    console.log(responseOptions);
    shuffle(responseOptions);
    console.log(responseOptions);
    
    responseOptionText = responseOptions[0] + "\t\t\t" + responseOptions[1] + "\t\t\t" + responseOptions[2] + "\t\t\t" + responseOptions[3];
    
    
    StimRespOpts.setText(responseOptionText);
    StimResponseKey.keys = undefined;
    StimResponseKey.rt = undefined;
    _StimResponseKey_allKeys = [];
    // keep track of which components have finished
    stimResponseComponents = [];
    stimResponseComponents.push(BlackRectStim);
    stimResponseComponents.push(StimRespOpts);
    stimResponseComponents.push(StimResponseKey);
    
    for (const thisComponent of stimResponseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function stimResponseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stimResponse'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stimResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BlackRectStim* updates
    if (t >= 0.0 && BlackRectStim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlackRectStim.tStart = t;  // (not accounting for frame time here)
      BlackRectStim.frameNStart = frameN;  // exact frame index
      
      BlackRectStim.setAutoDraw(true);
    }

    frameRemains = 0.0 + rt - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BlackRectStim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BlackRectStim.setAutoDraw(false);
    }
    
    // *StimRespOpts* updates
    if (t >= 0.0 && StimRespOpts.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StimRespOpts.tStart = t;  // (not accounting for frame time here)
      StimRespOpts.frameNStart = frameN;  // exact frame index
      
      StimRespOpts.setAutoDraw(true);
    }

    frameRemains = 0.0 + rt - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StimRespOpts.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StimRespOpts.setAutoDraw(false);
    }
    
    // *StimResponseKey* updates
    if (t >= 0.0 && StimResponseKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StimResponseKey.tStart = t;  // (not accounting for frame time here)
      StimResponseKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { StimResponseKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { StimResponseKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { StimResponseKey.clearEvents(); });
    }

    frameRemains = 0.0 + rt - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StimResponseKey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StimResponseKey.status = PsychoJS.Status.FINISHED;
  }

    if (StimResponseKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = StimResponseKey.getKeys({keyList: ['1', '2', '9', '0'], waitRelease: false});
      _StimResponseKey_allKeys = _StimResponseKey_allKeys.concat(theseKeys);
      if (_StimResponseKey_allKeys.length > 0) {
        StimResponseKey.keys = _StimResponseKey_allKeys[0].name;  // just the first key pressed
        StimResponseKey.rt = _StimResponseKey_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimResponseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function stimResponseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stimResponse'-------
    for (const thisComponent of stimResponseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    responseOptions = ((((((responseOptions[0] + " ") + responseOptions[1]) + " ") + responseOptions[2]) + " ") + responseOptions[3]);
    thisExp.addData("responseOptions", responseOptions);
    
    psychoJS.experiment.addData('StimResponseKey.keys', StimResponseKey.keys);
    if (typeof StimResponseKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('StimResponseKey.rt', StimResponseKey.rt);
        routineTimer.reset();
        }
    
    StimResponseKey.stop();
    // the Routine "stimResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function rt_adjustRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rt_adjust'-------
    t = 0;
    rt_adjustClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    rt_adjustComponents = [];
    
    for (const thisComponent of rt_adjustComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function rt_adjustRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rt_adjust'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rt_adjustClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of rt_adjustComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function rt_adjustRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rt_adjust'-------
    for (const thisComponent of rt_adjustComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    console.log(StimResponseKey.keys);
    console.log(non_missed_trials);
    console.log(rt);
    if ((StimResponseKey.keys === undefined)) {
        non_missed_trials = 0;
        if ((rt <= 1.75)) {
            rt = (rt + 0.25);
        }
    } else {
        non_missed_trials += 1;
    }
    if (((non_missed_trials >= 10) && (rt >= 1.5))) {
        rt = (rt - 0.25);
    }
    console.log(rt);
    
    // the Routine "rt_adjust" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Inc_stim_idxRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Inc_stim_idx'-------
    t = 0;
    Inc_stim_idxClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    Inc_stim_idxComponents = [];
    
    for (const thisComponent of Inc_stim_idxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function Inc_stim_idxRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Inc_stim_idx'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inc_stim_idxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inc_stim_idxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Inc_stim_idxRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Inc_stim_idx'-------
    for (const thisComponent of Inc_stim_idxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stim_idx = (stim_idx + 1);
    
    // the Routine "Inc_stim_idx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
