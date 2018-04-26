import numpy as np

#for part 1
all_cause_mortality=18/1000
stroke_mortality=36.2/100000
non_stroke_mortality=all_cause_mortality - stroke_mortality
strokedeath_rate=-np.log(1 - stroke_mortality)
nonstrokedeath_rate=-np.log(1-non_stroke_mortality)
print("part 1")
print("the annual rate of stroke-related death", strokedeath_rate)
print("the annual rate of non-stroke-related death mortality events", nonstrokedeath_rate)

#for part2
first_stroke=15/1000
firststroke_rate= - np.log(1-first_stroke)
print("part 2")
print("the annual rate of stroke events for our population",firststroke_rate)

#for part3
lambda1=firststroke_rate*0.9
lambda2=firststroke_rate*0.1
print("part 3")
print("the annual rate of transition from state “Well” to “Stroke", lambda1)
print("the annual rate of transition from state “Well” to “Stroke to death",lambda2)

#for part4
recurrent_rate = np.log(1-0.17)*(-1/5)
print("part 4")
print("the annual rate of recurrent stroke events", recurrent_rate)

#part5
post_stroke_rate=recurrent_rate*0.8
post_strokedeath_rate=recurrent_rate*0.2
print("part 5")
print("the annual transition rates from state “Post-Stroke” to “Stroke", post_stroke_rate)
print("the annual transition rates from state “Post-Stroke” to “Stroke Death",post_strokedeath_rate)

#For part6
stroketime=7/365
stroke_post_rate=1/stroketime
print("part 6")
print("the annual rate of transition from “Stroke” to “Post-Stroke", stroke_post_rate)