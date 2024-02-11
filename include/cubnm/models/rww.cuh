#ifndef RWW_CUH
#define RWW_CUH
#include "rww.hpp"
// the following are necessary as cuda code is compiled separately
// but the function is called from the main code that is compiled by g++
// therefore, from nvcc's perspective, there is no need to compile the
// function for this model, because it is not used in the cuda code
// TODO: remove them 
template void _run_simulations_gpu<rWWModel>(
    double*, double*, double*, 
    u_real**, u_real**, u_real*, 
    u_real*, u_real*, 
    BaseModel*
);

template void _init_gpu<rWWModel>(BaseModel*, BWConstants);
#endif