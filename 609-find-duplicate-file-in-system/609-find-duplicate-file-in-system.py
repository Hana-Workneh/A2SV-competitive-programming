class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for path in paths:
            ps=path.split(' ')
            fold=ps[0]
            for i in range(1,len(ps)):
                file=ps[i]
                fs=file.split('(')
                fnm=fs[0]
                key=fs[1][0:-1]
                m[key].append(fold+'/'+fnm)
                
       
        res=[]
        for k in m:
            if len(m[k])>1:
                res.append(m[k])
        return res