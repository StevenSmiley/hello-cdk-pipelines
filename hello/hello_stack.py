from aws_cdk import (
    core as cdk,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as sns_subs,
)


class HelloStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Stack resource defined here
        queue = sqs.Queue(
            self, "ExampleQueue",
            visibility_timeout=cdk.Duration.seconds(300),
        )

        topic = sns.Topic(self, "ExampleTopic")
        topic.add_subscription(sns_subs.SqsSubscription(queue))
