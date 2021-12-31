if __name__ == '__main__':
    scores_list=[];
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        scores_list.append([name,score])
second_highest = sorted(set([score for name, score in scores_list])) [1]
print('\n'.join(sorted([name for name, score in scores_list if score == second_highest])))
