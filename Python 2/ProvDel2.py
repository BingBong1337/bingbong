import numpy as np
x = -0.5
numpy_log_val = np.log(1+x)

log_series_10a = x -x**2/2 + x**3/3-x**4/4+x**5/5-x**6/6+x**7/7-x**8/8+x**9/9-x**10/10
print(numpy_log_val-log_series_10a)
max = 1/10000000

log_series_10b = x -x**2/2 + x**3/3-x**4/4+x**5/5-x**6/6+x**7/7-x**8/8+x**9/9-x**10/10+x**11/11-x**12/12+x**13/13-x**14/14+x**15/15-x**16/16+x**17/17-x**18/18+x**19/19
s = abs(numpy_log_val-log_series_10b)
print(s)
if s < max:
    print('True')

