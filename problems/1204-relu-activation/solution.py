#include <cuda_runtime.h>
#include <vector>

__global__ void relu_kernel(const float* x, float* out, int n) {
    // out[i] = max(0, x[i])
}

float max(const float & x){
    if(x> 0){
        return  x;
    }
    return 0;


}

std::vector<float> relu(const std::vector<float>& x) {
    std::vector<float> res;
    for(int i = 0; i < x.size(); i ++){
        res.push_back(max(x[i]));
    }

    return res;
}
