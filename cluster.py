import os
import sys

class Data:
	def __init__(self, id_, x_, y_):
		self.id = int(id_)
		self.x = float(x_)
		self.y = float(y_)
		self.label = None

class DBSCAN:
	def __init__(self, datas_, eps_, min_pts_):
		self.datas = datas_
		self.eps = eps_
		self.min_pts = min_pts_

	def get_density_reachable(self, point):
		pts = []
		for i in range(len(self.datas)):
			if(distance(point,self.datas[i]) <= self.eps):
				pts.append(self.datas[i])
		pts.remove(point)
		return pts

	def getDatas(self):
		return self.datas

	def getMinPts(self):
		return self.min_pts

	def getEps(self):
		return self.eps

def distance(point1, point2):
	return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

def sortByID(cluster):
	cluster = list(cluster)
	for i in range(len(cluster)):
		lowest = cluster[i].id
		idx = i
		for j in range(i, len(cluster)):
			if (cluster[j].id < i):
				idx = j
				lowest = cluster[j].id
		tmp = cluster[i]
		cluster[i] = cluster[idx]
		cluster[idx] = tmp
	return set(cluster)

def fetch(txt):
	fetched_datas = []
	f = open(txt, "r")
	lines = f.read()
	line = lines.split('\n')
	for i in range(len(line)-1):
		features = line[i].split('\t')
		data_ = Data(int(features[0]),float(features[1]),float(features[2]))
		fetched_datas.append(data_)
	return fetched_datas

def clust(dbscan):
	cluster_count = 0
	clusters = []
	for pt in dbscan.getDatas():
		if(pt.label != None):
			continue
		dr = dbscan.get_density_reachable(pt)
		if len(dr) < dbscan.getMinPts():    #is not core
			pt.label = "OUTLIER"
			continue
		cluster_count += 1
		curr_cluster = set([])
		pt.label = cluster_count
		curr_cluster.add(pt)
		data_set = set(dr)
		while data_set:
			q = data_set.pop()
			if q.label == "OUTLIER":
				q.label = cluster_count     # is border
			if(q.label != None):
				continue
			q.label = cluster_count
			curr_cluster.add(q)
			dr = dbscan.get_density_reachable(q)
			if len(dr) >= dbscan.getMinPts():
				data_set.update(dr)
		clusters.append(curr_cluster)
	return clusters


def main(arguments):
	data = fetch(arguments[1])
	dbscan = DBSCAN(data, float(arguments[3]), int(arguments[4]))
	clusters = clust(dbscan)
	clusters.sort(key=len, reverse=True)

	if len(clusters) > int(arguments[2]):
		clusters = clusters[0:int(arguments[2])]

	for i in range(len(clusters)):
		clusters[i] = sortByID(clusters[i])
		f = open(arguments[1][:-4] +"_cluster_" +str(i)+".txt", 'w')
		for pt in clusters[i]:
			f.write(str(pt.id) + '\n')
		f.close()

if __name__ == '__main__':
	main(sys.argv)