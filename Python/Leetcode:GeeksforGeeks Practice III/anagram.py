__author__ = 'bozeng'


def anagrams(strs):
        if not strs:
            return []

        count={}

        for (indx,each) in enumerate(strs):
            temp="".join(sorted(each))

            if temp not in count:
                count[temp]=[]
                count[temp].append(indx)
            else:
                count[temp].append(indx)


        result=[]
        for key in count.keys():
            if len(count[key])>1:
                for each in count[key]:
                    result.append(strs[each])

        return result

print(anagrams(["cat","act","bbs","asda","565","223","sbb"]))