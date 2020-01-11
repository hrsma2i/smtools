# chainer-sagemaker-tools

This repository is a collection of tools to run SageMaker jobs.

It contains

- CLIs : Some command line tools to use SageMaker easily. See below guidelines.
- ~~[`sage_extensions`](./sage_extensions) : Some Extensions for Chainer Trainer.~~ → Use `smtools.extensions`, but keep this package to reflect the original repository's update.
- [`smtools`](./smtools) : Utilities and Chainer extensions modified by hrsma2i.

# Table of contents

- [Installation](#Installation)
- [Run SageMaker training jobs](#Run-SageMaker-training-jobs)
- [Deploy trained model](#Deploy-trained-model)
- [Run batch inference](#Run-batch-inference)

# Installation

```bash
$ git clone https://github.com/tn1031/chainer-sagemaker-tools.git
$ cd chainer-sagemaker-tools
$ pip install .
```

When installing to the ML instances, since installing to them is based on the contents of `requirements.txt` , it is necessary to contain the below line on `requirements.txt`.

```
git+https://github.com/tn1031/chainer-sagemaker-tools.git
```

Then put the file in the `source_dir` .

# Run SageMaker training jobs

`smtrain` is a command line tool to run SageMaker training jobs.

### Usage

```bash
$ smtrain {path_to_setting} [-j {job_name} -p {aws_profile_name} -l]
```

- `path_to_setting` - Path to the setting file. The format of this file is described in [here](examples/train.yml).
- `job_name` - Training job name. It must be unique in the same AWS account. Its default is `{setting_name}-{unixtime}`.
- `aws_profile_name` - The name of profile that are stored in `~/.aws/config` . You can also designate this from the setting file with the key `profile_name`.
- `-l`, `--local`: Excute the entry point on the local machine for efficient debugging.

# Deploy trained model

`smdeploy` is a command line tool to deploy.

### Usage

```bash
$ smdeploy <endpoint_name> <path_to_setting> [-p <aws_profile_name>]
```

- `endpoint_name` - Endpoint name.
- `path_to_setting` - Path to the setting file. The format of this file is described in [here](https://github.com/tn1031/chainer-sagemaker-tools/blob/master/examples/deploy.yml).
- `aws_profile_name` - The name of profile that are stored in `~/.aws/config` .

# Run batch inference

`smbatch` is a command line tool to run batch inference.

### Usage

```bash
$ smbatch <model_name> <path_to_setting> [-p <aws_profile_name>]
```

- `model_name` - Model name which used for inference.
- `path_to_setting` - Path to the setting file. The format of this file is described in [here](https://github.com/tn1031/chainer-sagemaker-tools/blob/master/examples/batch.yml).
- `aws_profile_name` - The name of profile that are stored in `~/.aws/config` .
