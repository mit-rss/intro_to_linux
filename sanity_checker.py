from copy import deepcopy
import re
def end_line(line):
	pattern = re.compile("^([#]+)(End of Question)([#]+)$")
	return pattern.match(line.strip()) is not None
def strt_line(line):
	pattern = re.compile("^([#]+)([0-9][a-zA-Z])([#]+)$")
	return pattern.match(line.strip()) is not None
def get_id(line):
	return re.search("[0-9][a-zA-Z]",line.strip()).group(0)
def parser(filename):
	_file = open(filename,"r");
	lines = _file.readlines()
	#print lines
	_file.close()
	answers = {}
	answer_lines = []
	name = "None"
	_ready = False
	while lines:
		line = lines.pop(0)
		if end_line(line):
			#print "end_line"
			answers[name]=deepcopy(answer_lines)
			answer_lines = []
			_ready=False
		elif strt_line(line):
			#print "strt_line"
			name = get_id(line);
			_ready = True
		elif _ready:
			if line.strip()!='':
				answer_lines.append(line.strip())
	return answers
#print parser("solution.txt").keys()

def checker(filename):
	expected_keys = ['1a', '1b', '1c', '1d', '1e', '2a', '2b', '2c', '2d', '2e', '2f', '2g', '3a', '3b', '3c', '3d']
	cmd_map = parser(filename)
	missing = [key for key in expected_keys if not key in cmd_map]
	added = [key for key in cmd_map if not key in expected_keys]
	if missing!=[]:
		raise KeyError(str(missing)+' are not present in your solution! MAKE NOT TO REMOVE ANY OF \######<question number>###### or ######End of Question#### lines')
	if added!=[]:
		raise KeyError(str(added)+' are unexpected question ids! MAKE NOT TO REMOVE ANY OF \######<question number>###### or ######End of Question#### lines')
	empty=[]
	answered = []
	for q in sorted(expected_keys):
		if cmd_map[q]!=[]:
			answered.append(q)
		else:
			empty.append(q)
	print "------------FILLED QUESTIONS-----------"
	for q in answered:
		print "<<<<<<<<<< "+q+" >>>>>>>>>>>>"
		print "commands:"
		for cmd in cmd_map[q]:
			print cmd
	print "------------EMPTY QUESTIONS-----------"
	for q in empty:
		print "<<<<<<<<<< "+q+" >>>>>>>>>>>>"
if __name__=="__main__":
	checker("linux_exercise.txt")
