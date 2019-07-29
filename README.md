# OpenVino-Model-Optimization
### OpenVino Installation
In this paced up tutorial, you will get to know how to optimize your slow neural network using intel OpenVino.
If you own an intel CPU,NCS-1,NCS-2 then we are good to go.Otherwise i suggest you to buy one.
OpenVino use the Intel Math Kernel Library for Deep Neural Networks and the OpenMP to parallelize calculations.
You May Download OpenVino From Here. https://software.intel.com/en-us/openvino-toolkit/choose-download

### After Installation
After you are done with installation dont forget to add setupvars to your bash file.
 ```echo "source /opt/intel/openvino/bin/setupvars.sh" >> ~/.bashrc ```

### Steps to Convert
1. First Save your keras model weights using command 'model.save('model_file_name.h5')'
2. Freeze the graph using freeze.py file.
3. Run OpenVino_Optimizer.sh to optimize the freezed model.
4. Run Inference.py to load your optimized code.

###References:

