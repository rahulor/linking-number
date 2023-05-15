from scipy.signal import butter

seed = 42
# -----------------------------------------------------
ncombination= 2000      # number of loop combinations
npoints     = 50        # on the curve
nrotation   = 36
# setting standard filter requirements.
b_lpf, a_lpf = butter(5, 1./10, 'low')

# array manipulation
arr_pad = 50
arr_rot = 30