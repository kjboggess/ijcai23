# Adapted from:
#Author: Thomas Wagenaar (t.wagenaar@student.tue.nl)
#
# Implementation of the algorithms desribed in the paper "Improving Robot
# Controller Transparency Through Autonomous Policy Explanation" by B. Hayes and
# J.A. Shah.
#Original Code Location: https://gitlab.tue.nl/ha800-hri/hayes-shah
#
# Algorithm 1: getLanguage()

from quine_mccluskey.qm import QuineMcCluskey
import json
import random

class Explainer():
    def __init__(self, states, actions, predicates):
        self.states = states;
        self.actions = actions;
        self.predicates = predicates;

        self.numStates = len(states);

    # Algorithm 1: Convert State Region to Language
    def getLanguage(self, targetStates, convertedQuery,failedTask,timeStep,numberOfAgents):
        """Describes the difference between the target and non-target states"""
        #self._validateInput(targetStates, nonTargetStates)

        # Find the minterms
        minterms = self._getMinTerms(targetStates);

        bestMinterm = {}
        for i in minterms:
            score = 0
            for j in range(len(i)):
                if i[j] == convertedQuery[j]:
                    score += 1
            bestMinterm[i] = score

        find_max = max(bestMinterm.values())
        bestMinterm_list = []
        for i in bestMinterm.keys():
            if bestMinterm[i] == find_max:
                bestMinterm_list.append(i)

        #mintermChoice = random.choice(bestMinterm_list) #Random
        mintermChoice = bestMinterm_list[0] #Selected Same Each Time

        # Find the clauses
        clauses = self._findClauses(minterms,mintermChoice,failedTask,timeStep,numberOfAgents,convertedQuery);

        return(clauses,mintermChoice)
        #return ' or '.join(clauses)


    def _validateInput(self, targetStates, nonTargetStates):
        """Checks if target and non-target state set are mutually exclusive"""
        hashedTargetStates = [];
        hashedNonTargetStates = [];

        # Since the states can be nested dictionaries, we hash each of the
        # states by converting them to JSONs. Note: this is inefficient. Better
        # would be to associate an id per state.
        for state in targetStates:
            hashedTargetStates.append(json.dumps(state))

        for state in nonTargetStates:
            hashedNonTargetStates.append(json.dumps(state))

        # Assert targetStates intersection nonTargetStates is null
        intersection = list(set(hashedTargetStates).intersection(hashedNonTargetStates))
        if intersection != []:
            raise Exception('There must be no intersection between targetStates and nonTargetStates');

    def _findValidPredicatesInSet(self, stateSet):
        """String encodes the states based on boolean predicates"""
        targetList = []
        for s in stateSet:
            state_val = '';
            for c in self.predicates:
                state_val += str(int(c['verify'](s)))

            targetList.append(state_val)
        return targetList

    def _generateBitStrings(self, n):
        """Generates all possible n-bit strings, e.g. if n=2: 00,01,10,11"""
        return [bin(x)[2:].rjust(n, '0') for x in range(2**n)];

    def _getMinTerms(self, targetStates):
        """Applies the Quine-McCluskey algorithm to get the minterms"""
        ones = self._findValidPredicatesInSet(targetStates)

        n_bits = len(ones[0])
        all_states = self._generateBitStrings(n_bits)
        zeros = list(set(all_states) - set(ones))
        ones.sort()
        zeros.sort()
        dont_care = []

        #print("These are ones", ones)
        #print("These are zeros", zeros)
        #print("THESE ARE DONT CARES",dont_care)

        qm = QuineMcCluskey();
        minterms = list(qm.simplify_los(ones, dont_care))
        overLap = True
        while overLap:
            overLap = False
            for i in minterms:
                indexes = [j for j, ltr in enumerate(i) if ltr == "-"]
                for k in dont_care:
                    newK = k
                    for l in indexes:
                        newK = newK[:l] + "-" + newK[l + 1:]
                    if newK == i:
                        overLap = True
                        dont_care.remove(k)
            if overLap:
                qm = QuineMcCluskey();
                minterms = list(qm.simplify_los(ones, dont_care))

        #print("THESE ARE THE MINTERMS",minterms)

        return minterms

    def _findClauses (self,minterms,bestMinterm,failedTask,timeStep,numberOfAgents,convertedQuery):
        """Converts the minterms to real clauses based on the given predicates"""

        task = failedTask
        time_step = str(timeStep)
        neededClauses = "Needed Changes: "

        for i in range(len(bestMinterm)):
            predicate = self.predicates[i];
            if convertedQuery[i] == '0' and bestMinterm[i] == '1':
                neededClauses = neededClauses + predicate['true'] + " "
            elif convertedQuery[i] == '1' and bestMinterm[i] == '0':
                neededClauses = neededClauses + predicate['false'] + " "

        return neededClauses
