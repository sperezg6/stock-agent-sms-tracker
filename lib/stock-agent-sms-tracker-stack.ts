import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as path from 'path';

export interface StockAgentSmsTrackerStackProps extends cdk.StackProps {
  twilioAccountSid?: string;
  twilioAuthToken?: string;
  toPhoneNumber?: string;
  fromPhoneNumber?: string;
  finnhubApiKey?: string;
  openaiApiKey?: string;

}

export class StockAgentSmsTrackerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: StockAgentSmsTrackerStackProps) {
    super(scope, id, props);

    // Create Lambda Layer for dependencies
    const dependenciesLayer = new lambda.LayerVersion(this, 'DependenciesLayer', {
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda'), {
        bundling: {
          image: lambda.Runtime.PYTHON_3_11.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r requirements.txt -t /asset-output/python && cp -r . /asset-output/'
          ],
        },
      }),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_11],
      description: 'Dependencies for Stock Agent SMS Tracker',
    });
    

    // StockAgentSmsTrackerStack Lambda Function
    const stockAgentSmsTrackerFunction = new lambda.Function(this, 'StockAgentSmsTrackerFunction', {
      functionName: 'stock-agent-tracks-lambda',
      runtime: lambda.Runtime.PYTHON_3_11,
      code: lambda.Code.fromAsset(path.join(__dirname, '../lambda')),
      layers: [dependenciesLayer],
      handler: 'main.handler',
      memorySize: 256,
      timeout: cdk.Duration.seconds(600),
      environment: {
        ACCOUNT_SID: props?.twilioAccountSid || this.node.tryGetContext('twilioAccountSid') || '',
        AUTH_TOKEN: props?.twilioAuthToken || this.node.tryGetContext('twilioAuthToken') || '',
        TO_PHONE_NUMBER: props?.toPhoneNumber || this.node.tryGetContext('toPhoneNumber') || '',
        FROM_PHONE_NUMBER: props?.fromPhoneNumber || this.node.tryGetContext('fromPhoneNumber') || '',
        FINNHUB_API_KEY: props?.finnhubApiKey || this.node.tryGetContext('finnhubApiKey') || '',
        OPENAI_API_KEY: props?.openaiApiKey || this.node.tryGetContext('openaiApiKey') || '',
      },
      description: 'A Lambda function to track stock prices and send SMS alerts.',
    });

    // Add Tags to the Lambda function
    cdk.Tags.of(stockAgentSmsTrackerFunction).add('Project', 'StockAgentSmsTracker');
    cdk.Tags.of(stockAgentSmsTrackerFunction).add('Owner', 'Santiago Perez Gutierrez');
    cdk.Tags.of(stockAgentSmsTrackerFunction).add('Environment', 'Production');

    // Create EventBridge rule for weekdays at 8 AM
    const weekdayRule = new events.Rule(this, 'WeekdayMorningRule', {
      ruleName: 'stock-agent-weekday-8am-rule',
      description: 'Trigger stock agent Lambda every weekday at 8 AM',
      schedule: events.Schedule.expression('cron(0 8 ? * MON-FRI *)'),
    });

     // Add Lambda as target for the EventBridge rule
    weekdayRule.addTarget(new targets.LambdaFunction(stockAgentSmsTrackerFunction, {
      retryAttempts: 2,
      maxEventAge: cdk.Duration.hours(2)
    }));


  }
}
