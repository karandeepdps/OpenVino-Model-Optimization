import os
try:
	if not 'computer_vision_sdk' in os.environ['PYTHONPATH']:
		os.system('source /opt/intel/openvino/bin/setupvars.sh')
		print('Please set correct openvino setupvars if you cant get past this')
except Exception as e:
	print('Please set correct openvino setupvars')
try:
	from openvino import inference_engine as ie
    from openvino.inference_engine import IENetwork,IEPlugin
except ModuleNotFoundError as e:
	print(e)
	print('Exiting...')
	sys.exit(1)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--model_xml",required=1,help="path to model_xml")
parser.add_argument("--model_bin",required=1,help="path to model_bin")
parser.add_argument("--device_type",required=1,help="CPU,MYRIAD")
parser.add_argument("--img",required=1,help="path to image")
args = parser.parse_args()
plugin = IEPlugin(args.device_type)
net = IENetwork.from_ir(model=args.model_xml, weights=args.model_bin)
exec_net = plugin.load(network=net)
print('Please make sure your image is preprocessed and resized')
res = exec_net.infer(inputs={next(iter(net.inputs)): args.img})
print(res)
