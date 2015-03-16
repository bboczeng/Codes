__author__ = 'bozeng'

def lengthOfLongestSubstring(s):
        maxlength=0
        templength=0
        charused={}
        start=0
        for i in range(len(s)):
            if s[i] not in charused or charused[s[i]]<start:
                charused[s[i]]=i
                templength+=1
                maxlength=max(maxlength,templength)
            elif s[i] in charused :
                start=charused[s[i]]+1
                charused[s[i]]=i
                templength=i-start+1
                maxlength=max(maxlength,templength)


        return maxlength


print(lengthOfLongestSubstring("abcabcbb"))