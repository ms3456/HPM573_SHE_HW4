import HW4_Q1 as lol
headProb = 0.4
timeSteps = 20
realizationNumber = 1000

#flip = lol.Game (id =2, head_prob = headProb)
#flip.Simulate(timeSteps)
#flip.get_exp_value(timeSteps)

myCohort = lol.Realization(id = 2, realization_number = realizationNumber, head_prob = headProb)
myCohort.simulate(timeSteps)

print 'Average expected reward (dollors):', myCohort.get_ave_exp_value()

