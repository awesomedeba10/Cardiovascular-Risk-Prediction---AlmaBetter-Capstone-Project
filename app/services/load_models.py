import pickle, os
import numpy as np
from app import app

class LoadModel:
    """
    Loads the model from the pickle file and predicts the data
    """
    def __init__(self):
        self.model_base_dir = app.config.get('MODEL_DIR')
        self.model_dict = {
            '0': {
                'name': 'Random Forest (Oversampled)',
                'file': 'os_rf_model_over_sampled.pickle'
            },
            '1': {
                'name': 'KNN (Oversampled)',
                'file': 'os_knn_model_over_sampled.pickle'
            },
            '2': {
                'name': 'Decision Tree (Oversampled)',
                'file': 'os_tree_model_over_sampled.pickle'
            },
            '3': {
                'name': 'Logistic Regression (Oversampled)',
                'file': 'os_log_model_over_sampled.pickle'
            },
            '4': {
                'name': 'Linear SVC (Oversampled)',
                'file': 'os_svc_model_over_sampled.pickle'
            },
            '5': {
                'name': 'Bernoulli Naive Bayes (Oversampled)',
                'file': 'os_bnb_model_over_sampled.pickle'
            },
            '6': {
                'name': 'Random Forest (Default)',
                'file': 'rf_model_default_sampled.pickle'
            },
            '7': {
                'name': 'Decision Tree (Default)',
                'file': 'tree_model_default_sampled.pickle'
            },
            '8': {
                'name': 'Logistic Regression (Default)',
                'file': 'log_model_default_sampled.pickle'
            },
            '9': {
                'name': 'Bernoulli Naive Bayes (Default)',
                'file': 'bnb_model_default_sampled.pickle'
            },
            '10': {
                'name': 'Linear SVC (Default)',
                'file': 'svc_model_default_sampled.pickle'
            },
            '11': {
                'name': 'KNN (Default)',
                'file': 'knn_model_default_sampled.pickle'
            }
        }

    def predict(self, data):
        """Load the model, prepare the data and predict the data

        Args:
            data (dict): data to predict

        Returns:
            result (dict): result of the model
        """
        model = self.__load_model(data['model'])
        data = self.__feed_data(data)

        result = {}
        result['prediction'] = str(model.predict(data)[0])
        result['target_label'] = self.__get_target_label(result['prediction'])
        try:
            result['probability'] = 'Confidence Score ' + str(np.max(model.predict_proba(data)[0]))
        except:
            result['probability'] = 'Decision Function Score ' + str(model.decision_function(data)[0])

        return result

    def __load_model(self, model_id: int):
        """Load a model from pickle file using the model id

        Args:
            model_id (int): model id to get value from model_dict

        Returns:
            model (object): model object
        """
        model_file = self.model_dict.get(model_id, '0')['file']
        model_path = os.path.join(self.model_base_dir, model_file)
        return self.__load_pickle(model_path)

    def __feed_data(self, data) -> np.ndarray:
        """Prepare data for the model prediction
           Order of the attributes is as follows: 
                'diaBP', 'glucose', 'totChol', 'age', 'cigsPerDay', 'sysBP'

        Args:
            data (dict): data to feed to the model

        Returns:
            data (np.ndarray): data to feed to the model
        """
        return np.array([
            data['dia_bp'],
            data['glucose'],
            data['tot_chol'],
            data['age'],
            data['cigsPerDay'],
            data['sys_bp']
        ]).reshape(1, -1)

    def __load_pickle(self, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def __get_target_label(self, prediction: int) -> str:
        """Get the target label from the prediction

        Args:
            prediction (int): prediction from the model

        Returns:
            target_label (str): target label
        """
        return 'Risk of CHD' if prediction == '1' else 'Out of Risk'
