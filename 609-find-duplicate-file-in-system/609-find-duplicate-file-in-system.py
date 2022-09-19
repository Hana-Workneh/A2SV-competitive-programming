class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(lambda:[])
        for path in paths:
            p = path.split()
            fa = [i.split('(') for i in p[1:]]
            for i in fa:
                hashmap[i[1][:-1]].append(p[0]+'/'+i[0])
        
        return [v for v in hashmap.values() if len(v)>1]