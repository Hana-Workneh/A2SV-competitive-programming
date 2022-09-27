class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans, q = [], []
        for idx, ch in enumerate(dominoes):
            if ch == '.':
                q.append(idx)
            elif ch == 'R':
                if q:
                    if dominoes[q[0]] == 'R':
                        ans += ['R'] * len(q)
                    else:
                        ans += ['.'] * len(q)
                    q.clear()
                q.append(idx)
            elif ch == 'L':
                if q:
                    if dominoes[q[0]] == 'R':
                        if (len(q)+1) % 2:
                            ans += ['R'] * ((len(q)+1)//2) + ['.'] + ['L'] * ((len(q)+1)//2)
                        else:
                            ans += ['R'] * ((len(q)+1)//2) + ['L'] * ((len(q)+1)//2)
                    else:
                        ans += ['L'] * (len(q)+1)
                    q.clear()
                else:
                    ans.append('L')
        if q:
            if dominoes[q[0]] == 'R':
                ans += ['R'] * len(q)
            else:
                ans += ['.'] * len(q)
        return ''.join(ans)