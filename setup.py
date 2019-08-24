from setuptools import setup

setup(
    author="tn1031",
    author_email="ttt.nakamura1031@gmail.com",
    name="smtools",
    description="Some extensions and tools to run Chainer jobs on Amazon SageMaker",
    version="0.1.8.4",
    packages=["sagemaker_tools", "sage_extensions", "smtools"],
    install_requires=["boto3", "pyyaml<4.3,>=4.2b1", "sagemaker", "slackweb"],
    entry_points={
        "console_scripts": [
            "smtrain=sagemaker_tools.exec_train:main",
            "smdeploy=sagemaker_tools.deploy_endpoint:main",
            "smbatch=sagemaker_tools.batch_inference:main",
            "mgconf=sagemaker_tools.merge_configs:main",
        ]
    },
    license="MIT license",
)
