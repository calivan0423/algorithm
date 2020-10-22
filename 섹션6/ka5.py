from datetime import datetime
from itertools import permutations


def between(times):

  FMT = '%y:%M:%S'

  start = [i[0] for i in times]
  end = [i[1] for i in times]

  latest_start = sorted(start, key=lambda x : datetime.strptime(x, FMT))[-1]
  earliest_end = sorted(end, key=lambda x : datetime.strptime(x, FMT))[0]

  delta = datetime.strptime(earliest_end, FMT)-datetime.strptime(latest_start, FMT)

  if delta.days >= 0:
    return ([latest_start, earliest_end])
  else:
    return None

def trans_logs(logs):
  new = []
  for i in logs:
      new.append(i.split('-'))
  return new


def combination(logs):
  return list(map(list, permutations(logs, 2)))


def max(logs, before):
	if len(logs) == 0:
		return before
	if len(logs) == 1:
		return logs[0]
	else:
		com = combination(logs)
		between = []
		for i in com:
			a = between(i)
			if a != None and a not in between:
				between.append(a)
		return max(between, logs)


logs = trans_logs(logs)


answer=(max(logs, logs))