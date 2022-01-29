def swap(my_list, i, j):
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp

def is_target(word_list, target, end_idx):
    s = ''
    for i in range(0,end_idx):
        s+=word_list[i]
    return s == target

def concat(word_list,target,idx):
    if len(word_list) == idx :
        return "".join(word_list) == target
    else:
        for i in range(idx,len(word_list)):
            swap(word_list, idx, i)
            if is_target(word_list,target,idx+1):
                return True
            if concat(word_list,target,idx+1):
                return True
            swap(word_list, idx, i)
            
def solve(word_list, target):
    return_word = []
    for word in word_list:
        length = len(word)
        start_idx = 0
        for i in range(len(target)//length):
            start_idx = i * length
            if start_idx + length >= len(target):
                if target[start_idx - length::] == word:
                    return_word.append(word)
                    break
            if target[start_idx:start_idx+length:] == word:
                return_word.append(word)
                break
    if concat(return_word, target, 0):
        return tuple(return_word)
    else:
        return None
    

if __name__ == '__main__':

    print(solve(['ab', 'bc','cd'], 'cdab'))
    print(solve(['ab', 'bc','cd'], 'abcd')) 
    print(solve(['ab', 'bc','cd'], 'abab'))



