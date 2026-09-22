#include <cuda_runtime.h>
#include <vector>

__global__ void scale_kernel(const float* x, float a, float* y, int n) {
    // y[i] = a * x[i]
}

std::vector<float> scalar_multiply(const std::vector<float>& x, float a) {
    std::vector<float> res;
    for(int i = 0; i < x.size(); i++){
        res.push_back(x[i] * a);
    }
    
    return res;
}
