#!/bin/bash
clear
echo "Now Running Intel Model Optimizer"
echo "Make Sure You Have installed the prerequisites"
echo "Please Install /deployment_tools/model_optimizer/install_prerequisites/install_prerequisites_tf"
echo "Ignore if already installed"
sleep 1
clear
MO_TF_PATH='/opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py'
echo "Taking Default Path for mo_tf.py $MO_TF_PATH"
read -p "Please Input Model Path : " PB_FILE_PATH
echo "Now Optimizing $PB_FILE_PATH"
echo "************Please Select Output Format************"
echo "  1)FP32 (Intel CPU)"
echo "  2)FP16 (MYRIAD)"
read n
case $n in
  1) OUT='FP32';;
  2) OUT='FP16';;
  *) echo "invalid option";;
esac
read -p "Please Enter model  first layer height or width : " NET_INP
sleep 2
clear
echo "#####################################################"
echo "#####Now Taking Input as [1,$NET_INP,$NET_INP,3]#####"
echo "#####################################################"
echo "##################Data Type is $OUT##################"
echo "#####################################################"
echo "##########Model is located at $PB_FILE_PATH##########"
echo "#####################################################"
echo "python3 $MO_TF_PATH --input_model $PB_FILE_PATH --output_dir ./ --input_shape [1,$NET_INP,$NET_INP,3] --data_type $OUT"
python3 $MO_TF_PATH --input_model $PB_FILE_PATH --output_dir ./ --input_shape [1,$NET_INP,$NET_INP,3] --data_type $OUT

