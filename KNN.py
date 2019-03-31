def classify0(inX, dataset, labels,k):
	datasetSize = dataset.shape[0]
	diffMat = tile(inX,(datasetSize,1))-dataset #tile的功能是重复某个数组,重复inX数组的行(dataSize)次，列重复1
	sqDiffMat = diffMat**2 #平方操作
	sqDistances = sqDiffMat.sum(axis=1) # 每一个列向量相加,axis=0为行相加
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount={}
	    ######累计次数构成字典######
    for i in range(k):
        #print sortedDistIndicies[i]
        voteIlabel = labels[sortedDistIndicies[i]] #排名前k个贴标签
        #print voteIlabel
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1 # 不断累加计数的过程，体现在字典的更新中
        #print classCount.get(voteIlabel,0)
        #print classCount
        #get(key,default=None),就是造字典


    ######找到出现次数最大的点######
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse=True)
    #以value值大小进行排序，reverse=True降序
    #print classCount.iteritems()
    #print sortedClassCount
    #key = operator.itemgetter(1)，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值

    return sortedClassCount[0][0]
    #返回出现次数最多的value的key
