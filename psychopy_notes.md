# psycopy-qna

[toc]

## PsychoPy tutorials with highlights

- [Logging data (Highlighted)](http://marker.to/jwOZbQ)
- [Logging data](https://www.psychopy.org/coder/codeLogging.html)

## Python

### Python: iterables, iterators, generators

https://www.youtube.com/watch?v=jTYiNjvnHZY

- iterable: can be looped over
- How can we tell if something is iterable?
    - Whether the object has the dunder iter method
- dunder iter (iterable) -> iterator
- How can we tell if something is an iterator?
    - Whether the object has the dunder next method and dunder iter method (just returns self)
    - An interator is an object with a state such that it remembers where it is during iteration.
- Example: simulate looping through a list

```python
nums = [1, 2, 3]

i_nums = iter(nums)

while True:
	try:
		item = next(i_nums)
		print(item)
  except StopIteration:
  	break
```

- Example: range

```python
class MyRange:
  # both:
  # - iterable: can be used in a for loop
  # - iterator: has __next__ method
  
  def __init__(self, start, end):
    self.value = start
    self.end = end
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.value >= self.end:
      raise StopIteration
    current = self.value
    self.value += 1
    return current
```

- Example: generator (`__iter__` and `__next__` are auto-generated for convenience and readability)

```python
def my_range(start, end):
	current = start
	while current < end:
		yield current
		current += 1
```

## PsychoPy

### data.ExperimentHandler



### data.TrialHandler(_BaseHandler)

Documentation:

- https://www.psychopy.org/api/data.html#psychopy.data.TrialHandler

Source code:

- https://www.psychopy.org/_modules/psychopy/data/trial.html#TrialHandler

Parameters:

- trialList: a list of ordered dictionaries specifiying variable-value pairs
- nReps: number of repeats (each repeat loops through all the conditions / all rows)
- method:
    - 'random': a shuffle of conditions for each repeat, each condition occur exactly once during a repeat

    - ’sequential’: needless to say
    - ‘fullRandom’: needless to say
- dataTypes
- extraInfo:
    - type: dictionary
    - metadata about the experiment and the participant
- seed
- originPath: 
    - type: string
    - a string describing the location of the script / experiment file path
    - If `OriginPath==-1` then nothing will be stored.

Attributes::

Methods:

- _makeIndices

```python
def _makeIndices(self, inputArray):
    """
    Creates an array of tuples the same shape as the input array
    where each tuple contains the indices to itself in the array.

    Useful for shuffling and then using as a reference.
    """
    # make sure its an array of objects (can be strings etc)
    inputArray = np.asarray(inputArray, 'O')
    
    # get some simple variables for later
    dims = inputArray.shape  # shape of inputArray
    dimsProd = np.product(dims)  # number of items
    dimsN = len(dims)  # number of axes / dimensions
    dimsList = list(range(dimsN))  # [0, 1, ..., dimsN - 1]
    
    # this creates space for an array of any objects
    arrayOfTuples = np.ones(dimsProd, 'O')

    # for each dimension create list of its indices (using modulo)
    listOfLists = []
    for thisDim in dimsList:  
        prevDimsProd = np.product(dims[:thisDim])  # ??
        thisDimVals = np.arange(dimsProd) / prevDimsProd % dims[thisDim]
        listOfLists.append(thisDimVals)

    # convert to array
    indexArr = np.asarray(listOfLists)
    for n in range(dimsProd):
        arrayOfTuples[n] = tuple((indexArr[:, n]))
    return (np.reshape(arrayOfTuples, dims)).tolist()
```

- _createSequenc

```python
def _createSequence(self):
    """Pre-generates the sequence of trial presentations
    (for non-adaptive methods). This is called automatically when
    the TrialHandler is initialised so doesn't need an explicit call
    from the user.

    The returned sequence has form indices[stimN][repN]
    Example: sequential with 6 trialtypes (rows), 5 reps (cols), returns:
        [[0 0 0 0 0]
         [1 1 1 1 1]
         [2 2 2 2 2]
         [3 3 3 3 3]
         [4 4 4 4 4]
         [5 5 5 5 5]]
    These 30 trials will be returned by .next() in the order:
        0, 1, 2, 3, 4, 5,   0, 1, 2, ...  ... 3, 4, 5

    To add a new type of sequence (as of v1.65.02):
    - add the sequence generation code here
    - adjust "if self.method in [ ...]:" in both __init__ and .next()
    - adjust allowedVals in experiment.py -> shows up in DlgLoopProperties
    Note that users can make any sequence whatsoever outside of PsychoPy,
    and specify sequential order; any order is possible this way.
    """
    # create indices for a single rep
    indices = np.asarray(self._makeIndices(self.trialList), dtype=int)

    if self.method == 'random':
        sequenceIndices = []
        seed = self.seed
        for thisRep in range(self.nReps):
            thisRepSeq = shuffleArray(indices.flat, seed=seed).tolist()
            seed = None  # so that we only seed the first pass through!
            sequenceIndices.append(thisRepSeq)
        sequenceIndices = np.transpose(sequenceIndices)
    elif self.method == 'sequential':
        sequenceIndices = np.repeat(indices, self.nReps, 1)
    elif self.method == 'fullRandom':
        # indices*nReps, flatten, shuffle, unflatten; only use seed once
        sequential = np.repeat(indices, self.nReps, 1)  # = sequential
        randomFlat = shuffleArray(sequential.flat, seed=self.seed)
        sequenceIndices = np.reshape(
            randomFlat, (len(indices), self.nReps))
    if self.autoLog:
        msg = 'Created sequence: %s, trialTypes=%d, nReps=%i, seed=%s'
        vals = (self.method, len(indices), self.nReps, str(self.seed))
        logging.exp(msg % vals)
    return sequenceIndices
```

- next

```python
def __next__(self):
    """Advances to next trial and returns it.
    Updates attributes; thisTrial, thisTrialN and thisIndex
    If the trials have ended this method will raise a StopIteration error.
    This can be handled with code such as::

        trials = data.TrialHandler(.......)
        for eachTrial in trials:  # automatically stops when done
            # do stuff

    or::

        trials = data.TrialHandler(.......)
        while True:  # ie forever
            try:
                thisTrial = trials.next()
            except StopIteration:  # we got a StopIteration error
                break #break out of the forever loop
            # do stuff here for the trial
    """
    # update pointer for next trials
    self.thisTrialN += 1  # number of trial this pass
    self.thisN += 1  # number of trial in total
    self.nRemaining -= 1
    if self.thisTrialN == len(self.trialList):
        # start a new repetition
        self.thisTrialN = 0
        self.thisRepN += 1
    if self.thisRepN >= self.nReps:
        # all reps complete
        self.thisTrial = []
        self.finished = True

    if self.finished == True:
        self._terminate()

    # fetch the trial info
    if self.method in ('random', 'sequential', 'fullRandom'):
        self.thisIndex = self.sequenceIndices[
            self.thisTrialN][self.thisRepN]
        self.thisTrial = self.trialList[self.thisIndex]
        self.data.add('ran', 1)
        self.data.add('order', self.thisN)
    if self.autoLog:
        msg = 'New trial (rep=%i, index=%i): %s'
        vals = (self.thisRepN, self.thisTrialN, self.thisTrial)
        logging.exp(msg % vals, obj=self.thisTrial)
    return self.thisTrial
```

### data.importConditions('csvs/noise_conditions.csv')

- Documentation:

    - https://www.psychopy.org/api/data.html#psychopy.data.importConditions
    
- Returns: 

    - ```python
        [
        	OrderedDict([('condition', 'condition_1')]), 
        	OrderedDict([('condition', 'condition_2')]), 
        	OrderedDict([('condition', 'condition_3')]), 
        	OrderedDict([('condition', 'condition_4')])
        ]
        ```

    - An OrderedDict is a **dictionary** subclass that remembers the order that keys were first inserted.