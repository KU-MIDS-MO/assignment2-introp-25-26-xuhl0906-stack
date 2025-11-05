def breakdown_time(seconds):
    ### Replace with your own code (begin) ###
    if not isinstance(seconds, int) or seconds<0:
        return -1
    if seconds==0:
        return{}
    hours=seconds//3600
    seconds=seconds%3600
    minutes=seconds//60
    seconds=seconds%60
    result={}
    if hours>0:
        result[3600]=hours
    if minutes>0:
        result[60]=minutes
    if seconds>0:
        result[1]=seconds
    return result
    ### Replace with your own code (end)   ###
