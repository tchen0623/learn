def permute(self,nums:List[int])->List[List[int]]:
    result = []
    track=[]
    def trackBack(nums_,track_):
        if len(track_)==len(nums_):
            result.append(track_[:])
            return
        for i in nums_:
            if i in track_:
                continue
                track.append(i)
                trackBack(nums_,track_)
                track.pop()
    trackBack(nums,track)
    return result