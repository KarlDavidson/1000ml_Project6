pip install xgboost==1.0.2

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier as XGBc
import pandas as pd
import pickle

reduced_num_cols = ['wrong_fragment','hot','num_failed_logins','num_compromised','num_root',
                    'count','num_file_creations','num_shells', 'num_access_files','srv_count',
                    'serror_rate','srv_serror_rate','dst_host_count','dst_host_srv_count',
                    'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
                    'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
                    'dst_host_rerror_rate','dst_host_srv_rerror_rate']

reduced_cat_cols = ['protocol_type = tcp','protocol_type = icmp','service = domain_u',
                    'service = http','service = smtp','service = ftp_data','service = ftp',
                    'service = other','service = ecr_i','service = telnet','service = tim_i',
                    'service = uucp','service = courier','service = private','flag = SF',
                    'flag = REJ','flag = SH','logged_in','is_host_login','is_guest_login','root_shell']

target=['target']

transformed_cols = reduced_num_cols+reduced_cat_cols

# Insert file path here
path = '' # Insert file path within quotes

# Load the model, make sure the file is within the path specified
model_filename = 'finalized_model.sav'
data_filename = 'insert file name here.csv'
data = pd.read_csv(data_filename)
loaded_model = pickle.load(open(path+model_filename, 'rb'))

result = pd.DataFrame(loaded_model.predict(data), columns=['Result'])

data_result = pd.concat(data,result,axis=1)
pd.to_csv('predictions.csv',data_result)