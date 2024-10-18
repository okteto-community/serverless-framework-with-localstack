# Running Serverless Framework with LocalStack

1. Install [Serverless Framework](https://www.serverless.com/framework/docs/getting-started#installation) and [LocalStack](https://docs.localstack.cloud/getting-started/installation/)
2. Install the [Serverless-LocalStack plugin](https://docs.localstack.cloud/user-guide/integrations/serverless-framework/#install-and-configure-serverless-localstack-plugin)
3. Run LocalStack: `localstart start`
4. To deploy to LocalStack run: `serverless deploy --stage local`
5. To deploy to AWS run: `serverless deploy`
