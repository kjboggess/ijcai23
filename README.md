# Explainable MARL For Temporal Queries
<hr>
Repository for supplementary material for "Explainable Multi-Agent Reinforcement Learning For Temporal Queries" published in IJCAI 2023.
<hr>
OS tested on
"Centos Linux 7"
<hr>
<b>Set up:</b><br>
 1. Download Shared Experience Actor Critic for MARL and install as instructed<br>
	*Used for training and evaluation policiesv
	Location: https://github.com/semitable/seac<br>
	Rename "seac-master" folder to "seac"<br>
 2. Download Level-based Foraging Environment and install as instructed<br>
	*Used to register search and rescue and level-based foraging environments to gym<br>
	Location: https://github.com/uoe-agents/lb-foraging<br>
 3. Download further domains if preferred and install as instructed<br>
	Robotic warehouse domain location: https://github.com/uoe-agents/robotic-warehouse<br>
	Pressure plate location: https://github.com/semitable/pressureplate<br>
 4. Download "Improving Robot Controller Transparency Through Autonomous Policy Explanation" Implemenation and install as instructed<br>
	*Used to set up Quine-Mccluskey algorithm<br>
	Location: https://gitlab.tue.nl/ha800-hri/hayes-shah<br>
 5. Install remaining requirements in "requirements.txt" if needed<br>
<hr>
<b>Training a policy:</b>
 1. Polices should be trained as described by Shared Experience Actor Critic for MARL
	Location: https://github.com/semitable/seac
 2. Any other MARL method can be used to train a policy a preferred
 3. An example policy for each domain is given in "Code Pipeline/results/trained_models/###/u####
 4. An example environment for training is given in Code Pipeline/seac MARL replacement files
<hr>
<b>Evaluating a policy:</b>
 1. Add the "evaluateForConRoll.py" file to "seac/seac" folder
 2. Set policy path, environment name, time limit, number of evaluation steps, number of agents, number of tasks, and start state in file (Examples given in file)
 3. Define any new rules for low-level to high-level state conversion in file
 4. Run file -> "python evaluateForConRoll.py"
 5. Example files produced from small evaluation (100 steps) are given in "Model Examples/runningexample"
 4. An example environment for evaluation is given in Code Pipeline/seac MARL replacement files
<hr>
<b>Generating an explanation with guided rollout:</b>
 1. Add the "abstractToPrism.py", "generateExplanations.py", "generateNotPossExp_3agTotalQ.py", and "policyConRoll3agABATotalQ.py" files to seac/seac folder. You may need to add "convertStates.py" to the seac/seac folder if the file is available.
 2. Make sure files produced from evaluating a policy are in the seac/seac folder.
 3. Add the "hayes_shah" and "quine_mcclusky" folders to seac/seac folder, replacing others if needed
 4. Replace seac files of the same name with those found in seac MARL replacement files folder
 5. Set user query in main function of "policyConRoll3agABATotalQ.py"(Examples in file)
 6. Set search parameters in main function of "policyConRoll3agABATotalQ.py"(Examples in file)
 7. Define any new rules for low-level to high-level state conversion
 8. Run file -> "python policyConRoll3agABATotalQ.py"
	*Generates abstract mmdp through guided rollout and explanation for any impossible tasks
 10. Example log output produced from evaluation are given in explanation output folder along with generated PRISM model and properties
