
def count_words(cont):
    lst = cont.split()
    return len(lst)

def count_chars(cont):
    cont = cont.lower()
    dic = dict()
    for c in cont:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

def alpha_count_index(count_dic):
    sorted_dic = []
    for char in count_dic:
        if char.isalpha():
            sorted_dic.append({"char": char, "count": count_dic[char]})
    sorted_dic.sort(key=lambda x:x["count"], reverse=True)
    return sorted_dic