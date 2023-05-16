# Adapted from:
#Author: Thomas Wagenaar (t.wagenaar@student.tue.nl)
#
# Implementation of the algorithms desribed in the paper "Improving Robot
# Controller Transparency Through Autonomous Policy Explanation" by B. Hayes and
# J.A. Shah.
#Original Code Location: https://gitlab.tue.nl/ha800-hri/hayes-shah
# Import libraries

import json
import UMNumber
import hayes_shah.hs
import time
import importlib

def generatePredicates(failedTask, numberOfAgents):
    isAgent1NearShelf1 = {
        'true': 'Agent 1 is near the shelf1',
        'false': 'Agent 1 is not near the shelf1',
        'verify': lambda s : s['Agent1NearShelf1'] == '1'}

    isAgent1NearShelf2 = {
        'true': 'Agent 1 is near the shelf2',
        'false': 'Agent 1 is not near the shelf2',
        'verify': lambda s : s['Agent1NearShelf2'] == '1'}

    isAgent1NearShelf3 = {
        'true': 'Agent 1 is near the shelf3',
        'false': 'Agent 1 is not near the shelf3',
        'verify': lambda s : s['Agent1NearShelf3'] == '1'}

    isAgent1NearShelf4 = {
        'true': 'Agent 1 is near the shelf4',
        'false': 'Agent 1 is not near the shelf4',
        'verify': lambda s : s['Agent1NearShelf4'] == '1'}

    isAgent1NearShelf5 = {
        'true': 'Agent 1 is near the shelf5',
        'false': 'Agent 1 is not near the shelf5',
        'verify': lambda s : s['Agent1NearShelf5'] == '1'}

    isAgent1NearShelf6 = {
        'true': 'Agent 1 is near the shelf6',
        'false': 'Agent 1 is not near the shelf6',
        'verify': lambda s : s['Agent1NearShelf6'] == '1'}

    isAgent1NearShelf7 = {
        'true': 'Agent 1 is near the shelf7',
        'false': 'Agent 1 is not near the shelf7',
        'verify': lambda s : s['Agent1NearShelf7'] == '1'}

    isAgent1NearShelf8 = {
        'true': 'Agent 1 is near the shelf8',
        'false': 'Agent 1 is not near the shelf8',
        'verify': lambda s : s['Agent1NearShelf8'] == '1'}

    isAgent2NearShelf1 = {
        'true': 'Agent 2 is near the shelf1',
        'false': 'Agent 2 is not near the shelf1',
        'verify': lambda s : s['Agent2NearShelf1'] == '1'}

    isAgent2NearShelf2 = {
        'true': 'Agent 2 is near the shelf2',
        'false': 'Agent 2 is not near the shelf2',
        'verify': lambda s : s['Agent2NearShelf2'] == '1'}

    isAgent2NearShelf3 = {
        'true': 'Agent 2 is near the shelf3',
        'false': 'Agent 2 is not near the shelf3',
        'verify': lambda s : s['Agent2NearShelf3'] == '1'}

    isAgent2NearShelf4 = {
        'true': 'Agent 2 is near the shelf4',
        'false': 'Agent 2 is not near the shelf4',
        'verify': lambda s : s['Agent2NearShelf4'] == '1'}

    isAgent2NearShelf5 = {
        'true': 'Agent 2 is near the shelf5',
        'false': 'Agent 2 is not near the shelf5',
        'verify': lambda s : s['Agent2NearShelf5'] == '1'}

    isAgent2NearShelf6 = {
        'true': 'Agent 2 is near the shelf6',
        'false': 'Agent 2 is not near the shelf6',
        'verify': lambda s : s['Agent2NearShelf6'] == '1'}

    isAgent2NearShelf7 = {
        'true': 'Agent 2 is near the shelf7',
        'false': 'Agent 2 is not near the shelf7',
        'verify': lambda s : s['Agent2NearShelf7'] == '1'}

    isAgent2NearShelf8 = {
        'true': 'Agent 2 is near the shelf8',
        'false': 'Agent 2 is not near the shelf8',
        'verify': lambda s : s['Agent2NearShelf8'] == '1'}

    isAgent3NearShelf1 = {
        'true': 'Agent 3 is near the shelf1',
        'false': 'Agent 3 is not near the shelf1',
        'verify': lambda s : s['Agent3NearShelf1'] == '1'}

    isAgent3NearShelf2 = {
        'true': 'Agent 3 is near the shelf2',
        'false': 'Agent 3 is not near the shelf2',
        'verify': lambda s : s['Agent3NearShelf2'] == '1'}

    isAgent3NearShelf3 = {
        'true': 'Agent 3 is near the shelf3',
        'false': 'Agent 3 is not near the shelf3',
        'verify': lambda s : s['Agent3NearShelf3'] == '1'}

    isAgent3NearShelf4 = {
        'true': 'Agent 3 is near the shelf4',
        'false': 'Agent 3 is not near the shelf4',
        'verify': lambda s : s['Agent3NearShelf4'] == '1'}

    isAgent3NearShelf5 = {
        'true': 'Agent 3 is near the shelf5',
        'false': 'Agent 3 is not near the shelf5',
        'verify': lambda s : s['Agent3NearShelf5'] == '1'}

    isAgent3NearShelf6 = {
        'true': 'Agent 3 is near the shelf6',
        'false': 'Agent 3 is not near the shelf6',
        'verify': lambda s : s['Agent3NearShelf6'] == '1'}

    isAgent3NearShelf7 = {
        'true': 'Agent 3 is near the shelf7',
        'false': 'Agent 3 is not near the shelf7',
        'verify': lambda s : s['Agent3NearShelf7'] == '1'}

    isAgent3NearShelf8 = {
        'true': 'Agent 3 is near the shelf8',
        'false': 'Agent 3 is not near the shelf8',
        'verify': lambda s : s['Agent3NearShelf8'] == '1'}

    isAgent4NearShelf1 = {
        'true': 'Agent 4 is near the shelf1',
        'false': 'Agent 4 is not near the shelf1',
        'verify': lambda s : s['Agent4NearShelf1'] == '1'}

    isAgent4NearShelf2 = {
        'true': 'Agent 4 is near the shelf2',
        'false': 'Agent 4 is not near the shelf2',
        'verify': lambda s : s['Agent4NearShelf2'] == '1'}

    isAgent4NearShelf3 = {
        'true': 'Agent 4 is near the shelf3',
        'false': 'Agent 4 is not near the shelf3',
        'verify': lambda s : s['Agent4NearShelf3'] == '1'}

    isAgent4NearShelf4 = {
        'true': 'Agent 4 is near the shelf4',
        'false': 'Agent 4 is not near the shelf4',
        'verify': lambda s : s['Agent4NearShelf4'] == '1'}

    isAgent4NearShelf5 = {
        'true': 'Agent 4 is near the shelf5',
        'false': 'Agent 4 is not near the shelf5',
        'verify': lambda s : s['Agent4NearShelf5'] == '1'}

    isAgent4NearShelf6 = {
        'true': 'Agent 4 is near the shelf6',
        'false': 'Agent 4 is not near the shelf6',
        'verify': lambda s : s['Agent4NearShelf6'] == '1'}

    isAgent4NearShelf7 = {
        'true': 'Agent 4 is near the shelf7',
        'false': 'Agent 4 is not near the shelf7',
        'verify': lambda s : s['Agent4NearShelf7'] == '1'}

    isAgent4NearShelf8 = {
        'true': 'Agent 4 is near the shelf8',
        'false': 'Agent 4 is not near the shelf8',
        'verify': lambda s : s['Agent4NearShelf8'] == '1'}

    isAgent1HoldingShelf1 = {
        'true': 'Agent 1 is holding the shelf1',
        'false': 'Agent 1 is not holding the shelf1',
        'verify': lambda s : s['Agent1HoldingShelf1'] == '1'}

    isAgent1HoldingShelf2 = {
        'true': 'Agent 1 is holding the shelf2',
        'false': 'Agent 1 is not holding the shelf2',
        'verify': lambda s : s['Agent1HoldingShelf2'] == '1'}

    isAgent1HoldingShelf3 = {
        'true': 'Agent 1 is holding the shelf3',
        'false': 'Agent 1 is not holding the shelf3',
        'verify': lambda s : s['Agent1HoldingShelf3'] == '1'}

    isAgent1HoldingShelf4 = {
        'true': 'Agent 1 is holding the shelf4',
        'false': 'Agent 1 is not holding the shelf4',
        'verify': lambda s : s['Agent1HoldingShelf4'] == '1'}

    isAgent1HoldingShelf5 = {
        'true': 'Agent 1 is holding the shelf5',
        'false': 'Agent 1 is not holding the shelf5',
        'verify': lambda s : s['Agent1HoldingShelf5'] == '1'}

    isAgent1HoldingShelf6 = {
        'true': 'Agent 1 is holding the shelf6',
        'false': 'Agent 1 is not holding the shelf6',
        'verify': lambda s : s['Agent1HoldingShelf6'] == '1'}

    isAgent1HoldingShelf7 = {
        'true': 'Agent 1 is holding the shelf7',
        'false': 'Agent 1 is not holding the shelf7',
        'verify': lambda s : s['Agent1HoldingShelf7'] == '1'}

    isAgent1HoldingShelf8 = {
        'true': 'Agent 1 is holding the shelf8',
        'false': 'Agent 1 is not holding the shelf8',
        'verify': lambda s : s['Agent1HoldingShelf8'] == '1'}

    isAgent2HoldingShelf1 = {
        'true': 'Agent 2 is holding the shelf1',
        'false': 'Agent 2 is not holding the shelf1',
        'verify': lambda s : s['Agent2HoldingShelf1'] == '1'}

    isAgent2HoldingShelf2 = {
        'true': 'Agent 2 is holding the shelf2',
        'false': 'Agent 2 is not holding the shelf2',
        'verify': lambda s : s['Agent2HoldingShelf2'] == '1'}

    isAgent2HoldingShelf3 = {
        'true': 'Agent 2 is holding the shelf3',
        'false': 'Agent 2 is not holding the shelf3',
        'verify': lambda s : s['Agent2HoldingShelf3'] == '1'}

    isAgent2HoldingShelf4 = {
        'true': 'Agent 2 is holding the shelf4',
        'false': 'Agent 2 is not holding the shelf4',
        'verify': lambda s : s['Agent2HoldingShelf4'] == '1'}

    isAgent2HoldingShelf5 = {
        'true': 'Agent 2 is holding the shelf5',
        'false': 'Agent 2 is not holding the shelf5',
        'verify': lambda s : s['Agent2HoldingShelf5'] == '1'}

    isAgent2HoldingShelf6 = {
        'true': 'Agent 2 is holding the shelf6',
        'false': 'Agent 2 is not holding the shelf6',
        'verify': lambda s : s['Agent2HoldingShelf6'] == '1'}

    isAgent2HoldingShelf7 = {
        'true': 'Agent 2 is holding the shelf7',
        'false': 'Agent 2 is not holding the shelf7',
        'verify': lambda s : s['Agent2HoldingShelf7'] == '1'}

    isAgent2HoldingShelf8 = {
        'true': 'Agent 2 is holding the shelf8',
        'false': 'Agent 2 is not holding the shelf8',
        'verify': lambda s : s['Agent2HoldingShelf8'] == '1'}

    isAgent3HoldingShelf1 = {
        'true': 'Agent 3 is holding the shelf1',
        'false': 'Agent 3 is not holding the shelf1',
        'verify': lambda s : s['Agent1HoldingShelf1'] == '1'}

    isAgent3HoldingShelf2 = {
        'true': 'Agent 3 is holding the shelf2',
        'false': 'Agent 3 is not holding the shelf2',
        'verify': lambda s : s['Agent3HoldingShelf2'] == '1'}

    isAgent3HoldingShelf3 = {
        'true': 'Agent 3 is holding the shelf3',
        'false': 'Agent 3 is not holding the shelf3',
        'verify': lambda s : s['Agent3HoldingShelf3'] == '1'}

    isAgent3HoldingShelf4 = {
        'true': 'Agent 3 is holding the shelf4',
        'false': 'Agent 3 is not holding the shelf4',
        'verify': lambda s : s['Agent3HoldingShelf4'] == '1'}

    isAgent3HoldingShelf5 = {
        'true': 'Agent 3 is holding the shelf5',
        'false': 'Agent 3 is not holding the shelf5',
        'verify': lambda s : s['Agent3HoldingShelf5'] == '1'}

    isAgent3HoldingShelf6 = {
        'true': 'Agent 3 is holding the shelf6',
        'false': 'Agent 3 is not holding the shelf6',
        'verify': lambda s : s['Agent3HoldingShelf6'] == '1'}

    isAgent3HoldingShelf7 = {
        'true': 'Agent 3 is holding the shelf7',
        'false': 'Agent 3 is not holding the shelf7',
        'verify': lambda s : s['Agent3HoldingShelf7'] == '1'}

    isAgent3HoldingShelf8 = {
        'true': 'Agent 3 is holding the shelf8',
        'false': 'Agent 3 is not holding the shelf8',
        'verify': lambda s : s['Agent3HoldingShelf8'] == '1'}

    isAgent4HoldingShelf1 = {
        'true': 'Agent 4 is holding the shelf1',
        'false': 'Agent 4 is not holding the shelf1',
        'verify': lambda s : s['Agent4HoldingShelf1'] == '1'}

    isAgent4HoldingShelf2 = {
        'true': 'Agent 4 is holding the shelf2',
        'false': 'Agent 4 is not holding the shelf2',
        'verify': lambda s : s['Agent4HoldingShelf2'] == '1'}

    isAgent4HoldingShelf3 = {
        'true': 'Agent 4 is holding the shelf3',
        'false': 'Agent 4 is not holding the shelf3',
        'verify': lambda s : s['Agent4HoldingShelf3'] == '1'}

    isAgent4HoldingShelf4 = {
        'true': 'Agent 4 is holding the shelf4',
        'false': 'Agent 4 is not holding the shelf4',
        'verify': lambda s : s['Agent4HoldingShelf4'] == '1'}

    isAgent4HoldingShelf5 = {
        'true': 'Agent 4 is holding the shelf5',
        'false': 'Agent 4 is not holding the shelf5',
        'verify': lambda s : s['Agent4HoldingShelf5'] == '1'}

    isAgent4HoldingShelf6 = {
        'true': 'Agent 4 is holding the shelf6',
        'false': 'Agent 4 is not holding the shelf6',
        'verify': lambda s : s['Agent4HoldingShelf6'] == '1'}

    isAgent4HoldingShelf7 = {
        'true': 'Agent 4 is holding the shelf7',
        'false': 'Agent 4 is not holding the shelf7',
        'verify': lambda s : s['Agent4HoldingShelf7'] == '1'}

    isAgent4HoldingShelf8 = {
        'true': 'Agent 4 is holding the shelf8',
        'false': 'Agent 4 is not holding the shelf8',
        'verify': lambda s : s['Agent4HoldingShelf8'] == '1'}

    isAgent1InGoal = {'true': 'Agent 1 is in the goal',
        'false': 'Agent 1 is not in the goal',
        'verify': lambda s : s['Agent1InGoal'] == '1'}

    isAgent2InGoal = {'true': 'Agent 2 is in the goal',
        'false': 'Agent 2 is not in the goal',
        'verify': lambda s : s['Agent2InGoal'] == '1'}

    isAgent3InGoal = {'true': 'Agent 3 is in the goal',
        'false': 'Agent 3 is not in the goal',
        'verify': lambda s : s['Agent3InGoal'] == '1'}

    isAgent4InGoal = {'true': 'Agent 4 is in the goal',
        'false': 'Agent 4 is not in the goal',
        'verify': lambda s : s['Agent4InGoal'] == '1'}

    isPickUp1Complete = {'true': 'Shelf 1 is picked up',
        'false': 'Shelf 1 is picked up',
        'verify': lambda s : s['PickUp1Complete'] == '1'}

    isPickUp2Complete = {'true': 'Shelf 2 is picked up',
        'false': 'Shelf 2 is picked up',
        'verify': lambda s : s['PickUp2Complete'] == '1'}

    isPickUp3Complete = {'true': 'Shelf 3 is picked up',
        'false': 'Shelf 3 is picked up',
        'verify': lambda s : s['PickUp3Complete'] == '1'}

    isPickUp4Complete = {'true': 'Shelf 4 is picked up',
        'false': 'Shelf 4 is picked up',
        'verify': lambda s : s['PickUp4Complete'] == '1'}

    isPickUp5Complete = {'true': 'Shelf 5 is picked up',
        'false': 'Shelf 5 is picked up',
        'verify': lambda s : s['PickUp5Complete'] == '1'}

    isPickUp6Complete = {'true': 'Shelf 6 is picked up',
        'false': 'Shelf 6 is picked up',
        'verify': lambda s : s['PickUp6Complete'] == '1'}

    isPickUp7Complete = {'true': 'Shelf 7 is picked up',
        'false': 'Shelf 7 is picked up',
        'verify': lambda s : s['PickUp7Complete'] == '1'}

    isPickUp8Complete = {'true': 'Shelf 8 is picked up',
        'false': 'Shelf 8 is picked up',
        'verify': lambda s : s['PickUp8Complete'] == '1'}

    isDelivered1Complete = {'true': 'Shelf 1 is delivered',
        'false': 'Shelf 1 is delivered',
        'verify': lambda s : s['Delivered1Complete'] == '1'}

    isDelivered2Complete = {'true': 'Shelf 2 is delivered',
        'false': 'Shelf 2 is delivered',
        'verify': lambda s : s['Delivered2Complete'] == '1'}

    isDelivered3Complete = {'true': 'Shelf 3 is delivered',
        'false': 'Shelf 3 is delivered',
        'verify': lambda s : s['Delivered3Complete'] == '1'}

    isDelivered4Complete = {'true': 'Shelf 4 is delivered',
        'false': 'Shelf 4 is delivered',
        'verify': lambda s : s['Delivered4Complete'] == '1'}

    isDelivered5Complete = {'true': 'Shelf 5 is delivered',
        'false': 'Shelf 5 is delivered',
        'verify': lambda s : s['Delivered5Complete'] == '1'}

    isDelivered6Complete = {'true': 'Shelf 6 is delivered',
        'false': 'Shelf 6 is delivered',
        'verify': lambda s : s['Delivered6Complete'] == '1'}

    isDelivered7Complete = {'true': 'Shelf 7 is delivered',
        'false': 'Shelf 7 is delivered',
        'verify': lambda s : s['Delivered7Complete'] == '1'}

    isDelivered8Complete = {'true': 'Shelf 8 is delivered',
        'false': 'Shelf 8 is delivered',
        'verify': lambda s : s['Delivered8Complete'] == '1'}

    isAgent1DeliverShelf1 = {
        'true': 'Agent 1 can deliver shelf 1',
        'false': 'Agent 1 cannot deliver shelf 1',
        'verify': lambda s : s['Agent1DeliverShelf1'] == '1'}

    isAgent2DeliverShelf1 = {
        'true': 'Agent 2 can deliver shelf 1',
        'false': 'Agent 2 cannot deliver shelf 1',
        'verify': lambda s : s['Agent2DeliverShelf1'] == '1'}

    isAgent3DeliverShelf1 = {
        'true': 'Agent 3 can deliver shelf 1',
        'false': 'Agent 3 cannot deliver shelf 1',
        'verify': lambda s : s['Agent3DeliverShelf1'] == '1'}

    isAgent4DeliverShelf1 = {
        'true': 'Agent 4 can deliver shelf 1',
        'false': 'Agent 4 cannot deliver shelf 1',
        'verify': lambda s : s['Agent4DeliverShelf1'] == '1'}

    isAgent1DeliverShelf2 = {
        'true': 'Agent 1 can deliver shelf 2',
        'false': 'Agent 1 cannot deliver shelf 2',
        'verify': lambda s : s['Agent1DeliverShelf2'] == '1'}

    isAgent2DeliverShelf2 = {
        'true': 'Agent 2 can deliver shelf 2',
        'false': 'Agent 2 cannot deliver shelf 2',
        'verify': lambda s : s['Agent2DeliverShelf2'] == '1'}

    isAgent3DeliverShelf2 = {
        'true': 'Agent 3 can deliver shelf 2',
        'false': 'Agent 3 cannot deliver shelf 2',
        'verify': lambda s : s['Agent3DeliverShelf2'] == '1'}

    isAgent4DeliverShelf2 = {
        'true': 'Agent 4 can deliver shelf 2',
        'false': 'Agent 4 cannot deliver shelf 2',
        'verify': lambda s : s['Agent4DeliverShelf2'] == '1'}

    isAgent1DeliverShelf3 = {
        'true': 'Agent 1 can deliver shelf 3',
        'false': 'Agent 1 cannot deliver shelf 3',
        'verify': lambda s : s['Agent1DeliverShelf3'] == '1'}

    isAgent2DeliverShelf3 = {
        'true': 'Agent 2 can deliver shelf 3',
        'false': 'Agent 2 cannot deliver shelf 3',
        'verify': lambda s : s['Agent2DeliverShelf3'] == '1'}

    isAgent3DeliverShelf3 = {
        'true': 'Agent 3 can deliver shelf 3',
        'false': 'Agent 3 cannot deliver shelf 3',
        'verify': lambda s : s['Agent3DeliverShelf3'] == '1'}

    isAgent4DeliverShelf3 = {
        'true': 'Agent 4 can deliver shelf 3',
        'false': 'Agent 4 cannot deliver shelf 3',
        'verify': lambda s : s['Agent4DeliverShelf3'] == '1'}

    isAgent1DeliverShelf4 = {
        'true': 'Agent 1 can deliver shelf 4',
        'false': 'Agent 1 cannot deliver shelf 4',
        'verify': lambda s : s['Agent1DeliverShelf4'] == '1'}

    isAgent2DeliverShelf4 = {
        'true': 'Agent 2 can deliver shelf 4',
        'false': 'Agent 2 cannot deliver shelf 4',
        'verify': lambda s : s['Agent2DeliverShelf4'] == '1'}

    isAgent3DeliverShelf4 = {
        'true': 'Agent 3 can deliver shelf 4',
        'false': 'Agent 3 cannot deliver shelf 4',
        'verify': lambda s : s['Agent3DeliverShelf4'] == '1'}

    isAgent4DeliverShelf4 = {
        'true': 'Agent 4 can deliver shelf 4',
        'false': 'Agent 4 cannot deliver shelf 4',
        'verify': lambda s : s['Agent4DeliverShelf4'] == '1'}

    isAgent1DeliverShelf5 = {
        'true': 'Agent 1 can deliver shelf 5',
        'false': 'Agent 1 cannot deliver shelf 5',
        'verify': lambda s : s['Agent1DeliverShelf5'] == '1'}

    isAgent2DeliverShelf5 = {
        'true': 'Agent 2 can deliver shelf 5',
        'false': 'Agent 2 cannot deliver shelf 5',
        'verify': lambda s : s['Agent2DeliverShelf5'] == '1'}

    isAgent3DeliverShelf5 = {
        'true': 'Agent 3 can deliver shelf 5',
        'false': 'Agent 3 cannot deliver shelf 5',
        'verify': lambda s : s['Agent3DeliverShelf5'] == '1'}

    isAgent4DeliverShelf5 = {
        'true': 'Agent 4 can deliver shelf 5',
        'false': 'Agent 4 cannot deliver shelf 5',
        'verify': lambda s : s['Agent4DeliverShelf5'] == '1'}

    isAgent1DeliverShelf6 = {
        'true': 'Agent 1 can deliver shelf 6',
        'false': 'Agent 1 cannot deliver shelf 6',
        'verify': lambda s : s['Agent1DeliverShelf6'] == '1'}

    isAgent2DeliverShelf6 = {
        'true': 'Agent 2 can deliver shelf 6',
        'false': 'Agent 2 cannot deliver shelf 6',
        'verify': lambda s : s['Agent2DeliverShelf6'] == '1'}

    isAgent3DeliverShelf6 = {
        'true': 'Agent 3 can deliver shelf 6',
        'false': 'Agent 3 cannot deliver shelf 6',
        'verify': lambda s : s['Agent3DeliverShelf6'] == '1'}

    isAgent4DeliverShelf6 = {
        'true': 'Agent 4 can deliver shelf 6',
        'false': 'Agent 4 cannot deliver shelf 6',
        'verify': lambda s : s['Agent4DeliverShelf6'] == '1'}

    isAgent1DeliverShelf7 = {
        'true': 'Agent 1 can deliver shelf 7',
        'false': 'Agent 1 cannot deliver shelf 7',
        'verify': lambda s : s['Agent1DeliverShelf7'] == '1'}

    isAgent2DeliverShelf7 = {
        'true': 'Agent 2 can deliver shelf 7',
        'false': 'Agent 2 cannot deliver shelf 7',
        'verify': lambda s : s['Agent2DeliverShelf7'] == '1'}

    isAgent3DeliverShelf7 = {
        'true': 'Agent 3 can deliver shelf 7',
        'false': 'Agent 3 cannot deliver shelf 7',
        'verify': lambda s : s['Agent3DeliverShelf7'] == '1'}

    isAgent4DeliverShelf7 = {
        'true': 'Agent 4 can deliver shelf 7',
        'false': 'Agent 4 cannot deliver shelf 7',
        'verify': lambda s : s['Agent4DeliverShelf7'] == '1'}

    isAgent1DeliverShelf8 = {
        'true': 'Agent 1 can deliver shelf 8',
        'false': 'Agent 1 cannot deliver shelf 8',
        'verify': lambda s : s['Agent1DeliverShelf8'] == '1'}

    isAgent2DeliverShelf8 = {
        'true': 'Agent 2 can deliver shelf 8',
        'false': 'Agent 2 cannot deliver shelf 8',
        'verify': lambda s : s['Agent2DeliverShelf8'] == '1'}

    isAgent3DeliverShelf8 = {
        'true': 'Agent 3 can deliver shelf 8',
        'false': 'Agent 3 cannot deliver shelf 8',
        'verify': lambda s : s['Agent3DeliverShelf8'] == '1'}

    isAgent4DeliverShelf8 = {
        'true': 'Agent 4 can deliver shelf 8',
        'false': 'Agent 4 cannot deliver shelf 8',
        'verify': lambda s : s['Agent4DeliverShelf8'] == '1'}

    if numberOfAgents == 2:
        if failedTask == "pickup_shelf1":
            predicates = [isAgent1NearShelf1,isAgent2NearShelf1,isAgent3NearShelf1,isAgent1HoldingShelf1,isAgent2HoldingShelf1]
        if failedTask == "pickup_shelf2":
            predicates = [isAgent1NearShelf2,isAgent2NearShelf2,isAgent3NearShelf2,isAgent4NearShelf2,isAgent2HoldingShelf2]
        if failedTask == "pickup_shelf3":
            predicates = [isAgent1NearShelf3,isAgent2NearShelf3,isAgent3NearShelf3,isAgent4NearShelf3,isAgent2HoldingShelf3]
        if failedTask == "pickup_shelf4":
            predicates = [isAgent1NearShelf4,isAgent2NearShelf4,isAgent3NearShelf4,isAgent4NearShelf4,isAgent2HoldingShelf4]
        if failedTask == "pickup_shelf5":
            predicates = [isAgent1NearShelf5,isAgent2NearShelf5,isAgent3NearShelf5,isAgent4NearShelf5,isAgent2HoldingShelf5]
        if failedTask == "pickup_shelf6":
            predicates = [isAgent1NearShelf6,isAgent2NearShelf6,isAgent3NearShelf6,isAgent4NearShelf6,isAgent2HoldingShelf6]
        if failedTask == "deliver_shelf1":
            predicates = [isAgent1DeliverShelf1,isAgent2DeliverShelf1]
        if failedTask == "deliver_shelf2":
            predicates = [isAgent1DeliverShelf2,isAgent2DeliverShelf2]
        if failedTask == "deliver_shelf3":
            predicates = [isAgent1DeliverShelf3,isAgent2DeliverShelf3]
        if failedTask == "deliver_shelf4":
            predicates = [isAgent1DeliverShelf4,isAgent2DeliverShelf4]
        if failedTask == "deliver_shelf5":
            predicates = [isAgent1DeliverShelf5,isAgent2DeliverShelf5]
        if failedTask == "deliver_shelf6":
            predicates = [isAgent1DeliverShelf6,isAgent2DeliverShelf6]
    return predicates

def pickupFailure(targetState,shelfNumber,numberOfAgents):
    states = []
    actions = []
    one = []

    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 2:
            holdState = {'Agent1NearShelf'+str(shelfNumber): '0', 'Agent2NearShelf'+str(shelfNumber): '0','Agent1HoldingShelf'+str(shelfNumber): '0','Agent2HoldingShelf'+str(shelfNumber): '0'}
            if "True" in state[2*i-(3-1)]:
                holdState['Agent1NearShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*i-(3-2)]:
                holdState['Agent2NearShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(i+4)-(3-1)]:
                holdState['Agent1HoldingShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(i+4)-(3-2)]:
                holdState['Agent2HoldingShelf'+str(shelfNumber)] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("pickup_shelf"+str(shelfNumber),numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState["pickup_shelf"+str(shelfNumber)]:
        state = s.split(",")
        if numberOfAgents == 2:
            holdState = {'Agent1NearShelf'+str(shelfNumber): '0', 'Agent2NearShelf'+str(shelfNumber): '0','Agent1HoldingShelf'+str(shelfNumber): '0','Agent2HoldingShelf'+str(shelfNumber): '0'}
            if "True" in state[2*i-(3-1)]:
                holdState['Agent1NearShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*i-(3-2)]:
                holdState['Agent2NearShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(i+4)-(3-1)]:
                holdState['Agent1HoldingShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(i+4)-(3-2)]:
                holdState['Agent2HoldingShelf'+str(shelfNumber)] = '1'
        one.append(holdState)

    return explainer,one

def deliverFailure(targetState,shelfNumber,numberOfAgents):
    states = []
    actions = []
    one = []

    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 2:
            holdState = {'Agent1DeliverShelf'+str(shelfNumber): '0','Agent2DeliverShelf'+str(shelfNumber): '0'}
            if "True" in state[2*(shelfNumber+11)-(3-1)]:
                holdState['Agent1DeliverShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(shelfNumber+11)-(3-2)]:
                holdState['Agent2DeliverShelf'+str(shelfNumber)] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("deliver_shelf"+str(shelfNumber),numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState["deliver_shelf"+str(shelfNumber)]:
        state = s.split(",")
        if numberOfAgents == 2:
            holdState = {'Agent1DeliverShelf'+str(shelfNumber): '0','Agent2DeliverShelf'+str(shelfNumber): '0'}
            if "True" in state[2*(shelfNumber+11)-(3-1)]:
                holdState['Agent1DeliverShelf'+str(shelfNumber)] = '1'
            if "True" in state[2*(shelfNumber+11)-(3-2)]:
                holdState['Agent2DeliverShelf'+str(shelfNumber)] = '1'
        one.append(holdState)

    return explainer,one


def convertUserQuery(userQuery, failedTask):
    convertedQuery = ''
    timeStep = float('inf')
    for i in userQuery.keys():
        if failedTask in userQuery[i]:
            convertedQuery = convertedQuery + '1'
            timeStep = userQuery[i].index(failedTask)
        else:
            convertedQuery = convertedQuery + '0'

    return convertedQuery, timeStep

def updateUserQuery(userQuery,updatingQuery,failedTask,timeStep,numberOfAgents):
    newAgent = updatingQuery.index("1")
    index = -1
    for i in userQuery.keys():
        if failedTask in userQuery[i]:
            index = userQuery[i].index(failedTask)
            userQuery[i][index] = "*"
            userQuery["agent"+str(index+1)][index] = failedTask
            break

    return userQuery


def genNotPossExp(userQuery, numberOfAgents):
        importlib.reload(UMNumber)
        failedTasks = UMNumber.failedTasks
        targetState = UMNumber.targetState
        for failedTask in failedTasks:
            convertedQuery, timeStep = convertUserQuery(userQuery, failedTask)
            if targetState[failedTask] == []:
                print(failedTask + ":")
                bestMinterm_list = []
                print(failedTask + " cannot be completed.")
            elif "pickup_shelf" in failedTask:
                explainer,one = pickupFailure(targetState,int(failedTask[-1]),numberOfAgents)
                print(failedTask + ":")
                clauses,bestMinterm_list = explainer.getLanguage(one, convertedQuery,failedTask,timeStep,numberOfAgents)
                print(clauses)
            elif "deliver_shelf" in failedTask:
                explainer,one = deliverFailure(targetState,int(failedTask[-1]),numberOfAgents)
                print(failedTask + ":")
                clauses,bestMinterm_list = explainer.getLanguage(one, convertedQuery,failedTask,timeStep,numberOfAgents)
                print(clauses)
            userQuery = updateUserQuery(userQuery,bestMinterm_list,failedTask,timeStep,numberOfAgents)
            print("")

        return userQuery

def main():
    numberOfAgents = 2
    userQuery = {"agent1": ["*","*","*"],   #Not Possible Query
    "agent2":["deliver_shelf4","deliver_shelf2","deliver_shelf1"]}
    #genNotPossExp(userQuery, numberOfAgents)
main()
