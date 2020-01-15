# Rapid Adaptation

[toc]

## Question, Hypothesis, Conclusion

- hypothesis: 

    - > We hypothesized that even when intelligibility is matched, nonnative-accented speech would require greater listening effort relative to native-accented speech as measured by both a dual-task paradigm (Experiment 1) and pupillometry (Experiment 2). 

        - data / visualization may look like:
            - plot listening effort over time
        - what’s done in this paper:
            - plot listening effort over time

    - > we hypothesized that adaptation to nonnative-accented speech would reduce the listening effort required to process that accent to a greater extent than for native-accented speech.

        - data / visualization may look like: 
            - since pupillometry records a series of values over time for each trial and each participant, we can extract the maximum value out from each series and use that to quantify effort
            - <u>(listening effort post-adapation - listening effort pre-adaption) for nonnative > (listening effort post-adapation - listening effort pre-adaption) for native</u>
            - plot listening effort over time
        - what’s done in this paper (figure 4):
            - if you think about it, what we have to visualize is high-dimensional data with 4 dimensions: (1) accent, (2) trial number, (3) pupil diameters, (4) time during each trial
            - have to 2 separate axes for <u>accent</u>
                - have <u>pupil diameters</u> plotted against <u>time during each trial</u>, one plot for each <u>trial</u> bin
                - color-code each line plot
                - line plots gradually get lower and lower
            - a model can be built using all 4 dimensions of data easily so it is quite different from the visualization

## Experiment 1

<img src='https://imgur.com/QwA4JQR.png' width=500>

notes

 - visualization
     - x: trial number
     - y: mean response time to secondary task
 - model:
     - fixed effects: accent and trial number
 - result and conclusion:
     - r: both [accent] and [trial number] is [significant] (by likelihood ratio tests, by comparing with a model lacking one fixed effect)
     - r: [response times to the secondary number task] were on average an estimated 70 ms [slower] [in the nonnative] compared to the [native condition] 
         - technique: first neglect trial number, and take the average of response times for each accent
         - c: native English speakers expended more listening effort when recognizing fully intelligible speech produced by a nonnative Mandarin-accented English speaker relative to a native English speaker **(agree with hypothesis 1)**
     - r: for every trial, response times to the unrelated secondary task decreased by an estimated 1 ms
         - technique: first neglect accent, and take the average of response times for each trial)
         - c: it is unclear whether this effect reflects adaptation or practice effects (practice effects may mask adapation); that is, it may be that there is an interaction between accent and trial number, but the effects happen (and dissipate) so quickly that they are not detectable when examining the full dataset
         - **perform the same analysis but for a subset of data => exploratoy analysis (discussed in the last section)**
     - r: interaction between accent and trial number is not significant (by likelihood ratio test)

## Exploratory analysis
<img src='https://imgur.com/lDUid4z.png' width=500>

notes:
- model comparison:
	- models
		- accent, trial number, accent-and-trial interaction (better fit)
		- accent, trial number
	- result
		- r: accent and trial interaction is significant by likelihood-ratio test
		- r: response time decreased faster for non-native than native (p=0.046)
		    - c: weak evidence (because of the p-value) that participants adapt more quickly to nonnative than native speech in the early stages of exposure
		    - c: require further research due to the lack of data
		- r: conditional R value is 0.59
   - significance
	   - expose problems in the current methodology
	   - lead to thoughts on potential improvements

## Experiment 2

<img src='/Users/yangzhihan/My Files/Typora Pics/image-20200114164649944.png' width=500>

<img src='/Users/yangzhihan/My Files/Typora Pics/image-20200114172616196.png' width=500>

notes:

- model:
    - fixed effects: linear, quadratic, and cubic orthogonalized polynomial time terms, accent, trial number, two-way interactions, three-way interactions
    - random effects: participants, items, interaction between participants and accent
- result and conclusion:
    - r: all time terms are significant
        - c: interaction between accent and linear polynomial time term indicated that the <u>pupil diameter increased more rapidly after sentence onset for nonnative relative to native</u> **(weakly / not related to hypothesis 1)**
        - c: **agree with previous research** (McLaughlin & Van Engen)
    - r: accent term is significant
        - accent term indicated that on average, <u>the pupil diameter was greater for nonnative relative to native </u> **(agree with hypothesis 1)**
    - r: trial number is significant
        - c: the pupil diameter decreased across trials for both accents (likely reflecting adaptation and fatigue over time)
        - c: **agree with previous research** (adapation reduced efforts for both accents, agree with McGarrigle et al., 2016; Winn, Wendt, Koelewijn, & Kuchinsky, 2018)
    - r: interaction between accent and trial number is significant
        - r: marginal R value = 0.05; conditional R value of 0.24
        - c: the pupil diameter decreased more rapidly for the nonnative relative to the native accent across trials **(agree with hypothesis 2)**

## Reflections

- Before reading results, take note of the variables each hypothesis is most interested in.
- Remember that visualizations are often most complicated than they look; if you don’t like a particular visualization, read on the model.
- Is the purpose of mentioning effects / interactions that are not directly targeted to our hypotheses a way to improve the validity of our research?
- What guides your research? Can you list out all the possible interactions in similar experiments and just investigate unresearched interactions? Would that be a good way to start?





