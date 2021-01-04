# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import networkx for graph tools
import networkx as nx                           

# Import dwave_networkx for d-wave graph tools/functions
import dwave_networkx as dnx                    

# Import matplotlib.pyplot to draw graphs on screen
#import matplotlib
#matplotlib.use("agg")
#import matplotlib.pyplot as plt

# Set the solver we're going to use
from dwave.system.samplers import DWaveSampler        
from dwave.system.composites import EmbeddingComposite 

sampler = EmbeddingComposite(DWaveSampler())        

#Create empty graph
G = nx.Graph()                                       

 #Add edges to graph - this also adds the nodes
G.add_edges_from([(3, 4),(1,2)])                   

#Find the maximum independent set, S
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10)

# Print the solution for the user
#print('Maximum independent set size found is', len(S))
#print(S)

#----------------------------------
#zz =S[0]
#print (zz, "testing")


#if zz ==1:
    #print("HEADS")
#if zz  == 2:
    #print("TAILS")  


#print("  ")


#------------------insert DWAVE above



#   FOR AMUSEMENT ONLY
#   -- just a little python practice
#   P. Gitschner   2020
#
#GAMEPLAY-----------------------------------------
#
# You start with a 1,000 points balance.
# You enter a bet up - to your max
# A random number generator makes a binary decision, win or lose.
# To test:Python       Live: DwaveLeap QUANTUM
# Your balance is adjusted and saved as a new opening balance.
# using pickle. THIS MEANS PERSISTANT MEMORY. 
# If you hit zero, you are reloaded  to 1000
# To Reset an existing starting balance enter 123456
# then bet 0 to be at a fresh start
#
# ToDo: neg bets, empty bets,  str bets, grafic spinner w TK or pygame


# ----------------------------------------

import pickle
import random

#setup only. This plants the p file, then comment out and uncomment 94
#my_balance = 1000
#pickle.dump (my_balance, open ("save.p","wb"))



# Load the balance from the pickle file.
my_balance = pickle.load( open( "save.p", "rb" ) )
aa = my_balance



print("  ")
#print("-- QUANTUM SLOTS 2020 ---Your OPEN Balance is    ",aa)
    
    
#----------------------------------------

bet = input (" How much do you wager ")

if bet == "123456":
    aa = 1000
    
# negative bets work in reverse to win
# enter a string in bet and crashes, but balance still saved
    
if int(bet) >= (aa+1):    
    print('Cannot bet more than you have ')
    print(" Your CURRENT Balance is    ",aa)
    bet = input (" How much do you wager  ")



#------------Python Random Number for testing -----
spinner = (random.randint(0, 1))

print(" You bet ", bet,"   Spinner says ", spinner)
#--------------------------------------------------

if spinner == 1:
    bb = aa + int(bet)
    print ("  *****WINNER*****")
elif spinner == 0:
    bb = aa - int(bet)
    print("    SORRY")
    
#print( bb)

# balance  0
if bb == 0:
    print("You're tapped out. Will reset to 1000. ")
    bb = 1000

my_balance =bb
print(" Your END Balance is ",bb," . Rerun (Leap Green Arrow) to PLAY again")

#final save
pickle.dump( my_balance, open( "save.p", "wb" ) )
