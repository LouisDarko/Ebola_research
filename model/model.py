import os
os.chdir('../')

import DeepPurpose.property_pred as models
from DeepPurpose import utils, models, dataset, property_pred
from DeepPurpose.utils import *
from DeepPurpose.dataset import *

from sklearn.metrics import mean_squared_error, roc_auc_score, average_precision_score, f1_score

# Loading of dataset
train = pd.read_csv('/Users/louis/Desktop/Ebola_research/data/antiebola_train.csv')
val = pd.read_csv('/Users/louis/Desktop/Ebola_research/data/antiebola_val.csv')
test = pd.read_csv('/Users/louis/Desktop/Ebola_research/data/antiebola_test.csv')
    
    
    

X_train = train.smiles.values
y_train = train.activity.values
X_val = val.smiles.values
y_val = val.activity.values
X_test = test.smiles.values
y_test = test.activity.values


# Processing of Dataset
drug_encoding = 'CNN'

train = data_process(X_drug = X_train, y = y_train, drug_encoding = drug_encoding,split_method='no_split', 
                                        random_seed = 1)

val = data_process(X_drug = X_val, y = y_val, drug_encoding = drug_encoding,split_method='no_split', 
                                        random_seed = 1)

test = data_process(X_drug = X_test, y = y_test, drug_encoding = drug_encoding,split_method='no_split', 
                                        random_seed = 1)
# Model initialization
config = generate_config(drug_encoding = drug_encoding, 
                         cls_hidden_dims = [1024], 
                         train_epoch = 100, 
                         LR = 0.0001, 
                         batch_size = 16,
                         cnn_drug_filters = [16,96,1024],
                        cnn_drug_kernels = [16,32,54], 
                        )

model = property_pred.model_initialize(**config)
model
    
 # Training of model   
 model.train(train, val, test)

 # Saving model
 model.save_model('/Users/louis/Desktop/Ebola_research/result/model')

 # Importing the save model and the property predction parameters

 from DeepPurpose import property_pred

 model = property_pred.model_pretrained('/Users/louis/Desktop/Ebola_research/result/model')

 drug_smiles, drug_names = read_file_repurposing_library('/Users/louis/Desktop/Ebola_research/data/for_antiebola_drugs.txt')

# Anti-Ebola activity prediction using the trained model
pred = property_pred.repurpose(drug_smiles, model, drug_names, result_folder = "/Users/louis/Desktop/Ebola_research/result/", convert_y = False)