import math 
log_loss = []
def compute_log_loss(values): 
    
    for (x,y) in values:
        
        A = (x * math.log10 ( y )+ ( 1-x ) * math.log10 ( 1-y ))
        
        log_loss.append(A)
        
    return -1 * ( 1/len( values )) * sum(log_loss)

values = [[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]] #list of list
compute_log_loss(values)
