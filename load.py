import os 

def load_trained_model() :
  weight_file = f"{os.getcwd()}/model_phase_2.h5"
  assert os.path.isfile(weight_file), "ERROR: fail to locate the pretrained weight file"

