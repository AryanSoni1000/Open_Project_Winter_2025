import numpy as np

def load_dataset(path):
    """
    Load dataset from .npy or .npz file.

    Parameters:
        path (str): Path to dataset file

    Returns:
        numpy array or dict: Loaded dataset
    """
    try:
        data = np.load(path, allow_pickle=True)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
