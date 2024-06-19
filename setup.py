from setuptools import setup, find_packages

setup(
    name='transaction_risk_model',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==1.4.2',
        'numpy==1.23.1',
        'scikit-learn==1.0.2',
        'xgboost==1.6.1',
        'catboost==1.1.1',
        'lightgbm==3.3.2',
        'tensorflow==2.8.0',
        'scipy==1.8.1',
        'pyyaml==6.0',
        'pyarrow==7.0.0',
        'pyod==1.0.3'
    ],
    python_requires='>=3.7'
)
