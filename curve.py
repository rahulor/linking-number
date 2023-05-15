import numpy as np
from scipy.signal import filtfilt
import helper
from math import fabs
import random

def generate_loops(rng, npoints):
    N = npoints-1   # to make the below code better
    T = 1           # [s]
    dt = T/N        # [s]
    B = np.empty((N+1, 6)) # 6 columns; time in rows
    xi = np.sqrt(0.2*dt)*rng.randn(N+1, 6) # D = 0.1
    xi[0,:] = 0
    W = np.cumsum(xi, axis=0)
    for n in range(0, N+1):           
         t = n * dt
         B[n,:] = W[n,:] - (t/T)*W[N,:]                                                        
    return get_smooth_bridge(B)    # shape (N,6)

def pad_both_ends(arr_, pad, arr_rot):
    arr = np.roll(arr_, arr_rot, axis=0)
    return np.vstack(( arr[-pad:], arr, arr[0:pad]))

def get_smooth_bridge(B):
    from inputs import arr_pad, arr_rot, b_lpf, a_lpf 
    B_pad= pad_both_ends(B, arr_pad, arr_rot)
    B_smooth = filtfilt(b_lpf, a_lpf, B_pad, axis=0)[arr_pad:-arr_pad+1]
    return B_smooth    

def linking_number(R1, R2):
    dR1, dR2 = np.diff(R1, axis=0), np.diff(R2, axis=0)
    N = len(dR1)
    sum2 = 0
    for i in range(N):
        sum1 = 0
        for j in range(N):
            A = R1[i] - R2[j]
            B = np.cross(dR1[i], dR2[j])
            mag = np.sqrt(A.dot(A))
            sum1 = sum1 + A.dot(B)/(mag**3)
        sum2 = sum2+sum1
    Lk = sum2/(4*np.pi)
    return np.round(Lk, 3)
    
def rotation_about_z(theta):
    rot_about_z = np.array([
                            [np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta),  np.cos(theta), 0],
                            [0,                 0,          1]])
    return rot_about_z

def sort_Lk_values(L_):
    L = fabs(L_)
    if L < 0.1:
        L = 0
    elif 0.9<L<1.1:
        L = 1
    else:
        L = None
    return L
def generate_dataset(seed, fname):
    from inputs import ncombination, npoints, nrotation
    rng= np.random.RandomState(seed)
    loops_list = []
    label_list = []
    for i in range(ncombination):
        print(f'{i}/{ncombination} ----')
        loops = generate_loops(rng, npoints)
        shift = rng.uniform(-0.1, 0.1, size=3)
        R1, R2 = loops[:,0:3], loops[:,3:]+shift
        loops_list_temp = []
        label_list_temp = []
        for j in range(nrotation):
            theta = j * 2*np.pi/nrotation
            R_theat_z = rotation_about_z(theta)
            R2_rot = R_theat_z.dot(R2.T).T
            Lk = linking_number(R1, R2_rot)
            Lk = sort_Lk_values(Lk)
            if Lk is not None:
                loops_list_temp.append(np.hstack((R1, R2_rot)))
                label_list_temp.append(Lk)
        
        idx_one = np.where(np.array(label_list_temp)==1)[0]
        nfamily = len(idx_one)
        if nfamily>0:
            idx_zero = np.where(np.array(label_list_temp)==0)[0]
            idx_zero = random.sample(list(idx_zero), min(len(idx_zero), len(idx_one)))
            idx_mix = np.array(list(idx_one) + idx_zero)
            for idx in idx_mix:
                loops_list.append(loops_list_temp[idx])
                label_list.append(label_list_temp[idx])
    helper.pickle_to('data/' + fname + '_loops_labels', (loops_list, label_list))
    print(f'number of samples: {len(label_list)}')
    
def main():
    # for training
    seed        = 10
    print(f'generating dataset for training..')
    generate_dataset(seed, 'train')
    # for testing
    print(f'generating dataset for testing..')
    seed        = seed + 444444
    generate_dataset(seed, 'test')
    
if __name__== "__main__":
    main()
