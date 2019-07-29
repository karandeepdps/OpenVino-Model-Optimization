import argparse
import tensorflow as tf


class Freezer:
	
	def __init__(self, model_file, save_dir):
		self.model_file_name = model_file
		self.model = None
		self.session = None
		self.save_dir = save_dir

	def load_model(self):
		tf.keras.backend.clear_session()
		tf.keras.backend.set_learning_phase(0)
		from tensorflow.keras.models import load_model
		print('Loading Model {}'.format(self.model_file_name))
		self.model = load_model(self.model_file_name)
		
	def freezeit(self):
		from tensorflow.python.framework import graph_io
		self.session = tf.keras.backend.get_session()
		INPUT_NODE = [inp.op.name for inp in self.model.inputs]
		print('Input_Node: {} Len: {}'.format(INPUT_NODE,len(INPUT_NODE)))
		OUTPUT_NODE = [out.op.name for out in self.model.outputs]
		with self.session.graph.as_default():
			print("Prunes out nodes that aren't needed for inference")
			graphdef_pruned = tf.graph_util.remove_training_nodes(self.session.graph.as_graph_def())
			print('Replaces all the variables in a graph with constants of the same values.')
			graphdef_frozen = tf.graph_util.convert_variables_to_constants(self.session, graphdef_pruned, OUTPUT_NODE)
			graph_io.write_graph(graphdef_frozen, self.save_dir, 'frozen_model.pb', as_text=0)
			print('*'*5,'Model Saved at: {}'.format(self.save_dir),'*'*5)


if __name__=='__main__':
	print('Load')
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--model_file",required=1,help="model file to freeze")
	parser.add_argument("-o", "--output_dir",required=1,help="output dir for saved model")
	args = parser.parse_args()
	freezer_obj = Freezer(model_file=args.model_file, save_dir=args.output_dir)
	freezer_obj.load_model()
	freezer_obj.freezeit()
