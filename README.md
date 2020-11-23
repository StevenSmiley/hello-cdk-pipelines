# CDK Pipelines Template

This template creates a deployment pipeline and empty project using AWS CDK. Once the pipeline has been configured and deployed, it will deploy the app and any changes. This allows you to start using CDK with CI/CD capability built-in from the start.

## Getting started

### Configure the pipeline stack

Change the pipeline stack to your source repository and create any resources necessary for access. This example stores a GitHub access token in AWS Secrets Manager as a plaintext secret.

### Bootstrap the target environment

CDK needs to set up initial resources and permissions to operate in each account it will deploy to.

```
$ export CDK_NEW_BOOTSTRAP=1 # CDK Pipelines requires the 'new/modern' bootstrap templates
$ cdk bootstrap 123456789012/us-west-2 --profile smiley-cdk # Repeat this for every target account
```

Deploy the pipeline stack. Note that the pipeline deploys all other stacks, so you never deploy them manually from your local machine.

```
$ cdk deploy --profile smiley-cdk
```

### Working on your local machine

This project uses Python 3 and virtualenv. If needed, you can create the virtualenv:

```

$ python3 -m venv .venv # Manually create a virtualenv
$ source .venv/bin/activate # Activate the virtualenv
$ pip install -r requirements.txt # Install required dependencies
$ cdk synth # Synthesize the app into CloudFormation
$ pytest # Run unit tests

```

To add additional dependencies, for example other CDK libraries, add to the requirements.txt file and rerun `pip install -r requirements.txt`

### CDK commands

- `cdk synth` emits the synthesized CloudFormation template
- `cdk docs` open CDK documentation
